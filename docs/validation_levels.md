# Validation Levels

Structural validity is only the first step. Open-World Evaluation Cards should also be assessed for evidence quality, deployment awareness, and audit readiness.

## Level 0: Structurally Valid

The card includes all required fields and passes `scripts/validate_card.py`.

Minimum expectation:

- all eight required dimensions exist;
- required strings and lists are non-empty;
- the file is parseable as JSON-compatible YAML or YAML.

## Level 1: No Placeholders

The card contains no placeholder text such as "replace with", "TBD", or empty generic claims.

Minimum expectation:

- system claim is concrete;
- human-signal limits are stated;
- rollback authority is named.

## Level 2: Evidence-Aware

The card identifies concrete verifiers and constraints.

Minimum expectation:

- hard and soft verifiers are separated;
- unsupported claims are stated;
- at least one verifier-gaming or correlated-failure risk is described;
- constraints are operational rather than purely narrative.

## Level 3: Deployment-Aware

The card connects evaluation to post-deployment evidence.

Minimum expectation:

- monitoring signals are concrete;
- rollback triggers are event- or threshold-based;
- review frequency or incident response path is stated;
- revision authority is assigned to a role or institution.

## Level 4: Audit-Ready

The card includes enough provenance for external review.

Minimum expectation:

- evidence bundle links to artifacts, datasets, harnesses, or reports;
- stakeholder representation is explicit;
- reproducibility notes are included;
- reviewers and card status are recorded.

These levels are quality signals, not safety certifications.
