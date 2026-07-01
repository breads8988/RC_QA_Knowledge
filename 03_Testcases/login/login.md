# Test Case Register — Login

| Field                | Value                                         |
| -------------------- | --------------------------------------------- |
| **Version**          | 1.0                                           |
| **Last updated**     | 2026-07-01                                    |
| **Feature**          | Login                                         |
| **SRS ref**          | [[01_SRS/login/epic]]                         |
| **Jira tickets**     | `RC-6`, `RC-66`, `RC-26` (parent epic `RC-4`) |
| **Owner**            | QC Team                                       |
| **Reviewer**         | —                                             |
| **Sprint / Release** | —                                             |

> Traced to AC spec `02_Acceptance_Criteria/login/login.md`. Every TC names the `AC-LOGIN-NN` / `BR-LOGIN-NN` it verifies. TC priority = the verifying AC's criticality. New TCs: `Coverage: 🔵 Pending`, `Status: ⬜ Not Run` — detailed steps are written by the Cucumber automation layer.

## Coverage Summary

| Total TCs | Automated | Manual | Pending | Coverage % |
| --------- | --------- | ------ | ------- | ---------- |
| 16        | 0         | 0      | 16      | 0%         |

| Critical | High | Medium | Low |
| -------- | ---- | ------ | --- |
| 5        | 6    | 5      | 0   |

## Test Case Table

### 1. Login entry points

