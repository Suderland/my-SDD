---
name: security
description: Applies secure software engineering to authentication, authorization, sensitive data, trust boundaries, APIs, dependencies, secrets, cryptography, abuse cases and externally exposed features. Use whenever a change affects security-relevant behavior or threat surface.
---


# Security

Treat security as a design constraint, not a final scan.

## Workflow

1. Identify assets, actors, trust boundaries and externally controlled input.
2. Identify abuse/failure modes relevant to the change.
3. Apply least privilege and deny-by-default authorization where appropriate.
4. Validate and canonicalize untrusted input at boundaries.
5. Protect sensitive data in transit, at rest and in logs according to project needs.
6. Use established cryptographic libraries/protocols; do not design custom crypto.
7. Keep secrets out of source, tests, Specs and logs.
8. Review dependency and supply-chain impact of new packages.
9. Add security-focused tests for critical authorization/input cases.
10. Verify security assumptions before completion.

## High-priority review areas

- authentication/session lifecycle;
- tenant/object-level authorization;
- injection and unsafe interpretation;
- secret/token handling;
- file/path handling;
- SSRF/outbound requests;
- deserialization;
- sensitive logging;
- rate/abuse controls when exposed;
- dependency provenance and update risk.

Do not weaken security controls to make tests or local development easier without an explicit safe alternative.
