# Open-World Evaluation Card: General-purpose foundation model assistant

## Summary

A foundation model deployed as an assistant for information seeking, writing, code help, and tool use.

## Supported Claim

- The assistant is evaluated for helpfulness, factuality, tool use, privacy, and misuse resistance under the stated settings.

## Unsupported Claims

- The assistant is generally truthful in all domains.
- The assistant is safe for unsupported high-stakes use.
- User preference alone establishes alignment.

## Target World State

Users should receive helpful, truthful, policy-compliant assistance without unacceptable misuse, privacy leakage, or hidden resource externalities.

Evidence required: Factuality tests, citation checks, tool-use success rates, privacy leakage tests, misuse evaluations, expert review, user feedback, incident reports, and resource accounting.

Failure definition: A material failure includes severe factual harm, privacy leakage, unsafe misuse assistance, unauthorized data exposure, repeated tool-use failure, or deployment incidents above agreed thresholds.

## Human-Signal Limits

Can verify: Human signals can assess usefulness, clarity, instruction following, policy interpretation, and whether answers appear responsive to user intent.

Cannot verify unaided: Unaided humans may not reliably verify hidden factual errors, source fidelity, privacy leakage, tool side effects, misuse pathways, or long-horizon social impact.

Role in decision: Human signals inform training, preference tuning, policy evaluation, deployment monitoring, and escalation, but do not replace factual, safety, privacy, and resource checks.

## Verifier Stack

### Hard Verifiers

- Privacy leakage tests
- Misuse policy evaluations
- Tool execution checks
- Citation fidelity checks for retrieval-backed answers
- Security red-team findings above severity threshold

### Soft Verifiers

- Helpfulness review
- Expert qualitative review
- Readability review
- User satisfaction feedback

### Independence Rationale

The stack separates user preference from expert review, judge-model outputs from factual checks, offline tests from deployment telemetry, and safety gates from aggregate helpfulness scores.

## Hard Constraints

- No prohibited privacy leakage
- No severe misuse enablement under defined threat models
- No unauthorized access to external tools or data
- No undisclosed policy override
- No deployment without incident-response ownership

Enforcement: Block release or model update when hard safety, privacy, or tool-use gates fail; require documented owner approval for high-risk deployment changes.

Override policy: No automatic override. Exceptions require documented review by the responsible safety, privacy, or deployment owner.

## Evaluator Frontier

Humans become weak supervisors when outputs require domain expertise, source verification, adversarial analysis, tool-state inspection, or delayed impact assessment.

Escalation conditions:

- High-stakes medical, legal, financial, security, or safety-sensitive request
- Missing or conflicting sources
- Tool state cannot be inspected
- Policy uncertainty is high
- Privacy risk is detected
- Verifier disagreement is high

## Absent Stakeholders

### Affected non-users

- People whose data appears in context
- People affected by user decisions made with model assistance
- Moderation and incident response teams
- Communities affected by generated misinformation or misuse

### Future or downstream stakeholders

- Future users exposed to model updates
- Organizations integrating the assistant
- People affected by downstream publication or automation
- Infrastructure and resource stakeholders

Representation: Represent absent stakeholders through policy review, privacy review, red-team evaluation, abuse reporting, incident analysis, and resource accounting.

## Monitoring and Rollback

### Signals

- Abuse reports
- Privacy incidents
- Factuality incident reports
- Tool-use failures
- Policy violation rates
- User appeals
- Resource consumption
- Rollback and mitigation records

### Rollback triggers

- Severe privacy leakage
- Confirmed high-severity misuse enablement
- Incident rate above pre-specified threshold
- Critical tool-use failure
- Policy gate invalidated by audit

Revision authority: Safety, privacy, security, and deployment owners can pause, restrict, roll back, or withdraw the model or specific capabilities.
