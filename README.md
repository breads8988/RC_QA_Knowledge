# RC QA Knowledge

QA knowledge base for **RepairCheck (RC)** — requirements, acceptance criteria, and test cases stored as Obsidian markdown and generated from Jira tickets with Claude Code.

RepairCheck is a multi-tenant SaaS for car accident and damage assistance (German market), built by MotionsCloud and sold to insurance companies. Three groups use it: **drivers** (Web App + Android), **Client Admins** at each insurance company (Web Portal), and **MCS Admins** (SaaS Admin).

Main flow: **Jira ticket → AC (BA) → Test Cases (QA) → Bug (on failure)**.

### Two files to read before you write anything

| File | What it holds |
| ---- | ------------- |
| `00_Project_Info/conventions.md` | **All structural rules** — paths, slugs, the registry, IDs, linking, templates. Single source of truth. |
| `CLAUDE.md` | **The business** — what the product is, who the actors are, German domain vocabulary, the entity model. |

This README is orientation and setup only. It deliberately does not repeat the rules — when they lived in five files at once they drifted apart, which is what broke the vault the first time.

---

## 1. Folder structure

```
00_Project_Info/
  conventions.md                  # Structural rules — the canonical one
  features.md                     # Registry: slug → code → entity, grouped by domain
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
CLAUDE.md                         # Business context for the agent
.claude/                          # Skills + commands (active when Claude Code runs at the vault)
mkdocs.yml, Makefile, scripts/, .github/   # Docs website (see section 8)
```

The three pillars **mirror each other** — the same feature sits at the same relative path under each, and the note's file name equals its leaf folder name:

```
01_SRS/workshop/wa_workshop/wa_workshop.md
02_Acceptance_Criteria/workshop/wa_workshop/wa_workshop.md
03_Testcases/workshop/wa_workshop/wa_workshop.md
```

`wa_` = Web App (driver), `wp_` = Web Portal (Client Admin) — the prefix identifies the **actor**, so `wa_workshop` and `wp_workshop` are two different features, not two views of one. Full rules in `conventions.md` §1–§2.

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

Before working on a **new** feature, add a row: slug + code + entity, under the right `##` section (the section is what tells the skills the domain).

| Section         | Slug          | Code    | Entity              | Example ID     |
| --------------- | ------------- | ------- | ------------------- | -------------- |
| `## Standalone` | `login`       | `LOGIN` | `User`              | `TC-LOGIN-001` |
| `## Standalone` | `my_vehicle`  | `MV`    | `Vehicle`           | `TC-MV-001`    |
| `## Workshop`   | `wa_workshop` | `WS`    | `Workshop` `Voucher` | `TC-WS-001`   |
| `## Workshop`   | `wp_workshop` | `WPWS`  | `Workshop` `Voucher` | `TC-WPWS-001` |

⚠️ Once a code is used in an ID it **must not change** — it breaks traceability. If you run a command for a feature not in the table, the skill asks for the code, domain and entity, then adds the row for you.

The **Entity** column is how cross-feature impact is found: search the registry for an entity and you get every feature sharing those records — often in a *different* domain, so the hub will not show them. Rules for filling it: `conventions.md` §3–§4.

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

**All of them live in `00_Project_Info/conventions.md`** — read it there, not here. Section map:

| § | Covers |
| - | ------ |
| 1 | The three mirrored pillars; file name = leaf folder name |
| 2 | Slug rules and the `wa_` / `wp_` platform prefix |
| 3 | Feature registry: codes, code immutability, the Entity column |
| 4 | Finding impact across features |
| 5 | Traceability and the coverage rule |
| 6 | Linking discipline — one hop per level; never link to a folder |
| 7 | Templates |
| 8 | Writing rules (English, high-level TCs, never fabricate) |
| 9 | Generated folders — `docs/`, `site/` |

Two that bite most often, repeated here only as a warning: a feature is **1 file per pillar** and grows by appending (never renumber existing IDs), and **`docs/` + `site/` are generated** — edit the real folders at the repo root.

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
