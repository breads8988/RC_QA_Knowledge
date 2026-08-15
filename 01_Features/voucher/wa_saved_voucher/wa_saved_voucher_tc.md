---
type: tc
feature: "[[wa_saved_voucher]]"
code: SV
jira: [RC-65]
version: 1.0
updated: 2026-08-06
owner: QC Team
reviewer: 
sprint: 
tc_total: 10
tc_automated: 0
tc_pending: 10
status: Draft
---

# Test Case Register — Saved Voucher (`SV`)

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 10        | 0         | 0      | 10      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 2        | 5    | 2      | 1   |

> Coverage % = Automated / Total × 100. Update after each sprint.

## Test Case Table

### 1. Happy Path

| TC ID        | Test Scenario                                                | AC        | Jira                                                    | Priority    | Coverage   | Cucumber Tag       | Preconditions                                                                                          | Test Data                                                                                                          | High-level Steps                                                                                                   | Expected Result                                                                                                                                        | Status    | Note |
| ------------ | -------------------------------------------------------------- | --------- | -------------------------------------------------------- | ----------- | ---------- | ------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-SV-001    | Open Saved Vouchers page and view the default "All" voucher list | AC-SV-01  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🔴 Critical | 🔵 Pending | `@TC-SV-001` | User is logged in and has saved 2 vouchers via **Save voucher** on the Workshop page (one regular, one specialized) | Voucher A: Jackel Gmbh, Workshop, 10% OFF, code `ADSGDISL`, Use by 10 Oct 2023. Voucher B: Riparo Workshops, Specialized werkstatt, 10% OFF, code `VKKGW1SL`, Use by 10 Oct 2023 | 1. Log in as the user.<br>2. Open the menu and select **Saved vouchers**.<br>3. Observe the page's default filter and each listed card.                       | Saved Vouchers page opens with the **All** tab selected by default<br>And both vouchers are shown as cards with workshop name, type badge, discount %, code, expiry date, and a **View Details** action | ⬜ Not Run |      |
| TC-SV-002    | View a saved voucher's details                                  | AC-SV-05  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🟠 High     | 🔵 Pending | `@TC-SV-002` | User is on the Saved Vouchers page with ≥1 voucher listed                                              | Riparo Workshops, code `VKKGW1SL`, 10% OFF, Use by 10 Oct 2023                                                        | 1. Open the Saved Vouchers page.<br>2. Tap **View Details** on a voucher card.<br>3. Inspect the detail view.                                                  | A small popup panel opens anchored to the bottom of the screen, showing the workshop name, discount, redemption code, and expiry date matching the selected voucher card | ⬜ Not Run |      |

### 2. Filtering

| TC ID        | Test Scenario                                                | AC                    | Jira                                                    | Priority    | Coverage   | Cucumber Tag       | Preconditions                                                                                          | Test Data                                                                                                          | High-level Steps                                                                                                   | Expected Result                                                                                                                                        | Status    | Note |
| ------------ | -------------------------------------------------------------- | ---------------------- | -------------------------------------------------------- | ----------- | ---------- | ------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-SV-003    | Filter by "Workshop" shows only regular-workshop vouchers        | AC-SV-02, BR-SV-02      | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🟠 High     | 🔵 Pending | `@TC-SV-003` | User has vouchers saved from both a regular workshop and a specialized workshop                        | Voucher A: Jackel Gmbh (Workshop). Voucher B: Riparo Workshops (Specialized werkstatt)                                | 1. Open the Saved Vouchers page (All tab).<br>2. Select the **Workshop** filter tab.<br>3. Inspect the resulting list.                                        | Only the regular-workshop voucher (Jackel Gmbh) is shown<br>And the specialized-workshop voucher (Riparo Workshops) is hidden                              | ⬜ Not Run |      |
| TC-SV-004    | Filter by "Special workshop" shows only specialized-workshop vouchers | AC-SV-03, BR-SV-02 | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🟠 High     | 🔵 Pending | `@TC-SV-004` | User has vouchers saved from both a regular workshop and a specialized workshop                        | Voucher A: Jackel Gmbh (Workshop). Voucher B: Riparo Workshops (Specialized werkstatt)                                | 1. Open the Saved Vouchers page (All tab).<br>2. Select the **Special workshop** filter tab.<br>3. Inspect the resulting list.                                | Only the specialized-workshop voucher (Riparo Workshops) is shown<br>And the regular-workshop voucher (Jackel Gmbh) is hidden                              | ⬜ Not Run |      |
| TC-SV-005    | Selecting a filter tab with no matching vouchers shows a blank list, not an empty-state message | BR-SV-04  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | ⚪ Low       | 🔵 Pending | `@TC-SV-005` | User has saved vouchers from regular workshops only (none from a specialized workshop)                 | Voucher A: Jackel Gmbh (Workshop) only                                                                                | 1. Open the Saved Vouchers page.<br>2. Select the **Special workshop** filter tab.<br>3. Observe the result.                                                   | The list area shows no voucher cards<br>And no empty-state message is displayed (blank list area) — distinct from the global empty state in TC-SV-006, which does show a message | ⬜ Not Run |      |

