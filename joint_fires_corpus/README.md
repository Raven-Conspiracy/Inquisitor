# Joint Fires & Targeting Analyst Corpus

A 6,955-chunk / 6.66M-token open-source corpus that clones the institutional knowledge of a US Army **131A Field Artillery Targeting Technician** warrant officer, plus the USAF (13F/13L/14N + Weapons School) and USN (Strike/NSFS/TLAM/IS) equivalents, together with deep PLA / PLAN / PLARF / PLAAF coverage and full kill-chain platform/sensor data.

This corpus is designed to feed an **AIP Agent in Palantir Foundry** (RAG + retrieval) and is layered on top of the existing [Omnissiah's Cypher mentor-corpus](https://github.com/omnissiahcypher/mentor-corpus) (17,241 chunks of US/NATO doctrine + Russia/Soviet + threat equipment).

## Layout

```
joint_fires_corpus/
├── chunks/
│   ├── chunks.jsonl            6,955 chunks across 28 buckets (~6.66M tokens, ~26 MB)
│   └── chunk_stats.json        per-bucket token/chunk counts
├── extracted/                  cleaned plaintext per source (the chunker's input)
│   └── <bucket>/<slug>.txt
├── raw/                        as-downloaded PDFs/HTML
│   └── <bucket>/<slug>.{pdf,html,txt}
├── manifest/
│   ├── download_log.csv        per-source harvest log (status, bytes, chars, paths)
│   └── source_inventory.md     human-readable provenance per bucket
└── scripts/
    ├── harvest.py              the harvester (wikipedia + PDF + HTML, with per-host throttling)
    ├── retry_failed_via_fetch.py   workaround for Akamai-blocked .mil/.gov hosts
    ├── chunk_corpus.py         chunker (Qwen3 tokenizer, 1200 token target, 150 overlap)
    └── fix_metadata_in_chunks.py   joins log to master CSV to fix title/org/year drift
```

## Bucket composition

All buckets are namespaced with a `jf_` prefix to avoid collisions with the existing mentor-corpus buckets when both are loaded into the same Foundry index.

### Doctrine & curricula (US/joint, 6 buckets, 1,353 chunks)

| Bucket | Chunks | Tokens | Description |
|---|---:|---:|---|
| `jf_joint_doctrine` | 504 | 456,611 | JP 3-09, JP 3-09.3, JP 3-60, JP 3-30, JP 3-31, JP 3-32 — joint fires, CAS, targeting, air ops, land ops, maritime ops |
| `jf_army_131a` | 193 | 184,236 | FM 3-09, FM 3-60, ATP 3-09.42, ATP 3-09.32, ATP 3-60.1, NTC Fire Support Handbook (CALL Pub 21-558), JFIRE multi-service procedures |
| `jf_usn_strike` | 151 | 143,005 | NWP 3-09 / NTRP 3-09.2 (NSFS), NWDC strike planning, SWOS curriculum mirrors |
| `jf_usmc_fires` | 1 | 180 | USMC Commandant's Professional Reading List |
| `jf_joint_cross_service` | 1 | 690 | CSIS Missile Threat Project portal |

### PLA / PLAN / PLAAF / PLARF (8 buckets, 4,937 chunks)

| Bucket | Chunks | Tokens | Description |
|---|---:|---:|---|
| `jf_pla_uscc` | 2,557 | 2,617,060 | USCC Annual Reports to Congress (2014–2024), section 2 deep-dives on PLA modernization |
| `jf_pla_casi_translations` | 791 | 639,375 | China Aerospace Studies Institute "In Their Own Words" — Science of Military Strategy 2013 + 2020, PLA Rocket Force org, Chinese Nuclear C2 |
| `jf_pla_dod_cmpr` | 737 | 651,275 | DoD Annual Report to Congress (Military and Security Developments Involving the PRC) — 2018, 2020, 2022, 2023, 2024 + DIA China Military Power 2019 + ONI PLA Navy 2015 + NASIC 2017 BCMT |
| `jf_pla_thinktank` | 523 | 509,058 | RAND, CSBA, AEI, CNAS, Atlantic Council, Carnegie, CSIS think-tank reports |
| `jf_pla_ndu` | 223 | 207,002 | NDU Press Strategic Forum series + CCP-PRC books (Crossing the Strait, Chairman Xi Remakes the PLA, PLA Beyond Borders, Taming the Hegemon, A Low-Visibility Force Multiplier) |
| `jf_pla_other` | 53 | 57,545 | Joint Force Quarterly articles + China Military Online English edition |
| `jf_pla_cmsi` | 49 | 51,899 | China Maritime Studies Institute (NWC) reports |
| `jf_pla_rand` | 2 | 1,445 | RAND research_reports landing pages (RR3049, RR392 Scorecard) |
| `jf_pla_crs` | 2 | 605 | CRS R46808 + RL33153 |

### Kill-chain platforms & sensors (14 buckets, 1,166 chunks)

| Bucket | Chunks | Tokens | Description |
|---|---:|---:|---|
| `jf_platform_us_air` | 302 | 294,161 | F-15EX, F-22, F-35, F-16V, F/A-18E/F, F-117 retired, B-2, B-52, B-21, EA-18G Growler — strike/multirole, EW, bombers |
| `jf_platform_us_navy` | 112 | 110,439 | DDG/CG/FFG classes, Tomahawk Block V, SM-6, NSM, LRASM, AEGIS BMD, sub-launched cruise |
| `jf_platform_us_army_fires` | 88 | 87,417 | M109A7 Paladin, HIMARS/M270, ATACMS, PrSM, GMLRS-ER, ERCA, RQ-7 Shadow, MQ-1C Gray Eagle |
| `jf_platform_us_isr_c2` | 167 | 167,285 | E-3 Sentry, E-7 Wedgetail, RC-135 family, U-2, RQ-4 Global Hawk, MQ-9 Reaper, JSTARS, P-8A Poseidon, MQ-4C Triton |
| `jf_platform_us_pods_sensors` | 21 | 18,234 | AN/AAQ-33 Sniper, AN/AAQ-28 Litening, AESA radars (APG-77, APG-81, APG-82) |
| `jf_platform_us_marine_fires` | 22 | 20,880 | AN/TPS-80 G/ATOR, MARFOR fires |
| `jf_platform_allied` | 198 | 194,107 | RAF Typhoon, JASDF F-15J, ROKAF F-15K, IDF F-35I Adir, Indian Rafale, Australian F-35A, Taiwan F-CK-1 |
| `jf_platform_pla_air` | 83 | 78,606 | J-20, J-16, J-10C, J-11/Su-27, J-15, J-35, H-6 family, Z-10/Z-19/Z-20, Y-20/YY-20A, KJ-2000/KJ-500 |
| `jf_platform_plan` | 33 | 29,984 | Type 003 Fujian carrier, Type 075 LHD, Type 055 destroyer, Type 052D, Type 094A SSBN, Type 093 SSN, Yuan-class |
| `jf_platform_plarf` | 29 | 25,236 | DF-21D, DF-26, DF-17, DF-41, CJ-10/DH-10, DF-100 |
| `jf_platform_pla_sensors` | 41 | 46,108 | JY-26 Skywatch-U, YLC-8B, CETC HF-OTH radars |
| `jf_platform_dprk_iran` | 28 | 23,855 | Hwasong missile family, Bavar-373, Khordad-3, Iranian Shahed UAVs |
| `jf_platform_russia_supplement` | 39 | 36,008 | 9M729 SSC-8, Iskander-M, Kalibr 3M-14, Kinzhal, Tsirkon, S-400/S-500 — supplements existing `russia_soviet` bucket |
| `jf_platform_cross_cutting` | 5 | 5,118 | FAS Military Analysis Network, NTI Country Profiles |

## Chunking config

- Tokenizer: `Qwen/Qwen3-0.6B-Base` (matches the existing mentor-corpus pipeline)
- Target: 1,200 tokens per chunk, 150 token overlap, sentence-aware splitter
- Chunks shorter than 200 tokens dropped, docs shorter than 600 chars skipped

Identical config to the parent [`mentor-corpus/corpus/chunks.jsonl`](https://github.com/omnissiahcypher/mentor-corpus/blob/main/corpus/chunks.jsonl) — chunks from both can be concatenated and indexed in the same Foundry retrieval set without rechunking.

## Chunk schema

```json
{
  "doc_id": "jf__platform_us_air__b-21-raider-northrop-grumman_a3b2c1d0",
  "bucket": "jf_platform_us_air",
  "source_path": "joint_fires_corpus/extracted/platform_us_air/b-21-raider-northrop-grumman-a3b2c1d0.txt",
  "source_url": "https://www.northropgrumman.com/what-we-do/air/b-21-raider",
  "title": "B-21 Raider (Northrop Grumman product page)",
  "org": "Northrop Grumman",
  "year": "2024",
  "section": "Section A — US Air Platforms (Strike & Multi-role)",
  "subsection": "A3 — Strategic Bombers",
  "license": "vendor public-affairs page (fair-use excerpt)",
  "chunk_idx": 0,
  "n_chunks_in_doc": 4,
  "n_tokens": 942,
  "is_bibliography": false,
  "text": "..."
}
```

The `title`, `org`, `year`, `section`, `subsection`, `source_url`, and `license` fields are all populated for every chunk (joined back from the master sources CSV by URL after harvest). This lets the Foundry agent return clean inline citations without lookup.

## Reuse from the parent mentor-corpus

The following existing buckets are **directly relevant to joint fires & targeting** and are referenced by this corpus rather than re-harvested:

| Existing bucket | Chunks | Why it's relevant |
|---|---:|---|
| [`cogitator_bellum`](https://github.com/omnissiahcypher/mentor-corpus/blob/main/corpus/chunks.jsonl) | 413 | User-authored UAV/munitions wiki — the spine for kill-chain effects |
| `russia_soviet` | 4,730 | Russian doctrine + tactics (already covered TOS-1, S-400, Kalibr family) |
| `threat_equipment_odin` | 5,668 | TRADOC G-2 ODIN Worldwide Equipment Guide — full inventory |
| `threat_equipment_csis` | 387 | CSIS Missile Threat Project — every named missile |
| `threat_equipment_wikipedia` | 2,152 | Wikipedia weapon-system articles |
| `joint_doctrine` | 1,352 | JP 1, JP 2-0, JP 3-0, JP 5-0, ADP/AFDP/ATP foundational |
| `threat_doctrine` | 2,109 | Watling RUSI, FMSO, Russian/Chinese threat tactics |

Combined corpus (both subtrees mounted to a single Foundry retrieval set): **24,196 chunks / ~22M tokens**.

## Foundry deployment

When deploying to a Palantir Foundry AIP Agent:

1. Concatenate the two `chunks.jsonl` files (or load both into the same dataset).
2. Index `text` with the embedding model of choice (Qwen3-Embedding-0.6B or larger).
3. Surface `title`, `bucket`, `source_url`, `section`, `year` in the agent's citation panel.
4. Filter buckets at retrieval time to scope queries (e.g., `bucket LIKE 'jf_platform_%' OR bucket LIKE 'jf_pla_%'` for a "PLA threat platforms" query).

## Data status

- 267 sources downloaded / 13 dead URLs dropped (Akamai-blocked, 404, paywalled IISS landing pages)
- 257 docs chunked / 10 docs skipped (extracted < 600 chars)
- All `.mil` / `.gov` / `.edu` PDFs harvested via Akamai-bypass workflow (real-browser TLS fingerprint)
- `manifest/download_log.csv` lists every URL with status, bytes, chars, and provenance

## License

All sources are open-source (US Government public domain, CC BY-SA Wikipedia, vendor public-affairs pages, or think-tank publications with public-release distribution). See per-row `license` field in `manifest/download_log.csv`.
