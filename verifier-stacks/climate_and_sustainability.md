# Climate and Sustainability Verifier Stack

## Domain Claim

The system forecasts, optimizes, or recommends actions for climate, energy, resource, or sustainability outcomes.

## Human Signals

- Domain-expert review
- Policy stakeholder review
- User usefulness feedback
- Scenario-planning review

## Human-Signal Limits

Humans are weak supervisors when benefits depend on long-horizon system response, rebound effects, externalities, and affected communities outside the user base.

## Hard Verifiers

- Out-of-sample forecast skill
- Resource accounting
- Sensitivity analysis
- Externality accounting
- Policy baseline comparison
- Post-deployment impact monitoring

## Soft Verifiers

- Expert plausibility review
- Stakeholder review
- Scenario narrative review

## Independence Rationale

Forecast skill, accounting, sensitivity analysis, and stakeholder review address different climate and policy failure modes.

## Verifier-Gaming Risks

- Reporting efficiency gains without rebound monitoring.
- Ignoring distributional impacts.
- Choosing favorable baselines.
- Treating short-term proxy gains as long-term benefit.

## Hard Constraints

- No unsupported emissions-reduction claim.
- No hidden resource-cost tradeoff.
- No policy recommendation without uncertainty disclosure.

## Escalation Conditions

- High-impact policy use
- Missing affected-stakeholder review
- Model outside validated geography or time horizon
- Large uncertainty interval

## Monitoring Signals

- Forecast drift
- Resource-use drift
- Rebound-effect indicators
- Distributional impact reports
- Policy outcome audits

## Rollback Triggers

- Impact estimate invalidated
- Externality exceeds threshold
- Affected-stakeholder review identifies material harm
