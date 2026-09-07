---
name: documentation
description: Creates and updates durable technical documentation that explains system contracts, decisions, operations and developer workflows without duplicating obvious code. Use when behavior, architecture, APIs, setup, operations, migrations or non-obvious decisions change.
---


# Documentation

Document what future engineers and agents cannot reliably infer from code alone.

## Priorities

- public behavior and contracts;
- architecture boundaries and consequential decisions;
- setup/runtime prerequisites;
- migrations and operational procedures;
- failure/recovery procedures;
- security-sensitive assumptions;
- non-obvious domain rules;
- examples that demonstrate real usage.

## Avoid

- duplicating implementation line by line;
- stale version-specific claims without a maintenance mechanism;
- aspirational architecture presented as current truth;
- verbose textbook explanations of common concepts.

Keep project-specific truth in `.agents/specs/` when it belongs to requirements/design state. Keep reusable guidance in Skills.
