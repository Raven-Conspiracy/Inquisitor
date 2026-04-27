# US Army Operations Process — Foundry Ontology Accelerator

A doctrine-derived, **unclassified** ontology starter package designed to accelerate a Palantir Foundry build of the **US Army operations process** (plan, prepare, execute, assess) and to support a **Joint Targeting Cycle (JTC)** workflow through Phases 1–3.

This is **not an official Palantir Foundry export** and **not an authoritative doctrinal product**. It is a structured starter that translates publicly available Army and joint doctrine into Foundry-shaped object types, link types, action types, value types, and seed data so an analyst or platform engineer can import and adapt it quickly. Adapt all `apiName`s and property type names to match the destination Foundry tenant's conventions before promoting beyond a sandbox.

## Purpose

Provide a single, importable starter for Foundry that gives a JTC build:

- A coherent operations-process backbone (operations, plans/orders, missions, intent, COAs, tasks, decision points, running estimates, MOEs/MOPs, indicators, assessment plans).
- JTC Phase 1–3 support objects/links/actions (targeting guidance, target system/set/target, target development records, target nominations, collection requirements, NAIs/TAIs, effects, capabilities).
- Army organizations from team to theater army, headquarters, command posts, staff sections and elements, joint force elements.
- Equipment and readiness (equipment, equipment type, weapon system, sensor system, platform, comms system, maintenance status, work orders, readiness reports, capabilities).
- Sustainment and supply (Class I–X, supply items/requirements/requests, supply points, ASLs, basic loads, LOGPACs, distribution nodes, transportation assets, SSAs).
- Geography/mission context (AO, AOI, OE, location, route, control measures).
- Shared value types (enumerations) for status, classification, readiness, supply class, target lifecycle, etc.

## Scope

In scope:

- Doctrine-derived structure of objects, links, and actions for the operations process and JTC Phases 1–3.
- Public-domain doctrinal references for every object/link/action/value type where feasible.
- Seed data for Classes of Supply, JTC phases 1–3, and operations process activities.

Out of scope (deliberately):

- Real ORBAT, real targeting data, classified TTPs, restricted distribution doctrine excerpts.
- Foundry-specific platform features beyond ontology-shaped JSON (no native Workshop/Slate config).
- Implementation of access control, security marking enforcement, audit pipelines (left to the destination tenant).

## Naming convention

- `apiName` and property `apiName`: **lowerCamelCase**.
- `displayName` (object/link/action/value types): **TitleCase**.
- Property types use a portable vocabulary: `string`, `integer`, `double`, `boolean`, `date`, `timestamp`, `geoshape`, `geopoint`, `attachment`, `array<string>`, `enum:<valueType apiName>`. Map to your Foundry tenant's exact property type names during import.

## Layout

```
foundry/ontology/us_army_operations_process/
  README.md                            # this file
  manifest.json                        # package metadata, file list, import order
  source_mapping.json                  # doctrine bibliography
  value_types.json                     # enumerations / shared value types
  object_types.json                    # object type definitions
  link_types.json                      # link type definitions
  action_types.json                    # action type definitions
  seed_data/
    classes_of_supply.json             # Class I–X seed data
    jtc_phases_1_to_3.json             # JTC Phases 1–3 seed data
    operations_process_activities.json # Plan/Prepare/Execute/Assess seed data
  schema/
    *.schema.json                      # lightweight JSON Schemas
  scripts/
    validate_ontology_json.py          # validates JSON well-formedness + schema
  docs/
    import_notes.md                    # Foundry import/adaptation guidance
```

## Recommended import order

This order resolves cross-references cleanly:

1. `source_mapping.json` (sourceIds referenced everywhere)
2. `value_types.json` (enums referenced by object/action types)
3. `object_types.json`
4. `link_types.json` (depends on object types)
5. `action_types.json`
6. `seed_data/classes_of_supply.json`
7. `seed_data/operations_process_activities.json`
8. `seed_data/jtc_phases_1_to_3.json`

The same order is also encoded in `manifest.json` under `importOrder`.

## Validation

```bash
cd foundry/ontology/us_army_operations_process
python3 scripts/validate_ontology_json.py
```

The script:

- Parses every JSON file with stdlib `json` (always runs).
- If `jsonschema` is installed, validates each file against its schema (`pip install jsonschema`).
- Performs lightweight cross-reference checks (link endpoints reference real object types; `enum:<valueType>` references are resolvable).

Exit code 0 = pass; 1 = fail.

## Assumptions

- Foundry tenant uses an Ontology Manager–style configuration with object types, link types, action types, and value types. Map each JSON entity to the corresponding Foundry construct (see `docs/import_notes.md`).
- Property types in this package are **portable**, not Foundry-tenant-exact. Translate to your tenant's exact type names during import.
- All content is unclassified and based on publicly accessible doctrine. No CUI, FOUO, or classified content is included or implied.
- The user has already built JTC Phase 1–3 in Foundry; this package is intended to backfill a coherent operations-process and sustainment graph that the existing JTC work can hang off of.

