# Constraint Erasure

## Definition

Hard constraints are described in prose but do not affect scoring, deployment gates, abstention, or rollback.

## Warning Signs

- Constraints are listed but no enforcement mechanism is named.
- The result can improve while violating stated constraints.
- Overrides are possible without named authority.

## Card Fields Affected

- `hard_constraints`
- `monitoring_and_rollback`
- `claim_boundaries`

## Mitigation Checklist

- Convert constraints into measurable gates or review requirements.
- State override policy and authority.
- Include constraint violations in rollback triggers.
- Report constraint failures separately from aggregate score.

## Reviewer Questions

- What prevents a constraint violation from being traded for score?
- Who can override the constraint?
- Where would a constraint violation appear in the evidence bundle?

## Related Resources

- [Hard constraints](../awesome/hard_constraints.md)
- [Governance and auditing](../awesome/governance_and_auditing.md)
