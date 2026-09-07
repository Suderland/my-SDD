---
name: software-design
description: Applies senior-level object/module design using SOLID as heuristics, cohesion/coupling, composition, information hiding, refactoring and design patterns. Use when creating or reviewing classes/modules, introducing abstractions, reducing complexity, refactoring, or evaluating maintainability trade-offs.
---


# Software Design

Use principles as decision heuristics, not checkboxes.

## Core heuristics

- Give each module one cohesive reason to change at its level of abstraction.
- Hide volatile implementation details behind stable contracts when that improves change isolation.
- Prefer composition over inheritance unless a true substitutable hierarchy exists.
- Introduce abstractions for observed variation or important boundaries, not imagined future reuse.
- Make illegal states difficult to represent.
- Keep mutation and side effects near explicit boundaries.
- Prefer explicit domain types over primitive obsession when the concept has rules or semantics.

## SOLID, operationalized

- **SRP**: split when responsibilities change for materially different reasons and cohesion improves.
- **OCP**: prefer extension points only where variation is expected or already present.
- **LSP**: subtypes must preserve caller-visible behavioral contracts.
- **ISP**: consumers should depend on the smallest coherent capability they need.
- **DIP**: stable policy should not depend directly on volatile details.

## Pattern use

Name a pattern only when it clarifies communication. Prefer the smallest structure that solves the actual force. Remove pattern ceremony that does not reduce coupling, complexity or risk.

## Review questions

- What knowledge does this module own?
- What can change independently?
- Does this abstraction hide volatility or merely add indirection?
- Can behavior be tested without irrelevant infrastructure?
- Is failure behavior explicit?
- Is naming aligned with domain language?
