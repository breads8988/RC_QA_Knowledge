# Acceptance Criteria — Lawyer (Unfall Rechtsberatung)

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| **Version**            | 1.0                                                            |
| **Last updated**       | 2026-07-09                                                     |
| **Feature**            | Lawyer page — Unfall Rechtsberatung (Accident legal advice)    |
| **SRS ref**            | [[01_SRS/lawyer/]]                                             |
| **Jira tickets**       | `RC-116` (child of Epic `RC-101` — Web App)                    |
| **BA Owner**           | QC Team                                                        |
| **Reviewer (PO/Lead)** | TBD                                                            |
| **Status**             | Draft                                                          |

## User Story

**As a** RepairCheck web-app user who needs legal help after an accident
**I want** to open "Unfall Rechtsberatung", browse a list of lawyers, filter them by rating, and request an appointment
**So that** I can find suitable legal representation and have the lawyer contact me to arrange it

## Scenario-based AC — Given / When / Then

> Grounded in RC-116 and the Lawyer-page Figma (`01_SRS/lawyer/figma/lawyer.png`). **Confirmed flow (2026-07-09):** "Get appointment" → "Do you want &lt;Lawyer&gt; to contact you?" → **"Yes, contact me" opens Calendly** (`https://calendly.com/alextyl/jaekelgmbh`) **in a new browser tab** (the Repair Check tab is preserved); after the user completes the booking, they **return to the Repair Check tab themselves** and see a **"Thanks for booking your appointment" popup** (no automatic redirect).

| AC ID        | Scenario           | Jira         | Type      | Criticality | Given (context)             | When (action / trigger)      | Then (expected outcome)                          | Linked TCs      | Status |
| ------------ | ------------------ | ------------ | --------- | ----------- | --------------------------- | ---------------------------- | ------------------------------------------------ | --------------- | ------ |
| AC-LAW-01 | Open the lawyer list from "Unfall Rechtsberatung" | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Happy | 🟠 High | A signed-in user on the Home page | They tap the "Unfall Rechtsberatung" (Accident legal advice) tile | The "Lawyers" list page opens and shows the available lawyers | `TC-LAW-001` | Draft |
| AC-LAW-02 | View the list of lawyers | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Happy | 🔴 Critical | The user has opened the Lawyers page | The list is displayed | A list of lawyer cards is shown; each card shows the lawyer's name, law firm, star rating with review count, full address, phone number, email, and a "Get appointment" action | `TC-LAW-002`, `TC-LAW-012` | Draft |
| AC-LAW-03 | Open the rating filter panel | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Alternate | 🟡 Medium | The Lawyers list is displayed | They tap the filter icon in the header | A "Filter by" panel opens showing a RATINGS selector with values 1★, 2★, 3★, 4★, 5★ | `TC-LAW-003` | Draft |
| AC-LAW-04 | Filter lawyers by minimum rating | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Alternate | 🟠 High | The "Filter by" panel is open | They select a minimum star rating and apply | Only lawyers whose rating meets or exceeds the selected value are listed (e.g. selecting 2★ shows lawyers rated 2★ and above) | `TC-LAW-004` | Draft |
| AC-LAW-05 | "Get appointment" opens a contact-confirmation prompt | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Happy | 🔴 Critical | The Lawyers list is displayed | They tap "Get appointment" on a lawyer card | A prompt "Do you want &lt;Lawyer&gt; to contact you?" is shown, explaining the lawyer will contact them to arrange the appointment, with "Yes, contact me" and "No, I will check later" | `TC-LAW-006` | Draft |
| AC-LAW-06 | "Yes, contact me" opens the lawyer's Calendly in a new tab | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Happy | 🔴 Critical | The contact-confirmation prompt is shown | They select "Yes, contact me" | The Calendly scheduling page (`https://calendly.com/alextyl/jaekelgmbh`) opens in a **new browser tab** and the Repair Check tab is preserved, so the user can pick a day and time | `TC-LAW-007` | Draft |
| AC-LAW-07 | Complete the booking → "Thank you" popup on return to the app tab | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Happy | 🔴 Critical | The lawyer's Calendly page is open in a separate tab; the booking has been completed | They switch back to the Repair Check tab | A "Thanks for booking your appointment" popup is shown on the Repair Check tab, with an "Ok, Back to lawyers" action (no automatic redirect from Calendly) | `TC-LAW-008` | Draft |
| AC-LAW-08 | Decline the appointment request | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Alternate | 🟡 Medium | The contact-confirmation prompt is shown | They select "No, I will check later" | The prompt closes, Calendly is not opened, no request is submitted, and they return to the lawyer list | `TC-LAW-009` | Draft |
| AC-LAW-09 | Return to the lawyer list from the confirmation | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Alternate | ⚪ Low | The "Thanks for booking your appointment" popup is shown | They select "Ok, Back to lawyers" | They are returned to the lawyer list | `TC-LAW-010` | Draft |
| AC-LAW-10 | No lawyers match the rating filter (empty state) | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Edge | 🟡 Medium | The "Filter by" panel is open | They apply a minimum rating that no lawyer satisfies | A no-results / empty state is shown and no lawyer cards are listed | `TC-LAW-005` | Draft |
| AC-LAW-11 | Responsive layout on phone and tablet | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Edge | 🟡 Medium | The Lawyer flow opened in the mobile web app | It is viewed on a phone and on a tablet | The layout renders correctly and all cards, the filter, and the appointment actions remain usable on both form factors | `TC-LAW-011` | Draft |

