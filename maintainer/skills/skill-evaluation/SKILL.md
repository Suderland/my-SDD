---
name: skill-evaluation
description: Designs and validates evaluations for my-SDD Skills, including trigger/near-miss cases, behavioral assertions, baseline comparisons, token/time trade-offs and regression testing. Use when deciding whether a Skill improves agent behavior or when revising a Skill description/workflow.
---


# Skill Evaluation

Evaluate behavior, not merely document shape.

## Evaluation set

Include realistic prompts covering:

- clear should-trigger cases;
- implicit should-trigger cases;
- near-miss should-not-trigger cases;
- edge cases competing with adjacent Skills;
- at least one failure mode the Skill was created to correct.

## Assertions

Prefer objectively verifiable assertions for structure, commands, files, traceability and safety-critical workflow. Use qualitative review for judgment-heavy architecture/writing quality.

## Compare

Where feasible compare:

- with-Skill vs baseline;
- previous Skill vs revised Skill;
- pass rate;
- tokens/context loaded;
- runtime;
- flaky/low-discrimination assertions.

A Skill that improves pass rate slightly while greatly increasing context may be a regression for my-SDD's goals.

## Trigger quality

Test both recall and precision. Vague descriptions cause under/over-triggering and permanent metadata cost.
