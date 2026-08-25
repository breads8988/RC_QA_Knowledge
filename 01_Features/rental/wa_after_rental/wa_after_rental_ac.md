---
type: ac
feature: "[[wa_after_rental]]"
code: ARE
jira: [RC-137]
version: 1.0
updated: 2026-08-25
ba_owner:
reviewer:
status: Draft
---

# Acceptance Criteria — After Rental (`ARE`)

## User Story

**As a** driver who has just returned a rented vehicle
**I want** to capture photos of any new damage per zone, review the AI-detected damage list, and see a side-by-side cost comparison against my Before Rental submission
**So that** I have clear, dated evidence of what changed during the rental period before the estimate is finalized

> **Grounded against** `01_Features/rental/wa_after_rental/screens/*.png` (3 screenshots supplied by the requester, covering the zone-capture diagram, guided camera, damage annotation, damage-entry form, AI processing, AI estimated repair cost table, and the "Car rental cost estimates" list/delete screens) and the RC-137 description. Screens are low-resolution; exact copy/spacing beyond what the ticket text states is unconfirmed — only structure and states visible in both are used below.

## Scenario-based AC — Given / When / Then

| AC ID | Scenario | Jira | Type | Criticality | Given (context) | When (action / trigger) | Then (expected outcome) | Linked TCs | Status |
| ----- | -------- | ---- | ---- | ------------ | ---------------- | ------------------------ | ------------------------- | ---------- | ------ |
| AC-ARE-01 | "Digital cost estimates" opens the Car rental cost estimates page | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | User is logged in and on the My Activities page (`AC-MA-01`) | User taps **Digital cost estimates** | The Car rental cost estimates page opens, listing all of the user's rental data | `TC-ARE-001` | Draft |
| AC-ARE-02 | Completed Before Rental section shows a checkmark and View button | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟠 High | A vehicle's Before Rental (`BRE`) submission is finished | User views that vehicle's card on Car rental cost estimates | The "Before rental" section shows a completed state: a green checkmark and a **View** button | `TC-ARE-002` | Draft |
| AC-ARE-03 | Unfinished Before Rental lets the user continue it from this page | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Alternate | 🟠 High | A vehicle's Before Rental (`BRE`) submission is not finished | User views that vehicle's card on Car rental cost estimates | The user can continue the Before Rental steps from this card, rather than only the After Rental steps | `TC-ARE-003` | Draft |
| AC-ARE-04 | Vehicle card displays the 4-step After Rental timeline | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟡 Medium | A vehicle's Before Rental section is complete | User views that vehicle's card | The After Rental timeline is shown with 4 steps in order: Capture photos, Capture damaged photos, Get AI Cost estimate, Submit | `TC-ARE-004` | Draft |
| AC-ARE-05 | "Continue estimation after rental" starts the After Rental flow | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | A vehicle's Before Rental section is complete and After Rental has not been submitted | User taps **Continue estimation after rental** | The After Rental flow opens at the Capture Photos step for that vehicle | `TC-ARE-005` | Draft |
| AC-ARE-06 | Capture Photos shows the same 9-zone diagram as Before Rental | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟡 Medium | User has started the After Rental flow | User views the Capture photos screen | A top-down 9-zone vehicle diagram is shown (Vorne Links, Vorne, Vorne Rechts, Links, Dach, Rechts, Hinten Links, Hinten, Hinten Rechts), each zone with a camera icon, matching `BRE`'s zone diagram (`BR-ARE-03`) | `TC-ARE-006` | Draft |
| AC-ARE-07 | "Save it for later" preserves After Rental capture progress as a draft | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Alternate | 🟡 Medium | User has captured some but not all 9 zones | User taps **Save it for later** | The current progress is saved as a draft and can be resumed later | `TC-ARE-007` | Draft |
| AC-ARE-08 | Proceed stays inactive until a photo is captured or skip is confirmed | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Edge | 🟠 High | User is on the Capture Photos screen with zero zones captured | User taps **Proceed** | Proceed does not advance the flow unless the user has captured ≥1 photo or explicitly confirms skipping capture (`BR-ARE-02`) | `TC-ARE-008` | Draft |
| AC-ARE-09 | Confirming skip with zero photos allows Proceed to continue | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Alternate | 🟡 Medium | User is on the Capture Photos screen with zero zones captured | User taps **Proceed** and confirms the skip prompt | The flow advances to Vehicle Part Details / AI processing without any zone photos | `TC-ARE-009` | Draft |
| AC-ARE-10 | Vehicle Part Details lists AI-detected damage grouped by part | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟠 High | AI has produced a damage list for the captured zones | User views Vehicle Part Details | Damage is listed grouped by car part (e.g. "Front bumper"), each row showing damage type, damaged car part, side 1, side 2, and an **Edit** action | `TC-ARE-010` | Draft |
| AC-ARE-11 | Fixed bottom bar shows the total AI-estimated repair cost | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | User is on Vehicle Part Details with ≥1 damage entry | User views the bottom of the screen | A fixed section shows the total cost as "€[Amount] AI estimated repair cost" | `TC-ARE-011` | Draft |
| AC-ARE-12 | "Add damage" opens a form to manually add a missed damage entry | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Alternate | 🟡 Medium | User is on Vehicle Part Details | User taps **Add damage** | A form opens allowing the user to manually add a damage entry the AI missed | `TC-ARE-012` | Draft |
| AC-ARE-13 | Done finalizes the assessment list and proceeds to AI Processing | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | User is on Vehicle Part Details with ≥1 damage entry | User taps **Done** | The assessment list is confirmed and finalized, and the flow proceeds | `TC-ARE-013` | Draft |
| AC-ARE-14 | AI Processing shows a loading animation and wait text | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟡 Medium | User has finalized Vehicle Part Details | User views the AI Processing screen | A loading animation is shown with the text "Please wait AI is processing to assess damages" | `TC-ARE-014` | Draft |
| AC-ARE-15 | Back/exit is disabled during AI Processing | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Negative | 🟠 High | The AI Processing screen is active | User attempts to navigate back or exit | The back/exit action is disabled/blocked, so the AI assessment cannot be interrupted (`BR-ARE-01`) | `TC-ARE-015` | Draft |
| AC-ARE-16 | Edit/Add Damage modal supports the same fields as Before Rental | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟠 High | User opens the Edit/Add Damage bottom sheet from Vehicle Part Details | User views the modal | The same fields as `BRE`'s damage-entry form are shown: multi-select damage type (Crack/Dent/Scratch), damaged car part, side 1, side 2 (`BR-ARE-03`, `BR-ARE-04`) | `TC-ARE-016` | Draft |
| AC-ARE-17 | Done on AI Estimated Repair Cost opens the Submission Success screen | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | User is on the AI Estimated Repair Cost screen after AI processing completes | User taps **Done** | The Submission Success screen opens with the text "Rental images have been submitted for before and after rental. Please take a look at the comparison of AI Cost estimate of Before rental and after rental" and a primary **View comparison** button | `TC-ARE-017` | Draft |
| AC-ARE-18 | "View comparison" opens the Comparison Screen | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | User is on the Submission Success screen | User taps **View comparison** | The Comparison Screen opens for that vehicle's rental estimate | `TC-ARE-018` | Draft |
| AC-ARE-19 | Comparison table shows Before vs After columns per part | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | User is on the Comparison Screen for a completed after-rental submission | User views the comparison table | Each affected part (e.g. "Front bumper", "Front headlight") shows a "Before rental" column and an "After rental" column, comparing Damage, Car part, Side 1, Side 2 | `TC-ARE-019` | Draft |
| AC-ARE-20 | Sticky footer shows the Before/After total cost comparison | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🔴 Critical | User is on the Comparison Screen | User views the bottom of the screen | A fixed footer shows "BEFORE RENTAL: €[Amount]" and "AFTER RENTAL: €[Amount]" | `TC-ARE-020` | Draft |
| AC-ARE-21 | "Back to home" returns to the Home page from the Comparison Screen | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Alternate | ⚪ Low | User is on the Comparison Screen | User taps **Back to home** | The user is navigated to the Home page | `TC-ARE-021` | Draft |
| AC-ARE-22 | Completed After Rental shows a completed state and View button | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟠 High | The After Rental flow has been submitted for a vehicle | User views that vehicle's card on Car rental cost estimates | The "After rental" step shows a completed state with a **View** button | `TC-ARE-022` | Draft |
| AC-ARE-23 | View (After rental) re-opens that rental's submitted data | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟡 Medium | The After Rental step is in its completed state on a vehicle's card | User taps **View** | The user can review the submitted rental data | `TC-ARE-023` | Draft |
| AC-ARE-24 | Card's primary action becomes "View compared cost estimate" once complete | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟠 High | Both Before Rental and After Rental are complete for a vehicle | User views that vehicle's card | The primary action button reads **View compared cost estimate** (replacing "Continue estimation...") and opens the Comparison Screen | `TC-ARE-024` | Draft |
| AC-ARE-25 | 3-dot/more-options icon opens the Delete Estimate action sheet | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟡 Medium | User is on the Car rental cost estimates page with ≥1 vehicle card | User taps the card's 3-dot/more-options icon | A bottom sheet opens with **Delete Estimate** and **Cancel** | `TC-ARE-025` | Draft |
| AC-ARE-26 | Deleting an estimate shows a "deleted successfully" toast | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Happy | 🟠 High | The Delete Estimate action sheet is open for a vehicle's card | User taps **Delete Estimate** | The estimate is removed from the list and a toast reads "[car name] deleted successfully" | `TC-ARE-026` | Draft |
| AC-ARE-27 | Cancel dismisses the action sheet without changes | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Alternate | ⚪ Low | The Delete Estimate action sheet is open for a vehicle's card | User taps **Cancel** | The bottom sheet closes and the card is unchanged | `TC-ARE-027` | Draft |
| AC-ARE-28 | Comparison table and vehicle graphic stay usable on small screens | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Edge | 🟡 Medium | User is on a small-screen device | User views the Comparison Screen and the 360 vehicle graphic | The comparison table and the 360-car graphic layout do not break or overflow unreadably | `TC-ARE-028` | Draft |

