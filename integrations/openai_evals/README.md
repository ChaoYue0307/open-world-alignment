# OpenAI Evals Mapping

OpenAI Evals-style harnesses can contribute task definitions, model outputs, scoring logic, and reproducibility records. Treat them as evidence channels, not as a complete open-world claim.

## Useful Card Evidence

- Benchmark or judge definitions for `human_signal_role.benchmarks_or_judges`.
- Scoring logic for `verifier_stack`.
- Run logs for `evidence_bundle`.
- Failure cases for `claim_boundaries.known_failure_modes`.

## Limits

A single eval harness does not establish broad safety, alignment, deployment readiness, or real-world benefit. Model-graded evals should be marked as soft verifiers unless validated against independent evidence.

## Recommended Card Fields

- `human_signal_role`
- `verifier_stack.soft_verifiers`
- `verifier_stack.independence_rationale`
- `claim_boundaries.unsupported_claims`
- `uncertainty.known_unknowns`
