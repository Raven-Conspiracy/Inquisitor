#!/usr/bin/env python3
"""Build the inquisitor_corpus README + manifest from final deduped chunks."""
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path("/home/user/workspace/inquisitor_corpus")
DEDUP = ROOT / "chunks" / "chunks_dedup.jsonl"
DEDUP_REPORT = ROOT / "chunks" / "dedupe_report.json"
RAW_STATS = ROOT / "chunks" / "chunk_stats.json"
LOG_PASS1 = ROOT / "manifest" / "download_log.csv"
LOG_PASS2 = ROOT / "manifest" / "retry_pass_log.csv"
LOG_PASS3 = ROOT / "manifest" / "fetch_url_recovery_log.csv"

OUT_README = ROOT / "README.md"
OUT_MANIFEST = ROOT / "manifest" / "MANIFEST.json"

# --- Compute stats from deduped chunks ---
n_chunks = 0
n_tokens = 0
buckets: Counter = Counter()
bucket_tokens: Counter = Counter()
docs_by_bucket: dict[str, set] = defaultdict(set)
structured_count = 0
prose_count = 0
priority_count: Counter = Counter()
year_count: Counter = Counter()
top_orgs: Counter = Counter()

with open(DEDUP) as f:
    for line in f:
        rec = json.loads(line)
        n_chunks += 1
        n_tokens += rec.get("n_tokens", 0)
        b = rec["bucket"]
        buckets[b] += 1
        bucket_tokens[b] += rec.get("n_tokens", 0)
        docs_by_bucket[b].add(rec["doc_id"])
        if rec.get("is_structured"):
            structured_count += 1
        else:
            prose_count += 1
        if rec.get("priority"):
            priority_count[rec["priority"]] += 1
        if rec.get("year"):
            year_count[rec["year"]] += 1
        if rec.get("org"):
            top_orgs[rec["org"]] += 1

dedup_report = json.load(open(DEDUP_REPORT))
raw_stats = json.load(open(RAW_STATS))

# Acquisition stats from log files
acquired_urls = set()
total_urls = 0
status_counter: Counter = Counter()
with open(LOG_PASS1) as f:
    for r in csv.DictReader(f):
        url = r.get("url", "").strip()
        if not url:
            continue
        total_urls += 1
        if r.get("status") == "ok":
            acquired_urls.add(url)
        status_counter[r.get("status", "")] += 1

# Add pass2/pass3 successes (URL-keyed)
for log in (LOG_PASS2, LOG_PASS3):
    if not log.exists():
        continue
    with open(log) as f:
        for r in csv.DictReader(f):
            url = r.get("url", "").strip()
            if r.get("status") == "ok" and url:
                acquired_urls.add(url)

acquired_count = len(acquired_urls)
acquisition_rate = acquired_count / max(total_urls, 1)

# --- Bucket categorization for the README ---
def categorize(b: str) -> str:
    if "oob" in b:
        return "OOB"
    if b.startswith("inq_ct"):
        return "Counter-Terrorism"
    if "ukr" in b:
        return "Ukraine 2022–2025"
    if "china" in b:
        return "China"
    if "dprk" in b:
        return "DPRK"
    if "iran" in b:
        return "Iran"
    return "Other"

cat_chunks: Counter = Counter()
cat_tokens: Counter = Counter()
cat_docs: defaultdict = defaultdict(set)
for b, n in buckets.items():
    cat = categorize(b)
    cat_chunks[cat] += n
    cat_tokens[cat] += bucket_tokens[b]
    cat_docs[cat].update(docs_by_bucket[b])

