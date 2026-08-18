---
type: tc
feature: "[[tourguide]]"
code: TG
jira: [RC-49]
version: 1.0
updated: 2026-08-06
owner: QC Team
reviewer: 
sprint: 
tc_total: 12
tc_automated: 0
tc_pending: 12
status: Draft
---

# Test Case Register — Tour Guide (`TG`)

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 12        | 0         | 0      | 12      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 5        | 6    | 1      | 0   |

## Test Case Table

### 1. Happy Path — Auto-display on first access

| TC ID          | Test Scenario | AC        | Jira                                              | Priority    | Coverage   | Cucumber Tag      | Preconditions                                                            | Test Data                                             | High-level Steps                                                                                                   | Expected Result                                                                                                   | Status    | Note |
| -------------- | ------------- | --------- | -------------------------------------------------- | ----------- | ---------- | ------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-TG-001 | Tour guide auto-displays on first access for a guest user | AC-TG-01 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🔴 Critical | 🔵 Pending | `@TC-TG-001` | Guest (not logged in) user; this browser/device has never opened the web app before | Non-login features available: Clever tanken, Parkplatz Suche | 1. Open the web app as a guest for the first time<br>2. Observe the screen shown | The tour guide displays automatically<br>And the hint popup shown is for the first non-login feature (e.g. Clever tanken) | ⬜ Not Run |      |
| TC-TG-002 | Tour guide auto-displays on first access for a logged-in user | AC-TG-02 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🔴 Critical | 🔵 Pending | `@TC-TG-002` | Logged-in user; this account has never opened the web app before | Full feature set (login-required + non-login features) | 1. Log in and open the web app for the first time<br>2. Observe the screen shown | The tour guide displays automatically<br>And the hint popup shown is for the first feature in the sequence | ⬜ Not Run |      |
| TC-TG-012 | Hint popup shows the correct guide content and highlights the right feature | AC-TG-01 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🟡 Medium | 🔵 Pending | `@TC-TG-012` | Tour guide is open and displaying the hint popup for a given feature | Feature: Clever tanken | 1. Trigger the tour guide (auto or manual)<br>2. Inspect the hint popup shown for the current feature | The popup visually associates with the correct feature tile<br>And shows the guide message text and a **Next** action | ⬜ Not Run | UI ref: `01_Features/tourguide/screens/Screenshot 2026-08-06 at 09.56.16.png` |

### 2. Happy Path — Navigation (Next button)

| TC ID          | Test Scenario | AC        | Jira                                              | Priority    | Coverage   | Cucumber Tag      | Preconditions                                                            | Test Data                                             | High-level Steps                                                                                                   | Expected Result                                                                                                   | Status    | Note |
| -------------- | ------------- | --------- | -------------------------------------------------- | ----------- | ---------- | ------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-TG-003 | Next advances the guest tour to the next non-login feature | AC-TG-03 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🔴 Critical | 🔵 Pending | `@TC-TG-003` | Guest user's tour guide is open on the hint popup for "Clever tanken"; "Parkplatz Suche" is next in sequence | Non-login features: Clever tanken → Parkplatz Suche | 1. With the tour guide open on the current feature's popup, tap **Next** | The current popup closes<br>And the hint popup for "Parkplatz Suche" (next non-login feature) is displayed | ⬜ Not Run |      |
| TC-TG-004 | Next advances the logged-in tour to the next feature | AC-TG-04 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🔴 Critical | 🔵 Pending | `@TC-TG-004` | Logged-in user's tour guide is open on the hint popup for the current feature; another feature is next in sequence | Full feature set | 1. With the tour guide open on the current feature's popup, tap **Next** | The current popup closes<br>And the hint popup for the next feature in the sequence is displayed | ⬜ Not Run |      |
| TC-TG-005 | Tour guide closes after the last feature (logged in) | AC-TG-05 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🟠 High | 🔵 Pending | `@TC-TG-005` | Logged-in user's tour guide is open on the hint popup for the **last** feature in the sequence | Full feature set | 1. With the tour guide open on the last feature's popup, tap **Next** | The tour guide closes<br>And no further hint popup is shown<br>And the user can interact with the app normally | ⬜ Not Run |      |
| TC-TG-011 | Logged-in tour guide sequence covers every feature exactly once | BR-TG-03 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🟠 High | 🔵 Pending | `@TC-TG-011` | Logged-in user's tour guide is open at the first feature's popup | Full feature set | 1. Tap **Next** repeatedly until the tour guide closes<br>2. Record every feature whose hint popup was shown | Every feature in the app's feature set had its hint popup displayed exactly once, with no repeats and no omissions | ⬜ Not Run |      |