## Doctrine citations

Each object/link/action/value type carries `sourceDoctrine` ids that map into `source_mapping.json`. The principal sources used:

- **ADP 5-0, The Operations Process** — operations process backbone, MDMP, TLP. https://armypubs.army.mil/ (alt: https://irp.fas.org/doddir/army/adp5_0.pdf)
- **FM 5-0, Planning and Orders Production** (Nov 2024) — planning, orders production, assessment planning. https://armypubs.army.mil/ (alt: https://aviation-assets.info/wp-content/uploads/ARN42404-FM_5-0-000-WEB-1.pdf)
- **ADP 3-0 / FM 3-0, Operations** — multidomain operations, warfighting functions, operational framework. https://armypubs.army.mil/ (alt: https://irp.fas.org/doddir/army/adp3_0.pdf)
- **FM 3-94, Armies, Corps, and Division Operations** — echelons above brigade. https://armypubs.army.mil/ (alt: https://irp.fas.org/doddir/army/fm3_94.pdf)
- **FM 3-96, Brigade Combat Team** — IBCT/SBCT/ABCT. https://armypubs.army.mil/ (alt: https://www.army.mil/article/158747/field_manual_3_96_the_brigade_combat_team_published_last_month)
- **ATP 3-21.8, Infantry Rifle Platoon and Squad** — small unit. https://armypubs.army.mil/ (alt: https://commons.wikimedia.org/wiki/File:ATP_3-21.8_Infantry_Rifle_Platoon_and_Squad_January_2024.pdf)
- **ADP 4-0, Sustainment** — sustainment overview, operational reach/freedom of action/endurance. https://armypubs.army.mil/ (alt: https://cascom.army.mil/asrp/doctrine-pubs.html)
- **ATP 4-42, General Supply and Field Services Operations** — Class II, III packaged, IV, VI, configured loads. https://armypubs.army.mil/ (alt: https://www.bits.de/NRANEU/others/amd-us-archive/ATP4-42(14).pdf)
- **ATP 4-42.2, Supply Support Activity Operations** — SSA, classes of supply table. https://armypubs.army.mil/ (alt: https://www.bits.de/NRANEU/others/amd-us-archive/ATP4-42x2(14).pdf)
- **AR 710-2, Supply Policy Below the National Level** — accountability, ASL, basic load. https://armypubs.army.mil/
- **AR 750-1, Army Materiel Maintenance Policy** — field/sustainment maintenance. https://armypubs.army.mil/ (alt: https://aviation-assets.info/wp-content/uploads/ARN32929-AR_750-1-000-WEB-1.pdf)
- **DA PAM 750-3, Soldiers' Guide for Field Maintenance Operations** — PMCS, TAMMS, equipment records. https://www.benning.army.mil/infantry/199th/2-16/ABOLC/content/pdf/p750_3.pdf
- **JP 3-60, Joint Targeting** — JTC phases. https://www.jcs.mil/
- **CJCSM 3108.01, Joint Fires Element** — JFE, JTCB, JTWG, JIPTL/JTL/NSL, combat assessment. https://www.jcs.mil/Portals/36/Documents/Library/Manuals/CJCSM%203108.01.pdf
- **Joint Targeting Staff Course 2023 Syllabus** — supplementary JTC phase objectives. https://www.jcs.mil/Portals/36/Documents/Doctrine/training/jts/2023joint_target_staff_course_syllabus.pdf?ver=bXDtvS7rwbmnfI28cXro3g%3D%3D
- **ADP 1-02, Operational Terms and Military Symbols** — operational terms, symbols, control measures. https://armypubs.army.mil/ (alt: https://irp.fas.org/doddir/army/adp1_02.pdf)

The full bibliography lives in `source_mapping.json`.

## Caveats and limitations

- Foundry tenants differ in property-type vocabulary, action SDK conventions, and link-type modeling. Treat this package as a **structured starting point** — most apiNames will need a tenant-specific prefix or namespace.
- The doctrine references include public mirrors and convenience PDFs. Always treat the Army Publishing Directorate (`https://armypubs.army.mil/`) and the Joint Chiefs of Staff (`https://www.jcs.mil/`) as authoritative for the latest editions.
- Joint targeting content draws on JP 3-60, CJCSM 3108.01, and the Joint Targeting Staff Course syllabus. JP 3-60 itself may be controlled distribution; do not infer specific edition or page citations beyond what publicly available material supports.
- Nothing in this package should be used to populate live targeting, ORBAT, or mission systems without separate tenant-side authority-to-operate, classification handling, and validation.
