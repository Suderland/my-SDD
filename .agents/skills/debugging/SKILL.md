---
name: debugging
description: Uses evidence-driven debugging to reproduce, localize and fix defects without speculative rewrites. Use for bugs, failing tests, regressions, unexpected behavior, flaky failures, performance anomalies, or production incidents requiring root-cause analysis.
---


# Debugging

Prefer evidence over intuition.

## Workflow

1. Define expected vs actual behavior precisely.
2. Reproduce the failure with the smallest reliable case.
3. Gather relevant logs/state/traces without exposing secrets.
4. Narrow the failing boundary using binary isolation where useful.
5. Form one falsifiable hypothesis at a time.
6. Test the hypothesis with the least invasive experiment.
7. Identify root cause, not only the nearest symptom.
8. Add/strengthen a regression test when the defect is reproducible automatically.
9. Apply the smallest coherent fix.
10. Verify the original failure and adjacent behavior.

## Avoid

- changing multiple unrelated things before re-testing;
- suppressing errors/retries to hide a deterministic defect;
- relying on log volume instead of targeted evidence;
- assuming correlation proves causation;
- deleting failing tests without proving they are invalid.

For flaky tests, classify the nondeterminism source (time, ordering, shared state, network, async waiting, random seed, resource contention) and remove it rather than normalizing retries.
