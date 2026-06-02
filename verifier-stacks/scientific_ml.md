# Scientific ML Verifier Stack

## Domain Claim

The system generates hypotheses, predictions, structures, simulations, or interventions whose value depends on empirical, mathematical, or physical validation.

## Human Signals

- Research-goal selection
- Hypothesis framing
- Experimental-design judgment
- Domain-expert review
- Interpretation of evidence

## Human-Signal Limits

Humans are weak supervisors when outputs require expensive experiments, specialized instrumentation, long-horizon validation, or formal checks that cannot be inferred from plausibility.

## Hard Verifiers

- Experimental validation
- Replication
- Simulation fidelity checks
- Physical-law consistency checks
- Theorem checking where applicable
- Out-of-sample predictive performance
- Calibration and uncertainty evaluation

## Soft Verifiers

- Domain-expert plausibility review
- Novelty review
- Research-utility review
- Peer review

## Independence Rationale

Human plausibility, simulation, experiment, and formal checking fail in different ways and should be cross-checked before strong claims are made.

## Verifier-Gaming Risks

- Optimizing against a proxy assay.
- Reporting only favorable simulations.
- Treating correlation as causal evidence.
- Reusing contaminated datasets or benchmark splits.

## Hard Constraints

- No fabricated evidence.
- No unsupported causal claim.
- No safety or biosafety violation.
- No deployment without domain-appropriate review.

## Escalation Conditions

- High-risk intervention proposal
- Missing replication path
- Material uncertainty about external validity
- Conflict between simulation and experiment

## Monitoring Signals

- Replication outcomes
- Failed validation attempts
- Downstream experimental incidents
- Calibration drift
- Corrections, audit findings, or withdrawals

## Rollback Triggers

- Failed critical replication
- Invalidated dataset or analysis pipeline
- Safety reviewer rejects the protocol
- Claim no longer matches available evidence