## Business Rules (rule-based AC)

| Rule ID      | Business Rule                                  | Jira         | Rationale / Source     | Criticality | Linked TCs      | Status |
| ------------ | ---------------------------------------------- | ------------ | ---------------------- | ----------- | --------------- | ------ |
| BR-LAW-01 | Each lawyer entry displays the lawyer's name, law firm, average star rating with review count, full address, phone number, and email address. (No distance is shown, unlike the expert list.) | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Figma lawyer list (`lawyer.png`) | 🟡 Medium | `TC-LAW-002` | Draft |
| BR-LAW-02 | The lawyer list can be filtered by minimum rating (1–5 stars). Selecting N★ returns lawyers whose rating is **greater than or equal to** N (e.g. 2★ → lawyers rated ≥ 2★). | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | Figma "Filter by" (RATINGS) + RC-116 dev comment (2026-07-09): "filter is getting records that have higher value than the selected filter value" | 🟠 High | `TC-LAW-004` | Draft |
| BR-LAW-03 | The appointment flow is: "Get appointment" → contact-confirmation prompt → "Yes, contact me" opens **Calendly** (`https://calendly.com/alextyl/jaekelgmbh`) in a **new browser tab** (the Repair Check tab is preserved). After completing the booking, the user returns to the Repair Check tab themselves and a "Thanks for booking your appointment" popup is shown there (no automatic redirect from Calendly). | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | RC-116 Story 3 + stakeholder confirmation (2026-07-09) + Figma popups | 🔴 Critical | `TC-LAW-006`, `TC-LAW-007`, `TC-LAW-008` | Draft |
| BR-LAW-04 | The Lawyer page must render and function correctly on both phone and tablet form factors. | [RC-116](https://motionscloud.atlassian.net/browse/RC-116) | RC-116 requirement + QA comment (iPad display defect) | 🟡 Medium | `TC-LAW-011` | Draft |

## Traceability

```
Jira RC-101 (Epic — Web App)
 └─ RC-116 (Fix Lawyer page)  ──▶  AC-LAW-01…11 / BR-LAW-01…04  ──▶  TC-LAW-NNN (via /gen-tc)
```

- **Upward**: header `SRS ref` + each row's `Jira` column link the AC to its source ticket (RC-116).
- **Downward**: the `Linked TCs` column lists the verifying test cases in `03_Testcases/lawyer/lawyer.md` (filled by `/gen-tc`).
- **Coverage rule**: every Critical/High AC and every business rule needs ≥1 Linked TC.

## Open Questions / Assumptions (BA — confirm with stakeholders before TC generation)

1. **✅ DECIDED (2026-07-09) — Appointment flow opens Calendly in a new tab.** "Get appointment" → contact-confirmation prompt → **"Yes, contact me" opens Calendly** (`https://calendly.com/alextyl/jaekelgmbh`) in a **new browser tab**. After completing the booking, the user **returns to the Repair Check tab themselves** and sees a "Thanks for booking your appointment" popup (no automatic redirect). Captured in AC-LAW-05/06/07 and BR-LAW-03. **Follow-up:** is the Calendly link **shared** for all lawyers, or is there a **per-lawyer** link (the expert page uses per-expert links per BR-ECA-05)?
2. **Rating filter semantics.** RC-116 comment thread: QA reported "filter 2★ shows 3★ and 4★" as a bug; dev replied the filter returns records **≥** the selected value (minimum-rating semantics). BR-LAW-02 assumes minimum-rating is the intended behaviour (consistent with the expert list). **Confirm** this is intended (not exact-match). Also confirm how a decimal rating (e.g. 4.8) is matched to a star bucket.
3. **Empty-state UI (AC-LAW-09).** The design does not show a "no lawyers match" state. Confirm the expected message/behaviour when the rating filter excludes every lawyer.
4. **Filter apply model & multi-select.** Confirm whether the rating filter is single-select (one star value) or multi-select, and whether it applies live or on an explicit "Apply"/close action. Figma shows one value (4★) highlighted.
5. **Lawyer list data source & ordering.** Confirm where the lawyer list comes from and the default ordering (the expert list is nearest-first by distance, but lawyer cards show no distance — confirm there is no location/distance concept here).
6. **Callback request persistence.** Confirm what "Yes, contact me" does server-side (creates a request record? notifies the lawyer/firm?) and whether the user can see/track the request afterward.
7. **SRS note.** No `01_SRS/lawyer/epic.md` exists yet; the SRS ref points at the folder. Create the SRS note if the team wants a formal SRS anchor.
