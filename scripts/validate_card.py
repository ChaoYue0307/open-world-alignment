#!/usr/bin/env python3
"""Validate an Open-World Evaluation Card.

The repository templates are JSON-compatible YAML, so the validator works with
Python's standard library. If PyYAML is installed, ordinary YAML files are also
accepted.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_STRUCTURE: dict[str, dict[str, type]] = {
    "claim_type": {
        "description": str,
        "beyond_human_claim": bool,
        "claim_scope": str,
        "supervision_boundary": str,
    },
    "target_world_state": {
        "intended_real_world_outcome": str,
        "evidence_required": str,
        "failure_definition": str,
    },
    "human_signal_role": {
        "labels_used": bool,
        "preferences_used": bool,
        "benchmarks_or_judges": list,
        "human_signal_can_verify": str,
        "human_signal_cannot_verify": str,
        "role_in_decision": str,
    },
    "verifier_stack": {
        "hard_verifiers": list,
        "soft_verifiers": list,
        "human_review_channels": list,
        "external_tools_or_simulators": list,
        "independence_rationale": str,
    },
    "hard_constraints": {
        "non_negotiable_constraints": list,
        "enforcement_mechanism": str,
        "override_policy": str,
    },
    "evaluator_frontier": {
        "where_humans_become_weak_supervisors": str,
        "required_tooling_for_human_review": str,
        "abstention_or_escalation_conditions": list,
    },
    "absent_stakeholders": {
        "affected_non_users": list,
        "future_or_downstream_stakeholders": list,
        "representation_mechanism": str,
    },
    "monitoring_and_rollback": {
        "deployment_signals_to_monitor": list,
        "rollback_triggers": list,
        "revision_authority": str,
    },
}

TOP_LEVEL_REQUIRED: dict[str, type] = {
    "schema_version": str,
    "system_name": str,
}


def load_card(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError as json_error:
        try:
            import yaml  # type: ignore
        except ImportError as import_error:
            raise ValueError(
                "Card is not JSON-compatible YAML, and PyYAML is not installed. "
                "Use the repository template format or install PyYAML."
            ) from import_error

        try:
            return yaml.safe_load(text)
        except Exception as yaml_error:  # pragma: no cover - depends on PyYAML
            raise ValueError(f"Could not parse {path}: {yaml_error}") from json_error


def is_non_empty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_non_empty_list(value: object) -> bool:
    if not isinstance(value, list) or not value:
        return False
    return all(item is not None and (not isinstance(item, str) or bool(item.strip())) for item in value)


def validate_field(path: str, value: object, expected_type: type) -> list[str]:
    errors: list[str] = []

    if not isinstance(value, expected_type):
        errors.append(f"{path}: expected {expected_type.__name__}, got {type(value).__name__}")
        return errors

    if expected_type is str and not is_non_empty_string(value):
        errors.append(f"{path}: must be a non-empty string")
    elif expected_type is list and not is_non_empty_list(value):
        errors.append(f"{path}: must be a non-empty list")

    return errors


def validate_card(card: Any) -> list[str]:
    errors: list[str] = []

    if not isinstance(card, dict):
        return ["card: expected top-level object"]

    for key, expected_type in TOP_LEVEL_REQUIRED.items():
        if key not in card:
            errors.append(f"{key}: missing required top-level field")
            continue
        errors.extend(validate_field(key, card[key], expected_type))

    for section, fields in REQUIRED_STRUCTURE.items():
        if section not in card:
            errors.append(f"{section}: missing required section")
            continue

        section_value = card[section]
        if not isinstance(section_value, dict):
            errors.append(f"{section}: expected object, got {type(section_value).__name__}")
            continue

        for field, expected_type in fields.items():
            full_path = f"{section}.{field}"
            if field not in section_value:
                errors.append(f"{full_path}: missing required field")
                continue
            errors.extend(validate_field(full_path, section_value[field], expected_type))

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/validate_card.py path/to/card.yaml", file=sys.stderr)
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2

    try:
        card = load_card(path)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    errors = validate_card(card)
    if errors:
        print(f"{path}: invalid")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"{path}: valid")
    for section in REQUIRED_STRUCTURE:
        print(f"  ok {section}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
