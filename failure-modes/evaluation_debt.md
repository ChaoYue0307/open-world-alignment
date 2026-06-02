# Evaluation Debt

## Definition

Evaluation coverage lags behind system capability, deployment scope, or known failure modes, causing old evidence to support new claims.

## Warning Signs

- The card has no review frequency or update path.
- The system version changes but evidence does not.
- Known failures are deferred without scoped limits.

## Card Fields Affected

- `system_version`
- `evidence_bundle`
- `monitoring_and_rollback`
- `uncertainty`

## Mitigation Checklist

- Bind evidence to system version and deployment stage.
- Track review frequency and stale evidence.
- Require re-validation after major model, data, policy, or tool changes.
- Treat unresolved critical gaps as unsupported claims.

## Reviewer Questions

- Does the evidence match the current system version?
- What changed since the evidence was collected?
- Which claim becomes invalid when evaluation is stale?

## Related Resources

- [Monitoring and rollback](../awesome/monitoring_and_rollback.md)
- [Governance and auditing](../awesome/governance_and_auditing.md)
