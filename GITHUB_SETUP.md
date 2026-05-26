# 🚀 GitHub Hosting Instructions
## TOR Checklist — GDCC Open Data 2569

Complete step-by-step guide to push this package to GitHub and manage
document versions going forward.

---

## Prerequisites

Install these once on your machine:

| Tool | Download | Verify Install |
|------|----------|----------------|
| **Git** | https://git-scm.com/downloads | `git --version` |
| **GitHub account** | https://github.com/signup | — |
| **GitHub CLI** *(optional but recommended)* | https://cli.github.com | `gh --version` |

---

## Part 1 — One-Time Setup

### Step 1 — Configure Git (first time only)

Open Terminal (Mac/Linux) or Git Bash (Windows) and run:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

---

### Step 2 — Create a GitHub Repository

**Option A — Via GitHub website:**
1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `tor-checklist-gdcc`
   - **Description:** `TOR Checklist — GDCC Open Data FY2569`
   - **Visibility:** `Private` ← recommended for procurement docs
   - ❌ Do NOT tick "Add a README" (we already have one)
3. Click **"Create repository"**
4. Copy the URL shown (e.g. `https://github.com/your-org/tor-checklist-gdcc.git`)

**Option B — Via GitHub CLI (faster):**
```bash
gh auth login          # one-time login
gh repo create tor-checklist-gdcc --private --description "TOR Checklist GDCC Open Data FY2569"
```

---

### Step 3 — Initialise the Local Repository

Navigate to the folder you downloaded/extracted this package into:

```bash
cd path/to/tor-checklist-gdcc    # adjust to your actual path

git init
git add .
git commit -m "feat: initial release v1.0.0 — TOR GDCC Open Data FY2569"
```

---

### Step 4 — Connect and Push to GitHub

```bash
# Replace the URL with the one you copied in Step 2
git remote add origin https://github.com/your-org/tor-checklist-gdcc.git

git branch -M main
git push -u origin main
```

---

### Step 5 — Tag the First Release

```bash
git tag -a v1.0.0 -m "Initial release — TOR GDCC Open Data FY2569"
git push origin v1.0.0
```

✅ Your repo is now live at `https://github.com/your-org/tor-checklist-gdcc`

---

## Part 2 — Day-to-Day Workflow

### Updating a document

```bash
# 1. Pull latest changes first (always do this before editing)
git pull origin main

# 2. Edit the file(s) in docs/ as needed

# 3. Stage and commit
git add docs/TOR_Checklist_GDCC_OpenData.md
git commit -m "fix: correct penalty clause in item 9.1"

# 4. Push
git push origin main
```

---

### Making a bigger change (new version)

```bash
# 1. Create a branch
git checkout -b update/add-company-4

# 2. Make your edits

# 3. Update CHANGELOG.md — add an entry under [Unreleased]

# 4. Commit
git add .
git commit -m "feat: add บริษัท X as 4th company column"

# 5. Push the branch
git push origin update/add-company-4

# 6. Open a Pull Request on GitHub for review
#    (go to github.com → your repo → "Compare & pull request")
```

---

### Releasing a new version

After your PR is merged to `main`:

```bash
git checkout main
git pull origin main

# Tag the new version
git tag -a v1.1.0 -m "feat: added 4th company column"
git push origin v1.1.0
```

Then update `CHANGELOG.md`:
- Move items from `[Unreleased]` into a new `[v1.1.0] — YYYY-MM-DD` section

---

### Re-generating the Excel file

If you edit the checklist data and want to rebuild the `.xlsx`:

```bash
pip install openpyxl          # once only
python scripts/export_xlsx.py
git add docs/TOR_Checklist_GDCC_OpenData.xlsx
git commit -m "chore: regenerate Excel checklist"
git push origin main
```

---

## Part 3 — Invite Collaborators

### Add team members to the private repo

1. Go to `https://github.com/your-org/tor-checklist-gdcc/settings/access`
2. Click **"Add people"**
3. Enter their GitHub username or email
4. Set role:
   - **Write** — can push commits directly
   - **Triage** — can open/close issues only
   - **Read** — view-only access

---

## Part 4 — Useful GitHub Features for This Use Case

### Protected `main` branch (recommended)
Prevents accidental direct pushes. All changes go through Pull Requests.

1. Go to **Settings → Branches → Add rule**
2. Branch name pattern: `main`
3. Enable:
   - ✅ Require a pull request before merging
   - ✅ Require approvals (set to 1)
   - ✅ Do not allow bypassing the above settings

---

### GitHub Releases (for major versions)
1. Go to **Releases → Draft a new release**
2. Choose your version tag (e.g. `v1.1.0`)
3. Attach the `.xlsx` and `.md` files as release assets
4. Publish — stakeholders can download pinned versions directly

---

### Issues (for tracking change requests)
Use GitHub Issues to log:
- Requested edits from NT or companies
- Questions about specific TOR clauses
- Discrepancies found during review

Label examples: `correction`, `new-company`, `question`, `v2-scope`

---

## Part 5 — Clone on Another Machine

Anyone with access can clone and work locally:

```bash
git clone https://github.com/your-org/tor-checklist-gdcc.git
cd tor-checklist-gdcc
```

---

## Quick Reference

| Action | Command |
|--------|---------|
| Pull latest | `git pull origin main` |
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push | `git push origin main` |
| New branch | `git checkout -b branch-name` |
| See history | `git log --oneline` |
| See what changed | `git diff` |
| List tags | `git tag` |
| Create tag | `git tag -a vX.Y.Z -m "message"` |
| Push tag | `git push origin vX.Y.Z` |

---

*For issues or questions, open a GitHub Issue in the repository.*
