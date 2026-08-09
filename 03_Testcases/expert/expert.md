# Test Case Register — Expert Call Appointment

| Field                | Value                                   |
| -------------------- | --------------------------------------- |
| **Version**          | 1.0                                     |
| **Last updated**     | 2026-08-06                              |
| **Feature**          | Find an Expert / expert call appointment (vehicle-diagnosis expert callback & video-call booking) |
| **SRS ref**          | [[01_SRS/expert/]]                      |
| **Jira tickets**     | `RC-112` (under Epic [RC-101](https://motionscloud.atlassian.net/browse/RC-101)) |
| **Owner**            | QC Team                                 |
| **Reviewer**         | \<Lead name\>                           |
| **Sprint / Release** | \<Sprint X\>                            |

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 14        | 0         | 0      | 14      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 6        | 5    | 3      | 0   |

> **AC source:** [`02_Acceptance_Criteria/expert/expert.md`](../../02_Acceptance_Criteria/expert/expert.md) — all 12 AC (`AC-ECA-01…12`) and 7 business rules (`BR-ECA-01…07`) have ≥1 covering TC (BR-ECA-07 verified at the Home-page tile level, see `homepage.md`).

> ⚠️ **UI coverage is partial.** `01_SRS/expert/Screenshot 2026-08-06 at 09.23.55.png` shows only two flows (Make an appointment, Schedule a video call). The rating-filter control and error states are **not** visible in it. TCs marked `[DEP] UI pending` assert only the behaviour the ticket describes.

> ✅ **All 10 open questions resolved (2026-08-06)** — see `## Confirmed Decisions` in the AC spec: mandatory location permission (new TC-ECA-014), rating filter is ≥N★ (same as `lawyer`), option chooser always shows both icons, callback request only shows a "Thank you" popup, page access follows Admin feature-config, and no distance-radius restriction. TCs below updated to match.

## Test Case Table

### 1. Navigation & List Display

| TC ID       | Test Scenario                                              | AC        | Jira                                                        | Priority    | Coverage   | Cucumber Tag  | Preconditions                                                                 | Test Data                                    | High-level Steps                                                              | Expected Result                                                                                                          | Status    | Note                                                    |
| ----------- | ------------------------------------------------------------ | --------- | -------------------------------------------------------------- | ----------- | ---------- | ------------- | -------------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------- |
| TC-ECA-001  | Open the Find an Expert page and view available experts     | AC-ECA-01 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🔴 Critical | 🔵 Pending | `@TC-ECA-001` | At least 3 experts/workshops are available near the user's current location       | 3 experts with distinct names, ratings, distances | 1. Open the Web App. 2. Navigate to "Experte für Fahrzeugdiagnose".            | The expert list opens and lists all 3 available experts; each entry shows at least name, rating and distance.            | ⬜ Not Run | `[DEP]` UI pending — card contents unconfirmed beyond screenshot |
| TC-ECA-002  | Expert list shows available experts (regression)            | AC-ECA-07 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🔴 Critical | 🔵 Pending | `@TC-ECA-002` | At least 1 expert/workshop is available near the user                             | 1 expert                                      | 1. Open the Find an Expert page. 2. Inspect the list.                          | The available expert is shown in the list; the list is not empty when qualifying data exists.                             | ⬜ Not Run | `[BUG]` Regression for Ann's 2026-07-08 report "Can't see any in expert page" |
| TC-ECA-003  | Distance reflects the user's current location                 | BR-ECA-03 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟠 High     | 🔵 Pending | `@TC-ECA-003` | The user's device location is known and differs from a second test location       | 2 known device locations; 1 expert at a fixed workshop location | 1. Open the Find an Expert page at location A, note the shown distance. 2. Change the device location to B. 3. Reopen the page. | The displayed distance is the map distance between the current device location and the workshop, and updates when the device location changes. | ⬜ Not Run | `[DATA]`                                                |
| TC-ECA-004  | No experts available at all (default view is not radius-restricted) | AC-ECA-11, BR-ECA-04 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟡 Medium   | 🔵 Pending | `@TC-ECA-004` | No expert/workshop exists at all                                                  | —                                              | 1. Open the Find an Expert page with zero experts in the system.               | An explicit empty state is shown, distinguishable from a loading or broken page.                                          | ⬜ Not Run | `[DEP]` UI pending — empty-state copy detail |
| TC-ECA-014  | Denying location permission shows a warning and blocks the list | AC-ECA-12, BR-ECA-03 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🔴 Critical | 🔵 Pending | `@TC-ECA-014` | User opens the Find an Expert page for the first time (no location permission granted yet) | —                                              | 1. Open the Find an Expert page. 2. Deny the location-permission prompt. 3. Observe the result. | A warning is shown telling the user location access is required, and the expert list is not displayed until permission is granted. | ⬜ Not Run |      |

### 2. Option Chooser

| TC ID       | Test Scenario                                            | AC        | Jira                                                        | Priority    | Coverage   | Cucumber Tag  | Preconditions                              | Test Data | High-level Steps                                                     | Expected Result                                                                                                  | Status    | Note                                                       |
| ----------- | ------------------------------------------------------------ | --------- | -------------------------------------------------------------- | ----------- | ---------- | ------------- | --------------------------------------------- | --------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------- |
| TC-ECA-005  | Open the option chooser for an expert                     | AC-ECA-02 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟠 High     | 🔵 Pending | `@TC-ECA-005` | The expert list is shown with ≥1 entry          | 1 expert  | 1. Select an expert entry from the list.                                | The option-chooser popup is shown for that expert, always offering both the "Schedule a video call" and "Make an appointment" icons (confirmed — no per-expert gating). | ⬜ Not Run |      |
| TC-ECA-006  | Option chooser reliably appears on every selection (regression) | AC-ECA-08 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🔴 Critical | 🔵 Pending | `@TC-ECA-006` | The expert list is shown with ≥1 entry          | 1 expert, selected repeatedly | 1. Select the same expert entry 5 times in a row, closing the popup between each. | The option-chooser popup is shown every time the entry is selected — never silently fails to appear.       | ⬜ Not Run | `[BUG]` Regression for Ann's 2026-07-13 report "click Expert dont' show popup" |

### 3. Callback Request ("Make an appointment")

| TC ID       | Test Scenario                                          | AC                    | Jira                                                        | Priority    | Coverage   | Cucumber Tag  | Preconditions                                     | Test Data       | High-level Steps                                                                                  | Expected Result                                                                                          | Status    | Note                                     |
| ----------- | ------------------------------------------------------------ | ---------------------- | -------------------------------------------------------------- | ----------- | ---------- | ------------- | ------------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------- |
| TC-ECA-007  | Submit a callback request via "Make an appointment"     | AC-ECA-03, BR-ECA-01   | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🔴 Critical | 🔵 Pending | `@TC-ECA-007` | The option chooser is open for expert *X*               | Expert *X* = "John Doe" | 1. Select the "Make an appointment" icon. 2. Confirm "Do you want *X* to call you back and arrange an appointment?" via "Send Request". | A callback request for expert *X* is submitted, a "Thank you" confirmation popup is shown (no separate trackable status afterward), and no Calendly page is opened.  | ⬜ Not Run | `[DATA]` |

### 4. Video Call Scheduling (Calendly)

| TC ID       | Test Scenario                                             | AC                              | Jira                                                        | Priority    | Coverage   | Cucumber Tag  | Preconditions                                       | Test Data                       | High-level Steps                                                                                       | Expected Result                                                                                                       | Status    | Note                                     |
| ----------- | -------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------- | ----------- | ---------- | ------------- | -------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | --------- | ------------------------------------------- |
| TC-ECA-008  | Open the expert's own Calendly page via "Schedule a video call" | AC-ECA-04, BR-ECA-01, BR-ECA-02  | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🔴 Critical | 🔵 Pending | `@TC-ECA-008` | The option chooser is open for expert *X*                | Expert *X* = "Riparo Workshops"    | 1. Select the "Schedule a video call" icon. 2. Inspect the destination that opens.                          | Expert *X*'s own Calendly page opens in a new browser tab (not the shared `calendly.com/alextyl/jaekelgmbh` link), and no callback-request confirmation is shown. | ⬜ Not Run | `[DEP]` External service; per-expert Calendly link |
| TC-ECA-009  | Book a slot on the opened Calendly page                   | AC-ECA-05                       | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟠 High     | 🔵 Pending | `@TC-ECA-009` | Expert *X*'s Calendly page is open with available days/times | A future day with an open slot     | 1. Select a day, then a time. 2. Enter the required details. 3. Select "Schedule Event".                     | The video call is booked for the selected slot and a booking confirmation is shown.                                   | ⬜ Not Run | `[DEP]` External service; call duration/timezone not tested (deprioritized) |

### 5. Rating Filter

| TC ID       | Test Scenario                                | AC        | Jira                                                        | Priority  | Coverage   | Cucumber Tag  | Preconditions                                       | Test Data                            | High-level Steps                                              | Expected Result                                                                                                | Status    | Note                                     |
| ----------- | ------------------------------------------------ | --------- | -------------------------------------------------------------- | --------- | ---------- | ------------- | -------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------- |
| TC-ECA-010  | Filter by 2★ returns that rating and above (regression)  | AC-ECA-06, BR-ECA-05, BR-ECA-06 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟡 Medium | 🔵 Pending | `@TC-ECA-010` | The expert list contains experts across multiple ratings, including a decimal aggregate rating   | Experts rated 2★, 3★, 3.4★ (floors to 3★ bucket) and 4★             | 1. Apply the 2★ rating filter. 2. Inspect the result set and its order.                 | The 2★, 3★ (including the 3.4★ expert) and 4★ experts are shown, ordered rating-descending; results below 2★ are excluded.      | ⬜ Not Run | `[BUG]` Regression for Ann's 2026-07-18 report "filter by rating, don't show anything" |
| TC-ECA-011  | Rating filter matches no expert                | AC-ECA-10, BR-ECA-05 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟠 High   | 🔵 Pending | `@TC-ECA-011` | No expert matches the selected rating filter (≥N★) | Experts rated 2★ and 3★ only; filter set to 5★ | 1. Apply the 5★ rating filter. 2. Inspect the page and the filter control. | No expert entry is listed, an explicit "no results" state is shown instead of a blank page, and the filter stays applied. | ⬜ Not Run |      |

### 6. Error Handling & Resilience

| TC ID       | Test Scenario                     | AC        | Jira                                                        | Priority  | Coverage   | Cucumber Tag  | Preconditions                                         | Test Data | High-level Steps                                                    | Expected Result                                                                                     | Status    | Note                                     |
| ----------- | -------------------------------------- | --------- | -------------------------------------------------------------- | --------- | ---------- | ------------- | ----------------------------------------------------------- | --------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | --------- | ------------------------------------------- |
| TC-ECA-012  | Handle the expert's Calendly page being unreachable | AC-ECA-09 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟡 Medium | 🔵 Pending | `@TC-ECA-012` | Access to the expert's Calendly page is blocked                | —         | 1. Select "Schedule a video call" for an expert while Calendly is unreachable. 2. Return to the expert list. | The failure is reported to the user with a way to retry, and the expert list remains usable.           | ⬜ Not Run | `[DEP]` Needs network blocking |

### 7. Regression

| TC ID       | Test Scenario                              | AC  | Jira                                                        | Priority | Coverage   | Cucumber Tag  | Preconditions                                                  | Test Data | High-level Steps                                                                       | Expected Result                                                                                                              | Status    | Note                                                     |
| ----------- | ----------------------------------------------- | --- | -------------------------------------------------------------- | -------- | ---------- | ------------- | ------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| TC-ECA-013  | Confirm the Lawyer page is unaffected           | —   | [RC-112](https://motionscloud.atlassian.net/browse/RC-112)  | 🟠 High  | 🔵 Pending | `@TC-ECA-013` | Both the Find an Expert page and the Lawyer page are deployed         | —         | 1. Open the Lawyer page. 2. Apply its rating filter. 3. Open its scheduling options.          | The Lawyer list, rating filter and "Terminierungsoptionen" behave exactly as before this ticket's change — no shared-component regression. | ⬜ Not Run | `[DEP]` Cross-feature — belongs to `lawyer` (RC-116); duplicated here as RC-112 regression cover, symmetric to TC-LAW-019 |

## Regression Impact (§15)

| Impacted area                                                   | Risk                                                                                           | Covered by  |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| Lawyer page (RC-116) — shares the list + rating-filter + Calendly pattern | A shared list/filter/Calendly component changed for the Find an Expert page could alter Lawyer page behaviour | TC-ECA-013  |
| "Experte für Fahrzeugdiagnose" entry point in the Web App navigation | The entry point had to keep pointing at the reworked page after the UI update                   | TC-ECA-001  |

## Techniques not applied

| Technique                             | Why not applicable                                                                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| §6 Decision Table                      | The only condition driving the list outcome is the selected rating; no second interacting condition to combine.                            |
| §7 Pairwise / all-pairs                | Too few independent parameters to need combinatorial reduction.                                                                              |
| §8 State Transition                    | Selecting a callback request or opening Calendly are isolated actions, not steps in an in-app entity lifecycle; the booking state lives in Calendly. |
| §9 Field-level validation              | No app-owned input field is described — the callback confirmation is a Yes/No action, and the Calendly detail form is an external page out of this app's scope. |
| §13 Non-functional (perf / security / a11y / responsive / i18n) | RC-112 states no performance target, security requirement, accessibility scope, or phone/tablet requirement (unlike RC-116); none is inferred. |
| §3 Unauthorised access                 | Confirmed access follows the Admin feature-config mechanism (BR-ECA-07), same as the Home page. Gating is tested at the Home-page tile level (`homepage.md` TC-HOME-002/009), not duplicated here. |

## Gherkin Mapping (Automated TCs only)

> Add scenarios here as automation is implemented. The TC ID tag is mandatory for result tracing.

## Note Tag Reference

| Tag       | Meaning                                                            |
| --------- | ------------------------------------------------------------------ |
| `[FLAKY]` | Unstable — fails intermittently on CI. Check logs before rerunning |
| `[BUG]`   | Blocked by / verifying an open bug — include ticket ID             |
| `[DEP]`   | Depends on specific env, mock service, fixture, or config          |
| `[SKIP]`  | Temporarily skipped — include reason and owner                     |
| `[DATA]`  | Requires complex or manual data setup                              |
