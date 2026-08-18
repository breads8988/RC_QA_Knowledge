---
type: tc
feature: "[[homepage]]"
code: HOME
jira: [RC-1, RC-106]
version: 1.0
updated: 2026-08-06
owner: QC Team
reviewer: 
sprint: 
tc_total: 14
tc_automated: 0
tc_pending: 14
status: Draft
---

# Test Case Register — Home Page (`HOME`)

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 14        | 0         | 0      | 14      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 3        | 5    | 5      | 1   |

> **AC source:** [`01_Features/homepage/homepage_ac.md`](homepage_ac.md) — all 13 AC (`AC-HOME-01…13`) and 4 business rules (`BR-HOME-01…04`) have ≥1 covering TC.

> ⚠️ **UI coverage is partial.** `01_Features/homepage/screens/Screenshot 2026-08-06 at 09.36.25.png` is a cropped capture of only the "LOGGED IN" Splash + Home flow — no guest view, inactive-tile styling, or the section cut off below it ("FIRST REGISTRATIO…") is visible. RC-1's Figma links (mobile + web) were not fetched. TCs marked `[DEP] UI pending` assert only behaviour the tickets describe.

> ✅ **All 8 open questions resolved (2026-08-06)** — see `## Confirmed Decisions` in the AC spec. TCs below have been updated to match: inactive-tile tap now redirects to Login (TC-HOME-009), tip/intro persistence is cookie-based (TC-HOME-004/005/006/007), and device-adaptation depth is deprioritized (TC-HOME-013).

## Test Case Table

### 1. Feature Grid Display

