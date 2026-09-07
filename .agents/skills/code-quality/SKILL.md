---
name: code-quality
description: Reviews and improves code quality through maintainability, correctness, refactoring, duplication, complexity, naming, dependency hygiene and diff-focused review. Use for code review, refactoring, cleanup, maintainability problems, or before integrating broad changes.
---


# Code Quality

Optimize for code that is easy to reason about and change safely.

## Review order

1. Correctness and requirement alignment.
2. Security/data integrity.
3. Architectural boundaries.
4. Testability and verification.
5. Complexity, cohesion and coupling.
6. Naming and readability.
7. Duplication and incidental ceremony.
8. Performance only where material or measured.

## Refactoring rules

- Preserve externally observable behavior unless the Spec changes it.
- Keep tests green through small steps.
- Remove dead code instead of preserving speculative paths.
- Prefer local clarity over premature generalization.
- Consolidate duplication when the duplicated knowledge is genuinely the same and likely to change together.
- Do not combine an unrelated redesign with a focused bug fix without need.

## Diff review

Inspect for accidental generated files, debug code, secrets, unrelated changes, weakened error handling, missing tests, stale docs/spec state and dependency changes.
