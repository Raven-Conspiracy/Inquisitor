# Kill-Chain Platforms, Sensors & Targeting Pods — Open-Source Reading List
## Joint Fires & Targeting Analyst Training Corpus

**Prepared for:** US Joint Fires & Targeting Analyst (131A + USAF/USN equivalents)
**Scope:** Unclassified, publicly accessible sources only — platform/sensor layer of the kill chain
**Purpose:** Third corpus pass; fills platform/sensor/targeting-pod layer for RAG ingestion
**Date compiled:** 2025
**Pass context:** Pass 1 = joint/service doctrine + curricula. Pass 2 = PLA/PLAN/PLARF reports & scholarly works. This pass (Pass 3) = platforms & sensors.

---

## Notes on Methodology

- URLs verified via `fetch_url` during research are marked **[VERIFIED]**. Approximately 30 URLs were spot-checked.
- Wikipedia is the primary source per user direction — CC BY-SA 4.0 license, comprehensive, frequently updated.
- Manufacturer public marketing pages used as secondary sources for specifications Wikipedia lacks.
- CSIS Missile Threat pages used for missile system data.
- No paywalled, registration-required, forum, or classified sources included.
- **Estimated chunk count** assumes ~800-token chunks for a standard RAG pipeline.
- All US Government materials are public domain per 17 U.S.C. § 105.

---

## Section A — US Air Platforms (Strike & Multi-role)

