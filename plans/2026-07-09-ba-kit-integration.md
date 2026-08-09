# BA-Kit Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the AI-BA-Kit *upstream analysis layer* (requirement analysis, context finding, open questions, impact, risk) plus a *persistent knowledge base* into the RC_QA_Knowledge vault, feeding the existing `/gen-ac → /gen-tc` pipeline — without changing the AC/TC format, criticality scheme, traceability, Jira/Figma integration, or MkDocs publishing.

**Architecture:** RC_QA_Knowledge stays the host. We graft two things from AI-BA-Kit: (1) a durable knowledge base under `00_Project_Info/knowledge/` (feature catalog, shared business rules, data model, permission matrix, terminology, decision log) that acts as BA memory; (2) a new `/gen-analysis` step that runs *before* `/gen-ac`, writing a per-feature analysis file to `01_SRS/<feature>/analysis.md` and blocking on unanswered High-priority questions. `/gen-ac` is then wired to read the knowledge base + the analysis file so AC cite confirmed rules instead of re-inventing them. New pipeline: `Jira → /gen-analysis → /gen-ac → /gen-tc`.

**Tech Stack:** Obsidian markdown, Claude Code project skills (`.claude/skills/`) + slash commands (`.claude/commands/`), Atlassian Jira MCP, MkDocs Material (`make build` renders the site from symlinks built by `scripts/build-docs-tree.sh`).

## Global Constraints

- **English only** in every committed file (body, cell content, headers, Type/Criticality/Status values). The vault is shared on GitHub. (Chat replies to the user may be Vietnamese.)
- **Concise but unambiguous** — bullets and short bold-led lines over paragraphs; state observable outcomes explicitly, no vague words.
- **Templates in `04_Templates/` are the single source of truth** — skills read them each run, never hardcode a copy of the format.
- **Feature codes are immutable** once used in any ID (`00_Project_Info/features.md`). New feature ⇒ add a registry row first.
- **Criticality scale is fixed:** 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low (impact if it fails — NOT MoSCoW).
- **Never invent business rules.** Unconfirmed ⇒ raise as an Open Question, do not decide silently.
- **AC/TC format is unchanged** by this plan. AC stay high-level (the *what*, not the *how*); automation (Cucumber) owns step detail.
- **Do not touch `.obsidian/`.** Do not hand-edit `docs/` or `site/` — they are generated and git-ignored (`build-docs-tree.sh` runs `rm -rf docs`).
- **Verification build command:** `make build` (runs `scripts/build-docs-tree.sh` then `mkdocs build`). It must exit 0.

## New ID conventions (added by this plan)

| Artifact | ID format | Lives in |
| --- | --- | --- |
| Open question | `Q-<CODE>-NN` | `01_SRS/<feature>/analysis.md` |
| Risk | `RISK-<CODE>-NN` | `01_SRS/<feature>/analysis.md` |
| Shared business rule (cross-feature) | `BR-SHARED-NN` | `00_Project_Info/knowledge/business_rules.md` |
| Decision | `DEC-NN` | `00_Project_Info/knowledge/decision_log.md` |

Feature-specific business rules keep living in the AC file as `BR-<CODE>-NN` (unchanged). The knowledge base holds only **shared / cross-feature** rules.

## File map (created / modified)

```
00_Project_Info/
  features.md                          MODIFY  (add knowledge-base + analysis note)
  knowledge/                           CREATE  (durable BA memory)
    feature_catalog.md                 CREATE
    business_rules.md                  CREATE
    data_model.md                      CREATE
    permission_matrix.md               CREATE
    terminology.md                     CREATE
    decision_log.md                    CREATE
01_SRS/<feature>/analysis.md           (runtime output of /gen-analysis — not created by this plan)
04_Templates/
  ac_template.md                       MODIFY  (add "Analysis ref" header field)
  analysis_template.md                 CREATE
.claude/skills/
  gen-ac-from-jira/SKILL.md            MODIFY  (read knowledge base + analysis)
  gen-analysis-from-jira/
    SKILL.md                           CREATE
    references/analysis-techniques.md  CREATE
.claude/commands/
  gen-analysis.md                      CREATE
README.md                              MODIFY  (new workflow, folders, commands)
```

---

### Task 1: Persistent knowledge base

**Files:**
- Create: `00_Project_Info/knowledge/feature_catalog.md`
- Create: `00_Project_Info/knowledge/business_rules.md`
- Create: `00_Project_Info/knowledge/data_model.md`
- Create: `00_Project_Info/knowledge/permission_matrix.md`
- Create: `00_Project_Info/knowledge/terminology.md`
- Create: `00_Project_Info/knowledge/decision_log.md`
- Modify: `00_Project_Info/features.md`

**Interfaces:**
- Produces: six knowledge files at stable paths `00_Project_Info/knowledge/*.md`. `/gen-analysis` (Task 4) and `/gen-ac` (Task 6) read these by exact path. Shared-rule IDs `BR-SHARED-NN`; decision IDs `DEC-NN`.

