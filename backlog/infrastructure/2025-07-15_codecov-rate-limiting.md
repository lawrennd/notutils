---
id: "2025-07-15_codecov-rate-limiting"
title: "Fix Codecov rate limiting with repository upload token"
status: "proposed"
priority: "medium"
created: "2025-07-15"
last_updated: "2025-07-15"
owner: "Neil Lawrence"
dependencies: []
tags:
  - infrastructure
  - ci-cd
  - codecov
  - rate-limiting
---

# Task: Fix Codecov rate limiting with repository upload token

## Description

Codecov is currently rate limiting uploads with the error: "Rate limit reached. Please upload with the Codecov repository upload token to resolve issue." This is preventing coverage reports from being uploaded to Codecov.

## Current Status

- ❌ Codecov uploads are failing due to rate limiting
- ❌ No repository upload token configured
- ✅ Coverage reports are still being generated locally
- ✅ Coverage artifacts are still being uploaded to GitHub Actions

## Error Details

```
Error uploading to https://codecov.io: Error: There was an error fetching the storage URL during POST: 429 - {"message":"Rate limit reached. Please upload with the Codecov repository upload token to resolve issue. Expected time to availability: 567s."}
```

## Solution

1. **Get Codecov Token**: Obtain a repository upload token from Codecov
2. **Add GitHub Secret**: Add the token as `CODECOV_TOKEN` in GitHub repository secrets
3. **Update Workflow**: Configure the Codecov action to use the token
4. **Test Upload**: Verify that coverage uploads work correctly

## Implementation Steps

### Step 1: Get Codecov Token
1. Go to https://codecov.io
2. Sign in and navigate to the notutils repository
3. Go to Settings > Repository Upload Token
4. Copy the upload token

### Step 2: Add GitHub Secret
1. Go to GitHub repository settings
2. Navigate to Secrets and variables > Actions
3. Add new repository secret:
   - Name: `CODECOV_TOKEN`
   - Value: [Codecov upload token]

### Step 3: Update Workflow
The workflow has been updated to use the token:
```yaml
- name: Upload coverage reports to Codecov
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
    flags: unittests
    name: codecov-umbrella
    fail_ci_if_error: false
    token: ${{ secrets.CODECOV_TOKEN }}
```

## Acceptance Criteria

- [ ] Codecov uploads succeed without rate limiting errors
- [ ] Coverage reports are visible on Codecov dashboard
- [ ] Coverage badge updates correctly
- [ ] CI/CD pipeline doesn't fail due to Codecov issues

## Technical Notes

- **Token Security**: The Codecov token should be kept secure and not committed to the repository
- **Fallback**: Coverage artifacts are still uploaded to GitHub Actions as backup
- **Rate Limits**: Codecov has rate limits for anonymous uploads, but tokens provide higher limits

## Related

- GitHub Actions workflow: .github/workflows/test.yml
- Codecov configuration: coverage.xml generation

## Progress Updates

### 2025-07-15
Task created. Codecov rate limiting issue identified. Workflow updated to use token, but token needs to be added to GitHub secrets. 