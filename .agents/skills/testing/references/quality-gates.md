# Quality Gates

Inner loop: affected unit and smallest relevant integration tests. PR: required unit, relevant integration/contract, critical E2E, changed-code mutation where supported, static/build/security checks. Scheduled: full mutation, broad E2E matrices, performance/resilience as needed. Project Specs own numeric thresholds. Never lower gates silently.
