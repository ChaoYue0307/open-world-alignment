# Open-World Evaluation Cards

An Open-World Evaluation Card is a reporting artifact for systems or benchmarks whose claims exceed direct human supervision.

Use a card when a system's outputs are consequential and unaided humans may be unable to reliably generate, rank, verify, or forecast the relevant candidates and downstream effects.

## Required Dimensions

1. `claim_type`: the capability claim and where unaided supervision becomes weak.
2. `target_world_state`: the outcome the system is supposed to improve.
3. `human_signal_role`: labels, preferences, ratings, benchmarks, judge models, and their limits.
4. `verifier_stack`: hard checks, soft checks, human review channels, and external tools.
5. `hard_constraints`: requirements that cannot be traded away for score or approval.
6. `evaluator_frontier`: abstention, escalation, and stronger-verification conditions.
7. `absent_stakeholders`: affected parties outside the direct rating loop.
8. `monitoring_and_rollback`: deployment signals, rollback triggers, and revision authority.

## Quality Bar

A strong card should:

- scope the claim narrowly enough that it can be evaluated;
- state what human-facing evidence can and cannot verify;
- separate hard verifiers from soft advisory checks;
- keep non-negotiable constraints outside aggregate scores;
- identify affected non-users and delayed externalities;
- define mechanical escalation or rollback triggers;
- name the role or institution with authority to pause, revise, or withdraw the system.

## Common Failure Modes

- Treating a benchmark score as proof of a broad capability claim.
- Listing judge models as independent verifiers without explaining inherited blind spots.
- Mentioning safety, privacy, rights, or sustainability as prose values without operational gates.
- Monitoring incidents without assigning rollback authority.
- Omitting stakeholders who bear consequences but never rate the system.

## Examples

- [Coding agent](examples/coding_agent_card.yaml): detailed reference example for repository-level issue resolution.
- [Foundation model](examples/foundation_model_card.yaml): factuality, misuse, privacy, resource, and deployment monitoring checks.
- [Scientific ML](examples/scientific_ml_card.yaml): experimental validation, replication, physical constraints, and scientific uncertainty.
- [Forecasting](examples/forecasting_card.yaml): calibration, out-of-sample accuracy, operational thresholds, and decision monitoring.

## Validation

Validate a card with:

```bash
python scripts/validate_card.py cards/examples/coding_agent_card.yaml
```

Validate every example:

```bash
find cards -name '*.yaml' -print0 | xargs -0 -n1 python scripts/validate_card.py
```
