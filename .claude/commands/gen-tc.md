---
description: Generate test cases from a Jira ticket + Figma screenshots into the per-feature register
argument-hint: <feature> <JIRA-KEY or link> [vault-path]
---

The user wants to generate test cases (TCs) from a Jira ticket and Figma screenshots.

Input given: **$ARGUMENTS**

- The **first argument** is the **feature slug** (e.g. `login`, `user_management`) — same slugs as `01_SRS/`. It sets the register file name (`03_Testcases/<feature>.md`). The skill resolves the short ID code (e.g. `UM` → `TC-UM-NNN`) from the registry `00_Project_Info/features.md`.
- The **second argument** is a Jira issue key (e.g. `RC-4`) or a full Jira URL — extract the issue key from it.
- The **third argument** (optional) is the Obsidian vault path. If omitted, use the **current working directory** (`.`) — this command lives inside the vault's `.claude/`, so Claude Code is already running at the vault root. All output paths (`02_Acceptance_Criteria/`, `03_Testcases/`, `04_Templates/`, `00_Project_Info/`) are relative to it. Do NOT hardcode any machine-specific absolute path.

If the feature slug is missing, ask the user for it before proceeding (do not guess).

Now invoke the **gen-tcs-from-jira** skill and follow it exactly. Pass it the feature slug, the extracted Jira key, and the resolved vault path.
