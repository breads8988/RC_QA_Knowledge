# AC writing techniques (BABOK-aligned)

How a senior BA decomposes a requirement into acceptance criteria. Apply every technique that fits; skip one only when it genuinely doesn't apply.

## 1. Analyse the requirement first

This step drives ~70% of AC quality. Before writing any AC, identify:

- **Functional requirements** — what the system must do.
- **Business rules** — constraints, policies, limits, formulas.
- **Actors** — who/what interacts (users, roles, systems).
- **Preconditions** — conditions that must already be true before the behaviour can occur.
- **Triggers** — what starts the behaviour.
- **Outputs** — results, messages, data produced.
- **State changes** — what persists or transitions.
- **External dependencies** — services, APIs, integrations.
- **Impacted existing behaviour** — existing rules / flows this change modifies or may break (feeds downstream regression).
- **Assumptions** — anything unstated you assumed (flag for §7).

Then frame it: restate as **As a** `<role>` **I want** `<capability>` **so that** `<benefit>`, and INVEST-check the story (Independent, Negotiable, Valuable, Estimable, Small, **Testable**).

## 2. Choose the form per requirement

- **Given / When / Then** — for observable behaviour and flows (most AC). One scenario = one outcome.
- **Business rule** — a reusable policy that applies across multiple scenarios, such as:

  - validation
  - calculation
  - authorization
  - state transition
  - time-based policy
  - configuration / feature flag
  - country or regulatory rule
  - data integrity

  Keep reusable business rules separate from GWT.
  Use GWT only to verify the observable behaviour when those rules are applied.

## 3. Scenario coverage — write one AC per class

For each capability, cover only the classes that genuinely apply (not every class fits every capability):

- **Happy path** — the main success scenario, valid inputs, authorised user.
- **Alternate flow** — other valid ways to reach success (e.g. login by email vs phone).
- **Negative** — invalid input, missing required field, wrong state, unauthorised access. State the rejection + the error message/code.
- **Rule / condition combinations** — when the outcome depends on a *combination* of conditions (eligibility, pricing, tiered permissions), enumerate the meaningful combinations (decision-table thinking); write an AC or business rule for each distinct outcome, plus the default/else.
- **Boundary / edge** — push every input to its limits:
  - numeric: min−1 / min / max / max+1, zero, negative, overflow, decimal precision / rounding
  - length: empty, min, max, max+1 (truncation)
  - null / emptiness: null, empty, whitespace-only, missing field, default value
  - characters: special chars, Unicode / emoji, leading / trailing spaces
  - collections: zero / one / many, max+1, duplicate values, ordering
  - date / time: timezone, DST, leap year, expired vs future dates
  - concurrency: concurrent updates, duplicate / double submission, stale data
- **Permission** — who can / cannot perform the action, and what each sees.
- **State transitions** — valid and invalid transitions if the entity has a lifecycle.
- **Non-functional / quality attributes** — cross-cutting; write as their own AC where they apply:
  - performance: response-time / throughput targets (e.g. P95 < 2s)
  - security: authn / authz, data protection, input sanitisation, rate limiting
  - accessibility: WCAG 2.1 AA — keyboard, screen-reader, contrast
  - compatibility: supported devices / OS / browsers
  - localization / i18n: language, date / number / currency formats, RTL
  - reliability: availability, graceful degradation, recovery
  - observability: audit log / events for key actions

## 4. Write each Given / When / Then well

- **Given** = preconditions/context that are already true. Compound with `And`.
- **When** = the single action or event under test. Keep it to one trigger.
- **Then** = the observable, verifiable result. Must be objectively pass/fail — include status, error code, message, computed value, or persisted state when applicable. Compound consequences with `And`; contrast with `But`.
- Describe the **what**, never the **how** — no UI clicks, no API/DB/tech detail. ("Then the transfer is rejected", not "Then the red toast `.error-banner` appears").
- **Illustrate with concrete examples** — for rules, calculations, and boundaries, pin down real example values (e.g. *balance $100, transfer $150 → rejected*). Examples make the AC unambiguous and directly testable (Specification by Example).

## 5. Quality bar (reject an AC that fails any)

- **Testable** — you can write a pass/fail check for the Then.
- **Unambiguous** — no "fast", "user-friendly", "appropriate", "etc." Quantify everything.
- **Atomic** — one outcome per AC; split compound criteria.
- **Consistent** — no contradiction with other AC or business rules.
- **Complete** — together the AC cover every described behaviour; no silent gap.
- **Implementation-free** — survives a UI/tech redesign.
- **Traceable** — every AC maps back to a requirement or business rule (recorded via the Jira column); no orphan or invented AC.

## 6. Rate criticality (impact if it fails)

Rate each AC by the business impact if it fails — NOT MoSCoW (MoSCoW scopes stories/features, not AC). This should guide the priority of downstream test design and execution.

- **🔴 Critical** — core behaviour, or security / data-integrity failure. Must pass to ship.
- **🟠 High** — important behaviour; a failure has no clean workaround.
- **🟡 Medium** — secondary behaviour; failure is tolerable short-term.
- **⚪ Low** — cosmetic or rare edge; minimal impact.

## 7. Surface the gaps (BA duty)

- List every assumption you had to make and every ambiguity the ticket left open as **open questions** for stakeholders — do not invent business rules to fill silence.
- An AC built on an unconfirmed assumption must be flagged.

## 8. Coverage rule

Check coverage in both directions, then report:

- **Requirement → AC** — every functional requirement, business rule, and user-visible behaviour in the ticket maps to at least one AC. Nothing described is left without an AC.
- **AC → Test** — every `Critical` and `High` AC and every business rule must be coverable by at least one downstream test case.
- **Report** — show the count by type / criticality, note which scenario classes were intentionally skipped and why, and flag anything uncovered in either direction.

## 9. Final check before handoff

Quick gate before QA Lead review — verify, don't re-explain (section it enforces in brackets):

- [ ] Every requirement has ≥1 AC (§8)
- [ ] Every AC is testable (§5)
- [ ] Business rules kept out of GWT (§2)
- [ ] No implementation details (§4)
- [ ] No ambiguous wording (§5)
- [ ] Error messages/codes specified where applicable (§4)
- [ ] Permissions covered (§3)
- [ ] State transitions covered (§3)
- [ ] Boundary cases identified (§3)
- [ ] Rule / condition combinations covered where outcomes combine (§3)
- [ ] Non-functional aspects covered where applicable (§3)
- [ ] Open questions documented (§7)
- [ ] All assumptions are either confirmed or explicitly flagged (§7)

## Example (login feature)

GWT AC — **AC-LOGIN-03** (Negative, 🔴 Critical): Given a registered user, When they submit a wrong password, Then login is rejected with error `AUTH_INVALID_CREDENTIALS` and no session is created.

Business rule — **BR-LOGIN-01** (🔴 Critical): Account locks for 15 minutes after 5 consecutive failed logins.
