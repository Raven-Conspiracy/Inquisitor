# Inquisitor Corpus

**Version:** v2026-05-09
**Persona:** 350F Intel Tech Warrant — Intel Support to Targeting orchestrator
**Scope:** China + Counter-Terrorism (primary); Ukraine / OOB / DPRK / Iran (depth)

## Totals

| Metric | Value |
|---|---:|
| Chunks (deduped) | 6,481 |
| Tokens | 8,875,471 |
| Documents | 782 |
| Buckets | 139 |
| Avg tokens/chunk | 1369.5 |
| Structured OOB chunks | 413 |
| Prose chunks | 6,068 |

## Acquisition

| Stage | Value |
|---|---:|
| Master sources | 514 |
| Successfully acquired | 398 |
| Acquisition rate | 77.4% |

Three passes:
1. **Pass 1 — Harvest** — requests with browser fallback for 50+ think-tank/.mil hosts
2. **Pass 2 — Chrome 124 retry** — Sec-Ch-Ua headers, homepage warm-up cookies, per-host throttling
3. **Pass 3 — fetch_url recovery** — for Akamai/Cloudflare-warded hosts (recovered 21/50)

## Dedup

Compared against existing mentor-corpus repo (chunks.jsonl + joint_fires_corpus/chunks.jsonl).

| Metric | Value |
|---|---:|
| Raw chunks (pre-dedup) | 6,705 |
| Kept | 6,481 |
| Dropped — vs mentor corpus | 0 |
| Dropped — vs joint_fires | 80 |
| Dropped — intra-corpus | 144 |

## Coverage by Category

| Category | Docs | Chunks | Tokens |
|---|---:|---:|---:|
| Counter-Terrorism | 127 | 3,217 | 3,931,731 |
| OOB | 475 | 1,161 | 1,667,949 |
| China | 58 | 1,139 | 1,404,008 |
| Ukraine 2022–2025 | 59 | 635 | 1,201,022 |
| DPRK | 30 | 169 | 353,244 |
| Iran | 33 | 160 | 317,517 |

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
| `inq_china_uscc_new` | 3 | 633 | 643,621 |
| `inq_ct_org_aq_family` | 19 | 598 | 715,617 |
| `inq_ct_doctrine_uk` | 2 | 336 | 348,893 |
| `inq_ct_tradecraft_ic` | 8 | 302 | 328,112 |
| `inq_ct_doctrine_us_sof` | 6 | 242 | 281,681 |
| `inq_ct_org_hezbollah` | 8 | 233 | 286,235 |
| `inq_ct_doctrine_nato` | 2 | 215 | 186,791 |
| `inq_ukr_p1_cna` | 4 | 195 | 196,188 |
| `inq_oob_isw_russia_ukraine` | 5 | 164 | 322,497 |
| `inq_ct_org_is_family` | 10 | 163 | 243,290 |
| `inq_ct_org_shabaab` | 3 | 143 | 156,475 |
| `inq_ct_org_taliban_ttp` | 5 | 143 | 176,948 |
| `inq_oob_iran_structured` | 134 | 134 | 42,554 |
| `inq_ct_doctrine_us_army` | 4 | 129 | 122,136 |
| `inq_oob_china_structured` | 123 | 123 | 41,617 |
| `inq_oob_project2049_pla` | 4 | 123 | 142,927 |
| `inq_ukr_p1_csba` | 1 | 121 | 112,964 |
| `inq_oob_ru_other` | 3 | 112 | 122,605 |
| `inq_oob_dia_russia` | 1 | 98 | 96,619 |
| `inq_ct_doctrine_us_joint` | 1 | 96 | 83,685 |
| `inq_oob_dia_china` | 1 | 96 | 110,088 |
| `inq_ct_org_farc` | 2 | 87 | 104,152 |
| `inq_ct_org_irgc` | 1 | 84 | 97,468 |
| `inq_china_tw_govt` | 7 | 83 | 105,955 |
| `inq_oob_dprk_structured` | 79 | 79 | 32,785 |

## Structured OOB Buckets

These buckets contain curated, hand-built unit records from the Inquisitor OOB schema:

| Bucket | Chunks | Notes |
|---|---:|---|
| `inq_oob_china_structured` | 123 | 5 theaters / 33 GAs+fleets+bases / 85 brigades (52 elite) |
| `inq_oob_iran_structured` | 134 | 9 services / 46 regions / 79 brigades (bifurcated Iran schema) |
| `inq_oob_dprk_structured` | 79 | 7 directorates / 30 corps+fleets / 42 brigades (4-tier KPA) |
| `inq_oob_red_ledger` | 77 | 5 districts / 20 armies / 15 divs / 36 brigades (Russian Red Ledger DB) |

## Files

- `chunks/chunks.jsonl` — final deduped corpus (use this for retrieval)
- `chunks/chunk_stats.json` — per-bucket raw stats (pre-dedup)
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
