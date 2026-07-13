# Test Case Register — Lawyer (Unfall Rechtsberatung)

| Field                | Value                                   |
| -------------------- | --------------------------------------- |
| **Version**          | 1.0                                     |
| **Last updated**     | 2026-07-09                              |
| **Feature**          | Lawyer page — Unfall Rechtsberatung (Accident legal advice) |
| **SRS ref**          | [[01_SRS/lawyer/]]                      |
| **Jira tickets**     | `RC-116` (child of Epic `RC-101` — Web App) |
| **Owner**            | QC Team                                 |
| **Reviewer**         | TBD                                     |
| **Sprint / Release** | TBD                                     |

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 12        | 0         | 0      | 12      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 4        | 2    | 4      | 2   |

> Coverage % = Automated / Total × 100. Update after each sprint.

## Test Case Table

### 1. Entry & lawyer-list display

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-LAW-001 | Open the lawyer list from "Unfall Rechtsberatung" | AC-LAW-01 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🟠 High | 🔵 Pending | `@TC-LAW-001` | User signed in, on the Home page | — | 1. Tap the "Unfall Rechtsberatung" tile on Home | The "Lawyers" list page opens and shows the available lawyer cards | ⬜ Not Run | |
| TC-LAW-002 | Show basic information of lawyer | AC-LAW-02, BR-LAW-01 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🔴 Critical | 🔵 Pending | `@TC-LAW-002` | On the Lawyers list page | ≥1 lawyer seeded | 1. Open the Lawyers list 2. Inspect a lawyer card | Each card shows the lawyer's name, law firm, star rating with review count, full address, phone number, email, and a "Get appointment" action; no distance is shown | ⬜ Not Run | [DATA] |

### 2. Filtering (by rating)

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-LAW-003 | Open the rating filter panel | AC-LAW-03 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🟡 Medium | 🔵 Pending | `@TC-LAW-003` | On the Lawyers list page | — | 1. Tap the filter icon in the header | A "Filter by" panel opens showing a RATINGS selector with values 1★, 2★, 3★, 4★, 5★ | ⬜ Not Run | |
| TC-LAW-004 | Filter lawyers by minimum rating (≥ selected) | AC-LAW-04, BR-LAW-02 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🟠 High | 🔵 Pending | `@TC-LAW-004` | "Filter by" panel open; lawyers seeded at mixed ratings | Rating = 2★; lawyers rated 1★ / 2★ / 3★ / 4★ / 5★ | 1. Select minimum rating 2★ 2. Apply | Only lawyers rated **≥ 2★** are listed (2★, 3★, 4★, 5★ shown; 1★ excluded) | ⬜ Not Run | [DATA] min-rating semantics per RC-116 |
| TC-LAW-005 | No lawyers match the rating filter (empty state) | AC-LAW-10 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🟡 Medium | 🔵 Pending | `@TC-LAW-005` | "Filter by" panel open | Rating = 5★; no lawyer rated 5★ | 1. Apply a minimum rating no lawyer satisfies | A no-results / empty state is shown and no lawyer cards are listed | ⬜ Not Run | Empty-state UI pending — confirm design |

### 3. Appointment flow (Get appointment → Calendly)

> Flow: **Get appointment → "Do you want &lt;Lawyer&gt; to contact you?" → "Yes, contact me" → Calendly opens in a new tab → complete booking → user returns to the Repair Check tab → "Thank you" popup.**

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-LAW-006 | "Get appointment" opens contact-confirmation prompt | AC-LAW-05, BR-LAW-03 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🔴 Critical | 🔵 Pending | `@TC-LAW-006` | On the Lawyers list page | Lawyer = "Mrs Kate Bergner" | 1. Tap "Get appointment" on a lawyer card | A prompt "Do you want Mrs Kate Bergner to contact you?" is shown with "Yes, contact me" and "No, I will check later" | ⬜ Not Run | |
| TC-LAW-007 | "Yes, contact me" opens Calendly in a new tab | AC-LAW-06, BR-LAW-03 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🔴 Critical | 🔵 Pending | `@TC-LAW-007` | Contact-confirmation prompt shown | Calendly link `https://calendly.com/alextyl/jaekelgmbh` | 1. Select "Yes, contact me" | The Calendly scheduling page opens in a new browser tab and the Repair Check tab is preserved, so the user can pick a day and time | ⬜ Not Run | [DEP] Calendly |
| TC-LAW-008 | Return to app tab after booking → "Thank you" popup | AC-LAW-07, BR-LAW-03 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🔴 Critical | 🔵 Pending | `@TC-LAW-008` | Booking completed on the Calendly tab; Repair Check tab still open | A free slot; name + email | 1. Complete the Calendly booking 2. Switch back to the Repair Check tab | A "Thanks for booking your appointment" popup is shown on the Repair Check tab, with an "Ok, Back to lawyers" action (no automatic redirect from Calendly) | ⬜ Not Run | [DEP] Calendly |
| TC-LAW-009 | Decline the appointment request | AC-LAW-08 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🟡 Medium | 🔵 Pending | `@TC-LAW-009` | Contact-confirmation prompt shown | — | 1. Select "No, I will check later" | The prompt closes, Calendly is not opened, no request is submitted, and the user returns to the lawyer list | ⬜ Not Run | |
| TC-LAW-010 | Return to the lawyer list from confirmation | AC-LAW-09 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | ⚪ Low | 🔵 Pending | `@TC-LAW-010` | "Thanks for booking your appointment" popup shown | — | 1. Select "Ok, Back to lawyers" | The user is returned to the lawyer list | ⬜ Not Run | |

### 4. Cross-cutting (responsive & resilience)

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-LAW-011 | Responsive layout on phone and tablet | AC-LAW-11, BR-LAW-04 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | 🟡 Medium | 🔵 Pending | `@TC-LAW-011` | Lawyer flow in the mobile web app | Phone + tablet (incl. iPad) breakpoints | 1. Open the Lawyer flow on a phone 2. Open it on a tablet / iPad | Layout renders correctly and all cards, the filter, and the appointment actions remain usable on both form factors | ⬜ Not Run | [DEP] regression — RC-116 iPad display defect |
| TC-LAW-012 | Lawyer list load failure shows error state | AC-LAW-02 | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | ⚪ Low | 🔵 Pending | `@TC-LAW-012` | Lawyer-list API unavailable / times out | Simulated network failure | 1. Open the Lawyers list while the API is failing | An error / retry state is shown instead of a blank or frozen page | ⬜ Not Run | Error-state UI pending — confirm design [DEP] |

## Gherkin Mapping (Automated TCs only)

> Add scenarios here as automation is implemented. The TC ID tag is mandatory for result tracing.

## Note Tag Reference

| Tag       | Meaning                                                            |
| --------- | ------------------------------------------------------------------ |
| `[FLAKY]` | Unstable — fails intermittently on CI. Check logs before rerunning |
| `[BUG]`   | Blocked by open bug — include ticket ID                            |
| `[DEP]`   | Depends on specific env, mock service, fixture, or config          |
| `[SKIP]`  | Temporarily skipped — include reason and owner                     |
| `[DATA]`  | Requires complex or manual data setup                              |
