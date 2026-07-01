# Acceptance Criteria — Login

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| **Version**            | 1.0                                            |
| **Last updated**       | 2026-07-01                                     |
| **Feature**            | Login                                          |
| **SRS ref**            | [[01_SRS/login/epic]]                          |
| **Jira tickets**       | `RC-6`, `RC-66`, `RC-26` (parent epic `RC-4`)  |
| **BA Owner**           | —                                              |
| **Reviewer (PO/Lead)** | —                                              |
| **Status**             | Draft                                          |

> **Source note:** `RC-4` is the parent **Epic** (no detail of its own). Login requirements come from its child tickets: **RC-6** (login page), **RC-66** (login + forgot-password error handling), and **RC-26** (login entry points on the landing/home screen). UI grounded in `01_SRS/login/figma/login.png`. Home-page, registration (RC-8) and tour-guide behaviours are owned by other features — only login-relevant entry points are covered here.

## User Story

**As a** registered user
**I want** to log in to the web app (and recover my password if forgotten)
**So that** I can use the paid/registered features — while undecided users can browse as a guest or register.

## Scenario-based AC — Given / When / Then

| AC ID       | Scenario                              | Jira                                                     | Type       | Criticality | Given (context)                                                                    | When (action / trigger)                                          | Then (expected outcome)                                                                                | Linked TCs      | Status |
| ----------- | ------------------------------------- | -------------------------------------------------------- | ---------- | ----------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------- | ------ |
| AC-LOGIN-01 | Open Login from landing               | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | Happy      | 🔴 Critical | A non-logged-in user is on the landing screen                                      | Taps **Login**                                                   | The Login page opens with Email address and Password fields                                            | `TC-LOGIN-001`  | Draft  |
| AC-LOGIN-02 | Login prompt on a charge feature      | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | Permission | 🟠 High     | A guest / non-logged-in user is on the home page                                   | Taps a charge (login-only) feature, e.g. *Unfallhilfe*           | A login popup is displayed and the feature is not opened until the user logs in                        | `TC-LOGIN-002`  | Draft  |
| AC-LOGIN-03 | Continue as guest                     | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | Alternate  | 🟡 Medium   | A non-logged-in user is on the landing screen                                      | Taps **Continue as a guest**                                     | The home page for non-logged-in users is shown (charge features inactive)                              | `TC-LOGIN-003`  | Draft  |
| AC-LOGIN-04 | Go to registration                    | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | Alternate  | 🟡 Medium   | A non-logged-in user is on the landing screen                                      | Taps **"Don't have an account? Register"**                       | The registration page opens (implemented in RC-8)                                                      | `TC-LOGIN-004`  | Draft  |
| AC-LOGIN-05 | Successful login                      | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | Happy      | 🔴 Critical | A registered user on the Login page with a valid email + correct password, "I'm not a robot" passed | Taps **Login**                                                   | Login succeeds, a session is created, and the charge (registered) features become active               | `TC-LOGIN-005`  | Draft  |
| AC-LOGIN-06 | Wrong username / password             | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | Negative   | 🔴 Critical | A registered user on the Login page                                                | Submits a wrong username or password                             | An error message is displayed and no session is created (exact message/code TBD)                       | `TC-LOGIN-006`  | Draft  |
| AC-LOGIN-07 | Invalid email format                  | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | Negative   | 🟠 High     | A user on the Login page                                                           | Enters a badly formatted email (e.g. `John.xyx`) and leaves the field | Inline **"Invalid email address"** error is shown and the **Login** button is disabled                 | `TC-LOGIN-007`  | Draft  |
| AC-LOGIN-08 | Show / hide password                  | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | Alternate  | 🟡 Medium   | A password has been typed and is masked                                            | Toggles the reveal (eye) control                                 | The password characters become visible; toggling again re-masks them                                   | `TC-LOGIN-010`  | Draft  |
| AC-LOGIN-09 | Remember me                           | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | Alternate  | 🟡 Medium   | A user on the Login page                                                           | Enables **Remember me** and logs in successfully                 | The session persists across app restarts per the remember-me policy (duration TBD)                     | `TC-LOGIN-011`  | Draft  |
| AC-LOGIN-10 | Anti-bot verification required        | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | Negative   | 🟠 High     | A valid email + password are entered but "I'm not a robot" is **not** completed    | Attempts to log in                                               | the **Login** button is disabled until the verification is completed; once passed, it becomes enabled  | `TC-LOGIN-009`  | Draft  |
| AC-LOGIN-11 | Open Forgot Password                  | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | Happy      | 🟠 High     | A user on the Login page                                                           | Taps **Forgot Password?**                                        | The "Enter your registered email" screen opens                                                         | `TC-LOGIN-012`  | Draft  |
| AC-LOGIN-12 | Request password-reset code           | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | Happy      | 🟠 High     | A user on "Enter your registered email" with a **registered** email                | Taps **Next**                                                    | A verification code is sent to that email and the code-entry step opens                                | `TC-LOGIN-013`  | Draft  |
| AC-LOGIN-13 | Forgot password — wrong email         | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | Negative   | 🟠 High     | A user on "Enter your registered email"                                            | Enters a wrong / unregistered email and taps **Next**            | An error message is displayed and no code is sent                                                      | `TC-LOGIN-014`  | Draft  |
| AC-LOGIN-14 | Forgot password — reset limitation    | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | Negative   | 🟡 Medium   | A user reaches the reset-password step of the forgot-password flow                 | Enters a new password                                            | The password cannot be changed — strength always shows **"Password strength: Okay"** and the user cannot proceed (known limitation — confirm scope) | `TC-LOGIN-015`  | Draft  |

