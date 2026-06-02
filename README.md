# Open-World Alignment

Evaluation infrastructure for AI systems beyond direct human supervision.

This repository turns the open-world alignment framework into reusable artifacts:

1. Open-World Evaluation Card templates
2. Verifier-stack design patterns
3. Reviewer and deployment checklists
4. Curated resources on scalable oversight, human-feedback limits, and AI evaluation

The central idea is simple: when systems make consequential claims that exceed unaided human ability to generate, rank, verify, or forecast, human approval should not be the sole instance-level target. Human authority should move up a level: mandate formation, verifier design, hard constraints, uncertainty-aware escalation, and rollback-capable monitoring.

## Quickstart

Copy the card template:

```bash
cp cards/open_world_evaluation_card.yaml my_card.yaml
```

Fill in the system claim, verifier stack, constraints, evaluator frontier, absent stakeholders, and monitoring rules.

Validate the card:

```bash
python scripts/validate_card.py my_card.yaml
```

Start from the coding-agent example if your system produces software patches:

```bash
python scripts/validate_card.py cards/examples/coding_agent_card.yaml
```

## Repository Map

- `cards/`: Open-World Evaluation Card templates, schema, and filled examples.
- `scripts/`: Lightweight validation tools for card files.
- `verifier-stacks/`: Domain-specific verifier-stack templates.
- `checklists/`: Reviewer and deployment checklists.
- `awesome/`: Expandable resource list for open-world alignment topics.
- `docs/`: Glossary and concept notes.

## Open-World Evaluation Card

The card is organized around eight dimensions:

1. `claim_type`: What capability is being claimed, and where does unaided human supervision become weak?
2. `target_world_state`: What real-world outcome is the system supposed to improve?
3. `human_signal_role`: Which human labels, preferences, ratings, benchmarks, or judge models are used, and what can they not verify?
4. `verifier_stack`: Which executable, empirical, mathematical, physical, or domain-specific checks test the claim?
5. `hard_constraints`: Which safety, legal, privacy, rights, resource, or ecological constraints cannot be traded away?
6. `evaluator_frontier`: When should the system abstain, defer, trigger human review, or invoke stronger verification?
7. `absent_stakeholders`: Which affected people, downstream users, future populations, institutions, or ecosystems are outside the rating loop?
8. `monitoring_and_rollback`: Which post-deployment signals trigger redesign, suspension, rollback, or withdrawal?

## Related Work Through the Card Lens

This reading map collects papers and artifacts that fit the open-world alignment frame. Each entry is summarized through the Evaluation Card fields it most directly informs.

