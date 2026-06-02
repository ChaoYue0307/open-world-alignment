# Robotics Verifier Stack

## Domain Claim

The system perceives, plans, or acts in a physical environment with safety-relevant consequences.

## Human Signals

- Operator review
- Task-success annotation
- Safety-zone review
- Usability feedback

## Human-Signal Limits

Humans are weak supervisors for rare physical failures, sensor blind spots, multi-agent interactions, and delayed maintenance effects.

## Hard Verifiers

- Simulation tests with scenario coverage
- Hardware-in-the-loop tests
- Safety interlock checks
- Geofence or workspace-boundary checks
- Incident and near-miss logs

## Soft Verifiers

- Operator review
- Human-factors review
- Task-quality review

## Independence Rationale

Simulation, physical trials, and operator review cover different parts of the physical-risk surface.

## Verifier-Gaming Risks

- Overfitting to simulator assumptions.
- Ignoring rare edge cases.
- Treating task completion as safety.
- Missing human co-worker exposure.

## Hard Constraints

- No operation outside validated workspace.
- No disabled safety interlocks.
- No autonomous action when uncertainty exceeds threshold.

## Escalation Conditions

- Sensor uncertainty
- Human enters operating zone
- Simulation-to-real mismatch
- Unexpected force or trajectory

## Monitoring Signals

- Near misses
- Safety-stop events
- Sensor faults
- Maintenance reports
- Operator overrides

## Rollback Triggers

- Safety interlock failure
- Unreviewed workspace expansion
- Repeated near misses above threshold
