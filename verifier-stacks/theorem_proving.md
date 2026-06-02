# Theorem Proving Verifier Stack

## Domain Claim

The system proposes formal proof steps or complete proofs for a specified theorem-proving environment.

## Human Signals

- Theorem relevance review
- Proof strategy review
- Readability review
- Library-maintainer feedback

## Human-Signal Limits

Humans are weak supervisors for long formal proof states, hidden assumptions, tactic behavior, and library-version dependencies.

## Hard Verifiers

- Theorem-prover acceptance
- Proof replay
- Library version checks
- Held-out theorem evaluation
- Dependency graph inspection

## Soft Verifiers

- Mathematician review
- Formal-methods reviewer comments
- Proof readability review

## Independence Rationale

Formal checking establishes syntactic and logical validity under an environment; human review establishes usefulness and interpretability.

## Verifier-Gaming Risks

- Benchmark contamination.
- Library-specific shortcuts.
- Hidden assumptions outside stated environment.
- Natural-language proof sketch mistaken for formal proof.

## Hard Constraints

- No correctness claim without proof-checker acceptance.
- No hidden assumptions outside the stated environment.
- No benchmark result without library version record.

## Escalation Conditions

- Proof replay fails
- Dependencies are unclear
- Theorem is outside validated library

## Monitoring Signals

- Proof replay failures
- Library incompatibilities
- Reported invalid assumptions

## Rollback Triggers

- Proof checker rejects the artifact
- Dependency invalidates the proof
- Benchmark contamination is found
