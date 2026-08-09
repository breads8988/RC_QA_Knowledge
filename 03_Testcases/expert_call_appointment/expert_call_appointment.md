# Test Case Register — Expert Call & Appointment (Find an Expert)

| Field                | Value                                   |
| -------------------- | --------------------------------------- |
| **Version**          | 1.0                                     |
| **Last updated**     | 2026-07-07                              |
| **Feature**          | Expert call & appointment / Find an Expert |
| **SRS ref**          | [[01_SRS/expert_call_appointment/]]     |
| **Jira tickets**     | `RC-112` (child of Epic `RC-101` — Web App) |
| **Owner**            | QC Team                                 |
| **Reviewer**         | TBD                                     |
| **Sprint / Release** | TBD                                     |

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 20        | 0         | 0      | 20      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 6        | 2    | 9      | 3   |

> Coverage % = Automated / Total × 100. Update after each sprint.

## Test Case Table

### 1. Entry & appointment-type selection

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-ECA-001 | Show appointment-type chooser on entering Find-an-Expert | AC-ECA-01 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟠 High | 🔵 Pending | `@TC-ECA-001` | User signed in, on Home page | — | 1. Open the "Experte für Fahrzeuggutachten" (Find an Expert) feature | A "Please choose an option" chooser is shown with **"Schedule a video call"** and **"Make an appointment"** options and a **Next** action | ⬜ Not Run | |
| TC-ECA-002 | List experts with "Get appointment" action (Make an appointment) | AC-ECA-02, BR-ECA-01 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🔴 Critical | 🔵 Pending | `@TC-ECA-002` | On the appointment-type chooser | Option = "Make an appointment" | 1. Select "Make an appointment" 2. Proceed with Next | Expert list is shown; each card displays name, workshop, address, distance, rating, and a **"Get appointment"** action | ⬜ Not Run | [DATA] ≥2 experts seeded |
| TC-ECA-003 | List experts with "Schedule a video call" action (distinct flow) | AC-ECA-02, BR-ECA-04 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🔴 Critical | 🔵 Pending | `@TC-ECA-003` | On the appointment-type chooser | Option = "Schedule a video call" | 1. Select "Schedule a video call" 2. Proceed with Next | Expert list is shown with a **"Schedule a video call"** action on each card; this action opens Calendly directly (no "Get appointment → Yes, contact me" contact prompt), so it is distinct from the appointment flow | ⬜ Not Run | [DATA] ≥2 experts seeded |

### 2. Expert list display, sorting & distance

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-ECA-004 | Experts listed nearest-first | AC-ECA-03 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | ⚪ Low | 🔵 Pending | `@TC-ECA-004` | Expert list reachable; ≥3 experts at different distances | Experts at 3.7 / 3.8 / 4.1 km | 1. Open the expert list 2. Observe the ordering | Experts are ordered by distance ascending (nearest first) | ⬜ Not Run | [DATA] |
| TC-ECA-005 | Distance measured from user's current location to workshop | BR-ECA-03 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-005` | Location permission granted; current location known | Known user coords + known workshop coords | 1. Open the expert list 2. Compare each card's distance to the map distance user→workshop | The distance on each card equals the map distance from the user's current location to that workshop | ⬜ Not Run | [DEP] geolocation |

### 3. Filtering

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-ECA-006 | Filter experts by minimum rating (integer-part matching) | AC-ECA-04, BR-ECA-02 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-006` | Expert list with mixed ratings; filter panel open | Rating filter = 4★; one expert rated 3.9 and one rated 4.0 | 1. Open the filter 2. Select minimum rating 4★ 3. Apply | Only experts whose **integer** rating ≥ 4 are listed — the 4.0 expert is shown; the 3.9 expert is excluded (rating matched by integer part, not rounded: 3.9 → 3★, 4.0 → 4★) | ⬜ Not Run | [DATA] |
| TC-ECA-007 | Filter experts by maximum distance | AC-ECA-05, BR-ECA-02 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-007` | Expert list with mixed distances; filter panel open | Distance = boundary values (min 0 km / max 100 km) | 1. Open the filter 2. Set a maximum distance on the slider 3. Apply | Only experts within the selected distance are listed | ⬜ Not Run | [DATA] BVA 0 & 100 km |
| TC-ECA-008 | Combine rating and distance filters | AC-ECA-06 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-008` | Filter panel open | Rating = 4★ AND distance ≤ 5 km | 1. Set both minimum rating and maximum distance 2. Apply | Only experts satisfying **both** constraints are listed | ⬜ Not Run | [DATA] |
| TC-ECA-009 | No experts match the filters (empty state) | AC-ECA-07 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-009` | Filter panel open | Rating = 5★ AND distance = 0 km (excludes all) | 1. Apply filters that no expert satisfies | A no-results / empty state is shown and no expert cards are listed | ⬜ Not Run | Empty-state UI pending — confirm design |

### 4. Make an appointment flow (Get appointment → Calendly)

