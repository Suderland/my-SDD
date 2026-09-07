---
name: database-design
description: Guides relational/document data modeling, constraints, indexes, transactions, migrations, concurrency and data lifecycle. Use for schemas, persistence changes, migration design, query performance, consistency or retention decisions.
---


# Database Design

Model data around invariants, access patterns and lifecycle.

## Rules

- Enforce critical integrity constraints at the strongest practical layer, including the database when appropriate.
- Choose keys intentionally; do not assume UUID or integer universally.
- Normalize by default for relational integrity, denormalize for measured/read-model reasons.
- Add indexes for actual query/selectivity needs and account for write/storage cost.
- Define transaction/isolation needs from consistency requirements.
- Handle optimistic/pessimistic concurrency explicitly when lost updates matter.
- Treat migrations as production code: test, sequence, observe and plan rollback/forward repair.
- Define ownership, retention, deletion and archival for sensitive/large data.

Avoid embedding storage-specific concerns into domain policy unless the storage characteristic is itself a business constraint.
