# Open-World Alignment

[![Validate Cards](https://github.com/ChaoYue0307/open-world-alignment/actions/workflows/validate.yml/badge.svg)](https://github.com/ChaoYue0307/open-world-alignment/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/code-MIT-green.svg)](LICENSE)
[![Docs: CC BY 4.0](https://img.shields.io/badge/docs-CC_BY_4.0-blue.svg)](LICENSE-docs)
![Card schema: v0.1](https://img.shields.io/badge/card_schema-v0.1-informational)

Evaluation infrastructure for AI systems beyond direct human supervision.

Open-world alignment starts from a practical observation: some AI systems make consequential claims that exceed unaided human ability to generate, rank, verify, or forecast. In those settings, human approval remains necessary, but it should not be the only instance-level target. Human authority needs to move up a level: mandate formation, verifier design, hard constraints, uncertainty-aware escalation, and rollback-capable monitoring.

This repository turns that idea into reusable research artifacts.

## Who This Is For

- Researchers writing or reviewing papers about frontier AI evaluation.
- Benchmark builders who need to state what their benchmark can and cannot support.
- Developers of agents, foundation models, scientific ML systems, and forecasting systems.
- Governance, audit, and safety teams that need explicit monitoring and rollback criteria.

## What You Can Use Today

- [Open-World Evaluation Card template](cards/open_world_evaluation_card.md): a reporting artifact for beyond-human or ASI-relevant claims.
- [Machine-readable card template](cards/open_world_evaluation_card.yaml): a JSON-compatible YAML card that can be validated without extra dependencies.
- [JSON Schema](cards/open_world_evaluation_card.schema.json): the current schema for automated checks.
- [Filled example cards](cards/examples/): coding agents, foundation models, scientific ML, and forecasting.
- [Verifier-stack templates](verifier-stacks/): domain checklists for designing stronger evidence channels.
- [Reviewer checklist](checklists/reviewer_checklist.md): a compact checklist for papers, benchmarks, and deployment reports.
- [Curated resources](awesome/README.md): papers and artifacts grouped by Evaluation Card dimension.

## 3-Minute Workflow

Copy the template:

```bash
cp cards/open_world_evaluation_card.yaml my_card.yaml
```

Fill in the eight required dimensions:

1. `claim_type`
2. `target_world_state`
3. `human_signal_role`
4. `verifier_stack`
5. `hard_constraints`
6. `evaluator_frontier`
7. `absent_stakeholders`
8. `monitoring_and_rollback`

Validate the card:

```bash
python scripts/validate_card.py my_card.yaml
```

Or validate all example cards:

```bash
find cards -name '*.yaml' -print0 | xargs -0 -n1 python scripts/validate_card.py
```

## Open-World Evaluation Card

The card asks each system or benchmark to separate human-facing evidence from world-facing evidence. A good card should make clear:

- what capability is being claimed;
- where unaided human supervision becomes weak;
- which human signals are used and what they cannot verify;
- which hard and soft verifiers test the target claim;
- which constraints cannot be traded away for approval or benchmark score;
- when uncertainty triggers abstention or escalation;
- which affected stakeholders are absent from the rating loop;
- which deployment signals trigger revision, suspension, rollback, or withdrawal.

See [cards/README.md](cards/README.md) for adaptation guidance and quality criteria.

## Selected Related Work

- [Open Problems and Fundamental Limitations of RLHF](https://arxiv.org/abs/2307.15217): motivates explicit reporting of human-signal limits.
- [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390): makes the evaluator frontier concrete.
- [SWE-bench](https://arxiv.org/abs/2310.06770): shows how coding-agent claims can be tied to executable repository-level checks.
- [HELM](https://arxiv.org/abs/2211.09110): demonstrates transparent multi-metric evaluation rather than a single leaderboard score.
- [Datasheets for Datasets](https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/): a precedent for standardized reporting artifacts.

For a fuller map, see [docs/related_work.md](docs/related_work.md) and [awesome/README.md](awesome/README.md).

## Repository Map

- `cards/`: card templates, schema, and filled examples.
- `scripts/`: dependency-light validation tools.
- `tests/`: validator behavior tests and invalid fixtures.
- `verifier-stacks/`: domain-specific verifier-stack templates.
- `checklists/`: reviewer and deployment checklists.
- `awesome/`: curated literature and tooling resources.
- `docs/`: glossary and related-work notes.

## Citation

If you use this repository, cite the toolkit:

```bibtex
@misc{he2026openworldalignment,
  title  = {Open-World Alignment: Evaluation Infrastructure for AI Systems Beyond Direct Human Supervision},
  author = {He, Chaoyue},
  year   = {2026}
}
```

## License

Code in this repository is released under the MIT License. Documentation, card templates, checklists, and examples are released under Creative Commons Attribution 4.0 International. See [LICENSE](LICENSE) and [LICENSE-docs](LICENSE-docs).
