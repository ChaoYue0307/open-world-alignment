# Synthetic Judge Monism

## Definition

A single model-based judge, or a family of similar judges, becomes the dominant evidence channel for a claim.

## Warning Signs

- The card treats model judgments as ground truth.
- Human review only validates judge outputs, not the target property.
- No hard verifier or external evidence is included.

## Card Fields Affected

- `human_signal_role`
- `verifier_stack`
- `evaluator_frontier`
- `uncertainty`

## Mitigation Checklist

- Label synthetic judges as soft verifiers unless independently validated.
- Add hard verifiers or external evidence for high-stakes claims.
- Test judge disagreement and calibration.
- Escalate when judge outputs conflict with world-facing evidence.

## Reviewer Questions

- Why should this judge be trusted for this domain?
- What independent evidence checks the judge?
- What happens when the judge and external evidence disagree?

## Related Resources

- [Human-signal limits](../awesome/human_signal_limits.md)
- [Verifier-stack design](../awesome/verifier_stack_design.md)
