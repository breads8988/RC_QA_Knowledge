# Test design techniques checklist

Apply every technique that fits the requirement and the screenshots. Skip one only when it genuinely does not apply, and say why in the report.

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

## 5. Field-level validation (from the screenshot)
For each input visible in the UI:
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
- Boundary dates (timezone, leap year), special characters/emoji/unicode, very long text.
- Localization / RTL if relevant.
- Accessibility basics: keyboard navigation, screen-reader labels (note if in scope).

## Prioritization
Assign each TC a priority:
- **P1** — core happy path + critical negative (security, data loss). Must pass to ship.
- **P2** — important validations and common error states.
- **P3** — edge cases, cosmetic, rare states.

## Coverage rule
Every requirement / scenario described in the ticket must map to at least one TC. In the final report, show the breakdown by theme/group and flag any described behaviour left with zero coverage.
