# Governance

This repository is maintained as a research artifact toolkit and emerging reporting standard.

## Maintainer Responsibilities

Maintainers should:

- preserve the eight required card dimensions;
- avoid turning the repo into a generic AI safety link list;
- require concrete verifier, constraint, and rollback language in examples;
- keep tooling dependency-light unless a dependency clearly improves adoption;
- reject contributions that include operationally harmful instructions.

## Change Policy

- Required schema fields should not be removed before v1.0.
- Optional fields may be added in minor versions.
- Breaking changes should be documented in `CHANGELOG.md`.
- New examples should validate and include concrete human-signal limits.

## Decision Process

Small documentation and example improvements may be merged by the maintainer. Changes to required card fields, validator behavior, schema compatibility, or repository scope should be discussed in an issue first.
