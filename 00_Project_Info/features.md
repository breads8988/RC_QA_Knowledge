# Feature Registry

Single source of truth mapping each **feature** to its short **code**. `/gen-ac` and `/gen-tc` read this to keep IDs stable across runs. Define a feature here **once**, before generating AC/TC for it.

| Feature (slug / file) | Code    | Description                     | SRS                        |
| --------------------- | ------- | ------------------------------- | -------------------------- |
| login                 | `LOGIN` | User login / authentication     | [[01_SRS/login/epic]]      |
| registration          | `REG`   | User registration / sign-up (4-step onboarding) | [[01_SRS/registration/]] |
| my_vehicle            | `MV`    | My Vehicle management           | [[01_SRS/my_vehicle/]]     |
| user_management       | `UM`    | User management / accounts      | [[01_SRS/user_management/]] |

## Rules

- **Slug** — lowercase, matches `01_SRS/<slug>/`, `02_Acceptance_Criteria/<slug>/<slug>.md`, `03_Testcases/<slug>/<slug>.md`. This is what you pass to the commands.
- **Code** — 2–6 UPPERCASE letters, **unique**. Used only in IDs: `AC-<CODE>-NN`, `BR-<CODE>-NN`, `TC-<CODE>-NNN` (e.g. `user_management` → `UM` → `TC-UM-001`).
- A code, once used in any ID, **must never change** (it would break traceability). To add a feature, append a new row here first.
