# Autonomous Research Verifier Stack

## Domain Claim

The system plans or coordinates literature search, hypothesis generation, experiment design, analysis, or reporting under bounded review.

## Human Signals

- Principal investigator review
- Protocol review
- Expert novelty assessment
- Ethics or safety review

## Human-Signal Limits

Humans are weak supervisors when research plans span many sources, tools, experiments, statistical assumptions, or downstream consequences.

## Hard Verifiers

- Source existence checks
- Protocol safety review
- Statistical validation
- Tool-permission checks
- Replication or reproduction evidence

## Soft Verifiers

- Expert plausibility review
- Novelty review
- Research-utility review

## Independence Rationale

Source verification, tool logs, expert review, and empirical validation test different parts of the research pipeline.

## Verifier-Gaming Risks

- Fabricated or irrelevant citations.
- Unsupported discovery claims.
- Hidden tool side effects.
- Favorable selective reporting.

## Hard Constraints

- No fabricated sources.
- No high-risk experiment without approval.
- No claim of discovery without validation.

## Escalation Conditions

- Source cannot be verified
- Protocol has safety implications
- Statistical assumptions fail
- Tool action has external effects

## Monitoring Signals

- Invalid citations
- Protocol violations
- Failed replications
- Tool incidents

## Rollback Triggers

- Fabricated source
- Unsafe protocol
- Invalid analysis
- Ethics or safety reviewer rejects the workflow
