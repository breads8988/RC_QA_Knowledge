---
description: Write BABOK-aligned acceptance criteria from a Jira ticket into the per-feature AC spec
argument-hint: <feature> <JIRA-KEY or link> [figma-folder]
---

The user wants to generate acceptance criteria (AC) from a Jira ticket, acting as a senior BA.

Input given: **$ARGUMENTS**

- The **first argument** is the **feature slug** (e.g. `login`, `user_management`) — same slugs as `01_SRS/`. It sets the AC spec file name (`02_Acceptance_Criteria/<feature>/<feature>.md`). The skill resolves the short ID code (e.g. `UM` → `AC-UM-NN`, `BR-UM-NN`) from the registry `00_Project_Info/features.md`.
- The **second argument** is a Jira issue key (e.g. `RC-4`) or a full Jira URL — extract the issue key from it.
- The **third argument** (optional) is a **folder of Figma screenshots** for the feature (e.g. `01_SRS/login/figma`). If given, the skill reads every image in it (`.png` / `.jpg` / `.jpeg` / `.webp`) to ground UI-behaviour scenarios — no pasting needed. If omitted, the user may paste screenshots in chat, or the AC is derived from the ticket alone.
- **Vault path** is always the **current working directory** (`.`) — this command lives inside the vault's `.claude/`, so Claude Code already runs at the vault root. All output paths (`02_Acceptance_Criteria/`, `03_Testcases/`, `04_Templates/`, `00_Project_Info/`) are relative to it. Never hardcode a machine-specific absolute path.

If the feature slug is missing, ask the user for it before proceeding (do not guess).

Now invoke the **gen-ac-from-jira** skill and follow it exactly. Pass it the feature slug, the extracted Jira key, and the Figma-screenshots folder (if provided).
