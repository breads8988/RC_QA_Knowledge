# AC writing techniques (BABOK-aligned)

How a senior BA decomposes a requirement into acceptance criteria. Apply every technique that fits; skip one only when it genuinely doesn't apply.

## 1. Analyse the requirement first

This step drives ~70% of AC quality. Before writing any AC, identify:

- **Functional requirements** — what the system must do.
- **Business rules** — constraints, policies, limits, formulas.
- **Actors** — who/what interacts (users, roles, systems).
- **Preconditions** — state that must be true before.
- **Triggers** — what starts the behaviour.
- **Outputs** — results, messages, data produced.
- **State changes** — what persists or transitions.
- **External dependencies** — services, APIs, integrations.
- **Assumptions** — anything unstated you assumed (flag for §7).

Then frame it: restate as **As a** `<role>` **I want** `<capability>` **so that** `<benefit>`, and INVEST-check the story (Independent, Negotiable, Valuable, Estimable, Small, **Testable**).

## 2. Choose the form per requirement

- **Given / When / Then** — for observable behaviour and flows (most AC). One scenario = one outcome.
- **Business rule** — for constraints/policies/limits/formulas/permissions that apply across scenarios (e.g. "password 8–32 chars", "session expires after 15 min"). Don't force these into GWT.

## 3. Scenario coverage — write one AC per class

For each capability, cover:

- **Happy path** — the main success scenario, valid inputs, authorised user.
- **Alternate flow** — other valid ways to reach success (e.g. login by email vs phone).
- **Negative** — invalid input, missing required field, wrong state, unauthorised access. State the rejection + the error message/code.
- **Boundary / edge** — min−1 / min / max / max+1 for any limit; empty, very long, special chars, timezone/leap-year dates, concurrency/double-submit.
- **Permission** — who can / cannot perform the action, and what each sees.
- **State transitions** — valid and invalid transitions if the entity has a lifecycle.

## 4. Write each Given / When / Then well

- **Given** = preconditions/context that are already true. Compound with `And`.
- **When** = the single action or event under test. Keep it to one trigger.
- **Then** = the observable, verifiable result. Must be objectively pass/fail — include status, error code, message, computed value, or persisted state where relevant. Compound consequences with `And`; contrast with `But`.
- Describe the **what**, never the **how** — no UI clicks, no API/DB/tech detail. ("Then the transfer is rejected", not "Then the red toast `.error-banner` appears").

## 5. Quality bar (reject an AC that fails any)

- **Testable** — you can write a pass/fail check for the Then.
- **Unambiguous** — no "fast", "user-friendly", "appropriate", "etc." Quantify everything.
- **Atomic** — one outcome per AC; split compound criteria.
- **Consistent** — no contradiction with other AC or business rules.
- **Complete** — together the AC cover every described behaviour; no silent gap.
- **Implementation-free** — survives a UI/tech redesign.

## 6. Prioritise (MoSCoW)

- **Must** — release-blocking; core behaviour + critical negative/security/data-integrity.
- **Should** — important but has a workaround for this release.
- **Could** — nice-to-have, low impact.
- **Won't** — explicitly out of scope this time (record it so it's not forgotten).

## 7. Surface the gaps (BA duty)

List every assumption you had to make and every ambiguity the ticket left open as **open questions** for stakeholders — do not invent business rules to fill silence. An AC built on an unconfirmed assumption must be flagged.

## 8. Coverage rule

Check coverage in both directions, then report:

- **Requirement → AC** — every functional requirement, business rule, and user-visible behaviour in the ticket maps to at least one AC. Nothing described is left without an AC.
- **AC → Test** — every `Must` AC and every business rule must be coverable by at least one downstream test case.
- **Report** — show the count by type/priority and flag anything uncovered in either direction.
