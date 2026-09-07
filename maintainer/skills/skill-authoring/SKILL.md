---
name: skill-authoring
description: Creates or improves my-SDD Agent Skills with concise frontmatter, progressive disclosure, deterministic resources and evaluation-driven iteration. Use when adding or modifying Skills in the my-SDD framework, not for ordinary project feature development.
---


# Skill Authoring

Create the smallest Skill that measurably improves agent decisions.

## Capture intent

Define:

1. what capability the Skill should enable;
2. when it should trigger;
3. expected outputs/behavior;
4. representative failure cases without the Skill;
5. how success can be evaluated.

## Authoring

- `name`: lowercase letters/numbers/hyphens; concise and activity-oriented.
- `description`: include both what the Skill does and concrete trigger contexts; this is the primary discovery mechanism.
- Keep `SKILL.md` operational and preferably well below 500 lines.
- Assume the model already knows generic textbook material.
- Put detailed variants in one-level-deep `references/`.
- Put deterministic/repetitive logic in `scripts/` and prefer executing it over loading its source.
- Put reusable templates/examples in `assets/`.
- Match instruction strictness to task fragility.

## Iteration

1. establish representative baseline behavior;
2. write minimal instructions for observed gaps;
3. run evals;
4. inspect decision quality, token/time cost and failure modes;
5. remove instructions that do not pull their weight;
6. generalize from failures rather than overfitting examples;
7. repeat until improvement is meaningful and stable.

Use `skill-evaluation` for the evaluation design.
