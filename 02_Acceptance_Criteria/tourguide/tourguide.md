# Acceptance Criteria — Tour Guide

| Field                  | Value                                   |
| ---------------------- | ---------------------------------------- |
| **Version**            | 1.0                                       |
| **Last updated**       | 2026-08-06                                |
| **Feature**            | Tour Guide                                |
| **SRS ref**            | [[01_SRS/tourguide/tourguide]]                     |
| **Jira tickets**       | `RC-49`                                   |
| **BA Owner**           | —                                         |
| **Reviewer (PO/Lead)** | —                                         |
| **Status**             | Draft                                     |

## User Story

**As a** first-time user of the web app (guest or logged in)
**I want** a guided walkthrough that highlights each available feature with a short hint popup
**So that** I can quickly discover what the app offers without having to explore it on my own

## Scenario-based AC — Given / When / Then

| AC ID        | Scenario                                                        | Jira                                              | Type      | Criticality | Given (context)                                                                                     | When (action / trigger)                              | Then (expected outcome)                                                                                                   | Linked TCs | Status |
| ------------ | ----------------------------------------------------------------- | -------------------------------------------------- | --------- | ----------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| AC-TG-01     | Tour guide auto-displays on first access (not logged in)          | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Happy     | 🔴 Critical | User is not logged in (guest)<br>And this is the user's first time accessing the web app               | User accesses (loads) the web app                        | The tour guide automatically displays<br>And it opens on the hint popup of the first non-login-required feature            | `TC-TG-001`, `TC-TG-012` | Draft  |
| AC-TG-02     | Tour guide auto-displays on first access (logged in)               | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Happy     | 🔴 Critical | User is logged in<br>And this is the user's first time accessing the web app                            | User accesses (loads) the web app                        | The tour guide automatically displays<br>And it opens on the hint popup of the first feature                                | `TC-TG-002` | Draft  |
| AC-TG-03     | Next button advances hint popup (guest, non-login features only)  | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Happy     | 🔴 Critical | Guest user's tour guide is open and showing a feature's hint popup<br>And more non-login-required features remain in the sequence | User taps/clicks **Next** on the current hint popup       | The current hint popup closes<br>And the hint popup of the next non-login-required feature is displayed                     | `TC-TG-003` | Draft  |
| AC-TG-04     | Next button advances hint popup (logged-in user, all features)    | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Happy     | 🔴 Critical | Logged-in user's tour guide is open and showing a feature's hint popup<br>And more features remain in the sequence | User taps/clicks **Next** on the current hint popup       | The current hint popup closes<br>And the hint popup of the next feature is displayed                                        | `TC-TG-004` | Draft  |
| AC-TG-05     | Tour guide stops after the last feature (logged in)                | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Happy     | 🟠 High     | Logged-in user's tour guide is open and showing the hint popup of the last feature in the sequence      | User taps/clicks **Next** on the last hint popup          | The tour guide closes<br>And no further hint popups are displayed<br>And the user is returned to normal app interaction     | `TC-TG-005` | Draft  |
| AC-TG-06     | Tour guide does not auto-display on second access (guest)          | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Alternate | 🟠 High     | Guest user has already completed (or previously triggered) the tour guide once                          | The same guest user accesses the web app again            | The tour guide does **not** automatically display                                                                            | `TC-TG-006` | Draft  |
| AC-TG-07     | Tour guide does not auto-display on second access (logged in)      | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Alternate | 🟠 High     | Logged-in user has already completed (or previously triggered) the tour guide once                      | The same logged-in user accesses the web app again         | The tour guide does **not** automatically display                                                                            | `TC-TG-007` | Draft  |
| AC-TG-08     | Guest manually replays tour guide via "Get tour guide" button      | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Alternate | 🟠 High     | Guest user is on the Menu screen<br>And the tour guide did not auto-display (already seen)               | User taps/clicks the **Get tour guide** button             | The tour guide displays again, starting from the first non-login-required feature's hint popup                              | `TC-TG-008` | Draft  |
| AC-TG-09     | Logged-in user manually replays tour guide                         | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Alternate | 🟠 High     | Logged-in user is in the app<br>And the tour guide did not auto-display (already seen)                   | User taps/clicks the **tour guide** button                 | The tour guide displays again, starting from the first feature's hint popup, covering all features                          | `TC-TG-009` | Draft  |
| AC-TG-10     | Login-required features are excluded from the guest tour sequence  | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Permission | 🔴 Critical | Guest user's tour guide is running<br>And the app contains at least one feature that requires login      | The tour guide progresses through its sequence of hint popups | No hint popup is ever displayed for a feature that requires login                                                            | `TC-TG-010` | Draft  |