## Business Rules (rule-based AC)

| Rule ID | Business Rule | Jira | Rationale / Source | Criticality | Linked TCs | Status |
| ------- | -------------- | ---- | ------------------- | ----------- | ---------- | ------ |
| BR-ARE-01 | Back and exit navigation must be disabled while the AI Processing screen is active, so the damage assessment cannot be interrupted. | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Ticket, verbatim: "Disable back/exit actions to prevent interrupting the process." | 🟠 High | `TC-ARE-015` | Draft |
| BR-ARE-02 | On the Capture Photos step, "Proceed" is enabled only when at least one zone photo has been captured, or the user has explicitly confirmed skipping capture. | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Ticket, verbatim: "'Proceed': Move to the AI processing step (only active if at least one photo is captured or the user confirms to skip)." | 🟠 High | `TC-ARE-008`, `TC-ARE-009` | Draft |
| BR-ARE-03 | The zone-capture diagram, guided camera, Vehicle Part Details editor, and Edit/Add Damage modal must behave identically to the Before Rental (`BRE`) equivalents. | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Ticket marks Steps 2, 3, 4 and 5 verbatim as "like the Before rental screen" | 🟠 High | `TC-ARE-006`, `TC-ARE-010`, `TC-ARE-016` | Draft |
| BR-ARE-04 | A damaged part's damage-type field is multi-select — one part can carry more than one type simultaneously, consistent with `BRE` (`BR-BRE-03`) and `AA` (`BR-AA-06`). | [RC-137](https://motionscloud.atlassian.net/browse/RC-137) | Inherited via `BR-ARE-03` from the Before Rental damage-entry form, which the ticket ties this step to | 🟡 Medium | `TC-ARE-016` | Draft |

