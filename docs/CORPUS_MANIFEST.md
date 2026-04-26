# Training Corpus Manifest
**Project**: Domain-expert chatbot — IC analytic tradecraft, DoD/IC writing standards, US joint terminology, Russian/Soviet warfare
**Persona**: Professional senior mentor speaking to a junior
**Base model (planned)**: `Qwen/Qwen3-0.6B-Base` via TRL `SFTTrainer` + LoRA
**HF account**: OmnissiahsCypher

---

## Summary

| Bucket | Documents | Pages |
|---|---:|---:|
| IC analytic standards | 9 | ~100 |
| Writing & style standards | 7 | ~600 |
| US joint doctrine & terminology | 13 | ~2,300 |
| US threat doctrine on Russia/OPFOR | 11 | ~3,400 |
| IC writing exemplars | 2 | ~130 |
| Russian / Soviet warfare (NATO-sourced) | 77 | ~6,800 |
| Worldwide Equipment Guide (TRADOC) | 5 | ~1,540 |
| ODIN equipment entries (TRADOC, structured) | 3,823 entries | — |
| CSIS Missile Threat entries | 159 entries | — |
| Wikipedia RU/CN equipment articles | 824 articles | — |
| Cogitator Bellum wiki (user-authored) | 374 entries | — |
| **Total documents/entries** | **~5,283** | **~14,940 + entry data** |

Most documents are unclassified, public-release, NATO-country-authored.
Wikipedia entries are CC BY-SA 4.0. CSIS entries are publicly published research used for educational reference.
Approximately **675 MB** of source files (PDF + JSON + HTML + text).

### Corpus chunk statistics (current)

| Bucket | Chunks | Tokens |
|---|---:|---:|
| ic_doctrine | 87 | 80,757 |
| writing_style | 343 | 323,159 |
| joint_doctrine | 1,352 | 1,265,765 |
| threat_doctrine | 2,109 | 2,127,079 |
| russia_soviet | 4,730 | 4,540,264 |
| threat_equipment_odin | 5,668 | 4,629,855 |
| threat_equipment_csis | 387 | 346,132 |
| threat_equipment_wikipedia | 2,152 | 1,987,878 |
| cogitator_bellum | 413 | 245,793 |
| **Total** | **17,241** | **15,546,682** |

---

## Bucket 1 — IC Analytic Standards

| File | Source |
|---|---|
| `icds-203-206-208-combined.pdf` | ODNI ICD 203 (Analytic Standards), ICD 206 (Sourcing), ICD 208 (Maximizing Utility) — combined, with Dec 2022 technical amendment |
| `icd-204-nipf.pdf` | ODNI ICD 204 — National Intelligence Priorities Framework |
| `icd-205-analytic-outreach.pdf` | ODNI ICD 205 — Analytic Outreach |
| `icd-207-national-intel-council.pdf` | ODNI ICD 207 — National Intelligence Council |
| `niu-analytic-tradecraft-standards.pdf` | NIU Research Short on the 9 Analytic Tradecraft Standards (Jun 2024) |

## Bucket 2 — Writing & Style Standards

| File | Source |
|---|---|
| `odni-style-writing-2011-2013.pdf` | ODNI Official Style Book (2011) + Writing Guide (2013) — FOIA release |
| `cia-style-manual-writers-guide.pdf` | CIA Style Manual & Writer's Guide for Intelligence Publications, 8th ed. |
| `cia-tradecraft-primer-2009.pdf` | A Tradecraft Primer: Structured Analytic Techniques (US Govt, 2009) |
| `cia-psychology-intelligence-analysis-heuer.pdf` | Richards J. Heuer — Psychology of Intelligence Analysis (CIA) |
| `cia-ic-struggle-express-uncertainty.pdf` | CIA CSI — The Intelligence Community's Struggle to Express Analytic Uncertainty |
| `dod-writing-style-guide.pdf` | DoD Writing Style Guide and Preferred Usage for DoD Issuances (2020) |
| `analysts-style-manual.pdf` | The Analyst's Style Manual (MCIIS — derived from CIA Writing Manual + Army Military Writing Reference) |