## Business Rules (rule-based AC)

| Rule ID  | Business Rule                                                                                                      | Jira                                              | Rationale / Source                     | Criticality | Linked TCs | Status |
| -------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------- | ----------- | ---------- | ------ |
| BR-TG-01 | The tour guide auto-displays only on a user's first access to the web app; it must not auto-display on any subsequent access. | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Ticket: "will not automatically display when users access it for the second time" | 🔴 Critical | `TC-TG-006`, `TC-TG-007` | Draft  |
| BR-TG-02 | For a not-logged-in (guest) user, the tour guide sequence includes hint popups only for features that do not require login. | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Ticket: "only display for non-login feature" | 🔴 Critical | `TC-TG-010` | Draft  |
| BR-TG-03 | For a logged-in user, the tour guide sequence includes hint popups for all features.                              | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Ticket: "Show the hint popup of each feature (all features)" | 🔴 Critical | `TC-TG-011` | Draft  |
| BR-TG-04 | Regardless of whether the tour guide has already auto-displayed, the user can always manually re-trigger it via the tour guide button. | [RC-49](https://motionscloud.atlassian.net/browse/RC-49) | Ticket: "they can click on the tour guide button and show it again" | 🟠 High     | `TC-TG-008`, `TC-TG-009` | Draft  |

## Column Guide

| Column          | Description                                                       | Values / Format                                   |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------- |
| **AC ID**       | Unique scenario id — TCs trace back to this                      | `AC-TG-NN`                                  |
| **Rule ID**     | Unique business-rule id — TCs trace back to this                 | `BR-TG-NN`                                  |
| **Scenario**    | Short title of the behaviour, start with an action verb          | Plain text                                        |
| **Jira**        | The ticket this AC came from                                     | `[RC-49](url)`                                     |
| **Type**        | Class of scenario                                               | Happy / Alternate / Negative / Edge / Permission  |
| **Criticality** | Impact if this AC fails — drives the verifying TC's priority     | 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low          |
| **Given**       | Precondition / context true before the action                   | One state per clause; `<br>And …` to compound     |
| **When**        | The single action or event that triggers behaviour             | One trigger                                        |
| **Then**        | Observable, verifiable outcome — pass/fail must be objective    | Include error code / message / state where relevant |
| **Linked TCs**  | TCs in `03_Testcases/tourguide/tourguide.md` that verify this AC          | `TC-TG-NNN`, comma-separated                |
| **Status**      | Review state of the criterion                                   | Draft / Reviewed / Approved                        |

## Traceability

```
Jira ticket  ──▶  AC-TG-NN / BR-TG-NN  ──▶  TC-TG-NNN
 (the why)         (the what — this file)                  (the how to verify)
```

- **Upward**: header `SRS ref` + each row's `Jira` column link the AC to its source.
- **Downward**: the `Linked TCs` column lists the test cases that verify each AC.
- **Coverage rule**: every `Critical` and `High` AC and every business rule must have ≥1 Linked TC. Flag any such AC with zero TCs as a coverage gap. Conversely, every TC must name the `AC` it verifies — no orphan TCs.
