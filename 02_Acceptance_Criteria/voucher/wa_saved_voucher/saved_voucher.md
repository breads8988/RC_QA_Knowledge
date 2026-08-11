# Acceptance Criteria — Saved Voucher

| Field                  | Value                                   |
| ---------------------- | ---------------------------------------- |
| **Version**            | 1.0                                       |
| **Last updated**       | 2026-08-06                                |
| **Feature**            | Saved Voucher page                        |
| **SRS ref**            | [[01_SRS/saved_voucher/]]                 |
| **Jira tickets**       | `RC-65`                                   |
| **BA Owner**           | —                                         |
| **Reviewer (PO/Lead)** | —                                         |
| **Status**             | Draft                                     |

## User Story

**As a** vehicle owner who has saved discount vouchers from workshops
**I want** to view and filter all my saved vouchers in one place and see each one's details
**So that** I can easily find and use the right saved voucher when I visit a workshop

## Scenario-based AC — Given / When / Then

| AC ID     | Scenario                                                    | Jira                                                    | Type       | Criticality | Given (context)                                                                                       | When (action / trigger)                                  | Then (expected outcome)                                                                                                                                                                                                              | Linked TCs | Status |
| --------- | ------------------------------------------------------------ | -------------------------------------------------------- | ---------- | ----------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ |
| AC-SV-01  | Opening Saved Vouchers from the menu shows all saved vouchers | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Happy      | 🔴 Critical | A logged-in user has saved one or more vouchers via **Save voucher** on the Workshop page                | User selects **Saved vouchers** from the menu                | The Saved Vouchers page opens with the **All** filter selected by default<br>And each saved voucher is shown as a card with the workshop name, type badge (e.g. "Specialized werkstatt" or "Werkstatt"), discount (e.g. "10% OFF"), voucher code (e.g. "VKKGW1SL"), expiry date (e.g. "Use by 10 Oct 2023"), and a **View Details** action | `TC-SV-001` | Draft |
| AC-SV-02  | Filtering saved vouchers by "Workshop"                        | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Alternate  | 🟠 High     | The user is on the Saved Vouchers page with vouchers saved from both regular and specialized workshops   | User selects the **Workshop** filter tab                     | Only vouchers saved from regular (non-specialized) workshops are shown (e.g. "Jackel Gmbh")<br>And vouchers saved from specialized workshops are hidden                                                                                | `TC-SV-003` | Draft |
| AC-SV-03  | Filtering saved vouchers by "Special workshop"                | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Alternate  | 🟠 High     | The user is on the Saved Vouchers page with vouchers saved from both regular and specialized workshops   | User selects the **Special workshop** filter tab              | Only vouchers saved from specialized workshops are shown (e.g. "Riparo Workshops")<br>And vouchers saved from regular workshops are hidden                                                                                             | `TC-SV-004` | Draft |
| AC-SV-04  | Empty state when no vouchers are saved                        | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Edge       | 🟡 Medium   | A logged-in user has never saved a voucher                                                                | User opens the Saved Vouchers page                            | An empty-state message is shown indicating no vouchers have been saved yet<br>And no voucher cards are displayed                                                                                                                        | `TC-SV-005`, `TC-SV-006` | Draft |
| AC-SV-05  | Viewing a saved voucher's details                              | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Happy      | 🟠 High     | The user is on the Saved Vouchers page with at least one saved voucher listed                             | User taps **View Details** on a voucher card                 | The voucher's detail view opens showing the workshop name, discount, redemption code, and expiry date for that voucher                                                                                                                  | `TC-SV-002` | Draft |
| AC-SV-06  | Saved Vouchers page requires an authenticated user             | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Permission | 🔴 Critical | A user is not logged in                                                                                   | User attempts to access the Saved Vouchers page               | The user cannot view any saved voucher list<br>And is redirected/forced to the login screen                                                                                                                                             | `TC-SV-007` | Draft |

## Business Rules (rule-based AC)

| Rule ID  | Business Rule                                                                                                                                     | Jira                                                    | Rationale / Source                                                                          | Criticality | Linked TCs | Status |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------- | ---------- | ------ |
| BR-SV-01 | A voucher is added to a user's Saved Vouchers list only after that user taps **Save voucher** for it on the Workshop page; the list is scoped to that user's own account, not shared across users. | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Cross-feature dependency confirmed with stakeholder: "voucher save in workshop will display in Saved voucher page" | 🟠 High     | `TC-SV-008`, `TC-SV-009` | Draft |
| BR-SV-02 | Each saved voucher's filter category ("Workshop" vs "Special workshop") is determined by the type of the workshop it was saved from.                    | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Ticket requirement: "Users can filter by All or Workshop or Special workshop"                | 🟡 Medium   | `TC-SV-003`, `TC-SV-004` | Draft |
| BR-SV-03 | An expired voucher remains visible in the Saved Vouchers list with no "Expired" badge and no auto-hide — expiry does not affect its display on this page (unlike the Workshop map/list, which does hide expired vouchers). | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Stakeholder confirmed: "hiện tại không có, vẫn luôn hiện" (no expiry-based hiding; always shown) | 🟡 Medium   | `TC-SV-010` | Draft |
| BR-SV-04 | When a selected filter tab (Workshop / Special workshop) has zero matching vouchers, the list area shows nothing — no empty-state message. The empty-state message (AC-SV-04) only appears when the user has zero saved vouchers overall. | [RC-65](https://motionscloud.atlassian.net/browse/RC-65) | Stakeholder confirmed: "không hiện gì cả" (nothing is shown for an empty filter result) | ⚪ Low       | `TC-SV-005` | Draft |

## Column Guide

| Column          | Description                                                       | Values / Format                                   |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------- |
| **AC ID**       | Unique scenario id — TCs trace back to this                      | `AC-SV-NN`                                  |
| **Rule ID**     | Unique business-rule id — TCs trace back to this                 | `BR-SV-NN`                                  |
| **Scenario**    | Short title of the behaviour, start with an action verb          | Plain text                                        |
| **Jira**        | The ticket this AC came from                                     | `[RC-65](url)`                                     |
| **Type**        | Class of scenario                                               | Happy / Alternate / Negative / Edge / Permission  |
| **Criticality** | Impact if this AC fails — drives the verifying TC's priority     | 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low          |
| **Given**       | Precondition / context true before the action                   | One state per clause; `<br>And …` to compound     |
| **When**        | The single action or event that triggers behaviour             | One trigger                                        |
| **Then**        | Observable, verifiable outcome — pass/fail must be objective    | Include error code / message / state where relevant |
| **Linked TCs**  | TCs in `03_Testcases/saved_voucher/saved_voucher.md` that verify this AC          | `TC-SV-NNN`, comma-separated                |
| **Status**      | Review state of the criterion                                   | Draft / Reviewed / Approved                        |

## Traceability

```
Jira ticket  ──▶  AC-SV-NN / BR-SV-NN  ──▶  TC-SV-NNN
 (the why)         (the what — this file)                  (the how to verify)
```
