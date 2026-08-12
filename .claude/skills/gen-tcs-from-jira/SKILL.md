---
name: gen-tcs-from-jira
description: Use when generating test cases (TCs) from a Jira ticket plus Figma screenshots. Fetches the ticket via the Atlassian (Jira) MCP, reads the feature's acceptance-criteria spec if present, reads UI screenshots from a folder (3rd arg) or pasted by the user, applies full test-design techniques, and appends to a per-feature Test Case Register (grouped markdown tables) in an Obsidian QA vault, with every TC traced to the AC it verifies and the Jira ticket.
---

# Generate Test Cases from Jira + Figma

Turn a Jira ticket and its Figma UI into a complete, traceable Test Case Register written as Obsidian markdown — **one register file per feature**, grouped tables, every TC linked to the AC it verifies and to its Jira ticket.

## Read the conventions first

**Read `00_Project_Info/conventions.md` before writing any path, ID, or link.** It is the single source of truth for the vault's structure — the three mirrored pillars, slug and `wa_`/`wp_` prefix rules, the registry and its Entity column, how impact is found, and the linking discipline. This skill does not restate those rules; if it ever appears to contradict that file, that file wins.

Also read `CLAUDE.md` for the business layer — the actors behind `wa_`/`wp_`, the German domain vocabulary, and the entity model. A `wa_` feature and its `wp_` twin have different actors and different failure modes, so the same screen name does not mean the same test.

## Inputs

- **Feature slug** — e.g. `login` (standalone), `wa_workshop` (under the `workshop` domain). Must match a row in `00_Project_Info/features.md`. Passed explicitly in the command.
- **Feature code** — the short ID prefix (e.g. `UM`), resolved from the registry `00_Project_Info/features.md`, NOT invented ad hoc. See step 1.
- **Jira key** — e.g. `RC-4` (the command extracts this from a key or URL).
- **Vault path** — always the **current working directory** (`.`). This skill is project-scoped inside the vault's `.claude/`, so Claude Code runs at the vault root; all paths below are **relative** to it. Never hardcode a machine-specific absolute path (the vault is shared via GitHub — absolute paths break on teammates' machines).
- **Figma screenshots** — a **folder path** passed as the 3rd argument (e.g. `01_SRS/workshop/wa_workshop/figma`); read every image in it (`.png` / `.jpg` / `.jpeg` / `.webp`). If no folder is given, the user may paste images in chat (step 3). Do NOT fetch Figma automatically.

## Prerequisite check (do this first)

Confirm the Atlassian Jira MCP is connected. If no Jira MCP tool is available (look for a tool like `getJiraIssue`, `jira_get_issue`, or an `atlassian`-namespaced tool), STOP and tell the user to set it up:

```
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp/authv2
```

Then run `/mcp` and authenticate (OAuth in browser). Resume `/gen-tc` after that. Do not invent ticket contents if the MCP is missing.

## Process

Create a todo per step and work through them in order.

### 1. Resolve the feature code AND its path

Read `00_Project_Info/features.md` and find the row for the feature slug.

- **Code** — use the row's **Code** as the ID prefix (`<CODE>`). Never invent a code silently, and never use a different code than the registry for a feature that already has one.
- **Path** — the section the row sits under gives the domain. A row under `## Workshop` means `<domain>` = `workshop`; a row under `## Standalone` has no domain. Build the target path from that, then **verify it against the disk** (`ls 01_SRS/<domain>/<slug>/`) before writing. If the folder does not exist, stop and ask — do not create a second home for a feature that already has one.

- **Entity** — read the row's **Entity** column. It names the records this feature owns, and it is how regression impact is found in step 4b.

