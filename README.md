# Inquisitor — Intelligence Orchestrator

> *"By the Throne, my brothers and sisters, no question goes unanswered, no signal goes unheeded. The Emperor's intelligence demands rigor, and the Inquisitor delivers."*

**Inquisitor** is an intelligence orchestrator: a small-model mentor stack plus 8 domain-specific intel agents that route a question to the right tradecraft, ground it in primary-source corpus, and refuse to hallucinate the things that get analysts killed (grid coordinates, signature data, false confidence).

Built on a **30,677-chunk / 31.1M-token** doctrinal corpus across three layered subtrees, fine-tuned from `Qwen/Qwen3-0.6B-Base`, deployable standalone or as a Palantir Foundry AIP Agent.

## The Orchestrator

```
                          ┌──────────────────────────┐
   user query  ─────────► │      INQUISITOR          │ ◄── persona scaffold
                          │  (Intel Tech Warrant     │     (35F / 350F / O5)
                          │   350F dispatch model)   │
                          └────────────┬─────────────┘
                                       │
        ┌──────────┬──────────┬────────┼────────┬──────────┬──────────┬──────────┐
        ▼          ▼          ▼        ▼        ▼          ▼          ▼          ▼
     HUMINT     SIGINT     GEOINT    OSINT    MASINT   AllSource    CI    TargetingIntel
       │          │          │        │        │          │          │          │
       └──────────┴──────────┴────────┴────────┴──────────┴──────────┴──────────┘
                                       │
                              corpus retrieval
                              (chunks.jsonl × 3 subtrees)
```

Every claim the orchestrator emits is tagged by source category:

- `[CORPUS]` — directly grounded in retrieved primary source
- `[INFERRED]` — analytic judgment, marked with confidence
- `[GAP]` — known unknown, flagged for collection
- `[COLLECTION-REQUIREMENT]` — a CCIR/PIR/SIR the analyst should generate

The orchestrator **refuses to fabricate grid coordinates, signature data, or unit dispositions** that are not in the corpus. This is non-negotiable: the model has been instructed and adversarially tested on these refusals.

## The Three Subtrees

| Subtree | Chunks | Tokens | Purpose |
|---|---:|---:|---|
| [`corpus/`](corpus/) | 17,241 | 15.5M | US/NATO IC + military doctrine + threat equipment foundation |
| [`joint_fires_corpus/`](joint_fires_corpus/) | 6,955 | 6.7M | Joint fires & targeting (131A WO + USAF 13F/14N + USN Strike + deep PLA platforms) |
| [`inquisitor_corpus/`](inquisitor_corpus/) | 6,481 | 8.9M | Intel Support to Targeting (350F): China + CT + Ukraine + structured OOB + DPRK/Iran |
| **Total** | **30,677** | **31.1M** | |

