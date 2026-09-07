---
name: spec-lifecycle
description: Creates and maintains project feature specifications, implementation plans, executable tasks, requirement status, traceability and reconciliation. Use for substantial new features, multi-step changes, persisted requirements, progress tracking, or when determining what is implemented, verified, blocked, or next.
---


# Spec Lifecycle

Use persistent Specs to preserve project truth across sessions without loading the full project context.

## Feature artifacts

For a substantial feature create:

```text
.agents/specs/features/<FEATURE-ID>/
├── SPEC.md
├── PLAN.md
├── TASKS.md
└── STATE.json
```

Use the templates in `assets/`. The project Specs directory starts empty.

## Lifecycle

1. **Specify** — write intent, scope, non-goals, stable requirement IDs and measurable acceptance criteria.
2. **Clarify** — invoke `requirements-discovery` for consequential unresolved decisions.
3. **Plan** — map architecture, data/API changes, migrations, risks, test strategy and rollout.
4. **Task** — split the plan into executable tasks linked to requirement IDs and required test evidence.
5. **Implement** — update requirement/task state as evidence changes.
6. **Verify** — move requirements to `verified` only after acceptance and required checks pass.
7. **Reconcile** — compare Spec, Plan, Tasks, State, implementation and tests; repair drift.
8. **Index** — run `scripts/spec_status.py` to regenerate `.agents/specs/INDEX.md` when feature state exists.

## Requirement state

Normal path:

`not_started -> in_progress -> implemented -> verified`

Side states: `blocked`, `deferred`, `cancelled`.

Do not skip directly to `verified` without evidence.

## Traceability

Every implementation task should map to at least one requirement. Every requirement should have acceptance criteria and, when implemented, evidence. Avoid tasks that exist only because a plan section mentioned them without a requirement/risk rationale.

## Reconciliation checks

Look for:

- missing or duplicate requirement/task IDs;
- requirements without tasks where work is required;
- tasks not linked to requirements;
- `verified` requirements with absent evidence;
- state inconsistent with code/tests;
- acceptance criteria not covered by verification;
- outdated blockers, waivers or plan assumptions.

## Deterministic status

Run:

```bash
python .agents/skills/spec-lifecycle/scripts/spec_status.py .
```

The script reads `STATE.json` files and writes the generated `INDEX.md`. Do not hand-edit generated progress values.
