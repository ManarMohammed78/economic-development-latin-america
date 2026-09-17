# Branching Workflow

For the Economic Development in Latin America app. Kept simple on purpose — one main branch, short-lived feature branches, pull requests for review.

## Branches

- **main** — always deployable. This is what Streamlit Community Cloud deploys from. No direct commits to main except for small documentation fixes.
- **feature/\*** — all new work. Examples:
  - `feature/overview-page`
  - `feature/social-development-page`
  - `feature/filters-and-missing-data`
  - `feature/insights-panel`
  - `feature/data-table-export`
- **fix/\*** — for bug fixes:
  - `fix/argentina-inflation-scale`

No `develop` branch needed for this size. If the team grows later, we can add it.

## Workflow Steps

1. **Create a branch from main**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/overview-page
   ```

2. **Commit often with clear messages**
   Use simple, descriptive messages:
   ```
   feat: add Overview page with GDP and unemployment charts
   fix: handle missing Brazil poverty data as 'No data available'
   docs: update README setup instructions
   style: adjust sidebar filter layout
   ```
   Keep commits small — one logical change per commit.

3. **Push and open a pull request**
   ```bash
   git push -u origin feature/overview-page
   ```
   Then open a PR on GitHub: feature branch → main.
   Add a short description, link the related Issue (e.g., Closes #2), and request a review.

4. **Review and merge**
   - Check the app still runs locally (`streamlit run app.py`)
   - Check the dataset still validates (`python scripts/validate_dataset.py`)
   - Reviewer approves, then squash and merge to keep history clean.
   - Delete the feature branch after merge.

5. **Pull updated main**
   ```bash
   git checkout main
   git pull origin main
   ```

## Commit Rules

- Commit messages in English, lower case type: `feat:`, `fix:`, `docs:`, `chore:`
- One sentence, under 50 characters for the first line
- No secrets or large data files in commits — the CSV is already in `data/` and should not be duplicated

## Deployment

Streamlit Cloud auto-deploys from `main`. So every merge to main should be tested locally first. If a deploy fails, fix on a new `fix/` branch and merge again.

## Issues

All Milestone 4 tasks are tracked as GitHub Issues (see `github-issues-milestone-4.md`). Each feature branch should link to its Issue number in the PR description.

This workflow matches the project's needs: small team, single source of truth on GitHub, static dataset, and Streamlit Cloud hosting as decided in Milestone 2.
