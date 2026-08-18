---
description: Generate test cases from a Jira ticket + Figma screenshots into the per-feature register
argument-hint: <slug> <JIRA-KEY or link> [figma-folder]
---

The user wants to generate test cases (TCs) from a Jira ticket and Figma screenshots.

Input given: **$ARGUMENTS**

- The **first argument** is the **feature slug** — it names a folder under `01_Features/`. Standalone features are a bare slug (`login`, `registration`); features under a shared domain carry a platform prefix (`wa_workshop`, `wp_lawyer`). The skill reads **both** the short ID code (e.g. `WS` → `TC-WS-NNN`) **and** the target path from that feature's hub note `01_Features/<domain>/<slug>/<slug>.md` — the output goes to `01_Features/<domain>/<slug>/<slug>_tc.md`, beside the feature's SRS. If the feature has no hub yet, the skill creates one, asking you to confirm only its **code** and **entity**.
- The **second argument** is a Jira issue key (e.g. `RC-4`) or a full Jira URL — extract the issue key from it.
- The **third argument** (optional) is a **folder of Figma screenshots** for the feature (e.g. `01_Features/login/screens`, `01_Features/workshop/wa_workshop/screens`). If given, the skill reads every image in it (`.png` / `.jpg` / `.jpeg` / `.webp`) to ground the UI states under test — no pasting needed. If omitted, the user may paste screenshots in chat; if none are provided, mark UI coverage as pending.
- **Vault path** is always the **current working directory** (`.`) — this command lives inside the vault's `.claude/`, so Claude Code already runs at the vault root. All output paths (`01_Features/`, `04_Templates/`, `00_Project_Info/`) are relative to it. Never hardcode a machine-specific absolute path.

If the feature slug is missing, ask the user for it before proceeding (do not guess).

Now invoke the **gen-tcs-from-jira** skill and follow it exactly. Pass it the feature slug, the extracted Jira key, and the Figma-screenshots folder (if provided).
