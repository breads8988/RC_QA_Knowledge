# Bug Report — Template (→ Jira issue type: **Bug**)

Draft a bug here, then create it in Jira as a **Bug**. Fields map 1:1 to Jira's Bug issue type; the **Description block** is ready to paste straight into the Jira *Description* field (or pass to the Atlassian MCP `createJiraIssue`).

- Write so a developer reproduces it without asking a single question — exact, ordered steps.
- A bug found while running a TC: reference that `TC-<KEY>-NNN` and flag it `[BUG]` in the register.

---

## Jira fields

| Jira field          | Value                                                          |
| ------------------- | -------------------------------------------------------------- |
| **Project**         | `RC`                                                           |
| **Issue Type**      | Bug                                                            |
| **Summary**         | `[<Module>] <concise symptom — what is broken>`                |
| **Priority**        | Highest / High / Medium / Low / Lowest                         |
| **Severity** *(custom field, if enabled)* | Blocker / Critical / Major / Minor / Trivial |
| **Components**      | <component / module>                                           |
| **Affects version/s** | <build / version where reproduced>                          |
| **Environment**     | <env · OS · browser/device · account>                          |
| **Labels**          | <e.g. `qa-found`, `regression`>                                |
| **Linked issues**   | relates to `<KEY>` · blocks `<KEY>`                            |
| **Related TC / AC** | `TC-<KEY>-NNN` · `AC-<KEY>-NN`                                 |
| **Reporter**        | <name>                                                         |
| **Assignee**        | <dev / triage>                                                 |

## Description  *(paste into the Jira Description field)*

```markdown
h3. Description
<What is wrong, in 1–2 sentences + user/business impact.>

h3. Steps to Reproduce
# ...
# ...
# ...

h3. Expected Result
<what should happen — quote the AC if there is one>

h3. Actual Result
<what actually happens — exact error message / code / wrong value>

h3. Environment
<env · build · OS · browser/device · account>

h3. Reproducibility
<Always / Intermittent (x of y) / Once> — note any timing or data dependency.

h3. Evidence
<attach screenshot / screen recording / log snippet / request-response>
```

> The `h3.` / `#` markers are Jira wiki markup. If creating via the MCP with Markdown, use `###` headings and `1.` numbered lists instead.

---

## Field guides

### Summary convention
`[<Module>] <symptom>` — lead with the symptom, not the cause. Good: `[Login] App crashes when password field is empty`. Bad: `Login bug`.

### Priority (Jira) vs Severity — set both, they're independent
| | Meaning | Set by |
| --- | --- | --- |
| **Severity** | Technical impact of the defect | QA |
| **Priority** | How soon it must be fixed | QA + PO/Lead |

A logo typo can be **Trivial** severity but **High** priority. A rare crash can be **Blocker** severity but **Low** priority.

### Severity values
| Severity | Meaning |
| -------- | ------- |
| Blocker  | Core function unusable, data loss/corruption, security hole — stop ship |
| Critical | Major feature broken, no reasonable workaround |
| Major    | Feature works wrongly but has a workaround |
| Minor    | Small functional issue, low impact |
| Trivial  | Cosmetic — typo, alignment, wording |
