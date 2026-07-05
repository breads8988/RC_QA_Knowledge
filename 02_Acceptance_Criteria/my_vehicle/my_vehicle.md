# Acceptance Criteria — My Vehicle

| Field                  | Value                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| **Version**            | 1.1                                                                                           |
| **Last updated**       | 2026-07-04                                                                                    |
| **Feature**            | My Vehicle management                                                                          |
| **SRS ref**            | [[01_SRS/my_vehicle/]]                                                                         |
| **Jira tickets**       | `RC-109`, `RC-105` (under Epic [RC-101](https://motionscloud.atlassian.net/browse/RC-101))    |
| **BA Owner**           | anhvu51                                                                                        |
| **Reviewer (PO/Lead)** | <name>                                                                                         |
| **Status**             | Draft                                                                                          |

## User Story

**As a** registered Repair Check app user
**I want** to register my vehicle(s) and view, edit, and remove them from a "My Vehicle" page
**So that** my vehicle details are available for accident-assistance, repair, and expert-matching flows

> **Note:** the vehicle registration form (Brand → auto-filled details) is shared with the onboarding **registration** feature. The **Vehicle ownership (Owner / Rental)** field is documented under registration ([AC-REG-35 / BR-REG-11](../registration/registration.md)) — default "Owner" — and is intentionally **not** duplicated here.

---

## Scenario-based AC — Given / When / Then

> One row = one scenario. Sourced from the Figma design (`01_SRS/my_vehicle/figma`) as RC-109 / RC-105 carry no detailed spec of their own. Fields observed in German are noted with an English gloss.

| AC ID        | Scenario                              | Jira                                                        | Type       | Criticality | Given (context)                                                                                   | When (action / trigger)                                                     | Then (expected outcome)                                                                                                                       | Linked TCs               | Status |
| ------------ | ------------------------------------- | ---------------------------------------------------------- | ---------- | ----------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------ |
| AC-MV-01     | Open My Vehicle page                   | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Happy      | 🟠 High     | The user is logged in and on any main screen                                                       | The user selects "My Vehicle" from the bottom navigation menu               | The My Vehicle page opens and shows the user's current vehicles (or the empty state)                                                          | `TC-MV-001`              | Draft  |
| AC-MV-02     | Empty state — no vehicle registered    | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Alternate  | 🟠 High     | The logged-in user has no vehicle registered                                                       | The user opens the My Vehicle page                                          | The page shows a "No vehicle registered" message<br>And a "Register vehicle" call-to-action is displayed                                       | `TC-MV-002`, `TC-MV-011` | Draft  |
| AC-MV-03     | Register a vehicle (happy path)        | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Happy      | 🔴 Critical | The user is on the vehicle registration form and has fewer than 4 vehicles registered              | The user selects a Brand (which auto-populates Model, Year, Vehicle type, Engine, No. of doors and No. of seats) and confirms "Register" | The vehicle is saved and appears as a card in the My Vehicle list showing brand, model, year, no. of doors and no. of seats                    | `TC-MV-003`              | Draft  |
| AC-MV-04     | Register — Brand not selected          | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Negative   | 🔴 Critical | The user is on the vehicle registration form                                                       | The user submits "Register" without selecting a Brand                       | Registration is rejected<br>And a validation message indicates Brand is required<br>And no vehicle is added to the list                        | `TC-MV-006`              | Draft  |
| AC-MV-05     | Selecting Brand auto-fills details     | [RC-105](https://motionscloud.atlassian.net/browse/RC-105) | Happy      | 🟠 High     | The user is on the vehicle registration form with no Brand selected                                 | The user selects a Brand                                                    | The Model, Year, Vehicle type, Engine, No. of doors and No. of seats fields are auto-populated with that Brand's data from the predefined lists | `TC-MV-004`              | Draft  |
| AC-MV-06     | Override values via "Edit Manually"    | [RC-105](https://motionscloud.atlassian.net/browse/RC-105) | Alternate  | 🟡 Medium   | The user is on the vehicle registration form with a Brand selected and fields auto-filled            | The user enables "Edit Manually" and changes the vehicle details by hand    | The user can override the auto-filled details manually and register the vehicle with the edited values                                          | `TC-MV-005`              | Draft  |
| AC-MV-07     | View registered vehicle list           | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Happy      | 🟠 High     | The user has one or more registered vehicles                                                        | The user opens the My Vehicle page                                          | Each vehicle is shown as a card with its brand, model + variant, year, no. of doors and no. of seats, and a per-card options (⋮) menu          | `TC-MV-008`              | Draft  |
| AC-MV-08     | Edit a vehicle                         | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Happy      | 🟠 High     | The user has a registered vehicle                                                                   | The user opens the vehicle's ⋮ menu and selects "Edit Vehicle" (same fields as registration, all editable), updates a field, and saves | The vehicle's details are updated and the card reflects the new values                                                                        | `TC-MV-009`              | Draft  |
| AC-MV-09     | Remove a vehicle                       | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Happy      | 🔴 Critical | The user has a registered vehicle                                                                   | The user opens the vehicle's ⋮ menu and selects "Remove Vehicle"           | The vehicle is removed immediately from the My Vehicle list with no confirmation prompt<br>And if it was the last vehicle, the empty state (AC-MV-02) is shown | `TC-MV-010`, `TC-MV-011` | Draft  |
| AC-MV-10     | Dismiss the options menu               | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Alternate  | ⚪ Low       | The vehicle options action sheet (Edit / Remove / Cancel) is open                                   | The user selects "Cancel"                                                   | The action sheet closes and no change is made to the vehicle                                                                                  | `TC-MV-012`              | Draft  |
| AC-MV-11     | Add beyond the maximum vehicle limit   | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Negative   | 🔴 Critical | The user already has 4 vehicles registered (the maximum)                                            | The user attempts to register another vehicle                              | A limit notice is shown ("…you have exceeded the limit. You can only add up to 4 vehicles… please contact John@repaircheck.de")<br>And no new vehicle is added | `TC-MV-014`              | Draft  |
| AC-MV-12     | Registration form fields are usable    | [RC-105](https://motionscloud.atlassian.net/browse/RC-105) | Edge       | 🟡 Medium   | The user is on the vehicle registration form                                                        | The user opens the "Brand" / "Model" search selectors                       | Each search box is large enough to display the search input and results legibly (regression of the RC-105 styling defect)                      | `TC-MV-015`              | Draft  |

## Business Rules (rule-based AC)

> For constraints, policies, limits, permissions — things that govern many scenarios.

| Rule ID      | Business Rule                                                                                                                       | Jira                                                       | Rationale / Source                                | Criticality | Linked TCs               | Status |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------- | ----------- | ------------------------ | ------ |
| BR-MV-01     | A user may register at most **4** vehicles. Beyond 4, adding is blocked with the "exceeded the limit… contact John@repaircheck.de" notice. | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Figma "exceeded the limit" modal (limit confirmed = 4) | 🔴 Critical | `TC-MV-013`, `TC-MV-014` | Draft  |
| BR-MV-02     | **Brand** is the only required field to register. Selecting a Brand auto-populates Model, Year (Baujahr), Vehicle type (Fahrzeugtyp), Engine (Motor), No. of doors and No. of seats. | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Figma registration form (confirmed)               | 🔴 Critical | `TC-MV-003`, `TC-MV-006` | Draft  |
| BR-MV-03     | The Model and dependent fields are constrained to values belonging to the selected Brand (cascading dependency).                     | [RC-105](https://motionscloud.atlassian.net/browse/RC-105) | Figma Brand→Model dependency                       | 🟡 Medium   | `TC-MV-004`              | Draft  |
| BR-MV-04     | No. of doors and No. of seats are chosen from predefined dropdown values (auto-filled from the selected Brand), not free-typed.      | [RC-109](https://motionscloud.atlassian.net/browse/RC-109) | Figma dropdown fields (confirmed)                 | 🟡 Medium   | `TC-MV-007`              | Draft  |

## Traceability

```
Jira RC-101 (Epic) ─▶ RC-109 / RC-105 ─▶ AC-MV-NN / BR-MV-NN ─▶ TC-MV-NNN
```

- **Upward**: header `SRS ref` + each row's `Jira` column link the AC to its source ticket.
- **Downward**: `Linked TCs` lists the verifying test cases in `03_Testcases/my_vehicle/my_vehicle.md`.
- **Coverage rule**: every Critical/High AC and every business rule needs ≥1 Linked TC.
- **Cross-feature**: Vehicle ownership (Owner/Rental) is owned by the `registration` feature (AC-REG-35 / BR-REG-11), not repeated here.
