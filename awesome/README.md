# Awesome Open-World Alignment

This resource map collects work for evaluating AI systems when direct human judgment is insufficient. The focus is on settings where correctness is external, delayed, technical, physical, institutional, or distributed across affected stakeholders who are not in the rating loop.

Open-world alignment does not reject human intent. It asks when human intent must be coupled with external verifiers, hard constraints, uncertainty-aware abstention, and monitoring with rollback authority.

## Inclusion Rule

A category belongs here when at least one of these is true:

1. Human preference can be wrong.
2. Human evaluation is too slow, expensive, or tool-dependent.
3. Human experts or stakeholders disagree.
4. The outcome appears only later.
5. The affected people are not the raters.
6. The benchmark is only a proxy.
7. The system can game the verifier.
8. The system acts over many steps or affects the physical world.
9. The system changes incentives or shifts externalities.
10. The claim needs post-deployment monitoring or rollback authority.

## Taxonomy

### Foundations

- [Open-world alignment](foundations/open_world_alignment.md)
- [Human-signal monism](foundations/human_signal_monism.md)
- [Evaluator frontier](foundations/evaluator_frontier.md)
- [Beyond-human supervision](foundations/beyond_human_supervision.md)

### Human-Signal Limits

- [RLHF limitations](human_signal_limits/rlhf_limitations.md)
- [Weak supervision](human_signal_limits/weak_supervision.md)
- [Synthetic judges](human_signal_limits/synthetic_judges.md)
- [Expert disagreement](human_signal_limits/expert_disagreement.md)

### Measurement and Claims

- [Measurement validity](measurement_and_claims/measurement_validity.md)
- [Benchmark overclaiming](measurement_and_claims/benchmark_overclaiming.md)
- [Data contamination](measurement_and_claims/data_contamination.md)
- [Distribution shift](measurement_and_claims/distribution_shift.md)
- [Leaderboard validity](measurement_and_claims/leaderboard_validity.md)
- [Reporting standards](measurement_and_claims/reporting_standards.md)

### Scalable Oversight

- [Scalable oversight](scalable_oversight/scalable_oversight.md)
- [AI-assisted evaluation](scalable_oversight/ai_assisted_evaluation.md)
- [Debate and adversarial review](scalable_oversight/debate_and_adversarial_review.md)
- [Weak-to-strong generalization](scalable_oversight/weak_to_strong_generalization.md)

### Verifier Ecologies

- [Verifier-stack design](verifier_ecologies/verifier_stack_design.md)
- [Hard verifiers](verifier_ecologies/hard_verifiers.md)
- [Soft verifiers](verifier_ecologies/soft_verifiers.md)
- [Formal verification](verifier_ecologies/formal_verification.md)
- [Simulation-based evaluation](verifier_ecologies/simulation_based_evaluation.md)
- [Real-world outcomes](verifier_ecologies/real_world_outcomes.md)
- [Verifier gaming](verifier_ecologies/verifier_gaming.md)

### Agentic Systems

- [Agent evaluation frameworks](agentic_systems/agent_evaluation_frameworks.md)
- [Long-horizon evaluation](agentic_systems/long_horizon_evaluation.md)
- [Tool-use evaluation](agentic_systems/tool_use_evaluation.md)
- [Computer-use agents](agentic_systems/computer_use_agents.md)
- [Multi-agent systems](agentic_systems/multi_agent_systems.md)
- [Autonomous research agents](agentic_systems/autonomous_research_agents.md)

### Domains

- [Software engineering](domains/software_engineering.md)
- [Mathematics and theorem proving](domains/mathematics_and_theorem_proving.md)
- [Scientific discovery](domains/scientific_discovery.md)
- [Forecasting and planning](domains/forecasting_and_planning.md)
- [Robotics and embodied AI](domains/robotics_and_embodied_ai.md)
- [Medicine and health](domains/medicine_and_health.md)
- [Law, policy, and institutions](domains/law_policy_and_institutions.md)
- [Economics and resource allocation](domains/economics_and_resource_allocation.md)
- [Sustainability and environment](domains/sustainability_and_environment.md)
- [Education and human development](domains/education_and_human_development.md)
- [Information ecosystems](domains/information_ecosystems.md)
- [Cybersecurity evaluation](domains/cybersecurity_evaluation.md)

### Constraints and Stakeholders

- [Hard constraints](constraints_and_stakeholders/hard_constraints.md)
- [Rights-based evaluation](constraints_and_stakeholders/rights_based_evaluation.md)
- [Privacy-preserving evaluation](constraints_and_stakeholders/privacy_preserving_evaluation.md)
- [Absent stakeholders](constraints_and_stakeholders/absent_stakeholders.md)
- [Externalities](constraints_and_stakeholders/externalities.md)

### Deployment

- [Post-deployment monitoring](deployment/post_deployment_monitoring.md)
- [Rollback triggers](deployment/rollback_triggers.md)
- [Incident reporting](deployment/incident_reporting.md)
- [Drift detection](deployment/drift_detection.md)
- [Evaluation debt](deployment/evaluation_debt.md)

### Governance

- [AI risk management frameworks](governance/ai_risk_management_frameworks.md)
- [AI auditing](governance/ai_auditing.md)
- [Assurance cases](governance/assurance_cases.md)
- [Model release governance](governance/model_release_governance.md)
- [Evaluation governance](governance/evaluation_governance.md)

### Failure Modes

- [Reward hacking](failure_modes/reward_hacking.md)
- [Specification gaming](failure_modes/specification_gaming.md)
- [Proxy collapse](failure_modes/proxy_collapse.md)
- [Benchmark overfitting](failure_modes/benchmark_overfitting.md)
- [Correlated verifier failure](failure_modes/correlated_verifier_failure.md)
- [Monitoring without power](failure_modes/monitoring_without_power.md)
- [Synthetic judge laundering](failure_modes/synthetic_judge_laundering.md)

### Open Problems

- [Good verifiers](open_problems/good_verifiers.md)
- [Absent stakeholder measurement](open_problems/absent_stakeholder_measurement.md)
- [Beyond expert knowledge](open_problems/beyond_expert_knowledge.md)
- [Longitudinal agent auditing](open_problems/longitudinal_agent_auditing.md)

## Contribution Standard

Every external resource entry should use this format:

```markdown
- [Stable resource title](https://stable-url.example): one sentence explaining which Open-World Evaluation Card field it strengthens.
```

Do not add generic AI-safety link dumps, tracking query parameters, duplicate URLs, or links that do not improve evaluation, verification, monitoring, constraints, stakeholder representation, or governance practice.
