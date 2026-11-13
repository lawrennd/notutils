---
id: "2025-07-13_github-actions-pypi-release"
title: "Set up GitHub Actions for automated PyPI release via uv on new version tag"
status: "In Progress"
priority: "high"
created: "2025-07-13"
last_updated: "2026-11-13"
owner: "Neil Lawrence"
github_issue: ""
dependencies:
  - "CIP-0002"
  - "CIP-0003"
tags:
  - "backlog"
  - "infrastructure"
  - "ci-cd"
  - "release"
  - "uv"
  - "pypi"
---

# Task: Set up GitHub Actions for automated PyPI release via uv on new version tag

## Description

Implement a GitHub Actions workflow to automatically build and publish the package to PyPI using uv whenever a new version tag is pushed to the repository. This will streamline the release process, reduce manual errors, and ensure that new versions are published promptly. Packaging tooling moved from Poetry to uv in CIP-0003.

The workflow should:
- Trigger on new version tags (e.g., v1.2.3)
- Build the package using uv
- Publish the package to PyPI using a secure token
- Run on the main branch only
- Provide clear feedback on release status and errors
- Fail gracefully if build or upload fails
- Optionally upload build artifacts for review

## Acceptance Criteria

- [x] GitHub Actions workflow file created in `.github/workflows/publish.yml`
- [x] Workflow triggers on GitHub Release published (tag `vX.Y.Z`)
- [x] Package is built using uv
- [x] Package is published to PyPI using `UV_PUBLISH_TOKEN` / `PYPI_API_TOKEN`
- [x] Uses `release` environment
- [x] Build artifacts uploaded for review
- [ ] Release status and errors reported in GitHub interface (validate on first release)
- [ ] Workflow runs in under 5 minutes (validate on first release)
- [ ] Documentation updated to describe release process

## Implementation Notes

### Technical Approach
1. *Workflow Structure*:
   - Use `ubuntu-latest` as the runner
   - Trigger on `push` to tags matching `v*.*.*`
   - Use uv for build and publish

2. *PyPI Publishing*:
   - Use `UV_PUBLISH_TOKEN` (from `secrets.PYPI_API_TOKEN`) for authentication
   - Build and publish with `uv build` and `uv publish` (CIP-0003 succeeded Poetry for packaging)
   - Ensure version in `pyproject.toml` matches tag

3. *Error Handling*:
   - Fail workflow if build or publish fails
   - Provide clear error messages in GitHub Actions UI

4. *Security*:
   - Use GitHub secrets for PyPI token
   - Restrict workflow to main branch

### Dependencies
- Requires implementation of CIP-0002 (Comprehensive Testing Framework)
- uv must be available in the release job (`astral-sh/setup-uv`)
- PyPI token must be added to GitHub secrets

### Configuration Files Needed
- `.github/workflows/release.yml` - Main release workflow
- `pyproject.toml` - Ensure versioning is correct
- `uv.lock` - Committed lockfile from CIP-0003

## Related

- CIP: 0002 (Comprehensive Testing Framework), 0003 (Migrate from Poetry to uv)
- PRs: [#1](https://github.com/lawrennd/notutils/pull/1)
- Documentation: [uv publishing](https://docs.astral.sh/uv/guides/publish/), [GitHub Actions Documentation](https://docs.github.com/en/actions), [PyPI Publishing](https://pypi.org/help/#uploading)

## Progress Updates

### 2025-07-13
Task created with Proposed status. Waiting for implementation of CIP-0002 and PyPI token setup before proceeding.

### 2026-11-13
Reworked PR #1 onto post-CIP-0003 `main`: `publish.yml` now uses `astral-sh/setup-uv`, `uv sync` / `uv run pytest` / `uv build` / `uv publish`, and checks `[project].version` against the release tag. 