## Bucket 3 — US Joint Doctrine & Terminology

| File | Source |
|---|---|
| `dod-dictionary-jun2025.pdf` | DoD Dictionary of Military and Associated Terms — June 2025 (current) |
| `usmc-supplement-dod-dictionary.pdf` | USMC Supplement to the DoD Dictionary (MCRP 1-10.2, 2020) |
| `jp-2-0-joint-intelligence.pdf` | Joint Publication 2-0 — Joint Intelligence |
| `jp-3-0-joint-operations.pdf` | Joint Publication 3-0 — Joint Operations |
| `jp-5-0-joint-planning.pdf` | Joint Publication 5-0 — Joint Planning |
| `fm-6-0-commander-staff-2022.pdf` | Army FM 6-0 — Commander and Staff Organization and Operations (May 2022) |
| `afdp-1-air-force-doctrine.pdf` | Air Force Doctrine Publication 1 — The Air Force |
| `afdp-doctrine-101.pdf` | Air Force Doctrine 101 |
| `jp-1-doctrine-armed-forces.pdf` | JP 1 — Doctrine for the Armed Forces of the United States (2013) |
| `jp-2-01-joint-national-intel-support.pdf` | JP 2-01 — Joint and National Intelligence Support to Military Operations (2017) |
| `jp-2-01.3-jipoe.pdf` | JP 2-01.3 — Joint Intelligence Preparation of the Operational Environment (JIPOE, 2009) |
| `jp-3-13-information-operations.pdf` | JP 3-13 — Information Operations (2012) |
| `adp-2-0-intelligence.pdf` | ADP 2-0 — Intelligence (US Army, 2012) |
| `atp-2-22.9-osint.pdf` | ATP 2-22.9 — Open-Source Intelligence (US Army, 2012) |

## Bucket 4 — IC Analytic Doctrine (Gap-Fill Additions)

| File | Source |
|---|---|
| `icd-209-tearline.pdf` | ODNI ICD 209 — Tearline Production and Dissemination |
| `kent-words-estimative-probability.pdf` | Sherman Kent — Words of Estimative Probability (CIA CSI, 1964) |
| `kent-estimates-influence.pdf` | Sherman Kent — Estimates and Influence (CIA CSI) |
| `davis-kent-kendall-debate.pdf` | Jack Davis (ed.) — The Kent-Kendall Debate of 1949 (CIA CSI) |

## Bucket 5 — IC Writing Exemplars

| File | Source |
|---|---|
| `davis-compendium-tradecraft-notes.pdf` | Jack Davis — Compendium of Analytic Tradecraft Notes (NIC, 1997) |
| `declassified-nie-example.pdf` | NIE 11-14-63 — Capabilities of Soviet General Purpose Forces (CIA, 1963; declassified) |

## Bucket 6 — US Threat Doctrine on Russia / OPFOR

| File | Source |
|---|---|
| `atp-7-100.1-russian-tactics-2024.pdf` | ATP 7-100.1 — Russian Tactics (Feb 2024), official US Army threat doctrine |
| `tc-7-100-hybrid-threat.pdf` | TC 7-100 — Hybrid Threat (US Army, 2010) |
| `tc-7-100.2-opfor-tactics.pdf` | TC 7-100.2 — Opposing Force Tactics (US Army, Dec 2011) |
| `tc-7-100.3-irregular-opfor.pdf` | TC 7-100.3 — Irregular Opposing Forces (US Army) |
| `tradoc-weg-vol1-ground.pdf` | Worldwide Equipment Guide Vol. 1: Ground Systems (TRADOC, 2015) |
| `tradoc-weg-vol2-air-airdefense.pdf` | Worldwide Equipment Guide Vol. 2: Air & Air Defense Systems (TRADOC, 2015) |
| `tradoc-weg-vol2-air-airdefense-2011.pdf` | Worldwide Equipment Guide Vol. 2: Airspace & Air Defense Systems (TRADOC, 2011 — different equipment listings vs 2015) |
| `tradoc-weg-vol3-naval-littoral.pdf` | Worldwide Equipment Guide Vol. 3: Naval & Littoral Systems (TRADOC, 2015) |
| `tradoc-weg-vol3-naval-littoral-2011.pdf` | Worldwide Equipment Guide Vol. 3: Naval & Littoral Systems (TRADOC, 2011) |
| `tradoc-date-europe.pdf` | Decisive Action Training Environment (DATE) v2.2 — European Region (TRADOC) |
| `tradoc-oe-watch-latest.pdf` | OE Watch Vol. 14 Issue 8 (Nov 2024) — TRADOC G-2 FMSO |

