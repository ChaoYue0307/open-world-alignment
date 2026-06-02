# Claim Anti-Patterns

Use these anti-patterns to detect when an evaluation result is being inflated into a broader claim than the evidence supports.

## Benchmark-Score Inflation

Weak claim:

> Our system achieves 72% on Benchmark X, showing general autonomous research ability.

Open-world rewrite:

> Our system shows evidence of performance on Benchmark X under its task distribution. This does not establish general autonomous research ability because the benchmark does not test long-horizon experimental design, deployment monitoring, or absent-stakeholder effects.

## Human-Preference Collapse

Weak claim:

> Human raters preferred the system, so it is aligned.

Open-world rewrite:

> Human raters preferred the system on observed outputs. The card must still state what those raters could not verify, including factuality, security, delayed harms, and externalities.

## Judge-Model Laundering

Weak claim:

> An LLM judge scored the system highly, so the output is correct.

Open-world rewrite:

> The judge model is one soft verifier. The card should explain inherited blind spots and add task-facing checks where correctness matters.

## Verifier Omission

Weak claim:

> Reviewers approved the result, so no further checks are needed.

Open-world rewrite:

> If executable, empirical, mathematical, physical, legal, or operational checks exist, the verifier stack should explain whether they were used and why.

## Constraint-as-Prose

Weak claim:

> Safety and privacy are important considerations.

Open-world rewrite:

> Safety and privacy constraints are hard gates with named enforcement mechanisms, override policy, and rollback triggers.

## Deployment Blindness

Weak claim:

> Offline evaluation passed, so deployment is justified.

Open-world rewrite:

> Offline success supports only pre-deployment claims. The card must specify deployment signals, incident response, review frequency, and rollback authority.

## Stakeholder Invisibility

Weak claim:

> Users liked the system, so stakeholder impact is positive.

Open-world rewrite:

> User approval does not represent affected non-users, downstream users, future populations, or ecosystems. The card must state how absent stakeholders are represented.

## Leaderboard Monism

Weak claim:

> The highest leaderboard score is the best system.

Open-world rewrite:

> Leaderboard score is one evidence channel. The card should report hard constraints, evaluator frontier, and unsupported claims separately from aggregate performance.
