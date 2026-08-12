---
name: gen-ac-from-jira
description: Use when writing acceptance criteria (AC) from a Jira ticket, acting as a senior BA. Fetches the ticket via the Atlassian (Jira) MCP, optionally takes UI screenshots, decomposes the requirement into BABOK-aligned AC — Given/When/Then scenarios plus business rules, each rated by criticality — and appends to a per-feature AC spec in the Obsidian QA vault, ready for test-case generation.
---

# Generate Acceptance Criteria from Jira

Act as a **senior Business Analyst**. Turn a Jira ticket into a clear, testable, BABOK-aligned acceptance-criteria spec (BABOK §10.1) — Given/When/Then scenarios + business rules — written **per feature** so the QA team derives test cases from it via `/gen-tc`.

## Vault layout (read this before writing any path)

The three pillars are **mirror images**. A feature occupies the same relative path under each:

```
01_SRS/<domain>/<slug>/<slug>.md               02_Acceptance_Criteria/<domain>/<slug>/<slug>.md
01_SRS/<domain>/<slug>/*.png  (screens)        03_Testcases/<domain>/<slug>/<slug>.md
01_SRS/<domain>/<slug>/figma/*.png
```

- **The file name always equals its leaf folder name.** Never `workshop/wa_workshop/workshop.md`.
- A feature with no domain drops the `<domain>/` level: `02_Acceptance_Criteria/login/login.md`.
- A slug under a shared domain carries a platform prefix: `wa_` (Web App) or `wp_` (Web Portal) — e.g. `workshop/wa_workshop`, `workshop/wp_workshop`. Never use a bare domain name as a slug; it is ambiguous between the two platforms.
- Domains in use: `accident`, `lawyer`, `voucher`, `workshop`. Everything else is standalone.

Resolve the real path from `00_Project_Info/features.md` (step 1) — do not guess it from the slug alone.

## Inputs

- **Feature slug** — e.g. `login` (standalone), `wa_workshop` (under the `workshop` domain). Must match a row in `00_Project_Info/features.md`. Passed explicitly in the command.
- **Feature code** — the short ID prefix (e.g. `UM`), resolved from the registry `00_Project_Info/features.md`, NOT invented ad hoc. See step 1.
- **Jira key** — e.g. `RC-4` (the command extracts this from a key or URL).
- **Vault path** — always the **current working directory** (`.`). This skill is project-scoped inside the vault's `.claude/`, so Claude Code runs at the vault root; all paths below are **relative** to it. Never hardcode a machine-specific absolute path (the vault is shared via GitHub — absolute paths break on teammates' machines).
- **Figma screenshots** _(optional)_ — a **folder path** passed as the 3rd argument (e.g. `01_SRS/workshop/wa_workshop/figma`); read every image in it (`.png` / `.jpg` / `.jpeg` / `.webp`) to ground UI-behaviour scenarios. If no folder is given, the user may paste screenshots instead. Do NOT fetch Figma automatically.

## Prerequisite check (do this first)

Confirm the Atlassian Jira MCP is connected (a tool like `getJiraIssue`, `jira_get_issue`, or an `atlassian`-namespaced tool). If missing, STOP and tell the user to set it up:

```
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp/authv2
```

Then run `/mcp` and authenticate (OAuth in browser). Do not invent ticket contents if the MCP is missing.

## Process

Create a todo per step and work through them in order.

### 1. Resolve the feature code AND its path

Read `00_Project_Info/features.md` and find the row for the feature slug.

- **Code** — use the row's **Code** as the ID prefix (`<CODE>`). Never invent a code silently, and never use a different code than the registry for a feature that already has one.
- **Path** — the section the row sits under gives the domain. A row under `## Workshop` means `<domain>` = `workshop`; a row under `## Standalone` has no domain. Build the target path from that, then **verify it against the disk** (`ls 01_SRS/<domain>/<slug>/`) before writing. If the folder does not exist, stop and ask — do not create a second home for a feature that already has one.

If the slug is not listed at all, STOP and ask the user for a short code (2–6 uppercase letters) and which domain it belongs to, add a new row to the correct section of the registry, then continue.

### 2. Fetch the ticket

Call the Jira MCP to read the issue by key. Capture: summary, full description, issue type, status, labels/components, any existing acceptance criteria in the ticket, and clarifying comments.

