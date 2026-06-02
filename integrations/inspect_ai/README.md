# Inspect AI Mapping

Inspect AI can provide structured evaluation tasks, solvers, scorers, and logs. In an Open-World Evaluation Card, it usually contributes to `verifier_stack`, `evidence_bundle`, and `claim_boundaries`.

## Useful Card Evidence

- Hard or soft verifier definitions through tasks and scorers.
- Reproducibility notes through eval configuration and logs.
- Unsupported-claim evidence when tasks are narrow or simulated.
- Verifier-gaming tests through held-out tasks or adversarial task variants.

## Limits

Inspect AI does not by itself establish deployment readiness, stakeholder representation, rollback authority, or long-horizon target-world outcomes. Those must be written in the card and supported by additional evidence.

## Recommended Card Fields

- `verifier_stack.hard_verifiers`
- `verifier_stack.external_tools_or_simulators`
- `evidence_bundle.eval_harnesses`
- `claim_boundaries.unsupported_claims`
- `monitoring_and_rollback.rollback_triggers`
