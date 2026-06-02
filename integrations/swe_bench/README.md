# SWE-bench Mapping

SWE-bench is useful for coding-agent claims because it ties issue resolution to repository-level artifacts and executable checks.

## What Passing SWE-bench Supports

- The system can solve a subset of repository-level issue-resolution tasks under benchmark conditions.
- The generated patch can satisfy the benchmark's executable checks for those tasks.
- The evaluation can support a coding-agent `verifier_stack` with build, test, and patch-review evidence.

## What Passing SWE-bench Does Not Establish

- General software engineering competence across repositories.
- Deployment safety for autonomous coding agents.
- Security correctness beyond tested properties.
- Maintainability, licensing, performance, or product-fit claims unless separately verified.
- Alignment, ASI guidance, or open-world safety by itself.

## Card Artifact

Use [swe_bench_open_world_card.yaml](swe_bench_open_world_card.yaml) as a benchmark-specific Open-World Evaluation Card.

## Recommended Additions

- Hidden-test separation.
- Patch-review sampling.
- Security and dependency-policy checks.
- Post-merge monitoring when benchmark-derived claims are used in deployment.
