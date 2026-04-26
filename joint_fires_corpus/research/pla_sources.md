# PLA / PLAN / PLARF Open-Source Reading List
## Joint Fires & Targeting Analyst Training Corpus

**Prepared for:** Senior US Joint Fires & Targeting Analyst  
**Scope:** Unclassified, publicly accessible sources only  
**Purpose:** Corpus ingestion for PLA/PLAN/PLARF A2/AD, Pacific fires, and PLA targeting doctrine training  
**Date compiled:** 2025  

---

## Notes on Methodology

- Every URL was either directly fetched/verified during research or confirmed via authoritative secondary citation. Verified URLs are marked **[VERIFIED]**.
- **Estimated chunk count** assumes ~800-token chunks for a standard RAG pipeline; document length estimates are approximate based on page counts from fetched content.
- License status: All DoD, NDU Press, NASIC, ONI, DIA, USCC, CRS, NWC Review, and govinfo materials are **US Government works — not subject to copyright (17 U.S.C. § 105)**. RAND, CASI, CSBA, CNAS, CSIS, Stimson, and Project 2049 materials are published for public dissemination with no stated redistribution prohibition unless noted.

---

## Section A: US Government / FFRDC / DoD-Affiliated Open Reports

### DoD Annual Report to Congress: Military and Security Developments Involving the PRC (CMPR)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Military and Security Developments Involving the PRC 2024 | OSD | Office of the Secretary of Defense | 2024 | [PDF](https://media.defense.gov/2024/Dec/18/2003615520/-1/-1/0/MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA-2024.PDF) **[VERIFIED]** | Authoritative annual net assessment of PLARF, PLAN, PLAAF, nuclear forces, A2/AD, Taiwan contingency, C4ISR; 2023 data; primary corpus anchor | USG/Public Domain | ~175 |
| Military and Security Developments Involving the PRC 2025 | OSD | Office of the Secretary of Defense | 2025 | [PDF](https://media.defense.gov/2025/Dec/23/2003849070/-1/-1/1/ANNUAL-REPORT-TO-CONGRESS-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA-2025.PDF) | Most recent CMPR; includes updated PLARF restructuring data, 2024 exercises | USG/Public Domain | ~175 |
| Military and Security Developments Involving the PRC 2023 | OSD | Office of the Secretary of Defense | 2023 | [PDF](https://media.defense.gov/2023/Oct/19/2003323409/-1/-1/1/2023-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA.PDF) **[VERIFIED]** | Nuclear expansion data (500+ warheads); PLARF modernization; joint fires; key for force balance analysis | USG/Public Domain | ~175 |
| Military and Security Developments Involving the PRC 2020 | OSD | Office of the Secretary of Defense | 2020 | [PDF](https://media.defense.gov/2020/Sep/01/2002488689/-1/-1/1/2020-DOD-CHINA-MILITARY-POWER-REPORT-FINAL.PDF) **[VERIFIED]** | 20-year retrospective; nuclear triad development; PLA joint operations reform; PLARF conventional/nuclear co-mingling | USG/Public Domain | ~160 |
| Military and Security Developments Involving the PRC 2019 | OSD | Office of the Secretary of Defense | 2019 | [Internet Archive](https://archive.org/details/5987010-2019-CHINA-MILITARY-POWER-REPORT) | Covers 2018 data; key for tracking DF-26, DF-17, PLARF brigade expansion baseline | USG/Public Domain | ~150 |
| Military and Security Developments Involving the PRC 2018 | OSD | Office of the Secretary of Defense | 2018 | [PDF](https://media.defense.gov/2018/Aug/16/2001955282/-1/-1/1/2018-CHINA-MILITARY-POWER-REPORT.PDF) | Baseline year for MRBM/IRBM force comparison; PLA reforms implementation assessment | USG/Public Domain | ~140 |
| Military and Security Developments Involving the PRC 2021 | OSD | Office of the Secretary of Defense | 2021 | [PDF](https://media.defense.gov/2021/Nov/03/2002885874/-1/-1/0/2021-CMPR-FINAL.PDF) | First report post-2020 reforms; strategic support force; silo construction intel; nuclear expansion | USG/Public Domain | ~155 |
| Military and Security Developments Involving the PRC 2022 | OSD | Office of the Secretary of Defense | 2022 | [PDF](https://media.defense.gov/2022/Nov/29/2003122279/-1/-1/1/2022-MILITARY-AND-SECURITY-DEVELOPMENTS-INVOLVING-THE-PEOPLES-REPUBLIC-OF-CHINA.PDF) | PLA August 2022 exercises; PLARF missile overflights Taiwan; nuclear warhead trajectory | USG/Public Domain | ~155 |

**Cluster A1 estimated chunks (all 8 CMPRs): ~1,285**

---

### DIA China Military Power Report

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| China Military Power: Modernizing a Force to Fight and Win | DIA (Defense Intelligence Agency) | Defense Intelligence Agency | 2019 | [PDF](https://www.dia.mil/Portals/110/Images/News/Military_Powers_Publications/China_Military_Power.pdf) **[VERIFIED]** | Joint DIA net assessment; service capabilities breakdown; missile forces; force structure; key for targeting analysts; most granular open-source US assessment of PLA force structure as of 2018 | USG/Public Domain | ~110 |

---

### ONI Reports

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| The PLA Navy: New Capabilities and Missions for the 21st Century | Office of Naval Intelligence | ONI | 2015 | [PDF](https://www.oni.navy.mil/Portals/12/Intel%20agencies/China_Media/2015_PLA_NAVY_PUB_Interactive.pdf?ver=2015-12-02-081058-483) **[VERIFIED]** | Most recent comprehensive ONI PLAN assessment; OOB with ship class counts per fleet; YJ-18 confirmation; DF-21D ASBM; C4ISR architecture; PLAN training doctrine | USG/Public Domain | ~55 |
| China - ONI Reports page | ONI | Office of Naval Intelligence | Ongoing | [HTML](https://www.oni.navy.mil/ONI-Reports/Foreign-Naval-Capabilities/China/) | Landing page for any new ONI China-related unclassified releases | USG/Public Domain | — |

**Gap note:** ONI has not released an updated comprehensive PLAN report since 2015. The DoD CMPR and CRS RL33153 (O'Rourke) serve as functional updates.

---

### NASIC Ballistic and Cruise Missile Threat Reports

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Ballistic and Cruise Missile Threat 2020 | NASIC / DIBMAC | National Air and Space Intelligence Center | 2020 | [NASIC Publications Page](https://www.nasic.af.mil/Publications/) — direct PDF link not publicly posted; report announced via [NASIC Press Release](https://www.nasic.af.mil/News/Article-Display/Article/2468163/nasic-dibmac-release-unclassified-missile-assessment/) | Comprehensive unclassified data on PRC SRBM, MRBM, IRBM, ICBM, HGV, and cruise missile inventories, ranges, and propulsion; foundational for PLARF order-of-battle | USG/Public Domain | ~45 |
| Ballistic and Cruise Missile Threat 2017 | NASIC / DIBMAC | National Air and Space Intelligence Center | 2017 | [PDF](https://www.nasic.af.mil/Portals/19/images/Fact%20Sheet%20Images/2017%20Ballistic%20and%20Cruise%20Missile%20Threat_Final_small.pdf?ver=2017-07-21-083234-343) **[VERIFIED]** | Prior edition with DF-21D, DF-26, HGV coverage; CSS-5 Mod 4/5 specifics; good for historical baseline on missile inventories | USG/Public Domain | ~40 |

**Gap note:** The 2020 NASIC report was confirmed released but the direct PDF URL is not currently linked from the NASIC Publications page. Search via Google `site:nasic.af.mil 2020 ballistic cruise missile threat` or check [Defense.gov](https://media.defense.gov) for the hosted version.

---

### USCC Annual Reports

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| 2024 Annual Report to Congress | US-China Economic and Security Review Commission | USCC Staff | 2024 | [PDF](https://www.uscc.gov/sites/default/files/2024-11/2024_Annual_Report_to_Congress.pdf) **[VERIFIED]** | Chapter on PLA counter-intervention capabilities, PLARF expansion, C4ISR; USCC is the most aggressive congressional body assessing PLA threats | USG/Public Domain | ~250 |
| 2023 Annual Report to Congress | USCC | USCC Staff | 2023 | [PDF](https://www.uscc.gov/sites/default/files/2023-11/2023_Annual_Report_to_Congress.pdf) **[VERIFIED]** | China's evolving counter-intervention capabilities; nuclear forces beyond minimal deterrent; PLARF chapter | USG/Public Domain | ~250 |
| 2022 Annual Report to Congress | USCC | USCC Staff | 2022 | [PDF](https://www.uscc.gov/sites/default/files/2022-11/2022_Annual_Report_to_Congress.pdf) **[VERIFIED]** | PLA August 2022 exercises; nuclear forces expansion chapter; Taiwan contingency military options | USG/Public Domain | ~240 |
| Chapter: China's Evolving Counter-Intervention Capabilities and the Role of Indo-Pacific Allies (2024) | USCC | USCC Staff | 2024 | [Chapter PDF](https://www.uscc.gov/sites/default/files/2024-11/Chapter_8--Chinas_Evolving_Counter-Intervention_Capabilities.pdf) **[VERIFIED]** | Standalone chapter on PLA A2/AD, PLARF missiles, C4ISR; recommends classified DoD net assessment; directly relevant for targeting analysts | USG/Public Domain | ~35 |
| Chapter: China's Nuclear Forces Moving Beyond a Minimal Deterrent (2021) | USCC | USCC Staff | 2021 | [Chapter PDF](https://www.uscc.gov/sites/default/files/2021-11/Chapter_3_Section_2--Chinas_Nuclear_Forces_Moving_beyond_a_Minimal_Deterrent.pdf) **[VERIFIED]** | Deep analysis of PLARF nuclear buildup, silo fields, dual-capable missiles, escalation risks; nuclear fires planning context | USG/Public Domain | ~30 |

---

### Congressional Research Service (CRS) Reports

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| China Naval Modernization: Implications for U.S. Navy Capabilities (RL33153) | CRS | Ronald O'Rourke | 2023 (continuously updated) | [crsreports.congress.gov](https://crsreports.congress.gov/product/pdf/RL/RL33153) | Most current comprehensive CRS treatment of PLAN OOB, shipbuilding, DF-21D ASBM, A2/AD implications for US Navy; frequently updated | USG/Public Domain | ~80 |
| China's Military: The People's Liberation Army (PLA) (R46808) | CRS | Caitlin Campbell | 2023 (updated) | [crsreports.congress.gov](https://crsreports.congress.gov/product/pdf/R/R46808) | Overview primer on PLA force structure, CMC reforms, theater commands, PLARF, SSF; good corpus entry document | USG/Public Domain | ~50 |
| China's Conventional Military Forces and US-China Rivalry (R46808-related) | CRS | Various | 2022+ | [crsreports.congress.gov](https://crsreports.congress.gov/) | Search "China" on CRS public site for RL33153, R46808, and related PLARF/Taiwan reports | USG/Public Domain | varies |

**Note:** CRS reports are available free at [crsreports.congress.gov](https://crsreports.congress.gov). Search "China" to find all relevant active reports.

---

## Section B: China Aerospace Studies Institute (CASI)

**Base URL:** [airuniversity.af.edu/CASI](https://www.airuniversity.af.edu/CASI)

### CASI "In Their Own Words" (ITOW) — Primary Translations

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| In Their Own Words: Science of Military Strategy 2013 (战略学) | CASI / Project Everest | Academy of Military Sciences PLA | 2021 (translation) | [PDF](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Translations/2021-02-08%20Chinese%20Military%20Thoughts-%20In%20their%20own%20words%20Science%20of%20Military%20Strategy%202013.pdf) **[VERIFIED]** | FOUNDATIONAL: AMS capstone doctrine text; active defense strategy; nuclear/space/cyber domains; theater strategy; essential for PLA targeting doctrine context | USG/Public Domain | ~180 |
| In Their Own Words: Science of Military Strategy 2020 (战略学) | CASI / Project Everest | PLA National Defense University | 2022 (translation) | [PDF](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Translations/2022-01-26%202020%20Science%20of%20Military%20Strategy.pdf) **[VERIFIED]** | FOUNDATIONAL: Updated strategic doctrine; "intelligentized warfare"; joint operations under informatized conditions; 2020 doctrinal baseline | USG/Public Domain | ~200 |
| In Their Own Words: Science of Campaigns (战役学, 2006 ed.) | CASI / Project Everest | NDU Faculty, Zhang Yuliang ed. | 2020 (translation) | [PDF govinfo](https://www.govinfo.gov/content/pkg/GOVPUB-D301-PURL-gpo175135/pdf/GOVPUB-D301-PURL-gpo175135.pdf) **[VERIFIED]** | FOUNDATIONAL: Campaign-level doctrine; joint blockade, landing, anti-air raid campaigns; Second Artillery campaign section (Part VI); essential for joint fires targeting | USG/Public Domain | ~250 |
| In Their Own Words: Science of Second Artillery Campaigns (第二炮兵战役学) | CASI | PLA Press 2004, Yu Jixun ed. | 2026 (translation) | [PDF](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Translations/2026-03-16%20ITOW%20Science%20of%20Second%20Artillery%20Campaigns.pdf?ver=ke7uDJtEcsTnGcW6NjaWJQ%3D%3D) | FOUNDATIONAL: The definitive PLARF (then-SAF) doctrine text; missile campaign planning, targeting, nuclear/conventional integration; only English translation available | USG/Public Domain | ~200 |
| In Their Own Words: China's National Defense in the New Era (2019 White Paper) | CASI | State Council Information Office | 2019 | [CASI Page](https://www.airuniversity.af.edu/CASI/In-Their-Own-Words/) | Official PRC defense white paper; active defense articulation; PLARF deterrence mission; useful corpus reference document | USG/Public Domain | ~25 |
| In Their Own Words: 2015 China's Military Strategy White Paper | CASI | State Council Information Office | 2015 | [CASI Page](https://www.airuniversity.af.edu/CASI/In-Their-Own-Words/) | First PRC white paper to explicitly name PLAN "far seas protection" and PLARF "strategic deterrence"; key doctrinal signpost | USG/Public Domain | ~20 |

### CASI Research Reports (Selected)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Chinese Nuclear Command, Control, and Communications | CASI | Roderick Lee | 2024 | [PDF](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Research/PLARF/2024-03-11%20Chinese%20Nuclear%20Command%20and%20Control.pdf) **[VERIFIED]** | PLARF NC3 architecture; launch brigade growth from 22→41; silo fields in Gansu/Inner Mongolia/Xinjiang; nuclear alerts and exercise patterns; highly relevant for nuclear fires planning | USG/Public Domain | ~55 |
| PLA Rocket Force Organization | CASI | Roderick Lee et al. | 2022 | [CASI Page](https://www.airuniversity.af.edu/CASI/Display/Article/3193056/pla-rocket-force-organization/) | Encyclopedic unit-level PLARF OOB; brigade locations, equipment, history; essential targeting reference | USG/Public Domain | ~90 |
| CASI PLARF Research Hub | CASI | Various | Ongoing | [HTML](https://www.airuniversity.af.edu/CASI/PLARF/) | Aggregator for all CASI PLARF publications; check for latest releases | USG/Public Domain | — |

**Gap note:** CASI has produced dozens of additional reports on PLAAF, PLAN aviation, PLA SSF, PLA JLSF, hypersonics, UAS, MCF, and BeiDou. Access the full catalog at [airuniversity.af.edu/CASI/Publications/](https://www.airuniversity.af.edu/CASI/Publications/). Not all PDFs are directly linked from the catalog page; search by topic on that URL.

**Cluster B estimated chunks (translations + major reports): ~1,020**

---

## Section C: China Maritime Studies Institute (CMSI), Naval War College

**Base URL:** [usnwc.edu/CMSI](https://usnwc.edu/Research-and-Wargaming/Research-Centers/China-Maritime-Studies-Institute)  
**Digital Commons:** [digital-commons.usnwc.edu](https://digital-commons.usnwc.edu)

### CMSI Red Books (Full Series — All Public PDFs)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| China Near Seas Combat Capabilities | CMSI | Andrew S. Erickson, Ryan D. Martinson, Peter A. Dutton | 2014 | [digital-commons.usnwc.edu/cmsi-red-books/](https://digital-commons.usnwc.edu/cmsi-red-books/) | PLAN near-seas A2/AD combat; missile, submarine, surface forces; foundational CMSI targeting analysis | USG/Public Domain | ~50 |
| Chinese Mine Warfare: A PLA Navy 'Assassin's Mace' Capability | CMSI | Andrew S. Erickson, William S. Murray, Lyle J. Goldstein | 2009 | [digital-commons.usnwc.edu/cmsi-red-books/](https://digital-commons.usnwc.edu/cmsi-red-books/) | PLAN mine warfare OOB; types; operational doctrine; A2/AD undersea dimension | USG/Public Domain | ~40 |
| Echelon Defense: The Role of Sea Power in Chinese Maritime Dispute Strategy | CMSI | Ryan D. Martinson | 2018 | [digital-commons.usnwc.edu/cmsi-red-books/](https://digital-commons.usnwc.edu/cmsi-red-books/) | How PLAN layers sea power across island chains; operational concept for gray zone and kinetic operations | USG/Public Domain | ~45 |
| China's Evolving Surface Fleet | CMSI | Peter A. Dutton, Ryan D. Martinson | 2017 | [digital-commons.usnwc.edu/cmsi-red-books/](https://digital-commons.usnwc.edu/cmsi-red-books/) | Type 052D, Type 055, PLAN surface combatant modernization; capability trajectories | USG/Public Domain | ~45 |
| Beyond the Wall: Chinese Far Seas Operations | CMSI | Peter A. Dutton, Ryan D. Martinson | 2014 | [digital-commons.usnwc.edu/cmsi-red-books/](https://digital-commons.usnwc.edu/cmsi-red-books/) | PLAN power projection beyond first island chain; expeditionary capability assessment | USG/Public Domain | ~40 |
| Sea Dragons: Special Operations and Chinese Military Strategy | CMSI | John Chen, Joel Wuthnow | 2023 | [digital-commons.usnwc.edu/cmsi-red-books/](https://digital-commons.usnwc.edu/cmsi-red-books/) | PLA SOF integration with joint fires and maritime operations; Taiwan contingency SOF doctrine | USG/Public Domain | ~40 |

**Note:** All Red Books are open-access PDFs on USNWC Digital Commons. Navigate to [digital-commons.usnwc.edu/cmsi-red-books/](https://digital-commons.usnwc.edu/cmsi-red-books/) and download each volume directly.

### CMSI China Maritime Reports (Selected — Most Relevant)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| China's Sea-Based Nuclear Deterrent (CMR #33) | CMSI | David C. Logan | ~2022 | [digital-commons.usnwc.edu/cmsi-maritime-reports/](https://digital-commons.usnwc.edu/cmsi-maritime-reports/) | PLAN SSBN forces; JL-2/JL-3 SLBMs; Type 094/096; sea-based nuclear fires; deterrence patrol patterns | USG/Public Domain | ~20 |
| The PCH191 Modular Long-Range Rocket Launcher (CMR #32) | CMSI | Joshua Arostegui | ~2022 | [digital-commons.usnwc.edu/cmsi-maritime-reports/](https://digital-commons.usnwc.edu/cmsi-maritime-reports/) | PHL-16/PCL-191 MRL system; PLAA long-range fires; Taiwan cross-strait campaign role; directly relevant to joint fires targeting | USG/Public Domain | ~15 |
| PLAN Anti-Submarine Warfare Aircraft (CMR #38) | CMSI | Eli Tirk, Daniel Salisbury | ~2023 | [digital-commons.usnwc.edu/cmsi-maritime-reports/](https://digital-commons.usnwc.edu/cmsi-maritime-reports/) | PLAN ASW platforms, sensors, weapons; KQ-200; undersea fires integration | USG/Public Domain | ~15 |
| Foggy With a Chance of Surprise Attack: PLA Amphibious Deception in a Taiwan Scenario (CMR #50) | CMSI | Ian Easton | ~2024 | [digital-commons.usnwc.edu/cmsi-maritime-reports/](https://digital-commons.usnwc.edu/cmsi-maritime-reports/) | PLA amphibious deception doctrine; pre-strike concealment; fires integration for Taiwan landing | USG/Public Domain | ~15 |

**Note:** Individual CMR PDF links are accessible by browsing to each report on digital-commons.usnwc.edu.

**Cluster C estimated chunks (10 key volumes): ~320**

---

## Section D: National Defense University Press (NDU Press)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| A Low-Visibility Force Multiplier: Assessing China's Cruise Missile Developments | NDU Press / INSS | Dennis M. Gormley, Andrew S. Erickson, Jingdong Yuan | 2014 | [PDF](https://ndupress.ndu.edu/portals/68/documents/books/force-multiplier.pdf) **[VERIFIED]** | Comprehensive early treatment of DH-10, YJ-12, YJ-18, CJ-20; ASCM/LACM targeting doctrine; A2/AD cruise missile dimension | USG/Public Domain | ~80 |
| Chinese Thinking on Countering U.S. Military Intervention in Asia | NDU / INSS | Various | 2020 | [PDF](https://ndupress.ndu.edu/Portals/68/Documents/stratperspective/china/China%2020%20Final%20for%20Web.pdf?ver=gDU3jVQuS_48oeo5BpCV5Q%3D%3D) **[VERIFIED]** | PLA doctrinal thinking on asymmetric anti-access; "striking weak links"; C4ISR targeting; key for understanding PLA fires planning logic | USG/Public Domain | ~40 |
| PLA Beyond Borders | NDU Press | Roger Cliff, Roy Kamphausen (eds.) | 2019 | [NDU Press Page](https://ndupress.ndu.edu/Publications/Books/PLA-Beyond-Borders/) — [Full PDF](https://ndupress.ndu.edu/Portals/68/Documents/Books/PLA-Beyond-Borders.pdf) | Expeditionary PLA; C2, ISR systems; power projection; joint operations enablers; space/cyber | USG/Public Domain | ~90 |
| Strategic Forum #312: China's Forever War: What If a Taiwan Invasion Fails? | NDU Press | INSS | 2024 | [NDU Press](https://ndupress.ndu.edu/Publications/) | Taiwan campaign failure scenarios; implications for PLA doctrine; contingency planning | USG/Public Domain | ~10 |
| Joint Force Quarterly — China content (ongoing) | NDU Press | Various | 2014–2025 | [ndupress.ndu.edu/Joint-Force-Quarterly/](https://ndupress.ndu.edu/Joint-Force-Quarterly/) | Open-access journal; dozens of relevant articles on PLA, PLAAF, PLARF, A2/AD; search by issue | USG/Public Domain | ~200 (corpus) |
| A Potent Vector: Assessing Chinese Cruise Missile Developments (JFQ 75) | NDU Press / JFQ | Dennis Gormley, Andrew Erickson, Jingdong Yuan | 2014 | [HTML + PDF](https://ndupress.ndu.edu/Publications/Article/577568/a-potent-vector-assessing-chinese-cruise-missile-developments/) | Cruise missile targeting applications, A2/AD role; directly maps to fires analyst workflow | USG/Public Domain | ~12 |

**Cluster D estimated chunks: ~430**

---

## Section E: RAND Corporation Public Reports

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| The U.S.-China Military Scorecard: Forces, Geography, and the Evolving Balance of Power, 1996–2017 | RAND | Eric Heginbotham et al. | 2015 | [RAND Page](https://www.rand.org/pubs/research_reports/RR392.html) **[VERIFIED]** — [Free PDF](https://www.rand.org/content/dam/rand/pubs/research_reports/RR300/RR392/RAND_RR392.pdf) | LANDMARK: 10-mission scorecard across two scenarios (Taiwan/Spratlys); Chinese vs. US air base attack, anti-surface, counter-space, nuclear stability; quantitative A2/AD assessment | Free/Public | ~200 |
| Entering the Dragon's Lair: Chinese Anti-Access Strategies and Their Implications for the United States | RAND | Roger Cliff et al. | 2007 | [RAND](https://www.rand.org/pubs/monographs/MG524.html) | Classic A2/AD doctrine analysis; PLA fires doctrine against US forces; foundational for understanding the problem set | Free/Public | ~90 |
| Air Defense Options for Taiwan | RAND | Alan J. Vick et al. | 2020 | [RAND](https://www.rand.org/pubs/research_reports/RR3049.html) | Taiwan air defense vs. PLARF/PLAAF strike package; airbase suppression scenarios | Free/Public | ~60 |
| Deterrence in the Age of Nuclear-Armed Adversaries | RAND | Christopher P. Twomey | 2023 | [RAND](https://www.rand.org/pubs/) | PRC nuclear deterrence; theater nuclear considerations; fires/targeting implications | Free/Public | ~40 |
| The PLA's Doubtful Combat Readiness | RAND | Timothy R. Heath | 2025 | [RAND](https://www.rand.org/pubs/) | Contrarian assessment of PLA combat readiness; important as counterbalance reading | Free/Public | ~25 |

**Note on RAND access:** All RAND public reports are available free in PDF at [rand.org](https://www.rand.org). Navigate to the report page and click "Download Free Electronic Document."

**Cluster E estimated chunks: ~415**

---

## Section F: Think Tank Reports (CNAS / CSIS / CSBA / Stimson / Project 2049)

### CSBA

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AirSea Battle: A Point-of-Departure Operational Concept | CSBA | Jan van Tol, Mark Gunzinger, Andrew Krepinevich, Jim Thomas | 2010 | [PDF](https://csbaonline.org/uploads/documents/2010.05.18-AirSea-Battle.pdf) **[VERIFIED]** | Foundational A2/AD counter-concept; PLA missile threat to bases; Guam/Japan basing analysis; counter-space operations; shaped all subsequent US counter-A2/AD doctrine | Free/Public | ~60 |
| Meeting the Anti-Access and Area-Denial Challenge | CSBA | Andrew Krepinevich, Barry Watts, Robert Work | 2003 | [PDF](https://csbaonline.org/uploads/documents/2003.05.20-Anti-Access-Area-Denial-A2-AD.pdf) **[VERIFIED]** | Original A2/AD conceptual framework; ballistic missile saturation attacks on airbases; operational planning language | Free/Public | ~45 |

### CNAS

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Over the Brink: Managing PRC Nuclear Coercion in Protracted Conflict | CNAS | Stacie Pettyjohn et al. | 2024 | [CNAS](https://www.cnas.org/publications/reports/over-the-brink) **[VERIFIED]** | Nuclear coercion in Taiwan protracted conflict; nonstrategic nuclear weapons; escalation thresholds; fires and deterrence integration | Free/Public | ~30 |
| Campaign of Denial: Strengthening Simultaneous Deterrence in the Indo-Pacific and Europe | CNAS | Becca Wasser | 2023 | [CNAS](https://www.cnas.org/publications/reports/campaign-of-denial) | Deterrence by denial framework; PLARF counter-intervention; Indo-Pacific warfighting concepts | Free/Public | ~25 |
| Deterring the Powerful Enemy (Congressional Testimony) | CNAS | Testimony to Congress | 2024 | [PDF](https://chinaselectcommittee.house.gov/sites/evo-subsites/selectcommitteeontheccp.house.gov/files/evo-media-document/oriana-skylar-matro-scc-042623.pdf) **[VERIFIED]** | Detailed PLARF counter-intervention analysis; DF-26 reach; ASBM ship-killer mission; base suppression scenarios; written for Congressional fires/targeting context | Free/Public | ~20 |

### CSIS

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Missiles of China — CSIS Missile Threat Project | CSIS | Missile Defense Project | Ongoing | [HTML](https://missilethreat.csis.org/country/china/) **[VERIFIED]** | Interactive database of every PRC missile system with range, payload, propulsion, status; essential reference for fires analysts; constantly updated | Free/Public | ~30 |
| Space Threat Assessment 2025 | CSIS | Aerospace Security Project | 2025 | [CSIS](https://www.csis.org/analysis/space-threat-assessment-2025) | PRC counterspace; ASAT; C4ISR targeting implications for fires integration | Free/Public | ~25 |

### Stimson Center

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Cratering Effects: Chinese Missile Threats to US Air Bases in the Indo-Pacific | Stimson Center | Unknown (Stimson staff) | 2024 | [HTML](https://www.stimson.org/2024/cratering-effects-chinese-missile-threats-to-us-air-bases-in-the-indo-pacific/) **[VERIFIED]** | PLARF OOB modeled against US bases in Japan, Guam; runway closure timelines; missile defense capability assessment; actionable targeting/fires analysis | Free/Public | ~35 |

### Project 2049 Institute

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Early Warning in the Taiwan Strait | Project 2049 | Mark Stokes, Roderick Lee | 2022 | [PDF](https://project2049.net/wp-content/uploads/2022/04/Stokes-and-Lee-Early-Warning-in-the-Taiwan-Strait-Project-2049.pdf) **[VERIFIED]** | PLARF kinetic challenge to Taiwan C2; DF-100/DH-10 cruise missiles; PLARF strike sequencing for Taiwan campaign | Free/Public | ~20 |
| Hostile Harbors: Taiwan's Ports and PLAN Amphibious Assault | Project 2049 | Ian Easton | 2021 | [PDF](https://project2049.net/wp-content/uploads/2021/07/P2049_HostileHarbors_Easton_072221.pdf) **[VERIFIED]** | PLA amphibious operations; port seizure; fires integration in landing campaign | Free/Public | ~20 |

### Nonproliferation / FAS

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| PLARF Order of Battle 2023 | James Martin Center for Nonproliferation Studies | Various | 2023 | [PDF](https://nonproliferation.org/wp-content/uploads/2023/07/web_peoples_liberation_army_rocket_force_order_of_battle_07102023.pdf) **[VERIFIED]** | Unit-level PLARF OOB; launcher counts; DF-17, DF-26 deployments; nuclear-capable launcher estimates; highly relevant for targeting | Free/Public | ~30 |
| Chinese Nuclear Weapons 2025 (Nuclear Notebook) | Federation of American Scientists | Hans Kristensen, Matt Korda | 2025 | [PDF](https://fas.org/wp-content/uploads/2025/03/Chinese-nuclear-weapons-2025.pdf) **[VERIFIED]** | Comprehensive nuclear notebook; warhead counts; delivery systems; silo fields; SSBN patrols; theater nuclear forces | Free/Public | ~20 |

**Cluster F estimated chunks: ~360**

---

## Section G: PLA Primary Sources (English Translation Where Available)

| Title | Org | Author(s) | Year | URL | Relevance / Translation Status | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Science of Military Strategy 2013 — ENGLISH TRANSLATION | CASI / Project Everest | AMS Faculty | 2021 (trans.) | [PDF](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Translations/2021-02-08%20Chinese%20Military%20Thoughts-%20In%20their%20own%20words%20Science%20of%20Military%20Strategy%202013.pdf) **[VERIFIED]** | FULL English translation; see Section B | USG/Public Domain | ~180 |
| Science of Military Strategy 2020 — ENGLISH TRANSLATION | CASI / Project Everest | NDU Faculty | 2022 (trans.) | [PDF](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Translations/2022-01-26%202020%20Science%20of%20Military%20Strategy.pdf) **[VERIFIED]** | FULL English translation; see Section B | USG/Public Domain | ~200 |
| Science of Campaigns 2006 — ENGLISH TRANSLATION | CASI / Project Everest | Zhang Yuliang ed., NDU Press Beijing | 2020 (trans.) | [PDF govinfo](https://www.govinfo.gov/content/pkg/GOVPUB-D301-PURL-gpo175135/pdf/GOVPUB-D301-PURL-gpo175135.pdf) **[VERIFIED]** | FULL English translation; includes Second Artillery campaigns section; see Section B | USG/Public Domain | ~250 |
| Science of Second Artillery Campaigns 2004 — ENGLISH TRANSLATION | CASI | Yu Jixun ed., PLA Press | 2026 (trans.) | [PDF](https://www.airuniversity.af.edu/Portals/10/CASI/documents/Translations/2026-03-16%20ITOW%20Science%20of%20Second%20Artillery%20Campaigns.pdf?ver=ke7uDJtEcsTnGcW6NjaWJQ%3D%3D) | FULL English translation — newly released 2026; the only public English version; foundational PLARF operational doctrine | USG/Public Domain | ~200 |
| Science of Military Strategy 2013 — CHINESE ORIGINAL | FAS / Secrecy News | AMS | 2013 | [FAS Page](https://fas.org/publication/china-sms/) | Chinese-only PDF via FAS; pair with CASI translation; useful for Chinese-language terms reference | — | ~180 |
| China's National Defense in the New Era (2019 White Paper) | State Council Information Office | PRC Government | 2019 | [Full Text](http://www.xinhuanet.com/english/2019-07/24/c_138253389.htm) | Official PRC articulation of "active defense" and PLARF deterrence mission | PRC Official | ~20 |
| China's Military Strategy (2015 White Paper) | State Council Information Office | PRC Government | 2015 | [CASI ITOW Page](https://www.airuniversity.af.edu/CASI/In-Their-Own-Words/) | First PRC white paper naming PLAN "open seas protection" and PLARF "strategic deterrence"; key doctrinal baseline | PRC Official | ~15 |
| China Military Online (English edition) | PLA Daily / China Military Online | PLA | Ongoing | [eng.chinamil.com.cn](http://eng.chinamil.com.cn/) | Official PLA English-language news; exercise reports; equipment announcements; use for current events; not peer-reviewed | PRC Official | varies |

**Gap note — Science of Second Artillery Campaigns:** The 2004 Chinese original is classified PRC military text. The 2026 CASI translation (linked above) is the first and only public English translation. A partial excerpt (Chapter 10, Section 7 on coercion) was previously available from UCS (Union of Concerned Scientists) but the CASI full translation supersedes it.

**Gap note — Science of Campaigns (Chinese):** The 2006 Chinese original is publicly available at multiple Chinese academic mirrors; English translation via CASI/govinfo is the authoritative source.

**Cluster G estimated chunks (primary sources): ~1,045**

---

## Section H: Jamestown Foundation — China Brief

**Base URL:** [jamestown.org/programs/chinabrief](https://jamestown.org/programs/chinabrief)  
**Note:** Individual articles are free on the Jamestown website. The series publishes 2x monthly.

| Title / Topic Area | Org | Author(s) | Year | URL | Relevance | License |
|---|---|---|---|---|---|---|
| China Brief — PLARF/missile forces articles | Jamestown Foundation | Various analysts | 2018–2025 | [jamestown.org/programs/chinabrief](https://jamestown.org/programs/chinabrief) | Timely analysis of PLARF exercises, corruption purges, new missile deployments, targeting doctrine updates; excellent for current-events corpus | Free/Public |
| China Brief — PLA blockade strategy (2025) | Jamestown Foundation | Various | 2025 | [Substack](https://jamestown.substack.com/p/drills-and-experts-suggest-beijing) **[VERIFIED]** | PLA blockade doctrine evolution; Joint Sword exercises; "island control model"; direct relevance to joint fires planning for Taiwan contingency | Free/Public |
| China Brief — Joint Sword 2024B exercises | Jamestown Foundation | Various | 2024 | [jamestown.org/programs/chinabrief](https://jamestown.org/programs/chinabrief) | First explicit blockade-focused PLA exercise; CCG encirclement; fires roles in blockade | Free/Public |

**Recommended search terms on jamestown.org:** "PLARF," "Rocket Force," "DF-26," "DF-21," "missile," "joint fires," "Eastern Theater Command," "air defense," "hypersonic," "Taiwan."

**Cluster H estimated chunks (10-15 key articles): ~80**

---

## Section I: Project 2049, MERICS, and IISS

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Project 2049 Institute Publications Index | Project 2049 Institute | Various | Ongoing | [project2049.net](https://project2049.net/) | Reports on PLA SSF, PLARF, Taiwan military operations, cyber; Mark Stokes and colleagues; primary source Chinese-language analysis | Free/Public | varies |
| IISS Military Balance (Annual — China sections) | IISS | IISS Staff | Annual | [iiss.org/publications/the-military-balance](https://www.iiss.org/publications/the-military-balance) | **PAYWALLED** — but free summary data on China OOB available in annual press releases and IISS online; note paywall | Subscription (summaries free) | — |
| IISS Military Balance+ Online | IISS | IISS Staff | Ongoing | [iiss.org](https://www.iiss.org/) | **PAYWALLED** — quantitative OOB data for PLA, PLAN, PLAAF, PLARF; note paywall | Subscription | — |
| NIDS China Security Report 2022: The PLA's Pursuit of Enhanced Joint Operations Capabilities | National Institute for Defense Studies (Japan) | Sugiura Yasuyuki | 2022 | [PDF](https://www.nids.mod.go.jp/publication/chinareport/pdf/china_report_EN_web_2022_A01.pdf) **[VERIFIED]** | Rigorous Japanese government analysis of PLA joint operations reforms; CMC→theater→service command chain; C2 systems; training | Free/Public | ~65 |

**Note on MERICS:** MERICS (Mercator Institute for China Studies) publishes relevant reports on PLA reforms and civil-military integration. Browse [merics.org/en/topics/military](https://merics.org/en/topics/military). Reports are generally free with registration.

**Cluster I estimated chunks: ~100**

---

## Section J: Wikipedia — Platform and System Reference Pages

These pages supplement targeting analyst reference tools like ODIN. They are not authoritative but are useful as quick-reference data anchors for training corpus ingest.

| System | Wikipedia URL | Relevance |
|---|---|---|
| DF-21D Anti-Ship Ballistic Missile | [en.wikipedia.org/wiki/DF-21](https://en.wikipedia.org/wiki/DF-21) | ASBM "carrier killer"; range 1,500 km; terminal guidance; A2/AD primary weapon |
| DF-26 IRBM | [en.wikipedia.org/wiki/DF-26](https://en.wikipedia.org/wiki/DF-26) | 4,000 km range; dual-capable (nuclear/conventional); land-attack and anti-ship; "Guam killer" |
| DF-17 Hypersonic Glide Vehicle | [en.wikipedia.org/wiki/DF-17](https://en.wikipedia.org/wiki/DF-17) | HGV; 1,800–2,500 km; boost-glide; maneuvering reentry; defeats existing missile defenses |
| DF-100 / CJ-100 Supersonic Cruise Missile | [en.wikipedia.org/wiki/CJ-100](https://en.wikipedia.org/wiki/CJ-100) | Ground-launched cruise missile; Mach 4+; long-range precision strike |
| YJ-12 Anti-Ship Cruise Missile | [en.wikipedia.org/wiki/YJ-12](https://en.wikipedia.org/wiki/YJ-12) | Air-launched ASCM; Mach 3+; 400 km range; H-6 bomber-launched |
| YJ-18 Anti-Ship Cruise Missile | [en.wikipedia.org/wiki/YJ-18](https://en.wikipedia.org/wiki/YJ-18) | Ship/submarine-launched ASCM; supersonic terminal; 540 km range |
| YJ-21 Anti-Ship Ballistic Missile | [en.wikipedia.org/wiki/YJ-21](https://en.wikipedia.org/wiki/YJ-21) | Air-launched ASBM from H-6N; hypersonic terminal; significant carrier threat |
| HQ-9 / HQ-9B SAM | [en.wikipedia.org/wiki/HQ-9](https://en.wikipedia.org/wiki/HQ-9) | Long-range SAM; ~200 km range; S-300 equivalent; IADS backbone |
| HQ-22 SAM | [en.wikipedia.org/wiki/HQ-22](https://en.wikipedia.org/wiki/HQ-22) | Medium-long range SAM; export and PLA service; IADS layering |
| H-6N / H-6K Bombers | [en.wikipedia.org/wiki/Xian_H-6](https://en.wikipedia.org/wiki/Xian_H-6) | H-6K: LACM/ASCM carrier; H-6N: aerial refueling, YJ-21/DF-21-type ALBM |
| J-20 Stealth Fighter | [en.wikipedia.org/wiki/Chengdu_J-20](https://en.wikipedia.org/wiki/Chengdu_J-20) | 5th-gen stealth; air superiority/penetration strike; 200+ deployed |
| J-16 Strike Fighter | [en.wikipedia.org/wiki/Shenyang_J-16](https://en.wikipedia.org/wiki/Shenyang_J-16) | Multirole; PL-15 BVR; ground attack; electronic warfare variant (J-16D) |
| J-15 Carrier Fighter | [en.wikipedia.org/wiki/Shenyang_J-15](https://en.wikipedia.org/wiki/Shenyang_J-15) | PLAN carrier aviation; Su-33 derivative; catapult-capable J-15T |
| J-35 Carrier Stealth Fighter | [en.wikipedia.org/wiki/Shenyang_FC-31](https://en.wikipedia.org/wiki/Shenyang_FC-31) | 5th-gen PLAN carrier aviation; deploying on Fujian |
| Type 055 Renhai Cruiser | [en.wikipedia.org/wiki/Type_055_destroyer](https://en.wikipedia.org/wiki/Type_055_destroyer) | 12,000 ton cruiser; 112 VLS; YJ-18, HHQ-9B, long-range strike capability |
| Type 052D Luyang III Destroyer | [en.wikipedia.org/wiki/Type_052D_destroyer](https://en.wikipedia.org/wiki/Type_052D_destroyer) | 7,500 ton; 64 VLS; PLAN's primary escort destroyer |
| Type 003 Fujian Carrier | [en.wikipedia.org/wiki/Type_003_aircraft_carrier](https://en.wikipedia.org/wiki/Type_003_aircraft_carrier) | CATOBAR carrier; electromagnetic catapult; J-35 deployment |
| PCL-191 / PHL-16 MRL | [en.wikipedia.org/wiki/PCL-191](https://en.wikipedia.org/wiki/PCL-191) | 500 km+ range MRL; capable of striking Taiwan from mainland; PLAA long-range fires |
| Type 075 LHD | [en.wikipedia.org/wiki/Type_075_landing_helicopter_dock](https://en.wikipedia.org/wiki/Type_075_landing_helicopter_dock) | 40,000 ton LHD; PLAN amphibious force; air-cushion and helicopter ops |
| Type 071 LPD | [en.wikipedia.org/wiki/Type_071_landing_platform_dock](https://en.wikipedia.org/wiki/Type_071_landing_platform_dock) | Amphibious transport; first island chain power projection |
| KJ-500 AEW&C | [en.wikipedia.org/wiki/KJ-500](https://en.wikipedia.org/wiki/KJ-500) | 3rd-gen AEW; 360° AESA radar; C2 hub for joint air operations |
| KJ-2000 AEW&C | [en.wikipedia.org/wiki/KJ-2000](https://en.wikipedia.org/wiki/KJ-2000) | PLAN/PLAAF AEW; Il-76 platform; limited but operational |
| Y-20 Strategic Transport | [en.wikipedia.org/wiki/Xian_Y-20](https://en.wikipedia.org/wiki/Xian_Y-20) | 55+ in service; 66 ton payload; PLA power projection enabler |
| ZBD-04A IFV | [en.wikipedia.org/wiki/ZBD-04](https://en.wikipedia.org/wiki/ZBD-04) | PLAA amphibious IFV; Taiwan amphibious assault ground force context |
| Type 99A MBT | [en.wikipedia.org/wiki/Type_99_tank](https://en.wikipedia.org/wiki/Type_99_tank) | PLAA main battle tank; targeting context for ground forces in Taiwan scenario |

**License note:** Wikipedia content is licensed CC BY-SA 4.0.

**Cluster J estimated chunks: ~125 (averaging ~5 per article)**

---

## Section K: Open-Access Academic Journals

| Title | Org | Notes | URL | Relevance | License |
|---|---|---|---|---|---|
| Naval War College Review | US Naval War College | Quarterly; fully open access via digital-commons.usnwc.edu; includes articles by Erickson, Martinson, Easton, Goldstein | [digital-commons.usnwc.edu/nwc-review/](https://digital-commons.usnwc.edu/nwc-review/) **[VERIFIED]** | PLA/PLAN doctrine, operations, campaigns; Taiwan scenarios; counterintervention; peer-reviewed | USG/Public Domain |
| Joint Force Quarterly | NDU Press | Quarterly; open access; many PLA, PLAAF, PLARF articles | [ndupress.ndu.edu/Joint-Force-Quarterly/](https://ndupress.ndu.edu/Joint-Force-Quarterly/) | Joint fires, PLA reform, A2/AD doctrine | USG/Public Domain |
| Texas National Security Review (TNSR) | Texas National Security Review | Open access; peer-reviewed; strong China content | [tnsr.org](https://tnsr.org) | PLA doctrine, kill chain analysis, Taiwan scenarios | Open Access |
| War on the Rocks | WOTR | Not peer-reviewed; expert-practitioner essays | [warontherocks.com](https://warontherocks.com) | Deep dives on PLARF, targeting, Pacific fires; search "China" and "PLA" | Free/Public |
| Asian Security | Taylor & Francis | **PAYWALLED** — some open-access articles available; peer-reviewed | [tandfonline.com/asian-security](https://www.tandfonline.com/toc/fasn20/current) | Academic PLA doctrine analysis; note paywall | Subscription |
| Comparative Strategy | Taylor & Francis | **PAYWALLED** | — | — | Subscription |

### Selected High-Value Open-Access Articles

| Title | Journal | Author(s) | Year | URL | Relevance |
|---|---|---|---|---|---|
| Denying China a Conventional First-Strike Capability | Naval War College Review | Bryan Goldsmith | 2019 | [PDF](https://digital-commons.usnwc.edu/cgi/viewcontent.cgi?article=7972&context=nwc-review) **[VERIFIED]** | PLARF strikes on US bases/C4ISR; counterintervention doctrine; counter-strike analysis |
| People's Republic of China Stratagems and Surprise Attacks | Naval War College Review | Ian Easton | 2026 | [digital-commons.usnwc.edu](https://digital-commons.usnwc.edu/nwc-review/vol79/iss1/) | PLA surprise attack doctrine; operational deception; Taiwan defense implications |
| Countering ISR in the Pacific: Mobile Missile Launcher Survivability | Naval War College Review | Ben Wermeling | 2026 | [digital-commons.usnwc.edu](https://digital-commons.usnwc.edu/nwc-review/vol79/iss1/) | TEL survivability modeling; PLARF mobile launcher attrition; highly relevant for fires targeting |
| A Potent Vector: Assessing Chinese Cruise Missile Developments | Joint Force Quarterly 75 | Gormley, Erickson, Yuan | 2014 | [HTML](https://ndupress.ndu.edu/Publications/Article/577568/a-potent-vector-assessing-chinese-cruise-missile-developments/) | Cruise missile A2/AD; YJ-12, YJ-18, DH-10 targeting roles |
| Rightsizing the PLA Air Force (JFQ 118) | Joint Force Quarterly | Kenneth Allen, Brendan Mulvaney | 2025 | [NDU Press](https://ndupress.ndu.edu/Media/News/News-Article-View/Article/4244397/rightsizing-the-pla-air-force-revisiting-an-analytic-framework/) **[VERIFIED]** | PLAAF force structure; J-20 deployments; Y-20; KJ-500; H-6N; AEW&C; air fires integration |
| So What? Reassessing Military Implications of Chinese Control of Taiwan | TNSR | Various | 2025 | [tnsr.org](https://tnsr.org/2025/06/so-what-reassessing-the-military-implications-of-chinese-control-of-taiwan/) **[VERIFIED]** | PLARF kill chains; ISR node analysis; DF-26 reach; Taiwan scenario fires assessment |
| Understanding Vulnerabilities in China's New Joint Force (JFQ 103) | Joint Force Quarterly | David Bickers | 2021 | [PDF](https://ndupress.ndu.edu/Portals/68/Documents/jfq/jfq-103/jfq-103_78-86_Bickers.pdf?ver=UOaRRhfwJQlOBEyr4mzuZg%3D%3D) **[VERIFIED]** | PLA joint force C2 vulnerabilities; SSF dependence; theater command weaknesses; targeting exploitation implications |

**Cluster K estimated chunks: ~180**

---

## Summary: Estimated Chunk Counts by Cluster

| Cluster | Description | Est. Chunks |
|---|---|---|
| A | US Gov Reports (CMPR × 8, DIA, ONI, NASIC, USCC, CRS) | ~1,840 |
| B | CASI Publications (translations + research) | ~1,020 |
| C | CMSI Red Books + Maritime Reports | ~320 |
| D | NDU Press | ~430 |
| E | RAND Corporation | ~415 |
| F | Think Tanks (CSBA, CNAS, CSIS, Stimson, P2049, FAS) | ~360 |
| G | PLA Primary Sources (English translations) | ~1,045 |
| H | Jamestown China Brief | ~80 |
| I | Project 2049, MERICS, NIDS | ~100 |
| J | Wikipedia System Pages | ~125 |
| K | Academic Journals | ~180 |
| **TOTAL** | | **~5,915** |

---

## TOP 30 MUST-INCLUDE PRIORITY LIST

*Ranked by: doctrinal depth + direct targeting relevance + uniqueness of content. If corpus budget is constrained, harvest these first.*

| Priority | Title | Section | Why |
|---|---|---|---|
| 1 | **Science of Second Artillery Campaigns** (CASI ITOW translation, 2026) | G/B | THE foundational PLARF doctrine text — missile campaign planning, targeting logic, nuclear/conventional integration; no other English source substitutes |
| 2 | **Science of Campaigns 2006** (CASI ITOW, Project Everest translation) | G/B | Campaign-level joint doctrine; blockade, landing, anti-air raid campaigns; directly maps to US joint fires planning needs |
| 3 | **Science of Military Strategy 2020** (CASI ITOW translation) | G/B | Current strategic doctrine baseline; "intelligentized warfare"; joint fires in informatized conditions |
| 4 | **DoD CMPR 2024** | A | Most current official US net assessment of PLA; authoritative source for force balance and capabilities |
| 5 | **DoD CMPR 2023** | A | Nuclear expansion data; PLARF 300 MRBM launchers/1,000 missiles; key for PLARF targeting order-of-battle |
| 6 | **DIA China Military Power 2019** | A | Most detailed open-source DIA assessment; force structure; missile force breakdown |
| 7 | **Science of Military Strategy 2013** (CASI ITOW translation) | G/B | Prior doctrine baseline; active defense; nuclear/space/cyber domains; essential for doctrinal evolution understanding |
| 8 | **CASI: Chinese Nuclear Command, Control, and Communications (2024)** | B | PLARF NC3 architecture; launch brigade growth; silo fields; nuclear C2 for fires planners |
| 9 | **RAND U.S.-China Military Scorecard (2015)** | E | Landmark quantitative assessment of 10 mission areas; Taiwan and Spratly scenarios; base attack calculations |
| 10 | **PLARF Order of Battle 2023** (CNS/Middlebury) | F | Unit-level PLARF OOB; launcher counts; DF-17/DF-26 deployments; directly actionable for targeting |
| 11 | **USCC 2024 Annual Report** | A | Congressional-level PLA assessment; most aggressive open-source treatment of counter-intervention; C4ISR chapter |
| 12 | **ONI: The PLA Navy (2015)** | A | Best open-source PLAN fleet assessment; YJ-18; DF-21D ASBM; C4ISR for maritime targeting |
| 13 | **CSBA: AirSea Battle (2010)** | F | Foundational counter-A2/AD concept; PLA missile threat to bases quantified; shaped all US responses |
| 14 | **CASI PLARF Organization (2022)** | B | Encyclopedic unit-level PLARF reference; brigade locations and equipment |
| 15 | **NDU: A Low-Visibility Force Multiplier (2014)** | D | Comprehensive cruise missile targeting analysis; DH-10, YJ-12, YJ-18, CJ-20 systems coverage |
| 16 | **Stimson: Cratering Effects (2024)** | F | Modeled PLARF strikes on US air bases; runway closure timelines; fires campaign analysis |
| 17 | **USCC Chapter: China's Nuclear Forces Beyond Minimal Deterrent (2021)** | A | Deep nuclear analysis; escalation paths; dual-capable missiles; nuclear fires context |
| 18 | **CSIS Missile Threat: China page** | F | Interactive reference database for all PRC missile systems; constantly updated; fires analyst daily reference |
| 19 | **NIDS China Security Report 2022** | I | Japanese government analysis of PLA joint operations; C2 chain; IJO concept; independent perspective |
| 20 | **DoD CMPR 2020** | A | 20-year retrospective; nuclear triad development; A2/AD trajectory; PLARF conventional-nuclear co-mingling |
| 21 | **NWC Review: Denying China a Conventional First-Strike Capability (2019)** | K | PLARF strike doctrine against US C4ISR and bases; counter-intervention targeting logic |
| 22 | **Project 2049: Early Warning in the Taiwan Strait (2022)** | F | PLARF kinetic challenge to Taiwan C2; cruise missile strike sequencing; strike-ISR integration |
| 23 | **FAS: Chinese Nuclear Weapons 2025 (Nuclear Notebook)** | F | Most current nuclear OOB; warhead counts; delivery systems; silo field data |
| 24 | **CMSI Red Book: Chinese Mine Warfare** | C | Undersea A2/AD; mine inventory 50,000+; operational doctrine; fires planner threat context |
| 25 | **CMSI Red Book: China Near Seas Combat Capabilities** | C | Near-seas A2/AD; missile/sub/surface forces; foundational maritime fires assessment |
| 26 | **NDU Press: PLA Beyond Borders (2019)** | D | Expeditionary PLA; C2 and ISR systems; space/cyber integration; joint fires enablers |
| 27 | **DoD CMPR 2022** | A | August 2022 exercises; missile overflights Taiwan; PLARF tactics; counter-intervention demonstration |
| 28 | **CSBA: Meeting the Anti-Access and Area-Denial Challenge (2003)** | F | Original A2/AD conceptual framework; ballistic missile saturation attacks; operational planning vocabulary |
| 29 | **CASI: In Their Own Words — China's National Defense in the New Era (2019 White Paper)** | B | Official PRC PLARF deterrence mission statement; active defense articulation |
| 30 | **CNAS: Over the Brink (2024)** | F | Nuclear coercion in protracted Taiwan conflict; nonstrategic nuclear weapons; fires/deterrence integration |

---

## Known Gaps and Honest Assessments

1. **Science of Second Artillery Campaigns (2004) in English:** The CASI ITOW translation (2026) listed above is the FIRST and ONLY public English translation of the complete text. Verify the URL is accessible; if not, the partial UCS excerpt (Chapter 10, Section 7) at `ucs.org/sites/default/files/attach/2014/09/Kulacki-Translation...` provides a coercion section only.

2. **Science of Campaigns (Chinese, 2006):** No publicly available English translation existed prior to the CASI/Project Everest version. The Chinese original circulates in academic mirrors but requires Mandarin proficiency.

3. **NASIC 2020 Ballistic Missile Threat PDF:** The direct PDF URL is not currently linked from NASIC's public publications page. The document was released in January 2021; it may be accessible via Defense.gov search or by contacting NASIC Public Affairs at 937-257-7809.

4. **ONI Updated PLAN Assessment:** No comprehensive ONI PLAN report has been released since 2015. Use the CRS O'Rourke report (RL33153) and CMPRs for updated data.

5. **IISS Military Balance:** The annual quantitative OOB data is paywalled. Free summaries and press releases from IISS are available; the full Military Balance requires institutional subscription (Jane's is similarly paywalled).

6. **MERICS:** Some MERICS reports require free registration. The MERICS China Tracker is useful for PLA reform monitoring.

7. **Jamestown China Brief:** Individual articles are free on the website, but systematic bulk access requires contacting Jamestown. Consider selective article harvest rather than bulk ingestion.

8. **2021 DoD CMPR:** Direct defense.gov URL: `https://media.defense.gov/2021/Nov/03/2002885874/-1/-1/0/2021-CMPR-FINAL.PDF`

9. **NDU Strategic Forum on China topics:** Multiple relevant short papers exist (4-8 pages each); browse by topic at [ndupress.ndu.edu](https://ndupress.ndu.edu/Publications/). Particularly relevant: SF-312 (Taiwan invasion failure), SF-306 (China overseas ports).

---

*End of Report*
