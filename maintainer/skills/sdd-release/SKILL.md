---
name: sdd-release
description: Prepares and validates releases of the my-SDD framework, including repository validation, versioning, compatibility, changelog notes and installer/update safety. Use only when releasing or tagging my-SDD itself.
---


# SDD Release

## Release workflow

1. Run `python scripts/validate_repo.py`.
2. Run `python -m unittest discover -s tests -v`.
3. Review changed Skills and their evals.
4. Confirm installer `init` and `update` preserve project `.agents/specs/`.
5. Update `VERSION` using semantic versioning.
6. Document behavior/compatibility changes.
7. Review final diff for generated/debug/secrets artifacts.
8. Tag/release only after validation passes.

Treat changes to `AGENTS.md`, Skill names/descriptions and installer behavior as compatibility-sensitive because they can alter agent behavior across projects.