### 3. Repeat Visit — No auto re-display

| TC ID          | Test Scenario | AC        | Jira                                              | Priority    | Coverage   | Cucumber Tag      | Preconditions                                                            | Test Data                                             | High-level Steps                                                                                                   | Expected Result                                                                                                   | Status    | Note |
| -------------- | ------------- | --------- | -------------------------------------------------- | ----------- | ---------- | ------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-TG-006 | Tour guide does not auto-display on a guest's second visit | AC-TG-06 / BR-TG-01 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🟠 High | 🔵 Pending | `@TC-TG-006` | Guest user has already had the tour guide auto-display (or manually triggered it) once on this browser/device | — | 1. Close and reopen the web app as the same guest (same browser/device)<br>2. Observe the screen shown | The tour guide does **not** automatically display | ⬜ Not Run |      |
| TC-TG-007 | Tour guide does not auto-display on a logged-in user's second visit | AC-TG-07 / BR-TG-01 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🟠 High | 🔵 Pending | `@TC-TG-007` | Logged-in user has already had the tour guide auto-display (or manually triggered it) once | — | 1. Log out and log back in (or reopen the app) as the same user<br>2. Observe the screen shown | The tour guide does **not** automatically display | ⬜ Not Run |      |

### 4. Manual Replay

| TC ID          | Test Scenario | AC        | Jira                                              | Priority    | Coverage   | Cucumber Tag      | Preconditions                                                            | Test Data                                             | High-level Steps                                                                                                   | Expected Result                                                                                                   | Status    | Note |
| -------------- | ------------- | --------- | -------------------------------------------------- | ----------- | ---------- | ------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-TG-008 | Guest can manually replay the tour guide from the Menu screen | AC-TG-08 / BR-TG-04 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🟠 High | 🔵 Pending | `@TC-TG-008` | Guest user is on the Menu screen; tour guide already seen (not auto-displaying) | — | 1. Navigate to the Menu screen<br>2. Tap the **Get tour guide** bar | The tour guide displays again, starting from the hint popup of the first non-login feature | ⬜ Not Run | UI ref: `01_Features/tourguide/screens/Screenshot 2026-08-06 at 09.56.27.png` |
| TC-TG-009 | Logged-in user can manually replay the tour guide | AC-TG-09 / BR-TG-04 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🟠 High | 🔵 Pending | `@TC-TG-009` | Logged-in user is in the app; tour guide already seen (not auto-displaying) | — | 1. Tap the **tour guide** entry point | The tour guide displays again, starting from the hint popup of the first feature, covering all features | ⬜ Not Run | Entry point for logged-in users not shown in provided screenshots — location TBC |

### 5. Permission — Feature scope by login state

| TC ID          | Test Scenario | AC        | Jira                                              | Priority    | Coverage   | Cucumber Tag      | Preconditions                                                            | Test Data                                             | High-level Steps                                                                                                   | Expected Result                                                                                                   | Status    | Note |
| -------------- | ------------- | --------- | -------------------------------------------------- | ----------- | ---------- | ------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-TG-010 | Guest tour guide never shows a hint popup for a login-required feature | AC-TG-10 / BR-TG-02 | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | 🔴 Critical | 🔵 Pending | `@TC-TG-010` | Guest user; app contains ≥1 feature that requires login | Login-required feature(s) present in the app's feature set | 1. Trigger the guest tour guide (auto or manual)<br>2. Tap **Next** through the entire sequence<br>3. Record every feature shown | No hint popup is displayed for any feature that requires login | ⬜ Not Run |      |

## Gherkin Mapping (Automated TCs only)

> No TCs are automated yet — all 12 are 🔵 Pending. Add `.feature` scenarios here as automation is implemented.
