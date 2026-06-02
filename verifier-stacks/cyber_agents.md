# Cyber Agent Verifier Stack

## Domain Claim

The system assists defensive cybersecurity evaluation only in authorized environments.

## Human Signals

- Security-owner authorization
- Analyst review
- Report-quality review
- Incident-response review

## Human-Signal Limits

Humans are weak supervisors for hidden tool side effects, ambiguous authorization scope, sensitive-data exposure, and fast-changing operational context.

## Hard Verifiers

- Authorization-scope check
- Tool-permission gate
- Sensitive-data handling check
- Audit-log completeness check
- Policy compliance check

## Soft Verifiers

- Security analyst review
- Risk-owner review
- Report clarity review

## Independence Rationale

Authorization records, permission gates, logs, and human review constrain different security risks.

## Verifier-Gaming Risks

- Treating vague authorization as sufficient.
- Optimizing report plausibility while hiding uncertainty.
- Incomplete logs masking unsafe recommendations.
- Scope drift across assets or environments.

## Hard Constraints

- No unauthorized target interaction.
- No operational attack guidance.
- No sensitive-data leakage.
- No high-risk tool action without approval.

## Escalation Conditions

- Authorization unclear
- Sensitive data detected
- High-risk action requested
- Scope boundary ambiguous

## Monitoring Signals

- Authorization failures
- Sensitive-data events
- Policy violations
- Analyst escalations
- Audit-log gaps

## Rollback Triggers

- Unauthorized interaction
- Sensitive-data leakage
- High-risk unapproved action
- Security owner invalidates the evidence
