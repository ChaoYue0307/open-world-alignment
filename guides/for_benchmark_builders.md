# Guide for Benchmark Builders

Use a card to state what your benchmark supports and what it cannot establish.

## Workflow

1. Start from [benchmark_card.yaml](../cards/templates/benchmark_card.yaml).
2. Define the benchmark's target-world proxy in `target_world_state`.
3. Add supported and unsupported claims in `claim_boundaries`.
4. Describe contamination, distribution shift, and benchmark-gaming risks.
5. Add hard constraints such as no deployment-safety claim from score alone.
6. Compare against [benchmark cards](../cards/examples/benchmark_cards/).

## Required Review Questions

- What real-world claim is this benchmark a proxy for?
- What important property is not measured?
- What would invalidate the benchmark result?
- How should downstream papers cite the benchmark without overclaiming?

## Useful Tools

- `python3 ../scripts/validate_card.py benchmark_card.yaml`
- `python3 ../scripts/lint_card_quality.py benchmark_card.yaml`
- `python3 ../scripts/score_card.py benchmark_card.yaml`
