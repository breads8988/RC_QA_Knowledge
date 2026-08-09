# Feature Registry

Single source of truth mapping each **feature** to its short **code**. `/gen-ac` and `/gen-tc` read this to keep IDs stable across runs. Define a feature here **once**, before generating AC/TC for it.

| Feature (slug / file) | Code    | Description                     | SRS                        |
| --------------------- | ------- | ------------------------------- | -------------------------- |
| login                 | `LOGIN` | User login / authentication     | [[01_SRS/login/epic]]      |
| registration          | `REG`   | User registration / sign-up (4-step onboarding) | [[01_SRS/registration/]] |
| my_vehicle            | `MV`    | My Vehicle management           | [[01_SRS/my_vehicle/]]     |
| user_management       | `UM`    | User management / accounts      | [[01_SRS/user_management/]] |
| lawyer                | `LAW`   | Lawyer page / accident legal advice ("Unfall Rechtsberatung") | [[01_SRS/lawyer/]] |
| expert                | `ECA`   | Find an Expert / expert call appointment (callback request + per-expert Calendly video call) | [[01_SRS/expert/]] |
| homepage              | `HOME`  | Home page (feature grid for logged-in/guest users, banner, quick menu, feature config) | [[01_SRS/homepage/]] |
| tourguide             | `TG`    | Tour guide (feature hint popups shown on first web-app access, logged-in vs not-logged-in flows) | [[01_SRS/tourguide/]] |
| my_accident           | `MA`    | My Accidents page (reported/saved accidents list, report-accident final submission, delete accident) | [[01_SRS/my_accident/]] |
| accident_assistant    | `AA`    | Accident Assistance / Unfallhilfe — Report Accident flow entry, Overview, Step 1 Accident details (location, incident type, parties involved) | [[01_SRS/accident_assistant/]] |
| workshop               | `WS`    | Workshop finder & voucher (nearby-workshop map/list search, voucher redemption code, save voucher, request appointment/callback) | [[01_SRS/workshop/]] |
| saved_voucher          | `SV`    | Saved Voucher page (lists vouchers the user saved during the Workshop flow; separate page, connected to workshop's save-voucher action) | [[01_SRS/saved_voucher/]] |
| expert_call_appointment | `ECA` | Find an Expert — list, filter, book appointment / schedule call (Calendly) | [[01_SRS/expert_call_appointment/]] |
| lawyer                | `LAW`   | Lawyer page (Unfall Rechtsberatung) — list lawyers, filter by rating, request appointment | [[01_SRS/lawyer/]] |

## Rules

- **Slug** — lowercase, matches `01_SRS/<slug>/`, `02_Acceptance_Criteria/<slug>/<slug>.md`, `03_Testcases/<slug>/<slug>.md`. This is what you pass to the commands.
- **Code** — 2–6 UPPERCASE letters, **unique**. Used only in IDs: `AC-<CODE>-NN`, `BR-<CODE>-NN`, `TC-<CODE>-NNN` (e.g. `user_management` → `UM` → `TC-UM-001`).
- A code, once used in any ID, **must never change** (it would break traceability). To add a feature, append a new row here first.
