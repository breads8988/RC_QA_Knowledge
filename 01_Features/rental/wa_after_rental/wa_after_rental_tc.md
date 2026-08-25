---
type: tc
feature: "[[wa_after_rental]]"
code: ARE
jira: [RC-137]
version: 1.0
updated: 2026-08-25
owner: QC Team
reviewer: "<Lead name>"
sprint: "<Sprint X>"
tc_total: 28
tc_automated: 0
tc_pending: 28
status: Draft
---

# Test Case Register — After Rental (`ARE`)

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 28        | 0         | 0      | 28      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 8        | 9    | 9      | 2   |

> **Note:** the zone-capture diagram, guided camera and damage-entry form (Steps 2, 3, 5) are governed by the same behaviour as `BRE` — see `TC-BRE-006`–`TC-BRE-013`, `TC-BRE-021`–`TC-BRE-025`. Not re-verified in full depth here; `TC-ARE-006`, `TC-ARE-010`, `TC-ARE-016` cover only this flow's entry into that shared behaviour. The My Activities menu itself is verified in `TC-MA-001`.

## Test Case Table

### 1. Car Rental Cost Estimates — Entry & Before Rental State

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-001 | "Digital cost estimates" opens the Car rental cost estimates page | AC-ARE-01 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-001` | User is logged in and on the My Activities page | — | 1. Tap **Digital cost estimates**. | The Car rental cost estimates page opens, listing the user's rental data. | ⬜ Not Run | Entry tile name conflicts with `AC-MA-01` — see AC file Open Question 1 |
| TC-ARE-002 | Completed Before Rental section shows a checkmark and View button | AC-ARE-02 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-002` | Vehicle's Before Rental (`BRE`) submission is finished | 1 vehicle, Before Rental complete | 1. Open Car rental cost estimates. 2. View the vehicle's card. | The "Before rental" section shows a green checkmark and a **View** button. | ⬜ Not Run | |
| TC-ARE-003 | Unfinished Before Rental can be continued from this page | AC-ARE-03 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-003` | Vehicle's Before Rental (`BRE`) submission is not finished | 1 vehicle, Before Rental partial | 1. Open Car rental cost estimates. 2. View the vehicle's card. | The Before Rental steps can be continued from the card. | ⬜ Not Run | [DATA] |
| TC-ARE-004 | Vehicle card shows the 4-step After Rental timeline | AC-ARE-04 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-004` | Vehicle's Before Rental section is complete | 1 vehicle, Before Rental complete | 1. View the vehicle's card. | The After Rental timeline shows 4 steps in order: Capture photos, Capture damaged photos, Get AI Cost estimate, Submit. | ⬜ Not Run | |
| TC-ARE-005 | "Continue estimation after rental" opens the After Rental flow | AC-ARE-05 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-005` | Vehicle's Before Rental is complete, After Rental not submitted | 1 vehicle | 1. Tap **Continue estimation after rental**. | The After Rental flow opens at the Capture Photos step, scoped to that vehicle. | ⬜ Not Run | |

### 2. Capture Photos — Zone Diagram

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-006 | Capture Photos shows the same 9-zone diagram as Before Rental | AC-ARE-06, BR-ARE-03 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-006` | User has started the After Rental flow | — | 1. View the Capture Photos screen. | 9-zone top-down diagram shown, each zone with a camera icon, matching `BRE` (regression of `TC-BRE-006`). | ⬜ Not Run | |
| TC-ARE-007 | "Save it for later" preserves partial After Rental capture progress | AC-ARE-07 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-007` | User has captured some but not all 9 zones | 3 of 9 zones captured | 1. Tap **Save it for later**. | Progress is saved as a draft and can be resumed later. | ⬜ Not Run | |
| TC-ARE-008 | Proceed stays inactive with zero zones captured and no skip confirmed | AC-ARE-08, BR-ARE-02 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-008` | User is on Capture Photos with 0 zones captured | 0 photos | 1. Tap **Proceed** without capturing any photo or confirming skip. | Proceed does not advance the flow. | ⬜ Not Run | |
| TC-ARE-009 | Confirming skip with zero photos allows Proceed to continue | AC-ARE-09, BR-ARE-02 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-009` | User is on Capture Photos with 0 zones captured | 0 photos | 1. Tap **Proceed**. 2. Confirm the skip prompt. | The flow advances without any zone photos captured. | ⬜ Not Run | [DATA] confirmation UI not specified by the ticket — see AC file Open Question 6 |

### 3. Vehicle Part Details

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-010 | Vehicle Part Details lists AI-detected damage grouped by part | AC-ARE-10, BR-ARE-03 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-010` | AI has produced a damage list for the captured zones | Front bumper: Scratch | 1. View Vehicle Part Details. | Damage grouped by part, each row showing damage type, part, side 1, side 2, with an **Edit** action. | ⬜ Not Run | |
| TC-ARE-011 | Fixed bottom bar shows the total AI-estimated repair cost | AC-ARE-11 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-011` | User is on Vehicle Part Details with ≥1 damage entry | 1 damage entry | 1. View the bottom of the screen. | Total cost shown as "€[Amount] AI estimated repair cost". | ⬜ Not Run | |
| TC-ARE-012 | "Add damage" opens a form to manually add a missed damage entry | AC-ARE-12 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-012` | User is on Vehicle Part Details | — | 1. Tap **Add damage**. | A manual damage-entry form opens. | ⬜ Not Run | |
| TC-ARE-013 | Done finalizes the assessment list and proceeds to AI Processing | AC-ARE-13 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-013` | User is on Vehicle Part Details with ≥1 damage entry | 1 damage entry | 1. Tap **Done**. | The assessment list is finalized and the flow proceeds to AI Processing. | ⬜ Not Run | |

### 4. AI Processing

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-014 | AI Processing shows a loading animation and wait text | AC-ARE-14 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-014` | User has finalized Vehicle Part Details | — | 1. Observe the AI Processing screen. | Loading animation shown with text "Please wait AI is processing to assess damages". | ⬜ Not Run | |
| TC-ARE-015 | Back/exit is disabled during AI Processing | AC-ARE-15, BR-ARE-01 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-015` | The AI Processing screen is active | — | 1. Attempt to navigate back. 2. Attempt to exit the screen. | Both actions are disabled/blocked; the assessment continues uninterrupted. | ⬜ Not Run | |

### 5. Edit/Add Damage Modal

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-016 | Edit/Add Damage modal supports the same fields as Before Rental | AC-ARE-16, BR-ARE-03, BR-ARE-04 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-016` | User opens the Edit/Add Damage bottom sheet | — | 1. Open the modal. 2. Select multiple damage types (Scratch, Dent). 3. Select part, side 1, side 2. | Multi-select damage type, damaged car part, side 1 and side 2 fields all behave as in `BRE` (regression of `TC-BRE-022`/`TC-BRE-023`). | ⬜ Not Run | |

