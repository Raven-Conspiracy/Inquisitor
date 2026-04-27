# Foundry Import Notes

This document explains how to map this package's JSON files into Palantir Foundry concepts and what to adapt for a specific tenant.

## Mapping table

| Package file | Foundry concept | Notes |
|---|---|---|
| `value_types.json` | Ontology Manager > Value Types (or shared enums) | Each entry is an enumeration with `apiName`, `baseType`, and `values`. If your tenant does not use first-class value types, model these as constrained `string`/`integer` properties with backed code-list datasets. |
| `object_types.json` | Ontology Manager > Object Types | Each entry has `apiName`, `displayName`, `primaryKey`, `titleProperty`, and a flat list of `properties`. Wire each property to a backing dataset column at import time. |
| `link_types.json` | Ontology Manager > Link Types | Bidirectional, with `cardinality`. Foundry's link-type cardinality maps directly to `ONE_TO_ONE`, `ONE_TO_MANY`, `MANY_TO_ONE`, `MANY_TO_MANY`. |
| `action_types.json` | Ontology Manager > Action Types | Each `inputs[]` becomes an action parameter; `effects[]` is a human-readable description of side effects (model in TypeScript/Foundry SDK on the tenant). `preconditions[]` map to action validators. `auditFields[]` describe expected `actor` / `actionTimestamp` / `classificationMarking` capture. |
| `seed_data/*.json` | Datasets feeding initial object instances | Land each into a separate dataset and use a backing transform / OSv2 spec to materialize objects. |
| `source_mapping.json` | Reference dataset (doctrine) | Land as a dataset; expose as a small `Doctrine` object type if useful. |
| `manifest.json` | Build/CI metadata | Use `importOrder` to drive scripted creation order. |
| `schema/*.schema.json` | Pre-import validation only | Not imported into Foundry. Run via `scripts/validate_ontology_json.py` in CI. |

## Property type translation

This package uses a portable property-type vocabulary. Translate to your Foundry tenant's exact names during import:

| Package type | Typical Foundry equivalent |
|---|---|
| `string` | string |
| `integer` | integer |
| `double` | double |
| `boolean` | boolean |
| `date` | date |
| `timestamp` | timestamp |
| `geopoint` | geopoint / geohash |
| `geoshape` | geoshape |
| `attachment` | attachment |
| `array<string>` | string array |
| `enum:<valueType>` | reference to the matching value type / coded string |

## Naming and namespacing

- All `apiName`s are lowerCamelCase and plain (no namespace prefix). Most tenants prefer a stable namespace (e.g. `usa.opsProcess.operation`). Add the prefix during import; do not edit it back into the source files.
- `displayName`s are TitleCase and human-readable. Safe to use as-is.

## Action implementation guidance

Action types in this package describe the **shape and intent** of each action; implement the actual server-side logic in your tenant's preferred SDK (TypeScript Foundry SDK, OSv2 actions, Workshop logic). Use the package's `preconditions[]` and `effects[]` strings as the test plan for the implementation.

Cross-cutting fields to capture in every action by convention:

- `actor` — Foundry user invoking the action
- `actionTimestamp` — server-side time
- `classificationMarking` — pulled from the input or default tenant marking
- `sourceDoctrineIds` (where applicable) — preserved on derived objects

## JTC integration

The user already has a JTC build supporting Phases 1–3. This package backfills the operations-process graph that JTC artifacts hang off of:

- `targetingGuidance` ↔ `operation` and `objective` (Phase 1 anchor)
- `targetSystem` → `targetSet` → `target` → `targetDevelopmentRecord` (Phase 2 chain)
- `effect` ↔ `target`, `effect` ↔ `objective`, `weaponSystem` / `equipment` ↔ `capability` (Phase 3 capabilities analysis)
- `collectionRequirement` ↔ `target` / `namedAreaOfInterest` / `targetAreaOfInterest` (collection in support of targeting)

If your existing JTC ontology already names these concepts differently, treat this package as a **mapping reference**: use the doctrine citations on each entry to bridge to your existing apiNames rather than adopting wholesale.

## Sustainment integration

Sustainment objects (`classOfSupply`, `supplyItem`, `supplyRequirement`, `supplyRequest`, `supplyPoint`, `authorizedStockageList`, `basicLoad`, `logisticsPackage`, `distributionNode`, `transportationAsset`, `supplySupportActivity`) connect to the operations-process backbone via:

- `supplyRequirement` → `task` (forecasted consumption supports planned tasks)
- `supplyRequest` → `armyOrganization` (who's requesting)
- `logisticsPackage` → `armyOrganization` (delivery destination)
- `route` → `distributionNode` (network topology)

This lets a Foundry analyst run "what supplies does this operation actually need?" queries by traversing `operation` → `phase` → `task` → `supplyRequirement` → `supplyItem` → `classOfSupply`.

## Caveats

- Treat this package as a **starter**, not a drop-in production schema. Most large tenants will rename, namespace, and prune entries before promoting beyond a sandbox.
- The package does not include access-control rules, marking enforcement, or backing dataset definitions. Those are tenant-side concerns and should be added after import.
- Doctrine citations point to current public sources at time of authoring. Confirm against `https://armypubs.army.mil/` and `https://www.jcs.mil/` for the authoritative current edition before finalizing any ontology promotion review.
