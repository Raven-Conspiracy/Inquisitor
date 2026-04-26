"""
Joint Fires Corpus harvester.

Reads /home/user/workspace/joint_fires_research/joint_fires_master_sources.csv
(filtered to include == 'Y') and downloads / extracts text for each source.

Output layout under /home/user/workspace/joint_fires_corpus/:
  raw/<bucket>/<slug>.{pdf,html,txt}        # raw bytes
  extracted/<bucket>/<slug>.txt              # cleaned plain text ready for chunking
  manifest/download_log.csv                  # per-source result log
  manifest/failed.csv                        # failures only
"""
from __future__ import annotations
import csv
import hashlib
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse, unquote
import concurrent.futures as cf
import requests

ROOT = Path("/home/user/workspace/joint_fires_corpus")
CSV_IN = Path("/home/user/workspace/joint_fires_research/joint_fires_master_sources.csv")

# Two UA profiles: bot UA for Wikipedia (preferred there), browser UA for mil/.gov hosts that block bots
UA_BOT = "JointFiresCorpusBot/1.0 (research/educational; contact: omnissiahcypher@github)"
UA_BROWSER = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
HEADERS = {"User-Agent": UA_BOT, "Accept": "*/*"}
BROWSER_HEADERS = {
    "User-Agent": UA_BROWSER,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

BROWSER_HOSTS = {
    "www.doctrine.af.mil", "doctrine.af.mil",
    "www.marines.mil", "marines.mil",
    "www.usni.org", "usni.org",
    "www.mynavyhr.navy.mil", "mynavyhr.navy.mil",
    "www.nwdc.usff.navy.mil", "nwdc.usff.navy.mil",
    "www.esd.whs.mil", "esd.whs.mil",
    "armypubs.army.mil",
    "www.armypubs.army.mil",
    "home.army.mil",
    "www.airuniversity.af.edu",
    "airuniversity.af.edu",
    "www.uscc.gov",
    "uscc.gov",
    "media.defense.gov",
    "www.defense.gov",
    "www.dia.mil", "dia.mil",
    "www.oni.navy.mil", "oni.navy.mil",
    "www.nasic.af.mil", "nasic.af.mil",
    "crsreports.congress.gov",
    "www.kongsberg.com",
}

def _headers_for(url: str) -> dict:
    host = urlparse(url).netloc.lower()
    if host in BROWSER_HOSTS or host.endswith(".mil") or host.endswith(".gov"):
        return BROWSER_HEADERS
    return HEADERS
TIMEOUT = 60
MAX_BYTES = 200 * 1024 * 1024  # 200 MB hard cap per file

# Wikipedia API: use clean plaintext extract
WIKI_API = "https://en.wikipedia.org/w/api.php"

# Per-host throttling: minimum delay between requests to the same host
import threading
from collections import defaultdict
_HOST_LOCKS = defaultdict(threading.Lock)
_LAST_REQ = defaultdict(float)
_HOST_DELAY = {
    "en.wikipedia.org": 2.0,   # be very polite to wikipedia API
    "default": 0.25,
}

def _throttle(host: str):
    delay = _HOST_DELAY.get(host, _HOST_DELAY["default"])
    with _HOST_LOCKS[host]:
        elapsed = time.monotonic() - _LAST_REQ[host]
        if elapsed < delay:
            time.sleep(delay - elapsed)
        _LAST_REQ[host] = time.monotonic()


def _request_with_retry(method: str, url: str, **kwargs):
    host = urlparse(url).netloc
    last_exc = None
    for attempt in range(5):
        _throttle(host)
        try:
            r = requests.request(method, url, **kwargs)
            if r.status_code == 429:
                # exponential backoff with jitter
                ra = r.headers.get("Retry-After")
                wait = float(ra) if ra and ra.isdigit() else (2 ** attempt) + 0.5
                time.sleep(min(wait, 30))
                continue
            if r.status_code in (500, 502, 503, 504):
                time.sleep((2 ** attempt) + 0.5)
                continue
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            last_exc = e
            time.sleep((2 ** attempt) + 0.3)
    if last_exc:
        raise last_exc
    raise RuntimeError(f"failed after retries: {url}")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:140] or "untitled"


def url_kind(url: str) -> str:
    """Classify a URL: wikipedia | pdf | html | unknown."""
    if not url:
        return "unknown"
    p = urlparse(url)
    host = p.netloc.lower()
    path = p.path.lower()
    if "wikipedia.org" in host:
        return "wikipedia"
    if path.endswith(".pdf") or "PDF" in url or "/pdf/" in path:
        return "pdf"
    if "crsreports.congress.gov/product/pdf" in url:
        return "pdf"
    return "html"


