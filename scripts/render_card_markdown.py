#!/usr/bin/env python3
"""Render an Open-World Evaluation Card YAML file as Markdown."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from validate_card import load_card, validate_card


def bullet_list(items: Any) -> str:
    if not isinstance(items, list) or not items:
        return "- Not specified"
    return "\n".join(f"- {item}" for item in items)


def section(title: str, body: str) -> str:
    return f"## {title}\n\n{body.strip()}\n"


def render(card: dict[str, Any]) -> str:
    claim = card.get("claim_type", {})
    target = card.get("target_world_state", {})
    human = card.get("human_signal_role", {})
    verifiers = card.get("verifier_stack", {})
    constraints = card.get("hard_constraints", {})
    frontier = card.get("evaluator_frontier", {})
    absent = card.get("absent_stakeholders", {})
    rollback = card.get("monitoring_and_rollback", {})
    boundaries = card.get("claim_boundaries", {})

    parts = [f"# Open-World Evaluation Card: {card.get('system_name', 'Unnamed Card')}\n"]
    parts.append(section("Summary", card.get("system_description", "No description provided.")))
    parts.append(section("Supported Claim", bullet_list(boundaries.get("supported_claims", [claim.get("description", "Not specified")]))))
    parts.append(section("Unsupported Claims", bullet_list(boundaries.get("unsupported_claims", []))))
    parts.append(section("Target World State", f"{target.get('intended_real_world_outcome', '')}\n\nEvidence required: {target.get('evidence_required', '')}\n\nFailure definition: {target.get('failure_definition', '')}"))
    parts.append(section("Human-Signal Limits", f"Can verify: {human.get('human_signal_can_verify', '')}\n\nCannot verify unaided: {human.get('human_signal_cannot_verify', '')}\n\nRole in decision: {human.get('role_in_decision', '')}"))
    parts.append(section("Verifier Stack", f"### Hard Verifiers\n\n{bullet_list(verifiers.get('hard_verifiers'))}\n\n### Soft Verifiers\n\n{bullet_list(verifiers.get('soft_verifiers'))}\n\n### Independence Rationale\n\n{verifiers.get('independence_rationale', '')}"))
    parts.append(section("Hard Constraints", f"{bullet_list(constraints.get('non_negotiable_constraints'))}\n\nEnforcement: {constraints.get('enforcement_mechanism', '')}\n\nOverride policy: {constraints.get('override_policy', '')}"))
    parts.append(section("Evaluator Frontier", f"{frontier.get('where_humans_become_weak_supervisors', '')}\n\nEscalation conditions:\n\n{bullet_list(frontier.get('abstention_or_escalation_conditions'))}"))
    parts.append(section("Absent Stakeholders", f"### Affected non-users\n\n{bullet_list(absent.get('affected_non_users'))}\n\n### Future or downstream stakeholders\n\n{bullet_list(absent.get('future_or_downstream_stakeholders'))}\n\nRepresentation: {absent.get('representation_mechanism', '')}"))
    parts.append(section("Monitoring and Rollback", f"### Signals\n\n{bullet_list(rollback.get('deployment_signals_to_monitor'))}\n\n### Rollback triggers\n\n{bullet_list(rollback.get('rollback_triggers'))}\n\nRevision authority: {rollback.get('revision_authority', '')}"))
    return "\n".join(parts)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/render_card_markdown.py path/to/card.yaml", file=sys.stderr)
        return 2

    path = Path(argv[1])
    card = load_card(path)
    errors = validate_card(card)
    if errors:
        print(f"{path}: invalid", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    assert isinstance(card, dict)
    sys.stdout.write(render(card).rstrip() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
