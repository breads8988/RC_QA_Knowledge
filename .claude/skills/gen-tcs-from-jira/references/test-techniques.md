# Test design techniques (BABOK-aligned)

How a senior QA engineer designs test cases from a requirement. Apply only the techniques that add meaningful coverage. State explicitly when a technique is not applicable, and say why in the report.

Keep each TC **high-level** — one scenario + an observable expected result. Do NOT write click-by-click steps; the automation layer (Cucumber) owns the detail. These techniques say _what to cover_, not how to script it.

## When to use acceptance criteria

Acceptance criteria are **recommended** for medium and complex requirements.

For simple, low-risk requirements (e.g. typo fix, label change, single optional field), test cases may be designed **directly from the requirement**, provided full requirement coverage is maintained. Set the TC's **AC** column to `—`.

```
Requirement
│
├──► Acceptance Criteria (recommended)
│         │
│         └──► Test Cases
│
└────────────────► Test Cases (when AC is intentionally omitted)
```

## 1. Analyse the requirement first

This step drives most of TC quality. Before designing any test case, identify:

- **Functional requirements** — what the system must do.
- **Business rules** — constraints, policies, limits, formulas.
- **Acceptance criteria** — read `02_Acceptance_Criteria/<feature>.md` when it exists; it is the primary source.
- **Actors / roles** — who performs the action and who is affected.
- **Preconditions** — conditions that must already be true.
- **Triggers** — what starts the behaviour under test.
- **Expected outcomes** — observable results, messages, persisted state.
- **State transitions** — valid and invalid lifecycle changes.
- **External dependencies** — services, APIs, integrations.
- **Assumptions** — anything unstated; flag gaps rather than inventing behaviour.

List the test conditions grouped by theme before writing TCs so coverage is visible.

## 2. Positive / happy path

- Design **at least one test case for every Happy Path acceptance criterion** when AC exist.
- Each valid alternate flow (e.g. login via email vs. via SSO).
- When AC are omitted, cover the main success scenario for each requirement / flow in the ticket.
- Trace each TC to its **AC ID** (preferred) or to the **requirement** when no AC exist.

## 3. Negative

Cover only the classes that genuinely apply:

- **Invalid input** — wrong format, wrong type, wrong credentials per field.
- **Missing required data** — required field left empty.
- **Invalid state** — action attempted while disabled, expired session, wrong workflow step.
- **Unauthorised access** — permission denied, wrong role.
- **Business rule violation** — valid input but rejected by a policy (not a format error). Examples: daily transfer limit exceeded, recipient account frozen, unsupported currency, insufficient balance, expired offer.

State the expected rejection and error message/code where known.

## 4. Boundary Value Analysis (BVA)

For every input with a range or length limit, test: min−1, min, min+1, max−1, max, max+1.

- String length limits, numeric ranges, date ranges, file size/count limits.
- Combine boundary checks into one TC when they verify the same behaviour (see §11).

## 5. Equivalence Partitioning (EP)

- One representative value per valid class and per invalid class, so you cover classes without exploding the count.

## 6. Field-level validation

For each user input **defined by the requirement or visible in the UI** (do not depend on screenshots alone).

- Format validation (email, phone, currency, date).
- Inline error message wording and trigger (on blur / on submit).
- Mandatory marker vs. optional.
- Max length / character restrictions / paste behavior.
- Default value, placeholder, masking (passwords).

## 7. UI / UX states

Apply **where UI is provided** (screenshot, design spec, or ticket description).

- Empty state, populated state, loading/skeleton, success, error.
- Disabled vs. enabled controls and what enables them.
- Responsive / different breakpoints if the design shows them.
- Element presence, labels, button states, focus order.

## 8. Error & resilience

- Network failure / timeout / slow response.
- Server-side error (4xx/5xx) handling and message shown.
- Partial data / null / missing fields from the backend.
- Concurrent action / double-submit.

## 9. Edge cases

Beyond BVA (§4, numeric/length ranges) and concurrency (§8), push inputs to their limits:

- null / emptiness: null, empty, whitespace-only, missing field, default value.
- characters: special chars, Unicode / emoji, leading / trailing spaces, very long text.
- collections: zero / one / many, max+1, duplicate values, ordering.
- date / time: timezone, DST, leap year, expired vs future dates.
- localization / RTL, if relevant.
- accessibility basics: keyboard navigation, screen-reader labels (note if in scope).

## 10. Non-functional

Include **only when explicitly required or implied by the requirement** (mirrors AC §3 Non-functional):

