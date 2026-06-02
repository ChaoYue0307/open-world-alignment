# 15-Minute Reviewer Checklist

## Claim and Scope

- Does `claim_type.description` state the capability, setting, and supervision boundary?
- Are supported and unsupported claims separated?
- Is the target-world outcome more specific than "better performance"?

## Human Signal

- What human labels, preferences, benchmarks, or judges are used?
- What can those signals verify?
- What can they not verify?

## Verifier Stack

- Is there a hard verifier for the central claim?
- Are soft verifiers labeled as soft?
- Does the card explain independence and correlated failure risks?

## Constraints and Frontier

- Are hard constraints operationalized as gates, thresholds, or named reviews?
- Does the card say where humans become weak supervisors?
- Are abstention or escalation conditions concrete?

## Stakeholders and Rollback

- Are affected non-users named?
- Is monitoring tied to rollback triggers?
- Is revision authority named?

## Decision

- Accept as strong evidence: hard verifiers, claim boundaries, constraints, and rollback are all concrete.
- Accept as limited evidence: structural fields are present but key claims need narrowing.
- Request revision: benchmark score is treated as open-world proof without boundaries.
