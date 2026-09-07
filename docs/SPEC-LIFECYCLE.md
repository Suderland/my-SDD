# Spec Lifecycle

Substantial features use a four-artifact model:

```text
SPEC.md  -> normative WHAT and acceptance criteria
PLAN.md  -> implementation HOW and trade-offs
TASKS.md -> executable work mapped to requirements/tests
STATE.json -> machine-readable current progress and evidence
```

## Requirement IDs

Use stable identifiers such as `REQ-AUTH-001`. Never renumber or reuse an ID after it has been referenced.

## States

Normal path:

`not_started -> in_progress -> implemented -> verified`

Side states:

- `blocked`
- `deferred`
- `cancelled`

`implemented` means the implementation appears to exist. `verified` means acceptance criteria and required verification evidence have been established.

## Feature layout

```text
.agents/specs/
├── INDEX.md                # generated summary once first feature exists
└── features/
    └── AUTH-001/
        ├── SPEC.md
        ├── PLAN.md
        ├── TASKS.md
        └── STATE.json
```

The project begins with `.agents/specs/` empty. `INDEX.md` is generated only after feature state exists.

## Reconciliation

A reconciliation pass checks for:

- requirements without tasks;
- tasks without requirement linkage;
- `verified` requirements without evidence;
- implementation completed while state is stale;
- tests that do not prove acceptance criteria;
- plan/spec contradictions;
- stale blockers or waivers.