| TC ID        | Test Scenario                                         | AC                    | Jira                                                                                                          | Priority    | Coverage   | Cucumber Tag   | Preconditions                                                                        | Test Data                                                                                       | High-level Steps                                                          | Expected Result                                                                                                                  | Status    | Note                                                     |
| ------------- | ---------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------- | ----------- | ---------- | -------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------- |
| TC-HOME-001   | Open the Home page as a logged-in user                 | AC-HOME-01             | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)                                                       | 🔴 Critical | 🔵 Pending | `@TC-HOME-001` | The user is logged in<br>At least 3 features are enabled in the Admin config                 | 3 Admin-enabled features                                                                            | 1. Log in. 2. Navigate to the Home page.                                          | The banner is shown and every Admin-enabled feature appears as an active tile.                                                         | ⬜ Not Run | `[DEP]` UI pending — exact tile content unconfirmed          |
| TC-HOME-002   | Open the Home page as a guest                           | AC-HOME-02, BR-HOME-02 | [RC-1](https://motionscloud.atlassian.net/browse/RC-1), [RC-106](https://motionscloud.atlassian.net/browse/RC-106) | 🔴 Critical | 🔵 Pending | `@TC-HOME-002` | The user is not logged in<br>Admin config has ≥1 no-login feature and ≥1 login-required feature | "Clever tanken" (no-login, per BR-HOME-02 baseline), "Unfallhilfe" (login-required, per BR-HOME-02 baseline) | 1. Open the Home page without logging in. 2. Inspect each tile's active/inactive state. | The banner is shown; no-login features appear active and login-required features appear visibly inactive, matching Figma.               | ⬜ Not Run | `[DEP]` UI pending — inactive-tile styling unconfirmed       |
| TC-HOME-010   | Admin-disabled feature is hidden                        | AC-HOME-10, BR-HOME-01 | [RC-106](https://motionscloud.atlassian.net/browse/RC-106)                                                   | 🟠 High     | 🔵 Pending | `@TC-HOME-010` | A feature is disabled in the Admin feature-config page                                      | 1 feature toggled "disabled" in `/admin/features`                                                     | 1. Disable a feature in Admin. 2. Open the Home page as a guest. 3. Open it again as a logged-in user. | The disabled feature's tile does not appear on the Home page for either user type.                                                       | ⬜ Not Run | `[DATA]`                                                     |
| TC-HOME-011   | Not-yet-implemented free feature stays inactive         | AC-HOME-11, BR-HOME-03 | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)                                                       | 🟡 Medium   | 🔵 Pending | `@TC-HOME-011` | "Clever tanken" or "Parkplatz Suche" is Admin-enabled as a no-login feature                  | "Clever tanken" enabled, login not required                                                          | 1. Open the Home page as a guest. 2. Open it again as a logged-in user. 3. Attempt to tap the tile in each case. | The tile is shown but inactive/non-tappable for both user types.                                                                       | ⬜ Not Run | `[DATA]`                                                     |

### 2. Guest Access & Login Gating (Regression)

| TC ID        | Test Scenario                                            | AC        | Jira                                                                                                          | Priority    | Coverage   | Cucumber Tag   | Preconditions                                                                     | Test Data                                       | High-level Steps                                                     | Expected Result                                                                                                    | Status    | Note                                                                 |
| ------------- | -------------------------------------------------------------- | --------- | ------------------------------------------------------------------------------------------------------------- | ----------- | ---------- | -------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------------- |
| TC-HOME-003   | Use a guest-accessible feature (regression)                | AC-HOME-03 | [RC-106](https://motionscloud.atlassian.net/browse/RC-106)                                                   | 🔴 Critical | 🔵 Pending | `@TC-HOME-003` | A feature is Admin-enabled with "login required" unchecked<br>The user is a guest          | 1 feature, e.g. "Werkstatt Finden" with login required unchecked | 1. Open the Home page as a guest. 2. Tap the guest-accessible feature's tile. | The guest is taken into that feature's page — not a silent no-op.                                                       | ⬜ Not Run | `[BUG]` Regression for Ann's 2026-07-09 report ("click on don't show anything") |
| TC-HOME-009   | Login-required feature tile redirects a guest to the Login page | AC-HOME-09 | [RC-1](https://motionscloud.atlassian.net/browse/RC-1), [RC-106](https://motionscloud.atlassian.net/browse/RC-106) | 🟠 High     | 🔵 Pending | `@TC-HOME-009` | A feature is Admin-configured "login required"<br>The user is a guest                      | 1 feature, e.g. "Unfallhilfe" with login required            | 1. Open the Home page as a guest. 2. Tap the login-required feature's tile.  | The guest is not taken into that feature's page<br>And is redirected to the Login page instead.                    | ⬜ Not Run |      |

### 3. First-Use Tips & Intro Popups

| TC ID        | Test Scenario                                    | AC                      | Jira                                                     | Priority  | Coverage   | Cucumber Tag   | Preconditions                                                          | Test Data          | High-level Steps                                                                       | Expected Result                                                                                            | Status    | Note                                                        |
| ------------- | ------------------------------------------------------ | ------------------------ | ----------------------------------------------------------- | --------- | ---------- | -------------- | ----------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------- |
| TC-HOME-004   | First-time tip on a feature                       | AC-HOME-04, BR-HOME-04  | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)   | 🟡 Medium | 🔵 Pending | `@TC-HOME-004` | The user has never seen the tip for feature *X*                                | Feature *X* = "Unfallhilfe" | 1. Log in as a user who has never visited the Home page. 2. Open the Home page.                 | The first-use tip for feature *X* is shown.                                                                    | ⬜ Not Run | `[DEP]` UI pending — tip content/placement unconfirmed        |
| TC-HOME-005   | Skip a tip so it does not reappear                | AC-HOME-05, BR-HOME-04  | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)   | 🟡 Medium | 🔵 Pending | `@TC-HOME-005` | The first-use tip for feature *X* is showing                                   | Feature *X* = "Unfallhilfe" | 1. Skip the tip. 2. Navigate away from the Home page. 3. Return to the Home page (same browser, cookie retained).               | The tip is dismissed immediately and does not reappear on the later visit.                                    | ⬜ Not Run | `[DATA]` seen-state tracked via browser cookie    |
| TC-HOME-014   | Clearing cookies resets the tip's "seen" state    | AC-HOME-05, BR-HOME-04  | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)   | 🟡 Medium | 🔵 Pending | `@TC-HOME-014` | The user previously skipped/saw the tip for feature *X* in this browser         | Feature *X* = "Unfallhilfe" | 1. Skip the tip. 2. Clear the browser's cookies (or open a new browser/device). 3. Return to the Home page.               | The first-use tip for feature *X* is shown again, since the cookie tracking the "seen" state was cleared.        | ⬜ Not Run | `[DATA]`    |
| TC-HOME-006   | First tap on a feature shows its intro popup      | AC-HOME-06, BR-HOME-04  | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)   | 🟠 High   | 🔵 Pending | `@TC-HOME-006` | A logged-in user has never opened feature *X* before                           | Feature *X* = "Unfallhilfe" | 1. Log in. 2. Tap feature *X*'s tile for the first time. 3. Proceed past the intro popup.         | An intro popup for feature *X* is shown, and after proceeding the user reaches feature *X*'s page.               | ⬜ Not Run | `[DEP]` UI pending — popup content unconfirmed                |
| TC-HOME-007   | Later taps skip the intro popup                   | AC-HOME-07, BR-HOME-04  | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)   | 🟡 Medium | 🔵 Pending | `@TC-HOME-007` | The user already saw the intro popup for feature *X* (same browser, cookie retained)                           | Feature *X* = "Unfallhilfe" | 1. Return to the Home page. 2. Tap feature *X*'s tile again.                                     | The user goes directly to feature *X*'s page; the intro popup does not reappear.                               | ⬜ Not Run | `[DATA]` seen-state tracked via browser cookie    |

