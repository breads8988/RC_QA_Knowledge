---
type: tc
feature: "[[wa_before_rental]]"
code: BRE
jira: [RC-127]
version: 1.0
updated: 2026-08-25
owner: QC Team
reviewer: "<Lead name>"
sprint: "<Sprint X>"
tc_total: 35
tc_automated: 0
tc_pending: 35
status: Draft
---

# Test Case Register — Before Rental (`BRE`)

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 35        | 0         | 0      | 35      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 6        | 9    | 17     | 3   |

> **Note:** the 4-vehicle registration cap and the Owner/Rental ownership field are owned by other features and verified there — see `TC-MV-013` / `TC-MV-014` (`MV`, `BR-MV-01`) and `TC-REG-038` (`REG`, `BR-REG-11`). Not re-verified in depth here; `TC-BRE-004`/`005` cover only this flow's entry points into those existing behaviours.

## Test Case Table

### 1. Select Car (Vehicle Selection)

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-001 | Select Car lists only Rental-flagged vehicles | AC-BRE-01, BR-BRE-01 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🔴 Critical | 🔵 Pending | `@TC-BRE-001` | User is logged in and has ≥1 vehicle with ownership `Owner` and ≥1 vehicle with ownership `Rental` (`BR-REG-11`) | 1 Owner vehicle, 1 Rental vehicle | 1. From Home, tap **Ein Auto Mieten**. 2. View the Select car list. | Select car screen opens subtitled "Please select your car"; only the Rental-flagged vehicle(s) are listed; the Owner-flagged vehicle does not appear. | ⬜ Not Run | |
| TC-BRE-002 | Vehicle card shows brand/model, Rental badge, specs and Proceed | AC-BRE-02 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-002` | User is on the Select car screen with ≥1 rental vehicle listed | — | 1. View a vehicle card. | Card shows brand + model, a "Rental" badge top-right, and specs (doors, seats, power in KW) with icons, plus a **Proceed** action. | ⬜ Not Run | |
| TC-BRE-003 | Proceed opens Capture Photos overview for the selected vehicle | AC-BRE-03 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🔴 Critical | 🔵 Pending | `@TC-BRE-003` | User is on the Select car screen with ≥2 rental vehicles listed | Vehicle: rental vehicle #1 | 1. Tap **Proceed** on vehicle #1's card. | User is navigated to the Capture photos overview screen scoped to vehicle #1. | ⬜ Not Run | |
| TC-BRE-004 | Register Vehicle opens the add-vehicle flow | AC-BRE-04 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-004` | User is on the Select car screen, has < 4 registered vehicles | — | 1. Tap the sticky **Register Vehicle** button. | The add-vehicle flow opens (same flow as `REG`; see `TC-REG-021`). | ⬜ Not Run | |
| TC-BRE-005 | Register Vehicle blocked once the 4-vehicle cap is reached | AC-BRE-05, BR-BRE-02 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-005` | User already has 4 registered vehicles (max, per `BR-MV-01`) | — | 1. Tap **Register Vehicle** on the Select car screen. | The same limit notice as `AC-MV-11` is shown and no new vehicle is added (regression of `TC-MV-014`). | ⬜ Not Run | [DATA] |

### 2. Capture Photos — Zone Diagram

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-006 | Capture Photos overview shows the 9-zone diagram and instruction text | AC-BRE-06 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-006` | User has navigated to Capture photos for a selected vehicle | — | 1. View the screen. | Prompt "Wählen Sie die Bereiche aus, auf denen ihr Fahrzeug beschädigt ist" is shown above a top-down 9-zone vehicle diagram. | ⬜ Not Run | |
| TC-BRE-007 | Tapping an empty zone's camera icon opens the guided camera | AC-BRE-07, BR-BRE-04 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-007` | A zone is in its empty state (zone name + camera icon) | Zone: Vorne | 1. Tap the zone's camera icon. | The camera screen opens for that zone (regression pattern of `TC-AA-029`). | ⬜ Not Run | |
| TC-BRE-008 | A captured zone shows green text, checkmark and photo count | AC-BRE-08 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-008` | User has captured 1 photo for a zone | Zone: Vorne, 1 photo | 1. Return to the Capture Photos diagram. | The zone's text turns green, the camera icon is replaced by a checkmark, and the photo count is shown (e.g. "1 Foto"). | ⬜ Not Run | |
| TC-BRE-009 | "Save it for later" preserves partial progress | AC-BRE-09 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-009` | User has captured photos for some but not all 9 zones | 3 of 9 zones captured | 1. Tap **Save it for later** (outline button). | Progress is saved; the flow can be resumed later without all 9 zones having been captured. | ⬜ Not Run | |
| TC-BRE-010 | Rear-left zone label reads "HINTEN LINKS" | AC-BRE-10, BR-BRE-06 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | ⚪ Low | 🔵 Pending | `@TC-BRE-010` | User is on the Capture Photos diagram | — | 1. View the rear-left zone label. | Label reads exactly "HINTEN LINKS" — the design's "HIINTEN" typo is corrected. | ⬜ Not Run | |