- [ ] **Step 1: Create `00_Project_Info/knowledge/feature_catalog.md`**

```markdown
# Feature Catalog

> One section per feature — durable BA memory. `/gen-analysis` and `/gen-ac` search this first (Context step) and cross-check it during Impact analysis. A stale entry is worse than a missing one: it looks authoritative. Keep every field current. Feature slugs/codes are defined in [[features]] — this file describes them.

## Feature: login  (`LOGIN`)

- **Purpose:** Authenticate a registered user into Repair Check.
- **Main users:** Registered vehicle owner.
- **Main workflow:** Open Login → enter email + password → submit → session created → landing.
- **Business rules:** feature-local `BR-LOGIN-*` in `02_Acceptance_Criteria/login/login.md`; shared: [[business_rules]] `BR-SHARED-*`.
- **Related screens:** Login. See `01_SRS/login/figma/`.
- **Related data:** [[data_model]] → User, Session.
- **Known limitations:** [FILL IN]
- **Future enhancements:** [FILL IN]

---

## Feature: <slug>  (`<CODE>`)

- **Purpose:**
- **Main users:**
- **Main workflow:**
- **Business rules:**
- **Related screens:**
- **Related data:**
- **Known limitations:**
- **Future enhancements:**

---
(Duplicate the block above — one feature per section. Every feature in [[features]] should eventually have an entry.)
```

- [ ] **Step 2: Create `00_Project_Info/knowledge/business_rules.md`**

```markdown
# Business Rules (shared)

> Single source of truth for **cross-feature** rules the business requires (security, session, data retention, org-wide policy). Feature-specific rules stay in that feature's AC file as `BR-<CODE>-NN`. Every rule here must cite a source — an unsourced rule belongs in an Open Question, not this table.

| ID | Rule | Rationale | Source | Criticality | Applies to | Status |
| --- | --- | --- | --- | --- | --- | --- |
| BR-SHARED-01 | <e.g. "Session expires after 15 min idle."> | <why> | <doc / stakeholder / DEC-NN> | 🔴 Critical | login, ... | Active |

## Conventions

- IDs are permanent — never reuse or renumber a retired rule; mark it `Deprecated`.
- **Status:** `Proposed` (raised in analysis, not yet confirmed) → `Active` (confirmed by a stakeholder; log the confirmation in [[decision_log]]) → `Deprecated`.
- If two rules conflict, do not delete either — flag both and record the resolution in [[decision_log]].
- **Criticality** uses the vault scale: 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low.
```

- [ ] **Step 3: Create `00_Project_Info/knowledge/data_model.md`**

```markdown
# Data Model

> Entity-level reference for DB impact analysis — not a full schema dump, just the fields and relationships that matter for business logic. `/gen-analysis` reads this for the "Affected DB" impact row.

## Entity: <Name>

- **Purpose:** <what it represents>
- **Key fields:** <field — type — meaning; mark PII / sensitive fields>
- **Relationships:** <to other entities, cardinality>
- **Related feature:** [[feature_catalog]]
- **Notes:** <soft-delete vs hard-delete, audit fields, etc.>

---
(Duplicate per entity.)

## ER Diagram

[Link to or embed the entity-relationship diagram.]
```

- [ ] **Step 4: Create `00_Project_Info/knowledge/permission_matrix.md`**

```markdown
# Permission Matrix

> Who can do what. Checked on every impact analysis — a change that silently alters who can access a feature is one of the most common shipped bugs. `/gen-analysis` reads this for the "Affected Permissions" impact row.

| Role | Feature / Action | Allowed? | Conditions | Notes |
| --- | --- | --- | --- | --- |
| <role> | <action> | Yes / No | <e.g. "own records only"> | |

## Conventions

- A new feature must add rows here before it is marked ready for AC — "who can do this" is a requirement, not an afterthought.
- If permissions differ by data ownership, tenant, or plan tier, state that in **Conditions** explicitly.
```

- [ ] **Step 5: Create `00_Project_Info/knowledge/terminology.md`**

```markdown
# Terminology

> Shared vocabulary. If two people (or a person and Claude) mean different things by one word, fix it here once. Generated docs (AC, TC, analysis) must prefer the term defined here.

| Term | Definition | Also known as | Notes |
| --- | --- | --- | --- |
| <term> | <definition> | <synonyms> | <context> |

## Conventions

- If a term is ambiguous in real usage, document both meanings and which context each applies to — never pick one silently.
```

- [ ] **Step 6: Create `00_Project_Info/knowledge/decision_log.md`**

