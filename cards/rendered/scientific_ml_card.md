# Open-World Evaluation Card: Scientific ML hypothesis generator

## Summary

A system that generates scientific hypotheses, candidate mechanisms, or predicted structures for expert review and experimental follow-up.

## Supported Claim

- The system can propose candidates that merit validation under the stated scientific protocol.

## Unsupported Claims

- The system establishes causal truth without validation.
- The system replaces domain expert review.
- A simulation result alone establishes real-world validity.

## Target World State

The system should improve scientific discovery by proposing candidates that survive domain-appropriate validation and reduce wasted experimental effort.

Evidence required: Experimental validation, replication, simulation fidelity, physical-law checks, held-out prediction performance, uncertainty calibration, and expert interpretation.

Failure definition: A material failure includes fabricated evidence, unsupported causal claims, invalid simulations, non-replicable findings, unsafe experimental recommendations, or unreported uncertainty.

## Human-Signal Limits

Can verify: Experts can judge plausibility, relevance, novelty framing, experimental feasibility, and interpretation of validation evidence.

Cannot verify unaided: Unaided experts may not verify hidden data leakage, physical validity, expensive experimental outcomes, long-horizon replication, or causal mechanism.

Role in decision: Human signals frame the scientific question, select validation priorities, and interpret evidence, but empirical and physical verifiers decide whether claims are supported.

## Verifier Stack

### Hard Verifiers

- Held-out predictive performance
- Experimental replication
- Simulation fidelity checks
- Physical-law consistency checks
- Data leakage checks
- Safety and biosafety review where applicable

### Soft Verifiers

- Expert plausibility review
- Novelty assessment
- Interpretability review
- Experimental feasibility review

### Independence Rationale

The stack separates expert plausibility from empirical validation, simulation from experiment, benchmark performance from replication, and novelty assessment from safety gates.

## Hard Constraints

- No fabricated evidence
- No unsupported causal claim presented as established
- No unsafe experimental recommendation
- No hidden data leakage
- No violation of domain safety or resource limits

Enforcement: Block claims or downstream recommendations when validation, leakage, safety, or uncertainty gates fail.

Override policy: No override for fabricated evidence, safety violations, or data leakage. Scientific uncertainty must be reported rather than suppressed.

## Evaluator Frontier

Humans become weak supervisors when candidates require costly validation, complex physical reasoning, hidden data audits, or long-horizon replication.

Escalation conditions:

- Uncertainty is high
- Validation evidence conflicts
- Candidate touches safety-sensitive domain
- Data provenance is unclear
- Simulation assumptions are violated
- Replication fails or is unavailable

## Absent Stakeholders

### Affected non-users

- Experimental participants or affected communities
- Laboratory staff
- Downstream practitioners
- People affected by premature scientific claims

### Future or downstream stakeholders

- Future researchers building on the claim
- Institutions allocating resources based on results
- Patients, ecosystems, or communities affected by application
- Replication teams

Representation: Represent stakeholders through ethics review, safety review, replication norms, uncertainty reporting, and clear limits on unsupported claims.

## Monitoring and Rollback

### Signals

- Replication outcomes
- Failed validation attempts
- Safety incidents
- Retractions or corrections
- Resource use
- Downstream misuse or overclaiming
- Calibration drift

### Rollback triggers

- Failed independent replication
- Confirmed data leakage
- Safety violation
- Evidence of fabricated or invalid validation
- Material uncertainty omitted from reported claim

Revision authority: Project leads, safety reviewers, ethics boards, or publication owners can revise, suspend, retract, or withdraw the claim.
