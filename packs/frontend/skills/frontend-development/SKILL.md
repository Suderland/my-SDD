---
name: frontend-development
description: Guides maintainable frontend architecture, state ownership, component boundaries, server/client data, forms, error/loading states, performance and testability. Use for web UI features, component architecture, frontend state or user interaction flows.
---


# Frontend Development

Design around user journeys and explicit state ownership.

## Rules

- Keep components cohesive and prefer composition.
- Separate server state from ephemeral UI state.
- Derive state instead of duplicating it when possible.
- Make loading, empty, success, validation and failure states explicit.
- Keep domain/business rules out of purely presentational components when they belong in reusable policy.
- Avoid global state for local concerns.
- Treat URL state as a contract when navigation/shareability requires it.
- Measure performance before complex memoization/caching.
- Preserve keyboard/accessibility semantics when customizing controls.
- Test behavior from the user's perspective at appropriate layers.

Stack-specific implementation guidance belongs in stack packs rather than this universal frontend Skill.