### 3. Empty State

| TC ID        | Test Scenario                              | AC        | Jira                                                    | Priority    | Coverage   | Cucumber Tag       | Preconditions                                       | Test Data | High-level Steps                                                              | Expected Result                                                                                     | Status    | Note |
| ------------ | --------------------------------------------- | --------- | -------------------------------------------------------- | ----------- | ---------- | ------------------- | ---------------------------------------------------- | --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | --------- | ---- |
| TC-SV-006    | Saved Vouchers page shows empty state when no vouchers are saved | AC-SV-04  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🟡 Medium   | 🔵 Pending | `@TC-SV-006` | Logged-in user has never saved a voucher              | —         | 1. Log in as a user with no saved vouchers.<br>2. Open the Saved Vouchers page. | An empty-state message is shown indicating no vouchers have been saved yet<br>And no voucher cards are displayed | ⬜ Not Run |      |

### 4. Permission & Data Security

| TC ID        | Test Scenario                                                    | AC        | Jira                                                    | Priority    | Coverage   | Cucumber Tag       | Preconditions                                                                        | Test Data                                                        | High-level Steps                                                                                                       | Expected Result                                                                                                          | Status    | Note |
| ------------ | -------------------------------------------------------------------- | --------- | -------------------------------------------------------- | ----------- | ---------- | ------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------- | ---- |
| TC-SV-007    | Unauthenticated user cannot access the Saved Vouchers page             | AC-SV-06  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🔴 Critical | 🔵 Pending | `@TC-SV-007` | User is logged out                                                                        | —                                                                    | 1. While logged out, attempt to open the Saved Vouchers page (via menu or direct route).<br>2. Observe the result.               | No saved voucher list is displayed<br>And the user is redirected/forced to the login screen                                                    | ⬜ Not Run |      |
| TC-SV-008    | A user's saved vouchers are not visible on another user's Saved Vouchers page | BR-SV-01  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🟠 High     | 🔵 Pending | `@TC-SV-008` | User A has saved 1 voucher; User B is a separate account with no saved vouchers            | User A: Jackel Gmbh, code `ADSGDISL`. User B: no saved vouchers        | 1. Log in as User A and confirm the voucher is listed.<br>2. Log out.<br>3. Log in as User B and open Saved Vouchers.            | User B's Saved Vouchers page does not show User A's voucher<br>And User B sees only their own (empty) list                        | ⬜ Not Run |      |

### 5. Cross-feature Integration / Regression

| TC ID        | Test Scenario                                                        | AC        | Jira                                                    | Priority    | Coverage   | Cucumber Tag       | Preconditions                                                                              | Test Data                                    | High-level Steps                                                                                                          | Expected Result                                                                                                                              | Status    | Note |
| ------------ | ------------------------------------------------------------------------ | --------- | -------------------------------------------------------- | ----------- | ---------- | ------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-SV-009    | Saving a voucher on the Workshop page makes it appear on the Saved Vouchers page | BR-SV-01  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🟠 High     | 🔵 Pending | `@TC-SV-009` | User is logged in, viewing a workshop's voucher redemption panel on the Workshop page, voucher not yet saved | Riparo Workshops voucher, code `VKKGW1SL`       | 1. On the Workshop page, tap **Save voucher** for the workshop's voucher.<br>2. Open the menu and navigate to **Saved vouchers**. | The voucher appears in the Saved Vouchers list with the matching workshop name, code, and expiry date                                                | ⬜ Not Run | Cross-references `TC-WS-009` in feature `WS` (`wa_workshop`) |
| TC-SV-010    | An expired saved voucher remains visible in the Saved Vouchers list | BR-SV-03  | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | 🟡 Medium   | 🔵 Pending | `@TC-SV-010` | User has a saved voucher whose expiry date ("Use by") has already passed                    | Jackel Gmbh voucher, code `ADSGDISL`, Use by a past date | 1. Log in as the user.<br>2. Open the Saved Vouchers page.<br>3. Locate the expired voucher's card.                               | The expired voucher's card is still displayed in the list, with the same fields as a non-expired voucher (no "Expired" badge, not hidden) | ⬜ Not Run | Contrasts with `TC-WS-015` in feature `WS` (`wa_workshop`) (Workshop page *does* hide expired vouchers) |

## Gherkin Mapping (Automated TCs only)

> No TCs are automated yet — add scenarios here as automation is implemented.

## Note Tag Reference

| Tag       | Meaning                                                            |
| --------- | ------------------------------------------------------------------ |
| `[FLAKY]` | Unstable — fails intermittently on CI. Check logs before rerunning |
| `[BUG]`   | Blocked by open bug — include ticket ID                            |
| `[DEP]`   | Depends on specific env, mock service, fixture, or config          |
| `[SKIP]`  | Temporarily skipped — include reason and owner                     |
| `[DATA]`  | Requires complex or manual data setup                              |
| `[GAP]`   | Requirement/AC did not specify this case — flagged assumption, confirm with BA/stakeholder |