### 4. Navigation

| TC ID        | Test Scenario                              | AC        | Jira                                                        | Priority | Coverage   | Cucumber Tag   | Preconditions                          | Test Data | High-level Steps                                                 | Expected Result                                        | Status    | Note                                            |
| ------------- | ------------------------------------------------ | --------- | ---------------------------------------------------------------- | -------- | ---------- | -------------- | -------------------------------------------- | --------- | ------------------------------------------------------------------------ | -------------------------------------------------------- | --------- | -------------------------------------------------------- |
| TC-HOME-008   | Return to Home via the RepairCheck logo    | AC-HOME-08 | [RC-106](https://motionscloud.atlassian.net/browse/RC-106)      | 🟠 High  | 🔵 Pending | `@TC-HOME-008` | The user is on any non-Home page of the web app | —         | 1. Navigate to any other page. 2. Click/tap the RepairCheck logo.          | The user is redirected to the Home page.                  | ⬜ Not Run | `[BUG]` Regression fix per RC-106 description             |

### 5. Responsive / Compatibility

| TC ID        | Test Scenario                                    | AC        | Jira                                                       | Priority  | Coverage   | Cucumber Tag   | Preconditions                                             | Test Data | High-level Steps                                                                        | Expected Result                                                                                                              | Status    | Note                                                        |
| ------------- | ------------------------------------------------------ | --------- | --------------------------------------------------------------- | --------- | ---------- | -------------- | ---------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------------------------------------------------------------ |
| TC-HOME-012   | Home page works on phone and tablet               | AC-HOME-12 | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)         | 🟠 High   | 🔵 Pending | `@TC-HOME-012` | A phone-sized viewport, then a tablet-sized viewport                | —         | 1. Open the Home page on a phone. 2. Open it on a tablet.                                     | The banner and quick menu are fully visible and operable in each; no content is clipped, overlapping, or requires horizontal scroll. | ⬜ Not Run | `[DEP]` UI pending — no design to compare against              |
| TC-HOME-013   | Banner and quick menu adapt to the device         | AC-HOME-13 | [RC-1](https://motionscloud.atlassian.net/browse/RC-1)         | ⚪ Low    | 🔵 Pending | `@TC-HOME-013` | The Home page is open                                               | —         | 1. Open the Home page on a phone. 2. Open the same page on a tablet/desktop viewport.          | The banner and quick menu remain usable and reasonably positioned on each viewport — exact "floating" mechanics/breakpoints not verified (deprioritized per stakeholder).                                                | ⬜ Not Run |      |

## Regression Impact (§15)

| Impacted area                                                             | Risk                                                                                                   | Covered by              |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------ |
| Every feature page reachable from Home (`expert`, `lawyer`, and others)        | The Home page is the sole entry point for these features; a tile/config regression blocks access to all of them | TC-HOME-001, TC-HOME-003, TC-HOME-006 |
| Admin feature-config page (`/admin/features`)                                 | Home page visibility now depends on this external config; a config-read regression could hide or wrongly expose features | TC-HOME-002, TC-HOME-010 |
| Global navigation (RepairCheck logo)                                          | The logo-click redirect is used from every page in the app                                              | TC-HOME-008              |

## Techniques not applied

| Technique                             | Why not applicable                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| §6 Decision Table                      | Tile state depends on two conditions (Admin-enabled × login-required vs. user login state) but only 4 combinations exist; each is covered directly by TC-HOME-001/002/003/009/010/011 without needing formal decision-table notation. |
| §7 Pairwise / all-pairs                | Too few independent parameters (login state, Admin config, device) to need combinatorial reduction; each is covered directly.            |
| §8 State Transition                    | The Home page has no entity lifecycle beyond the per-feature "tip seen" / "intro seen" flags, covered under BR-HOME-04 (TC-HOME-004…007). |
| §9 Field-level validation              | The Home page has no user-input fields.                                                                                                    |
| §13 Non-functional (perf / security / a11y / i18n) | Neither ticket states a performance target, security requirement, or accessibility/localisation scope; only **compatibility** is required, covered by TC-HOME-012/013. |
| §3 Unauthorised access (roles beyond guest/logged-in) | Confirmed the Admin feature-config schema has no role/market variants (BR-HOME-01) — only guest vs. logged-in apply, both already covered (TC-HOME-001/002). |

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
