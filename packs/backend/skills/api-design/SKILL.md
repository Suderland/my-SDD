---
name: api-design
description: Designs stable HTTP/RPC/event APIs with explicit contracts, validation, errors, compatibility, idempotency, pagination and versioning. Use when creating or changing public/service interfaces or message contracts.
---


# API Design

Treat APIs as durable consumer contracts.

## Rules

- Model resources/actions using domain language, not database tables blindly.
- Validate inputs and define error semantics consistently.
- Make authentication/authorization requirements explicit.
- Use idempotency for retryable non-safe operations where duplicates matter.
- Define pagination/order/filter semantics for collections.
- Prefer additive compatible evolution; version when compatibility cannot be preserved.
- Define time/date/identifier/number formats unambiguously.
- For asynchronous APIs, define event schema ownership, delivery semantics and deduplication expectations.
- Add contract tests for independently consumed boundaries.

Document consumer-visible behavior in project Specs/OpenAPI/AsyncAPI as appropriate.