**If the issue is an Epic** (`issuetype.name` = Epic) or otherwise has child issues, fetch **all** children with `searchJiraIssuesUsingJql` (JQL `parent = <KEY>`, include the `description` and `comment` fields) and read each. An Epic usually has no detail of its own — the real requirements live in its children. Use the children **relevant to this feature** as the requirement sources, and trace each AC's **Jira** column to the **specific child ticket** it came from, not the Epic.

### 3. Analyse the requirement (BA work)

Apply `references/ac-techniques.md` §1: identify functional requirements, business rules, actors, preconditions, triggers, outputs, state changes, dependencies, impacted existing behaviour, and assumptions. Then restate as a **user story** (`As a <role>, I want <capability>, so that <benefit>`). This step drives most of the AC quality. If a Figma-screenshots folder was passed, list it and **Read every image file** to ground UI states; otherwise use any pasted screenshots. Never fabricate UI elements you have not seen.

### 4. Decompose into AC

Read `references/ac-techniques.md` and apply it. Produce two complementary forms:

- **Scenario-based (Given/When/Then)** — cover happy path first, then alternate flows, negative cases, rule/condition combinations, edge/boundary, and permission cases. One scenario = one outcome (atomic).
- **Business rules** — constraints, limits, formulas, policies, permissions that govern many scenarios.

Rate each AC/rule by **criticality** (🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low — impact if it fails, see `references/ac-techniques.md` §6), which maps 1:1 to the verifying TC's priority. Keep every AC testable, unambiguous, and free of implementation detail (the _what_, not the _how_).

### 5. Write / append the AC spec

Target file: the path resolved in step 1 — `02_Acceptance_Criteria/<domain>/<slug>/<slug>.md`, or `02_Acceptance_Criteria/<slug>/<slug>.md` when standalone. Use the format in `04_Templates/ac_template.md` (single source of truth — read it from the vault). Use `mkdir -p`.

The header's **SRS ref** must be a resolving wiki-link to the feature's SRS note: `[[01_SRS/<domain>/<slug>/<slug>]]`. Check the target file exists first — a link to a folder (trailing `/`) or to a note that was never written shows up as a dead grey node in Obsidian's graph.

- **If the file does not exist**, create it: header (Feature, SRS ref, Jira tickets, BA Owner), user story, GWT table, Business Rules table.
- **If it exists**, **append** this ticket's criteria — continue the feature's numbering (highest existing `AC-<CODE>-NN` / `BR-<CODE>-NN`), and add this `<KEY>` to the header's "Jira tickets" list.

AC IDs `AC-<CODE>-NN`, rule IDs `BR-<CODE>-NN`. Each row's **Jira** column links this ticket. Leave the `Linked TCs` column blank — `/gen-tc` fills it. New AC start at `Status: Draft`.

### 6. Self-check & report

Run the final gate in `references/ac-techniques.md` §9 and fix any miss before reporting. Then print a summary: AC added this run + feature total, by type and priority. Then, as a BA, list **open questions / ambiguities** the ticket left unresolved (anything you had to assume) so the user can confirm with stakeholders before TCs are written. Never silently invent business rules — flag assumptions explicitly.

## Handling collisions

The per-feature file is expected to grow, so default for an existing file is **append** (continue numbering). Never renumber existing AC. If this `<KEY>` was already added before, ask the user: replace that ticket's rows, add anyway, or abort.

## Output conventions

- One feature = one AC spec at the mirror path of its SRS folder, accumulating AC from all its tickets.
- **Linking discipline** — the AC spec links **up** to its own SRS note only. Do not link it to `00_Project_Info/features.md`, to a domain hub, or to a sibling feature's spec. Cross-feature references belong in prose using the other feature's `<CODE>`, not a wiki-link. This keeps Obsidian's graph a clean tree (`features → domain hub → feature → AC/TC`) instead of a hairball.
- IDs are feature-based: `AC-<CODE>-NN` / `BR-<CODE>-NN`, continuous within the feature.
- AC format lives in `04_Templates/ac_template.md` (user-managed) — read it each run, do not hardcode a copy.
- Traceability flow `Jira → AC → TC`: this skill produces the AC layer; `/gen-tc` consumes it.
- Write all content in English (the vault is shared on GitHub) — body text, cell content, headers, and Type/Priority/Status values.
- Never modify `.obsidian/` config.
