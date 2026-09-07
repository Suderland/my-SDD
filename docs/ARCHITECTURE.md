# my-SDD Architecture

## Purpose

my-SDD is a portable engineering governance layer for AI coding agents. It separates stable reusable engineering guidance from project-specific truth.

## Three-part model

### AGENTS.md — governance

A compact execution contract. It establishes precedence, context discipline, workflow, testing baseline and Definition of Done. It routes agents to Skills and Specs rather than embedding an encyclopedia of engineering knowledge.

### `.agents/skills/` — reusable engineering knowledge

Core Skills are installed into every project. Each Skill should be cohesive, concise and progressively disclosed:

1. frontmatter metadata for discovery;
2. `SKILL.md` for operational workflow;
3. one-level-deep references/scripts/assets loaded only when needed.

### `.agents/specs/` — project truth

Project-specific requirements, plans, tasks, architecture decisions, data/API specifications and current execution state live here. The directory starts empty.

## Core and packs

- **Core**: universal engineering Skills copied from `.agents/skills/`.
- **Backend pack**: backend development, API, database and observability.
- **Frontend pack**: frontend architecture and accessibility.
- **Stack packs**: technology-specific implementation guidance; intentionally sparse in v0.1.
- **Maintainer pack**: Skill authoring/evaluation and release workflow for the my-SDD repository itself; not installed in normal projects.

## Precedence

`user > project Specs > AGENTS.md > applicable Skills > framework conventions > general knowledge`

## Context budget

The primary optimization target is decision quality per token loaded. Skills should omit generic textbook explanations the model already knows and focus on operational constraints, project-independent decision rules, failure modes, and verification loops.

## Update boundary

`my_sdd.py update` may update framework-owned `AGENTS.md` and installed Skills. It must never modify `.agents/specs/`.