See each subtree's README for full bucket-level provenance:
- [`corpus/` doctrine bucket breakdown](#mentor-corpus-doctrine--equipment) (below)
- [`joint_fires_corpus/README.md`](joint_fires_corpus/README.md)
- [`inquisitor_corpus/README.md`](inquisitor_corpus/README.md)

## The Eight Domain Agents

Each agent owns a slice of the IC tradecraft space and is trained on a curated subset of the corpus, with its own retrieval scope and refusal rules.

| Agent | Disciplinary Focus | Primary Buckets |
|---|---|---|
| **HUMINT** | Source operations, debriefing, network analysis, vetting | `ct_tradecraft_humint`, `ct_tradecraft_network`, `ic_doctrine` |
| **SIGINT** | ELINT/COMINT, EW context, technical collection theory | `joint_doctrine`, `threat_equipment_*` (sensors), Watling RUSI |
| **GEOINT** | Imagery, geospatial analysis, terrain, IPB | `joint_doctrine` (JP 2-03), Project 2049, ISW geo products |
| **OSINT** | Public-source synthesis, social media exploitation, ACH | `ct_tradecraft_pol`, `ct_tradecraft_ic`, RAND/CSIS think-tank |
| **MASINT** | Measurement & signature intel, technical exploitation | `threat_equipment_csis`, `threat_equipment_odin`, FAS missile |
| **AllSource** | Fusion, ACH, structured analytic techniques, IPOE | `ic_doctrine` (ICD-203, NIU), `joint_doctrine`, `writing_style` |
| **CI** | Counter-intel tradecraft, deception, insider threat | `ct_tradecraft_*`, `russia_soviet` (HUMINT defense) |
| **TargetingIntel** | F3EAD, JIPOE, target development, BDA | `joint_fires_corpus/*` (full), `ct_tradecraft_targeted_killing`, OOB structured |

## What the Mentor Sounds Like

Trained model: [`OmnissiahsCypher/cogitator-bellum-mentor`](https://huggingface.co/OmnissiahsCypher) on Hugging Face, base: [`Qwen/Qwen3-0.6B-Base`](https://huggingface.co/Qwen/Qwen3-0.6B-Base).

The mentor speaks like a senior US/NATO intelligence and military mentor talking to a junior analyst. Anchored in concrete tradecraft, faithful to source material, with mentor voice markers ("Here's the way to think about it…", "Don't conflate X with Y…").

## Repo Layout

```
corpus/                          # Subtree 1: mentor doctrine + equipment
  chunks.jsonl                   # 17,241 chunks across 9 buckets (~15.5M tokens, 64 MB)
  chunk_stats.json
joint_fires_corpus/              # Subtree 2: joint fires & targeting (131A)
  chunks/chunks.jsonl            # 6,955 chunks
  extracted/                     # raw text by bucket
  manifest/                      # download logs, MANIFEST.json
  scripts/                       # harvest + chunk pipeline
  research/                      # source-curation notes
  README.md
inquisitor_corpus/               # Subtree 3: intel support to targeting (350F)
  chunks/chunks.jsonl            # 6,481 deduped chunks
  extracted/                     # 817 raw text files across 140 buckets
  manifest/                      # 3-pass harvest logs (pass1+pass2+pass3 fetch_url)
  scripts/                       # harvest + chunk + dedup
  README.md
qa/                              # Mentor Q&A for SFT
  qa_combined.jsonl              # 490 mentor-style Q&A (Claude Sonnet 4.6)
  qa_combined_stats.json
  qa_shard_0000.jsonl            # 150 Q&A from shard 0
  qa_shard_0001.jsonl            # 122 Q&A from shard 1
  qa_smoke_partial.jsonl         # 218 Q&A from smoke validation
docs/
  CORPUS_MANIFEST.md             # full per-source provenance for subtree 1
foundry/                         # Path A — Palantir Foundry deployment
  README.md
training/                        # Path B — Colab/Kaggle/HF Jobs deployment
  README.md
sft/
  sft_chat.jsonl                 # 490 examples with mentor system prompt + chat template
scripts/                         # subtree 1 chunkers + Q&A prompts
  qa_prompt.md
  qa_worker_full_template.txt
  shard_chunks.py
  chunk_wiki.py
  incremental_chunk_equipment.py
```

## Mentor Corpus Doctrine + Equipment

(Subtree 1 — `corpus/`)

| Bucket | Chunks | Tokens | Source |
|---|---:|---:|---|
| `ic_doctrine` | 87 | 80,757 | ICD 203, NIU Tradecraft Standards, etc. |
| `writing_style` | 343 | 323,159 | IC writing-style guides |
| `joint_doctrine` | 1,352 | 1,265,765 | JP / ADP / AFDP / ATP publications |
| `threat_doctrine` | 2,109 | 2,127,079 | Watling RUSI, FMSO, etc. |
| `russia_soviet` | 4,730 | 4,540,264 | Russian/Soviet doctrine sources |
| `threat_equipment_odin` | 5,668 | 4,629,855 | TRADOC G-2 ODIN Worldwide Equipment Guide |
| `threat_equipment_csis` | 387 | 346,132 | CSIS Missile Threat Project |
| `threat_equipment_wikipedia` | 2,152 | 1,987,878 | Wikipedia weapon-system articles |
| `cogitator_bellum` | 413 | 245,793 | User-authored UAV/munitions wiki |
| **Total** | **17,241** | **15,546,682** | |

Full per-source provenance: [`docs/CORPUS_MANIFEST.md`](docs/CORPUS_MANIFEST.md).

## Q&A Schema

One JSON object per line:

```json
{"chunk_id":"afdp-1-air-force-doctrine__c003",
 "doc_id":"afdp-1-air-force-doctrine",
 "bucket":"joint_doctrine",
 "source_path":"afdp-1-air-force-doctrine.pdf",
 "q":"What does AFDP-1 mean when it says Airmen support JADO by conducting operations 'in, from, and through' specific domains?",
 "a":"Here's the way to think about it. JADO stands for Joint All-Domain Operations…"}
```

Every Q&A in `qa_combined.jsonl` has been validated against the chunk index — `bucket`/`doc_id`/`source_path` are repaired from `chunks.jsonl` to guarantee schema correctness.

## Q&A Generation

`qa_combined.jsonl` was produced by Claude Sonnet 4.6 using the persona and prompt in `scripts/qa_prompt.md`. The prompt enforces:

- First-person mentor voice, no "according to the passage" hedging
- 7 question shapes (definitional, conceptual, operational, comparative, specification recall, pitfall, source-anchored) — mixed across the 5 questions per chunk
- Faithfulness: every number/date/name must match source exactly
- Equipment passages mix specs with doctrinal context

## Inquisitor Corpus Highlights

(Subtree 3 — `inquisitor_corpus/` — full details in its [README](inquisitor_corpus/README.md))

- **413 hand-curated structured OOB unit records** across 4 adversaries:
  - China: 5 theaters / 33 GAs+fleets+bases / 85 brigades (52 elite)
  - Iran: 9 services / 46 regions / 79 brigades (bifurcated Iran schema)
  - DPRK: 7 directorates / 30 corps+fleets / 42 brigades (4-tier KPA)
  - Russia: 5 districts / 20 armies / 15 divs / 36 brigades (Red Ledger DB)
- **3-pass acquisition pipeline** — 398/514 sources (77.4%):
  - Pass 1: requests + browser fallback for 50+ think-tank/.mil hosts
  - Pass 2: Chrome 124 spoofing + Sec-Ch-Ua + cookie warm-up
  - Pass 3: fetch_url recovery for Akamai/Cloudflare-warded hosts
- **CT depth** — 3,217 chunks: AQ family, IS family, Hezbollah, Hamas, Houthi, IRGC-QF, Taliban/TTP, plus US/UK/AU/CA doctrine and full F3EAD/HUMINT/network-analysis tradecraft.

## Companion Repos

| Repo | Purpose |
|---|---|
| [Raven-Conspiracy/the-red-ledger](https://github.com/Raven-Conspiracy/the-red-ledger) | Russian OOB live database — source for `inquisitor_corpus/oob_red_ledger` |
| [omnissiahcypher/munitions-uav-wiki](https://github.com/omnissiahcypher/munitions-uav-wiki) | User-authored UAV/munitions wiki — source for `cogitator_bellum` bucket |
| [OmnissiahsCypher on HF](https://huggingface.co/OmnissiahsCypher) | Trained mentor model |

## Training & Deployment

Two deployment paths:

- **[`training/`](training/README.md)** — train standalone on Colab/Kaggle/HF Jobs and push the model to Hugging Face Hub. Best for fast iteration on personal GPU.
- **[`foundry/`](foundry/README.md)** — train inside Palantir Foundry as a `ModelAdapter`, publish as a Foundry model resource, surface in AIP Agent Studio. Best for enterprise deployment with Ontology integration and AIP tooling.

Pre-formatted SFT data is at `sft/sft_chat.jsonl` (490 examples with mentor system prompt + chat template) and is consumed by both paths.

## Reproducing the Corpus

```bash
# Subtree 1 — mentor corpus
python scripts/incremental_chunk_equipment.py    # re-chunk equipment buckets
python scripts/chunk_wiki.py                     # re-chunk wiki bucket
python scripts/shard_chunks.py                   # shard for parallel Q&A
# Then generate Q&A using scripts/qa_prompt.md + scripts/qa_worker_full_template.txt

# Subtree 2 — joint_fires_corpus
python joint_fires_corpus/scripts/harvest.py
python joint_fires_corpus/scripts/chunk_corpus.py

# Subtree 3 — inquisitor_corpus
python inquisitor_corpus/scripts/harvest.py             # pass 1
python inquisitor_corpus/scripts/retry_pass.py          # pass 2 (Chrome 124)
python inquisitor_corpus/scripts/fetch_url_recovery.py  # pass 3 (Akamai)
python inquisitor_corpus/scripts/chunk_corpus.py        # tokenize + chunk
python inquisitor_corpus/scripts/dedupe_against_parent.py  # dedup vs subtrees 1+2
python inquisitor_corpus/scripts/build_manifest.py      # MANIFEST.json + README
```

## License

- DoD doctrine publications: public domain (US Government works).
- Watling RUSI / FMSO / NDU Press: open access; cite per their terms.
- ODIN / CSIS / Wikipedia: redistributed under fair-use / CC-BY-SA where applicable; original sources cited in `docs/CORPUS_MANIFEST.md`.
- Inquisitor corpus think-tank sources (ASPI, RAND, CNAS, CSBA, USCC, Project 2049, FPRI, Atlantic Council, etc.): redistributed for research use; original publishers cited per-chunk in `source_url` field.
- Cogitator Bellum wiki: user-owned, training-permitted (sourced from [`omnissiahcypher/munitions-uav-wiki`](https://github.com/omnissiahcypher/munitions-uav-wiki)).
- Q&A pairs: generated by Claude Sonnet 4.6, under Anthropic's terms of service.

This corpus is intended for research and personal model training. If you redistribute, preserve original-source attributions in `CORPUS_MANIFEST.md` and per-chunk `source_url` metadata.

## Citation

```
Inquisitor — Intelligence Orchestrator (2026).
30,677-chunk doctrinal + targeting corpus across mentor / joint fires / intel-support-to-targeting subtrees.
https://github.com/Raven-Conspiracy/Inquisitor
```

---

*The Inquisitor sees what others miss. The Inquisitor remembers what others forget. The Inquisitor refuses to invent what it does not know.*
