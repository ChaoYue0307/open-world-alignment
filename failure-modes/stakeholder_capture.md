# Stakeholder Capture

## Definition

The evaluation reflects the preferences of system builders or direct users while affected non-users, future users, or downstream communities are absent.

## Warning Signs

- The card lists only developers, raters, or customers.
- Affected non-users are mentioned but not represented in evidence.
- Externalities are treated as out of scope without justification.

## Card Fields Affected

- `absent_stakeholders`
- `target_world_state`
- `hard_constraints`

## Mitigation Checklist

- Identify affected non-users and downstream stakeholders.
- Add representation, audit, or proxy evidence mechanisms.
- Tie stakeholder harms to constraints or rollback triggers.
- State why any excluded group is outside scope.

## Reviewer Questions

- Who bears risk without rating the system?
- How are absent stakeholders represented in the evidence?
- Which harm would force revision even if direct users approve?

## Related Resources

- [Absent stakeholders](../awesome/absent_stakeholders.md)
- [Sustainability and externalities](../awesome/sustainability_and_externalities.md)
