#!/usr/bin/env python3
"""Re-key chunk metadata (title/org/year/section/subsection/license) from
the canonical master CSV by joining on URL.

The harvest log had column drift for some buckets (curricula 7-col schema),
producing chunks with title='B10' etc. This script fixes the chunks.jsonl
in place by looking up the URL in the master CSV.
"""
import csv
import json
from pathlib import Path

ROOT = Path("/home/user/workspace/joint_fires_corpus")
MASTER = Path("/home/user/workspace/joint_fires_research/joint_fires_master_sources.csv")
CHUNKS = ROOT / "chunks" / "chunks.jsonl"

# Build URL -> canonical metadata
url2meta = {}
with open(MASTER) as f:
    for r in csv.DictReader(f):
        url = (r.get("url") or "").strip()
        # Some URLs appear inside a markdown link in the "year" column due to
        # the curricula CSV having 7 cols vs platforms 8 cols. Try to recover.
        if not url:
            for fld in ("year", "authors"):
                v = r.get(fld) or ""
                if "http" in v:
                    # extract first http... up to ) or whitespace
                    import re
                    m = re.search(r"https?://[^\s)\]]+", v)
                    if m:
                        url = m.group(0)
                        break
        if not url:
            continue
        if url in url2meta:
            continue
        url2meta[url] = {
            "title": (r.get("title") or "").strip(),
            "org": (r.get("org") or "").strip(),
            "year": (r.get("year") or "").strip(),
            "section": (r.get("section") or "").strip(),
            "subsection": (r.get("subsection") or "").strip(),
            "license": (r.get("license") or "").strip(),
        }

# Strip markdown link syntax from year/license fields if present
import re
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
for u, m in url2meta.items():
    if "[" in m["year"]:
        m["year"] = LINK_RE.sub(r"\1", m["year"]).strip()
    # If year still looks like an org/affiliation, try to extract a year
    yr = m["year"]
    yr_match = re.search(r"\b(19|20)\d{2}\b", yr)
    if yr_match and len(yr) > 8:
        # Keep both: just the year is more useful
        m["year_display"] = yr
        m["year"] = yr_match.group(0)
    else:
        m["year_display"] = yr

print(f"Loaded {len(url2meta)} URL->metadata entries from master CSV")

# Rewrite chunks.jsonl
n_total = 0
n_fixed = 0
n_no_match = 0
out_lines = []
with open(CHUNKS) as f:
    for line in f:
        rec = json.loads(line)
        n_total += 1
        url = rec.get("source_url", "")
        m = url2meta.get(url)
        if m:
            if rec.get("title") != m["title"]:
                n_fixed += 1
            rec["title"] = m["title"]
            rec["org"] = m["org"]
            rec["year"] = m["year_display"] or m["year"]
            rec["section"] = m["section"]
            rec["subsection"] = m["subsection"]
            if m.get("license"):
                rec["license"] = m["license"]
        else:
            n_no_match += 1
        # Update the inline header at top of chunk_idx=0 chunks too
        out_lines.append(json.dumps(rec, ensure_ascii=False) + "\n")

CHUNKS.write_text("".join(out_lines))
print(f"Total chunks: {n_total}")
print(f"Title-fixed:  {n_fixed}")
print(f"No URL match: {n_no_match}")
