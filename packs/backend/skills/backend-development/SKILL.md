---
name: backend-development
description: Guides backend application structure, use cases, transactions, concurrency, idempotency, background work, error handling and infrastructure boundaries. Use for backend features, application services, repositories, workers, transactions or distributed interaction.
---


# Backend Development

Keep business policy explicit and infrastructure replaceable at meaningful seams.

## Workflow

1. Start from the use case and acceptance criteria.
2. Identify transaction and consistency boundary.
3. Validate authorization and input at appropriate boundaries.
4. Keep application orchestration separate from infrastructure details.
5. Make idempotency explicit for retried writes/events where required.
6. Define error semantics intentionally.
7. Handle concurrency using the data consistency model rather than timing assumptions.
8. Make background work observable and retry-safe.
9. Add boundary-appropriate tests.

Prefer simple synchronous flows until asynchronous/distributed behavior has a concrete need.