> Flow: **Get appointment → "Yes, contact me" → open Calendly → schedule event → "Thank you" popup.**

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-ECA-010 | "Get appointment" opens contact-confirmation prompt | AC-ECA-08, BR-ECA-08 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🔴 Critical | 🔵 Pending | `@TC-ECA-010` | Expert list in "Make an appointment" mode | Expert = "John Doe" | 1. Tap "Get appointment" on an expert | A prompt "Did you want John Doe to contact you?" is shown with "Yes, contact me" and "No, I will check later" | ⬜ Not Run | |
| TC-ECA-011 | "Yes, contact me" opens the expert's Calendly | AC-ECA-09, BR-ECA-08 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🔴 Critical | 🔵 Pending | `@TC-ECA-011` | Contact-confirmation prompt shown | Expert = "John Doe" | 1. Select "Yes, contact me" | The expert's Calendly scheduling page opens so the user can pick a day and time | ⬜ Not Run | [DEP] Calendly |
| TC-ECA-012 | Decline contact request | AC-ECA-10 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-012` | Contact-confirmation prompt shown | — | 1. Select "No, I will check later" | The prompt closes, Calendly is not opened, and the user is returned to the expert list | ⬜ Not Run | |
| TC-ECA-013 | Schedule the appointment event → "Thank you" popup | AC-ECA-11, BR-ECA-06 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🔴 Critical | 🔵 Pending | `@TC-ECA-013` | Expert's Calendly open (after "Yes, contact me") | Name + Email; a free slot | 1. Select a day and time 2. Enter name and email 3. Confirm "Schedule Event" | The event is booked and a "Thank you" popup is shown confirming the appointment | ⬜ Not Run | [DEP] Calendly |

### 5. Schedule a video call flow (Calendly)

> Flow: **Schedule a video call → open Calendly → schedule event → "Thank you" popup.**

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-ECA-014 | "Schedule a video call" opens the expert's Calendly | AC-ECA-12, BR-ECA-05, BR-ECA-04 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🔴 Critical | 🔵 Pending | `@TC-ECA-014` | Expert list in "Schedule a video call" mode | Expert with its own Calendly link | 1. Tap "Schedule a video call" on an expert | The expert's **own** Calendly scheduling page opens so the user can pick a day and time (no intermediate contact prompt) | ⬜ Not Run | [DEP] Calendly |
| TC-ECA-015 | Schedule the video-call event → "Thank you" popup | AC-ECA-13, BR-ECA-06 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟠 High | 🔵 Pending | `@TC-ECA-015` | Expert's Calendly page open | Name + Email; a free 1-hr slot | 1. Select a day and time 2. Enter name and email 3. Confirm "Schedule Event" | The 1-hour video call is booked and a "Thank you" popup is shown confirming the appointment | ⬜ Not Run | [DEP] Calendly |
| TC-ECA-016 | Block scheduling when Name is empty | AC-ECA-14, BR-ECA-07 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-016` | Calendly "Enter Details" with day & time chosen | Name empty, Email valid | 1. Leave Name empty, enter Email 2. Attempt "Schedule Event" | The event is not scheduled and the missing Name field is indicated | ⬜ Not Run | [DEP] Calendly-side |
| TC-ECA-017 | Block scheduling when Email is empty | AC-ECA-14, BR-ECA-07 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-017` | Calendly "Enter Details" with day & time chosen | Name valid, Email empty | 1. Enter Name, leave Email empty 2. Attempt "Schedule Event" | The event is not scheduled and the missing Email field is indicated | ⬜ Not Run | [DEP] Calendly-side |
| TC-ECA-018 | Block scheduling on invalid email format | BR-ECA-07 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | ⚪ Low | 🔵 Pending | `@TC-ECA-018` | Calendly "Enter Details" with day & time chosen | Email = `abcd.xyz` (invalid) | 1. Enter Name and an invalid-format email 2. Attempt "Schedule Event" | The event is not scheduled and an invalid-email indication is shown | ⬜ Not Run | [DEP] Calendly-side |

### 6. Cross-cutting (responsive & resilience)

| TC ID        | Test Scenario | AC | Jira | Priority | Coverage | Cucumber Tag | Preconditions | Test Data | High-level Steps | Expected Result | Status | Note |
| ------------ | ------------- | -- | ---- | -------- | -------- | ------------ | ------------- | --------- | ---------------- | --------------- | ------ | ---- |
| TC-ECA-019 | Responsive layout on phone and tablet | AC-ECA-15 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | 🟡 Medium | 🔵 Pending | `@TC-ECA-019` | Find-an-Expert flow in the mobile web app | Phone + tablet breakpoints | 1. Open the expert flow on a phone 2. Open it on a tablet | Layout renders correctly and all cards, filters, and actions remain usable on both form factors | ⬜ Not Run | |
| TC-ECA-020 | Expert list load failure shows error state | AC-ECA-02 | [RC-112](https://motionscloud.atlassian.net/browse/RC-112) | ⚪ Low | 🔵 Pending | `@TC-ECA-020` | Expert-list API unavailable / times out | Simulated network failure | 1. Open the expert list while the API is failing | An error / retry state is shown instead of a blank or frozen screen | ⬜ Not Run | Error-state UI pending — confirm design [DEP] |

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