```markdown
# Decision Log

> Every non-trivial decision — especially one that resolved a conflict flagged during analysis — is logged here permanently. Never edit a past entry's outcome; add a new entry that supersedes it and link back.

| ID | Date | Decision | Context | Alternatives considered | Rationale | Owner | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-01 | <YYYY-MM-DD> | <decision> | <what prompted it> | <what else was considered> | <why this won> | <name> | Active |

## Conventions

- Superseded decisions stay in the table marked `Superseded`, with a pointer to the ID that replaced them — never delete history.
- Any conflict surfaced by analysis that gets a human ruling belongs here, even if it feels minor.
```

- [ ] **Step 7: Add a knowledge-base + analysis note to `00_Project_Info/features.md`**

In `00_Project_Info/features.md`, after the `## Rules` section, append:

```markdown

## Knowledge base & analysis

- **`knowledge/`** — durable BA memory shared across features: [[knowledge/feature_catalog]], [[knowledge/business_rules]] (`BR-SHARED-NN`), [[knowledge/data_model]], [[knowledge/permission_matrix]], [[knowledge/terminology]], [[knowledge/decision_log]] (`DEC-NN`). `/gen-analysis` and `/gen-ac` read these; after AC review, promote confirmed rules/decisions into them.
- **`01_SRS/<slug>/analysis.md`** — per-feature BA analysis (requirement, context, open questions `Q-<CODE>-NN`, impact, risk `RISK-<CODE>-NN`) produced by `/gen-analysis`, accumulating per ticket.
```

- [ ] **Step 8: Verify the build renders the new folder**

Run: `make build`
Expected: exits 0; output lists `docs/00_Project_Info` symlink. Confirm the six files are picked up:
Run: `ls site/00_Project_Info/knowledge/`
Expected: six directories/pages (`business_rules/`, `data_model/`, `decision_log/`, `feature_catalog/`, `permission_matrix/`, `terminology/`).

- [ ] **Step 9: Commit**

```bash
git add 00_Project_Info/knowledge 00_Project_Info/features.md
git commit -m "feat(ba): add persistent knowledge base (feature catalog, shared rules, data model, permissions, terminology, decision log)"
```

---

### Task 2: Analysis-techniques reference

**Files:**
- Create: `.claude/skills/gen-analysis-from-jira/references/analysis-techniques.md`

**Interfaces:**
- Produces: the methodology doc the `gen-analysis` skill (Task 4) reads each run — mirrors how `gen-ac-from-jira` reads `references/ac-techniques.md`. Defines the five analysis steps and their guardrails.

- [ ] **Step 1: Create the reference file**