def wiki_title_from_url(url: str) -> str | None:
    p = urlparse(url)
    if "wikipedia.org" not in p.netloc:
        return None
    parts = p.path.split("/wiki/", 1)
    if len(parts) != 2:
        return None
    return unquote(parts[1])


def _wiki_search_title(query: str) -> str | None:
    """Search Wikipedia for a query string and return the best matching page title."""
    params = {
        "action": "query", "format": "json", "list": "search",
        "srsearch": query, "srlimit": 1,
    }
    try:
        r = _request_with_retry("GET", WIKI_API, params=params, headers=HEADERS, timeout=TIMEOUT)
        j = r.json()
        hits = j.get("query", {}).get("search", [])
        if hits:
            return hits[0]["title"]
    except Exception:
        pass
    return None


def _wiki_extract(title: str) -> str | None:
    params = {
        "action": "query", "format": "json", "titles": title,
        "prop": "extracts", "explaintext": 1, "redirects": 1,
    }
    r = _request_with_retry("GET", WIKI_API, params=params, headers=HEADERS, timeout=TIMEOUT)
    j = r.json()
    pages = j.get("query", {}).get("pages", {})
    for pid, page in pages.items():
        if pid == "-1":
            return None
        return page.get("extract", "") or ""
    return None


def fetch_wikipedia(url: str, fallback_query: str | None = None) -> tuple[str, str] | None:
    """Return (raw_html, plaintext) using MediaWiki API. Falls back to search if direct title misses or returns stub."""
    MIN_LEN = 500  # treat anything shorter than 500 chars as missing/stub
    title = wiki_title_from_url(url)
    best_text = ""
    best_meta = ""
    if title:
        text = _wiki_extract(title) or ""
        if len(text) > len(best_text):
            best_text, best_meta = text, f"direct_title: {title}"
    if len(best_text) < MIN_LEN and fallback_query:
        found = _wiki_search_title(fallback_query)
        if found:
            text = _wiki_extract(found) or ""
            if len(text) > len(best_text):
                best_text, best_meta = text, f"resolved_via_search: {found}"
    if len(best_text) >= 200:  # accept anything reasonable
        return (best_meta, best_text)
    return None


def fetch_binary(url: str) -> tuple[bytes, str] | None:
    """Return (bytes, content_type) for any URL. Streams with size cap."""
    host = urlparse(url).netloc
    headers = _headers_for(url)
    last_exc = None
    for attempt in range(5):
        _throttle(host)
        try:
            with requests.get(url, headers=headers, stream=True, timeout=TIMEOUT, allow_redirects=True) as r:
                if r.status_code == 429:
                    time.sleep((2 ** attempt) + 0.5)
                    continue
                if r.status_code in (500, 502, 503, 504):
                    time.sleep((2 ** attempt) + 0.5)
                    continue
                r.raise_for_status()
                ct = r.headers.get("Content-Type", "").lower()
                buf = bytearray()
                for chunk in r.iter_content(64 * 1024):
                    if not chunk:
                        continue
                    buf.extend(chunk)
                    if len(buf) > MAX_BYTES:
                        raise ValueError(f"size cap exceeded ({MAX_BYTES} bytes)")
                return (bytes(buf), ct)
        except requests.exceptions.RequestException as e:
            last_exc = e
            time.sleep((2 ** attempt) + 0.3)
    if last_exc:
        raise last_exc
    raise RuntimeError(f"failed after retries: {url}")


def extract_pdf_text(pdf_bytes: bytes) -> str:
    """Extract text from PDF bytes. Tries pypdf then pdfminer.six fallback."""
    try:
        import pypdf
        from io import BytesIO
        reader = pypdf.PdfReader(BytesIO(pdf_bytes))
        parts = []
        for page in reader.pages:
            try:
                parts.append(page.extract_text() or "")
            except Exception:
                continue
        return "\n\n".join(parts)
    except Exception:
        pass
    try:
        from pdfminer.high_level import extract_text
        from io import BytesIO
        return extract_text(BytesIO(pdf_bytes)) or ""
    except Exception as e:
        return f"[PDF EXTRACTION FAILED: {e}]"


def extract_html_text(html_bytes: bytes) -> str:
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_bytes, "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer", "noscript"]):
            tag.decompose()
        text = soup.get_text("\n", strip=True)
        # Collapse 3+ newlines
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text
    except Exception as e:
        return f"[HTML EXTRACTION FAILED: {e}]"


