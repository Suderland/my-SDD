---
name: testing
description: Defines mandatory and risk-based software testing across unit, integration, contract, end-to-end, mutation, property-based, regression and non-functional tests. Use for any production behavior change, bug fix, test strategy, testing review, critical path, API/data change, or before declaring implementation verified.
---


# Testing

Use tests as executable evidence of behavior, not as a coverage-production exercise.

## Mandatory baseline

For every executable system with project-owned behavior:

1. **Unit testing is required** for meaningful deterministic project-owned logic.
2. **E2E testing is required** for at least the critical public system journey(s).
3. **Mutation testing is required** over meaningful project-owned logic.

A mandatory category may be waived only when structurally inapplicable. Record an explicit reason in project Specs/configuration. "Not implemented", "too slow" or "tooling not configured" is not a valid applicability waiver.

## Additional layers

- Integration: infrastructure/component boundaries.
- Contract: independently consumed HTTP/RPC/message contracts.
- Property-based: invariants, parsers, transformations, broad input spaces.
- Regression: confirmed reproducible defects.
- Performance/load/resilience/security/accessibility/migration/compatibility: when the corresponding risk or Spec exists.

## Selection rule

Prove behavior at the lowest layer that reliably detects the relevant failure. Add higher-layer tests only for risks that exist at those boundaries. Do not duplicate the same assertion mechanically at every layer.

## New behavior

1. Identify observable behavior and acceptance criteria.
2. Select the lowest sufficient test layer.
3. For testable business behavior, use a small Red -> Green -> Refactor loop unless Specs require another workflow.
4. Add boundary-specific integration/contract/E2E evidence.
5. Run mutation testing on affected meaningful logic.
6. Run required verification before completion.

## Bug fix

1. Reproduce the defect.
2. Add a regression test at the seam where the defect is observable when practical.
3. Confirm it fails for the intended reason.
4. Apply the minimal fix.
5. Confirm the regression and relevant suites pass.
6. When practical, confirm causality against the pre-fix behavior.
7. Run mutation testing when meaningful project-owned logic changed.

## Coverage

Coverage is diagnostic, not proof of correctness. Numeric thresholds belong to project Specs/CI configuration. For decision-heavy code, prefer branch/condition coverage where supported. Pair coverage with mutation evidence for critical logic.

## Test doubles

Prefer the highest fidelity that remains fast, deterministic, safe and maintainable: real implementation -> maintained fake -> stub/spy -> interaction mock. Mock when the interaction itself is the contract, not merely to isolate every class.

## E2E meaning

E2E exercises a public entry point through the relevant assembled stack. It can be browser, HTTP API, CLI, worker/event input, or another public system interface.

## Mutation

- target domain/business rules, authorization, validation, calculations, state transitions, parsers and other meaningful logic;
- use changed-code/affected-module mutation in PRs when full runs are expensive;
- use scheduled broader runs when appropriate;
- investigate surviving mutants; do not write meaningless assertions solely to kill them;
- justify exclusions for generated/trivial/framework glue.

## References

Load only as needed:

- `references/unit-testing.md`
- `references/integration-testing.md`
- `references/contract-testing.md`
- `references/e2e-testing.md`
- `references/mutation-testing.md`
- `references/property-based-testing.md`
- `references/quality-gates.md`

## Completion evidence

Report tests changed, commands actually executed, results observed, mutation outcome when required, waivers and remaining testing risk. Never claim unexecuted tests passed.
