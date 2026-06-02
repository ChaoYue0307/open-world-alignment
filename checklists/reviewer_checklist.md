# Open-World Alignment Reviewer Checklist

Use this checklist when reviewing a paper, benchmark, model card, system card, deployment report, or evaluation claim.

## Claim Clarity

- Does the work distinguish human-facing preference metrics from world-facing performance metrics?
- Does it specify whether the system makes a beyond-human or ASI-relevant capability claim?
- Is the claim scoped to a domain, benchmark, deployment setting, population, or institution?
- Does the work state what the evidence does not support?

## Human-Signal Limits

- Does it explain which labels, preferences, ratings, benchmarks, or judge models are used?
- Does it state whether these signals are used for training, evaluation, deployment gates, or interpretation?
- Does it specify where human evaluators become weak supervisors?
- Does it explain what human raters can and cannot verify unaided?

## Verifier Stack

- Are hard verifiers separated from soft verifiers?
- Are task-facing checks included where available?
- Are synthetic judges treated as inherited human proxies rather than independent world verifiers?
- Are verifier-gaming and correlated verifier failure considered?
- Are public tests, hidden tests, human review, model critique, and deployment telemetry distinguished?

## Hard Constraints

- Are non-negotiable constraints technically operationalized?
- Can aggregate scores override safety, legal, privacy, rights, resource, or ecological constraints?
- Are hard gates reported separately from soft preferences?
- Is override authority explicit?

## Evaluator Frontier

- Does the work say when the system should abstain, defer, escalate, or invoke stronger verification?
- Are unfamiliar inputs, weak coverage, verifier disagreement, and high-consequence errors handled?
- Does the paper report the tooling humans need for meaningful review?

## Absent Stakeholders

- Are affected non-users identified?
- Are downstream users, future populations, institutions, or ecosystems considered where relevant?
- Are omitted externalities reported as part of system quality rather than optional commentary?

## Monitoring and Rollback

- Are deployment signals specified?
- Are rollback triggers mechanical rather than narrative?
- Who has authority to pause, revise, roll back, or withdraw the system?
- Does monitoring have operational consequences?