- performance: response time / load / large datasets (e.g. P95 < 2s).
- security: authn / authz, input sanitisation (XSS / SQLi), sensitive-data exposure, rate limiting.
- accessibility: WCAG 2.1 AA — keyboard, screen-reader, contrast, focus order (basics also §9).
- compatibility: supported devices / OS / browsers / screen sizes (responsive also §7).
- localization / i18n: language, date / number / currency formats, RTL (also §9).
- reliability: see §8 Error & resilience.
- observability: audit log / events recorded for key actions.

## 11. Test design optimization

Avoid redundant test cases. Prefer combining compatible checks into one TC when they verify the same behaviour.

Split into multiple TCs only when:

- expected outcome differs
- preconditions differ
- business rule differs
- priority differs

Do not create separate TCs for every boundary value when one TC can represent the partition (use EP §5).

## Quality bar (reject a TC that fails any)

- **Atomic** — one scenario / one purpose per TC.
- **Clear expected result** — observable, objectively pass/fail (status / message / state / value).
- **High-level** — says WHAT to verify, not click-by-click steps (automation owns detail).
- **Self-contained** — preconditions + test data stated, so it runs independently and repeatably.
- **Traceable** — names the AC / business rule / requirement it verifies; no orphan TC.
- **Unambiguous** — one interpretation; no vague wording.

## Prioritization

Assign each TC a priority **based on the criticality of the acceptance criterion it verifies** (1:1 with AC §6). When there is no AC, judge by business impact if it fails:

- **🔴 Critical** — core happy path or security / data-integrity. Must pass to ship.
- **🟠 High** — important validation / common error state; no clean workaround.
- **🟡 Medium** — secondary behaviour; tolerable short-term.
- **⚪ Low** — edge, cosmetic, rare state.

Chain: Requirement → AC (Criticality) → TC Priority.

## Traceability

Every test case shall reference:

- **Requirement ID** — the Jira ticket key (recorded in the **Jira** column).
- **AC ID** — `AC-<CODE>-NN` or `BR-<CODE>-NN` when AC exist; `—` when designed directly from the requirement.
- **Business rule** — when the TC verifies a business rule, name the `BR-<CODE>-NN` ID.

No orphan TC. No TC that cannot be traced back to a requirement.

## Coverage rule

Every requirement must be covered by one or more test cases.

Where acceptance criteria are available, design test cases against the acceptance criteria.

Where acceptance criteria are intentionally omitted (e.g. simple or low-risk changes), design test cases directly from the requirement.

Every business rule must be verified by at least one test case.

Check both directions, then report:

- **Requirement → TC** — every described behaviour in the ticket maps to ≥1 TC.
- **AC → TC** (when AC exist) — every `Critical` and `High` AC maps to ≥1 TC.
- **Business rule → TC** — every business rule maps to ≥1 TC.
- **TC → source** — every TC names the AC / business rule / requirement it verifies.
- **Report** — breakdown by theme and criticality; note which techniques were not applicable and why; flag anything uncovered.

## Final check before handoff

Quick gate before QA Lead review — verify, don't re-explain (section it enforces in brackets):

- [ ] Every requirement covered by ≥1 TC (Coverage rule)
- [ ] Every Critical / High AC covered by ≥1 TC when AC exist (Coverage rule)
- [ ] Every business rule covered by ≥1 TC (Coverage rule)
- [ ] No duplicate TC — optimization applied (§11)
- [ ] Every TC traces to AC / requirement — no orphan (Traceability)
- [ ] Every TC has a clear, observable expected result (Quality bar)
- [ ] Each TC is one scenario, kept high-level — no click-by-click (Quality bar)
- [ ] Preconditions + test data stated where needed
- [ ] Priority set on every TC (= AC criticality, or business impact when no AC)
- [ ] Negative (§3), boundary (§4/§9), and NFR (§10) covered where applicable
- [ ] Techniques not applied are stated with reason

## Example (login feature)

**TC-LOGIN-001** (🔴 Critical, verifies **AC-LOGIN-01**): Registered user submits valid credentials → login succeeds and session is created.

**TC-LOGIN-002** (🔴 Critical, verifies **AC-LOGIN-03**): Registered user submits wrong password → login rejected with `AUTH_INVALID_CREDENTIALS`, no session created.

**TC-LOGIN-003** (🔴 Critical, verifies **BR-LOGIN-01**): Sixth consecutive failed login within the lockout window → account locked for 15 minutes.
