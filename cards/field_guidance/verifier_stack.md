# Verifier Stack

## Purpose

This field records the hard and soft checks that test whether the claim is actually supported.

## Strong Answer

The stack separates public tests, hidden tests, static analysis, human review, model-generated critique, deployment telemetry, and independent audits.

## Weak Answer

We used a benchmark and a judge model.

## Common Failure Mode

Verifier omission: stronger task-facing checks exist but are absent from the evaluation loop.

## Reviewer Question

Are the verifiers independent enough to catch different failure modes?

## Coding-Agent Example

Build checks, regression tests, hidden tests, security scans, maintainer review, and deployment incident monitoring.

## Foundation-Model Example

Factuality checks, retrieval citation checks, tool-use sandboxing, misuse evaluations, privacy tests, and incident reports.
