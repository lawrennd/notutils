---
id: "2025-07-13_github-actions-pypi-release"
title: "Set up GitHub Actions for automated PyPI release via Poetry on new version tag"
status: "proposed"
priority: "high"
created: "2025-07-13"
last_updated: "2025-07-13"
owner: "Neil Lawrence"
github_issue: ""
dependencies:
  - "CIP-0002"
tags:
  - "backlog"
  - "infrastructure"
  - "ci-cd"
  - "release"
  - "poetry"
  - "pypi"
---

# Task: Set up GitHub Actions for automated PyPI release via Poetry on new version tag

## Description

Implement a GitHub Actions workflow to automatically build and publish the package to PyPI using Poetry whenever a new version tag is pushed to the repository. This will streamline the release process, reduce manual errors, and ensure that new versions are published promptly.

The workflow should:
- Trigger on new version tags (e.g., v1.2.3)
- Build the package using Poetry
- Publish the package to PyPI using a secure token
- Run on the main branch only
- Provide clear feedback on release status and errors
- Fail gracefully if build or upload fails
- Optionally upload build artifacts for review

## Acceptance Criteria

- [ ] GitHub Actions workflow file created in `.github/workflows/`
- [ ] Workflow triggers on new version tag (e.g., v1.2.3)
- [ ] Package is built using Poetry
- [ ] Package is published to PyPI using a secure token
- [ ] Release only occurs on main branch
- [ ] Build artifacts uploaded for review (optional)
- [ ] Release status and errors reported in GitHub interface
- [ ] Workflow runs in under 5 minutes
- [ ] Documentation updated to describe release process

## Implementation Notes

### Technical Approach
1. *Workflow Structure*:
   - Use `ubuntu-latest` as the runner
   - Trigger on `push` to tags matching `v*.*.*`
   - Use Poetry for build and publish

2. *PyPI Publishing*:
   - Use `POETRY_PYPI_TOKEN_PYPI` secret for authentication
   - Build and publish with `poetry build` and `poetry publish`
   - Ensure version in `pyproject.toml` matches tag

3. *Error Handling*:
   - Fail workflow if build or publish fails
   - Provide clear error messages in GitHub Actions UI

4. *Security*:
   - Use GitHub secrets for PyPI token
   - Restrict workflow to main branch

### Dependencies
- Requires implementation of CIP-0002 (Comprehensive Testing Framework)
- Poetry must be configured for publishing
- PyPI token must be added to GitHub secrets

### Configuration Files Needed
- `.github/workflows/release.yml` - Main release workflow
- `pyproject.toml` - Ensure versioning is correct
- Poetry configuration for publishing

## Related

- CIP: 0002 (Comprehensive Testing Framework)
- PRs: 
- Documentation: [Poetry Publishing](https://python-poetry.org/docs/publishing/), [GitHub Actions Documentation](https://docs.github.com/en/actions), [PyPI Publishing](https://pypi.org/help/#uploading)

## Progress Updates

### 2025-07-13
Task created with Proposed status. Waiting for implementation of CIP-0002 and PyPI token setup before proceeding. 