---
name: architecture
description: Guides system architecture using Clean Architecture, Hexagonal Architecture, DDD, modular boundaries and dependency direction. Use for service/module decomposition, domain boundaries, integration seams, architectural refactors, cross-cutting dependencies, or deciding where responsibilities belong.
---


# Architecture

Optimize for explicit boundaries, changeability and testability rather than pattern compliance.

## Decision workflow

1. Identify business capabilities and externally visible responsibilities.
2. Identify volatility and trust boundaries.
3. Keep domain policy independent from transport, frameworks and persistence.
4. Direct dependencies toward stable policy.
5. Define ports/interfaces only at meaningful boundaries or substitution seams.
6. Choose the simplest deployment shape that satisfies current constraints.
7. Record consequential trade-offs in the project Spec/ADR.

## Clean/Hexagonal guidance

- Domain/application policy must not require infrastructure to be testable.
- Infrastructure implements outward-facing ports/contracts.
- Delivery mechanisms adapt external input to application use cases.
- Do not create layers that only forward calls without isolating policy or volatility.

## DDD guidance

Use DDD tactically where domain complexity justifies it:

- preserve ubiquitous language;
- make invariants explicit;
- use value objects for meaningful immutable concepts;
- treat aggregate boundaries as consistency boundaries;
- use domain events for meaningful domain facts, not as an automatic decoupling trick;
- avoid forcing rich-domain patterns onto CRUD-only areas.

## Modularity

Prefer high cohesion within modules and explicit contracts between modules. Prevent cycles. Keep shared kernels small and intentional.

## Avoid

- framework-centric domain models;
- interface-per-class cargo culting;
- repository abstractions that leak query/storage details into domain policy;
- distributed systems without a real deployment/scale/team boundary need;
- speculative microservices;
- architecture diagrams that do not match the code.
