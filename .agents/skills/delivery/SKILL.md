---
name: delivery
description: Guides safe software delivery including CI/CD readiness, migrations, rollout, compatibility, feature flags, rollback, release risk and repository integration. Use for deployment-affecting changes, releases, schema migrations, breaking changes, or preparing work for merge/production.
---


# Delivery

Design changes so they can be integrated and rolled out safely.

## Before delivery

- verify requirements and quality gates;
- identify backward/forward compatibility needs;
- plan schema/data migrations and rollback where relevant;
- ensure configuration/secrets are externalized safely;
- ensure observability can detect failure after rollout;
- avoid combining unrelated high-risk changes;
- prefer incremental rollout for risky behavior when supported.

## Database/API changes

Use expand-migrate-contract patterns when zero/low downtime compatibility matters. Do not deploy a breaking consumer/provider change without sequencing or versioning strategy.

## Rollback

A rollback plan must account for data/schema compatibility, not only application binaries. Some migrations are not safely reversible; plan forward repair when appropriate.

## Integration

Keep commits/PRs cohesive and explain risk, verification and migration needs. Do not claim release readiness until `verification` passes.
