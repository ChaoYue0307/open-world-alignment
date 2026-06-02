# Coding Agent Verifier Stack

## Domain Claim

The system proposes, edits, reviews, or selects code changes for repository-level tasks.

## Human Signals

- Issue interpretation
- Maintainer preferences
- Code review
- Architecture and release-risk judgment

## Human-Signal Limits

Humans are weak supervisors when the change is large, cross-cutting, security-sensitive, performance-sensitive, or hard to reproduce locally.

## Hard Verifiers

- Build and compilation checks
- Unit, regression, and hidden tests
- Type checks and linters
- Reproducer scripts
- Security and dependency-policy checks
- Performance regression checks for critical paths

## Soft Verifiers

- Maintainability review
- Architecture review
- Documentation review
- Model-generated critique used only as advisory evidence

## Independence Rationale

Executable checks, policy checks, and human review test different failure surfaces and should not be treated as interchangeable.

## Verifier-Gaming Risks

- Patch passes visible tests while missing the bug.
- Patch overfits to benchmark harness.
- Patch removes or weakens relevant tests.
- Reviewer accepts plausible code without reproduction.

## Hard Constraints

- No failing existing tests.
- No high-severity vulnerability.
- No secret or private-data leakage.
- No unauthorized dependency, license, or public API change.

## Escalation Conditions

- Conflicting tests
- Weak coverage
- Security-critical paths
- Underspecified issue
- Large or cross-cutting diff

## Monitoring Signals

- Revert rate
- Escaped defects
- Security tickets
- Performance regressions
- User bug reports

## Rollback Triggers

- Hard-constraint violation
- Severe incident linked to the patch
- High-severity vulnerability detected
- Maintainer or security owner invalidates the verifier evidence
