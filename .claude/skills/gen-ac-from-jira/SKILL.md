---
name: gen-ac-from-jira
description: Use when writing acceptance criteria (AC) from a Jira ticket, acting as a senior BA. Fetches the ticket via the Atlassian (Jira) MCP, optionally takes UI screenshots, decomposes the requirement into BABOK-aligned AC — Given/When/Then scenarios plus business rules with MoSCoW priority — and appends to a per-feature AC spec in the Obsidian QA vault, ready for test-case generation.
---

# Generate Acceptance Criteria from Jira

Act as a **senior Business Analyst**. Turn a Jira ticket into a clear, testable, BABOK-aligned acceptance-criteria spec (BABOK §10.1) — Given/When/Then scenarios + business rules — written **per feature** (`02_Acceptance_Criteria/<feature>.md`) so the QA team derives test cases from it via `/gen-tc`.

## Inputs

- **Feature slug** — e.g. `login`, `user_management` (same slugs as `01_SRS/`). Passed explicitly in the command. Sets the spec file name `02_Acceptance_Criteria/<feature>.md`.
- **Feature code** — the short ID prefix (e.g. `UM`), resolved from the registry `00_Project_Info/features.md`, NOT invented ad hoc. See step 1.
- **Jira key** — e.g. `RC-4` (the command extracts this from a key or URL).
- **Vault path** — default is the **current working directory** (`.`). This skill is project-scoped inside the vault's `.claude/`, so Claude Code runs at the vault root; all paths below are **relative** to it. Never hardcode a machine-specific absolute path (the vault is shared via GitHub — absolute paths break on teammates' machines).
- **Figma screenshots** *(optional)* — pasted by the user; use them to ground UI-behaviour scenarios. Do NOT fetch Figma automatically.

## Prerequisite check (do this first)

Confirm the Atlassian Jira MCP is connected (a tool like `getJiraIssue`, `jira_get_issue`, or an `atlassian`-namespaced tool). If missing, STOP and tell the user to set it up:

```
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp/authv2
```

Then run `/mcp` and authenticate (OAuth in browser). Do not invent ticket contents if the MCP is missing.

## Process

Create a todo per step and work through them in order.

### 1. Resolve the feature code
Read `00_Project_Info/features.md` and find the row for the feature slug. Use its **Code** as the ID prefix (`<CODE>`). If the slug is not listed, STOP and ask the user for a short code (2–6 uppercase letters), add a new row to the registry, then continue. Never invent a code silently or use a different code than the registry for a feature that already has one.

### 2. Fetch the ticket
Call the Jira MCP to read the issue by key. Capture: summary, full description, issue type, status, labels/components, any existing acceptance criteria in the ticket, and clarifying comments.

### 3. Analyse the requirement (BA work)
Apply `references/ac-techniques.md` §1: identify functional requirements, business rules, actors, preconditions, triggers, outputs, state changes, dependencies, and assumptions. Then restate as a **user story** (`As a <role>, I want <capability>, so that <benefit>`). This step drives most of the AC quality. If screenshots are provided, use them to ground UI states.

### 4. Decompose into AC
Read `references/ac-techniques.md` and apply it. Produce two complementary forms:
- **Scenario-based (Given/When/Then)** — cover happy path first, then alternate flows, negative cases, edge/boundary, and permission cases. One scenario = one outcome (atomic).
- **Business rules** — constraints, limits, formulas, policies, permissions that govern many scenarios.

Assign each AC/rule a **MoSCoW** priority (Must / Should / Could / Won't). Keep every AC testable, unambiguous, and free of implementation detail (the *what*, not the *how*).

### 5. Write / append the AC spec
Target file: `02_Acceptance_Criteria/<feature>.md`, using the format in `04_Templates/ac_template.md` (single source of truth — read it from the vault). Use `mkdir -p`.
- **If the file does not exist**, create it: header (Feature, SRS ref, Jira tickets, BA Owner), user story, GWT table, Business Rules table.
- **If it exists**, **append** this ticket's criteria — continue the feature's numbering (highest existing `AC-<CODE>-NN` / `BR-<CODE>-NN`), and add this `<KEY>` to the header's "Jira tickets" list.

AC IDs `AC-<CODE>-NN`, rule IDs `BR-<CODE>-NN`. Each row's **Jira** column links this ticket. Leave the `Linked TCs` column blank — `/gen-tc` fills it. New AC start at `Status: Draft`.

### 6. Report & raise questions
Print a summary: AC added this run + feature total, by type and priority. Then, as a BA, list **open questions / ambiguities** the ticket left unresolved (anything you had to assume) so the user can confirm with stakeholders before TCs are written. Never silently invent business rules — flag assumptions explicitly.

## Handling collisions
The per-feature file is expected to grow, so default for an existing file is **append** (continue numbering). Never renumber existing AC. If this `<KEY>` was already added before, ask the user: replace that ticket's rows, add anyway, or abort.

## Output conventions
- One feature = one AC spec (`02_Acceptance_Criteria/<feature>.md`), accumulating AC from all its tickets.
- IDs are feature-based: `AC-<CODE>-NN` / `BR-<CODE>-NN`, continuous within the feature.
- AC format lives in `04_Templates/ac_template.md` (user-managed) — read it each run, do not hardcode a copy.
- Traceability flow `Jira → AC → TC`: this skill produces the AC layer; `/gen-tc` consumes it.
- Write all content in English (the vault is shared on GitHub) — body text, cell content, headers, and Type/Priority/Status values.
- Never modify `.obsidian/` config.
