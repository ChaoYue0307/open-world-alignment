# Hard Constraints

## Purpose

This field states what cannot be traded away for higher score, stronger approval, or broader capability.

## Strong Answer

No high-severity security finding, secret leakage, unauthorized dependency change, or critical compatibility regression may be accepted.

## Weak Answer

Safety and privacy are considered.

## Common Failure Mode

Constraint erasure: non-negotiable requirements are mentioned in prose but not operationalized as gates.

## Reviewer Question

Can aggregate performance override any stated constraint?

## Coding-Agent Example

No failed existing tests, no high-severity vulnerability, and no unauthorized dependency or license change.

## Foundation-Model Example

No prohibited privacy leakage, severe misuse enablement, or unauthorized tool action.
