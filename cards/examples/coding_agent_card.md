# Filled Open-World Evaluation Card: Coding Agent

This example applies the Open-World Evaluation Card to a coding agent that generates or selects candidate patches for repository-level issues.

## 1. Claim Type

The system is claimed to resolve repository-level issues in settings where unaided human reviewers may not fully inspect every candidate, dependency interaction, hidden failure mode, or downstream consequence.

The claim should be scoped to a specified repository class, issue type, test harness, and deployment setting rather than stated as general software autonomy.

## 2. Target World State

The accepted patch should solve the intended issue without introducing regressions, security vulnerabilities, compatibility breaks, or excessive maintenance burden.

Evidence should include build results, existing tests, hidden tests, reproducer scripts, static analysis, security checks, maintainer review, and deployment telemetry.

## 3. Human-Signal Role

Human signals include issue interpretation, maintainer preferences, style judgments, code-review comments, and assessments of intent, maintainability, and contextual fit.

These signals help define the task and interpret verifier outcomes, but they do not replace executable verification.

## 4. Verifier Stack

Candidate patches should be evaluated by task-facing checks such as:

- Compilation
- Existing unit and regression tests
- Hidden tests
- Property-based tests
- Static type checks
- Linters
- Reproducer scripts
- Issue-resolution harnesses
- Fuzzing or domain-specific analyzers where appropriate

The stack should distinguish public tests from hidden tests, static analysis from dynamic tests, human review from model-generated critiques, and offline benchmarks from deployment telemetry.

## 5. Hard Constraints

Hard gates may include:

- No failed existing tests
- No high-severity security finding
- No secret, credential, or private-data leakage
- No unauthorized dependency or license change
- No violation of repository policy
- No regression on critical performance, safety, or compatibility budgets

Aggregate benchmark score, local issue-resolution success, or stylistic approval should not override these constraints.

## 6. Evaluator Frontier

Escalation is triggered when:

- Tests conflict
- Coverage is weak
- The patch touches security-critical code
- The issue is underspecified
- The diff is unusually large
- The system cannot reproduce the bug
- Verifier disagreement is high
- Human reviewers disagree about intent or risk

## 7. Absent Stakeholders

Relevant stakeholders include maintainers, downstream users, security teams, API consumers, release managers, future maintainers, and users affected by regressions.

The card should specify who can approve deployment, trigger escalation, or force rollback.

## 8. Monitoring and Rollback

Post-deployment monitoring should track revert rate, escaped defects, incident reports, security tickets, performance regressions, user bug reports, and maintenance burden.

Rollback should be triggered by hard-constraint violations, severe incidents, or pre-specified monitoring thresholds. Rollback authority should be assigned to maintainers, release managers, or security owners.