```markdown
# Requirement-analysis techniques (BA upstream)

How a senior BA analyses a Jira ticket *before* writing AC. Apply every step that fits; the output is written to `01_SRS/<feature>/analysis.md`. Core posture: **facts** (cited) vs **assumptions** (flagged) vs **recommendations** (labeled opinion) — never blur them, and never invent a business rule to fill silence.

## 1. Requirement analysis

- Restate the requirement in precise language — resolve pronouns, vague roles ("the user" → which role?), implicit scope.
- Identify the **underlying business problem**, not just the literal ask.
- Classify: New feature / Change / Bug-as-requirement / Process change.
- Identify **requester** vs **beneficiary** (not always the same).
- If the ticket bundles two or more requirements, split them and say so.
- Do NOT resolve ambiguity by guessing — record it as an open question (§3).

## 2. Context finding (search project memory first)

Search, in order, and record every relevant hit:

1. `01_SRS/<feature>/` (existing requirements, Figma) and other features' SRS.
2. `00_Project_Info/knowledge/feature_catalog.md`, then `business_rules.md`, then `decision_log.md`, then the rest of `knowledge/`.
3. Existing `02_Acceptance_Criteria/` and `03_Testcases/` for the same or adjacent features.
4. Jira (via MCP) for linked/related tickets.

- Judge relevance — list what informs *this* requirement, not everything that keyword-matched.
- "No related knowledge found" is a valid, important output. If a source turns up nothing, say so explicitly rather than omitting it.
- Score your own confidence (Low / Medium / High) and list **Missing Information** you would expect to exist but could not find.

## 3. Open questions

- Convert every gap/ambiguity into a **specific, answerable** question — not "what about edge cases?" but "if a user has two vehicles with the same plate, which one is primary?".
- **Prioritise** by design impact: a question whose answer changes the design is High; cosmetic is Low. Use the vault criticality feel: High/Medium/Low.
- Group related questions so a stakeholder isn't re-reading context five times.
- Offer a **suggested** default where you have a defensible one — clearly labeled as a suggestion, never as the answer.
- **BLOCKING:** a High-priority question that is unanswered blocks AC generation. Do not guess forward.

## 4. Impact analysis

Trace the change across every category below. For each, state the impact or explicitly write "No impact identified" (with a one-line why for anything non-obvious) — never skip a category silently. Cross-check every affected item against `00_Project_Info/knowledge/` before listing it.

| Category | Where to check |
| --- | --- |
| Affected features | `knowledge/feature_catalog.md` |
| Affected UI | screens / components (Figma) |
| Affected APIs | endpoints new/changed/deprecated |
| Affected DB | `knowledge/data_model.md` — new fields, tables, migrations |
| Affected permissions | `knowledge/permission_matrix.md` |
| Affected notifications | emails, push, in-app alerts |
| Affected reports / dashboards | data/logic changes |
| Migration needs | backfill, one-time scripts |
| Backward compatibility | breaking vs non-breaking; who depends on current behaviour |

## 5. Risk analysis

- Assess risk across: Technical / Business / Data / Timeline / Adoption.
- For each risk state **Likelihood** (Low/Med/High) and **Impact** (Low/Med/High), plus a mitigation.
- **Data risk** (loss, corruption, PII exposure) and **backward-compatibility risk** must be actively checked even if the ticket doesn't mention data — never silently omit them.
- Don't inflate risk to seem thorough — an unjustified "High" is as unhelpful as a missed one.
- End with an **Overall Risk Level** (Low/Medium/High) + one-line justification.

## 6. Hand-off to /gen-ac

The analysis is BA working material that justifies the AC. When `/gen-ac` runs it:
- reuses the confirmed business rules (cite `BR-SHARED-NN` / `DEC-NN`, don't re-invent),
- inherits the impact/permission findings into scenario coverage,
- carries any still-open High question into the AC "open questions" report.

## 7. Final gate before hand-off

- [ ] Requirement restated unambiguously; bundled requirements split (§1)
- [ ] Context searched in all sources; confidence + missing-info stated (§2)
- [ ] Every gap is a specific, answerable question with a priority (§3)
- [ ] No High-priority question left silently unanswered (§3)
- [ ] All 9 impact categories addressed (impact or "none identified") (§4)
- [ ] Data and backward-compatibility risk explicitly checked (§5)
- [ ] Facts cited, assumptions flagged, no invented business rule (posture)
```

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/gen-analysis-from-jira/references/analysis-techniques.md
git commit -m "feat(ba): add requirement-analysis techniques reference"
```

---

### Task 3: Analysis template

**Files:**
- Create: `04_Templates/analysis_template.md`

**Interfaces:**
- Consumes: ID conventions from the Global Constraints section (`Q-<CODE>-NN`, `RISK-<CODE>-NN`), criticality scale.
- Produces: the single-source-of-truth format for `01_SRS/<feature>/analysis.md`. The `gen-analysis` skill (Task 4) reads this file each run.

- [ ] **Step 1: Create the template**

````markdown
# Requirement Analysis — Template

BA upstream analysis for a feature, produced by `/gen-analysis` **before** `/gen-ac`. **One analysis file per feature** at `01_SRS/<feature>/analysis.md`, accumulating one block per Jira ticket. It records *why* the AC look the way they do: the restated requirement, what context existed, what is still unknown (open questions), what this change impacts, and what could go wrong.

- `<CODE>` is the feature's short code from [[features]]. `NN` is zero-padded and **continuous within the feature** across all its tickets.
- Replace every `<...>` placeholder. Keep it concise — bullets and short cells, not prose.
- Criticality / priority use the vault scale: 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low.

---

## Analysis header

```markdown
# Requirement Analysis — <Feature name>

| Field            | Value                                    |
| ---------------- | ---------------------------------------- |
| **Version**      | 1.0                                      |
| **Last updated** | <YYYY-MM-DD>                             |
| **Feature**      | <feature name>                           |
| **SRS ref**      | [[01_SRS/<feature>/epic]]                |
| **Jira tickets** | `RC-4`, `RC-12` (tickets covered so far) |
| **BA Owner**     | <BA name>                                |
| **Status**       | Draft                                    |
```

## Per-ticket block

> Repeat this whole block once per Jira ticket. Head it with the ticket key.

### `<KEY>` — <short title>

**1. Requirement**

- **Restated:** <clear, unambiguous version>
- **Underlying problem:** <the business problem this solves>
- **Type:** New feature / Change / Bug-as-requirement / Process change
- **Requester:** <who> — **Beneficiary:** <who benefits, if different>

**2. Context found**

| Source | Ref | Summary |
| --- | --- | --- |
| feature_catalog / business_rules / decision_log / data_model / SRS / Jira / ... | <file, ID, or ticket key> | <what it says + why it matters here> |

- **Confidence:** Low / Medium / High — <one line>
- **Missing information:** <what you'd expect to exist but couldn't find, or "none">

**3. Open questions**

| Q ID | Question | Details | Priority | Suggestion | Status |
| --- | --- | --- | --- | --- | --- |
| Q-<CODE>-01 | <specific, answerable question> | <context> | 🟠 High | <suggested default, labeled as suggestion> | Open |

> A 🔴/🟠 question with Status `Open` **blocks** `/gen-ac`. Resolve or explicitly accept it before writing AC.

**4. Impact analysis**

| Category | Impact |
| --- | --- |
| Affected features | <from feature_catalog, or "none identified"> |
| Affected UI | <screens / components> |
| Affected APIs | <new / changed / deprecated> |
| Affected DB | <from data_model — fields, tables, migrations> |
| Affected permissions | <from permission_matrix> |
| Affected notifications | <emails / push / in-app> |
| Affected reports / dashboards | <data or logic changes> |
| Migration needs | <backfill / one-time scripts> |
| Backward compatibility | <breaking vs non-breaking; who depends on current behaviour> |

**5. Risk analysis**

| Risk ID | Risk | Category | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- | --- | --- |
| RISK-<CODE>-01 | <description> | Technical / Business / Data / Timeline / Adoption | Low/Med/High | Low/Med/High | <mitigation> |

- **Overall risk level:** Low / Medium / High — <one-line justification>

---

## Column & value guide

| Field | Meaning | Values |
| --- | --- | --- |
| **Q ID / Risk ID** | Continuous within the feature | `Q-<CODE>-NN`, `RISK-<CODE>-NN` |
| **Priority / Criticality** | Impact if unresolved / if it fails | 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low |
| **Question Status** | Resolution state | Open / Answered / Accepted-as-assumption |
| **Confidence** | Completeness of the context search | Low / Medium / High |

## Flow

```
Jira ticket ──▶ analysis.md (this file) ──▶ AC-<CODE>-NN ──▶ TC-<CODE>-NNN
 (the why)        (understand + de-risk)      (the what)        (the how)
