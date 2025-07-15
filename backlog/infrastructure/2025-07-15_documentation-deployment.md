---
id: "2025-07-15_documentation-deployment"
title: "Deploy Sphinx documentation to inverseprobability.com/notutils"
status: "proposed"
priority: "high"
created: "2025-07-15"
last_updated: "2025-07-15"
owner: "Neil Lawrence"
dependencies: []
tags:
  - infrastructure
  - documentation
  - deployment
  - sphinx
---

# Task: Deploy Sphinx documentation to inverseprobability.com/notutils

## Description

The Sphinx documentation is currently being built successfully by GitHub Actions, but it's not deployed to the expected public URL at https://inverseprobability.com/notutils. The documentation should be accessible at this URL for users to browse the API reference and usage examples.

## Current Status

- ✅ Sphinx documentation framework is set up and working
- ✅ GitHub Actions workflow builds documentation successfully
- ✅ Documentation artifacts are generated and available for download
- ❌ Documentation is not deployed to inverseprobability.com/notutils
- ❌ No public URL for users to access the documentation

## Requirements

1. **Deployment Target**: Documentation should be accessible at https://inverseprobability.com/notutils
2. **Automated Deployment**: Documentation should be automatically deployed when changes are pushed to main branch
3. **Version Control**: Documentation should reflect the current state of the codebase
4. **Accessibility**: Documentation should be publicly accessible without authentication

## Implementation Options

### Option 1: GitHub Pages (Recommended)
- Deploy to GitHub Pages using gh-pages branch
- Update GitHub Actions workflow to deploy to gh-pages branch
- Documentation will be accessible at inverseprobability.com/notutils (since inverseprobability.com is already a GitHub Pages server)

### Option 2: Read the Docs
- Host documentation on Read the Docs platform
- Configure custom domain
- Integrate with GitHub repository for automatic builds

## Acceptance Criteria

- [ ] Documentation is accessible at https://inverseprobability.com/notutils
- [ ] Documentation automatically updates when code changes are pushed
- [ ] Documentation reflects the current state of the main branch
- [ ] All API functions are properly documented and accessible
- [ ] Search functionality works correctly
- [ ] Mobile-responsive design is maintained

## Technical Considerations

- **Build Process**: Documentation is currently built with `make html` in the docs directory
- **Artifacts**: Built documentation is in `docs/build/html/`
- **Dependencies**: Requires Sphinx and sphinx-rtd-theme
- **Domain Configuration**: May require DNS changes for inverseprobability.com

## Related

- CIP: 0001 (Comprehensive Code Documentation)
- GitHub Actions workflow: .github/workflows/docs.yml
- Sphinx configuration: docs/source/conf.py

## Progress Updates

### 2025-07-15
Task created. Sphinx documentation is building successfully but not deployed to public URL. Need to investigate deployment options and implement automated deployment pipeline. 