## Bucket 7 — Russia / Soviet Warfare (77 docs)

Stored in `russia_soviet/`. Full provenance in `russia_soviet_reading_list.csv`, `download_log.csv`, and `gap_download_log.csv`.

### Gap-fill additions (translated primary sources + air/naval/nuclear deep dives)
| File | Source |
|---|---|
| `russia_soviet/voroshilov-lectures-vol1.pdf` | Voroshilov General Staff Academy Lesson — Ground Forces (CIA trans. 1985; ISCAP declassified 2015) |
| `russia_soviet/svechin-strategy.pdf` | Aleksandr Svechin — Strategy (East View/SAMS 1991 English ed.; orig. 1926) |
| `russia_soviet/galeotti-gerasimov-doctrine.pdf` | Mark Galeotti — The 'Gerasimov Doctrine' and Russian Non-Linear War (2014) |
| `russia_soviet/rand__russian-nuclear-doctrine.pdf` | NIPP / US Nuclear Strategy Forum — Russian Nuclear Doctrine (2021) |
| `russia_soviet/cna__russian-navy-strategy.pdf` | CNA — Russian Navy: Strategy and Purpose (2018) |
| `russia_soviet/rand__russian-aerospace-forces.pdf` | CNA / Bronk — Russian Combat Air Strengths and Limitations (2023) |

### Original 71-doc reading list

### Coverage by source country
- **USA**: 50 (Army, RAND, CNA, CSIS, CEPA, CSBA, FPRI, ISW, Atlantic Council, NDU, NWC, USAWC)
- **Estonia**: 6 (ICDS, NATO CCDCOE)
- **UK**: 5 (RUSI — Watling/Reynolds Ukraine reports)
- **Latvia**: 4 (NATO StratCom COE)
- **Germany**: 4 (SWP, GIDS Hamburg)
- **Sweden**: 3 (FOI — Swedish Defence Research Agency)
- **France**: 3 (IFRI, French MoD DGRIS)
- **Finland**: 2 (FIIA, Finnish NDU)
- **Poland**: 2 (PISM)
- **NATO HQ**: 1
- **Multinational NATO**: 1

### Coverage by category
| Category | Count | Filename prefix |
|---|---:|---|
| FMSO / Army Doctrine | 5 | `fmso__` |
| TRADOC / CALL / CAC handbooks | 6 | `tradoc__` |
| Army War College / NDU | 8 | `usawc__` |
| Naval War College | 3 | `nwc__` |
| NATO COEs / NATO HQ | 8 | `nato__` |
| RAND | 4 | `rand__` |
| RUSI | 5 | `rusi__` |
| CNA | 3 | `cna__` |
| CSIS | 1 | `csis__` |
| CSBA | 2 | `csba__` |
| CEPA | 2 | `cepa__` |
| FPRI | 2 | `fpri__` |
| ISW | 2 | `isw__` |
| Atlantic Council | 3 | `atlcouncil__` |
| FOI Sweden | 3 | `foi__` |
| FIIA Finland | 1 | `fiia__` |
| ICDS Estonia | 4 | `icds__` |
| SWP Germany | 3 | `swp__` |
| PISM Poland | 2 | `pism__` |
| IFRI France | 2 | `ifri__` |
| French MoD | 1 | `frmod__` |
| Parameters / Military Review | 2 | `params__` / `milrev__` |
| Historical / Soviet Studies (Glantz, Grau, etc.) | 5 | `hist__` |
| Military Strategy Magazine | 1 | `msmag__` |