```

- Confirmed business rules found/raised here are promoted to [[knowledge/business_rules]]; resolved conflicts to [[knowledge/decision_log]] (after review).
- `/gen-ac` reads this file if present and cites its confirmed rules instead of re-inventing them.
````

- [ ] **Step 2: Verify the build renders the template**

Run: `make build`
Expected: exits 0; `ls site/04_Templates/` includes `analysis_template/`.

- [ ] **Step 3: Commit**

```bash
git add 04_Templates/analysis_template.md
git commit -m "feat(ba): add per-feature analysis template"
```

---

### Task 4: `gen-analysis-from-jira` skill

**Files:**
- Create: `.claude/skills/gen-analysis-from-jira/SKILL.md`

**Interfaces:**
- Consumes: `00_Project_Info/features.md` (feature code), `00_Project_Info/knowledge/*` (Task 1), `04_Templates/analysis_template.md` (Task 3), `references/analysis-techniques.md` (Task 2), Jira MCP.
- Produces: `01_SRS/<feature>/analysis.md`. Downstream `/gen-ac` (Task 6) reads it. Skill `name` must be exactly `gen-analysis-from-jira` (the command in Task 5 invokes it by this name).

- [ ] **Step 1: Create the skill file**

```markdown
---
name: gen-analysis-from-jira
description: Use when analysing a Jira ticket as a senior BA before writing acceptance criteria. Fetches the ticket via the Atlassian (Jira) MCP, searches the project knowledge base, and produces a per-feature analysis (restated requirement, context found, prioritised open questions, impact across 9 categories, and risk) appended to 01_SRS/<feature>/analysis.md. Blocks AC generation on unanswered High-priority questions.
---

# Analyse a Jira Requirement (BA upstream)

Act as a **senior Business Analyst**. Turn a Jira ticket into a structured, de-risked analysis **before** acceptance criteria are written — restated requirement, context from project memory, prioritised open questions, impact, and risk — written **per feature** (`01_SRS/<feature>/analysis.md`) so `/gen-ac` and stakeholders build AC on solid ground.

**Posture (non-negotiable):** distinguish **facts** (cited) from **assumptions** (flagged) from **recommendations** (labeled opinion). Never invent a business rule to fill silence — raise it as an open question. Say "not documented" as a first-class answer.

## Inputs

- **Feature slug** — e.g. `login` (same slugs as `01_SRS/`). Sets the file `01_SRS/<feature>/analysis.md`.
- **Feature code** — the ID prefix (e.g. `LOGIN`), resolved from `00_Project_Info/features.md`, never invented. See step 1.
- **Jira key** — e.g. `RC-4` (extracted from a key or URL).
- **Vault path** — always the current working directory (`.`). This skill is project-scoped; all paths below are relative. Never hardcode an absolute path.
- **Figma screenshots** _(optional)_ — a folder path passed as the 3rd argument (e.g. `01_SRS/<feature>/figma`); read every image (`.png`/`.jpg`/`.jpeg`/`.webp`) to ground UI impact. Do NOT fetch Figma automatically.

## Prerequisite check (do this first)

Confirm the Atlassian Jira MCP is connected (a tool like `getJiraIssue` / `searchJiraIssuesUsingJql`). If missing, STOP and tell the user:

```
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp/authv2
```

Then run `/mcp` and authenticate. Never invent ticket contents if the MCP is missing.

## Process

Create a todo per step and work through them in order. Apply `references/analysis-techniques.md` throughout.

### 1. Resolve the feature code

Read `00_Project_Info/features.md` and find the row for the slug; use its **Code** as `<CODE>`. If the slug is not listed, STOP and ask the user for a short code (2–6 uppercase letters), add a registry row, then continue. Never invent a code silently.

### 2. Fetch the ticket

Read the issue by key via the MCP. Capture: summary, full description, issue type, status, labels/components, any existing AC, and clarifying comments. **If it is an Epic** (or has children), fetch all children (`searchJiraIssuesUsingJql`, JQL `parent = <KEY>`, include `description` and `comment`) and analyse the ones relevant to this feature; trace each finding to the **specific child ticket**.

### 3. Requirement analysis

Apply `references/analysis-techniques.md` §1: restate precisely, name the underlying problem, classify the type, identify requester vs beneficiary, split bundled requirements. If a Figma folder was passed, **Read every image** to ground UI impact; never fabricate UI you haven't seen.

### 4. Context finding

Apply §2: search `01_SRS/`, then `00_Project_Info/knowledge/` (feature_catalog → business_rules → decision_log → rest), then existing `02_Acceptance_Criteria/`/`03_Testcases/`, then related Jira tickets. Record relevant hits, a confidence score, and missing information. "No related knowledge found" is a valid output — state it, don't stretch a weak match.

### 5. Impact analysis

Apply §4: address all 9 categories (impact or "No impact identified" with a one-line why). Cross-check every affected item against `00_Project_Info/knowledge/`.

### 6. Open questions (blocking gate)

Apply §3: turn every gap/ambiguity into a specific, answerable question; assign a priority (🔴/🟠/🟡/⚪); offer a labeled suggestion where defensible. **Any 🔴/🟠 question with Status `Open` blocks `/gen-ac`** — call these out clearly at the end so the user resolves them with stakeholders first.

### 7. Risk analysis

Apply §5: Technical/Business/Data/Timeline/Adoption; likelihood × impact + mitigation per risk; explicitly check data-loss/PII and backward-compatibility risk; end with an Overall Risk Level.

### 8. Write / append the analysis file

Target: `01_SRS/<feature>/analysis.md`, using `04_Templates/analysis_template.md` (single source of truth — read it each run). Use `mkdir -p`.

- **If the file does not exist**, create it: header + one per-ticket block.
- **If it exists**, **append** a new per-ticket block headed by this `<KEY>`; continue `Q-<CODE>-NN` / `RISK-<CODE>-NN` numbering (never renumber); add this `<KEY>` to the header's "Jira tickets" list.

### 9. Self-check & report

Run the final gate in `references/analysis-techniques.md` §7 and fix any miss. Then report: counts (context hits, open questions by priority, impacts flagged, risks by level), and a **Blocking** line listing every unresolved 🔴/🟠 question. Remind the user: resolve blockers, then run `/gen-ac <feature> <KEY>`.

## Handling collisions

The per-feature file grows, so default for an existing file is **append**. Never renumber. If this `<KEY>` block already exists, ask the user: replace it, add anyway, or abort.

## Output conventions

- One feature = one analysis file (`01_SRS/<feature>/analysis.md`), accumulating one block per ticket.
- IDs are feature-based and continuous: `Q-<CODE>-NN`, `RISK-<CODE>-NN`.
- Format lives in `04_Templates/analysis_template.md` — read it each run, do not hardcode a copy.
- Flow `Jira → analysis → AC → TC`: this skill produces the analysis layer; `/gen-ac` consumes it.
- Write all content in English. Never modify `.obsidian/`.
```

- [ ] **Step 2: Verify the skill front-matter parses**

Run: `head -5 .claude/skills/gen-analysis-from-jira/SKILL.md`
Expected: shows `---`, `name: gen-analysis-from-jira`, a `description:` line, `---`.

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/gen-analysis-from-jira/SKILL.md
git commit -m "feat(ba): add gen-analysis-from-jira skill (upstream BA analysis)"
```

---

### Task 5: `/gen-analysis` command

**Files:**
- Create: `.claude/commands/gen-analysis.md`

**Interfaces:**
- Consumes: invokes the `gen-analysis-from-jira` skill (Task 4) by exact name.
- Produces: the `/gen-analysis <feature> <JIRA-KEY> [figma-folder]` slash command.

- [ ] **Step 1: Create the command file**

```markdown
---
description: Analyse a Jira ticket as a senior BA (requirement, context, open questions, impact, risk) before writing AC
argument-hint: <feature> <JIRA-KEY or link> [figma-folder]
---

The user wants a senior-BA analysis of a Jira ticket, produced **before** acceptance criteria.

Input given: **$ARGUMENTS**

- The **first argument** is the **feature slug** (e.g. `login`) — same slugs as `01_SRS/`. It sets the analysis file `01_SRS/<feature>/analysis.md`. The skill resolves the short code (e.g. `LOGIN`) from `00_Project_Info/features.md`.
- The **second argument** is a Jira issue key (e.g. `RC-4`) or a full Jira URL — extract the key.
- The **third argument** (optional) is a **folder of Figma screenshots** (e.g. `01_SRS/login/figma`). If given, the skill reads every image to ground UI impact; otherwise the analysis is derived from the ticket alone.
- **Vault path** is always the current working directory (`.`). All output paths are relative. Never hardcode an absolute path.

If the feature slug is missing, ask the user for it before proceeding (do not guess).

Now invoke the **gen-analysis-from-jira** skill and follow it exactly. Pass it the feature slug, the extracted Jira key, and the Figma folder (if provided).
```

- [ ] **Step 2: Commit**

```bash
git add .claude/commands/gen-analysis.md
git commit -m "feat(ba): add /gen-analysis command"
```

---

### Task 6: Wire the knowledge base + analysis into `/gen-ac`

**Files:**
- Modify: `.claude/skills/gen-ac-from-jira/SKILL.md`
- Modify: `04_Templates/ac_template.md`

**Interfaces:**
- Consumes: `00_Project_Info/knowledge/*` (Task 1), `01_SRS/<feature>/analysis.md` (runtime output of Task 4).
- Produces: `/gen-ac` behaviour that reads the knowledge base + analysis and an `Analysis ref` header field in AC files. AC ID/format otherwise unchanged.

- [ ] **Step 1: Add knowledge-base + analysis reading to `gen-ac` step 3**

In `.claude/skills/gen-ac-from-jira/SKILL.md`, find the `### 3. Analyse the requirement (BA work)` section. Replace its **first sentence** —

```
Apply `references/ac-techniques.md` §1: identify functional requirements, business rules, actors, preconditions, triggers, outputs, state changes, dependencies, impacted existing behaviour, and assumptions.
```

— with:

```
First, read the project memory: `00_Project_Info/knowledge/feature_catalog.md`, `business_rules.md`, `permission_matrix.md`, `data_model.md`, and `terminology.md`. If `01_SRS/<feature>/analysis.md` exists, read it too — reuse its confirmed impact, permissions, and business rules (cite shared rules by `BR-SHARED-NN` and decisions by `DEC-NN` instead of re-inventing them), and carry any still-open High-priority question (`Q-<CODE>-NN`) into your step-6 open-questions report. Then apply `references/ac-techniques.md` §1: identify functional requirements, business rules, actors, preconditions, triggers, outputs, state changes, dependencies, impacted existing behaviour, and assumptions.
```

- [ ] **Step 2: Add the `Analysis ref` step to `gen-ac` step 5**

In the same file, in `### 5. Write / append the AC spec`, find the bullet:

```
- **If the file does not exist**, create it: header (Feature, SRS ref, Jira tickets, BA Owner), user story, GWT table, Business Rules table.
```

Replace it with:

```
- **If the file does not exist**, create it: header (Feature, SRS ref, **Analysis ref** = `[[01_SRS/<feature>/analysis]]` when that file exists, else `—`, Jira tickets, BA Owner), user story, GWT table, Business Rules table.
```

- [ ] **Step 3: Add the `Analysis ref` row to the AC template header**

In `04_Templates/ac_template.md`, in the `## AC Spec header` code block, add a row directly after the `**SRS ref**` row:

```
| **Analysis ref**       | [[01_SRS/<feature>/analysis]] (or `—` if none)         |
```

- [ ] **Step 4: Verify the build still succeeds and the wording landed**

Run: `make build`
Expected: exits 0.
Run: `grep -c "00_Project_Info/knowledge" .claude/skills/gen-ac-from-jira/SKILL.md`
Expected: `1` (or more).
Run: `grep -c "Analysis ref" 04_Templates/ac_template.md`
Expected: `1`.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/gen-ac-from-jira/SKILL.md 04_Templates/ac_template.md
git commit -m "feat(ba): gen-ac reads knowledge base + analysis; add Analysis ref to AC header"
```

---

### Task 7: Update README with the new pipeline

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: everything above (folder names, commands, ID conventions).
- Produces: README that documents the 3-step pipeline (`/gen-analysis → /gen-ac → /gen-tc`), the `knowledge/` folder, and the analysis file.

- [ ] **Step 1: Update the main-flow line**

In `README.md`, replace:

```
Main flow: **Jira ticket → AC (BA) → Test Cases (QA) → Bug (on failure)**.
```

with:

```
Main flow: **Jira ticket → Analysis (BA) → AC (BA) → Test Cases (QA) → Bug (on failure)**.
```

- [ ] **Step 2: Add the knowledge base + analysis to the folder-structure block**

In the `## 1. Folder structure` code block, insert after the `00_Project_Info/ ... features.md ...` line:

```
  knowledge/               # Durable BA memory: feature catalog, shared rules (BR-SHARED), data model, permissions, terminology, decisions
```

and insert after the `01_SRS/` line block, before `02_Acceptance_Criteria/`:

```
  <feature>/analysis.md    # Per-feature BA analysis (requirement, context, open questions, impact, risk)
```

- [ ] **Step 3: Add a Step-0 analysis stage to the workflow section**

In `## 3. Workflow`, insert a new subsection **before** `### Step 1 — (optional) Write Acceptance Criteria`:

```markdown
### Step 0 — (recommended) Analyse the ticket
Run this first for any **ambiguous / high-risk / cross-feature** ticket. It searches the knowledge base and surfaces open questions, impact, and risk before AC exist.

```
/gen-analysis <feature> <JIRA-KEY> [figma-folder]
```
Example: `/gen-analysis login RC-4` → creates/appends `01_SRS/login/analysis.md`. **Resolve any 🔴/🟠 open question before Step 1.**

```

- [ ] **Step 4: Add `/gen-analysis` to the commands table**

In `## 7. Commands & Skills`, add this row as the **first** data row of the table:

```
| `/gen-analysis <feature> <KEY>` | `gen-analysis-from-jira` | Analyse a ticket (context, questions, impact, risk) before AC |
```

- [ ] **Step 5: Verify the build renders the README/homepage**

Run: `make build`
Expected: exits 0 (the README is symlinked as `docs/index.md`).
Run: `grep -c "gen-analysis" README.md`
Expected: `3` (or more).

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "docs(ba): document the analysis stage, knowledge base, and /gen-analysis in README"
```

---

### Task 8: End-to-end verification

**Files:**
- None (verification only).

**Interfaces:**
- Consumes: everything above.

- [ ] **Step 1: Full clean build**

Run: `make clean && make build`
Expected: exits 0. No "file not found" / broken-symlink errors in output.

- [ ] **Step 2: Confirm all new artifacts are present**

Run:
```bash
ls 00_Project_Info/knowledge/ \
   04_Templates/analysis_template.md \
   .claude/skills/gen-analysis-from-jira/SKILL.md \
   .claude/skills/gen-analysis-from-jira/references/analysis-techniques.md \
   .claude/commands/gen-analysis.md
```
Expected: all six knowledge files + the four new skill/template/command paths list without error.

- [ ] **Step 3: Confirm skills are self-consistent (no hardcoded absolute paths, correct skill name)**

Run: `grep -rn "/Users/" .claude/skills/gen-analysis-from-jira/ .claude/commands/gen-analysis.md`
Expected: no output (no machine-specific absolute paths).
Run: `grep -n "name: gen-analysis-from-jira" .claude/skills/gen-analysis-from-jira/SKILL.md`
Expected: one match.

- [ ] **Step 4: Manual pipeline dry-run (requires Jira MCP connected)**

In Claude Code at the vault root, on a real ambiguous ticket:
```
/gen-analysis login <REAL-KEY> 01_SRS/login/figma
```
Expected: creates `01_SRS/login/analysis.md` with the header + all five sections filled, a prioritised open-questions table, and a **Blocking** line in the report. Then:
```
/gen-ac login <REAL-KEY> 01_SRS/login/figma
```
Expected: the AC file's header shows `Analysis ref → [[01_SRS/login/analysis]]`, and the run report references the analysis's open questions. (This step is manual — it needs the MCP and a live ticket; if unavailable, note it as untested rather than claiming it passed.)

- [ ] **Step 5: Final commit (if the dry-run produced sample files worth keeping, otherwise skip)**

```bash
git add -A
git commit -m "test(ba): verify analysis → AC pipeline end to end"
```

---

## Self-Review

- **Spec coverage:** knowledge base (Task 1), analysis methodology (Task 2), analysis format (Task 3), analysis skill (Task 4), command (Task 5), gen-ac wiring + criticality reuse (Task 6), docs (Task 7), verification (Task 8). Criticality scheme is reused from RC (Global Constraints); AC/TC format untouched (only an additive header field). ✓
- **Placeholder scan:** `<...>` tokens appear only inside *template files* (intended — they are fill-ins for runtime), never as plan-level TODOs. ✓
- **Type/name consistency:** skill name `gen-analysis-from-jira` is identical in Task 4 front-matter, Task 5 command, and Task 7 table. Paths `00_Project_Info/knowledge/`, `01_SRS/<feature>/analysis.md`, `04_Templates/analysis_template.md` are identical across tasks. ID formats `Q-<CODE>-NN` / `RISK-<CODE>-NN` / `BR-SHARED-NN` / `DEC-NN` match between Global Constraints, the reference (Task 2), the template (Task 3), and the skill (Task 4). ✓

## Out of scope (possible follow-ups)

- Porting the remaining AI-BA-Kit knowledge files (Product_Vision, Architecture, API_Catalog, Business_Process, UI_Guideline) — add only when a real need appears.
- A lighter workflow variant for trivial bugfix tickets, and a heavier one for cross-team epics.
- Promoting confirmed rules from AC review back into `knowledge/business_rules.md` automatically (currently a manual post-review step).
