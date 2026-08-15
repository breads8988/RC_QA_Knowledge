# Acceptance Criteria — Template

BABOK-aligned acceptance criteria (BABOK §10.1 *Acceptance and Evaluation Criteria*). **One AC spec per feature**, written **inside the feature's own folder**, beside its SRS and TC notes. AC is the bridge between the requirement (SRS / Jira) and the test cases — every TC in the matching `<slug>_tc.md` register traces back to an AC ID here.

| Feature kind   | AC spec path                                  |
| -------------- | --------------------------------------------- |
| Standalone     | `01_Features/<slug>/<slug>_ac.md`             |
| Under a domain | `01_Features/<domain>/<slug>/<slug>_ac.md`    |

e.g. `01_Features/login/login_ac.md`, `01_Features/workshop/wa_workshop/wa_workshop_ac.md`.

- `<CODE>` is the feature's short code, read from its hub note `01_Features/<domain>/<slug>/<slug>.md` (e.g. `wa_workshop` → `WS`). The **file** is named by the full feature slug; the **IDs** use the short code. `NN` is the zero-padded AC / rule number, **continuous within the feature** across all its tickets.
- A feature AC spec **accumulates** criteria from multiple Jira tickets. Each row's **Jira** column links the specific ticket it came from.
- Two complementary forms (BABOK allows both — use whichever fits each requirement):
  - **Scenario-based** — `Given / When / Then`, for observable behaviour & flows.
  - **Rule-based** — Business Rules table, for constraints/policies/calculations that don't fit a scenario cleanly.
- Replace every `<...>` placeholder. Keep AC from the **user/business perspective** — describe *what*, never *how* (no UI clicks, no tech/implementation detail).

> **Quality bar (each AC must be):** Testable · Unambiguous · Atomic (one outcome) · Consistent · Complete · Independent of implementation. If you can't write a Then that passes/fails objectively, the AC isn't done.

---

## AC Spec header

```markdown
---
type: ac
feature: "[[<slug>]]"
code: <CODE>
jira: [RC-4, RC-12]
version: 1.0
updated: <YYYY-MM-DD>
ba_owner: <BA name>
reviewer: <name>
status: Draft
---

# Acceptance Criteria — <Feature name> (`<CODE>`)

<!-- feature: links up to the hub. It is this note's ONLY link — never link an
     AC spec sideways to another feature; cite the other feature's code instead. -->
```

## User Story

```markdown
**As a** <role / persona>
**I want** <capability>
**So that** <business value / benefit>
```

## Scenario-based AC — Given / When / Then

> One row = one scenario. Compound steps: put extra steps in the same cell with `<br>And …` / `<br>But …`. Cover happy path first, then alternate, negative, edge.

| AC ID        | Scenario           | Jira         | Type      | Criticality | Given (context)             | When (action / trigger)      | Then (expected outcome)                          | Linked TCs      | Status |
| ------------ | ------------------ | ------------ | --------- | ----------- | --------------------------- | ---------------------------- | ------------------------------------------------ | --------------- | ------ |
| AC-<CODE>-01 | <happy path title> | [<KEY>](url) | Happy     | 🔴 Critical | <user state / system state> | <the action the user takes>  | <observable result><br>And <secondary assertion> | `TC-<CODE>-001` | Draft  |
| AC-<CODE>-02 | <alternate title>  | [<KEY>](url) | Alternate | 🟠 High     | <context>                   | <action>                     | <result>                                         | `TC-<CODE>-002` | Draft  |
| AC-<CODE>-03 | <negative title>   | [<KEY>](url) | Negative  | 🔴 Critical | <context>                   | <invalid action / bad input> | <rejection + error message / code>               | `TC-<CODE>-003` | Draft  |
| AC-<CODE>-04 | <edge title>       | [<KEY>](url) | Edge      | ⚪ Low       | <boundary context>          | <boundary action>            | <expected boundary behaviour>                    | `TC-<CODE>-004` | Draft  |

## Business Rules (rule-based AC)

> For constraints, policies, limits, formulas, permissions — things that govern many scenarios. State the rule precisely enough to test.

| Rule ID      | Business Rule                                  | Jira         | Rationale / Source     | Criticality | Linked TCs      | Status |
| ------------ | ---------------------------------------------- | ------------ | ---------------------- | ----------- | --------------- | ------ |
| BR-<CODE>-01 | <e.g. "Password must be 8–32 chars, ≥1 digit"> | [<KEY>](url) | <stakeholder / policy> | 🔴 Critical | `TC-<CODE>-005` | Draft  |
| BR-<CODE>-02 | <e.g. "Session expires after 15 min idle">     | [<KEY>](url) | <security policy>      | 🔴 Critical | `TC-<CODE>-006` | Draft  |

## Column Guide

| Column          | Description                                                       | Values / Format                                   |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------- |
| **AC ID**       | Unique scenario id — TCs trace back to this                      | `AC-<CODE>-NN`                                  |
| **Rule ID**     | Unique business-rule id — TCs trace back to this                 | `BR-<CODE>-NN`                                  |
| **Scenario**    | Short title of the behaviour, start with an action verb          | Plain text                                        |
| **Jira**        | The ticket this AC came from                                     | `[<KEY>](url)`                                     |
| **Type**        | Class of scenario                                               | Happy / Alternate / Negative / Edge / Permission  |
| **Criticality** | Impact if this AC fails — drives the verifying TC's priority     | 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low          |
| **Given**       | Precondition / context true before the action                   | One state per clause; `<br>And …` to compound     |
| **When**        | The single action or event that triggers behaviour             | One trigger                                        |
| **Then**        | Observable, verifiable outcome — pass/fail must be objective    | Include error code / message / state where relevant |
| **Linked TCs**  | TCs in the feature's `<slug>_tc.md` register that verify this AC         | `TC-<CODE>-NNN`, comma-separated                |
| **Status**      | Review state of the criterion                                   | Draft / Reviewed / Approved                        |

## Traceability

```
Jira ticket  ──▶  AC-<CODE>-NN / BR-<CODE>-NN  ──▶  TC-<CODE>-NNN
 (the why)         (the what — this file)                  (the how to verify)
```

- **Upward**: header `SRS ref` + each row's `Jira` column link the AC to its source.
- **Downward**: the `Linked TCs` column lists the test cases that verify each AC.
- **Coverage rule**: every `Critical` and `High` AC and every business rule must have ≥1 Linked TC. Flag any such AC with zero TCs as a coverage gap. Conversely, every TC must name the `AC` it verifies — no orphan TCs.

> Write all content in English (the vault is shared on GitHub) — body text, cell content, headers, and Type / Criticality / Status values.