### Time coverage
- WWII / Great Patriotic War (Glantz Soviet airborne, Tukhachevsky deep battle)
- Cold War Soviet doctrine
- Soviet–Afghan War (Grau "Bear Went Over the Mountain" + "Other Side of the Mountain")
- Post-Soviet (1990s–2000s)
- Georgia 2008
- Crimea / Donbas 2014
- Syria 2015–
- Ukraine 2022–present (extensive — RUSI, ISW, CNA, CSIS, RAND, CEPA, multiple NATO COE assessments)

---

## Bucket 8 — Russia / China Equipment Database (open-source substitute for Jane's)

A Jane's-style detailed equipment reference compiled from three complementary open sources. Stored under `sources/equipment_db/`.

### 8a. ODIN — TRADOC OE Data Integration Network (3,823 entries)
- **Source**: `https://odin.t2com.army.mil/WEG/List` (US Army TRADOC G-2 Worldwide Equipment Guide — live database)
- **Scope**: ground vehicles, fixed/rotary-wing aircraft, naval vessels, missiles, air-defense systems, small arms, artillery, EW, radars across all major adversary inventories with heavy Russia/China coverage.
- **Method**: full harvest via the dotCMS Lucene API (`POST /dotcms/api/content/_search` with `+contentType:WegCard +live:true`, 100 entries/page, 39 pages). Each entry then pulled by id from `/dotcms/api/content/id/{32-hex}` to obtain `notes` (prose) and `sections` (structured Variants / System / Dimensions / Automotive / Communications / Main Gun / ATGM / Coax / Aux / Fire Control / Protection).
- **Files**: 3,823 raw JSON in `odin/api_json/`, 3,823 cleaned per-entry text files in `odin/api_text/` (mean 4 KB each).
- **License**: Distribution A (US Government public release).
- **Note**: the visible "EXPORT" button on the list page produces `fullwegexportcompressed.pdf` (115 MB / 11,593 pages) but contains only 648 unique entries duplicated 6× across domain views; the API gives the full 3,823 unique entries.

### 8b. CSIS Missile Threat Project (159 entries)
- **Source**: `https://missilethreat.csis.org/` — sitemap `missile-sitemap.xml`.
- **Scope**: ballistic missiles, cruise missiles, hypersonic glide vehicles, defensive interceptors. Strong Russia/China/DPRK/Iran coverage with deployment status, range/payload, history.
- **Files**: 159 raw HTML pages in `csis/html/`, 159 cleaned text files in `csis/text/` (mean 6.5 KB).
- **License**: © CSIS — used here for research / educational reference; not redistributed in model weights.

### 8c. Wikipedia Russian / Chinese military equipment articles (824 articles)
- **Source**: enumerated from the Russian/Chinese equipment categories (`Category:Soviet_and_Russian_military_equipment`, `Category:Military_equipment_of_China`, and 8 sub-categories — tanks, AFVs, missiles, aircraft, ships, submarines, small arms, artillery).
- **Scope**: 918 candidate titles; 824 yielded substantive articles (≥95 % of Russia/China-attributable systems with English Wikipedia coverage).
- **Method**: bulk harvest via `https://en.wikipedia.org/wiki/Special:Export` (POST, 30 titles per request, `curonly=1`). Wikitext rendered to plain text with infoboxes preserved as `[INFOBOX] key: value` blocks.
- **Files**: 824 text files in `wikipedia/text/` (mean 7.9 KB, max 128 KB).
- **License**: CC BY-SA 4.0. Each file header preserves the canonical URL for attribution. Derivative training data inherits CC BY-SA 4.0.

