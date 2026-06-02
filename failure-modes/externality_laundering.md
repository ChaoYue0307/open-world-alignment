# Externality Laundering

## Definition

The evaluation reports direct task gains while hiding resource costs, rebound effects, labor impacts, environmental impacts, or downstream harms outside the benchmark.

## Warning Signs

- Efficiency or usefulness is reported without total resource accounting.
- The card does not identify affected non-users.
- Long-term or system-level impacts are excluded without justification.

## Card Fields Affected

- `target_world_state`
- `absent_stakeholders`
- `hard_constraints`
- `monitoring_and_rollback`

## Mitigation Checklist

- Add externality accounting to the target-world state.
- Report resource use and downstream monitoring signals.
- Represent affected stakeholders explicitly.
- Make externality thresholds rollback triggers where appropriate.

## Reviewer Questions

- Which costs are outside the benchmark but inside the real-world claim?
- Does higher task performance increase total resource use?
- Which affected group can invalidate the deployment claim?

## Related Resources

- [Sustainability and externalities](../awesome/sustainability_and_externalities.md)
- [Absent stakeholders](../awesome/absent_stakeholders.md)