### 3. Guided Camera & Photo Management

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-011 | Guided camera opens with a vehicle-outline overlay | AC-BRE-11, BR-BRE-04 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-011` | User has tapped a zone's camera icon | — | 1. Observe the camera screen as it opens. | A translucent vehicle-outline overlay is shown, matching the existing Report Accident (`AA`) camera behaviour (regression of `TC-AA-029`). | ⬜ Not Run | |
| TC-BRE-012 | A captured photo appears as a removable thumbnail | AC-BRE-12, BR-BRE-04 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-012` | User is in the guided camera for a zone | — | 1. Take a photo. | A thumbnail appears bottom-left with an "x" badge. | ⬜ Not Run | |
| TC-BRE-013 | Removing a photo shows a dismissible "photo deleted" toast | AC-BRE-13, BR-BRE-04 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-013` | A captured-photo thumbnail with an "x" badge is shown | — | 1. Tap the "x" on the thumbnail. | The photo is deleted and a dismissible toast reads "The photo deleted". | ⬜ Not Run | |

### 4. Vehicle Part Details — Overview

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-014 | Vehicle part details shows Part detail (active) and Photos tabs | AC-BRE-14, BR-BRE-05 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-014` | User has completed zone photo capture and continues to Vehicle part details | — | 1. View the screen. | Two tabs are shown: **Part detail** (active) and **Photos**. | ⬜ Not Run | |
| TC-BRE-015 | Part detail tab shows a rotatable, tappable diagram | AC-BRE-15, BR-BRE-05 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-015` | User is on the Part detail tab | — | 1. View the diagram. 2. Tap the left/right rotate arrows. | A FRONT SIDE / REAR SIDE diagram is shown with labeled, interactive parts (Hood, Windshield, L./R. Headlight, etc.); the arrows switch sides (regression pattern of `TC-AA-051`). | ⬜ Not Run | |
| TC-BRE-016 | First-time guidance hints where to tap | AC-BRE-16 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | ⚪ Low | 🔵 Pending | `@TC-BRE-016` | User opens Vehicle part details for the first time in this rental flow | — | 1. View the screen on first entry. | A floating tooltip reads "Tap on the car parts to add damage". | ⬜ Not Run | |
| TC-BRE-017 | Empty damaged-parts list shows the empty state | AC-BRE-17 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-017` | No damaged part has been added yet | — | 1. View the bottom sheet. | An icon and "No damaged parts added yet" are shown, with an **Add damaged part +** button in the header. | ⬜ Not Run | |
| TC-BRE-018 | Populated damaged-parts list shows each entry with an edit action | AC-BRE-18 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-018` | 1 damaged part has been added | Rear right backlight — Scratch, Dent | 1. View the bottom sheet. | The entry is listed with a summary (e.g. "Rear right backlight — Scratch, Dent") and an Edit icon. | ⬜ Not Run | |
| TC-BRE-019 | Done completes the Vehicle Part Details step | AC-BRE-19 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🔴 Critical | 🔵 Pending | `@TC-BRE-019` | User is on the Vehicle part details editor with ≥1 damaged part added | — | 1. Tap the primary **Done** button at the bottom. | The Vehicle Part Details step is marked complete and the flow proceeds to the AI Processing screen. | ⬜ Not Run | |
| TC-BRE-020 | Photos tab shows a labeled grid of all captured photos | AC-BRE-20 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-020` | ≥1 zone photo has been captured | — | 1. Switch to the **Photos** tab. | A grid of thumbnail cards is shown, each labeled by its capture location (e.g. "Front Left"). | ⬜ Not Run | |

### 5. Damage Entry Form (Add / Edit)

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-021 | Adding a damaged part opens the damage-entry panel | AC-BRE-21 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-021` | User is on the Vehicle part details editor | — | 1. Tap **Add damaged part +** (or a car node). | A bottom sheet opens titled "Please enter damage details". | ⬜ Not Run | |
| TC-BRE-022 | Damage type supports selecting more than one type at once | AC-BRE-22, BR-BRE-03 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-022` | The damage-entry panel is open | Damage types: Crack, Dent, Scratch | 1. Select **Scratch**. 2. Also select **Dent**. | Both selected types are applied to the entry (shown later as "Scratch, Dent"), consistent with `AA`'s multi-select (`BR-AA-06`, regression of `TC-AA-048`/`TC-AA-062`). | ⬜ Not Run | |
| TC-BRE-023 | User sets damaged part, side 1 and side 2 | AC-BRE-23 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-023` | The damage-entry panel is open | Part: Backlight; Side 1: Rear; Side 2: Left | 1. Select **Damaged car part** (dropdown). 2. Select **Damaged side 1** (Front/Rear). 3. Select **Damaged side 2** (Left/Right). | The selections are set on the entry form. | ⬜ Not Run | |
| TC-BRE-024 | Edit mode offers Delete Part above the primary action | AC-BRE-24 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-024` | User opened the damage-entry panel via an existing entry's Edit icon | — | 1. View the panel. | Panel is titled "Edit damage details"; a **Delete Part** (red) button is shown above the primary **Save and update** button. | ⬜ Not Run | |
| TC-BRE-025 | Add / Save and update saves the entry to the damaged-parts list | AC-BRE-25 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🔴 Critical | 🔵 Pending | `@TC-BRE-025` | The damage-entry panel is filled with a valid type, part, side 1 and side 2 | Scratch, Backlight, Rear, Right | 1. Tap **Add** (or **Save and update** in edit mode). | The entry is saved and appears in the "List of damaged parts". | ⬜ Not Run | |

