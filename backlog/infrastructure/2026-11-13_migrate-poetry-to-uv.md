---
id: "2026-11-13_migrate-poetry-to-uv"
title: "Migrate packaging from Poetry to uv"
status: "In Progress"
priority: "High"
created: "2026-11-13"
last_updated: "2026-11-13"
owner: "Neil Lawrence"
github_issue: ""
dependencies: ""
tags:
- backlog
- packaging
- uv
- poetry
- ci
---

# Task: Migrate packaging from Poetry to uv

## Description

Execute CIP-0003 on branch `cip0003-migrate-poetry-to-uv`: convert `pyproject.toml` to PEP 621 + hatchling, commit `uv.lock`, switch GitHub Actions and README to uv, and remove Poetry as the contributor/CI tool.

## Acceptance Criteria

- [x] `pyproject.toml` uses `[project]` / `[dependency-groups]` / hatchling
- [x] `uv.lock` is generated (commit pending)
- [x] Workflows `test.yml`, `lint.yml`, and `docs.yml` use `astral-sh/setup-uv` and `uv sync` / `uv run`
- [x] README documents `uv sync` and `uv run pytest` for contributors
- [x] `uv run pytest` passes locally with coverage ≥ 80%
- [x] `uv run mypy notutils/notutils.py --ignore-missing-imports` succeeds
- [x] `uv build` produces a wheel that includes the `notutils` package

## Implementation Notes

Mirror the approach taken in mlai CIP-0009 (`astral-sh/setup-uv@v6`, `[tool.uv] default-groups = ["dev"]`). Work in the `notutils-cip0003` git worktree.

## Related

- CIP: 0003
- PRs:
- Documentation: README Development & Contributing

## Progress Updates

### 2026-11-13

Task created; CIP-0003 accepted and implementation started on worktree branch `cip0003-migrate-poetry-to-uv`.

Local validation complete: 71 tests passed, mypy clean, wheel/sdist built, docs HTML built. Awaiting commit/PR.
