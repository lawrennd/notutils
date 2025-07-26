---
id: "2025-07-15_documentation-404-investigation"
title: "Investigate 404 error for documentation at inverseprobability.com/notutils"
status: "proposed"
priority: "high"
created: "2025-07-15"
last_updated: "2025-07-15"
owner: "Neil Lawrence"
dependencies: ["2025-07-15_documentation-deployment"]
tags:
  - infrastructure
  - documentation
  - deployment
  - troubleshooting
---

# Task: Investigate 404 error for documentation at inverseprobability.com/notutils

## Description

The documentation deployment is not working correctly. The URL https://inverseprobability.com/notutils/ returns a 404 error, indicating that either the deployment failed or the URL structure is incorrect.

## Current Status

- ❌ Documentation not accessible at inverseprobability.com/notutils/
- ❌ 404 error when accessing the URL
- ❌ gh-pages branch not created (as of last check)
- ✅ GitHub Actions workflow is configured
- ✅ Sphinx documentation builds successfully locally

## Investigation Points

### 1. GitHub Actions Workflow Status
- Check if the documentation workflow is running successfully
- Verify if gh-pages branch is being created
- Look for any error messages in the workflow logs

### 2. inverseprobability.com Structure
- Determine how inverseprobability.com is set up
- Check if it's a GitHub Pages site for a different repository
- Understand the URL routing structure

### 3. Deployment Configuration
- Verify if the `destination_dir: notutils` setting is correct
- Check if the deployment is going to the right location
- Ensure the gh-pages action has proper permissions

### 4. Repository Structure
- Check if the notutils repository is part of a larger organization setup
- Verify if there are any special requirements for this domain

## Possible Issues

### Issue 1: Wrong Repository
- inverseprobability.com might be served from a different repository
- The notutils documentation might need to be deployed to that repository instead

### Issue 2: Incorrect URL Structure
- The URL might need to be different (e.g., inverseprobability.com/projects/notutils)
- The domain routing might not support subdirectories

### Issue 3: Deployment Failure
- The GitHub Actions workflow might be failing silently
- The gh-pages branch might not be created due to permissions

### Issue 4: Domain Configuration
- The domain might not be configured to serve from the notutils repository
- DNS or GitHub Pages settings might need adjustment

## Investigation Steps

1. **Check GitHub Actions Logs**
   - Review the documentation workflow runs
   - Look for any error messages or warnings
   - Verify if gh-pages branch is being created

2. **Examine inverseprobability.com Setup**
   - Check what repository serves inverseprobability.com
   - Understand the current URL structure
   - Look for existing documentation or projects

3. **Test Alternative URLs**
   - Try inverseprobability.com/projects/notutils
   - Try inverseprobability.com/docs/notutils
   - Check if there are other project URLs that work

4. **Verify Repository Permissions**
   - Ensure the workflow has permission to create gh-pages branch
   - Check if GitHub Pages is enabled for the repository

## Acceptance Criteria

- [ ] Documentation is accessible at a working URL
- [ ] GitHub Actions workflow runs successfully
- [ ] gh-pages branch is created and updated
- [ ] URL structure is documented and understood
- [ ] Deployment process is reliable and automated

## Related

- GitHub Actions workflow: .github/workflows/docs.yml
- Previous task: 2025-07-15_documentation-deployment
- Sphinx configuration: docs/source/conf.py

## Progress Updates

### 2025-07-15
Task created. 404 error identified at inverseprobability.com/notutils/. Need to investigate the deployment process and domain configuration. 