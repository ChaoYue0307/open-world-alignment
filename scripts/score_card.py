#!/usr/bin/env python3
"""Score Open-World Evaluation Card maturity."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from validate_card import load_card, validate_card


DIMENSIONS = [
    ("claim_specificity", "Claim specificity"),
    ("human_signal_limitation_clarity", "Human-signal limitation clarity"),
    ("verifier_stack_strength", "Verifier-stack strength"),
    ("verifier_independence", "Verifier independence"),
    ("hard_constraint_operationalization", "Hard-constraint operationalization"),
    ("evaluator_frontier_clarity", "Evaluator-frontier clarity"),
    ("absent_stakeholder_coverage", "Absent-stakeholder coverage"),
    ("monitoring_and_rollback_concreteness", "Monitoring and rollback concreteness"),
    ("evidence_reproducibility", "Evidence reproducibility"),
]


def words(value: Any) -> int:
    if isinstance(value, str):
        return len(value.split())
    if isinstance(value, list):
        return sum(words(item) for item in value)
    if isinstance(value, dict):
        return sum(words(item) for item in value.values())
    return 0


def list_len(card: dict[str, Any], *path: str) -> int:
    value: Any = card
    for key in path:
        value = value.get(key, {}) if isinstance(value, dict) else {}
    return len(value) if isinstance(value, list) else 0


def score_dimension(card: dict[str, Any], dimension: str) -> int:
    if dimension == "claim_specificity":
        base = words(card.get("claim_type", {}))
        boundaries = list_len(card, "claim_boundaries", "unsupported_claims")
        return min(3, int(base >= 20) + int(boundaries > 0) + int(list_len(card, "claim_boundaries", "supported_claims") > 0))
    if dimension == "human_signal_limitation_clarity":
        return min(3, int(words(card.get("human_signal_role", {}).get("human_signal_can_verify", "")) >= 5) + int(words(card.get("human_signal_role", {}).get("human_signal_cannot_verify", "")) >= 5) + int(words(card.get("human_signal_role", {}).get("role_in_decision", "")) >= 5))
    if dimension == "verifier_stack_strength":
        return min(3, int(list_len(card, "verifier_stack", "hard_verifiers") >= 2) + int(list_len(card, "verifier_stack", "soft_verifiers") >= 1) + int(list_len(card, "verifier_stack", "external_tools_or_simulators") >= 1))
    if dimension == "verifier_independence":
        return min(3, int(words(card.get("verifier_stack", {}).get("independence_rationale", "")) >= 8) + int(list_len(card, "verifier_stack", "verifier_gaming_tests") > 0) + int(list_len(card, "verifier_stack", "correlated_failure_risks") > 0))
    if dimension == "hard_constraint_operationalization":
        return min(3, int(list_len(card, "hard_constraints", "non_negotiable_constraints") >= 1) + int(words(card.get("hard_constraints", {}).get("enforcement_mechanism", "")) >= 5) + int(words(card.get("hard_constraints", {}).get("override_policy", "")) >= 3))
    if dimension == "evaluator_frontier_clarity":
        return min(3, int(words(card.get("evaluator_frontier", {}).get("where_humans_become_weak_supervisors", "")) >= 8) + int(list_len(card, "evaluator_frontier", "abstention_or_escalation_conditions") >= 1) + int(words(card.get("uncertainty", {}).get("abstention_policy", "")) >= 3))
    if dimension == "absent_stakeholder_coverage":
        return min(3, int(list_len(card, "absent_stakeholders", "affected_non_users") >= 1) + int(list_len(card, "absent_stakeholders", "future_or_downstream_stakeholders") >= 1) + int(words(card.get("absent_stakeholders", {}).get("representation_mechanism", "")) >= 5))
    if dimension == "monitoring_and_rollback_concreteness":
        return min(3, int(list_len(card, "monitoring_and_rollback", "deployment_signals_to_monitor") >= 2) + int(list_len(card, "monitoring_and_rollback", "rollback_triggers") >= 1) + int(words(card.get("monitoring_and_rollback", {}).get("revision_authority", "")) >= 3))
    if dimension == "evidence_reproducibility":
        bundle = card.get("evidence_bundle", {})
        return min(3, int(list_len(card, "evidence_bundle", "artifacts") > 0) + int(list_len(card, "evidence_bundle", "eval_harnesses") > 0) + int(words(bundle.get("reproducibility_notes", "")) >= 5))
    return 0


def score_card(card: Any) -> tuple[dict[str, int], list[str]]:
    errors = validate_card(card)
    if errors:
        return {}, errors
    assert isinstance(card, dict)
    return {key: score_dimension(card, key) for key, _ in DIMENSIONS}, []


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/score_card.py path/to/card.yaml", file=sys.stderr)
        return 2

    path = Path(argv[1])
    card = load_card(path)
    scores, errors = score_card(card)
    if errors:
        print(f"{path}: invalid")
        for error in errors:
            print(f"  - {error}")
        return 1

    total = sum(scores.values())
    max_score = len(DIMENSIONS) * 3
    weakest = sorted(scores.items(), key=lambda item: item[1])[:3]

    print("Open-World Card Maturity Report")
    print()
    print(f"Card: {path}")
    print("Structural validity: PASS")
    print(f"Maturity score: {total} / {max_score}")
    print("Weakest dimensions:")
    for key, value in weakest:
        label = dict(DIMENSIONS)[key]
        print(f"- {label}: {value} / 3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