### A1 — Fifth-Generation Strike / Multi-role

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Lockheed Martin F-35 Lightning II | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Lockheed_Martin_F-35_Lightning_II](https://en.wikipedia.org/wiki/Lockheed_Martin_F-35_Lightning_II) **[VERIFIED]** | Comprehensive article on F-35A/B/C variants, EOTS, DAS, APG-81, stealth, multi-role mission sets; essential for understanding 5th-gen fires integration | Wikipedia (CC BY-SA 4.0) | ~15 |
| F-35 Lightning II (Lockheed Martin product page) | Lockheed Martin | Lockheed Martin | 2024 | [lockheedmartin.com/en-us/products/f-35.html](https://www.lockheedmartin.com/en-us/products/f-35.html) **[VERIFIED]** | Official manufacturer overview including avionics suite, sensor fusion, multi-role combat radius specs | Manufacturer (public marketing) | ~4 |
| Lockheed Martin F-22 Raptor | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Lockheed_Martin_F-22_Raptor](https://en.wikipedia.org/wiki/Lockheed_Martin_F-22_Raptor) **[VERIFIED]** | F-22 air superiority, AN/APG-77 AESA, LPI radar, internal weapons bays, DAS equivalent sensors, USAF combat employment | Wikipedia (CC BY-SA 4.0) | ~12 |
| F-15EX Eagle II | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_F-15EX_Eagle_II](https://en.wikipedia.org/wiki/Boeing_F-15EX_Eagle_II) | F-15EX, AN/APG-82 AESA, Eagle Passive/Active Warning Survivability System (EPAWSS), 29,500 lb payload capacity; key upgrade over F-15E | Wikipedia (CC BY-SA 4.0) | ~8 |
| McDonnell Douglas F-15E Strike Eagle | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/McDonnell_Douglas_F-15E_Strike_Eagle](https://en.wikipedia.org/wiki/McDonnell_Douglas_F-15E_Strike_Eagle) **[VERIFIED]** | F-15E deep strike, AN/APG-70/82, LANTIRN/Sniper pod integration, JDAM/GBU-28 carriage; primary USAF strike platform understanding | Wikipedia (CC BY-SA 4.0) | ~12 |
| General Dynamics F-16 Fighting Falcon | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon](https://en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon) | F-16C/D Block 70/72 (Viper), APG-83 SABR AESA, HMD/S, precision fires integration; mainstay of allied fire support and SEAD | Wikipedia (CC BY-SA 4.0) | ~15 |

**A1 subtotal: 6 sources, ~66 chunks**

---

### A2 — Naval Aviation Strike / Multi-role

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Boeing F/A-18E/F Super Hornet | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_F/A-18E/F_Super_Hornet](https://en.wikipedia.org/wiki/Boeing_F/A-18E/F_Super_Hornet) | F/A-18E/F strike, AN/APG-79 AESA, JHMCS, Lot 26 Block III (conformal fuel tanks, IRST21, advanced cockpit), CEC integration | Wikipedia (CC BY-SA 4.0) | ~12 |
| Boeing EA-18G Growler | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_EA-18G_Growler](https://en.wikipedia.org/wiki/Boeing_EA-18G_Growler) | Electronic attack platform, AN/ALQ-99/NGJ-MB pod, airborne electronic attack (AEA), SEAD/DEAD mission, kill chain EW layer | Wikipedia (CC BY-SA 4.0) | ~10 |
| McDonnell Douglas F/A-18 Hornet | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/McDonnell_Douglas_F/A-18_Hornet](https://en.wikipedia.org/wiki/McDonnell_Douglas_F/A-18_Hornet) | Legacy Hornet family context; A/B/C/D variants; allied operators (Canada, Australia, Finland, Switzerland) | Wikipedia (CC BY-SA 4.0) | ~12 |
| Grumman F-14 Tomcat | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Grumman_F-14_Tomcat](https://en.wikipedia.org/wiki/Grumman_F-14_Tomcat) | Historical naval strike context; Tomcat B/D strike role, LANTIRN pod, AIM-54 Phoenix beyond-visual-range; doctrinal baseline for carrier strike evolution | Wikipedia (CC BY-SA 4.0) | ~12 |
| BAE Systems AV-8B Harrier II | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/McDonnell_Douglas_AV-8B_Harrier_II](https://en.wikipedia.org/wiki/McDonnell_Douglas_AV-8B_Harrier_II) | USMC STOVL close air support, expeditionary fires, LITENING pod integration; legacy baseline for F-35B/EABO transition | Wikipedia (CC BY-SA 4.0) | ~10 |

**A2 subtotal: 5 sources, ~56 chunks**

---

### A3 — Strategic Bombers

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Northrop Grumman B-21 Raider | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Northrop_Grumman_B-21_Raider](https://en.wikipedia.org/wiki/Northrop_Grumman_B-21_Raider) **[VERIFIED]** | Next-generation stealth penetrating bomber; B61-12, LRSO carriage; replaces B-2; crucial for Pacific nuclear/conventional strike planning | Wikipedia (CC BY-SA 4.0) | ~8 |
| B-21 Raider (Northrop Grumman product page) | Northrop Grumman | Northrop Grumman | 2024 | [northropgrumman.com/what-we-do/air/b-21-raider/](https://www.northropgrumman.com/what-we-do/air/b-21-raider/) **[VERIFIED]** | Official manufacturer long-range strike overview; 6th-generation, penetrating ISR-strike, B61/LRSO carriage, production acceleration | Manufacturer (public marketing) | ~3 |
| Northrop Grumman B-2 Spirit | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Northrop_Grumman_B-2_Spirit](https://en.wikipedia.org/wiki/Northrop_Grumman_B-2_Spirit) | Flying wing stealth bomber; GBU-28/57 MOP; nuclear/conventional; low-observable penetration mission; Integrated Air Defense System (IADS) defeat | Wikipedia (CC BY-SA 4.0) | ~12 |
| Rockwell B-1 Lancer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Rockwell_B-1_Lancer](https://en.wikipedia.org/wiki/Rockwell_B-1_Lancer) | B-1B conventional standoff strike; JASSM-ER, LRASM, conventional rotary launcher (CRL); high-capacity internal carriage; Bone employment in maritime strike | Wikipedia (CC BY-SA 4.0) | ~12 |
| Boeing B-52 Stratofortress | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_B-52_Stratofortress](https://en.wikipedia.org/wiki/Boeing_B-52_Stratofortress) | B-52H with JASSM/LRASM, nuclear gravity bombs, standoff munitions; Commercial Engine Replacement Program (CERP); long-range maritime patrol/strike | Wikipedia (CC BY-SA 4.0) | ~15 |
| Lockheed F-117 Nighthawk | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Lockheed_F-117_Nighthawk](https://en.wikipedia.org/wiki/Lockheed_F-117_Nighthawk) | First operational stealth aircraft; historical baseline for penetrating precision strike; LO technology genesis; role in Desert Storm fires integration | Wikipedia (CC BY-SA 4.0) | ~10 |

**A3 subtotal: 6 sources, ~60 chunks**

---

### A4 — Special Operations / Close Air Support

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Lockheed AC-130J Ghostrider | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Lockheed_AC-130](https://en.wikipedia.org/wiki/Lockheed_AC-130) | AC-130J Ghostrider; 30mm, 105mm, precision strike package; SOF fires coordination; SOJTF/TACP integration; CAS for joint fires planners | Wikipedia (CC BY-SA 4.0) | ~12 |
| Fairchild Republic A-10 Thunderbolt II | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Fairchild_Republic_A-10_Thunderbolt_II](https://en.wikipedia.org/wiki/Fairchild_Republic_A-10_Thunderbolt_II) | A-10C CAS, GAU-8, Maverick, JDAM, LITENING/Sniper pod, survivability; JTAC-directed fires; USAF CAS mission planning baseline | Wikipedia (CC BY-SA 4.0) | ~12 |

**A4 subtotal: 2 sources, ~24 chunks**

**Section A total: 19 sources, ~206 chunks**

---

## Section B — US ISR / C2 / Tanker Platforms

### B1 — Strategic ISR

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Boeing RC-135 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_RC-135](https://en.wikipedia.org/wiki/Boeing_RC-135) **[VERIFIED]** | RC-135V/W Rivet Joint (SIGINT), RC-135S Cobra Ball (ballistic missile tracking), RC-135U Combat Sent (ELINT); 55th Wing; key ISR for kill chain cueing | Wikipedia (CC BY-SA 4.0) | ~12 |
| Lockheed U-2S | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Lockheed_U-2](https://en.wikipedia.org/wiki/Lockheed_U-2) | U-2S IMINT/SIGINT, SYERS-2 sensor, Senior Year electro-optical sensor; high-altitude strategic ISR for targeting | Wikipedia (CC BY-SA 4.0) | ~12 |
| Northrop Grumman RQ-4 Global Hawk | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Northrop_Grumman_RQ-4_Global_Hawk](https://en.wikipedia.org/wiki/Northrop_Grumman_RQ-4_Global_Hawk) **[VERIFIED]** | High-altitude, long-endurance UAS; EO/IR/SAR sensors; SIGINT variant (Block 40); persistent theater ISR; MQ-4C Triton maritime variant | Wikipedia (CC BY-SA 4.0) | ~10 |
| Lockheed RQ-170 Sentinel | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Lockheed_Martin_RQ-170_Sentinel](https://en.wikipedia.org/wiki/Lockheed_Martin_RQ-170_Sentinel) | Classified stealth UAS; public-domain details on LO design, forward-deployed ISR; USAF operational use over Afghanistan/Iran; kill chain overhead | Wikipedia (CC BY-SA 4.0) | ~6 |

**B1 subtotal: 4 sources, ~40 chunks**

---

### B2 — Theater/Operational ISR & MAOS

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| General Atomics MQ-9 Reaper | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/General_Atomics_MQ-9_Reaper](https://en.wikipedia.org/wiki/General_Atomics_MQ-9_Reaper) **[VERIFIED]** | MQ-9A/B multi-role UAS: Hellfire, GBU-12, SDB, Stinger; USAF/USN/USMC; CDE support; direct-action and ISR missions; kill chain execution | Wikipedia (CC BY-SA 4.0) | ~12 |
| General Atomics MQ-1C Gray Eagle | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/General_Atomics_MQ-1C_Gray_Eagle](https://en.wikipedia.org/wiki/General_Atomics_MQ-1C_Gray_Eagle) | US Army UAS; Hellfire, VIPER Strike, AN/ZPY-1 STARLite SAR; division-level ISR/attack; critical for Army fires kill chain | Wikipedia (CC BY-SA 4.0) | ~8 |
| Boeing MQ-25 Stingray | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_MQ-25_Stingray](https://en.wikipedia.org/wiki/Boeing_MQ-25_Stingray) | USN carrier-based tanker/ISR UAS; extends F/A-18E/F/F-35C combat radius; organic carrier tanking; enables long-range maritime strike | Wikipedia (CC BY-SA 4.0) | ~6 |

**B2 subtotal: 3 sources, ~26 chunks**

---

### B3 — Airborne Warning & Control / Battle Management

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Boeing E-3 Sentry (AWACS) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_E-3_Sentry](https://en.wikipedia.org/wiki/Boeing_E-3_Sentry) | E-3 AWACS; AN/APY-1/2 radar; NATO AWACS fleet; airspace management, track management, battle management; C2 for fires deconfliction | Wikipedia (CC BY-SA 4.0) | ~10 |
| Boeing E-7 Wedgetail | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_E-7](https://en.wikipedia.org/wiki/Boeing_E-7) | E-7A AEW&C (Australia/UK/USAF); MESA radar; AWACS replacement; advanced multi-role electronically scanned array; C2 node | Wikipedia (CC BY-SA 4.0) | ~8 |
| Northrop Grumman E-8 JSTARS | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Northrop_Grumman_E-8_Joint_STARS](https://en.wikipedia.org/wiki/Northrop_Grumman_E-8_Joint_STARS) | E-8C JSTARS; J/APY-3 MTI/SAR radar; ground moving target indicator; Army-Air Force fires integration; TITAN as replacement context | Wikipedia (CC BY-SA 4.0) | ~8 |
| Grumman E-2D Advanced Hawkeye | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Northrop_Grumman_E-2_Hawkeye](https://en.wikipedia.org/wiki/Northrop_Grumman_E-2_Hawkeye) | E-2D carrier-based AEW&C; AN/APY-9 UHF AESA; NIFC-CA node; Cooperative Engagement Capability uplink; naval fires command node | Wikipedia (CC BY-SA 4.0) | ~10 |
| Tactical Intelligence Targeting Access Node (TITAN) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Tactical_Intelligence_Targeting_Access_Node](https://en.wikipedia.org/wiki/Tactical_Intelligence_Targeting_Access_Node) | Army JSTARS ground replacement; space/air sensor processing; multi-domain targeting; TITAN as JSTARS/ABMS bridge for Army fires | Wikipedia (CC BY-SA 4.0) | ~5 |

**B3 subtotal: 5 sources, ~41 chunks**

---

### B4 — Maritime Patrol & Naval ISR

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Boeing P-8 Poseidon | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_P-8_Poseidon](https://en.wikipedia.org/wiki/Boeing_P-8_Poseidon) | P-8A ASW/ASUW; Harpoon, Mk-54 torpedo, sonobuoys, HAAS sensors; maritime kill chain; anti-submarine warfare targeting | Wikipedia (CC BY-SA 4.0) | ~10 |
| Sikorsky MH-60R Seahawk | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Sikorsky_MH-60R_Seahawk](https://en.wikipedia.org/wiki/Sikorsky_MH-60R_Seahawk) | MH-60R ASW/ASUW; APS-153 AESA radar, FLIR, sonobuoys, Hellfire/Penguin; ship-based kill chain execution | Wikipedia (CC BY-SA 4.0) | ~8 |

**B4 subtotal: 2 sources, ~18 chunks**

---

### B5 — Air Refueling

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Boeing KC-46 Pegasus | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_KC-46_Pegasus](https://en.wikipedia.org/wiki/Boeing_KC-46_Pegasus) | KC-46A tanker; remote vision system, boom/drogue, Advanced Aerial Refueling Boom; enables extended strike range; tanker force structure | Wikipedia (CC BY-SA 4.0) | ~10 |
| Boeing KC-135 Stratotanker | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_KC-135_Stratotanker](https://en.wikipedia.org/wiki/Boeing_KC-135_Stratotanker) | KC-135 backbone tanker; CFM56-powered R model; enables Pacific bomber operations; tanker-to-receiver pairing for strike planning | Wikipedia (CC BY-SA 4.0) | ~10 |
| McDonnell Douglas KC-10 Extender | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/McDonnell_Douglas_KC-10_Extender](https://en.wikipedia.org/wiki/McDonnell_Douglas_KC-10_Extender) | KC-10 large-capacity tanker/cargo; complementary to KC-135; retirement context for tanker force posture | Wikipedia (CC BY-SA 4.0) | ~8 |

**B5 subtotal: 3 sources, ~28 chunks**

**Section B total: 17 sources, ~153 chunks**

---

## Section C — US Targeting Pods & Airborne Sensors

### C1 — Targeting Pods

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AN/AAQ-33 Sniper Advanced Targeting Pod | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Sniper_Advanced_Targeting_Pod](https://en.wikipedia.org/wiki/Sniper_Advanced_Targeting_Pod) **[VERIFIED]** | Sniper ATP Gen I/II/III; LRIP Block 32, enhanced Sniper; two-color FLIR, HD-CCD, laser designator; F-15E/F-16/A-10C/B-52 integration; dominant USAF targeting pod | Wikipedia (CC BY-SA 4.0) | ~8 |
| LITENING Targeting Pod | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/LITENING](https://en.wikipedia.org/wiki/LITENING) | LITENING G4/G5; Rafael/Northrop Grumman; MW FLIR, CCD camera, laser rangefinder/designator; AV-8B/F-16/A-10/F-35B integration; USMC primary pod | Wikipedia (CC BY-SA 4.0) | ~6 |
| AN/AAQ-28 LITENING (Northrop Grumman product page) | Northrop Grumman | Northrop Grumman | 2024 | [northropgrumman.com/what-we-do/air/litening-targeting-pod/](https://www.northropgrumman.com/what-we-do/air/litening-targeting-pod/) | Manufacturer spec sheet: LITENING G5 dual-FOV FLIR, 1280x1080 CCD, laser spot tracker, range performance; pod weight/envelope data | Manufacturer (public marketing) | ~3 |
| AN/ASQ-228 ATFLIR (Advanced Targeting Forward-Looking Infrared) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/ASQ-228_ATFLIR](https://en.wikipedia.org/wiki/AN/ASQ-228_ATFLIR) | ATFLIR on F/A-18E/F/G; BAE Systems; wide-band sensor, targeting capability; USN primary targeting pod; replaces FLIR/TINS | Wikipedia (CC BY-SA 4.0) | ~5 |
| AN/AAS-44C(V) FLIR and Laser | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/AAS-44](https://en.wikipedia.org/wiki/AN/AAS-44) | Helicopter targeting system; MH-60R/S, AH-1Z; FLIR/laser for maritime and land attack targeting | Wikipedia (CC BY-SA 4.0) | ~4 |
| Raytheon MX-15 / MX-20 Electro-Optical System | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/MX-15](https://en.wikipedia.org/wiki/MX-15) | MX-15/MX-20 airborne EO/IR turrets; P-8A, Sentinel, ISR platforms; long-range MWIR/SWIR/LWIR; target acquisition at range | Wikipedia (CC BY-SA 4.0) | ~4 |

**C1 subtotal: 6 sources, ~30 chunks**

---

### C2 — Airborne Radar Systems

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AN/APG-81 (F-35 radar) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/APG-81](https://en.wikipedia.org/wiki/AN/APG-81) | Northrop Grumman AESA multifunction radar for F-35; synthetic aperture radar (SAR), ground moving target indicator (GMTI), air-to-air; LPI; 1,200+ T/R modules | Wikipedia (CC BY-SA 4.0) | ~6 |
| AN/APG-77 (F-22 radar) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/APG-77](https://en.wikipedia.org/wiki/AN/APG-77) | Northrop Grumman/Raytheon AESA for F-22; LPI operation; wide-bandwidth for SAR/GMTI; electronic attack; 5th-gen sensor baseline | Wikipedia (CC BY-SA 4.0) | ~5 |
| AN/APG-79 (Super Hornet radar) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/APG-79](https://en.wikipedia.org/wiki/AN/APG-79) | Raytheon AESA for F/A-18E/F Block II/III; simultaneous air-to-air and air-to-ground; DBS SAR mapping; critical for carrier air wing targeting | Wikipedia (CC BY-SA 4.0) | ~5 |
| AN/APG-82 AESA (F-15E/EX radar) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/APG-82](https://en.wikipedia.org/wiki/AN/APG-82) | Raytheon AESA for F-15E/EX; upgraded from APG-70; wide area surveillance, SAR, GMTI; high-resolution mapping for precision strike | Wikipedia (CC BY-SA 4.0) | ~5 |
| AN/APG-83 Scalable Agile Beam Radar (SABR) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/APG-83](https://en.wikipedia.org/wiki/AN/APG-83) | Northrop Grumman AESA for F-16V Block 70/72; SAR/GMTI; five modes vs three on AN/APG-68; allied F-16 fleet modernization | Wikipedia (CC BY-SA 4.0) | ~4 |

**C2 subtotal: 5 sources, ~25 chunks**

---

### C3 — F-35 Integrated Sensor Suite

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Electro-Optical Targeting System (EOTS) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Electro-Optical_Targeting_System](https://en.wikipedia.org/wiki/Electro-Optical_Targeting_System) | F-35 internal EOTS; Lockheed Martin; FLIR, laser designator/rangefinder; replaces external targeting pod; fused with DAS and radar | Wikipedia (CC BY-SA 4.0) | ~5 |
| AN/AAQ-37 Distributed Aperture System (DAS) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/AAQ-37](https://en.wikipedia.org/wiki/AN/AAQ-37) | F-35 360-degree passive sensor system; Northrop Grumman; missile warning, navigation, IRST function; revolutionary sensor fusion for 5th-gen | Wikipedia (CC BY-SA 4.0) | ~5 |

**C3 subtotal: 2 sources, ~10 chunks**

---

### C4 — Electronic Attack & Self-Protection Systems

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AN/ALQ-99 Tactical Jamming System | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/ALQ-99](https://en.wikipedia.org/wiki/AN/ALQ-99) | EA-18G legacy jamming system; multiple band coverage; airborne electronic attack in SEAD; being replaced by NGJ | Wikipedia (CC BY-SA 4.0) | ~6 |
| AN/ALQ-249 Next Generation Jammer (NGJ-MB) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/ALQ-249_Next_Generation_Jammer](https://en.wikipedia.org/wiki/AN/ALQ-249_Next_Generation_Jammer) | Raytheon NGJ-MB (mid-band) for EA-18G; active electronically scanned array jammer; DRFM-based; IOC 2029; EW modernization for kill chain protection | Wikipedia (CC BY-SA 4.0) | ~5 |

**C4 subtotal: 2 sources, ~11 chunks**

**Section C total: 15 sources, ~76 chunks**

---

## Section D — US Naval Surface Combatants & Strike Platforms

### D1 — Destroyers & Cruisers

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Arleigh Burke-class destroyer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Arleigh_Burke-class_destroyer](https://en.wikipedia.org/wiki/Arleigh_Burke-class_destroyer) **[VERIFIED]** | DDG Flight I/II/IIA/III; Aegis Baseline 9/10; AN/SPY-1D/SPY-6(V)1; VLS Mk-41; Tomahawk, SM-6, ESSM; primary USN surface fires platform | Wikipedia (CC BY-SA 4.0) | ~15 |
| Ticonderoga-class cruiser | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Ticonderoga-class_cruiser](https://en.wikipedia.org/wiki/Ticonderoga-class_cruiser) | CG-47 class; Aegis CMS Baseline 7; AN/SPY-1A/B; 122-cell Mk-41 VLS; Tomahawk LACM/TLAM, SM-2/3; phased retirement context | Wikipedia (CC BY-SA 4.0) | ~12 |
| Zumwalt-class destroyer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Zumwalt-class_destroyer](https://en.wikipedia.org/wiki/Zumwalt-class_destroyer) | DDG-1000; AMDR/AN/SPY-3; 80-cell VLS; Hypersonic Air Launched Offensive (HALO)/CPS conversion; land-attack destroyer concept evolution | Wikipedia (CC BY-SA 4.0) | ~10 |
| Constellation-class frigate | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Constellation-class_frigate](https://en.wikipedia.org/wiki/Constellation-class_frigate) | FFG(X); AN/SPY-6(V)3; 32-cell Mk-41 VLS; SM-6/ESSMBlock2/LRASM; future surface fires complement to DDG fleet | Wikipedia (CC BY-SA 4.0) | ~8 |

**D1 subtotal: 4 sources, ~45 chunks**

---

### D2 — Littoral Combat Ships

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Freedom-class littoral combat ship | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Freedom-class_littoral_combat_ship](https://en.wikipedia.org/wiki/Freedom-class_littoral_combat_ship) | LCS-1 class; surface warfare, mine countermeasure, ASW mission modules; Lockheed Martin; decommissioning context for fleet posture | Wikipedia (CC BY-SA 4.0) | ~8 |
| Independence-class littoral combat ship | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Independence-class_littoral_combat_ship](https://en.wikipedia.org/wiki/Independence-class_littoral_combat_ship) | LCS-2 trimaran; General Dynamics; SURFASS sonar, over-the-horizon Hellfire (LRASM integration studies), mine hunting; Pacific theater relevance | Wikipedia (CC BY-SA 4.0) | ~8 |

**D2 subtotal: 2 sources, ~16 chunks**

---

### D3 — Submarines

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Virginia-class submarine | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Virginia-class_submarine](https://en.wikipedia.org/wiki/Virginia-class_submarine) **[VERIFIED]** | SSN-774 attack submarine; Block V Virginia Payload Module (VPM) adds 40 Tomahawk; Mk-48 ADCAP; covert strike from subsurface kill chain | Wikipedia (CC BY-SA 4.0) | ~12 |
| Ohio-class submarine | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Ohio-class_submarine](https://en.wikipedia.org/wiki/Ohio-class_submarine) | SSBN/SSGN; converted SSGNs carry 154 Tomahawk + SDV/SEAL delivery; SSBN nuclear triad leg; OPLANS and nuclear fires | Wikipedia (CC BY-SA 4.0) | ~12 |
| Columbia-class submarine | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Columbia-class_submarine](https://en.wikipedia.org/wiki/Columbia-class_submarine) | SSBN-826 next-generation SSBN; life-of-core reactor; D5LE2 Trident II; nuclear deterrence; replaces Ohio SSBN from 2031 | Wikipedia (CC BY-SA 4.0) | ~8 |

**D3 subtotal: 3 sources, ~32 chunks**

---

### D4 — Aircraft Carriers & Amphibious Ships

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Gerald R. Ford-class aircraft carrier | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Gerald_R._Ford-class_aircraft_carrier](https://en.wikipedia.org/wiki/Gerald_R._Ford-class_aircraft_carrier) | CVN-78; EMALS, AAG, AN/SPY-3/6; 75+ aircraft; Dual Band Radar; CEC; primary carrier strike group (CSG) nucleus | Wikipedia (CC BY-SA 4.0) | ~12 |
| Nimitz-class aircraft carrier | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Nimitz-class_aircraft_carrier](https://en.wikipedia.org/wiki/Nimitz-class_aircraft_carrier) | CVN-68 class; AN/SPY-3; 10 ships; current operational backbone of CSG; strike wing package for Pacific fires | Wikipedia (CC BY-SA 4.0) | ~12 |
| America-class amphibious assault ship | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/America-class_amphibious_assault_ship](https://en.wikipedia.org/wiki/America-class_amphibious_assault_ship) | LHA-6/7 (aviation-centric); F-35B, MV-22, AH-1Z; Amphibious Ready Group (ARG); Marine fires platform for EABO | Wikipedia (CC BY-SA 4.0) | ~8 |
| Wasp-class amphibious assault ship | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Wasp-class_amphibious_assault_ship](https://en.wikipedia.org/wiki/Wasp-class_amphibious_assault_ship) | LHD-1 class; F-35B capable (modified decks); LCAC, LCU, CH-53; ARG/MEU fires node; decommissioning context | Wikipedia (CC BY-SA 4.0) | ~8 |
| San Antonio-class amphibious transport dock | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/San_Antonio-class_amphibious_transport_dock](https://en.wikipedia.org/wiki/San_Antonio-class_amphibious_transport_dock) | LPD-17; AN/SPS-73; Mk-46 30mm; LCAC; forcible entry fires integration; Expeditionary Strike Group (ESG) component | Wikipedia (CC BY-SA 4.0) | ~8 |
| Expeditionary Sea Base | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Expeditionary_Sea_Base](https://en.wikipedia.org/wiki/Expeditionary_Sea_Base) | ESB-class; forward logistics/SOF; MH-60S/MQ-8; Distributed Maritime Operations (DMO) support node; enables Pacific EABO fires | Wikipedia (CC BY-SA 4.0) | ~6 |

**D4 subtotal: 6 sources, ~54 chunks**

---

### D5 — Combat Systems & Strike Weapons

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Aegis Combat System | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Aegis_Combat_System](https://en.wikipedia.org/wiki/Aegis_Combat_System) **[VERIFIED]** | Baseline 9/10/CU; command and decision (C&D); engage-on-remote (EOR); Aegis BMD; C2 architecture for surface fires | Wikipedia (CC BY-SA 4.0) | ~12 |
| AN/SPY-1 radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/SPY-1](https://en.wikipedia.org/wiki/AN/SPY-1) | Phased array S-band radar for Aegis; SPY-1A/B/D(V); track-while-scan; 100+ simultaneous tracks; air/surface/sub-surface cuing | Wikipedia (CC BY-SA 4.0) | ~8 |
| AN/SPY-6 Air and Missile Defense Radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/SPY-6](https://en.wikipedia.org/wiki/AN/SPY-6) | Raytheon S-band AESA; DDG Flight III; 35× sensitivity gain over SPY-1D; volume search, BMD, terminal mode; critical for IAMD fires | Wikipedia (CC BY-SA 4.0) | ~6 |
| Cooperative Engagement Capability (CEC) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Cooperative_Engagement_Capability](https://en.wikipedia.org/wiki/Cooperative_Engagement_Capability) | CEC/NIFC-CA network; distributed netted fire control; engage-on-remote; allows E-2D to cue SM-6 from DDG/CG; joint fires integration | Wikipedia (CC BY-SA 4.0) | ~6 |
| Tomahawk cruise missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Tomahawk_cruise_missile](https://en.wikipedia.org/wiki/Tomahawk_cruise_missile) **[VERIFIED]** | BGM-109 TLAM; Block IV/V/Va/Vb; DSMAC, GPS, INS; 1,000 nm range; anti-ship Tomahawk (Block Va); subsurface and surface launch | Wikipedia (CC BY-SA 4.0) | ~12 |
| Mk 41 Vertical Launching System | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Mk_41_Vertical_Launching_System](https://en.wikipedia.org/wiki/Mk_41_Vertical_Launching_System) | Strike-length/tactical-length VLS; SM-2/3/6, Tomahawk, ASROC, ESSM; universal surface fires launcher; allied interoperability | Wikipedia (CC BY-SA 4.0) | ~8 |

**D5 subtotal: 6 sources, ~52 chunks**

**Section D total: 21 sources, ~199 chunks**

---

## Section E — US Army Fires Platforms & Sensors

### E1 — Cannon Artillery

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| M109 Paladin | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/M109_howitzer](https://en.wikipedia.org/wiki/M109_howitzer) | M109A7 Paladin; 155mm/39-cal; Paladin Integrated Management (PIM); IFCS; digital fires integration with AFATDS; self-propelled howitzer | Wikipedia (CC BY-SA 4.0) | ~10 |
| M777 howitzer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/M777_howitzer](https://en.wikipedia.org/wiki/M777_howitzer) | Ultralight 155mm towed; CH-47/C-130 transportable; Excalibur GPS-guided round; AFATDS integration; Marine and Army artillery | Wikipedia (CC BY-SA 4.0) | ~8 |

**E1 subtotal: 2 sources, ~18 chunks**

---

### E2 — Rocket Artillery & Missiles

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| M142 HIMARS | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/M142_HIMARS](https://en.wikipedia.org/wiki/M142_HIMARS) **[VERIFIED]** | High Mobility Artillery Rocket System; GMLRS, ATACMS, PrSM; single-pod launcher on FMTV; C-130 deployable; foundational for joint fires deep strike | Wikipedia (CC BY-SA 4.0) | ~10 |
| M270 MLRS | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/M270_Multiple_Launch_Rocket_System](https://en.wikipedia.org/wiki/M270_Multiple_Launch_Rocket_System) | M270A2 MLRS; dual-pod launcher; GMLRS, ATACMS, M30/31; Bradley chassis; Army and allied rocket fires | Wikipedia (CC BY-SA 4.0) | ~10 |
| MGM-140 ATACMS | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/MGM-140_ATACMS](https://en.wikipedia.org/wiki/MGM-140_ATACMS) | Army Tactical Missile System; Block I/IA/II; 300 km max (Block IA); GPS/INS; suppression of enemy air defenses (SEAD) and deep fires; Ukraine employment | Wikipedia (CC BY-SA 4.0) | ~8 |
| Precision Strike Missile (PrSM) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Precision_Strike_Missile](https://en.wikipedia.org/wiki/Precision_Strike_Missile) **[VERIFIED]** | PrSM Increment 1/2/3/4/5; 500+ km range; anti-ship seeker (Increment 2); HIMARS/MLRS compatible; ATACMS replacement; future deep fires | Wikipedia (CC BY-SA 4.0) | ~6 |
| Mid-Range Capability (Typhon) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Mid-Range_Capability](https://en.wikipedia.org/wiki/Mid-Range_Capability) | Typhon ground-based Tomahawk/SM-6 launcher; Army LRPF; deployed to Philippines 2024; key for Pacific A2/AD counter-fires | Wikipedia (CC BY-SA 4.0) | ~5 |
| Long Range Hypersonic Weapon (Dark Eagle) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Long_Range_Hypersonic_Weapon](https://en.wikipedia.org/wiki/Long_Range_Hypersonic_Weapon) | LRHW/Dark Eagle; Common Hypersonic Glide Body (C-HGB); Mach 17+; 2,775+ km range; first Army strategic fires capability | Wikipedia (CC BY-SA 4.0) | ~5 |
| Guided Multiple Launch Rocket System (GMLRS) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Guided_Multiple_Launch_Rocket_System](https://en.wikipedia.org/wiki/Guided_Multiple_Launch_Rocket_System) | M30/M31 GMLRS; 84 km range; GPS/INS; unitary/alternative warhead (M30A1 DPICM-like); dominant deep fires munition for 131A planners | Wikipedia (CC BY-SA 4.0) | ~6 |

**E2 subtotal: 7 sources, ~50 chunks**

---

### E3 — Counterfire & Target Acquisition Radars

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AN/TPQ-36 Firefinder | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/TPQ-36_Firefinder_radar](https://en.wikipedia.org/wiki/AN/TPQ-36_Firefinder_radar) | Mortar/rocket tracking counterfire radar; AN/TPQ-36/37 family; short-range mortar finding; AFATDS cueing for counterfire mission | Wikipedia (CC BY-SA 4.0) | ~5 |
| AN/TPQ-53 Firefinder | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/TPQ-53](https://en.wikipedia.org/wiki/AN/TPQ-53) | Q-53 Firefinder; 360° search; replaces TPQ-36/37; range up to 60 km for rockets; primary counterfire radar for BCT fires cells | Wikipedia (CC BY-SA 4.0) | ~5 |
| AN/TPQ-50 (Q-50 LCMR) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/TPQ-50](https://en.wikipedia.org/wiki/AN/TPQ-50) | Lightweight Counter-Mortar Radar; vehicle-mountable; complements Q-53 at smaller unit level; locate-and-report for fires | Wikipedia (CC BY-SA 4.0) | ~4 |

**E3 subtotal: 3 sources, ~14 chunks**

---

### E4 — Forward Observer / Laser Designation

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AN/PED-1 Lightweight Laser Designator Rangefinder (LLDR) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/PED-1_LLDR](https://en.wikipedia.org/wiki/AN/PED-1_LLDR) | Ground designator for laser-guided munitions; LLDR 2H with GLLD; JTAC/FO tool for terminal guidance of Copperhead/Excalibur/LGB | Wikipedia (CC BY-SA 4.0) | ~4 |
| Joint Effects Targeting System (JETS) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Joint_Effects_Targeting_System](https://en.wikipedia.org/wiki/Joint_Effects_Targeting_System) | AN/PSG-19 JETS; FO/JTAC individual targeting device; laser range-finder, GPS, digital data; replaces MFDS/PLGR for fires | Wikipedia (CC BY-SA 4.0) | ~3 |

**E4 subtotal: 2 sources, ~7 chunks**

---

### E5 — Army UAS

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AAI RQ-7 Shadow | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AAI_RQ-7_Shadow](https://en.wikipedia.org/wiki/AAI_RQ-7_Shadow) | Brigade-level tactical UAS; EO/IR, laser designator; TCDL link; fire support team (FIST) ISR tool; Army BCT fires integration | Wikipedia (CC BY-SA 4.0) | ~6 |
| Boeing Insitu RQ-21A Blackjack | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_Insitu_RQ-21_Blackjack](https://en.wikipedia.org/wiki/Boeing_Insitu_RQ-21_Blackjack) | Small tactical UAS; STUAS; Navy/Marine/Army; EO/IR, SIGINT; catapult launch/net recovery; shipboard and expeditionary fires ISR | Wikipedia (CC BY-SA 4.0) | ~5 |

**E5 subtotal: 2 sources, ~11 chunks**

**Section E total: 16 sources, ~100 chunks**

---

## Section F — US Marine Fires Platforms & Sensors

### F1 — Marine Ground Fires

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| M777 howitzer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/M777_howitzer](https://en.wikipedia.org/wiki/M777_howitzer) | [See Section E1 — same entry; USMC is primary operator] | Wikipedia (CC BY-SA 4.0) | ~8 |
| M142 HIMARS (USMC) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/M142_HIMARS](https://en.wikipedia.org/wiki/M142_HIMARS) | [See Section E2 — USMC HIMARS batteries; key for EABO/MLR fires concept] | Wikipedia (CC BY-SA 4.0) | ~10 |

**F1 subtotal: 2 sources (cross-referenced), ~18 chunks**

---

### F2 — Marine Anti-Ship & Coastal Defense

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Naval Strike Missile / NMESIS | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Naval_Strike_Missile](https://en.wikipedia.org/wiki/Naval_Strike_Missile) **[VERIFIED]** | NSM/RGM-184A; NMESIS (Navy Marine Expeditionary Ship Interdiction System) on JLTV; Kongsberg/Raytheon; maritime strike from shore; EABO fires node | Wikipedia (CC BY-SA 4.0) | ~8 |

**F2 subtotal: 1 source, ~8 chunks**

---

### F3 — Marine Radar & Sensors

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| AN/TPS-80 G/ATOR | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AN/TPS-80](https://en.wikipedia.org/wiki/AN/TPS-80) | Ground/Air Task Oriented Radar; USMC air traffic control + counter-UAS + air defense; S-band AESA; replaces multiple radars; expeditionary fires cueing | Wikipedia (CC BY-SA 4.0) | ~5 |

**F3 subtotal: 1 source, ~5 chunks**

---

### F4 — Marine Aviation (Fires-Relevant)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Lockheed Martin F-35B | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Lockheed_Martin_F-35_Lightning_II](https://en.wikipedia.org/wiki/Lockheed_Martin_F-35_Lightning_II) | [See Section A1 — F-35B STOVL variant; primary Marine CAS/strike; EABO deck-based fires] | Wikipedia (CC BY-SA 4.0) | ~15 |
| Bell Boeing MV-22 Osprey | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Bell_Boeing_V-22_Osprey](https://en.wikipedia.org/wiki/Bell_Boeing_V-22_Osprey) | MV-22B tiltrotor; EABO logistics/assault; AN/APQ-186 terrain-following radar; MAGTF fires enabling; range extends Marine strike reach | Wikipedia (CC BY-SA 4.0) | ~10 |
| General Atomics MQ-9A Reaper (USMC) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/General_Atomics_MQ-9_Reaper](https://en.wikipedia.org/wiki/General_Atomics_MQ-9_Reaper) | [See Section B2 — USMC Group 5 UAS; ISR + fires for MEF] | Wikipedia (CC BY-SA 4.0) | ~12 |

**F4 subtotal: 3 sources (cross-referenced), ~37 chunks**

**Section F total: 7 distinct sources, ~68 chunks**

---

## Section G — Allied / Partner Platforms (Pacific & European Focus)

### G1 — Japan (JSDF)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Mitsubishi F-15J Eagle | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Mitsubishi_F-15J](https://en.wikipedia.org/wiki/Mitsubishi_F-15J) | JASDF F-15J/DJ; MSIP upgrades; Air Self-Defense Force air superiority baseline; interoperability with USAF for Pacific contingencies | Wikipedia (CC BY-SA 4.0) | ~8 |
| Mitsubishi F-2 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Mitsubishi_F-2](https://en.wikipedia.org/wiki/Mitsubishi_F-2) | JASDF F-2 strike fighter; J/APG-1 AESA; ASM-2 anti-ship missile; close air support and maritime strike; F-16 derivative with AESA | Wikipedia (CC BY-SA 4.0) | ~8 |
| Kawasaki P-1 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Kawasaki_P-1](https://en.wikipedia.org/wiki/Kawasaki_P-1) | JMSDF maritime patrol; J/APS-1 AESA radar; domestically developed P-3C replacement; anti-submarine and anti-ship targeting | Wikipedia (CC BY-SA 4.0) | ~6 |
| Boeing E-767 AWACS | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_E-767](https://en.wikipedia.org/wiki/Boeing_E-767) | JASDF AEW&C; AN/APY-2 radar on 767 airframe; Japan's airspace battle management; interoperable with US AWACS C2 | Wikipedia (CC BY-SA 4.0) | ~5 |
| Type 12 Surface-to-Ship Missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_12_surface-to-ship_missile](https://en.wikipedia.org/wiki/Type_12_surface-to-ship_missile) | JGSDF/JMSDF coastal defense; 200 km range (extended version 1,000+ km); key Pacific maritime fires system; counter-PLAN | Wikipedia (CC BY-SA 4.0) | ~5 |
| Maya-class destroyer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Maya-class_destroyer](https://en.wikipedia.org/wiki/Maya-class_destroyer) | JMSDF Aegis-equipped DDG; AN/SPY-1D(V); BMD-capable (SM-3 Block IIA); CEC interoperability; NATO/US naval fires integration | Wikipedia (CC BY-SA 4.0) | ~6 |

**G1 subtotal: 6 sources, ~38 chunks**

---

### G2 — South Korea (ROK)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Korean Aerospace Industries KF-21 Boramae | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/KAI_KF-21_Boramae](https://en.wikipedia.org/wiki/KAI_KF-21_Boramae) | ROKAF 4.5-gen indigenous fighter; AESA radar; IRIS-T, AIM-120; Meteor integration planned; key allied capability development | Wikipedia (CC BY-SA 4.0) | ~8 |
| Hyunmoo ballistic missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Hyunmoo_(missile)](https://en.wikipedia.org/wiki/Hyunmoo_(missile)) | ROK ballistic missile family; Hyunmoo-2/3/4/5; 800+ km range (Hyunmoo-4); deep fires against DPRK/secondary adversaries | Wikipedia (CC BY-SA 4.0) | ~6 |
| Sejong the Great-class destroyer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Sejong_the_Great-class_destroyer](https://en.wikipedia.org/wiki/Sejong_the_Great-class_destroyer) | ROKN Aegis DDG; AN/SPY-1D; 128-cell VLS; SM-2/6, Hyunmoo-3; most capable non-US Aegis DDG; IAMD fires | Wikipedia (CC BY-SA 4.0) | ~6 |
| Boeing F-15K Slam Eagle | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_F-15K_Slam_Eagle](https://en.wikipedia.org/wiki/Boeing_F-15K_Slam_Eagle) | ROKAF F-15K; APG-63(V)1; SLAM-ER, Harpoon, JDAM; long-range strike against DPRK hard/buried targets; highest-spec F-15 export | Wikipedia (CC BY-SA 4.0) | ~6 |

**G2 subtotal: 4 sources, ~26 chunks**

---

### G3 — Australia (ADF)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Boeing E-7A Wedgetail (Australia) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Boeing_E-7](https://en.wikipedia.org/wiki/Boeing_E-7) | RAAF AEW&C lead operator; MESA radar; networked battle management; model for UK and USAF E-7 adoption; 5 airframes | Wikipedia (CC BY-SA 4.0) | ~8 |
| Hobart-class destroyer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Hobart-class_destroyer](https://en.wikipedia.org/wiki/Hobart-class_destroyer) | RAN DDG; AN/SPY-1D(V); Mk-41 VLS; SM-2/ESSM; aligned Aegis for coalition fires integration with USN | Wikipedia (CC BY-SA 4.0) | ~6 |
| Northrop Grumman MQ-4C Triton (Australia) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Northrop_Grumman_MQ-4C_Triton](https://en.wikipedia.org/wiki/Northrop_Grumman_MQ-4C_Triton) | RAAF/USN maritime ISR UAS; BAMS-D; 360° multi-sensor; Pacific-wide surveillance; kill chain maritime cueing | Wikipedia (CC BY-SA 4.0) | ~6 |

**G3 subtotal: 3 sources, ~20 chunks**

---

### G4 — United Kingdom (RAF/RN)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Eurofighter Typhoon FGR4 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Eurofighter_Typhoon](https://en.wikipedia.org/wiki/Eurofighter_Typhoon) | RAF Typhoon FGR4; CAPTOR-E AESA (Phase 3); Storm Shadow/Brimstone/Meteor; ECRS Mk2 jammer; NATO interoperability fires | Wikipedia (CC BY-SA 4.0) | ~15 |
| BAE Systems Astute-class submarine | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Astute-class_submarine](https://en.wikipedia.org/wiki/Astute-class_submarine) | RN SSN; Tomahawk Block IV/V; Spearfish torpedo; silent deep strike from subsurface; AUKUS context; 7 planned | Wikipedia (CC BY-SA 4.0) | ~8 |
| Daring-class destroyer (Type 45) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Daring-class_destroyer](https://en.wikipedia.org/wiki/Daring-class_destroyer) | RN Type 45 AAW destroyer; SAMPSON AESA + PAAMS (Aster 15/30); outstanding area air defense; NATO task force fires protection | Wikipedia (CC BY-SA 4.0) | ~8 |

**G4 subtotal: 3 sources, ~31 chunks**

---

### G5 — NATO European Allies

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Dassault Rafale | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Dassault_Rafale](https://en.wikipedia.org/wiki/Dassault_Rafale) | French/allied multirole; RBE2-AA AESA; SCALP-EG/ASMP-A nuclear carriage; SPECTRA EW suite; F3-R standard; coalition fires | Wikipedia (CC BY-SA 4.0) | ~12 |
| Saab JAS 39 Gripen | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Saab_JAS_39_Gripen](https://en.wikipedia.org/wiki/Saab_JAS_39_Gripen) | Swedish/NATO partner; Gripen E/F; ES-05 Raven AESA; Meteor, KEPD-350; deployed by 11 nations; agile base operations | Wikipedia (CC BY-SA 4.0) | ~10 |
| Panavia Tornado | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Panavia_Tornado](https://en.wikipedia.org/wiki/Panavia_Tornado) | Tornado IDS (GR4/ECR) legacy; Storm Shadow/HARM; Germany/Italy/Saudi operator; foundational NATO dual-capable fires aircraft baseline | Wikipedia (CC BY-SA 4.0) | ~10 |
| NATO Airborne Early Warning Force (E-3) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/NATO_Airborne_Early_Warning%26Control_Force](https://en.wikipedia.org/wiki/NATO_Airborne_Early_Warning%26Control_Force) | NATO E-3 Sentry fleet (17 aircraft); airspace battle management; fires deconfliction for multi-national operations | Wikipedia (CC BY-SA 4.0) | ~6 |

**G5 subtotal: 4 sources, ~38 chunks**

---

### G6 — Taiwan (ROC Armed Forces)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| General Dynamics F-16V Viper (Taiwan) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon](https://en.wikipedia.org/wiki/General_Dynamics_F-16_Fighting_Falcon) | ROCAF F-16V (Block 70 equivalent); AN/APG-83 SABR; AIM-120C/D; IDF integration; Taiwan strait air superiority | Wikipedia (CC BY-SA 4.0) | ~15 |
| AIDC F-CK-1 Ching-kuo | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/AIDC_F-CK-1_Ching-kuo](https://en.wikipedia.org/wiki/AIDC_F-CK-1_Ching-kuo) | ROCAF indigenous defense fighter; GD-53 radar; TC-2 AAM; Wan Chien cruise missile; homeland defense fires | Wikipedia (CC BY-SA 4.0) | ~6 |
| Hsiung Feng II/III anti-ship missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Hsiung_Feng_III](https://en.wikipedia.org/wiki/Hsiung_Feng_III) | ROCN ramjet supersonic AShM; Mach 2.0+; shore-based and ship-launched; maritime fires against PLAN amphibious forces | Wikipedia (CC BY-SA 4.0) | ~5 |
| Tien Kung III surface-to-air missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Tien_Kung_III](https://en.wikipedia.org/wiki/Tien_Kung_III) | Taiwan indigenous SAM; patriot-class performance; BMD capable; IADS component; Taiwan integrated air defense fires | Wikipedia (CC BY-SA 4.0) | ~5 |

**G6 subtotal: 4 sources, ~31 chunks**

**Section G total: 24 sources, ~184 chunks**

---

## Section H — PLA Air Platforms

### H1 — Fifth-Generation / Stealth

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Chengdu J-20 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Chengdu_J-20](https://en.wikipedia.org/wiki/Chengdu_J-20) **[VERIFIED]** | J-20A/S (two-seat); WS-10C/WS-15 engines; LO design; PL-15/PL-21 BVR; WS-15 thrust vectoring; PLAAF primary 5th-gen fighter | Wikipedia (CC BY-SA 4.0) | ~12 |
| Shenyang FC-31 / J-35 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shenyang_FC-31](https://en.wikipedia.org/wiki/Shenyang_FC-31) | FC-31/J-35A; carrier-based 5th-gen (J-35 for PLAN); rival to J-20; dual-internal bays; KLJ-7A candidate; carrier strike group threat | Wikipedia (CC BY-SA 4.0) | ~8 |

**H1 subtotal: 2 sources, ~20 chunks**

---

### H2 — Fourth/4.5-Generation Strike

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Shenyang J-16 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shenyang_J-16](https://en.wikipedia.org/wiki/Shenyang_J-16) **[VERIFIED]** | J-16 multirole strike; KLJ-7A AESA; 12 hardpoints; YJ-12, KD-88; J-16D electronic warfare variant (SEAD/EW); 330+ in service | Wikipedia (CC BY-SA 4.0) | ~10 |
| Shenyang J-11 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shenyang_J-11](https://en.wikipedia.org/wiki/Shenyang_J-11) | Su-27SK reverse-engineered; J-11B/BS/BH; N001VE radar; PL-8/PL-12; PLAAF primary air superiority fighter (Su-27 family) | Wikipedia (CC BY-SA 4.0) | ~8 |
| Chengdu J-10C | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Chengdu_J-10](https://en.wikipedia.org/wiki/Chengdu_J-10) | J-10C AESA variant; LRIP KLJ-7A; PL-15 AAM capable; TVC thrust vectoring; PLAAF medium fighter backbone upgrade | Wikipedia (CC BY-SA 4.0) | ~8 |
| Shenyang J-15 (carrier-based) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shenyang_J-15](https://en.wikipedia.org/wiki/Shenyang_J-15) | J-15/J-15T (catapult); PLAN carrier aviation strike; YJ-12 AShM carriage; Type 002/003 carrier air wing threat | Wikipedia (CC BY-SA 4.0) | ~8 |
| Xian JH-7A FBC-1 Flying Leopard | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Xian_JH-7](https://en.wikipedia.org/wiki/Xian_JH-7) | JH-7A maritime strike; YJ-91 anti-radiation/YJ-83 AShM; PLAN/PLAAF maritime attack; replacing J-8; aging strike role | Wikipedia (CC BY-SA 4.0) | ~6 |
| Shenyang J-8 Finback | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shenyang_J-8](https://en.wikipedia.org/wiki/Shenyang_J-8) | J-8II/IIF interceptor; radar-guided AAMs; declining but still in limited PLAAF service; historical threat baseline | Wikipedia (CC BY-SA 4.0) | ~6 |

**H2 subtotal: 6 sources, ~46 chunks**

---

### H3 — Strategic Bombers & Drones

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Xi'an H-6 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Xian_H-6](https://en.wikipedia.org/wiki/Xian_H-6) **[VERIFIED]** | H-6K/N/J variants; CJ-20/DF-21D standoff carriage (H-6K/N); aerial refueling (H-6N); 3,000+ km combat radius; PLARF/PLAAF dual-use | Wikipedia (CC BY-SA 4.0) | ~12 |
| CASC Rainbow CH-5 / GJ-11 Sharp Sword | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/GJ-11](https://en.wikipedia.org/wiki/GJ-11) | GJ-11 stealthy UCAV; delta flying wing; PL-15-class weapon carriage; LO design; PLAAF advanced drone strikes | Wikipedia (CC BY-SA 4.0) | ~5 |

**H3 subtotal: 2 sources, ~17 chunks**

---

### H4 — Early Warning & ISR

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Shaanxi KJ-500 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shaanxi_KJ-500](https://en.wikipedia.org/wiki/Shaanxi_KJ-500) | PLAAF AEW&C; phased array rotodome; Y-9 airframe; all-aspect radar; replaces KJ-200; primary Chinese airborne C2 node | Wikipedia (CC BY-SA 4.0) | ~6 |
| Ilyushin KJ-2000 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/KJ-2000](https://en.wikipedia.org/wiki/KJ-2000) | PLAAF large AEW&C; Il-76 derivative; three-face fixed array; high-value asset; battle management for air operations | Wikipedia (CC BY-SA 4.0) | ~5 |
| Shenyang Y-9JB (electronic reconnaissance) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shaanxi_Y-9](https://en.wikipedia.org/wiki/Shaanxi_Y-9) | Y-9 family ISR variants; SIGINT/ELINT collection; reconnaissance near Taiwan; signals intelligence for PLA fires cueing | Wikipedia (CC BY-SA 4.0) | ~6 |

**H4 subtotal: 3 sources, ~17 chunks**

---

### H5 — Attack Helicopters

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| CAIC Z-10 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/CAIC_Z-10](https://en.wikipedia.org/wiki/CAIC_Z-10) | PLA Army attack helicopter; HJ-10 ATGM, TY-90 AAM, 23mm cannon; dedicated anti-armor/CAS; emerging PLA Army aviation fires | Wikipedia (CC BY-SA 4.0) | ~6 |
| Harbin Z-19 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Harbin_Z-19](https://en.wikipedia.org/wiki/Harbin_Z-19) | PLA armed reconnaissance helicopter; FLIR/EO; HJ-8/10 missiles; Z-9 derivative; lighter attack/recon complement to Z-10 | Wikipedia (CC BY-SA 4.0) | ~5 |
| Sikorsky S-70 (Z-20) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Harbin_Z-20](https://en.wikipedia.org/wiki/Harbin_Z-20) | PLA utility/assault helicopter; Black Hawk equivalent; potential armed variant; PLAA air assault fires platform | Wikipedia (CC BY-SA 4.0) | ~5 |

**H5 subtotal: 3 sources, ~16 chunks**

**Section H total: 16 sources, ~116 chunks**

---

## Section I — PLA Sensors & Radars

### I1 — Airborne Fire Control Radars

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| KLJ-7A AESA radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/KLJ-7A](https://en.wikipedia.org/wiki/KLJ-7A) | NRIET AESA for J-10C/J-16; 1,856 T/R modules; comparable to AN/APG-79; LPI; SAR/GMTI capable; first Chinese AESA in wide service | Wikipedia (CC BY-SA 4.0) | ~5 |
| Type 1473 radar (J-20 radar) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Chengdu_J-20](https://en.wikipedia.org/wiki/Chengdu_J-20) | Subsection of J-20 article covering AESA radar (Type 1475/KLJ-5); forward array + EODAS; 5th-gen sensor suite comparable to APG-81 | Wikipedia (CC BY-SA 4.0) | ~5 |

**I1 subtotal: 2 sources, ~10 chunks**

---

### I2 — Ground-Based Early Warning & Long-Range Radars

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| JY-26 Skywatch-U UHF radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/JY-26](https://en.wikipedia.org/wiki/JY-26) | PLA 3D UHF phased array; stealth detection claimed; VHF/UHF for low-observable tracking; counter-F-35 threat | Wikipedia (CC BY-SA 4.0) | ~4 |
| JY-27A Wide Sky UHF radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/JY-27A](https://en.wikipedia.org/wiki/JY-27A) | PLA long-range 2D UHF/P-band early warning; 500+ km detection; stealth counter; exportable version of China's EW radar suite | Wikipedia (CC BY-SA 4.0) | ~4 |
| YLC-8B UHF radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/YLC-8](https://en.wikipedia.org/wiki/YLC-8) | PLA BMEW/tracking radar; UHF anti-stealth; early warning tier; integrated into IADS fire control chain | Wikipedia (CC BY-SA 4.0) | ~4 |
| SLC-2 counterfire radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/SLC-2](https://en.wikipedia.org/wiki/SLC-2) | PLA counterfire locating radar; mortar/rocket/artillery tracking; ground-based fires cueing; PLAAF and PLA Army integrated | Wikipedia (CC BY-SA 4.0) | ~3 |

**I2 subtotal: 4 sources, ~15 chunks**

---

### I3 — Naval Fire Control Radars

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Type 346 Dragon Eye AESA radar | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_346_radar](https://en.wikipedia.org/wiki/Type_346_radar) | Type 346/346A/346B active phased array; Type 052C/D/DL; Type 055; S-band + X-band; comparable to SPY-1 with AESA; AShM/BMD fire control | Wikipedia (CC BY-SA 4.0) | ~6 |

**I3 subtotal: 1 source, ~6 chunks**

---

### I4 — Electronic Warfare / SIGINT

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Shenyang J-16D (electronic warfare) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shenyang_J-16](https://en.wikipedia.org/wiki/Shenyang_J-16) **[VERIFIED]** | J-16D dedicated EW variant; 20 in service (2026); wingtip EW pods; internal EW replaces IRST and cannon; SEAD escort role | Wikipedia (CC BY-SA 4.0) | ~10 |

**I4 subtotal: 1 source, ~10 chunks**

**Section I total: 8 sources, ~41 chunks**

---

## Section J — PLAN Surface & Subsurface

### J1 — Aircraft Carriers

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Chinese aircraft carrier Fujian (Type 003) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Chinese_aircraft_carrier_Fujian](https://en.wikipedia.org/wiki/Chinese_aircraft_carrier_Fujian) **[VERIFIED]** | Type 003 Fujian; EMALS catapult; Type 346B radar; J-15T/J-35 carrier air wing; first full-sized Chinese carrier; PLAN force projection | Wikipedia (CC BY-SA 4.0) | ~8 |
| Chinese aircraft carrier Shandong (Type 002) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Chinese_aircraft_carrier_Shandong](https://en.wikipedia.org/wiki/Chinese_aircraft_carrier_Shandong) | Type 002; ski-jump; J-15 wing; indigenous build; second carrier; South Sea Fleet; full operational capability 2022 | Wikipedia (CC BY-SA 4.0) | ~6 |
| Chinese aircraft carrier Liaoning (Type 001) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Chinese_aircraft_carrier_Liaoning](https://en.wikipedia.org/wiki/Chinese_aircraft_carrier_Liaoning) | Type 001; refurbished Varyag; J-15 training and ops; North Sea Fleet; first PLAN carrier group exercises | Wikipedia (CC BY-SA 4.0) | ~6 |

**J1 subtotal: 3 sources, ~20 chunks**

---

### J2 — Amphibious Assault Ships

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Type 075 amphibious assault ship | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_075_amphibious_assault_ship](https://en.wikipedia.org/wiki/Type_075_amphibious_assault_ship) | PLAN LHD; Z-8/Z-18/Z-20 helicopter; LCAC; 3 ships commissioned 2021-2023; Taiwan/island seizure fires platform; PLAN Marine fires | Wikipedia (CC BY-SA 4.0) | ~6 |
| Type 071 amphibious transport dock | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_071_amphibious_transport_dock](https://en.wikipedia.org/wiki/Type_071_amphibious_transport_dock) | PLAN LPD; Type 726 LCAC; 8 commissioned; PLAN Marine Corps amphibious lift; South Sea Fleet primary amphibious assault force | Wikipedia (CC BY-SA 4.0) | ~5 |

**J2 subtotal: 2 sources, ~11 chunks**

---

### J3 — Destroyers & Frigates

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Type 055 destroyer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_055_destroyer](https://en.wikipedia.org/wiki/Type_055_destroyer) **[VERIFIED]** | Renhai-class cruiser (OSD); 112-cell VLS; Type 346B AESA; HHQ-9B/YJ-18A/YJ-21; BMD capability; flagship of PLAN surface forces | Wikipedia (CC BY-SA 4.0) | ~10 |
| Type 052D destroyer | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_052D_destroyer](https://en.wikipedia.org/wiki/Type_052D_destroyer) | Luyang III-class DDG; 64-cell VLS; Type 346A AESA; HHQ-9A/YJ-18/CJ-10; 25+ in service; primary PLAN surface fires | Wikipedia (CC BY-SA 4.0) | ~8 |
| Type 054A frigate | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_054A_frigate](https://en.wikipedia.org/wiki/Type_054A_frigate) | Jiangkai II FFG; 32-cell VLS; HHQ-16 SAM; 30+ in service; mainstay PLAN medium escort; anti-submarine fires | Wikipedia (CC BY-SA 4.0) | ~7 |
| Type 056A corvette | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_056_corvette](https://en.wikipedia.org/wiki/Type_056_corvette) | Jiangdao-class corvette; 60+ built; YJ-83 AShM; towed sonar; coastal defense and EEZ patrol fires | Wikipedia (CC BY-SA 4.0) | ~6 |
| Type 022 missile boat | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Type_022_missile_boat](https://en.wikipedia.org/wiki/Type_022_missile_boat) | Houbei-class wave-piercing catamaran; 8× YJ-83 AShM; 80+ in service; swarm anti-access saturation attack threat; littoral fires | Wikipedia (CC BY-SA 4.0) | ~5 |

**J3 subtotal: 5 sources, ~36 chunks**

---

### J4 — Submarines

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Type 094 (Jin-class) SSBN | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Jin-class_submarine](https://en.wikipedia.org/wiki/Jin-class_submarine) **[VERIFIED]** | Type 094/094A; JL-2/JL-3 SLBM; 6 operational; sea-based nuclear deterrent; PLAN second-strike capability; nuclear fires planning | Wikipedia (CC BY-SA 4.0) | ~8 |
| Type 093 (Shang-class) SSN | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shang-class_submarine](https://en.wikipedia.org/wiki/Shang-class_submarine) | Type 093/093A/093B; YJ-18A land-attack/AShM; torpedo; primary PLAN nuclear attack submarine; anti-carrier mission | Wikipedia (CC BY-SA 4.0) | ~6 |
| Type 039 (Yuan-class) submarine | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Yuan-class_submarine](https://en.wikipedia.org/wiki/Yuan-class_submarine) | Type 039A/B/C SSP; AIP (Stirling); ultra-quiet conventional; YJ-18/torpedo; 20+ in service; threat to CSG in littoral | Wikipedia (CC BY-SA 4.0) | ~6 |
| Type 035 (Ming-class) submarine | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Ming-class_submarine](https://en.wikipedia.org/wiki/Ming-class_submarine) | Type 035G conventional; aging design; being retired; historical PLAN submarine baseline for threat evolution | Wikipedia (CC BY-SA 4.0) | ~4 |

**J4 subtotal: 4 sources, ~24 chunks**

**Section J total: 14 sources, ~91 chunks**

---

## Section K — PLA Rocket Force Systems (PLARF)

### K1 — ICBMs

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| DF-5 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-5](https://en.wikipedia.org/wiki/DF-5) | DF-5B/C (MIRVed); liquid-fuel silo-based ICBM; 13,000+ km range; MRV/MIRV upgrades; PLARF oldest ICBM still operational | Wikipedia (CC BY-SA 4.0) | ~6 |
| DF-31 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-31](https://en.wikipedia.org/wiki/DF-31) | DF-31/AG; solid-fuel road-mobile ICBM; ~11,200 km range; penetration aids; first mobile ICBM giving PLARF survivability | Wikipedia (CC BY-SA 4.0) | ~6 |
| DF-41 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-41](https://en.wikipedia.org/wiki/DF-41) | DF-41; solid-fuel MIRV ICBM; 12,000–15,000 km range; road/rail/silo; can carry 10 MIRVs; most capable PLARF ICBM; silo construction at Yumen/Hami | Wikipedia (CC BY-SA 4.0) | ~6 |

**K1 subtotal: 3 sources, ~18 chunks**

---

### K2 — MRBMs / IRBMs / Anti-Ship Ballistic Missiles

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| DF-21 (CSS-5) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-21](https://en.wikipedia.org/wiki/DF-21) **[VERIFIED]** | DF-21A/C/D; solid-fuel MRBM; DF-21D ASBM (1,500 km, maneuvering RV targeting CVN); CSS-5 Mod 5; carrier-killer; A2/AD centerpiece | Wikipedia (CC BY-SA 4.0) | ~8 |
| DF-26 (CSS-18) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-26](https://en.wikipedia.org/wiki/DF-26) | DF-26; 4,000 km range; dual conventional/nuclear; anti-ship variant (DF-26B); Guam Express; intermediate-range threat to Guam | Wikipedia (CC BY-SA 4.0) | ~6 |
| DF-17 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-17](https://en.wikipedia.org/wiki/DF-17) **[VERIFIED]** | DF-17 with DF-ZF HGV; ~2,000 km range; Mach 5-10 glide; terminal maneuver; defeats current TMD; first operational HGV system | Wikipedia (CC BY-SA 4.0) | ~6 |
| DF-16 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-16](https://en.wikipedia.org/wiki/DF-16) | DF-16/G; solid-fuel SRBM/MRBM; 800-1,000 km; precision-guided conventional; terminal maneuver; Taiwanese and Guam target range | Wikipedia (CC BY-SA 4.0) | ~5 |
| DF-15 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-15](https://en.wikipedia.org/wiki/DF-15) | DF-15/B/C SRBM; 600 km; solid-fuel; rapid reload; Taiwan Strait target; MRBM precursor; conventional precision fires | Wikipedia (CC BY-SA 4.0) | ~5 |
| DF-11 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-11](https://en.wikipedia.org/wiki/DF-11) | DF-11/A SRBM; ~800 km range; solid-fuel TEL; PLARF Fujian-area brigades; Taiwan littoral fires | Wikipedia (CC BY-SA 4.0) | ~4 |

**K2 subtotal: 6 sources, ~34 chunks**

---

### K3 — Cruise Missiles

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| CJ-10 (DH-10) land-attack cruise missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/CJ-10](https://en.wikipedia.org/wiki/CJ-10) | CJ-10/CJ-10A LACM; 1,500-2,000 km range; terrain-following; ground-launched and H-6K air-launched (CJ-20); near-Kh-55 class | Wikipedia (CC BY-SA 4.0) | ~5 |
| DF-100 / CJ-100 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/DF-100](https://en.wikipedia.org/wiki/DF-100) | CJ-100/DF-100 ground-launched cruise missile; ~2,000 km range; supersonic terminal phase; 2019 parade debut; standoff precision strike | Wikipedia (CC BY-SA 4.0) | ~4 |

**K3 subtotal: 2 sources, ~9 chunks**

---

### K4 — Anti-Ship Missiles

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| YJ-12 (Eagle Strike 12) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/YJ-12](https://en.wikipedia.org/wiki/YJ-12) | H-6J/JH-7 air-launched; Mach 4; 400 km range; anti-ship; key PLAN/PLAAF AShM threat to CSG | Wikipedia (CC BY-SA 4.0) | ~5 |
| YJ-18 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/YJ-18](https://en.wikipedia.org/wiki/YJ-18) | Type 093/052D/055 submarine/surface-launched; 540 km range; subsonic cruise + Mach 3 terminal dash; anti-ship and land attack | Wikipedia (CC BY-SA 4.0) | ~5 |
| YJ-21 (Eagle Strike 21) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/YJ-21](https://en.wikipedia.org/wiki/YJ-21) | Type 055-launched; hypersonic AShM; Mach 6+ terminal; 1,000+ km range; 2022 test; carrier-killer from surface ship; PLAN A2/AD | Wikipedia (CC BY-SA 4.0) | ~5 |
| YJ-83 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/YJ-83](https://en.wikipedia.org/wiki/YJ-83) | C-803 export designation; subsonic AShM; Type 022/052/054A launched; 200+ km; most widely fielded PLAN AShM | Wikipedia (CC BY-SA 4.0) | ~4 |
| YJ-100 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/YJ-100](https://en.wikipedia.org/wiki/YJ-100) | H-6N air-launched long-range cruise; ~2,000 km range; land attack/AShM; extends PLAN/PLAAF long-range fires reach | Wikipedia (CC BY-SA 4.0) | ~4 |

**K4 subtotal: 5 sources, ~23 chunks**

---

### K5 — Surface-to-Air Missiles (PLA IADS)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| HQ-9 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/HQ-9](https://en.wikipedia.org/wiki/HQ-9) | HQ-9/9B/9BE; S-300P-derived; 200 km range (HQ-9B); active radar homing; multi-target engagement; backbone of PLA A2/AD IADS | Wikipedia (CC BY-SA 4.0) | ~8 |
| HQ-16 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/HQ-16](https://en.wikipedia.org/wiki/HQ-16) | Buk-M1 derived medium-range SAM; 40 km range; land and naval (HHQ-16) version; Type 052D/054A shipboard air defense | Wikipedia (CC BY-SA 4.0) | ~5 |
| HQ-22 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/HQ-22](https://en.wikipedia.org/wiki/HQ-22) | Long-range SAM; export designation FK-3; S-300P class; 170 km range; lower tier PLA integrated IADS; Serbia operated | Wikipedia (CC BY-SA 4.0) | ~4 |
| HQ-19 (BMD variant) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/HQ-19](https://en.wikipedia.org/wiki/HQ-19) | Ballistic missile defense SAM; HQ-9 family descendant; terminal-phase intercept; endo-atmospheric THAAD-class capability development | Wikipedia (CC BY-SA 4.0) | ~4 |

**K5 subtotal: 4 sources, ~21 chunks**

**Section K total: 20 sources, ~105 chunks**

---

## Section L — Russia / Soviet Legacy (Supplemental — New Items Only)

**Note:** The existing `pla_sources.md` and `curricula_reading_lists.md` corpora already contain extensive Russian/Soviet coverage (Su-27/30/35, S-300/400, Iskander, Kalibr, Kh-101, Tu-160, etc.). This section lists **only new/supplemental items** not covered in prior passes, focusing on post-2022 systems and emerging capabilities.

### L1 — New Systems Not in Prior Corpus

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Sukhoi Su-57 Felon | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Sukhoi_Su-57](https://en.wikipedia.org/wiki/Sukhoi_Su-57) | Russian 5th-gen stealth fighter; N036 Byelka AESA; R-77M/R-37M; limited production; PLA competitive analysis baseline; Ukraine employment | Wikipedia (CC BY-SA 4.0) | ~10 |
| Oreshnik IRBM | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Oreshnik_missile](https://en.wikipedia.org/wiki/Oreshnik_missile) | RS-26-derived IRBM; MRV/hypersonic glide bodies; Mach 10+; first employed vs. Ukraine Nov 2024; post-INF Russia escalation; new threat tier | Wikipedia (CC BY-SA 4.0) | ~5 |
| 9M729 (SSC-8 Screwdriver) cruise missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/9M729](https://en.wikipedia.org/wiki/9M729) | Ground-launched cruise missile; INF Treaty violation; ~2,500 km range; caused US INF withdrawal 2019; European theater LACM threat | Wikipedia (CC BY-SA 4.0) | ~5 |
| Kh-47M2 Kinzhal | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Kh-47M2_Kinzhal](https://en.wikipedia.org/wiki/Kh-47M2_Kinzhal) | Air-launched hypersonic; MiG-31K/Tu-22M3 carried; Mach 10; 2,000 km range; ASBM variant; Ukraine combat use; HGV threat comparison vs. DF-17 | Wikipedia (CC BY-SA 4.0) | ~6 |
| Zircon (3M22) hypersonic cruise missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/3M22_Zircon](https://en.wikipedia.org/wiki/3M22_Zircon) | Ship/submarine-launched Mach 8-9 AShCM; Gorshkov-class/Yasen-M platforms; 1,000 km range; PLAN and Russia comparison; carrier-killer | Wikipedia (CC BY-SA 4.0) | ~5 |
| Shahed-136 / Geran-2 (Russian employment) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shahed_136](https://en.wikipedia.org/wiki/Shahed_136) **[VERIFIED]** | Iranian-origin loitering munition; Russian Geran-2 designation; mass employment vs Ukraine infrastructure; replication/transfer threat for other adversaries | Wikipedia (CC BY-SA 4.0) | ~6 |

**Section L total: 6 sources, ~37 chunks**

---

## Section M — DPRK & Iran

### M1 — DPRK Ballistic Missiles

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Hwasong-17 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Hwasong-17](https://en.wikipedia.org/wiki/Hwasong-17) **[VERIFIED]** | DPRK's largest ICBM; liquid-fuel; 15,000+ km range; MIRV-capable; demonstrated 2022; poses direct threat to CONUS; nuclear fires context | Wikipedia (CC BY-SA 4.0) | ~6 |
| Hwasong-18 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Hwasong-18](https://en.wikipedia.org/wiki/Hwasong-18) | DPRK first solid-fuel ICBM; three-stage; 15,000+ km; 2023 tests; strategic significance — reduced preparation time vs. liquid-fuel | Wikipedia (CC BY-SA 4.0) | ~5 |
| Hwasong-19 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Hwasong-19](https://en.wikipedia.org/wiki/Hwasong-19) | DPRK ICBM; largest solid-fuel ICBM by diameter; 2024 test; latest in Hwasong family; escalation assessment for joint fires planners | Wikipedia (CC BY-SA 4.0) | ~4 |
| Pukguksong-3 / Pukguksong SLBM | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Pukguksong-3](https://en.wikipedia.org/wiki/Pukguksong-3) | DPRK solid-fuel SLBM; Pukguksong-3/4/5; submarine-based second strike; sea-based nuclear fires; Sinpo-C class submarine | Wikipedia (CC BY-SA 4.0) | ~5 |
| KN-23 ballistic missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/KN-23](https://en.wikipedia.org/wiki/KN-23) | DPRK quasi-ballistic SRBM; Iskander-like depressed trajectory; 690 km; pull-up maneuver; evades PAC-3 terminal defense; transferred to Russia | Wikipedia (CC BY-SA 4.0) | ~5 |
| KN-24 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/KN-24](https://en.wikipedia.org/wiki/KN-24) | DPRK ATACMS-like SRBM; 400 km; precision-guided; conventional fires threat to ROK/USFK; potentially transferred Russia/Ukraine | Wikipedia (CC BY-SA 4.0) | ~4 |
| KN-25 (600mm MLRS) | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/KN-25](https://en.wikipedia.org/wiki/KN-25) | DPRK 600mm super-large MLRS; 380 km range; saturation fires capability; deployed against ROK; DPRK strategic rocket forces | Wikipedia (CC BY-SA 4.0) | ~4 |
| Hwasal-2 cruise missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Hwasal-2](https://en.wikipedia.org/wiki/Hwasal-2) | DPRK subsonic LACM; 1,500-2,000 km range; Tomahawk-class; nuclear warhead capable; low-altitude terrain-following; first operational DPRK LACM | Wikipedia (CC BY-SA 4.0) | ~4 |

**M1 subtotal: 8 sources, ~37 chunks**

---

### M2 — Iran Missiles & Drones

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| HESA Shahed 136 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shahed_136](https://en.wikipedia.org/wiki/Shahed_136) **[VERIFIED]** | Iran's kamikaze loitering munition; 2,500 km range (Shahed-238 jet); widely transferred to Russia; delta-wing; low RCS; swarm threat | Wikipedia (CC BY-SA 4.0) | ~6 |
| Shahed-238 | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Shahed_238](https://en.wikipedia.org/wiki/Shahed_238) | Jet-propelled variant of Shahed-136; higher speed (Mach 0.6-0.7); enhanced evasion of point defense; 2023 emergence; asymmetric fires threat | Wikipedia (CC BY-SA 4.0) | ~4 |
| Fattah hypersonic missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Fattah_(missile)](https://en.wikipedia.org/wiki/Fattah_(missile)) | Iran's claimed hypersonic MRBM; Mach 13-15 glide vehicle; 1,400 km range; 2023 debut; IRGC strategic fires capability claim | Wikipedia (CC BY-SA 4.0) | ~4 |
| Kheibar Shekan ballistic missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Kheibar_Shekan](https://en.wikipedia.org/wiki/Kheibar_Shekan) | Solid-fuel MRBM; 1,450 km range; 500 kg warhead; used in 2024 Israel strike; precision IRGC missile capable of targeting US facilities | Wikipedia (CC BY-SA 4.0) | ~4 |
| Ghadr-110 ballistic missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Ghadr-110](https://en.wikipedia.org/wiki/Ghadr-110) | Liquid-fuel MRBM; Shahab-3 derivative; 1,950 km range; nuclear-capable (claimed); IRGC/IRGC Aerospace Force strategic fires | Wikipedia (CC BY-SA 4.0) | ~4 |
| Sejjil ballistic missile | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Sejjil](https://en.wikipedia.org/wiki/Sejjil) | Solid-fuel two-stage MRBM; 2,000-2,500 km range; maneuvering RV; rapid-launch advantage; covers full Middle East + SE Europe | Wikipedia (CC BY-SA 4.0) | ~4 |
| Bavar-373 air defense system | Wikipedia | Wikipedia contributors | 2024 | [en.wikipedia.org/wiki/Bavar-373](https://en.wikipedia.org/wiki/Bavar-373) | Iran indigenous S-300-class SAM; Sayyad-4B interceptor; 300 km range; 2019 IOC; Iran IADS backbone; US/Israeli strike planning SEAD target | Wikipedia (CC BY-SA 4.0) | ~5 |

**M2 subtotal: 7 sources, ~31 chunks**

**Section M total: 15 sources, ~68 chunks**

---

## Supplemental Sources — Cross-Cutting Reference Works

### S1 — Open-Access Reference Databases for Platform/Sensor Data

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| CSIS Missile Defense Project — Missiles of the World | CSIS | CSIS Missile Defense Project | Ongoing | [missilethreat.csis.org](https://missilethreat.csis.org) | Comprehensive missile database with range, payload, propulsion, guidance for 300+ systems; primary open-source missile data reference | Think tank (public release) | ~50 |
| Federation of American Scientists (FAS) — Military Systems | FAS | FAS Staff | Ongoing | [fas.org/programs/ssp/](https://fas.org/programs/ssp/) | Nuclear forces, delivery systems, warhead counts; FAS Nuclear Notebook; open-source nuclear posture reference for fires planners | Think tank (public release) | ~40 |
| Global Security — Military Systems | GlobalSecurity.org | John Pike, staff | Ongoing | [globalsecurity.org/military/systems](https://www.globalsecurity.org/military/systems.htm) | Cross-indexed military platforms, sensors, weapons; open-source; useful for system specifications not on Wikipedia | Think tank (public release) | ~80 |
| Naval News — PLAN Naval Order of Battle | Naval News | Naval News Staff | 2024 | [navalnews.com/naval-news/2024/01/plan-naval-order-of-battle-2024/](https://www.navalnews.com/naval-news/2024/01/plan-naval-order-of-battle-2024/) | Current PLAN ship counts by class; updated annually; most accessible open-source OOB reference for naval fires planners | Think tank (public release) | ~8 |
| The War Zone / The Drive — Defense Coverage | TWZ | Joseph Trevithick et al. | Ongoing | [thedrive.com/the-war-zone](https://www.thedrive.com/the-war-zone) | In-depth open-source reporting on platform capabilities, new systems, kill chain developments; essential supplemental tracker | Journalism (public) | ~30 |

**S1 subtotal: 5 sources, ~208 chunks**

---

### S2 — Key Manufacturer Pages (Supplemental)

| Title | Org | Author(s) | Year | URL | Relevance | License | Est. Chunks |
|---|---|---|---|---|---|---|---|
| Raytheon AN/SPY-6 product page | RTX/Raytheon | Raytheon | 2024 | [rtx.com/raytheon/what-we-do/naval-radar/spydr-family-of-radars](https://www.rtx.com/raytheon/what-we-do/naval-radar/spydr-family-of-radars) | SPY-6 family specification overview; AMDR, Volume Search Radar (VSR), SPQ-9B; BMD/IAMD integration | Manufacturer (public marketing) | ~3 |
| Lockheed Martin EOTS/DAS product page | Lockheed Martin | Lockheed Martin | 2024 | [lockheedmartin.com/en-us/products/electro-optical-targeting-system.html](https://www.lockheedmartin.com/en-us/products/electro-optical-targeting-system.html) | EOTS spec sheet; third-generation FLIR, SAL, laser range-finder; integrated with F-35 sensor fusion architecture | Manufacturer (public marketing) | ~3 |
| Northrop Grumman AN/APG-81 product page | Northrop Grumman | Northrop Grumman | 2024 | [northropgrumman.com/what-we-do/air/apg-81-active-electronically-scanned-array-aesa-radar/](https://www.northropgrumman.com/what-we-do/air/apg-81-active-electronically-scanned-array-aesa-radar/) | APG-81 AESA performance data; modes; electronic warfare; SAR resolution; interoperability | Manufacturer (public marketing) | ~3 |
| Boeing P-8 Poseidon product page | Boeing | Boeing Defense | 2024 | [boeing.com/defense/maritime-surveillance/p-8a-poseidon](https://www.boeing.com/defense/maritime-surveillance/p-8a-poseidon) | P-8A open-ocean ASUW/ASW specs; AN/APY-10 radar, MX-20A, Harpoon/SLAM-ER integration | Manufacturer (public marketing) | ~3 |
| Kongsberg Naval Strike Missile product page | Kongsberg | Kongsberg Defence & Aerospace | 2024 | [kongsberg.com/maritime/products-and-systems/defence-and-surveillance-systems/naval-strike-missile/](https://www.kongsberg.com/maritime/products-and-systems/defence-and-surveillance-systems/naval-strike-missile/) | NSM/JSM specs; passive RF seeker; terrain-following; NMESIS ground-launched; F-35 internal carriage (JSM) | Manufacturer (public marketing) | ~3 |

**S2 subtotal: 5 sources, ~15 chunks**

---

**Supplemental total: 10 sources, ~223 chunks**

---

## Final Summary Table

| Section | Title | Source Count | Est. Chunk Subtotal |
|---|---|---|---|
| A | US Air Platforms (Strike & Multi-role) | 19 | ~206 |
| B | US ISR / C2 / Tanker Platforms | 17 | ~153 |
| C | US Targeting Pods & Airborne Sensors | 15 | ~76 |
| D | US Naval Surface Combatants & Strike Platforms | 21 | ~199 |
| E | US Army Fires Platforms & Sensors | 16 | ~100 |
| F | US Marine Fires Platforms & Sensors | 7 | ~68 |
| G | Allied / Partner Platforms | 24 | ~184 |
| H | PLA Air Platforms | 16 | ~116 |
| I | PLA Sensors & Radars | 8 | ~41 |
| J | PLAN Surface & Subsurface | 14 | ~91 |
| K | PLA Rocket Force Systems (PLARF) | 20 | ~105 |
| L | Russia / Soviet Legacy (Supplemental) | 6 | ~37 |
| M | DPRK & Iran | 15 | ~68 |
| S | Supplemental Cross-Cutting Reference Works | 10 | ~223 |
| **GRAND TOTAL** | | **208** | **~1,667** |

---

## URL Verification Log

The following URLs were confirmed accessible via `fetch_url` during research (marked **[VERIFIED]** in the table above):

1. `en.wikipedia.org/wiki/Lockheed_Martin_F-35_Lightning_II` — F-35 Lightning II ✓
2. `en.wikipedia.org/wiki/Lockheed_Martin_F-22_Raptor` — F-22 Raptor ✓
3. `en.wikipedia.org/wiki/McDonnell_Douglas_F-15E_Strike_Eagle` — F-15E Strike Eagle ✓
4. `en.wikipedia.org/wiki/Northrop_Grumman_B-21_Raider` — B-21 Raider ✓
5. `en.wikipedia.org/wiki/Arleigh_Burke-class_destroyer` — Arleigh Burke DDG ✓
6. `en.wikipedia.org/wiki/M142_HIMARS` — M142 HIMARS ✓
7. `en.wikipedia.org/wiki/Chengdu_J-20` — J-20 Mighty Dragon ✓
8. `en.wikipedia.org/wiki/Type_055_destroyer` — Type 055 Renhai ✓
9. `en.wikipedia.org/wiki/DF-21` — DF-21 MRBM/ASBM ✓
10. `en.wikipedia.org/wiki/Sniper_Advanced_Targeting_Pod` — AN/AAQ-33 Sniper ATP ✓
11. `en.wikipedia.org/wiki/Boeing_RC-135` — RC-135 family ✓
12. `en.wikipedia.org/wiki/Northrop_Grumman_RQ-4_Global_Hawk` — RQ-4 Global Hawk ✓
13. `en.wikipedia.org/wiki/Aegis_Combat_System` — Aegis Combat System ✓
14. `en.wikipedia.org/wiki/Tomahawk_cruise_missile` — Tomahawk BGM-109 ✓
15. `en.wikipedia.org/wiki/DF-17` — DF-17 HGV carrier ✓
16. `en.wikipedia.org/wiki/Shahed_136` — HESA Shahed-136/Geran-2 ✓
17. `en.wikipedia.org/wiki/Hwasong-17` — Hwasong-17 ICBM ✓
18. `en.wikipedia.org/wiki/Chinese_aircraft_carrier_Fujian` — Fujian (Type 003) ✓
19. `en.wikipedia.org/wiki/Xian_H-6` — Xi'an H-6 bomber ✓
20. `en.wikipedia.org/wiki/Naval_Strike_Missile` — NSM/NMESIS ✓
21. `en.wikipedia.org/wiki/Shenyang_J-16` — J-16/J-16D EW ✓
22. `en.wikipedia.org/wiki/Jin-class_submarine` — Type 094 SSBN ✓
23. `en.wikipedia.org/wiki/Virginia-class_submarine` — Virginia SSN ✓
24. `en.wikipedia.org/wiki/General_Atomics_MQ-9_Reaper` — MQ-9 Reaper ✓
25. `en.wikipedia.org/wiki/Precision_Strike_Missile` — PrSM ✓
26. `lockheedmartin.com/en-us/products/f-35.html` — LM F-35 product page ✓
27. `northropgrumman.com/what-we-do/air/b-21-raider/` — NG B-21 product page ✓

**Total verified: 27 URLs**

---

*End of platforms_sensors_sources.md — Pass 3 of 3*
