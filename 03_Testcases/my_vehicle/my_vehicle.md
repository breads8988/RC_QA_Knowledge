# Test Case Register — My Vehicle

| Field                | Value                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------ |
| **Version**          | 1.1                                                                                        |
| **Last updated**     | 2026-07-04                                                                                 |
| **Feature**          | My Vehicle management                                                                       |
| **SRS ref**          | [[01_SRS/my_vehicle/]]                                                                      |
| **Jira tickets**     | `RC-109`, `RC-105` (under Epic [RC-101](https://motionscloud.atlassian.net/browse/RC-101)) |
| **Owner**            | QC Team                                                                                     |
| **Reviewer**         | <Lead name>                                                                                 |
| **Sprint / Release** | <Sprint X>                                                                                  |

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 15        | 0         | 0      | 15      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 4        | 6    | 4      | 1   |

> **Note:** Vehicle ownership (Owner / Rental, default Owner) is verified under the `registration` feature — see `03_Testcases/registration/registration.md` (AC-REG-35 / BR-REG-11). Not duplicated here.

## Test Case Table

### 1. Navigation & Empty State

| TC ID       | Test Scenario                          | AC        | Jira                                                       | Priority | Coverage   | Cucumber Tag    | Preconditions                                  | Test Data | High-level Steps                                                                 | Expected Result                                                                                     | Status    | Note |
| ----------- | -------------------------------------- | --------- | ---------------------------------------------------------- | -------- | ---------- | --------------- | ---------------------------------------------- | --------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-MV-001   | Open My Vehicle page from bottom menu   | AC-MV-01  | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🟠 High  | 🔵 Pending | `@TC-MV-001`    | User is logged in                              | —         | 1. Log in. 2. Tap "My Vehicle" in the bottom navigation.                         | The My Vehicle page opens and displays the user's vehicles or the empty state.                      | ⬜ Not Run |      |
| TC-MV-002   | Show empty state when no vehicles       | AC-MV-02  | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🟠 High  | 🔵 Pending | `@TC-MV-002`    | Logged-in user has no vehicle registered       | —         | 1. Open the My Vehicle page.                                                     | "No vehicle registered" message is shown and a "Register vehicle" call-to-action is displayed.      | ⬜ Not Run |      |

### 2. Register Vehicle — Happy Path

| TC ID       | Test Scenario                          | AC                     | Jira                                                       | Priority    | Coverage   | Cucumber Tag    | Preconditions                                        | Test Data                                            | High-level Steps                                                                                        | Expected Result                                                                                                              | Status    | Note |
| ----------- | -------------------------------------- | ---------------------- | ---------------------------------------------------------- | ----------- | ---------- | --------------- | ---------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-MV-003   | Register a vehicle by selecting Brand   | AC-MV-03, BR-MV-02     | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🔴 Critical | 🔵 Pending | `@TC-MV-003`    | User is logged in and has fewer than 4 vehicles      | Brand: Volkswagen → Atlas SEL Premium R-Line (2023)  | 1. Open the registration form. 2. Select a Brand (fields auto-fill). 3. Tap "Register".                 | Vehicle is saved and appears as a card in the My Vehicle list showing brand, model, year, no. of doors and no. of seats.     | ⬜ Not Run |      |
| TC-MV-004   | Brand selection auto-fills details      | AC-MV-05, BR-MV-03     | [RC-105](https://motionscloud.atlassian.net/browse/RC-105) | 🟠 High     | 🔵 Pending | `@TC-MV-004`    | User is on the registration form, no Brand selected  | Brand: Volkswagen                                    | 1. Open the registration form. 2. Select a Brand.                                                       | Model, Year, Vehicle type, Engine, No. of doors and No. of seats auto-populate with values belonging to the selected Brand. | ⬜ Not Run |      |
| TC-MV-005   | Override auto-filled data manually      | AC-MV-06               | [RC-105](https://motionscloud.atlassian.net/browse/RC-105) | 🟡 Medium   | 🔵 Pending | `@TC-MV-005`    | Registration form has a Brand selected & auto-filled | Edited model/year values                             | 1. Enable "Edit Manually". 2. Change one or more auto-filled fields. 3. Tap "Register".                 | The vehicle is registered with the manually edited values, not the original auto-filled ones.                               | ⬜ Not Run |      |

### 3. Register Vehicle — Validation & Business Rules

| TC ID       | Test Scenario                          | AC                     | Jira                                                       | Priority    | Coverage   | Cucumber Tag    | Preconditions                                  | Test Data          | High-level Steps                                                        | Expected Result                                                                                          | Status    | Note |
| ----------- | -------------------------------------- | ---------------------- | ---------------------------------------------------------- | ----------- | ---------- | --------------- | ---------------------------------------------- | ------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-MV-006   | Reject registration when Brand missing  | AC-MV-04, BR-MV-02     | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🔴 Critical | 🔵 Pending | `@TC-MV-006`    | User is on the registration form               | Brand: not selected | 1. Open the registration form. 2. Tap "Register" without selecting a Brand. | Registration is rejected, a validation message indicates Brand is required, and no vehicle is added.     | ⬜ Not Run |      |
| TC-MV-007   | Doors & seats limited to dropdown values | BR-MV-04             | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🟡 Medium   | 🔵 Pending | `@TC-MV-007`    | User is on the registration form               | —                  | 1. Open the No. of doors and No. of seats fields.                       | Values can only be chosen from the predefined dropdown options (auto-filled from Brand); no free text is accepted. | ⬜ Not Run |      |

### 4. Vehicle List & Management

| TC ID       | Test Scenario                          | AC        | Jira                                                       | Priority    | Coverage   | Cucumber Tag    | Preconditions                                       | Test Data | High-level Steps                                                                | Expected Result                                                                                          | Status    | Note |
| ----------- | -------------------------------------- | --------- | ---------------------------------------------------------- | ----------- | ---------- | --------------- | --------------------------------------------------- | --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- | --------- | ---- |
| TC-MV-008   | Display registered vehicles as cards    | AC-MV-07  | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🟠 High     | 🔵 Pending | `@TC-MV-008`    | User has ≥1 registered vehicle                      | —         | 1. Open the My Vehicle page.                                                    | Each vehicle is shown as a card with brand, model + variant, year, no. of doors, no. of seats and a ⋮ menu. | ⬜ Not Run |      |
| TC-MV-009   | Edit a registered vehicle               | AC-MV-08  | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🟠 High     | 🔵 Pending | `@TC-MV-009`    | User has ≥1 registered vehicle                      | New year value | 1. Open a vehicle's ⋮ menu. 2. Select "Edit Vehicle". 3. Change a field. 4. Save. | The vehicle's details are updated and the card reflects the new values (all fields are editable).        | ⬜ Not Run |      |
| TC-MV-010   | Remove a vehicle (no confirmation)      | AC-MV-09  | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🔴 Critical | 🔵 Pending | `@TC-MV-010`    | User has ≥2 registered vehicles                     | —         | 1. Open a vehicle's ⋮ menu. 2. Select "Remove Vehicle".                          | The vehicle is removed from the list immediately with no confirmation prompt.                            | ⬜ Not Run |      |
| TC-MV-011   | Remove the last vehicle → empty state   | AC-MV-09, AC-MV-02 | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🟡 Medium | 🔵 Pending | `@TC-MV-011`  | User has exactly 1 registered vehicle               | —         | 1. Open the vehicle's ⋮ menu. 2. Select "Remove Vehicle".                        | The vehicle is removed and the "No vehicle registered" empty state with the Register CTA is shown.       | ⬜ Not Run |      |
| TC-MV-012   | Cancel the vehicle options menu         | AC-MV-10  | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | ⚪ Low       | 🔵 Pending | `@TC-MV-012`    | The vehicle options action sheet is open            | —         | 1. Open a vehicle's ⋮ menu. 2. Select "Cancel".                                  | The action sheet closes and no change is made to the vehicle.                                            | ⬜ Not Run |      |

### 5. Maximum Vehicle Limit

| TC ID       | Test Scenario                          | AC                 | Jira                                                       | Priority    | Coverage   | Cucumber Tag    | Preconditions                                  | Test Data | High-level Steps                                                        | Expected Result                                                                                                            | Status    | Note   |
| ----------- | -------------------------------------- | ------------------ | ---------------------------------------------------------- | ----------- | ---------- | --------------- | ---------------------------------------------- | --------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | --------- | ------ |
| TC-MV-013   | Register the 4th vehicle (at limit)     | BR-MV-01           | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🟠 High     | 🔵 Pending | `@TC-MV-013`    | User has exactly 3 registered vehicles          | 4th vehicle data | 1. Open the registration form. 2. Register a 4th vehicle.               | The 4th vehicle is accepted and added to the list (boundary — up to 4 is allowed).                                         | ⬜ Not Run | [DATA] |
| TC-MV-014   | Block adding a 5th vehicle (over limit)  | AC-MV-11, BR-MV-01 | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | 🔴 Critical | 🔵 Pending | `@TC-MV-014`    | User already has 4 registered vehicles (max)    | 5th vehicle data | 1. Attempt to register another vehicle.                                | Limit notice is shown ("…you can only add up to 4 vehicles… contact John@repaircheck.de") and no new vehicle is added.     | ⬜ Not Run | [DATA] |

### 6. UI / Regression

| TC ID       | Test Scenario                          | AC        | Jira                                                       | Priority  | Coverage   | Cucumber Tag    | Preconditions                                  | Test Data | High-level Steps                                                        | Expected Result                                                                                          | Status    | Note                       |
| ----------- | -------------------------------------- | --------- | ---------------------------------------------------------- | --------- | ---------- | --------------- | ---------------------------------------------- | --------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------- | -------------------------- |
| TC-MV-015   | Brand/Model search boxes render legibly | AC-MV-12  | [RC-105](https://motionscloud.atlassian.net/browse/RC-105) | 🟡 Medium | 🔵 Pending | `@TC-MV-015`    | User is on the vehicle registration form       | —         | 1. Open the "Brand" search selector. 2. Open the "Model" search selector. | Each search box is large enough to show the input and results legibly (regression of the RC-105 styling defect). | ⬜ Not Run | [BUG] RC-105 regression    |

## Gherkin Mapping (Automated TCs only)

> Add scenarios here as automation is implemented. The TC ID tag is mandatory for result tracing.

## Note Tag Reference

| Tag       | Meaning                                                            |
| --------- | ------------------------------------------------------------------ |
| `[FLAKY]` | Unstable — fails intermittently on CI. Check logs before rerunning |
| `[BUG]`   | Blocked by / verifying an open bug — include ticket ID            |
| `[DEP]`   | Depends on specific env, mock service, fixture, or config          |
| `[SKIP]`  | Temporarily skipped — include reason and owner                     |
| `[DATA]`  | Requires complex or manual data setup                              |
