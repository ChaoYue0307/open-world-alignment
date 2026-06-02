# Coding Agent Verifier Stack

Use this stack when a system generates, edits, reviews, or selects code changes for repository-level issues.

## Human Signal

- Issue interpretation
- Maintainer preferences
- Code style review
- Architecture and maintainability judgment
- Release-risk judgment

## Hard Verifiers

- Build and compilation checks
- Existing unit and regression tests
- Hidden tests
- Reproducer scripts
- Type checks
- Security scans
- License and dependency policy checks
- Performance regression checks for critical paths

## Soft Verifiers

- Readability review
- Documentation quality review
- Architectural fit review
- Model-generated critique used only as advisory evidence

## Hard Constraints

- No failed existing tests
- No high-severity vulnerability
- No secret or private-data leakage
- No unauthorized dependency, license, or public API change
- No regression beyond critical performance, safety, or compatibility budgets

## Escalation Conditions

- Conflicting tests
- Weak coverage
- Security-critical code paths
- Underspecified issue
- Large or cross-cutting diff
- Inability to reproduce the bug
- High verifier disagreement

## Monitoring

- Revert rate
- Escaped defects
- Incident reports
- Security tickets
- Performance regressions
- User bug reports
- Maintenance burden

## Rollback Triggers

- Hard-constraint violation
- Severe incident linked to the patch
- High-severity vulnerability detected
- Regression above a pre-specified threshold
- Maintainer or security owner invalidates the verifier evidence
