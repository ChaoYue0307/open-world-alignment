# Open-World Evaluation Card: Medium-range forecasting system

## Summary

A forecasting system that predicts future events or states for operational decision support.

## Supported Claim

- The system provides calibrated forecasts under the stated horizon, domain, and data regime.

## Unsupported Claims

- The system is reliable outside the validated forecast horizon.
- The system justifies automated high-stakes action without review.
- Narrative plausibility establishes forecast quality.

## Target World State

Forecasts should improve decisions by providing calibrated, timely, and decision-relevant probability estimates without hiding uncertainty or shifting risk to unrepresented groups.

Evidence required: Out-of-sample accuracy, calibration curves, proper scoring rules, backtesting, stress tests, decision-utility analysis, and post-deployment monitoring.

Failure definition: A material failure includes persistent miscalibration, high-impact missed events, harmful decision recommendations, unreported drift, or threshold violations in high-stakes settings.

## Human-Signal Limits

Can verify: Humans can specify decision needs, choose acceptable risk thresholds, interpret forecasts, and assess whether outputs fit operational context.

Cannot verify unaided: Unaided humans may not reliably judge calibration, rare-event performance, distribution shift, counterfactual decision utility, or delayed harms.

Role in decision: Human signals define the decision context and acceptable risk, while out-of-sample outcomes and calibration metrics evaluate forecast quality.

## Verifier Stack

### Hard Verifiers

- Out-of-sample forecast accuracy
- Calibration evaluation
- Proper scoring rules
- Backtesting on held-out periods
- Drift detection
- Reliability thresholds for high-stakes use

### Soft Verifiers

- Expert plausibility review
- Decision-maker usability review
- Narrative explanation review

### Independence Rationale

The stack separates historical backtests from live monitoring, calibration from narrative plausibility, expert review from outcome scoring, and decision utility from raw accuracy.

## Hard Constraints

- No deployment when calibration falls below required threshold
- No high-stakes automated action without human review
- No suppression of uncertainty intervals
- No use outside the validated forecast horizon or domain
- No decision threshold change without risk-owner approval

Enforcement: Block deployment or trigger escalation when calibration, drift, domain, or threshold checks fail.

Override policy: No automatic override. Any exception must be time-limited, documented, and approved by the risk or operations owner.

## Evaluator Frontier

Humans become weak supervisors when forecast quality depends on statistical calibration, rare-event behavior, interacting variables, or delayed outcome feedback.

Escalation conditions:

- Inputs are outside training distribution
- Calibration degrades
- Forecast horizon exceeds validated scope
- Rare-event uncertainty is high
- Model and expert forecasts strongly disagree
- Decision consequence is high

## Absent Stakeholders

### Affected non-users

- People affected by decisions based on forecasts
- Communities exposed to false alarms or missed warnings
- Operators responsible for acting on forecasts

### Future or downstream stakeholders

- Future decision-makers using accumulated forecasts
- Institutions relying on threshold policies
- Populations affected by delayed or compounding forecast errors

Representation: Represent stakeholders through decision audits, appeal channels, outcome monitoring, and review of false-positive and false-negative impacts.

## Monitoring and Rollback

### Signals

- Calibration drift
- Out-of-sample error
- False alarm rate
- Missed-event rate
- Decision outcome metrics
- Appeals or complaints
- Data pipeline failures

### Rollback triggers

- Calibration below threshold
- Severe missed event linked to model failure
- Domain shift invalidates validation
- Decision harm above pre-specified threshold
- Data pipeline integrity failure

Revision authority: Risk owners, operations leads, or governance boards can pause, revise, roll back, or withdraw the forecasting system.