def harvest_one(row: dict) -> dict:
    """Return result dict for the download log."""
    url = row["url"].strip()
    bucket = row["bucket"].strip()
    title = row["title"].strip()
    if not url:
        return {**row, "status": "skip_no_url", "raw_path": "", "extracted_path": "", "bytes": 0, "chars": 0, "error": "no URL"}

    slug = slugify(title)
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    base = f"{slug}-{h}"

    raw_dir = ROOT / "raw" / bucket
    ext_dir = ROOT / "extracted" / bucket
    raw_dir.mkdir(parents=True, exist_ok=True)
    ext_dir.mkdir(parents=True, exist_ok=True)

    kind = url_kind(url)

    try:
        if kind == "wikipedia":
            res = fetch_wikipedia(url, fallback_query=title)
            if not res:
                raise ValueError("wiki extract failed")
            _, text = res
            raw_path = raw_dir / f"{base}.txt"
            ext_path = ext_dir / f"{base}.txt"
            raw_path.write_text(text, encoding="utf-8")
            ext_path.write_text(text, encoding="utf-8")
            return {**row, "status": "ok", "raw_path": str(raw_path), "extracted_path": str(ext_path),
                    "bytes": len(text.encode('utf-8')), "chars": len(text), "error": ""}
        else:
            data, ct = fetch_binary(url)
            if "pdf" in ct or kind == "pdf":
                raw_path = raw_dir / f"{base}.pdf"
                raw_path.write_bytes(data)
                text = extract_pdf_text(data)
            elif "html" in ct or "xml" in ct:
                raw_path = raw_dir / f"{base}.html"
                raw_path.write_bytes(data)
                text = extract_html_text(data)
            else:
                # unknown; save and try html extract
                raw_path = raw_dir / f"{base}.bin"
                raw_path.write_bytes(data)
                text = extract_html_text(data)
            ext_path = ext_dir / f"{base}.txt"
            ext_path.write_text(text, encoding="utf-8")
            return {**row, "status": "ok", "raw_path": str(raw_path), "extracted_path": str(ext_path),
                    "bytes": len(data), "chars": len(text), "error": ""}
    except Exception as e:
        return {**row, "status": "fail", "raw_path": "", "extracted_path": "", "bytes": 0, "chars": 0,
                "error": str(e)[:300]}


def main(filter_buckets: list[str] | None = None, max_workers: int = 8, limit: int | None = None,
         retry_failed: bool = False, skip_existing: bool = True):
    rows = []
    log_path = ROOT / "manifest" / "download_log.csv"
    already_ok = set()
    if skip_existing and log_path.exists():
        with log_path.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("status") == "ok":
                    already_ok.add(r.get("url", ""))
    with CSV_IN.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r.get("include", "Y").upper() != "Y":
                continue
            if filter_buckets and r["bucket"] not in filter_buckets:
                continue
            if not r.get("url"):
                continue
            if skip_existing and r["url"] in already_ok:
                continue
            rows.append(r)
    if limit:
        rows = rows[:limit]

    print(f"Harvesting {len(rows)} sources with {max_workers} workers...")
    results = []
    log_path = ROOT / "manifest" / "download_log.csv"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    completed = 0
    with cf.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(harvest_one, r): r for r in rows}
        for fut in cf.as_completed(futures):
            res = fut.result()
            results.append(res)
            completed += 1
            status = res["status"]
            print(f"  [{completed}/{len(rows)}] {status:5s} {res['bucket']:28s} {res['title'][:60]}")
            if res["status"] == "fail":
                print(f"      ERROR: {res['error']}")

    # Append (or write) results
    fields = list(results[0].keys()) if results else []
    write_header = not log_path.exists()
    mode = "a" if log_path.exists() else "w"
    with log_path.open(mode, newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            w.writeheader()
        w.writerows(results)

    failed = [r for r in results if r["status"] == "fail"]
    fail_path = ROOT / "manifest" / "failed.csv"
    if failed:
        with fail_path.open("a" if fail_path.exists() else "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            if not fail_path.exists() or fail_path.stat().st_size == 0:
                w.writeheader()
            w.writerows(failed)

    ok = sum(1 for r in results if r["status"] == "ok")
    total_chars = sum(r["chars"] for r in results)
    print()
    print(f"Done. {ok}/{len(results)} successful. Total extracted text: {total_chars/1_000_000:.2f} MB chars.")
    if failed:
        print(f"Failed: {len(failed)} (see manifest/failed.csv)")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--buckets", nargs="*", default=None, help="filter to these bucket names")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()
    main(filter_buckets=args.buckets, max_workers=args.workers, limit=args.limit)
