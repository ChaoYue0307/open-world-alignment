# Foundation Model Verifier Stack

## Domain Claim

The system provides general-purpose language, multimodal, or tool-use capabilities across many user contexts.

## Human Signals

- Helpfulness preferences
- Instruction-following judgments
- Expert review
- User feedback
- Policy interpretation

## Human-Signal Limits

Humans are weak supervisors for specialized factual claims, long-horizon consequences, hidden tool effects, adversarial misuse analysis, and ecosystem-level impact.

## Hard Verifiers

- Retrieval-grounded factuality checks
- Citation fidelity checks
- Tool-use success and side-effect checks
- Privacy leakage tests
- Misuse-risk evaluations
- Resource and energy accounting

## Soft Verifiers

- Expert review
- Red-team review
- User-feedback review
- Model-generated critique used only as advisory evidence

## Independence Rationale

Preference ratings, factual checks, policy checks, and incident monitoring test different constructs and should be reported separately.

## Verifier-Gaming Risks

- Model optimizes for rated helpfulness while hiding uncertainty.
- Synthetic judges share model blind spots.
- Retrieval evidence is cited but not faithfully used.
- Aggregate score masks severe subgroup or domain failures.

## Hard Constraints

- No prohibited privacy leakage.
- No severe misuse enablement under the stated policy.
- No undisclosed policy override.
- No unacceptable resource or compute-budget violation.

## Escalation Conditions

- High-impact domain query
- Conflicting evidence
- Missing source trace
- Policy boundary ambiguity
- Tool action with irreversible effects

## Monitoring Signals

- Abuse reports
- Factuality incident reports
- Policy violation rates
- Privacy incidents
- Resource consumption

## Rollback Triggers

- Repeated severe policy failures
- Confirmed privacy incident
- Tool side effect outside authorized scope
- Monitoring owner withdraws support for the release claim
