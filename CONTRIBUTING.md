# Contributing

Contributions should strengthen the repository as an evaluation artifact toolkit, not turn it into a generic AI safety link dump.

## What Belongs Here

- Filled Open-World Evaluation Cards for concrete systems or benchmarks.
- Verifier-stack templates for domains where direct human supervision becomes weak.
- Reviewer, deployment, monitoring, or rollback checklists.
- High-signal resources on scalable oversight, human-feedback limits, benchmark validity, verifier ecologies, deployment monitoring, and governance.

## Card Contributions

When adding a card:

1. Start from `cards/open_world_evaluation_card.yaml`.
2. Keep the eight required dimensions intact.
3. State what human signals can and cannot verify.
4. Separate hard constraints from soft preferences.
5. Specify who has authority to trigger escalation or rollback.
6. Run:

```bash
python3 scripts/validate_card.py path/to/card.yaml
```

## Resource Contributions

When adding resources under `awesome/`, include:

- A stable title.
- A short note explaining why the resource matters for open-world alignment.
- A topic category rather than a broad "misc" entry.
- A stable URL without tracking parameters such as `utm_source`.

Avoid promotional links, duplicate entries, unapproved manuscript-hosting links, and resources that only mention AI safety without contributing to evaluation, verification, monitoring, or governance.

Run:

```bash
make check-awesome
make check-links
```

## Writing Style

- Use concrete system claims and operational checks.
- Prefer short, testable statements over broad value claims.
- Distinguish "human preference", "human mandate", "task verifier", "hard constraint", and "deployment signal".