## Column Guide

| Column | Description | Values / Format |
| ------ | ------------ | ---------------- |
| **AC ID** | Unique scenario id — TCs trace back to this | `AC-ARE-NN` |
| **Rule ID** | Unique business-rule id — TCs trace back to this | `BR-ARE-NN` |
| **Scenario** | Short title of the behaviour, start with an action verb | Plain text |
| **Jira** | The ticket this AC came from | `[RC-137](url)` |
| **Type** | Class of scenario | Happy / Alternate / Negative / Edge / Permission |
| **Criticality** | Impact if this AC fails — drives the verifying TC's priority | 🔴 Critical / 🟠 High / 🟡 Medium / ⚪ Low |
| **Given** | Precondition / context true before the action | One state per clause; `<br>And …` to compound |
| **When** | The single action or event that triggers behaviour | One trigger |
| **Then** | Observable, verifiable outcome — pass/fail must be objective | Include error code / message / state where relevant |
| **Linked TCs** | TCs in `01_Features/rental/wa_after_rental/wa_after_rental_tc.md` that verify this AC | `TC-ARE-NNN`, comma-separated |
| **Status** | Review state of the criterion | Draft / Reviewed / Approved |

## Traceability

```
Jira ticket  ──▶  AC-ARE-NN / BR-ARE-NN  ──▶  TC-ARE-NNN
 (the why)         (the what — this file)                  (the how to verify)
```

