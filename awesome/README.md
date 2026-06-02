# Awesome Open-World Alignment

A curated resource list for evaluating AI systems beyond direct human supervision.

This list is organized by evaluation problem rather than by hype category. Add resources that clarify human-signal limits, verifier design, benchmark validity, deployment monitoring, governance, or externalities.

## Human Feedback and Its Limits

- Reinforcement learning from human feedback: useful for instruction following and preference learning, but insufficient as the sole evidence channel for beyond-human claims.
- Sycophancy and reward tampering work: shows how optimizing human-facing approval can produce failures that look good to evaluators.
- Critiques of RLHF limitations: useful for identifying what human labels and preferences cannot verify unaided.

## Weak-to-Strong and Scalable Oversight

- Weak-to-strong generalization: studies how stronger capabilities can be elicited from weaker supervision.
- Easy-to-hard generalization: examines alignment when supervision does not directly cover the hardest cases.
- Debate, critique, and assisted evaluation: useful as parts of verifier ecologies, but not replacements for world-facing checks.

## Benchmark Validity and Evaluation Rigor

- Construct-validity work: asks whether benchmarks measure the claim they are used to support.
- Behavioral and dynamic evaluation: tests models beyond static leaderboards.
- Reproducibility and empirical rigor: helps separate robust progress from benchmark overfitting.

## Verifier Ecologies

- Executable tests and issue-resolution harnesses for coding agents.
- Theorem provers and proof checkers for mathematical claims.
- Simulators and physical validation for scientific ML.
- Deployment monitors and external audits for real-world systems.

## Agent and Tool-Use Evaluations

- Repository-level coding benchmarks.
- Tool-use reliability evaluations.
- Sandboxed agent evaluations.
- Long-horizon task evaluations with explicit failure criteria.

## Governance, Auditing, and Rollback

- Model cards, system cards, datasheets, and audit frameworks.
- Incident reporting and rollback protocols.
- Public-sector contestability and due-process evaluation.
- Safety cases and assurance cases for high-consequence systems.

## Sustainability and Externalities

- AI resource and carbon accounting.
- Rebound-effect analysis.
- Environmental AI governance.
- Evaluation of ecological outcomes and downstream resource costs.
