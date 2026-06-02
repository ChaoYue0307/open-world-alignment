# Benchmark Overclaiming

## Definition

A benchmark result is described as proving a broader capability, safety, deployment, or alignment claim than the benchmark can support.

## Warning Signs

- The benchmark is named, but supported and unsupported claims are not separated.
- A leaderboard rank is used as evidence for deployment readiness.
- Contamination, task representativeness, and failure cases are not discussed.

## Card Fields Affected

- `claim_type`
- `claim_boundaries`
- `target_world_state`
- `evaluator_frontier`

## Mitigation Checklist

- List supported and unsupported claims.
- Name the target-world property the benchmark proxies.
- Add contamination and distribution-shift analysis.
- Add deployment-stage evidence before deployment claims.

## Reviewer Questions

- What does this benchmark establish, exactly?
- What important property does it not measure?
- Would a high score justify the deployment decision being implied?

## Related Resources

- [Benchmark validity](../awesome/benchmark_validity.md)
- [Claim type and measurement validity](../awesome/claim_type_and_measurement_validity.md)
