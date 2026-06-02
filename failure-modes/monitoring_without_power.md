# Monitoring Without Power

## Definition

The card lists post-deployment signals but gives no authority, threshold, or process for revising, suspending, rolling back, or withdrawing a claim.

## Warning Signs

- Monitoring signals are broad but rollback triggers are vague.
- No revision authority is named.
- Incident response depends on informal attention.

## Card Fields Affected

- `monitoring_and_rollback`
- `hard_constraints`
- `evidence_bundle`

## Mitigation Checklist

- Name revision authority.
- Define rollback triggers.
- Connect monitored signals to incident response.
- Record review frequency and decision logs.

## Reviewer Questions

- Who can stop use or withdraw the claim?
- Which signal triggers action rather than observation?
- Is monitoring still meaningful if the deployment owner disagrees?

## Related Resources

- [Monitoring and rollback](../awesome/monitoring_and_rollback.md)
- [Governance and auditing](../awesome/governance_and_auditing.md)