## Business Rules (rule-based AC)

| Rule ID     | Business Rule                                                                                             | Jira                                                     | Rationale / Source                | Criticality | Linked TCs                                     | Status |
| ----------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------- | ----------- | ---------------------------------------------- | ------ |
| BR-LOGIN-01 | **Login** is enabled only when ALL hold: email is a valid format, password is non-empty, and "I'm not a robot" is passed. | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | Figma — button enabled/disabled   | 🔴 Critical | `TC-LOGIN-005`, `TC-LOGIN-008`, `TC-LOGIN-009`, `TC-LOGIN-016` | Draft  |
| BR-LOGIN-02 | Email must match a valid email format; an invalid format shows the inline error **"Invalid email address"**. | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | Figma + RC-66                     | 🟠 High     | `TC-LOGIN-007`, `TC-LOGIN-016`                 | Draft  |
| BR-LOGIN-03 | The password is masked by default and can be toggled to visible via the reveal control.                  | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | Figma — password field            | 🟡 Medium   | `TC-LOGIN-010`                                 | Draft  |
| BR-LOGIN-04 | Charge (registered) features are usable only by logged-in users; a guest who taps one is shown a login popup. | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | RC-26 — access policy             | 🔴 Critical | `TC-LOGIN-002`                                 | Draft  |

## Open Questions (BA duty — confirm before TCs are finalised)

1. **Wrong-credentials error** (RC-66) — exact message/code and whether there is an **account lockout / rate-limit** after repeated failures.
2. **Forgot-password reset limitation** (RC-66) — is "user cannot proceed / strength always *Okay*" **intended for this phase**, or a defect to be fixed? What is the target end-state?
3. **Forgot-password code** — length, expiry, and resend rule?
4. **Remember me** — how long does the session persist? (from Figma only, not in tickets)
5. **Anti-bot ("I'm not a robot")** — required on every login or only after failures? Confirm vendor/version. (Figma only)
6. **Password policy** — min/max length and complexity for login/registration? (not specified)
7. **Post-login destination** — confirm success lands on the logged-in home page (RC-26).
8. **Show/hide password + Remember me** — from Figma only; confirm they are in scope for this phase.

## Traceability

```
RC-4 (Epic)  ─▶  RC-6 / RC-26 / RC-66 (child tickets)  ─▶  AC-LOGIN-NN / BR-LOGIN-NN (this file)  ─▶  TC-LOGIN-NNN (/gen-tc)
```

- **Coverage rule:** every `Critical` / `High` AC and every business rule has ≥1 Linked TC (filled above). Register: `03_Testcases/login/login.md`.
