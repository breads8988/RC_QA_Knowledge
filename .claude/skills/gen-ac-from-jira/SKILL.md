---
name: gen-ac-from-jira
description: Use when writing acceptance criteria (AC) from a Jira ticket, acting as a senior BA. Fetches the ticket via the Atlassian (Jira) MCP, optionally takes UI screenshots, decomposes the requirement into BABOK-aligned AC — Given/When/Then scenarios plus business rules, each rated by criticality — and appends to a per-feature AC spec in the Obsidian QA vault, ready for test-case generation.
---

# Generate Acceptance Criteria from Jira

Act as a **senior Business Analyst**. Turn a Jira ticket into a clear, testable, BABOK-aligned acceptance-criteria spec (BABOK §10.1) — Given/When/Then scenarios + business rules — written **per feature** so the QA team derives test cases from it via `/gen-tc`.

## Read the conventions first

**Read `00_Project_Info/conventions.md` before writing any path, ID, or link.** It is the single source of truth for the vault's structure — one folder per feature, slug and `wa_`/`wp_` prefix rules, the hub's frontmatter, the entity notes and how impact is found, and the linking discipline. This skill does not restate those rules; if it ever appears to contradict that file, that file wins.

Also read `CLAUDE.md` for the business layer — the actors behind `wa_`/`wp_`, the German domain vocabulary, and the entity model. AC quality depends far more on getting the actor right than on formatting.

## Inputs

- **Feature slug** — e.g. `login` (standalone), `wa_workshop` (under the `workshop` domain). Names a folder under `01_Features/`. Passed explicitly in the command.
- **Feature code** — the short ID prefix (e.g. `WS`), read from the feature hub's frontmatter, NOT invented ad hoc. See step 1.
- **Jira key** — e.g. `RC-4` (the command extracts this from a key or URL).
- **Vault path** — always the **current working directory** (`.`). This skill is project-scoped inside the vault's `.claude/`, so Claude Code runs at the vault root; all paths below are **relative** to it. Never hardcode a machine-specific absolute path (the vault is shared via GitHub — absolute paths break on teammates' machines).
- **Figma screenshots** _(optional)_ — a **folder path** passed as the 3rd argument (e.g. `01_Features/workshop/wa_workshop/screens`); read every image in it (`.png` / `.jpg` / `.jpeg` / `.webp`) to ground UI-behaviour scenarios. If no folder is given, the user may paste screenshots instead. Do NOT fetch Figma automatically.

## Prerequisite check (do this first)

Confirm the Atlassian Jira MCP is connected (a tool like `getJiraIssue`, `jira_get_issue`, or an `atlassian`-namespaced tool). If missing, STOP and tell the user to set it up:

```
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp/authv2
```

Then run `/mcp` and authenticate (OAuth in browser). Do not invent ticket contents if the MCP is missing.

## Process

Create a todo per step and work through them in order.

### 1. Locate the feature hub and read its metadata

Find the hub: `ls 01_Features/*/<slug>/<slug>.md 01_Features/<slug>/<slug>.md`. Read its frontmatter.

- **Code** — use the hub's `code` as the ID prefix (`<CODE>`). Never invent a code, and never use a different one for a feature that already has a hub.
- **Path** — the hub's own folder. Everything this skill writes goes inside it.
- **Entity** — the hub's `entity` links name the records this feature owns; they drive step 3b.

**If no hub exists**, do not stop and do not create a second home for the feature. Create it:

1. Propose a `code` derived from the slug (2–6 uppercase letters) and **verify it is unused**: `grep -rh '^code: ' 01_Features | sort`. 
2. Ask the user to confirm two things only — the **code** and the **entity** (valid values in `conventions.md` §4; do not declare an entity the feature merely branches on).
3. Write `01_Features/<domain>/<slug>/<slug>.md` from `04_Templates/feature_hub_template.md` and a screens-only `<slug>_srs.md` from `04_Templates/srs_template.md`; add a row to the domain hub if the feature sits in a domain.

If the hub exists but its `entity` is empty, do not guess it. Carry on with the run, and say so in the step-6 report so it gets filled.

### 2. Fetch the ticket

Call the Jira MCP to read the issue by key. Capture: summary, full description, issue type, status, labels/components, any existing acceptance criteria in the ticket, and clarifying comments.

**If the issue is an Epic** (`issuetype.name` = Epic) or otherwise has child issues, fetch **all** children with `searchJiraIssuesUsingJql` (JQL `parent = <KEY>`, include the `description` and `comment` fields) and read each. An Epic usually has no detail of its own — the real requirements live in its children. Use the children **relevant to this feature** as the requirement sources, and trace each AC's **Jira** column to the **specific child ticket** it came from, not the Epic.

### 3. Analyse the requirement (BA work)

Apply `references/ac-techniques.md` §1: identify functional requirements, business rules, actors, preconditions, triggers, outputs, state changes, dependencies, impacted existing behaviour, and assumptions. Then restate as a **user story** (`As a <role>, I want <capability>, so that <benefit>`). This step drives most of the AC quality. If a Figma-screenshots folder was passed, list it and **Read every image file** to ground UI states; otherwise use any pasted screenshots. Never fabricate UI elements you have not seen.

