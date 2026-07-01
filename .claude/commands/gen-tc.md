---
description: Generate test cases from a Jira ticket + Figma screenshots into the per-feature register
argument-hint: <feature> <JIRA-KEY or link> [figma-folder]
---

The user wants to generate test cases (TCs) from a Jira ticket and Figma screenshots.

Input given: **$ARGUMENTS**

- The **first argument** is the **feature slug** (e.g. `login`, `user_management`) — same slugs as `01_SRS/`. It sets the register file name (`03_Testcases/<feature>/<feature>.md`). The skill resolves the short ID code (e.g. `UM` → `TC-UM-NNN`) from the registry `00_Project_Info/features.md`.
- The **second argument** is a Jira issue key (e.g. `RC-4`) or a full Jira URL — extract the issue key from it.
- The **third argument** (optional) is a **folder of Figma screenshots** for the feature (e.g. `01_SRS/login/figma`). If given, the skill reads every image in it (`.png` / `.jpg` / `.jpeg` / `.webp`) to ground the UI states under test — no pasting needed. If omitted, the user may paste screenshots in chat; if none are provided, mark UI coverage as pending.
- **Vault path** is always the **current working directory** (`.`) — this command lives inside the vault's `.claude/`, so Claude Code already runs at the vault root. All output paths (`02_Acceptance_Criteria/`, `03_Testcases/`, `04_Templates/`, `00_Project_Info/`) are relative to it. Never hardcode a machine-specific absolute path.

If the feature slug is missing, ask the user for it before proceeding (do not guess).

Now invoke the **gen-tcs-from-jira** skill and follow it exactly. Pass it the feature slug, the extracted Jira key, and the Figma-screenshots folder (if provided).
