# Guide for Reviewers

Use this repository to check whether the evidence in a paper supports its open-world claim.

## Workflow

1. Start with the [5-minute checklist](../reviewer-package/reviewer_checklist_5min.md).
2. If the claim is broad, use the [15-minute checklist](../reviewer-package/reviewer_checklist_15min.md).
3. Score artifact quality with the [reviewer rubric](../rubrics/reviewer_rubric.md).
4. Map concerns to the [failure-mode library](../failure-modes/README.md).
5. Ask authors to narrow unsupported claims or add verifier evidence.

## Common Review Outcomes

- Strong: card has concrete claim boundaries, hard verifiers, constraints, and rollback.
- Limited: card supports a benchmark result but not deployment or safety claims.
- Weak: card relies on human approval, model judges, or aggregate score without independence.

## Review Language

"The evidence supports the reported evaluation result, but not the broader open-world claim as stated. Please separate supported and unsupported claims, add verifier independence rationale, and name rollback authority."