| Area | Work | Why it matters | Card lens |
| --- | --- | --- | --- |
| Human feedback limits | [Open Problems and Fundamental Limitations of RLHF](https://arxiv.org/abs/2307.15217) | Surveys why preference optimization cannot carry the full burden of alignment, including reward hacking, oversight limits, and disclosure needs. | `human_signal_role`: report what preference data can and cannot verify; `hard_constraints`: keep safety requirements outside scalar reward. |
| Weak supervision | [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390) | Studies whether weak supervisors can elicit stronger model capabilities, making the evaluator frontier explicit. | `evaluator_frontier`: identify where the supervisor is weaker than the system; `verifier_stack`: add checks beyond weak labels. |
| Beyond-human supervision | [Easy-to-Hard Generalization](https://arxiv.org/abs/2403.09472) | Uses easier human-labeled tasks to supervise harder reasoning tasks, directly matching the beyond-human supervision problem. | `claim_type`: scope the beyond-human claim; `human_signal_role`: distinguish easy-task labels from hard-task evidence. |
| Scalable oversight | [AI Safety via Debate](https://arxiv.org/abs/1805.00899) | Proposes debate as an assisted-evaluation structure when direct judging is too hard. | `verifier_stack`: debate can be a soft verifier; `evaluator_frontier`: use assisted review when direct review fails. |
| Process verification | [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | Shows the value of supervising intermediate reasoning steps rather than only final answers. | `verifier_stack`: separate process and outcome checks; `human_signal_role`: step labels are evidence channels, not final authority. |
| Truthfulness | [TruthfulQA](https://aclanthology.org/2022.acl-long.229/) | Demonstrates that larger models can produce plausible falsehoods, so fluent human approval is not enough. | `target_world_state`: truthfulness is world-facing; `verifier_stack`: factual checks should complement preference ratings. |
| Holistic evaluation | [HELM](https://arxiv.org/abs/2211.09110) | Makes evaluation more transparent by reporting many scenarios and metrics rather than one leaderboard score. | `claim_type`: disclose which claims a benchmark supports; `hard_constraints`: avoid silent objective collapse into one score. |
| Coding agents | [SWE-bench](https://arxiv.org/abs/2310.06770) | Evaluates models on real GitHub issues and executable patch success, making coding agents a concrete verifier-stack case. | `verifier_stack`: tests and issue-resolution harnesses are hard verifiers; `monitoring_and_rollback`: escaped defects still matter after merge. |
| Scientific discovery | [AlphaFold](https://www.nature.com/articles/s41586-021-03819-2) | Shows beyond-human usefulness anchored in structural accuracy rather than human preference alone. | `target_world_state`: protein-structure accuracy; `verifier_stack`: experimental and structural validation. |
| Forecasting | [GraphCast](https://www.science.org/doi/10.1126/science.adi2336) | Weather forecasting is judged by forecast skill and out-of-sample accuracy, not stylistic approval. | `target_world_state`: calibrated forecasts; `verifier_stack`: out-of-sample forecast evaluation. |
| Algorithm discovery | [AlphaTensor](https://www.nature.com/articles/s41586-022-05172-4) | Discovers algorithms whose value is checked by executable mathematical and hardware performance criteria. | `verifier_stack`: executable and mathematical verification; `hard_constraints`: correctness cannot be traded for speed. |
| Program search | [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) | Couples language models with programmatic evaluation to discover useful mathematical constructions. | `verifier_stack`: generated candidates must pass programmatic scoring; `human_signal_role`: humans frame and interpret discoveries. |
| Evaluation documentation | [Datasheets for Datasets](https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/) | Provides a precedent for standardized reporting artifacts that make hidden assumptions visible. | `claim_type`: document intended use; `absent_stakeholders`: surface dataset subjects and affected users. |
| Dataset context | [Data Statements for NLP](https://aclanthology.org/Q18-1041/) | Links system behavior to language communities, data provenance, and generalization boundaries. | `absent_stakeholders`: identify represented and omitted groups; `claim_type`: limit generalization claims. |
| Measurement validity | [Evaluating Generative AI Systems Is a Social Science Measurement Challenge](https://arxiv.org/abs/2502.00561) | Frames evaluation as measurement, emphasizing construct validity and the gap between concepts and instruments. | `claim_type`: define the construct; `evaluator_frontier`: state what the instrument cannot measure. |
| Sustainability | [Tackling Climate Change with Machine Learning](https://arxiv.org/abs/1906.05433) | Treats climate and sustainability outcomes as domain-specific targets that require external evidence. | `target_world_state`: ecological or climate outcomes; `absent_stakeholders`: ecosystems and future populations. |
| Externalities | [From Efficiency Gains to Rebound Effects](https://arxiv.org/abs/2501.16548) | Shows why AI efficiency gains can still produce indirect environmental costs. | `monitoring_and_rollback`: track second-order deployment effects; `hard_constraints`: resource ceilings should be explicit. |

## Citation

If you use this repository, cite the manuscript:

```bibtex
@misc{he2026beyondhumanmeasure,
  title  = {Beyond Human Measure: Toward Guiding ASI by Open-World Alignment},
  author = {He, Chaoyue and Zhou, Xin and Wang, Di and Xu, Hong and Liu, Wei and Miao, Chunyan},
  year   = {2026}
}
```

## License

Code in this repository is released under the MIT License. Documentation, card templates, checklists, and examples are released under Creative Commons Attribution 4.0 International. See `LICENSE` and `LICENSE-docs`.