| TC ID        | Test Scenario                              | AC                          | Jira                                                     | Priority    | Coverage   | Cucumber Tag     | Preconditions                       | Test Data                     | High-level Steps                                                        | Expected Result                                                    | Status    | Note |
| ------------ | ------------------------------------------ | --------------------------- | -------------------------------------------------------- | ----------- | ---------- | ---------------- | ----------------------------------- | ----------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------- | --------- | ---- |
| TC-LOGIN-001 | Open Login page from landing               | AC-LOGIN-01                 | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | 🔴 Critical | 🔵 Pending | `@TC-LOGIN-001` | App open, user not logged in        | —                             | 1. Open app on landing screen<br>2. Tap **Login**                       | Login page opens with Email address and Password fields           | ⬜ Not Run |      |
| TC-LOGIN-002 | Login popup when guest opens login-only feature | AC-LOGIN-02<br>BR-LOGIN-04 | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | 🟠 High     | 🔵 Pending | `@TC-LOGIN-002` | Guest on home page                  | feature: *Unfallhilfe*        | 1. Continue as a guest<br>2. Tap a login-only feature (e.g. Unfallhilfe)          | The app asks the user to log in first; the feature does not open                   | ⬜ Not Run |      |
| TC-LOGIN-003 | Continue as guest                          | AC-LOGIN-03                 | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | 🟡 Medium   | 🔵 Pending | `@TC-LOGIN-003` | User not logged in, on landing      | —                             | 1. Tap **Continue as a guest**                                          | Home page for non-logged-in users is shown; login-only features inactive | ⬜ Not Run |      |
| TC-LOGIN-004 | Navigate to registration                   | AC-LOGIN-04                 | [RC-26](https://motionscloud.atlassian.net/browse/RC-26) | 🟡 Medium   | 🔵 Pending | `@TC-LOGIN-004` | User not logged in, on landing      | —                             | 1. Tap **"Don't have an account? Register"**                            | The registration page opens                                       | ⬜ Not Run |      |

### 2. Login — happy path

| TC ID        | Test Scenario                    | AC                          | Jira                                                   | Priority    | Coverage   | Cucumber Tag     | Preconditions                     | Test Data                                              | High-level Steps                                                                                 | Expected Result                                                              | Status    | Note |
| ------------ | -------------------------------- | --------------------------- | ------------------------------------------------------ | ----------- | ---------- | ---------------- | --------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | --------- | ---- |
| TC-LOGIN-005 | Log in with valid credentials    | AC-LOGIN-05<br>BR-LOGIN-01 | [RC-6](https://motionscloud.atlassian.net/browse/RC-6) | 🔴 Critical | 🔵 Pending | `@TC-LOGIN-005` | Registered active account exists  | email: valid registered<br>password: correct          | 1. Enter valid email + password<br>2. Pass "I'm not a robot"<br>3. Tap **Login**                 | Login succeeds, a session is created, and the login-only features become active  | ⬜ Not Run |      |

### 3. Login — validation & errors

| TC ID        | Test Scenario                        | AC                          | Jira                                                     | Priority    | Coverage   | Cucumber Tag     | Preconditions              | Test Data                                          | High-level Steps                                                                       | Expected Result                                                                       | Status    | Note                 |
| ------------ | ------------------------------------ | --------------------------- | -------------------------------------------------------- | ----------- | ---------- | ---------------- | -------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------- | -------------------- |
| TC-LOGIN-006 | Reject login with wrong password     | AC-LOGIN-06                 | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | 🔴 Critical | 🔵 Pending | `@TC-LOGIN-006` | Registered account exists  | email: valid<br>password: incorrect               | 1. Enter valid email + wrong password<br>2. Pass captcha<br>3. Tap **Login**           | An error message is shown and no session is created                                   | ⬜ Not Run |                      |
| TC-LOGIN-007 | Reject invalid email format          | AC-LOGIN-07<br>BR-LOGIN-02 | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | 🟠 High     | 🔵 Pending | `@TC-LOGIN-007` | On Login page              | email: `John.xyx` (invalid)                        | 1. Enter an invalid-format email<br>2. Move focus off the field                        | Inline **"Invalid email address"** error is shown and the **Login** button is disabled | ⬜ Not Run |                      |
| TC-LOGIN-008 | Login disabled when password empty   | BR-LOGIN-01                 | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | 🔴 Critical | 🔵 Pending | `@TC-LOGIN-008` | On Login page              | email: valid<br>password: empty                    | 1. Enter valid email<br>2. Leave password empty<br>3. Pass captcha                     | The **Login** button is disabled                                                      | ⬜ Not Run |                      |
| TC-LOGIN-009 | Login disabled until anti-bot passed | AC-LOGIN-10<br>BR-LOGIN-01 | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | 🟠 High     | 🔵 Pending | `@TC-LOGIN-009` | On Login page              | email: valid<br>password: valid<br>captcha: unchecked | 1. Enter valid email + password<br>2. Leave "I'm not a robot" unchecked<br>3. Complete it | The **Login** button is disabled until captcha is passed, then becomes enabled        | ⬜ Not Run |                      |
| TC-LOGIN-016 | Login disabled when email empty      | BR-LOGIN-01<br>BR-LOGIN-02  | [RC-6](https://motionscloud.atlassian.net/browse/RC-6)   | 🔴 Critical | 🔵 Pending | `@TC-LOGIN-016` | On Login page              | email: empty<br>password: valid                    | 1. Leave email empty<br>2. Enter valid password<br>3. Pass captcha                     | Inline **"Invalid email address"** error is shown and the **Login** button is disabled | ⬜ Not Run |                      |

### 4. Login — password & session

| TC ID        | Test Scenario                | AC                          | Jira                                                   | Priority  | Coverage   | Cucumber Tag     | Preconditions                          | Test Data           | High-level Steps                                              | Expected Result                                                | Status    | Note                       |
| ------------ | ---------------------------- | --------------------------- | ------------------------------------------------------ | --------- | ---------- | ---------------- | -------------------------------------- | ------------------- | ------------------------------------------------------------ | -------------------------------------------------------------- | --------- | -------------------------- |
| TC-LOGIN-010 | Toggle password visibility   | AC-LOGIN-08<br>BR-LOGIN-03 | [RC-6](https://motionscloud.atlassian.net/browse/RC-6) | 🟡 Medium | 🔵 Pending | `@TC-LOGIN-010` | On Login page, password typed (masked) | password: any       | 1. Tap the reveal (eye) control<br>2. Tap it again           | The password becomes visible, then is masked again             | ⬜ Not Run |                            |
| TC-LOGIN-011 | Remember me persists session | AC-LOGIN-09                 | [RC-6](https://motionscloud.atlassian.net/browse/RC-6) | 🟡 Medium | 🔵 Pending | `@TC-LOGIN-011` | Registered account                     | Remember me: on     | 1. Enable **Remember me**<br>2. Log in successfully<br>3. Restart the app | The user remains logged in after restart                       | ⬜ Not Run | `[DEP]` persist policy TBD |

### 5. Forgot password

| TC ID        | Test Scenario                                  | AC          | Jira                                                     | Priority  | Coverage   | Cucumber Tag     | Preconditions                          | Test Data                     | High-level Steps                                     | Expected Result                                                              | Status    | Note                        |
| ------------ | ---------------------------------------------- | ----------- | -------------------------------------------------------- | --------- | ---------- | ---------------- | -------------------------------------- | ----------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------- | --------- | --------------------------- |
| TC-LOGIN-012 | Open Forgot Password screen                    | AC-LOGIN-11 | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | 🟠 High   | 🔵 Pending | `@TC-LOGIN-012` | On Login page                          | —                             | 1. Tap **Forgot Password?**                          | The "Enter your registered email" screen opens                               | ⬜ Not Run |                             |
| TC-LOGIN-013 | Send reset code to registered email            | AC-LOGIN-12 | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | 🟠 High   | 🔵 Pending | `@TC-LOGIN-013` | On "Enter your registered email"       | email: registered             | 1. Enter a registered email<br>2. Tap **Next**       | A verification code is sent and the code-entry step opens                    | ⬜ Not Run |                             |
| TC-LOGIN-014 | Reject unregistered email on reset             | AC-LOGIN-13 | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | 🟠 High   | 🔵 Pending | `@TC-LOGIN-014` | On "Enter your registered email"       | email: unregistered / invalid | 1. Enter an unregistered email<br>2. Tap **Next**    | An error message is shown and no code is sent                                | ⬜ Not Run |                             |
| TC-LOGIN-015 | Password reset cannot be completed (limitation) | AC-LOGIN-14 | [RC-66](https://motionscloud.atlassian.net/browse/RC-66) | 🟡 Medium | 🔵 Pending | `@TC-LOGIN-015` | Reached the reset-password step        | new password: any             | 1. Enter a new password                              | "Password strength: Okay" is always shown and the user cannot proceed        | ⬜ Not Run | `[BUG]` confirm scope RC-66 |

## Gherkin Mapping (Automated TCs only)

> Added as automation is implemented — each scenario tagged with its `@TC-LOGIN-NNN` for result tracing. None automated yet.
