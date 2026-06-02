# Verifier Gaming

## Definition

The system improves on a verifier without improving the target-world property the verifier was meant to support.

## Warning Signs

- Results rise on visible tests while real task performance does not.
- The card reports one verifier as if it were independent evidence.
- The verifier is also used during training, selection, or prompt tuning.

## Card Fields Affected

- `claim_type`
- `verifier_stack`
- `claim_boundaries`
- `monitoring_and_rollback`

## Mitigation Checklist

- Add held-out or adversarial verifier-gaming tests.
- Separate training, selection, and audit verifiers.
- Report unsupported claims explicitly.
- Monitor real-world failures after deployment.

## Reviewer Questions

- Can the system optimize this verifier without satisfying the intended claim?
- Which verifier is independent of the optimization process?
- What result would force the claim to be withdrawn?

## Related Resources

- [Verifier-stack design](../awesome/verifier_stack_design.md)
- [Benchmark validity](../awesome/benchmark_validity.md)
