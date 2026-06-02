# Awesome Open-World Alignment

A curated resource list for evaluating AI systems beyond direct human supervision.

This list is grouped by Open-World Evaluation Card dimension. Resources are included because they clarify human-signal limits, verifier design, benchmark validity, deployment monitoring, governance, or externalities.

## Claim Type and Measurement Validity

- [HELM: Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110): transparent multi-scenario, multi-metric evaluation for language models.
- [Evaluating Generative AI Systems Is a Social Science Measurement Challenge](https://arxiv.org/abs/2502.00561): frames evaluation as measurement and construct validity.
- [Dynabench](https://aclanthology.org/2021.naacl-main.324/): dynamic benchmarking for moving beyond static leaderboard assumptions.
- [CheckList](https://aclanthology.org/2020.acl-main.442/): behavioral testing methodology for NLP models.

## Human-Signal Role

- [Open Problems and Fundamental Limitations of RLHF](https://arxiv.org/abs/2307.15217): surveys limitations of optimizing against human feedback.
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155): important baseline for understanding instruction-following gains from human preference data.
- [TruthfulQA](https://aclanthology.org/2022.acl-long.229/): shows that plausible language can still fail truth-oriented evaluation.
- [Sycophancy to Subterfuge](https://arxiv.org/abs/2406.10162): studies how reward optimization can lead from approval-seeking to more serious failures.

## Evaluator Frontier and Scalable Oversight

- [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390): studies strong models supervised by weaker signals.
- [Easy-to-Hard Generalization](https://arxiv.org/abs/2403.09472): examines supervising hard reasoning through easier human-labeled tasks.
- [AI Safety via Debate](https://arxiv.org/abs/1805.00899): uses assisted adversarial argument as a scalable oversight proposal.
- [Self-critiquing models for assisting human evaluators](https://arxiv.org/abs/2206.05802): explores model assistance for human evaluation.

## Verifier Stack Design

- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050): process supervision for multi-step reasoning.
- [SWE-bench](https://arxiv.org/abs/2310.06770): real GitHub issue resolution with executable patch evaluation.
- [AlphaFold](https://www.nature.com/articles/s41586-021-03819-2): scientific progress anchored in structural accuracy.
- [AlphaTensor](https://www.nature.com/articles/s41586-022-05172-4): algorithm discovery with mathematical and executable verification.
- [FunSearch](https://www.nature.com/articles/s41586-023-06924-6): program search coupled to programmatic scoring.
- [GraphCast](https://www.science.org/doi/10.1126/science.adi2336): forecasting quality anchored in out-of-sample forecast skill.

## Hard Constraints

- [Fairness and Abstraction in Sociotechnical Systems](https://collaborate.princeton.edu/en/publications/fairness-and-abstraction-in-sociotechnical-systems/): explains why technical abstractions can erase social constraints.
- [Fairness and Machine Learning](https://fairmlbook.org/): formal and sociotechnical foundations for fairness constraints.
- [Gaps in the Safety Evaluation of Generative AI](https://ojs.aaai.org/index.php/AIES/article/view/31717): identifies safety-evaluation gaps that cannot be reduced to a single score.
- [On the Dangers of Stochastic Parrots](https://dl.acm.org/doi/10.1145/3442188.3445922): motivates resource, labor, and social constraints for language models.

## Absent Stakeholders and Documentation

- [Datasheets for Datasets](https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/): standardized dataset documentation as a precedent for cards.
- [Data Statements for NLP](https://aclanthology.org/Q18-1041/): documents language communities, provenance, and generalization limits.
- [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993): model reporting artifact for intended use and limitations.
- [Dataset Nutrition Label](https://arxiv.org/abs/1805.03677): compact dataset transparency artifact.

## Monitoring, Rollback, and Governance

- [Release Strategies and the Social Impacts of Language Models](https://arxiv.org/abs/1908.09203): staged release and monitoring strategies.
- [Sociotechnical Safety Evaluation of Generative AI Systems](https://arxiv.org/abs/2310.11986): surveys context gaps and deployment-stage safety concerns.
- [AI Incident Database](https://incidentdatabase.ai/): incident tracking resource for deployment evidence.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): governance vocabulary for mapping, measuring, managing, and monitoring AI risk.

## Sustainability and Externalities

- [Tackling Climate Change with Machine Learning](https://arxiv.org/abs/1906.05433): maps climate applications and evaluation needs.
- [From Efficiency Gains to Rebound Effects](https://arxiv.org/abs/2501.16548): explains why efficiency gains can increase total resource use.
- [Green AI](https://arxiv.org/abs/1907.10597): argues for reporting efficiency alongside accuracy.
- [Estimating the Carbon Footprint of BLOOM](https://jmlr.org/papers/v24/23-0069.html): detailed accounting for model training and deployment emissions.

## Contribution Standard

When adding a resource, include a stable link and one sentence explaining which Evaluation Card field it strengthens. Avoid generic AI safety links that do not improve evaluation, verification, monitoring, or governance practice.
