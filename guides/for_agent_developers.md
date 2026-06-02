# Guide for Agent Developers

Use cards when an agent can take actions through tools, code, web interfaces, research workflows, or other environments.

## Workflow

1. Start from [agent_card.yaml](../cards/templates/agent_card.yaml).
2. Define action boundaries in `claim_scope`, `intended_use`, and `out_of_scope_uses`.
3. Put tool permissions, logs, and side-effect checks in `verifier_stack`.
4. Turn no-go conditions into `hard_constraints`.
5. Add escalation conditions for ambiguity, uncertainty, and irreversible effects.
6. Monitor incidents, overrides, and rollback triggers after pilot use.

## Useful Examples

- [Coding agent card](../cards/examples/coding_agent_card.yaml)
- [Autonomous research agent card](../cards/examples/autonomous_research_agent_card.yaml)
- [Cyber agent card](../cards/examples/cyber_agent_card.yaml)

## Avoid

- Treating task success as safety.
- Giving tools broader authority than the card claims.
- Relying on logs without a named reviewer who can stop the workflow.