- **Upward**: each row's `Jira` column links the AC to its source, RC-137.
- **Downward**: the `Linked TCs` column lists the test cases that verify each AC.
- **Coverage rule**: every `Critical` and `High` AC and every business rule must have ≥1 Linked TC. Flag any such AC with zero TCs as a coverage gap. Conversely, every TC must name the `AC` it verifies — no orphan TCs.

## Open questions / ambiguities

1. **Entry-point tile name conflicts with the existing Activities menu.** RC-137 states clicking **"Digital cost estimates"** in My Activities opens the "Car rental cost estimates" page, but `AC-MA-01` (from RC-111) already documents My Activities as listing **three separate** tiles: "My accidents", "Digital cost estimates", and "Car rental cost estimates". Needs confirmation of which tile actually opens this page — RC-137's own text may have the wrong tile name.
2. **Unfinished Before Rental redirect target is unclear.** Step 1 says "If Before rental doesn't finish, the user can continue with Before rental steps (like damage report or after rental)" — it's not clear whether this means the user resumes `BRE`'s own steps, or is redirected into the Report Accident (`AA`) flow. Not asserted above (`AC-ARE-03` only states that Before Rental can be continued, not which flow it continues into).
3. **Delete Estimate deletion semantics are unstated.** RC-137 doesn't say whether "Delete Estimate" is a soft delete (record retained, hidden from the list) or a hard delete — `wa_my_accident`'s equivalent action is explicitly soft-delete-only (`BR-MA-02`). Not asserted as a rule here; needs confirmation before automating `AC-ARE-26`.
4. **No entry state defined for a vehicle with no Before Rental record at all.** RC-137 only describes the case where Before Rental exists but is unfinished (Step 1) — it doesn't describe what the Car rental cost estimates page shows for a vehicle that never started Before Rental. Not covered above to avoid inventing UI.
5. **No AI-processing failure state is described.** The ticket only specifies the loading/happy path for Step 4; no error, retry, or timeout behaviour is stated for the AI assessment call. Not asserted above.
6. **Skip-confirmation UI for zero-photo Proceed (Step 2) is unspecified.** `BR-ARE-02` requires either ≥1 photo or a confirmed skip, but the ticket doesn't describe the confirmation prompt's copy or UI. `AC-ARE-09` assumes a confirmation step exists without describing it.

## Impacted existing behaviour (checked, not just found)

- **`e_vehicle` backlinks** (`wa_before_rental`, `registration`, `my_vehicle`) — read all three. This feature is structurally the second half of `BRE`'s flow: Steps 2, 3, 4 and 5 are explicitly tied to `BRE`'s equivalent screens by the ticket itself (captured as `BR-ARE-03`/`BR-ARE-04`, citing `BR-BRE-03`/`BR-BRE-04`/`BR-BRE-05`). No conflict — this feature consumes `BRE`'s established UI pattern rather than redefining it.
- **`accident` domain, `wa_my_accident` (`MA`)** — read `wa_my_accident_ac.md` in full. Two things cross-checked:
  - The My Activities entry point: `AC-MA-01` lists "Digital cost estimates" and "Car rental cost estimates" as two distinct tiles, which conflicts with RC-137's own wording — flagged as Open Question 1 rather than silently picking one.
  - The delete-with-bottom-sheet pattern (`AC-MA-06`/`AC-MA-08`/`AC-MA-10`, `BR-MA-02`, `BR-MA-03`): RC-137's "Delete Estimate" / "Cancel" bottom sheet with a success toast matches this pattern structurally, but RC-137 does not state whether deletion is soft (like `BR-MA-02`) or hard — flagged as Open Question 3, not assumed either way.
- **Domain sibling check**: no Web Portal counterpart exists yet for the `rental` domain (only `wa_before_rental` and `wa_after_rental`), matching the note already recorded in `wa_before_rental_ac.md`. No admin-side obligation to cross-check today.
- **`wp_advertisement` (`WPAD`)**: RC-137 does not mention an ad banner on any After Rental screen (unlike `BRE`'s Capture Photos / AI Processing screens, which do per `BR-BRE`'s AC file open question 1) — nothing added here since the ticket doesn't state it, avoiding over-extending `BRE`'s ad-placement gap onto this feature.
- **Metadata drift**: none found while checking the above — `MV`, `REG`, `AA`, `MA`, `BRE` hubs all have populated `entity` links and existing `ac:` files. The `rental` domain itself had no domain hub before this run (only 1 feature existed under it); created `01_Features/rental/rental.md` now that the domain has 2 features, per convention §1.
