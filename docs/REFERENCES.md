# Design References

my-SDD is an original synthesis. It intentionally does not vendor or concatenate third-party Skill text. The following sources informed design choices and should be re-reviewed when evolving the framework:

## Agent Skill authoring

- Anthropic Agent Skills best practices: concise Skills, frontmatter discovery, progressive disclosure, one-level-deep references, deterministic scripts, evaluation-driven development.
- Skill Creator workflow supplied during design: capture intent, draft, create realistic evals, compare behavior, grade/analyze, iterate, and optimize triggering.

## Skill repositories reviewed during planning

- `wshobson/agents`: architecture patterns, JavaScript testing patterns, E2E testing patterns.
- `luckys/agent-skills`: DDD/TDD/OOP/refactoring/REST patterns.
- `PyModel/react-frontend-skills`: compact Vitest/Playwright Skills and rule prioritization.
- `mblode/agent-skills`: AGENTS.md/codebase architecture and Skill authoring patterns.
- other public SDD/TDD examples were used only as comparative inspiration for workflow ideas.

## External engineering references

- Google Testing Blog: test pyramid/E2E trade-offs and higher-fidelity test doubles.
- Playwright documentation: resilient user-facing locators and auto-waiting.
- Stryker documentation: mutation-testing concepts and interpretation.
- Pact documentation: consumer/provider contract-testing concepts.
- Hypothesis documentation: property-based testing concepts.

When borrowing implementation material in future revisions, verify the source license and add explicit attribution as required. Prefer extracting principles over copying prose/code.
