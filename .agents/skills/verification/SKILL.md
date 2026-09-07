---
name: verification
description: Performs evidence-based final verification of software changes using plan-validate-execute-verify loops, test/build/static/security checks, diff inspection and requirement reconciliation. Use before declaring material work complete, merging, releasing, migrating or performing risky operations.
---


# Verification

Completion requires observed evidence.

## Workflow

1. Re-read the relevant requirements and acceptance criteria.
2. Identify required verification from the change risk and project policy.
3. Run the narrowest checks that give fast feedback.
4. Fix failures and repeat until clean.
5. Run the broader project-required suite.
6. Inspect the final diff and generated artifacts.
7. Reconcile implementation/tests with Spec state.
8. Report commands/checks actually executed and their outcomes.

## Typical evidence

- formatter/linter/static analysis;
- type checks;
- unit/integration/contract/E2E tests;
- mutation testing;
- build/package;
- migrations/schema verification;
- security/dependency checks;
- manual/visual checks only where automation is unsuitable;
- requirement-to-test traceability.

## Rules

- Never state a check passed if it was not executed.
- Distinguish pre-existing failures from regressions introduced by the change.
- Do not weaken gates to obtain green output.
- When a required check cannot run, report the limitation and residual risk explicitly.
