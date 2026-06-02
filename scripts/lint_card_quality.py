#!/usr/bin/env python3
"""Quality linting for Open-World Evaluation Cards."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from validate_card import load_card, validate_card


PLACEHOLDERS = ("replace with", "tbd", "todo", "n/a", "not applicable")
VAGUE_TERMS = ("good", "robust", "safe", "aligned", "high quality", "best")


def walk_values(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for value_item in value for item in walk_values(value_item)]
    if isinstance(value, dict):
        return [item for value_item in value.values() for item in walk_values(value_item)]
    return []


def has_meaningful_list(card: dict[str, Any], path: tuple[str, ...]) -> bool:
    value: Any = card
    for key in path:
        if not isinstance(value, dict) or key not in value:
            return False
        value = value[key]
    return isinstance(value, list) and len([item for item in value if str(item).strip()]) > 0


def lint_card(card: Any) -> list[str]:
    errors = validate_card(card)
    if errors:
        return errors

    assert isinstance(card, dict)
    texts = walk_values(card)
    lowered = [text.lower().strip() for text in texts]

    for text in lowered:
        if any(marker in text for marker in PLACEHOLDERS):
            errors.append("quality: placeholder text remains")
            break

    claim = card.get("claim_type", {}).get("description", "").lower()
    if any(term == claim.strip() for term in VAGUE_TERMS) or len(claim.split()) < 6:
        errors.append("claim_type.description: claim is too vague")

    if not has_meaningful_list(card, ("claim_boundaries", "unsupported_claims")):
        errors.append("claim_boundaries.unsupported_claims: missing unsupported claims")

    rollback = card.get("monitoring_and_rollback", {})
    authority = str(rollback.get("revision_authority", "")).lower()
    if not authority or authority in {"owner", "team", "someone"}:
        errors.append("monitoring_and_rollback.revision_authority: authority is too vague")

    triggers = rollback.get("rollback_triggers", [])
    trigger_text = " ".join(str(item).lower() for item in triggers)
    if not triggers or trigger_text in {"monitoring", "issues", "problems"}:
        errors.append("monitoring_and_rollback.rollback_triggers: triggers are too vague")

    if not has_meaningful_list(card, ("verifier_stack", "hard_verifiers")):
        errors.append("verifier_stack.hard_verifiers: missing hard verifiers")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python scripts/lint_card_quality.py path/to/card.yaml [...]", file=sys.stderr)
        return 2

    failed = False
    for arg in argv[1:]:
        path = Path(arg)
        try:
            card = load_card(path)
        except ValueError as error:
            print(f"{path}: invalid")
            print(f"  - {error}")
            failed = True
            continue

        errors = lint_card(card)
        if errors:
            print(f"{path}: quality lint failed")
            for error in errors:
                print(f"  - {error}")
            failed = True
        else:
            print(f"{path}: quality lint passed")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
