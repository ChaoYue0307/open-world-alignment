# Forecasting Verifier Stack

## Domain Claim

The system forecasts future events, distributions, or decision-relevant quantities under uncertainty.

## Human Signals

- Question-writing review
- Domain-expert plausibility review
- User usefulness ratings
- Forecast explanation review

## Human-Signal Limits

Humans are weak supervisors before outcomes resolve and when correlated forecaster beliefs or ambiguous question wording distort apparent quality.

## Hard Verifiers

- Proper scoring rules
- Calibration curves
- Resolution records
- Baseline comparisons
- Backtesting on held-out periods

## Soft Verifiers

- Expert review of assumptions
- Scenario-analysis review
- Communication-quality review

## Independence Rationale

Outcome resolution, calibration, and expert review test different aspects of forecast quality.

## Verifier-Gaming Risks

- Ambiguous resolution criteria.
- Cherry-picked forecast windows.
- Herding on shared public signals.
- Optimizing confidence without actionable value.

## Hard Constraints

- No unresolved claim reported as proven.
- No missing resolution rule.
- No decision recommendation without uncertainty disclosure.

## Escalation Conditions

- High-impact decision context
- Ambiguous or disputed resolution
- Distribution shift relative to backtests

## Monitoring Signals

- Calibration drift
- Resolution disputes
- Baseline underperformance
- Forecast-update latency

## Rollback Triggers

- Repeated miscalibration beyond threshold
- Resolution process invalidated
- Forecast use expands beyond stated scope
