# Test design techniques (BABOK-aligned)

How a senior QA engineer designs test cases from a requirement. Apply only the techniques that add meaningful coverage. State explicitly when a technique is not applicable, and say why in the report.

Keep each TC **high-level** — one scenario + an observable expected result. Do NOT write click-by-click steps; the automation layer (Cucumber) owns the detail. These techniques say _what to cover_, not how to script it.

## When to use acceptance criteria

Acceptance criteria are **recommended** for medium and complex requirements.

For simple, low-risk requirements (e.g. typo fix, label change, single optional field), test cases may be designed **directly from the requirement**, provided full requirement coverage is maintained. Set the TC's **AC** column to `—`.

The absence of acceptance criteria must not reduce test coverage.

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
- **Impacted existing areas** — shared components / flows / data this change may affect (feeds §15).
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

During analysis, identify the boundary values for every input with a defined range or length limit: min−1, min, min+1, max−1, max, max+1 (e.g. string length, numeric ranges, dates, file size/count).

- These are the boundary values to **cover**, not a requirement to create six separate test cases.
- Use Equivalence Partitioning (§5) to group boundary values that produce the same expected outcome into a single TC.
- Split into multiple TCs only when the expected outcome, business rule, or preconditions differ (§16).

## 5. Equivalence Partitioning (EP)

- One representative value per valid class and per invalid class, so you cover classes without exploding the count.

## 6. Decision Table Testing

Use when an outcome depends on a **combination of conditions** (eligibility, pricing, permissions, discounts). BVA/EP test one variable — they miss bad combinations.

- List the conditions and the resulting actions/outcomes.
- Build rules = combinations of condition values → expected action; drop impossible ones.
- Write **one TC per meaningful rule** (not per cell); merge rules with the same outcome via EP (§5).
- Cover every rule with a distinct outcome, plus the default/else rule.
- Not applicable with a single condition or non-interacting conditions — say so.

## 7. Pairwise / all-pairs (combinatorial)

Use **only when many independent parameters combine** and the full cross-product is too large (e.g. plan × role × country × currency × device). Few interacting conditions → use Decision Table (§6) instead.

- Identify the parameters and their values.
- Cover **all pairs** of values rather than every full combination — most defects come from 2-way interactions.
- Add back any business-critical full combination the pairwise set skips.
- One selected combination = one high-level TC.
- State when not applicable (few parameters / no interaction).

## 8. State Transition Testing

Use when the entity has a **lifecycle / status** (draft→submitted→approved→paid; active/locked/closed). Identified in §1 — turn it into coverage here.

- **Valid transitions** — each allowed state+event → correct next state (≥1 TC each).
- **Invalid / blocked transitions** — event not allowed in the current state → rejected, state unchanged, correct message.
- **Guards** — conditions gating a transition (e.g. balance ≥ 0 to close).
- Note the state model (short table/list) so coverage is visible.
- Not applicable to stateless actions — say so.

## 9. Field-level validation

For each user input **defined by the requirement or visible in the UI** (do not depend on screenshots alone).

- Format validation (email, phone, currency, date).
- Inline error message wording and trigger (on blur / on submit).
- Mandatory marker vs. optional.
- Max length / character restrictions / paste behavior.
- Default value, placeholder, masking (passwords).

## 10. UI / UX states

Apply **where UI is provided** (screenshot, design spec, or ticket description).

- Empty state, populated state, loading/skeleton, success, error.
- Disabled vs. enabled controls and what enables them.
- Responsive / different breakpoints if the design shows them.
- Element presence, labels, button states, focus order.

## 11. Error & resilience

- Network failure / timeout / slow response.
- Server-side error (4xx/5xx) handling and message shown.
- Partial data / null / missing fields from the backend.
- Concurrent action / double-submit.

## 12. Edge cases

Beyond BVA (§4, numeric/length ranges) and concurrency (§11), push inputs to their limits:

- null / emptiness: null, empty, whitespace-only, missing field, default value.
- characters: special chars, Unicode / emoji, leading / trailing spaces, very long text.
- collections: zero / one / many, max+1, duplicate values, ordering.
- date / time: timezone, DST, leap year, expired vs future dates.
- localization / RTL, if relevant.
- accessibility basics: keyboard navigation, screen-reader labels (note if in scope).

