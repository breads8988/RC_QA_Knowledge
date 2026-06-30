---
name: gen-tcs-from-jira
description: Use when generating test cases (TCs) from a Jira ticket plus Figma screenshots. Fetches the ticket via the Atlassian (Jira) MCP, reads the feature's acceptance-criteria spec if present, takes UI screenshots pasted by the user, applies full test-design techniques, and appends to a per-feature Test Case Register (grouped markdown tables) in an Obsidian QA vault, with every TC traced to the AC it verifies and the Jira ticket.
---

# Generate Test Cases from Jira + Figma

Turn a Jira ticket and its Figma UI into a complete, traceable Test Case Register written as Obsidian markdown — **one register file per feature** (`03_Testcases/<feature>.md`), grouped tables, every TC linked to the AC it verifies and to its Jira ticket.

## Inputs

- **Feature slug** — e.g. `login`, `user_management` (same slugs as `01_SRS/`). Passed explicitly in the command. Sets the register file name `03_Testcases/<feature>.md`.
- **Feature code** — the short ID prefix (e.g. `UM`), resolved from the registry `00_Project_Info/features.md`, NOT invented ad hoc. See step 1.
- **Jira key** — e.g. `RC-4` (the command extracts this from a key or URL).
- **Vault path** — default is the **current working directory** (`.`). This skill is project-scoped inside the vault's `.claude/`, so Claude Code runs at the vault root; all paths below are **relative** to it. Never hardcode a machine-specific absolute path (the vault is shared via GitHub — absolute paths break on teammates' machines).
- **Figma screenshots** — pasted into the chat by the user during step 2. Do NOT fetch Figma automatically; this skill relies on pasted images.

## Prerequisite check (do this first)

Confirm the Atlassian Jira MCP is connected. If no Jira MCP tool is available (look for a tool like `getJiraIssue`, `jira_get_issue`, or an `atlassian`-namespaced tool), STOP and tell the user to set it up:

```
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp/authv2
```

Then run `/mcp` and authenticate (OAuth in browser). Resume `/gen-tc` after that. Do not invent ticket contents if the MCP is missing.

## Process

Create a todo per step and work through them in order.

### 1. Resolve the feature code

Read `00_Project_Info/features.md` and find the row for the feature slug. Use its **Code** as the ID prefix (`<CODE>`). If the slug is not listed, STOP and ask the user for a short code (2–6 uppercase letters), add a new row to the registry, then continue. Never invent a code silently or use a different code than the registry for a feature that already has one.

### 2. Fetch the ticket

Call the Jira MCP tool to read the issue by key. Capture: summary, full description, issue type, status, labels/components, and any clarifying comments. Acceptance criteria in the ticket are optional — use them if present. If the tool name differs from what you expect, use whatever Jira "get issue" tool the connected MCP exposes.

### 3. Get the UI

Ask the user to paste Figma screenshots of the screens/states involved (empty, filled, loading, error, success, validation states if relevant). Wait for them. If the user skips this, proceed using the ticket only and explicitly mark in the affected TCs' Note column that **UI coverage is pending** — never fabricate UI elements you have not seen.

### 4. Derive test conditions

First, check for the feature's AC spec at `02_Acceptance_Criteria/<feature>.md`:

- **If it exists**, read it. It is the primary source — derive TCs so that EVERY AC ID (`AC-<CODE>-NN`) and business rule (`BR-<CODE>-NN`) relevant to this ticket has at least one covering TC. Each TC records the AC/BR it verifies in its `AC` column.
- **If it does NOT exist**, that is fine — the AC layer is **optional/conditional**. Derive conditions from the ticket + screenshots and set each TC's `AC` column to `—`. Only suggest authoring it (via `/gen-ac <feature> <KEY>`) if the ticket is genuinely ambiguous, high-risk, or needs stakeholder sign-off; for clear, small tickets do not nag.

Then read `references/test-techniques.md` and follow it end-to-end: analyse the requirement first (§1), apply only techniques that add meaningful coverage (§2–§10), optimize to avoid redundant TCs (§11), and satisfy traceability + coverage rules before handoff. List conditions grouped by theme before writing so coverage is visible.

### 5. Write / append the register

Target file: `03_Testcases/<feature>.md`, using the format in `04_Templates/testcases_template.md` (single source of truth — read it from the vault, not from this skill). Use `mkdir -p`.

- **If the file does not exist**, create it: fill the header (Feature, SRS ref, Jira tickets) and write the grouped Test Case Table.
- **If it exists**, this ticket's TCs are **appended** — continue the feature's TC numbering (find the highest existing `TC-<CODE>-NNN` and carry on), add rows under the right theme groups, and add this `<KEY>` to the header's "Jira tickets" list.

TC IDs are feature-based and zero-padded (`TC-<CODE>-001`). Every row's **AC** column names the `AC-<CODE>-NN` / `BR-<CODE>-NN` it verifies (or `—`), and the **Jira** column links this ticket. New TCs start at `Coverage: 🔵 Pending`, `Status: ⬜ Not Run`. Keep each TC high-level (one scenario, 3–5 steps max, NO click-by-click — the automation/Cucumber layer writes detailed steps) and the expected result unambiguous (status / error code / state).

### 6. Update the Coverage Summary

Recount ALL TCs in the file (existing + new) and refresh the Coverage Summary tables (Total/Automated/Manual/Pending + Critical/High/Medium/Low).

### 7. Report

Print a short summary in chat: TCs added this run, new feature total, breakdown by priority and theme, and any gaps (UI not provided, conditions you could not cover). Surface anything uncovered — never imply full coverage silently.

## Handling collisions

The per-feature file is expected to grow, so the default for an existing file is **append** (continue numbering). Never renumber or overwrite existing TCs. If a ticket's TCs were already added before (same `<KEY>` in the header list), ask the user: replace that ticket's rows, add anyway, or abort.

## Output conventions

- One feature = one register file (`03_Testcases/<feature>/TCs_<feature>.md`), accumulating TCs from all its tickets.
- IDs are feature-based: `TC-<CODE>-NNN`, continuous within the feature.
- Register format lives in `04_Templates/testcases_template.md` (user-managed). Read it each run — do not hardcode a copy.
- Traceability: each TC links its ticket (**Jira** column). When AC exist, each TC names the AC/BR it verifies (**AC** column) — `Jira → AC → TC`. When AC are omitted, set **AC** to `—` — `Jira → TC`. Coverage rule: every requirement + business rule must have ≥1 TC; every `Critical`/`High` AC when present — flag gaps.
- Write all content in English (the vault is shared on GitHub) — body text, cell content, headers, and tag values.
- Never modify `.obsidian/` config.
