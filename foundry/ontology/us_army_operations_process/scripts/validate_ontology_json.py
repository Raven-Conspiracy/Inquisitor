#!/usr/bin/env python3
"""Validate the US Army Operations Process Foundry ontology accelerator JSON files.

Two-tier validation:
  1. JSON well-formedness (always runs; uses stdlib json).
  2. JSON Schema conformance for each file (runs only if `jsonschema` is installed).

Exit codes:
  0 - all validations passed
  1 - one or more validations failed (well-formedness or schema)

Usage:
  python3 scripts/validate_ontology_json.py [package_dir]

If `package_dir` is omitted, the script assumes it lives in `<package>/scripts/` and
validates files in its parent directory.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Optional, Tuple


FILE_TO_SCHEMA = {
    "manifest.json": "schema/manifest.schema.json",
    "object_types.json": "schema/object_types.schema.json",
    "link_types.json": "schema/link_types.schema.json",
    "action_types.json": "schema/action_types.schema.json",
    "value_types.json": "schema/value_types.schema.json",
    "source_mapping.json": "schema/source_mapping.schema.json",
    "seed_data/classes_of_supply.json": "schema/classes_of_supply.schema.json",
    "seed_data/jtc_phases_1_to_3.json": "schema/jtc_phases.schema.json",
    "seed_data/operations_process_activities.json": "schema/operations_process_activities.schema.json",
}


def load_json(path: Path) -> Tuple[Optional[object], Optional[str]]:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh), None
    except FileNotFoundError:
        return None, f"missing file: {path}"
    except json.JSONDecodeError as exc:
        return None, f"JSON parse error in {path}: {exc}"


def try_import_jsonschema():
    try:
        import jsonschema  # noqa: F401
        from jsonschema import Draft202012Validator

        return Draft202012Validator
    except Exception:
        return None


def main(argv: list[str]) -> int:
    here = Path(__file__).resolve().parent
    default_root = here.parent
    package_root = Path(argv[1]).resolve() if len(argv) > 1 else default_root

    print(f"[validate] package root: {package_root}")

    errors: list[str] = []
    parsed: dict[str, object] = {}

    # 1) JSON well-formedness for all known files
    for rel_path in FILE_TO_SCHEMA:
        full = package_root / rel_path
        data, err = load_json(full)
        if err:
            errors.append(err)
            print(f"  [FAIL] {rel_path}: {err}")
        else:
            parsed[rel_path] = data
            print(f"  [ ok ] {rel_path}: parsed")

    # Also validate every schema file is itself valid JSON
    schema_dir = package_root / "schema"
    if schema_dir.is_dir():
        for entry in sorted(schema_dir.iterdir()):
            if entry.suffix == ".json":
                _, err = load_json(entry)
                if err:
                    errors.append(err)
                    print(f"  [FAIL] schema/{entry.name}: {err}")
                else:
                    print(f"  [ ok ] schema/{entry.name}: parsed")

    # 2) Schema validation if jsonschema is available
    Validator = try_import_jsonschema()
    if Validator is None:
        print("[validate] jsonschema not installed; skipping schema conformance checks.")
    else:
        for rel_path, schema_rel in FILE_TO_SCHEMA.items():
            schema_path = package_root / schema_rel
            schema_data, err = load_json(schema_path)
            if err:
                errors.append(err)
                print(f"  [FAIL] schema {schema_rel}: {err}")
                continue
            data = parsed.get(rel_path)
            if data is None:
                continue
            try:
                validator = Validator(schema_data)
                schema_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
                if schema_errors:
                    for se in schema_errors:
                        path_repr = "/".join(str(p) for p in se.path) or "<root>"
                        msg = f"schema validation error in {rel_path} at {path_repr}: {se.message}"
                        errors.append(msg)
                        print(f"  [FAIL] {msg}")
                else:
                    print(f"  [ ok ] {rel_path}: schema-valid against {schema_rel}")
            except Exception as exc:
                errors.append(f"schema validator error for {rel_path}: {exc}")
                print(f"  [FAIL] {rel_path}: {exc}")

    # 3) Lightweight cross-reference checks (always)
    cross_errors = cross_reference_checks(parsed)
    for ce in cross_errors:
        errors.append(ce)
        print(f"  [FAIL] cross-ref: {ce}")

    print()
    if errors:
        print(f"[validate] FAILED with {len(errors)} error(s).")
        return 1
    print("[validate] PASSED.")
    return 0


def cross_reference_checks(parsed: dict[str, object]) -> list[str]:
    errs: list[str] = []
    object_types = parsed.get("object_types.json") or {}
    link_types = parsed.get("link_types.json") or {}
    value_types = parsed.get("value_types.json") or {}

    object_api_names = set()
    if isinstance(object_types, dict):
        for ot in object_types.get("objectTypes", []) or []:
            api = ot.get("apiName")
            if api:
                object_api_names.add(api)

    value_api_names = set()
    if isinstance(value_types, dict):
        for vt in value_types.get("valueTypes", []) or []:
            api = vt.get("apiName")
            if api:
                value_api_names.add(api)

    if isinstance(link_types, dict):
        for lt in link_types.get("linkTypes", []) or []:
            for end in ("fromObjectType", "toObjectType"):
                ref = lt.get(end)
                if ref and ref not in object_api_names:
                    errs.append(
                        f"link {lt.get('apiName')} references unknown object type for {end}: {ref}"
                    )

    # enum:<valueType> property type references
    if isinstance(object_types, dict):
        for ot in object_types.get("objectTypes", []) or []:
            for prop in ot.get("properties", []) or []:
                t = prop.get("type", "")
                if isinstance(t, str) and t.startswith("enum:"):
                    ref = t.split(":", 1)[1]
                    if ref not in value_api_names:
                        errs.append(
                            f"object {ot.get('apiName')}.{prop.get('name')} references unknown valueType: {ref}"
                        )

    return errs


if __name__ == "__main__":
    sys.exit(main(sys.argv))
