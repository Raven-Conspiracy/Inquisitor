#!/usr/bin/env python3
"""
fetch_url_recovery.py

Recovery script for URLs blocked by Akamai/Cloudflare.
This script documents the recovery process and results for the 50 URLs
in recoverable_via_fetch.json.

The actual fetching was done via agent fetch_url tool calls (not Python HTTP),
since fetch_url bypasses CDN/WAF protections that block standard HTTP clients.

Usage:
    This script can be used to check or update recovery status, but actual
    fetching must be done through the agent's fetch_url tool.
"""

import hashlib
import re
import json
import csv
from pathlib import Path

MANIFEST_PATH = '/home/user/workspace/inquisitor_corpus/manifest/recoverable_via_fetch.json'
LOG_PATH = '/home/user/workspace/inquisitor_corpus/manifest/fetch_url_recovery_log.csv'
EXTRACTED_BASE = '/home/user/workspace/inquisitor_corpus/extracted'


def make_slug(title: str, max_len: int = 140) -> str:
    """Convert title to URL-safe slug."""
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:max_len] or 'untitled'


def make_hash(url: str) -> str:
    """Return first 8 chars of SHA1 hash of URL."""
    return hashlib.sha1(url.encode()).hexdigest()[:8]


def get_extracted_path(url: str, bucket: str, title: str) -> str:
    """Return the expected extraction path for a given item."""
    slug = make_slug(title)
    h = make_hash(url)
    return f'{EXTRACTED_BASE}/{bucket}/{slug}-{h}.txt'


def save_content(url: str, bucket: str, title: str, content: str) -> tuple[str, int]:
    """Save fetched content to extracted path. Returns (path, len)."""
    path = get_extracted_path(url, bucket, title)
    d = Path(path).parent
    d.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(content, encoding='utf-8')
    return path, len(content)


def load_manifest() -> list[dict]:
    """Load the recoverable_via_fetch.json manifest."""
    return json.loads(Path(MANIFEST_PATH).read_text())


def read_log() -> list[dict]:
    """Read the recovery log CSV."""
    if not Path(LOG_PATH).exists():
        return []
    with open(LOG_PATH, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def print_summary():
    """Print a summary of recovery results."""
    rows = read_log()
    if not rows:
        print("No log found.")
        return
    
    ok = [r for r in rows if r['status'] == 'ok']
    fail = [r for r in rows if r['status'] == 'fail']
    
    print(f"Total: {len(rows)}")
    print(f"Recovered (ok): {len(ok)}")
    print(f"Still failed: {len(fail)}")
    print()
    
    for priority in ['P1', 'P2', 'P3']:
        p_ok = sum(1 for r in ok if r['priority'] == priority)
        p_fail = sum(1 for r in fail if r['priority'] == priority)
        p_total = p_ok + p_fail
        print(f"{priority}: {p_ok}/{p_total} recovered")
    
    print()
    print("FAILURES by error type:")
    error_types = {}
    for r in fail:
        err = r.get('error', 'unknown')[:50]
        error_types[err] = error_types.get(err, 0) + 1
    for err, count in sorted(error_types.items(), key=lambda x: -x[1]):
        print(f"  {count:2d}x {err}")


if __name__ == '__main__':
    print_summary()