# --- Manifest JSON ---
manifest = {
    "corpus_name": "inquisitor_corpus",
    "version": "v2026-05-09",
    "build_date": datetime.utcnow().isoformat() + "Z",
    "purpose": "Intel Support to Targeting orchestrator (Inquisitor / 350F persona) — China + CT focus, with OOB / Ukraine / DPRK / Iran depth",
    "totals": {
        "n_chunks": n_chunks,
        "n_tokens": n_tokens,
        "n_docs": sum(len(s) for s in docs_by_bucket.values()),
        "n_buckets": len(buckets),
        "avg_tokens_per_chunk": round(n_tokens / max(n_chunks, 1), 1),
        "structured_oob_chunks": structured_count,
        "prose_chunks": prose_count,
    },
    "acquisition": {
        "master_sources": total_urls,
        "successfully_acquired": acquired_count,
        "acquisition_rate": round(acquisition_rate, 3),
        "passes": ["pass1_harvest", "pass2_chrome_retry", "pass3_fetch_url_recovery"],
    },
    "dedup": {
        "raw_chunks": dedup_report["n_in"],
        "kept": dedup_report["n_kept"],
        "dropped_vs_mentor": dedup_report["dropped_breakdown"]["dup_with_mentor_corpus"],
        "dropped_vs_joint_fires": dedup_report["dropped_breakdown"]["dup_with_joint_fires_corpus"],
        "dropped_intra": dedup_report["dropped_breakdown"]["intra_corpus_duplicate"],
    },
    "by_category": {
        cat: {
            "chunks": cat_chunks[cat],
            "tokens": cat_tokens[cat],
            "docs": len(cat_docs[cat]),
        }
        for cat in sorted(cat_chunks)
    },
    "by_bucket": {
        b: {"chunks": buckets[b], "tokens": bucket_tokens[b], "docs": len(docs_by_bucket[b])}
        for b in sorted(buckets)
    },
    "schema": {
        "fields": [
            "doc_id", "bucket", "source_path", "source_url", "title",
            "org", "authors", "year", "section", "subsection", "license",
            "priority", "corpus_section", "is_structured", "chunk_idx",
            "n_chunks_in_doc", "n_tokens", "is_bibliography", "text",
        ],
        "tokenizer": "Qwen/Qwen3-0.6B-Base",
        "chunk_target_tokens": 1200,
        "chunk_overlap_tokens": 150,
        "structured_oob_chunking": "1 chunk per OOB unit file (no further splitting)",
    },
    "structured_oob_buckets": [
        "inq_oob_china_structured",
        "inq_oob_iran_structured",
        "inq_oob_dprk_structured",
        "inq_oob_red_ledger",
    ],
    "parent_corpus_repo": "github.com/omnissiahcypher/mentor-corpus",
    "subtree_target": "inquisitor_corpus/",
    "siblings": ["corpus/ (mentor)", "joint_fires_corpus/"],
}
OUT_MANIFEST.write_text(json.dumps(manifest, indent=2))
print(f"Wrote {OUT_MANIFEST}")

# --- README.md ---
def fmt_n(n): return f"{n:,}"

readme = f"""# Inquisitor Corpus

**Version:** v2026-05-09
**Persona:** 350F Intel Tech Warrant — Intel Support to Targeting orchestrator
**Scope:** China + Counter-Terrorism (primary); Ukraine / OOB / DPRK / Iran (depth)

## Totals

| Metric | Value |
|---|---:|
| Chunks (deduped) | {fmt_n(n_chunks)} |
| Tokens | {fmt_n(n_tokens)} |
| Documents | {fmt_n(sum(len(s) for s in docs_by_bucket.values()))} |
| Buckets | {fmt_n(len(buckets))} |
| Avg tokens/chunk | {round(n_tokens / max(n_chunks, 1), 1)} |
| Structured OOB chunks | {fmt_n(structured_count)} |
| Prose chunks | {fmt_n(prose_count)} |

## Acquisition

| Stage | Value |
|---|---:|
| Master sources | {total_urls} |
| Successfully acquired | {acquired_count} |
| Acquisition rate | {round(acquisition_rate * 100, 1)}% |

Three passes:
1. **Pass 1 — Harvest** — requests with browser fallback for 50+ think-tank/.mil hosts
2. **Pass 2 — Chrome 124 retry** — Sec-Ch-Ua headers, homepage warm-up cookies, per-host throttling
3. **Pass 3 — fetch_url recovery** — for Akamai/Cloudflare-warded hosts (recovered 21/50)

## Dedup

Compared against existing mentor-corpus repo (chunks.jsonl + joint_fires_corpus/chunks.jsonl).

| Metric | Value |
|---|---:|
| Raw chunks (pre-dedup) | {fmt_n(dedup_report['n_in'])} |
| Kept | {fmt_n(dedup_report['n_kept'])} |
| Dropped — vs mentor corpus | {dedup_report['dropped_breakdown']['dup_with_mentor_corpus']} |
| Dropped — vs joint_fires | {dedup_report['dropped_breakdown']['dup_with_joint_fires_corpus']} |
| Dropped — intra-corpus | {dedup_report['dropped_breakdown']['intra_corpus_duplicate']} |

## Coverage by Category

| Category | Docs | Chunks | Tokens |
|---|---:|---:|---:|
"""
for cat in sorted(cat_chunks, key=lambda c: -cat_chunks[c]):
    readme += f"| {cat} | {fmt_n(len(cat_docs[cat]))} | {fmt_n(cat_chunks[cat])} | {fmt_n(cat_tokens[cat])} |\n"

