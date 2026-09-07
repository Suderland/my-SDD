---
name: requirements-discovery
description: Resolves consequential ambiguity in software requirements before implementation. Use for new features, material behavior changes, architecture-sensitive requests, unclear acceptance criteria, or when multiple interpretations would materially change scope, data, security, compatibility, or cost of reversal.
---


# Requirements Discovery

Clarify only what materially improves the implementation decision.

## Workflow

1. Read relevant `.agents/specs/` entries if they exist.
2. Inspect the relevant code, interfaces, tests and conventions.
3. Restate the intended outcome internally as observable behavior.
4. List unresolved decisions and rank them by impact × uncertainty × cost of reversal.
5. Ask only questions whose answers materially affect implementation.
6. Prefer one focused decision at a time. When useful, include a recommended default and its trade-off.
7. Stop questioning when remaining uncertainty is low-impact, reversible, or safely inferable.
8. Feed resolved decisions into `spec-lifecycle` for substantial work.

## Ask when uncertainty affects

- externally observable behavior;
- architecture or module boundaries;
- data model, retention, migration or compatibility;
- authorization, privacy, security or abuse controls;
- integrations or contracts;
- acceptance criteria;
- irreversible or expensive decisions;
- non-goals and scope boundaries.

## Do not ask when

- the answer is already explicit in Specs;
- repository inspection establishes the convention safely;
- the choice is a small reversible implementation detail;
- asking would merely transfer ordinary engineering judgment to the user.

## Deep discovery mode

When the user explicitly requests a deep interview/grill, explore as applicable:

1. intent and target users;
2. success/failure outcomes;
3. domain rules and invariants;
4. boundaries and integrations;
5. data lifecycle;
6. security/privacy;
7. compatibility/migration;
8. operational expectations;
9. edge cases/failure modes;
10. non-goals;
11. acceptance criteria.

Do not turn deep discovery into an unbounded questionnaire. Prioritize consequential decisions.
