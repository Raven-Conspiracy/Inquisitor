"""
Retry failed downloads using the platform's fetch_url tool (which has a real browser TLS stack).

Reads failed URLs from manifest/download_log.csv, prints them as a list.
The actual fetch is done by the agent calling fetch_url for each URL.

This script:
1. Lists all currently-failed URLs (status='fail') with their slugs and buckets
2. After fetch_url calls, the agent can call this script with --consume to read the
   cached fetch_url outputs from tool_calls/fetch_url/, extract content, write to extracted/<bucket>/<slug>.txt,
   and update the manifest log.
"""
import csv
import json
import re
import sys
from pathlib import Path
import hashlib

ROOT = Path("/home/user/workspace/joint_fires_corpus")
LOG = ROOT / "manifest" / "download_log.csv"
TC_DIR = Path("/home/user/workspace/tool_calls/fetch_url")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:140] or "untitled"


def load_log():
    """Return latest-status dict by URL."""
    seen = {}
    with LOG.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            seen[r["url"]] = r
    return seen


def list_failed():
    seen = load_log()
    failed = [r for r in seen.values() if r["status"] == "fail" and r.get("url")]
    print(f"# {len(failed)} failed URLs to retry")
    for r in failed:
        print(json.dumps({
            "url": r["url"],
            "title": r["title"],
            "bucket": r["bucket"],
            "slug": slugify(r["title"]),
        }))


def consume_fetched():
    """Walk tool_calls/fetch_url outputs, match to failed URLs in log,
    and write extracted text + update log."""
    seen = load_log()
    # Index by URL
    failed_by_url = {r["url"]: r for r in seen.values() if r["status"] == "fail"}
    print(f"Looking for {len(failed_by_url)} failed URLs in fetch_url cache...")

    updates = {}  # url -> new row
    matched = 0
    for fp in TC_DIR.glob("output_*.json"):
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        url = data.get("url", "")
        if url not in failed_by_url:
            continue
        # Prefer "content" (full body) over "extracted" (LLM summary)
        text = data.get("content") or data.get("extracted") or ""
        if len(text) < 500:
            continue
        row = failed_by_url[url]
        bucket = row["bucket"]
        slug = slugify(row["title"])
        h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
        ext_dir = ROOT / "extracted" / bucket
        raw_dir = ROOT / "raw" / bucket
        ext_dir.mkdir(parents=True, exist_ok=True)
        raw_dir.mkdir(parents=True, exist_ok=True)
        ext_path = ext_dir / f"{slug}-{h}.txt"
        raw_path = raw_dir / f"{slug}-{h}.txt"
        ext_path.write_text(text, encoding="utf-8")
        raw_path.write_text(text, encoding="utf-8")
        new_row = dict(row)
        new_row["status"] = "ok"
        new_row["raw_path"] = str(raw_path)
        new_row["extracted_path"] = str(ext_path)
        new_row["bytes"] = len(text.encode("utf-8"))
        new_row["chars"] = len(text)
        new_row["error"] = "fetched_via_fetch_url"
        updates[url] = new_row
        matched += 1
        print(f"  ok: {bucket:28s} {row['title'][:60]} ({len(text)} chars)")

    if not updates:
        print("No matches found in fetch_url cache.")
        return

    # Rewrite log: replace fail entries with ok where we have updates
    rows = list(seen.values())
    new_rows = []
    for r in rows:
        if r["url"] in updates and r["status"] == "fail":
            new_rows.append(updates[r["url"]])
        else:
            new_rows.append(r)
    fields = list(rows[0].keys()) if rows else []
    with LOG.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(new_rows)
    print(f"\nUpdated {matched} entries in {LOG}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--consume":
        consume_fetched()
    else:
        list_failed()
