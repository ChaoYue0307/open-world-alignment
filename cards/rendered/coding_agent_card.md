# Open-World Evaluation Card: Repository-level coding agent

## Summary

A system that generates or selects candidate patches for software issues in existing repositories.

## Supported Claim

- The system can generate candidate patches for specified repository-level issues under the stated verifier stack.

## Unsupported Claims

- The system is production-ready without deployment monitoring.
- The system is secure by benchmark success alone.
- The system can autonomously maintain arbitrary repositories.

## Target World State

The accepted patch should solve the intended issue without introducing regressions, security vulnerabilities, compatibility breaks, or excessive maintenance burden.

Evidence required: Compilation, existing tests, hidden tests, reproducer scripts, property-based tests, static analysis, security checks, maintainer review, and deployment telemetry.

Failure definition: A material failure includes unresolved issue behavior, failed regression tests, hidden test failure, high-severity vulnerability, secret leakage, unauthorized API or dependency changes, or rollback after deployment.

## Human-Signal Limits

Can verify: Humans can assess intent, contextual fit, readability, maintainability, repository norms, and whether the proposed change matches the stated issue.

Cannot verify unaided: Unaided humans may not reliably verify hidden test behavior, dependency interactions, security edge cases, production regressions, or long-term maintenance cost.

Role in decision: Human signals help define the task, interpret verifier outcomes, and approve deployment, but they do not replace executable verification.

## Verifier Stack

### Hard Verifiers

- Compilation or build success
- Existing unit and regression tests
- Hidden tests
- Reproducer scripts
- Static type checks
- Security scans for high-severity findings

### Soft Verifiers

- Maintainability review
- Readability review
- Architectural fit review
- Documentation quality review

### Independence Rationale

The stack distinguishes public tests from hidden tests, static analysis from dynamic tests, human review from model critiques, and offline benchmarks from deployment telemetry.

## Hard Constraints

- No failed existing tests
- No high-severity security finding
- No secret, credential, or private-data leakage
- No unauthorized dependency or license change
- No violation of repository policy
- No regression on critical performance, safety, or compatibility budgets

Enforcement: Block merge or deployment when a hard gate fails; require explicit security or release-owner approval for sensitive paths.

Override policy: No automated override. Any exception must be documented and approved by the responsible maintainer, release manager, or security owner.

## Evaluator Frontier

Humans become weak supervisors when the bug is hard to reproduce, tests conflict, coverage is weak, the diff is unusually large, or risk depends on security, compatibility, or production behavior.

Escalation conditions:

- Tests conflict or coverage is weak
- Patch touches security-critical code
- Issue is underspecified
- Diff is unusually large
- System cannot reproduce the bug
- Verifier disagreement is high
- Human reviewers disagree about intent or risk

## Absent Stakeholders

### Affected non-users

- Downstream users affected by regressions
- Security teams
- API consumers
- Operators responsible for incidents

### Future or downstream stakeholders

- Release managers
- Future maintainers
- Organizations depending on the patched package
- Users affected by delayed compatibility breaks

Representation: Represent these stakeholders through release gates, security review, compatibility tests, incident channels, changelog review, and rollback authority.

## Monitoring and Rollback

### Signals

- Revert rate
- Escaped defects
- Incident reports
- Security tickets
- Performance regressions
- User bug reports
- Maintenance burden

### Rollback triggers

- Hard-constraint violation
- Severe production incident linked to the patch
- High-severity vulnerability detected
- Regression above a pre-specified threshold
- Maintainer or security owner determines that verifier evidence was invalid

Revision authority: Maintainers, release managers, and security owners can pause, revise, roll back, or withdraw the patch.
