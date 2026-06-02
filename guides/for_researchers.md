# Guide for Researchers

Use Open-World Evaluation Cards when a paper makes claims beyond a narrow benchmark result.

## Workflow

1. Start from [system_card.yaml](../cards/templates/system_card.yaml) or the closest [example card](../cards/examples/).
2. Write the central claim in `claim_type.description`.
3. Separate supported and unsupported claims in `claim_boundaries`.
4. Add hard verifiers before relying on human preference or model judges.
5. Use the [maturity rubric](../rubrics/card_maturity_rubric.md) to identify weak fields.
6. Render the card with `python3 ../scripts/render_card_markdown.py path/to/card.yaml` for an appendix.

## Good Research Use

- Append the card to a paper.
- Use it to narrow abstract and conclusion claims.
- Use it to explain why a benchmark result is useful but not sufficient.

## Avoid

- Treating the card as a generic ethics statement.
- Claiming deployment readiness from research-stage evidence.
- Leaving unsupported claims implicit.
