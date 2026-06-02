# Monitoring and Rollback

## Purpose

This field connects post-deployment evidence to authority to revise, suspend, roll back, or withdraw the system.

## Strong Answer

Rollback is triggered by hard-constraint violations, severe incidents, high-severity vulnerabilities, or monitoring thresholds; maintainers, release managers, or security owners have authority to act.

## Weak Answer

The system will be monitored.

## Common Failure Mode

Monitoring without power: incidents are tracked but no actor can act on them.

## Reviewer Question

What evidence would force claim revision or rollback, and who has authority?

## Coding-Agent Example

Revert rate, escaped defects, security tickets, performance regressions, and user bug reports trigger maintainer or security-owner review.

## Foundation-Model Example

Abuse reports, privacy incidents, policy violations, and tool-use failures trigger restriction, rollback, or capability withdrawal.
