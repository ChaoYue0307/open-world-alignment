# Open-World Evaluation Card to NIST AI RMF Mapping

This mapping is a vocabulary bridge, not a compliance claim.

## Govern

- `authors`, `reviewers`, `card_status`, and `revision_authority` identify accountability.
- `hard_constraints.override_policy` states who can and cannot override constraints.
- `GOVERNANCE.md` defines repository-level stewardship.

## Map

- `claim_type`, `intended_use`, and `out_of_scope_uses` define system context.
- `absent_stakeholders` identifies affected parties not represented by ordinary user feedback.
- `deployment_stage` and `risk_tier` locate the card in a lifecycle.

## Measure

- `target_world_state` states the outcome and failure definition.
- `verifier_stack` lists evidence channels.
- `uncertainty` and `evaluator_frontier` identify evaluation limits.

## Manage

- `hard_constraints` records non-negotiable controls.
- `monitoring_and_rollback` connects signals to revision, suspension, or withdrawal.
- `evidence_bundle` records artifacts needed to reproduce or audit evidence.

## Limits

An Open-World Evaluation Card can support RMF-style reasoning, but it does not replace organizational risk management, legal review, sector-specific compliance, or post-deployment governance.
