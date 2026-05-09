"""
Retry pass for Inquisitor harvest failures.

Strategy:
1. First attempt: stronger HTTP spoofing (full Chrome-like header set, cookies, retries)
   — recovers most Akamai/Cloudflare hosts without needing fetch_url
2. Tracks which URLs need a third pass via fetch_url (the heavy bypass)

Reads:    manifest/failed_urls.json
Outputs:  extracted/<bucket>/<slug>.txt (on success)
          manifest/retry_pass_log.csv
          manifest/still_failed.json (for fetch_url third pass)
"""
import csv
import hashlib
import json
import re
import time
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse
import concurrent.futures as cf
import threading
from collections import defaultdict
import requests
import pypdf
from bs4 import BeautifulSoup

ROOT = Path("/home/user/workspace/inquisitor_corpus")
FAILED_JSON = ROOT / "manifest" / "failed_urls.json"
LOG_OUT = ROOT / "manifest" / "retry_pass_log.csv"
STILL_FAILED = ROOT / "manifest" / "still_failed.json"

# Strong Chrome 124 spoofing
HEADERS_CHROME = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "DNT": "1",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": '"Google Chrome";v="124", "Chromium";v="124", "Not.A/Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

TIMEOUT = 90
MAX_BYTES = 200 * 1024 * 1024

# Per-host throttling
_HOST_LOCKS = defaultdict(threading.Lock)
_LAST_REQ = defaultdict(float)
_HOST_DELAY = defaultdict(lambda: 1.5)
_HOST_DELAY.update({
    "www.aspi.org.au": 3.0,
    "www.dni.gov": 2.0,
    "fas.org": 2.0,
    "www.dia.mil": 3.0,
    "media.defense.gov": 3.0,
    "csbaonline.org": 2.5,
    "www.start.umd.edu": 2.5,
    "www.38north.org": 2.0,
    "www.armyupress.army.mil": 2.5,
    "crsreports.congress.gov": 3.0,
    "www.iiss.org": 2.0,
})


def slugify(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s[:140] or "untitled"


def throttled_get(url: str, session: requests.Session) -> requests.Response:
    host = urlparse(url).netloc.lower()
    delay = _HOST_DELAY[host]
    with _HOST_LOCKS[host]:
        elapsed = time.time() - _LAST_REQ[host]
        if elapsed < delay:
            time.sleep(delay - elapsed)
        _LAST_REQ[host] = time.time()
    # Add Referer like a real browser navigation
    referer = f"https://{host}/"
    headers = {**HEADERS_CHROME, "Referer": referer}
    return session.get(url, headers=headers, timeout=TIMEOUT, stream=True, allow_redirects=True)


def fetch_with_session(url: str) -> tuple[bytes, str]:
    """Use a session that may capture cookies from a homepage GET first."""
    host = urlparse(url).netloc
    s = requests.Session()
    # Warm up: hit the homepage first to grab any session cookies / Akamai tokens
    try:
        s.get(f"https://{host}/", headers=HEADERS_CHROME, timeout=30, allow_redirects=True)
        time.sleep(0.5)
    except Exception:
        pass
    # Now fetch the target
    r = throttled_get(url, s)
    r.raise_for_status()
    ct = r.headers.get("Content-Type", "").lower()
    chunks = []
    n = 0
    for chunk in r.iter_content(64 * 1024):
        if not chunk:
            continue
        chunks.append(chunk)
        n += len(chunk)
        if n > MAX_BYTES:
            break
    return b"".join(chunks), ct


def extract_pdf(b: bytes) -> str:
    try:
        rdr = pypdf.PdfReader(BytesIO(b))
        return "\n\n".join((p.extract_text() or "") for p in rdr.pages)
    except Exception as e:
        return f"[PDF EXTRACTION FAILED: {e}]"


def extract_html(b: bytes) -> str:
    try:
        soup = BeautifulSoup(b, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        text = soup.get_text("\n")
        # collapse whitespace
        text = re.sub(r"\n\s*\n", "\n\n", text)
        text = re.sub(r"[ \t]+", " ", text)
        return text.strip()
    except Exception as e:
        return f"[HTML EXTRACTION FAILED: {e}]"


def retry_one(item: dict) -> dict:
    url = item["url"]
    bucket = item["bucket"]
    title = item["title"]
    slug = slugify(title)
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    base = f"{slug}-{h}"

    raw_dir = ROOT / "raw" / bucket
    ext_dir = ROOT / "extracted" / bucket
    raw_dir.mkdir(parents=True, exist_ok=True)
    ext_dir.mkdir(parents=True, exist_ok=True)

    try:
        data, ct = fetch_with_session(url)
        if "pdf" in ct or url.lower().endswith(".pdf"):
            raw_path = raw_dir / f"{base}.pdf"
            raw_path.write_bytes(data)
            text = extract_pdf(data)
        elif "html" in ct or "xml" in ct:
            raw_path = raw_dir / f"{base}.html"
            raw_path.write_bytes(data)
            text = extract_html(data)
        else:
            raw_path = raw_dir / f"{base}.bin"
            raw_path.write_bytes(data)
            text = extract_html(data)
        ext_path = ext_dir / f"{base}.txt"
        ext_path.write_text(text, encoding="utf-8")
        return {**item, "status": "ok",
                "raw_path": str(raw_path), "extracted_path": str(ext_path),
                "bytes": len(data), "chars": len(text), "error": ""}
    except Exception as e:
        return {**item, "status": "fail",
                "raw_path": "", "extracted_path": "",
                "bytes": 0, "chars": 0, "error": str(e)[:300]}


def main(max_workers: int = 4):
    items = json.loads(FAILED_JSON.read_text())
    print(f"Retrying {len(items)} failed URLs with strong Chrome spoofing + cookies...")

    results = []
    completed = 0
    with cf.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(retry_one, it): it for it in items}
        for fut in cf.as_completed(futures):
            r = fut.result()
            results.append(r)
            completed += 1
            mark = "OK" if r["status"] == "ok" else "X"
            print(f"  [{completed}/{len(items)}] {mark} {r['bucket']:28s} {r['title'][:60]}")
            if r["status"] == "fail":
                print(f"      ERROR: {r['error'][:200]}")

    # Write log
    fields = list(results[0].keys()) if results else []
    with LOG_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(results)

    # Save still-failed for next pass
    still = [r for r in results if r["status"] == "fail"]
    STILL_FAILED.write_text(json.dumps(still, indent=2))

    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"\n=== RETRY PASS COMPLETE ===")
    print(f"Recovered: {ok}/{len(items)} ({100*ok/len(items):.1f}%)")
    print(f"Still failed: {len(still)} → saved to {STILL_FAILED}")


if __name__ == "__main__":
    main()
