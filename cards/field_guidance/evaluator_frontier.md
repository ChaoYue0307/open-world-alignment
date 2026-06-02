# Evaluator Frontier

## Purpose

This field identifies where unaided humans become weak supervisors and what triggers abstention or escalation.

## Strong Answer

Escalate when tests conflict, coverage is weak, verifier disagreement is high, the task is underspecified, or the consequence of error is severe.

## Weak Answer

Humans review difficult cases.

## Common Failure Mode

Evaluator weakness: the system outruns the ability of reviewers to verify outputs directly.

## Reviewer Question

What happens when humans cannot inspect the relevant evidence unaided?

## Coding-Agent Example

Large diffs, security-critical paths, hidden failures, and non-reproducible bugs trigger escalation.

## Foundation-Model Example

High-stakes requests, missing sources, privacy risk, or policy uncertainty trigger abstention or stronger verification.
