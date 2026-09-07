# Engineering Contract

This file is the root execution contract for AI-assisted engineering in this repository.

## 1. Mission

Deliver production-grade software with the smallest sufficient context, explicit requirements, deliberate architecture, measurable verification, and traceable implementation evidence.

## 2. Instruction precedence

Apply instructions in this order when they conflict:

1. Explicit current user instruction.
2. Project-specific specifications in `.agents/specs/`.
3. This `AGENTS.md` engineering contract.
4. Applicable Skills in `.agents/skills/`.
5. Framework or library conventions.
6. General model knowledge.

Do not silently override a higher-priority rule. Surface material conflicts.

## 3. Context discipline

Treat context as a finite engineering resource.

Before non-trivial work:

1. Classify the task.
2. Read only the relevant project Specs.
3. Identify applicable Skills from `.agents/skills/`.
4. Load only those Skills.
5. Load a Skill's references only when the task requires them.

Do not recursively read the entire `.agents/` tree. Do not load all Skills "just in case".

If `.agents/specs/` is absent or empty, treat the project as having no persisted Specs yet.

## 4. Requirements before implementation

For material new behavior, use `requirements-discovery` when requirements contain consequential uncertainty.

Inspect existing Specs and code before asking questions. Ask only when an unresolved decision can materially change behavior, architecture, security, data, compatibility, acceptance criteria, cost of reversal, or scope.

Do not ask questions whose answers can be established safely from the repository.

For substantial features, use `spec-lifecycle` to create or update a feature Spec before implementation.

## 5. Planning

Plan before making broad, risky, cross-cutting, schema-changing, security-sensitive, or multi-component changes.

A useful plan identifies:

- affected requirements;
- architectural boundaries;
- data/API changes;
- migration or compatibility concerns;
- test strategy;
- risks and rollback needs;
- verifiable completion criteria.

Do not produce ceremonial plans for trivial changes.

## 6. Architecture and design

Prefer simple, cohesive designs with explicit boundaries.

- Keep domain/business policy independent from delivery and infrastructure concerns.
- Direct dependencies toward stable policy.
- Use abstractions at real volatility boundaries, not mechanically.
- Preserve domain language in code and Specs.
- Prefer composition and small cohesive modules over inheritance-heavy structures.
- Avoid speculative generalization.
- Make important architectural trade-offs explicit.

Use `architecture` and `software-design` for material design decisions.

## 7. Implementation

- Make the smallest coherent change that satisfies the requirement.
- Follow existing repository conventions unless a higher-priority instruction changes them.
- Preserve backward compatibility unless the Spec intentionally breaks it.
- Validate inputs at trust boundaries.
- Handle errors explicitly and preserve useful diagnostics.
- Do not introduce dependencies without a concrete benefit and maintenance rationale.
- Never hide failing validation by weakening gates without an explicit project decision.

## 8. Testing policy

Use the `testing` Skill for production behavior changes.

For executable systems, these are mandatory by default:

- unit testing for project-owned deterministic behavior;
- end-to-end testing for at least the critical public system journey(s);
- mutation testing over meaningful project-owned logic.

A category may be waived only when genuinely inapplicable. Waivers must be explicit and justified in the project testing Spec or state. "Not implemented yet" is not a waiver.

Add integration, contract, property-based, regression, security, performance, accessibility and resilience tests when the relevant risk exists.

Do not equate coverage percentage with correctness.

## 9. Verification

Use `verification` before declaring material work complete.

At minimum, verify the relevant subset of:

- static analysis/linting;
- unit tests;
- integration/contract tests;
- E2E tests;
- mutation tests;
- build/package;
- security checks;
- migrations;
- changed diff against requirements.

Never claim a command or test passed unless it was actually executed and its result observed.

## 10. Spec state

Feature lifecycle state is authoritative only when supported by implementation evidence.

Default requirement states:

`not_started -> in_progress -> implemented -> verified`

Side states: `blocked`, `deferred`, `cancelled`.

`verified` is the normal terminal success state. Code presence alone is insufficient.

After meaningful implementation work, reconcile the relevant Spec, tasks, state, code and tests.

## 11. Security and destructive operations

Use `security` for authentication, authorization, sensitive data, trust boundaries, secrets, cryptography, dependency risk, or externally exposed attack surfaces.

For destructive or irreversible operations:

1. create a reversible plan when feasible;
2. validate preconditions;
3. preserve or back up required state;
4. execute the smallest safe change;
5. verify the result.

Never expose secrets in source, logs, examples, tests, Specs, commits, or responses.

## 12. Repository and Git safety

- Do not discard unrelated user changes.
- Keep commits cohesive.
- Prefer conventional, descriptive commit messages where repository policy does not specify another format.
- Do not force-push or rewrite shared history unless explicitly requested.
- Review the final diff for accidental generated files, credentials, debug code, and unrelated changes.

## 13. Definition of Done

A material requirement is done only when:

1. acceptance criteria are satisfied;
2. required code/config/data changes exist;
3. required tests exist;
4. required verification passed;
5. relevant documentation/spec state is updated;
6. remaining risks are explicit;
7. requirement state is `verified`.

If any required evidence is missing, report the work as incomplete rather than overstating completion.
