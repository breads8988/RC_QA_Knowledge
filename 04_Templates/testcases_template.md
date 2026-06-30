# Test Case Register — Template

This is the output format for `gen-tcs-from-jira`. **One register file per feature**, written to `03_Testcases/<feature>.md` (e.g. `login.md`, `my_vehicle.md` — same feature slugs as `01_SRS/`).

- `<CODE>` is the feature's short code from the registry `00_Project_Info/features.md` (e.g. `user_management` → `UM`). The **file** is named by the full feature slug; the **IDs** use the short code. `NNN` is the zero-padded TC number, **continuous within the feature** (`001`, `002`, …) across all its tickets.
- A feature register **accumulates** TCs from multiple Jira tickets over time. Each row's **Jira** column links the specific ticket that TC came from.
- Replace every `<...>` placeholder with real content. Group TCs under `###` headings by theme (Happy Path, Validation, Error handling, Edge cases, …). The rows below show the required **shape**, not fixed content.
- Traceability: every TC links the **Jira** ticket (requirement). When AC exist, the **AC** column names `AC-<CODE>-NN` / `BR-<CODE>-NN` from `02_Acceptance_Criteria/<feature>.md` — flow: `Jira → AC → TC`. For simple tickets without AC, set **AC** to `—` — flow: `Jira → TC`.

---

## Register header

```markdown
# Test Case Register — <Feature name>

| Field                | Value                                   |
| -------------------- | --------------------------------------- |
| **Version**          | 1.0                                     |
| **Last updated**     | <YYYY-MM-DD>                            |
| **Feature**          | <feature name>                          |
| **SRS ref**          | [[01_SRS/<feature>/epic]]               |
| **Jira tickets**     | `RC-4`, `RC-12` (tickets covered so far) |
| **Owner**            | QC Team                                 |
| **Reviewer**         | <Lead name>                             |
| **Sprint / Release** | <Sprint X>                              |
```

## Coverage Summary

```markdown
| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| <N>       | 0         | 0      | <N>     | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| <c>      | <h>  | <m>    | <l> |
```

> Coverage % = Automated / Total × 100. Update after each sprint.

## Column Guide

| Column               | Description                                               | Values / Format                                    |
| -------------------- | -------------------------------------------------------- | -------------------------------------------------- |
| **TC ID**            | Unique identifier — must match `@tag` in `.feature` file | `TC-<CODE>-NNN` e.g. `TC-LOGIN-001`             |
| **Test Scenario**    | One-line title, start with an action verb                | Plain text                                         |
| **AC**               | The acceptance criterion / business rule this TC verifies | `AC-<CODE>-NN`, `BR-<CODE>-NN`, or `—` when designed directly from the requirement |
| **Jira**             | The ticket this TC came from                             | `[<KEY>](url)`                                      |
| **Priority**         | Business impact if this TC fails                         | 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low          |
| **Coverage**         | Automation status                                        | ✅ Automated / 🟡 Manual / 🔵 Pending               |
| **Cucumber Tag**     | `@TC-ID` used in `.feature` — mandatory if Automated     | `@TC-<CODE>-NNN` — must match TC ID exactly     |
| **Preconditions**    | System / data state required before test starts          | plain text                                         |
| **Test Data**        | Concrete input values — placeholders for sensitive data  | e.g. `amount: 100,000 VND`                         |
| **High-level Steps** | 3–5 steps describing the flow — no click-level detail    | numbered                                           |
| **Expected Result**  | Observable, verifiable outcome — no vague statements     | include status / error code / state where relevant |
| **Status**           | Latest execution result this cycle (≠ Coverage)          | ✅ Pass / ❌ Fail / ⛔ Blocked / ⬜ Not Run           |
| **Note**             | Flag special cases — include ticket/link if available    | `[FLAKY]` `[BUG]` `[DEP]` `[SKIP]` `[DATA]`        |

## Test Case Table

```markdown
### 1. <Group name — e.g. Happy Path>

| TC ID          | Test Scenario | AC            | Jira         | Priority    | Coverage   | Cucumber Tag      | Preconditions   | Test Data | High-level Steps | Expected Result | Status    | Note |
| -------------- | ------------- | ------------- | ------------ | ----------- | ---------- | ----------------- | --------------- | --------- | ---------------- | --------------- | --------- | ---- |
| TC-<CODE>-001 | <scenario>  | AC-<CODE>-01 | [<KEY>](url) | 🔴 Critical | 🔵 Pending | `@TC-<CODE>-001` | <preconditions> | <data>    | 1. … 2. … 3. …   | <expected>      | ⬜ Not Run |      |

### 2. <next group> …
```

## Gherkin Mapping (Automated TCs only)

> Add scenarios here as automation is implemented. The TC ID tag is mandatory for result tracing.

```gherkin
@TC-<CODE>-NNN @[suite] @[priority]
Scenario: <title from Test Scenario column>
  Given <precondition>
  When  <action>
  Then  <expected result>
  And   <additional assertion>
```

## Note Tag Reference

| Tag       | Meaning                                                            |
| --------- | ------------------------------------------------------------------ |
| `[FLAKY]` | Unstable — fails intermittently on CI. Check logs before rerunning |
| `[BUG]`   | Blocked by open bug — include ticket ID                            |
| `[DEP]`   | Depends on specific env, mock service, fixture, or config          |
| `[SKIP]`  | Temporarily skipped — include reason and owner                     |
| `[DATA]`  | Requires complex or manual data setup                              |