### Why three sources, not one
- ODIN gives **structured spec sheets** (the closest open analog to Jane's military-vehicle entries).
- CSIS gives **analytical narrative** on each missile system (history, status, doctrinal context).
- Wikipedia gives **broad coverage and developmental history** (variants, operators, combat use), often the only English source for older Soviet platforms.

Together they cover ~4,800 distinct systems with redundancy that lets the trained model triangulate facts.

---

## Bucket 9 — Cogitator Bellum Wiki (user-authored)

- **Source**: `https://github.com/omnissiahcypher/munitions-uav-wiki` — user-authored, 14,061 lines / ~821 KB single Markdown file.
- **Scope**: Comprehensive global munitions, UAV, EW, counter-UAS, ADA, and APS reference for the period 2006–2026. Two volumes:
  - **Volume I (Offensive)**: kinetic munitions (16 producers), drones & UAVs (8 producers), non-kinetic & EW (6 producers), cross-reference tables, sources.
  - **Volume II (Defensive)**: ADA systems, counter-UAS systems, EW defensive & soft-kill, active protection systems, threat-defense matrices, analytical sections (layered defense, cost-exchange, FPV problem, future trends).
- **Method**: split on `###` headers → 374 substantive weapon-system entries (after filtering 3 TOC stubs and 174 short structural headings). Each entry retains parent volume + section as bracketed context.
- **Files**: `sources/munitions_uav_wiki/cogitator_bellum.md` (the original) plus 374 normalised text mirrors under `dataset/text/`.
- **License**: user-owned, training-permitted by author.
- **Why valuable**: this is the most current and analytically-organised view in the corpus — includes 2024–2026 conflict lessons (Ukraine FPV problem, Houthi Red Sea campaign, Gaza 2023–24) that ODIN/Wikipedia don't capture. Each entry is a complete spec sheet with combat use, flight/explosives data, EW features, capabilities, and citations — ideal for mentor-style Q&A.

---

## Sources we did not retrieve

10 entries from the original Russia/Soviet reading list were unrecoverable from this environment (Akamai datacenter-IP blocking). All are topically duplicative with documents secured.

4 gap-fill targets were paywalled or unavailable as free PDFs:
- Triandafillov *Nature of Operations of Modern Armies* (Routledge paywalled; CGSC ContentDM serves HTML viewer only)
- Pherson & Heuer *Structured Analytic Techniques* (CQ Press paywalled — partially substituted by CIA Tradecraft Primer 2009 already in corpus)
- Treverton *Reshaping National Intelligence* (RAND/Cambridge paywalled)
- Bruce & George *Analyzing Intelligence* (Georgetown UP paywalled)

Full failure lists: `failed_urls.txt`, `download_log.csv` (FAILED rows), `gap_urls_failed.txt`, `gap_download_log.csv`.

---

## Licensing & redistribution notes

- **US government works** (ICDs, JPs, ATP, FM, AFDP, DoD Dictionary, FMSO, TRADOC, CALL, CIA, NDU, USAWC, NWC publications): public domain in the US (17 USC § 105). Free to use for training.
- **NATO HQ and NATO COE publications**: typically released for public distribution; some carry CC-BY-style terms. Check individual document covers before public redistribution of the trained model's outputs.
- **Think-tank reports** (RAND, RUSI, CSIS, CNA, ISW, CEPA, CSBA, FPRI, Atlantic Council, FOI, ICDS, FIIA, SWP, PISM, IFRI, etc.): published as freely-downloadable analysis, copyright retained by publisher. Use for fine-tuning a model is generally considered fair use (transformative), but: **we will not redistribute the source PDFs as part of the model upload** — only the trained model weights and our own derived training data.
- **Glantz / Grau historical works** in `hist__`: published as US Army CSI / FMSO institutional research, public domain.

---

## Next phase

These 115 documents (~12,500 pages) become the raw material for dataset preparation:
1. Text extraction (PyMuPDF / pdfplumber)
2. Cleanup (page numbers, headers/footers, OCR artifacts where present)
3. Chunking into passages
4. Synthetic conversation generation — for each passage, generate Q&A pairs in the *senior-mentor-to-junior* voice (mentor-explains-concept style) using a strong model
5. Format as TRL conversational dataset (`messages: [{role, content}]`)
6. Train via `SFTTrainer` + LoRA on Qwen3-0.6B-Base
7. Push adapter + model card to HF Hub under OmnissiahsCypher