### 3b. Find the impacted existing behaviour — read it, don't recall it

§1 asks for **impacted existing behaviour**. As a BA that means naming the existing rules this change can contradict, and you cannot do that from memory. Before decomposing:

1. Take this feature's `entity` links from the hub (step 1).
2. **Open each entity note and read its backlinks** — `grep -rl 'e_voucher' 01_Features` gives the same answer from the shell. Every other feature linking that entity shares those records, and is often in a **different domain**, so the domain hub will not reveal it. (Example: `e_voucher` is linked by `wa_workshop`, `wp_workshop`, `wa_saved_voucher` and `wp_user_voucher` — two domains, four features.)
3. Open those features' `<slug>_ac.md` and read their **Business Rules** tables. A new rule that contradicts an existing `BR-<CODE>-NN` is the single most expensive defect this skill can prevent — the two specs would each look correct on their own.
4. Also read the **domain hub** (`01_Features/<domain>/<domain>.md`) for the sibling on the other platform. A rule written for the driver's view (`wa_`) usually has a matching admin-side obligation (`wp_`), and vice versa.
5. Cite **real** `BR-<CODE>-NN` / `AC-<CODE>-NN` IDs when you reference an existing rule. **Never invent an ID** — if you did not open the file, say so.

Record what you find as prose in the AC spec's user-story section and, where it constrains this feature, as a business rule of its own. Conflicts you cannot resolve go to the step-6 open-questions list — do not silently pick a winner.

### 4. Decompose into AC

Read `references/ac-techniques.md` and apply it. Produce two complementary forms:

- **Scenario-based (Given/When/Then)** — cover happy path first, then alternate flows, negative cases, rule/condition combinations, edge/boundary, and permission cases. One scenario = one outcome (atomic).
- **Business rules** — constraints, limits, formulas, policies, permissions that govern many scenarios.

Rate each AC/rule by **criticality** (🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low — impact if it fails, see `references/ac-techniques.md` §6), which maps 1:1 to the verifying TC's priority. Keep every AC testable, unambiguous, and free of implementation detail (the _what_, not the _how_).

### 5. Write / append the AC spec

Target file: `<hub folder>/<slug>_ac.md`. Use the format in `04_Templates/ac_template.md` (single source of truth — read it from the vault).

Its frontmatter must carry `type: ac`, `feature: "[[<slug>]]"`, `code`, `jira`, and status fields — the `feature` link is the note's only link, and it must resolve.

**After writing, set the hub's `ac: "[[<slug>_ac]]"` property if it is not already there.** A hub that does not point at its own AC is invisible to `features.base`.

- **If the file does not exist**, create it: frontmatter, user story, GWT table, Business Rules table.
- **If it exists**, **append** this ticket's criteria — continue the feature's numbering (highest existing `AC-<CODE>-NN` / `BR-<CODE>-NN`), and add this `<KEY>` to the header's "Jira tickets" list.

AC IDs `AC-<CODE>-NN`, rule IDs `BR-<CODE>-NN`. Each row's **Jira** column links this ticket. Leave the `Linked TCs` column blank — `/gen-tc` fills it. New AC start at `Status: Draft`.

### 6. Self-check & report

Run the final gate in `references/ac-techniques.md` §9 and fix any miss before reporting. Then print a summary: AC added this run + feature total, by type and priority. Then, as a BA, list **open questions / ambiguities** the ticket left unresolved (anything you had to assume) so the user can confirm with stakeholders before TCs are written. Never silently invent business rules — flag assumptions explicitly.

Also report, every run:

- **Impacted existing behaviour from step 3b** — which features you checked (by entity and by domain sibling), which existing `BR-`/`AC-` IDs this ticket touches or contradicts, and any conflict you left unresolved. "None, isolated change" is a valid answer; silence is not.
- **Metadata drift** — if this feature's hub, or any hub you read while searching by entity, has an empty `entity`, a missing `ac:`/`tc:` link, or no hub at all, list those slugs and ask the user to fill them. Empty metadata silently shrinks every future impact search, so it must not pass unmentioned. `python scripts/check_links.py` catches broken links the same way.

## Handling collisions

The per-feature file is expected to grow, so default for an existing file is **append** (continue numbering). Never renumber existing AC. If this `<KEY>` was already added before, ask the user: replace that ticket's rows, add anyway, or abort.

## Output conventions

- One feature = one AC spec inside the feature's own folder, accumulating AC from all its tickets.
- **Linking discipline** — the AC spec links **up** to its feature hub only, through the `feature:` property. Do not link it to a domain hub, to an entity note, or to a sibling feature. Cross-feature references belong in prose using the other feature's `<CODE>`, not a wiki-link. Features meet each other at the entity notes, which only hubs link to.
- IDs are feature-based: `AC-<CODE>-NN` / `BR-<CODE>-NN`, continuous within the feature.
- AC format lives in `04_Templates/ac_template.md` (user-managed) — read it each run, do not hardcode a copy.
- Traceability flow `Jira → AC → TC`: this skill produces the AC layer; `/gen-tc` consumes it.
- Write all content in English (the vault is shared on GitHub) — body text, cell content, headers, and Type/Priority/Status values.
- Never modify `.obsidian/` config.
