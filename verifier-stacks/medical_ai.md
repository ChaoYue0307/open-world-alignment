# Medical AI Verifier Stack

## Domain Claim

The system supports clinical triage, diagnosis, monitoring, or treatment planning under defined clinical governance.

## Human Signals

- Clinician review
- Patient-history interpretation
- Workflow usability feedback
- Expert panel review

## Human-Signal Limits

Humans are weak supervisors when evidence is incomplete, clinical context is hidden, rare conditions are involved, or downstream care pathways are affected.

## Hard Verifiers

- Clinical validation on representative cohorts
- Calibration by subgroup
- Safety and contraindication checks
- Audit of false negatives and false positives
- Prospective monitoring where appropriate

## Soft Verifiers

- Clinician plausibility review
- Patient-safety review
- Workflow-fit review

## Independence Rationale

Clinician review, statistical validation, subgroup analysis, and safety monitoring catch different medical failure modes.

## Verifier-Gaming Risks

- Optimizing aggregate accuracy while masking subgroup harm.
- Treating retrospective validation as prospective safety.
- Ignoring workflow-induced errors.
- Overstating clinical authority.

## Hard Constraints

- No autonomous diagnosis or treatment outside approved scope.
- No unsupported high-risk recommendation.
- No deployment without named clinical responsibility.

## Escalation Conditions

- High-acuity case
- Missing or conflicting clinical data
- Subgroup outside validation evidence
- Patient-safety concern

## Monitoring Signals

- Override rates
- Adverse events
- Subgroup performance drift
- Clinician escalation reports
- Patient-safety incidents

## Rollback Triggers

- Confirmed patient-safety incident
- Calibration failure in monitored subgroup
- Clinical owner withdraws approval