### 6. AI Processing

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-026 | AI Processing shows spinner, wait text, ad and progress bar | AC-BRE-26 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-026` | User has completed Vehicle Part Details | — | 1. Observe the AI Processing screen. | A loading spinner, the text "Please wait AI is processing to assess damages", a determinate progress bar and an Admin-configured ad banner are shown. | ⬜ Not Run | |
| TC-BRE-027 | Processing completion opens AI Estimated Repair Cost | AC-BRE-27 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-027` | The AI Processing progress bar reaches completion | — | 1. Wait for processing to finish. | User is navigated to the AI Estimated Repair Cost screen. | ⬜ Not Run | Assumption: transition trigger inferred from screen order, not stated by the ticket — see AC file Open Question 3 |

### 7. AI Estimated Repair Cost

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-028 | Assessment list groups results by part with an Edit action | AC-BRE-28 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-028` | AI processing has completed with ≥1 damaged part assessed | — | 1. View AI Estimated Repair Cost. 2. Tap **Edit** on a result group. | Results are grouped by part (e.g. "Front bumper") showing damage type, part, side 1, side 2; Edit reopens the damage-entry form for that entry. | ⬜ Not Run | |
| TC-BRE-029 | Bottom sticky bar shows total cost and the primary actions | AC-BRE-29 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🔴 Critical | 🔵 Pending | `@TC-BRE-029` | User is on the AI Estimated Repair Cost screen | — | 1. View the bottom of the screen. | A sticky bar shows the total estimated cost (e.g. "€345"), an **Add damage** secondary button and a **Done** primary button. | ⬜ Not Run | |
| TC-BRE-030 | "Add damage" lets the user add another damaged part before finishing | AC-BRE-30 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-030` | User is on the AI Estimated Repair Cost screen | — | 1. Tap **Add damage**. 2. Fill and save a new damage entry. | The user can add another damaged-part entry before completing the step. | ⬜ Not Run | |
| TC-BRE-031 | Done submits the rental images and opens the success screen | AC-BRE-31 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🔴 Critical | 🔵 Pending | `@TC-BRE-031` | User is on the AI Estimated Repair Cost screen | — | 1. Tap **Done**. | The success screen is shown: a car-in-circle icon and "Rental images have been submitted", subtitled "Please schedule so you can submit after rental images". | ⬜ Not Run | |

### 8. Submission Success & Scheduling

| TC ID | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC-BRE-032 | Selecting both rental dates shows the notification helper text | AC-BRE-32 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-032` | User is on the submission success screen with the Rental start date and Rental end date fields shown | Start: today; End: today + 3 days | 1. Select a Rental start date. 2. Select a Rental end date. | The helper text "ⓘ You will get notified on [Rental end date]" is shown, reflecting the selected end date. | ⬜ Not Run | |
| TC-BRE-033 | "Add event to my calendar" adds a native calendar event | AC-BRE-33 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟠 High | 🔵 Pending | `@TC-BRE-033` | Rental start and end dates are selected on the submission success screen | Start: today; End: today + 3 days | 1. Tap **Add event to my calendar**. | An event for the rental end date is added to the device's native calendar and the Event Added confirmation bottom sheet is shown. | ⬜ Not Run | |
| TC-BRE-034 | "Back to home" returns to the home page from the success screen | AC-BRE-34 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | ⚪ Low | 🔵 Pending | `@TC-BRE-034` | User is on the submission success screen | — | 1. Tap **Back to home** (secondary, light green). | User is navigated to the Home page. | ⬜ Not Run | |
| TC-BRE-035 | Event Added confirmation shows success details and returns home | AC-BRE-35 | [RC-127](https://motionscloud.atlassian.net/browse/RC-127) | 🟡 Medium | 🔵 Pending | `@TC-BRE-035` | The calendar event has just been added successfully | — | 1. View the confirmation bottom sheet. 2. Tap **Ok, back to home**. | A calendar-in-circle success icon, "Event added", "You will be notified on the rental end date" are shown; tapping the primary action navigates to the Home page. | ⬜ Not Run | |

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