If the slug is not listed at all, STOP and ask the user for three things — a short code (2–6 uppercase letters), which domain it belongs to, and which **entity** it takes as its subject (see the registry's "Entity column" section for the valid list and the rule against declaring session state) — then add a complete row to the correct section of the registry and continue.

If the row exists but its **Entity** cell is blank, do not guess it. Carry on with the run, and say so in the step-7 report so it gets filled.

### 2. Fetch the ticket

Call the Jira MCP tool to read the issue by key. Capture: summary, full description, issue type, status, labels/components, and any clarifying comments. Acceptance criteria in the ticket are optional — use them if present. If the tool name differs from what you expect, use whatever Jira "get issue" tool the connected MCP exposes.

**If the issue is an Epic** (`issuetype.name` = Epic) or otherwise has child issues, fetch **all** children with `searchJiraIssuesUsingJql` (JQL `parent = <KEY>`, include `description` and `comment`) and read each — the Epic itself usually has no detail. Derive TCs from the children **relevant to this feature** and trace each TC's **Jira** column to the specific child ticket.

### 3. Get the UI

If a Figma-screenshots folder was passed as the 3rd argument, list it and **Read every image file** (`.png` / `.jpg` / `.jpeg` / `.webp`) to see the screens/states (empty, filled, loading, error, success, validation). Otherwise, ask the user to paste the screenshots and wait for them. If neither a folder nor pasted images are provided, proceed using the ticket only and explicitly mark in the affected TCs' Note column that **UI coverage is pending** — never fabricate UI elements you have not seen.

### 4. Derive test conditions

First, check for the feature's AC spec at the mirror path resolved in step 1 (`02_Acceptance_Criteria/<domain>/<slug>/<slug>.md`, or `02_Acceptance_Criteria/<slug>/<slug>.md` when standalone):

- **If it exists**, read it. It is the primary source — derive TCs so that EVERY AC ID (`AC-<CODE>-NN`) and business rule (`BR-<CODE>-NN`) relevant to this ticket has at least one covering TC. Each TC records the AC/BR it verifies in its `AC` column.
- **If it does NOT exist**, that is fine — the AC layer is **optional/conditional**. Derive conditions from the ticket + screenshots and set each TC's `AC` column to `—`. Only suggest authoring it (via `/gen-ac <slug> <KEY>`) if the ticket is genuinely ambiguous, high-risk, or needs stakeholder sign-off; for clear, small tickets do not nag.

Then read `references/test-techniques.md` and follow it end-to-end: analyse the requirement first (§1), apply only techniques that add meaningful coverage (§2–§15), optimize to avoid redundant TCs (§16), and satisfy traceability + coverage rules before handoff. List conditions grouped by theme before writing so coverage is visible.

### 4b. Regression impact — find the affected features, don't guess them

`references/test-techniques.md` §15 requires every ticket to state its regression impact and to **reuse existing TCs** for impacted areas. That is only possible if you actually go and read them. Do this before writing:

1. Take this feature's **Entity** values from the registry row (step 1).
2. Search `00_Project_Info/features.md` for each entity. Every **other** row listing the same entity is a regression candidate — these are features that read or write the same records, and they are often in a **different domain**, so the domain hub will not reveal them. (Example: `Voucher` is listed by `wa_workshop`, `wp_workshop`, `wa_saved_voucher` and `wp_user_voucher` — two domains, four features.)
3. Also read the **domain hub** (`01_SRS/<domain>/<domain>.md`) for sibling sub-features on the other platform. A `wa_` feature and its `wp_` twin act on the same records through different actors, so admin-side changes routinely break the driver-side view and vice versa.
4. For each candidate, open its TC register and skim the group headings and TC IDs. Cite **real** `TC-<CODE>-NNN` IDs when you say existing coverage applies. **Never invent a TC ID** — if you have not opened the file, say coverage is unverified instead.
5. If the change is company-scoped data (any list or filter), add a cross-tenant negative case: a Client Admin must never see another company's records. Multi-tenancy is a standing risk on every such feature.

Keep this proportionate — a self-contained UI-copy change may genuinely have no impact, and "none, isolated" is a valid finding. Report what you checked, not just what you found.

### 5. Write / append the register

Target file: the path resolved in step 1 — `03_Testcases/<domain>/<slug>/<slug>.md`, or `03_Testcases/<slug>/<slug>.md` when standalone. Use the format in `04_Templates/testcases_template.md` (single source of truth — read it from the vault, not from this skill). Use `mkdir -p`.

The header's **SRS ref** must be a resolving wiki-link to the feature's SRS note: `[[01_SRS/<domain>/<slug>/<slug>]]`. Check the target file exists first — a link to a folder (trailing `/`) or to a note that was never written shows up as a dead grey node in Obsidian's graph.

- **If the file does not exist**, create it: fill the header (Feature, SRS ref, Jira tickets) and write the grouped Test Case Table.
- **If it exists**, this ticket's TCs are **appended** — continue the feature's TC numbering (find the highest existing `TC-<CODE>-NNN` and carry on), add rows under the right theme groups, and add this `<KEY>` to the header's "Jira tickets" list.

TC IDs are feature-based and zero-padded (`TC-<CODE>-001`). Every row's **AC** column names the `AC-<CODE>-NN` / `BR-<CODE>-NN` it verifies (or `—`), and the **Jira** column links this ticket. New TCs start at `Coverage: 🔵 Pending`, `Status: ⬜ Not Run`. Keep each TC high-level (one scenario, 3–5 steps max, NO click-by-click — the automation/Cucumber layer writes detailed steps) and the expected result unambiguous (status / error code / state).

### 6. Update the Coverage Summary

Recount ALL TCs in the file (existing + new) and refresh the Coverage Summary tables (Total/Automated/Manual/Pending + Critical/High/Medium/Low).

### 7. Report

Print a short summary in chat: TCs added this run, new feature total, breakdown by priority and theme, and any gaps (UI not provided, conditions you could not cover). Surface anything uncovered — never imply full coverage silently.

Also report, every run:

- **Regression impact from step 4b** — which features you checked (by entity and by domain sibling), which existing TC IDs you verified as still-covering, and which impacted areas you could **not** cover here. "None, isolated change" is a valid answer; silence is not.
- **Registry drift** — if this feature's row, or any row you read while searching by entity, has a blank **Entity** cell, list those slugs and ask the user to fill them. A blank cell silently shrinks every future impact search, so it must not pass unmentioned.

## Handling collisions

The per-feature file is expected to grow, so the default for an existing file is **append** (continue numbering). Never renumber or overwrite existing TCs. If a ticket's TCs were already added before (same `<KEY>` in the header list), ask the user: replace that ticket's rows, add anyway, or abort.

## Output conventions

- One feature = one register file at the mirror path of its SRS folder, accumulating TCs from all its tickets.
- **Linking discipline** — the register links **up** to its own SRS note only. Do not link it to `00_Project_Info/features.md`, to a domain hub, or to a sibling feature's register. Cross-feature references belong in prose using the other feature's `<CODE>`, not a wiki-link. This keeps Obsidian's graph a clean tree (`features → domain hub → feature → AC/TC`) instead of a hairball.
- IDs are feature-based: `TC-<CODE>-NNN`, continuous within the feature.
- Register format lives in `04_Templates/testcases_template.md` (user-managed). Read it each run — do not hardcode a copy.
- Traceability: each TC links its ticket (**Jira** column). When AC exist, each TC names the AC/BR it verifies (**AC** column) — `Jira → AC → TC`. When AC are omitted, set **AC** to `—` — `Jira → TC`. Coverage rule: every requirement + business rule must have ≥1 TC; every `Critical`/`High` AC when present — flag gaps.
- Write all content in English (the vault is shared on GitHub) — body text, cell content, headers, and tag values.
- Never modify `.obsidian/` config.
