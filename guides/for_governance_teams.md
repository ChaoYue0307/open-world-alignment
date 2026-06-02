# Guide for Governance Teams

Use cards to connect evaluation claims to ownership, review, monitoring, and revision.

## Workflow

1. Require a card for high-risk benchmark, deployment, or beyond-human claims.
2. Check `risk_tier`, `deployment_stage`, `reviewers`, and `revision_authority`.
3. Map card fields to your governance vocabulary using the [NIST AI RMF mapping](../integrations/nist_ai_rmf/owa_to_nist_ai_rmf.md).
4. Require hard constraints and rollback triggers before pilot or production use.
5. Track review frequency and evidence staleness.

## Governance Questions

- Who owns the claim after deployment?
- Which signal forces revision rather than observation?
- What evidence must be preserved for audit?
- What affected stakeholder is outside direct user feedback?

## Useful Artifacts

- [Validation levels](../docs/validation_levels.md)
- [Governance file](../GOVERNANCE.md)
- [Full reviewer checklist](../reviewer-package/reviewer_checklist_full.md)