## 13. Non-functional

Include **only when explicitly required or implied by the requirement** (mirrors AC §3 Non-functional):

- performance: response time / load / large datasets (e.g. P95 < 2s).
- security: authn / authz, input sanitisation (XSS / SQLi), sensitive-data exposure, rate limiting.
- accessibility: WCAG 2.1 AA — keyboard, screen-reader, contrast, focus order (basics also §12).
- compatibility: supported devices / OS / browsers / screen sizes (responsive also §10).
- localization / i18n: language, date / number / currency formats, RTL (also §12).
- reliability: see §11 Error & resilience.
- observability: audit log / events recorded for key actions.

## 14. Test Data Design

State the data each TC needs so it runs independently (Quality bar: self-contained). Design across classes, not one happy value:

- **Representative** — one valid value per equivalence class (§5).
- **Boundary** — min/max and just-outside values (§4).
- **Invalid** — wrong type/format/out-of-range to drive negatives (§3).
- **Stateful / precondition** — data already in the required state (locked account, expired offer) so preconditions are real.
- **Synthetic & safe** — never real PII/secrets; fabricated but realistic; note any seed/fixture.
- Reference data in the TC's preconditions — automation (Cucumber) owns concrete values.

## 15. Regression Impact Analysis

A change rarely touches only new behaviour. For every ticket, identify what **existing** functionality it can affect and ensure coverage.

- **Impacted areas** — shared components, common flows, APIs, or data the change touches (from §1).
- **Regression TCs** — per impacted area, confirm existing behaviour still holds (reuse existing TCs; add/flag where missing).
- **Depth by risk** — cover in proportion to risk (see Prioritization risk lens); don't blanket-retest.
- **Flag, don't hide** — if an impacted area can't be covered here, call it out in the report.
- Every ticket states its regression impact — even "none, isolated new feature".

## 16. Test design optimization

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

Apply a **risk lens** — where likelihood × impact of failure is high (money movement, data integrity, security, shared / regression-prone areas), test deeper (more negative, boundary, and combination cases); where low, keep it light. Risk also sets how much of §15 to run.

Chain: Requirement → AC (Criticality) → TC Priority.

## Traceability

Every test case shall reference:

- **Requirement ID** — the Jira ticket key (recorded in the **Jira** column).
- **AC ID** — `AC-<CODE>-NN` or `BR-<CODE>-NN` when AC exist; `—` when designed directly from the requirement.
- **Business rule** — when the TC verifies a business rule, name the `BR-<CODE>-NN` ID.

No orphan TC. No TC that cannot be traced back to a requirement.

## Coverage rule

- Every requirement must be covered by one or more test cases.
- Where acceptance criteria are available, design test cases against the acceptance criteria.
- Where acceptance criteria are intentionally omitted (e.g. simple or low-risk changes), design test cases directly from the requirement.
- Every business rule must be verified by at least one test case.

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
- [ ] No duplicate TC — optimization applied (§16)
- [ ] Every TC traces to AC / requirement — no orphan (Traceability)
- [ ] Every TC has a clear, observable expected result (Quality bar)
- [ ] Each TC is one scenario, kept high-level — no click-by-click (Quality bar)
- [ ] Preconditions + test data stated where needed (§14)
- [ ] Priority set on every TC (= AC criticality, or business impact when no AC)
- [ ] Negative (§3), boundary (§4/§12), and NFR (§13) covered where applicable
- [ ] Combination & lifecycle logic covered — Decision Table / Pairwise / State Transition where they apply (§6–§8)
- [ ] Regression impact stated; impacted existing areas covered or flagged (§15)
- [ ] Techniques not applied are stated with reason

## Example (login feature)

**TC-LOGIN-001** (🔴 Critical, verifies **AC-LOGIN-01**): Registered user submits valid credentials → login succeeds and session is created.

**TC-LOGIN-002** (🔴 Critical, verifies **AC-LOGIN-03**): Registered user submits wrong password → login rejected with `AUTH_INVALID_CREDENTIALS`, no session created.

**TC-LOGIN-003** (🔴 Critical, verifies **BR-LOGIN-01**): Sixth consecutive failed login within the lockout window → account locked for 15 minutes.