readme += """
## Schema

Each chunk record (JSONL line):

```json
{
  "doc_id": "inq__<bucket>__<slug>",
  "bucket": "inq_<orig_bucket>",
  "source_path": "inquisitor_corpus/extracted/<bucket>/<slug>.txt",
  "source_url": "...",
  "title": "...", "org": "...", "authors": "...", "year": "...",
  "section": "...", "subsection": "...", "license": "...",
  "priority": "P1|P2|P3",
  "corpus_section": "China|CT|Ukraine|OOB|DPRK_Iran",
  "is_structured": true|false,
  "chunk_idx": 0, "n_chunks_in_doc": N, "n_tokens": ...,
  "is_bibliography": true|false,
  "text": "..."
}
```

- **Tokenizer:** Qwen/Qwen3-0.6B-Base
- **Chunk target:** 1200 tokens
- **Overlap:** 150 tokens
- **Structured OOB:** Curated unit-records — emitted as 1 chunk/file, NOT re-split

## Top Buckets (by chunks)

| Bucket | Docs | Chunks | Tokens |
|---|---:|---:|---:|
"""
top_buckets = sorted(buckets.items(), key=lambda x: -x[1])[:25]
for b, n in top_buckets:
    readme += f"| `{b}` | {len(docs_by_bucket[b])} | {fmt_n(n)} | {fmt_n(bucket_tokens[b])} |\n"

readme += """
## Structured OOB Buckets

These buckets contain curated, hand-built unit records from the Inquisitor OOB schema:

| Bucket | Chunks | Notes |
|---|---:|---|
"""
for b in ["inq_oob_china_structured", "inq_oob_iran_structured",
          "inq_oob_dprk_structured", "inq_oob_red_ledger"]:
    if b in buckets:
        notes = {
            "inq_oob_china_structured": "5 theaters / 33 GAs+fleets+bases / 85 brigades (52 elite)",
            "inq_oob_iran_structured": "9 services / 46 regions / 79 brigades (bifurcated Iran schema)",
            "inq_oob_dprk_structured": "7 directorates / 30 corps+fleets / 42 brigades (4-tier KPA)",
            "inq_oob_red_ledger": "5 districts / 20 armies / 15 divs / 36 brigades (Russian Red Ledger DB)",
        }[b]
        readme += f"| `{b}` | {fmt_n(buckets[b])} | {notes} |\n"

readme += """
## Files

- `chunks/chunks_dedup.jsonl` — final deduped corpus (use this for retrieval)
- `chunks/chunks.jsonl` — raw chunks before dedup
- `chunks/chunk_stats.json` — per-bucket raw stats
- `chunks/dedupe_report.json` — dedup details
- `manifest/MANIFEST.json` — machine-readable corpus metadata
- `manifest/download_log.csv` — pass 1 harvest log (514 rows, all sources)
- `manifest/retry_pass_log.csv` — pass 2 Chrome 124 retry log
- `manifest/fetch_url_recovery_log.csv` — pass 3 fetch_url recovery log
- `scripts/harvest.py` — pass 1 harvester (browser fallback for 50+ hosts)
- `scripts/retry_pass.py` — pass 2 Chrome 124 retry
- `scripts/fetch_url_recovery.py` — pass 3 recovery
- `scripts/chunk_corpus.py` — chunker (Qwen3 tokenizer, 1200/150)
- `scripts/dedupe_against_parent.py` — dedup vs mentor + joint_fires

## Companion Repos

| Repo | Purpose |
|---|---|
| [omnissiahcypher/mentor-corpus](https://github.com/omnissiahcypher/mentor-corpus) | Parent monorepo (this is a subtree) |
| [Raven-Conspiracy/the-red-ledger](https://github.com/Raven-Conspiracy/the-red-ledger) | Russian OOB live database (source of `oob_red_ledger`) |

## Architecture

The Inquisitor orchestrator dispatches across 8 domain-specific intel agents
(HUMINT, SIGINT, GEOINT, OSINT, MASINT, AllSource, CI, TargetingIntel).
See `inquisitor_research/inquisitor_architecture.md` for full design.

## Critical Constraints (architecture-level)

1. Tag every claim by source category: `[CORPUS]` / `[INFERRED]` / `[GAP]` / `[COLLECTION-REQUIREMENT]`
2. Refuse to manufacture grid coordinates or signature data
3. Scaffold output depth to user persona (35F vs 350F vs O5)
"""

OUT_README.write_text(readme)
print(f"Wrote {OUT_README}")
print(f"\n=== INQUISITOR CORPUS BUILD COMPLETE ===")
print(f"Chunks: {fmt_n(n_chunks)} | Tokens: {fmt_n(n_tokens)} | Docs: {fmt_n(sum(len(s) for s in docs_by_bucket.values()))}")
