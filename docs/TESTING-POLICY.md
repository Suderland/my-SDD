# Testing Policy

## Mandatory baseline

For any executable project with project-owned behavior:

1. **Unit tests** are mandatory for deterministic project-owned behavior.
2. **E2E tests** are mandatory for at least the critical public system journey(s). E2E means exercising a public entry point through the relevant assembled stack; it does not necessarily mean a browser.
3. **Mutation testing** is mandatory over meaningful project-owned logic.

A mandatory category can be waived only if it is structurally inapplicable. The reason must be explicit in project Specs/configuration.

## Risk-driven additions

Add integration, contract, property-based, regression, performance, load, resilience, accessibility, security, migration and compatibility tests where the failure risk exists.

## Test selection rule

Prove a behavior at the lowest layer that detects the relevant failure reliably. Higher-level tests should protect boundary-specific risks rather than duplicate the same assertion at every layer.

## Mutation

Prefer changed-code or affected-module mutation runs during pull requests and broader scheduled mutation runs when full execution is expensive. Surviving mutants are test-quality findings requiring interpretation, not automatic production defects.

## Coverage

Coverage is diagnostic evidence, not the definition of correctness. Numeric thresholds belong to project-specific Specs/CI policy, not the universal Skill.
