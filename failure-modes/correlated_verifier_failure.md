# Correlated Verifier Failure

## Definition

Multiple verifiers fail together because they share data, assumptions, model-generated judgments, or operational blind spots.

## Warning Signs

- Human review, synthetic judges, and benchmarks all depend on the same examples.
- The card lists many verifiers but no independence rationale.
- Failure analysis assumes disagreement will be detected automatically.

## Card Fields Affected

- `verifier_stack`
- `evaluator_frontier`
- `uncertainty`

## Mitigation Checklist

- State the independence rationale for each verifier.
- Add at least one world-facing or external verifier where possible.
- Test distribution shifts and correlated blind spots.
- Report correlated failure risks in the card.

## Reviewer Questions

- What makes these verifiers fail differently?
- Are the judges, benchmark data, and review rubrics independent?
- Which shared assumption would invalidate the stack?

## Related Resources

- [Scalable oversight](../awesome/scalable_oversight.md)
- [Uncertainty and abstention](../awesome/uncertainty_and_abstention.md)
