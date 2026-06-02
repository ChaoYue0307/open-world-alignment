# Open-World Evaluation Card Specification

Version: 0.2

The Open-World Evaluation Card is a reporting artifact for AI systems, benchmarks, or deployment settings whose capability claims exceed direct unaided human supervision.

A card is valid when it makes explicit:

1. what is being claimed;
2. what world state the claim is about;
3. what human signals can and cannot verify;
4. what verifier stack tests the claim;
5. what constraints cannot be traded away;
6. where unaided humans become weak supervisors;
7. which stakeholders are absent from the rating loop;
8. what monitoring evidence can trigger revision, rollback, or withdrawal.

## Scope

Use this specification for research artifacts, benchmark reports, model or system cards, deployment reports, and review checklists where human-facing approval is insufficient evidence for the stated claim.

Do not use the card as a substitute for domain-specific safety, legal, privacy, medical, security, or regulatory review. The card records evidence and limits; it does not certify a system as safe.

## Required Fields

Every Open-World Evaluation Card must include:

- `schema_version`
- `system_name`
- `claim_type`
- `target_world_state`
- `human_signal_role`
- `verifier_stack`
- `hard_constraints`
- `evaluator_frontier`
- `absent_stakeholders`
- `monitoring_and_rollback`

The eight substantive fields are mandatory because omitting any one of them recreates a common failure mode: overbroad claims, human-signal monism, verifier omission, constraint erasure, absent-stakeholder exclusion, or deployment blindness.

## Optional Audit Metadata

Schema v0.2 adds optional metadata for audit-ready cards:

- `card_id`
- `card_status`
- `system_version`
- `authors`
- `reviewers`
- `date_created`
- `date_updated`
- `risk_tier`
- `deployment_stage`
- `intended_use`
- `out_of_scope_uses`
- `evidence_bundle`
- `claim_boundaries`
- `uncertainty`

Optional metadata should be used when a card is attached to a paper, benchmark, model release, deployment review, or audit packet.

## Validation Levels

- Level 0: structurally valid.
- Level 1: no placeholders and all required fields are concrete.
- Level 2: evidence-aware, with concrete verifiers and constraints.
- Level 3: deployment-aware, with monitoring signals and rollback authority.
- Level 4: audit-ready, with evidence provenance, stakeholder representation, and reproducibility links.

See `docs/validation_levels.md` for scoring guidance.

## Versioning Policy

Minor schema versions may add optional fields. Required fields should not be removed before v1.0. Cards written for schema v0.1 remain structurally valid under v0.2 if they include the eight required dimensions.

## Compatibility Guarantees

The repository validator treats the eight core dimensions as the compatibility boundary. Optional fields are accepted for extensibility. Quality tools may warn about missing v0.2 metadata, but structural validation should remain backward-compatible for v0.1 cards.

## Valid and Invalid Claims

Strong claim:

> The system resolves repository-level bug-fix issues in Python packages with executable tests, documented reproduction steps, and maintainer review.

Weak claim:

> The system can autonomously code.

Strong claim:

> The benchmark supports claims about short-horizon factual QA under its dataset distribution. It does not support claims about long-horizon planning, deployment safety, or resistance to misuse.

Weak claim:

> The benchmark measures general intelligence.

## Citation

If you use this specification or the accompanying templates, cite the toolkit using the BibTeX entry in `README.md` or `CITATION.cff`.
