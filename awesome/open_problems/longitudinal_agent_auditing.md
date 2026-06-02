# Longitudinal Agent Auditing

## Relevance

Long-lived agents require evidence over time: memory, permissions, tool use, drift, incidents, and rollback history.

## Card Fields Strengthened

- `monitoring_and_rollback`
- `evidence_bundle`
- `review_frequency`

## Starter Resources

- [OpenTelemetry](https://opentelemetry.io/): provides observability concepts useful for tracing long-running agent behavior.

## Open Questions

- What should be logged for agentic systems without exposing sensitive data?
- How should memory drift and permission creep be audited?
- When should a longitudinal incident invalidate a prior evaluation card?
