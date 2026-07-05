# RC QA Knowledge

QA knowledge base for the **Repair Check (RC)** project — requirements, acceptance criteria, and test cases stored as Obsidian markdown and generated from Jira tickets with Claude Code.

Main flow: **Jira ticket → AC (BA) → Test Cases (QA) → Bug (on failure)**.

---

## 1. Folder structure

```
00_Project_Info/
  features.md              # Registry: maps feature slug → code (LOGIN, UM, MV...)
01_SRS/
  <feature>/epic.md        # Requirements / SRS, grouped by feature
02_Acceptance_Criteria/
  <feature>.md             # BABOK-aligned AC (Given/When/Then + Business Rules)
03_Testcases/
  <feature>.md             # Test Case Register (tables, grouped by theme)
04_Templates/
  ac_template.md           # AC format
  testcases_template.md     # TC register format
  bug_template.md          # Bug report format (creates a Jira Bug)
.claude/                   # Skills + commands (active when Claude Code runs at the vault)
mkdocs.yml, Makefile, scripts/, .github/   # Docs website (see section 8)
```

A **feature** (e.g. `login`) accumulates multiple Jira tickets. Files are named by feature for readability; IDs use a short code for brevity.

---

## 2. Setup (once per person after cloning)

The repo files work out of the box — you only need to connect the **Jira MCP** (OAuth is per-account, cannot be shared):

```bash
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp/authv2
```

Then inside Claude Code:
```
/mcp   → select atlassian → Authenticate (log in to Atlassian in the browser)
```

> Open Claude Code **at the vault root** so the `/gen-ac` and `/gen-tc` commands appear. All paths are relative — nothing is machine-specific.

---

## 3. Workflow

### Step 1 — (optional) Write Acceptance Criteria
Only when the ticket is **ambiguous / high-risk / needs PO-Dev sign-off**. For clear, small tickets, skip this and go to Step 2.

```
/gen-ac <feature> <JIRA-KEY>
```
Example: `/gen-ac login RC-4` → generates `02_Acceptance_Criteria/login.md` (BA reviews and edits).

### Step 2 — Generate Test Cases
```
/gen-tc <feature> <JIRA-KEY>
```
Example: `/gen-tc login RC-4` → creates/appends to `03_Testcases/login.md`. The skill will:
- Read the AC if present (cover every AC); otherwise trace directly to Jira.
- **Ask you to paste Figma screenshots** of the relevant screens.
- Apply the full set of test-design techniques (happy / negative / boundary / EP / UI / error / edge).

### Step 3 — Report a Bug (when a test fails)
Copy `04_Templates/bug_template.md`, fill it in, then create a Jira issue of type **Bug** (fields map 1:1).

---

## 4. Feature Registry (`00_Project_Info/features.md`)

Before working on a **new** feature, add a row to the registry: slug (lowercase) + code (2–6 uppercase letters, unique).

| Feature (file) | Code | Example ID |
| --- | --- | --- |
| login | `LOGIN` | `TC-LOGIN-001` |
| my_vehicle | `MV` | `TC-MV-001` |
| user_management | `UM` | `TC-UM-001` |

⚠️ Once a code is used in an ID it **must not change** (it breaks traceability). If you run a command for a feature not in the table, the skill will ask for a code and add it.

---

## 5. Traceability

```
Jira ticket  →  AC-<CODE>-NN / BR-<CODE>-NN  →  TC-<CODE>-NNN
  (why)            (what — definition of done)     (how — verification)
```

- AC links down to TCs via the `Linked TCs` column; TCs link up via the `AC` column. Every row has a `Jira` column pointing to the source ticket.
- Coverage rule: every `Must` AC and every Business Rule must have ≥1 TC.

---

## 6. Conventions

- **1 feature = 1 file** for both AC and TC, accumulating multiple tickets (append, continue numbering, never renumber).
- **Templates are the single source of truth** in `04_Templates/` — skills read them on every run. To change a format, edit the template, not the files in `.claude/`.
- **Write everything in English** (the vault is shared on GitHub).
- Do not touch `.obsidian/`.

---

## 7. Commands & Skills

| Command | Skill | Purpose |
| --- | --- | --- |
| `/gen-ac <feature> <KEY>` | `gen-ac-from-jira` | Write BABOK-aligned AC from a Jira ticket |
| `/gen-tc <feature> <KEY>` | `gen-tcs-from-jira` | Generate the TC register from Jira + Figma |

Everything is project-scoped under `.claude/` — it travels with the repo, so anyone who clones it can use it.

---

## 8. View as a website (MkDocs Material)

A free, searchable web UI for these docs — a lightweight alternative to Confluence.
The markdown files are **not moved**: `scripts/build-docs-tree.sh` builds a `docs/`
folder of symlinks and MkDocs renders from there. Obsidian and the skills keep
working against the repo root.

**One-time setup** (needs Python 3):
```bash
make install
```

**Preview locally** (auto-reloads on edits):
```bash
make serve      # then open http://127.0.0.1:8000
```

**Publish to the web (GitHub Pages):**
- Automatic — pushing to `main` runs `.github/workflows/docs.yml` and deploys.
  One-time: on GitHub → **Settings → Pages → Build and deployment → Source = GitHub Actions**.
  The site appears at `https://breads8988.github.io/RC_QA_Knowledge/`.
- Manual — `make deploy` (builds and pushes to the `gh-pages` branch).

`docs/` and `site/` are generated and git-ignored — never edit them by hand;
edit the real folders at the repo root.