### 6. Submission Success Screen

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-017 | Done on AI Estimated Repair Cost opens Submission Success | AC-ARE-17 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-017` | AI processing has completed with ≥1 damage entry | — | 1. Tap **Done** on AI Estimated Repair Cost. | Success screen shows "Rental images have been submitted for before and after rental. Please take a look at the comparison of AI Cost estimate of Before rental and after rental" with a **View comparison** button. | ⬜ Not Run | |
| TC-ARE-018 | "View comparison" opens the Comparison Screen | AC-ARE-18 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-018` | User is on the Submission Success screen | — | 1. Tap **View comparison**. | The Comparison Screen opens for that vehicle's rental estimate. | ⬜ Not Run | |

### 7. Comparison Screen

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-019 | Comparison table shows Before vs After columns per part | AC-ARE-19 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-019` | A completed after-rental submission exists with ≥1 affected part | Front bumper: before=none, after=Scratch | 1. Open the Comparison Screen. 2. View the table. | Each part shows "Before rental" vs "After rental" columns comparing Damage, Car part, Side 1, Side 2. | ⬜ Not Run | |
| TC-ARE-020 | Sticky footer shows the Before/After total cost comparison | AC-ARE-20 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🔴 Critical | 🔵 Pending | `@TC-ARE-020` | User is on the Comparison Screen | Before: €345, After: €465 | 1. View the bottom of the screen. | Fixed footer shows "BEFORE RENTAL: €345" and "AFTER RENTAL: €465". | ⬜ Not Run | |
| TC-ARE-021 | "Back to home" returns to the Home page | AC-ARE-21 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | ⚪ Low | 🔵 Pending | `@TC-ARE-021` | User is on the Comparison Screen | — | 1. Tap **Back to home**. | User is navigated to the Home page. | ⬜ Not Run | |

### 8. Completed State & Delete Estimate

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-ARE-022 | Completed After Rental shows a completed state and View button | AC-ARE-22 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-022` | The After Rental flow has been submitted for a vehicle | — | 1. View that vehicle's card. | The "After rental" step shows a completed state with a **View** button. | ⬜ Not Run | |
| TC-ARE-023 | View (After rental) re-opens the submitted rental data | AC-ARE-23 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-023` | The After Rental step is in its completed state | — | 1. Tap **View**. | The submitted rental data is shown for review. | ⬜ Not Run | |
| TC-ARE-024 | Card's primary action becomes "View compared cost estimate" | AC-ARE-24 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-024` | Both Before Rental and After Rental are complete | — | 1. View the vehicle's card. 2. Tap the primary action button. | Button reads **View compared cost estimate** and opens the Comparison Screen. | ⬜ Not Run | |
| TC-ARE-025 | 3-dot/more-options icon opens the Delete Estimate action sheet | AC-ARE-25 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-025` | User is on Car rental cost estimates with ≥1 vehicle card | — | 1. Tap the card's 3-dot icon. | Bottom sheet opens with **Delete Estimate** and **Cancel**. | ⬜ Not Run | |
| TC-ARE-026 | Deleting an estimate shows a "deleted successfully" toast | AC-ARE-26 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟠 High | 🔵 Pending | `@TC-ARE-026` | The Delete Estimate action sheet is open | Vehicle: "VW Golf" | 1. Tap **Delete Estimate**. | The estimate is removed from the list; toast reads "VW Golf deleted successfully". | ⬜ Not Run | Soft vs. hard delete unconfirmed — see AC file Open Question 3 |
| TC-ARE-027 | Cancel dismisses the action sheet without changes | AC-ARE-27 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | ⚪ Low | 🔵 Pending | `@TC-ARE-027` | The Delete Estimate action sheet is open | — | 1. Tap **Cancel**. | The bottom sheet closes; the card is unchanged. | ⬜ Not Run | |
| TC-ARE-028 | Comparison table and vehicle graphic stay usable on small screens | AC-ARE-28 | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | 🟡 Medium | 🔵 Pending | `@TC-ARE-028` | User is on a small-screen device (e.g. 360×640) | Viewport: 360×640 | 1. Open the Comparison Screen. 2. View the 360 vehicle graphic and comparison table. | No layout breakage or unreadable overflow on the small viewport. | ⬜ Not Run | |

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
