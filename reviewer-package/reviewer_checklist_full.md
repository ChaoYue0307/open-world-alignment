# Full Reviewer Checklist

## Structural Completeness

- All eight required dimensions are present.
- Optional v0.2 metadata identifies status, version, authors, reviewers, dates, risk tier, and deployment stage.
- Evidence is tied to the stated system version and deployment stage.

## Claim Validity

- The claim is specific, scoped, and falsifiable.
- Supported and unsupported claims are explicit.
- The target-world state names the real-world outcome and failure definition.

## Human-Signal Limits

- Human labels, preferences, benchmarks, and judges are listed.
- The card distinguishes what human signals can verify from what they cannot.
- Synthetic judges are not treated as hard evidence without validation.

## Verifier Stack

- Hard verifiers directly test the claim.
- Soft verifiers add context but do not carry the claim alone.
- Independence rationale is credible.
- Verifier-gaming and correlated-failure risks are tested or acknowledged.

## Constraints

- Hard constraints are measurable or tied to named review gates.
- Override policy is explicit.
- Constraint violations appear in monitoring or rollback.

## Evaluator Frontier

- The card states where unaided humans become weak supervisors.
- Required tooling for review is listed.
- Abstention or escalation conditions are concrete.

## Stakeholders

- Affected non-users and future/downstream stakeholders are named.
- Representation mechanism is credible for the claim.
- Externalities are not silently excluded.

## Monitoring and Rollback

- Monitoring signals are specific.
- Rollback triggers are actionable.
- Revision authority and incident response path are named.
- Review frequency matches system risk.

## Final Reviewer Judgment

Score the card using the [maturity rubric](../rubrics/card_maturity_rubric.md), then state whether the paper should narrow, support, or withdraw each open-world claim.
