# RC QA Knowledge

QA knowledge base for **RepairCheck (RC)** — requirements, acceptance criteria, and test cases stored as Obsidian markdown and generated from Jira tickets with Claude Code.

RepairCheck is a multi-tenant SaaS for car accident and damage assistance (German market), built by MotionsCloud and sold to insurance companies. Three groups use it: **drivers** (Web App + Android), **Client Admins** at each insurance company (Web Portal), and **MCS Admins** (SaaS Admin). Read `CLAUDE.md` for the business model, actors, and domain vocabulary — that context matters more than any format rule below.

Main flow: **Jira ticket → AC (BA) → Test Cases (QA) → Bug (on failure)**.

---

## 1. Folder structure

```
00_Project_Info/
  features.md                     # Registry: slug → code, grouped by domain
  system-high-level-design.md     # Architecture, actors, core entities
01_SRS/
  <domain>/<domain>.md            # Domain hub — lists that domain's sub-features
  <domain>/<slug>/<slug>.md       # Requirement note
  <domain>/<slug>/*.png           # Screens
  <domain>/<slug>/figma/*.png     # Figma exports
02_Acceptance_Criteria/
  <domain>/<slug>/<slug>.md       # BABOK-aligned AC (Given/When/Then + Business Rules)
03_Testcases/
  <domain>/<slug>/<slug>.md       # Test Case Register (tables, grouped by theme)
04_Templates/
  ac_template.md                  # AC format
  testcases_template.md           # TC register format
  bug_template.md                 # Bug report format (creates a Jira Bug)
CLAUDE.md                         # Business context + vault conventions
.claude/                          # Skills + commands (active when Claude Code runs at the vault)
mkdocs.yml, Makefile, scripts/, .github/   # Docs website (see section 8)
```

**The three pillars mirror each other** — a feature sits at the same relative path under `01_SRS/`, `02_Acceptance_Criteria/` and `03_Testcases/`, and the note's file name always equals its leaf folder name:

```
01_SRS/workshop/wa_workshop/wa_workshop.md
02_Acceptance_Criteria/workshop/wa_workshop/wa_workshop.md
03_Testcases/workshop/wa_workshop/wa_workshop.md
```

A feature that belongs to no domain drops the `<domain>/` level — `01_SRS/login/login.md`. Domains in use: `accident`, `lawyer`, `voucher`, `workshop`.

**The `wa_` / `wp_` prefix tells you the actor**, not just the app: `wa_` = Web App (driver), `wp_` = Web Portal (Client Admin). `wa_workshop` and `wp_workshop` are two different features — a driver searching for a garage vs. an admin editing the garage record. Never register a bare domain name (`workshop`) as a slug; it is ambiguous between the two.

A **feature** accumulates multiple Jira tickets. Files are named by slug for readability; IDs use a short code for brevity.

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
/gen-ac <slug> <JIRA-KEY> [figma-folder]
```
Examples:
- `/gen-ac login RC-4` → `02_Acceptance_Criteria/login/login.md` (standalone feature)
- `/gen-ac wa_workshop RC-36` → `02_Acceptance_Criteria/workshop/wa_workshop/wa_workshop.md` (under a domain)

The BA reviews and edits the result.

### Step 2 — Generate Test Cases
```
/gen-tc <slug> <JIRA-KEY> [figma-folder]
```
Example: `/gen-tc wa_workshop RC-36 01_SRS/workshop/wa_workshop/figma` → creates/appends to `03_Testcases/workshop/wa_workshop/wa_workshop.md`. The skill will:
- Read the AC if present (cover every AC); otherwise trace directly to Jira.
- **Ask you to paste Figma screenshots** of the relevant screens.
- Apply the full set of test-design techniques (happy / negative / boundary / EP / UI / error / edge).

### Step 3 — Report a Bug (when a test fails)
Copy `04_Templates/bug_template.md`, fill it in, then create a Jira issue of type **Bug** (fields map 1:1).

---

## 4. Feature Registry (`00_Project_Info/features.md`)

Before working on a **new** feature, add a row to the registry: slug (lowercase, matching the leaf folder name) + code (2–6 uppercase letters, unique across the whole registry). Put the row under the right `##` section — that section is what tells the skills which domain the feature belongs to.

| Section          | Slug          | Code   | Example ID       |
| ---------------- | ------------- | ------ | ---------------- |
| `## Standalone`  | `login`       | `LOGIN` | `TC-LOGIN-001`  |
| `## Standalone`  | `my_vehicle`  | `MV`    | `TC-MV-001`     |
| `## Workshop`    | `wa_workshop` | `WS`    | `TC-WS-001`     |
| `## Workshop`    | `wp_workshop` | `WPWS`  | `TC-WPWS-001`   |

⚠️ Once a code is used in an ID it **must not change** (it breaks traceability). If you run a command for a feature not in the table, the skill will ask for a code and which domain it belongs to, then add it.

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
- **Write everything in English** (the vault is shared on GitHub). German product terms stay German where the UI uses them; gloss them on first use.
- **Linking — one hop per level.** The graph reads `features.md → domain hub → feature SRS note → its AC/TC`. `features.md` links only to hubs and standalone features; an AC/TC note links only up to its own SRS note. Cross-feature references go in prose using the other feature's code, not a wiki-link.
- **Never link to a folder.** `[[01_SRS/accident/wa_my_accident/]]` with a trailing slash does not resolve — Obsidian links point at notes, not folders, so it renders as a dead grey node. Link the note: `[[01_SRS/accident/wa_my_accident/wa_my_accident]]`.
- Test cases stay **high-level** — one scenario, 3–5 steps, no click-by-click. The Cucumber layer writes the detailed steps.
- Do not touch `.obsidian/`.

---

## 7. Commands & Skills

| Command | Skill | Purpose |
| --- | --- | --- |
| `/gen-ac <slug> <KEY> [figma]` | `gen-ac-from-jira` | Write BABOK-aligned AC from a Jira ticket |
| `/gen-tc <slug> <KEY> [figma]` | `gen-tcs-from-jira` | Generate the TC register from Jira + Figma |

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
