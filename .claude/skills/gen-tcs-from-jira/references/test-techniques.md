# Test design techniques checklist

Apply every technique that fits the requirement and the screenshots. Skip one only when it genuinely does not apply, and say why in the report.

Keep each TC **high-level** — one scenario + an observable expected result. Do NOT write click-by-click steps; the automation layer (Cucumber) owns the detail. These techniques say _what to cover_, not how to script it.

## 1. Positive / happy path

- The main success scenario for each requirement / flow described in the ticket.
- Each valid alternate flow (e.g. login via email vs. via SSO).

## 2. Negative

- Wrong/invalid input per field (wrong format, wrong type, wrong credentials).
- Required field left empty.
- Action attempted in an invalid state (e.g. submit while disabled, expired session).
- Unauthorized access / permission denied.

## 3. Boundary Value Analysis (BVA)

For every input with a range or length limit, test: min−1, min, min+1, max−1, max, max+1.

- String length limits, numeric ranges, date ranges, file size/count limits.

## 4. Equivalence Partitioning (EP)

- One representative value per valid class and per invalid class, so you cover classes without exploding the count.

## 5. Field-level validation (from the screenshot or requirement)

For each user input defined by the requirement or visible in the UI.

- Format validation (email, phone, currency, date).
- Inline error message wording and trigger (on blur / on submit).
- Mandatory marker vs. optional.
- Max length / character restrictions / paste behavior.
- Default value, placeholder, masking (passwords).

## 6. UI / UX states (from the screenshot)

- Empty state, populated state, loading/skeleton, success, error.
- Disabled vs. enabled controls and what enables them.
- Responsive / different breakpoints if the design shows them.
- Element presence, labels, button states, focus order.

## 7. Error & resilience

- Network failure / timeout / slow response.
- Server-side error (4xx/5xx) handling and message shown.
- Partial data / null / missing fields from the backend.
- Concurrent action / double-submit.

## 8. Edge cases

Beyond BVA (§3, numeric/length ranges) and concurrency (§7), push inputs to their limits:

- null / emptiness: null, empty, whitespace-only, missing field, default value.
- characters: special chars, Unicode / emoji, leading / trailing spaces, very long text.
- collections: zero / one / many, max+1, duplicate values, ordering.
- date / time: timezone, DST, leap year, expired vs future dates.
- localization / RTL, if relevant.
- accessibility basics: keyboard navigation, screen-reader labels (note if in scope).

## 9. Non-functional

Test quality attributes where in scope (mirrors AC §3 Non-functional):

- performance: response time / load / large datasets (e.g. P95 < 2s).
- security: authn / authz, input sanitisation (XSS / SQLi), sensitive-data exposure, rate limiting.
- accessibility: WCAG 2.1 AA — keyboard, screen-reader, contrast, focus order (basics also §8).
- compatibility: supported devices / OS / browsers / screen sizes (responsive also §6).
- localization / i18n: language, date / number / currency formats, RTL (also §8).
- reliability: see §7 Error & resilience.
- observability: audit log / events recorded for key actions.

## Quality bar (reject a TC that fails any)

- **Atomic** — one scenario / one purpose per TC.
- **Clear expected result** — observable, objectively pass/fail (status / message / state / value).
- **High-level** — says WHAT to verify, not click-by-click steps (automation owns detail).
- **Self-contained** — preconditions + test data stated, so it runs independently and repeatably.
- **Traceable** — names the AC / requirement it verifies; no orphan TC.
- **Unambiguous** — one interpretation; no vague wording.

## Prioritization

Set each TC's priority = the criticality of the AC it verifies (1:1, AC §6). When there is no AC, judge by business impact if it fails:

- **🔴 Critical** — core happy path or security / data-integrity. Must pass to ship.
- **🟠 High** — important validation / common error state; no clean workaround.
- **🟡 Medium** — secondary behaviour; tolerable short-term.
- **⚪ Low** — edge, cosmetic, rare state.

## Coverage rule

Check both directions, then report:

- **AC / requirement → TC** — every Critical/High AC, every business rule, and every described behaviour maps to ≥1 TC.
- **TC → AC** — every TC names the AC / requirement it verifies; no orphan TC.
- **Report** — breakdown by theme and criticality; note which techniques were intentionally skipped and why; flag anything uncovered.

## Final check before handoff

- [ ] Every Critical/High AC has ≥1 TC (Coverage rule)
- [ ] Every TC traces to an AC / requirement — no orphan (Coverage rule)
- [ ] Every TC has a clear, observable expected result (Quality bar)
- [ ] Each TC is one scenario, kept high-level — no click-by-click (Quality bar)
- [ ] Preconditions + test data stated where needed
- [ ] Priority set on every TC (= AC criticality)
- [ ] Negative (§2), boundary (§3/§8), and NFR (§9) covered where applicable
- [ ] Skipped techniques noted with reason
