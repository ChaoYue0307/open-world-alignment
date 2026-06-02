# Glossary

## Open-World Alignment

A framework for evaluating frontier AI systems when direct human judgment is no longer sufficient as the sole optimization target. It couples human mandates to task-facing verifiers, hard constraints, uncertainty-aware escalation, and rollback-capable monitoring.

## ASI-Relevant Supervisory Regime

A setting in which consequential system outputs exceed unaided human ability to reliably generate, rank, verify, or forecast the relevant candidates and their downstream consequences.

## Human-Signal Monism

Over-reliance on human-facing signals, such as labels, preferences, expert ratings, benchmarks, judge models, or product metrics, as if they fully determine system quality.

## Human Signal

Any human-facing evidence channel used in training, evaluation, selection, deployment, or monitoring. Human signals remain indispensable, but their role and limits should be explicit.

## Mandate

The humanly authorized purpose of a system: what it is for, who authorizes it, and which stakeholders or institutions it must answer to.

## Verifier Stack

A layered set of checks used to evaluate whether system outputs are correct, useful, safe, legitimate, and robust. A verifier stack can include humans, tests, simulations, theorem provers, audits, monitors, and external evidence.

## Hard Verifier

A check that can serve as a gate because failure is operationally meaningful, such as a failed regression test, proof check, safety threshold, legal requirement, or high-severity security finding.

## Soft Verifier

An advisory or judgment-based evidence channel, such as readability review, expert interpretation, model critique, or qualitative stakeholder feedback.

## Hard Constraint

A safety, legal, privacy, rights, resource, ecological, or policy requirement that cannot be traded away for higher aggregate performance or approval.

## Evaluator Frontier

The boundary at which unaided human supervision becomes weak for a specific claim, task, or deployment setting.

## Absent Stakeholder

An affected person, institution, downstream user, future population, ecosystem, or other party that bears consequences but is not represented in the direct rating or feedback loop.

## Monitoring and Rollback

Post-deployment evidence collection tied to concrete authority to revise, suspend, roll back, or withdraw a system when monitored signals violate the card's assumptions or constraints.
