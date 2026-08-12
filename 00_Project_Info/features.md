# Feature Registry

Single source of truth mapping each **feature** to its short **code**. `/gen-ac` and `/gen-tc` read this to keep IDs stable across runs. Define a feature here **once**, before generating AC/TC for it.

Features are grouped by **domain**, matching the folder tree. `wa_` = Web App, `wp_` = Web Portal. A domain with more than one sub-feature has a hub note in `01_SRS/<domain>/<domain>.md`.

## Accident — [[01_SRS/accident/accident|hub]]

| Feature (slug / file)   | Code   | Description                                                                                                                                   | SRS                                                             |
| ----------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| wa_my_accident          | `MA`   | My Accidents page (reported/saved accidents list, report-accident final submission, delete accident)                                          | `01_SRS/accident/wa_my_accident/`               |
| wa_accident_assistant   | `AA`   | Accident Assistance / Unfallhilfe — Report Accident flow entry, Overview, Step 1 Accident details (location, incident type, parties involved)  | `01_SRS/accident/wa_accident_assistant/` |
| wp_accident_report      | `WPAR` | Web Portal — Accident Report (admin): filtered/curated view of accident data saved via the app-side `MA` and `AA` flows                        | `01_SRS/accident/wp_accident_report/`       |

## Lawyer — [[01_SRS/lawyer/lawyer|hub]]

| Feature (slug / file) | Code    | Description                                                                                                                     | SRS                                       |
| --------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| wa_lawyer             | `LAW`   | Lawyer page / accident legal advice ("Unfall Rechtsberatung") — list lawyers, filter by rating, request appointment              | `01_SRS/lawyer/wa_lawyer/`     |
| wp_lawyer             | `WPLAW` | Web Portal — Manage Lawyers (admin): add/edit/delete lawyer, filter, import/export lawyers                                       | `01_SRS/lawyer/wp_lawyer/`     |

## Workshop — [[01_SRS/workshop/workshop|hub]]

| Feature (slug / file) | Code   | Description                                                                                                                                   | SRS                                           |
| --------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| wa_workshop           | `WS`   | Workshop Web app & voucher (nearby-workshop map/list search, voucher redemption code, save voucher, request appointment/callback)              | `01_SRS/workshop/wa_workshop/`   |
| wp_workshop           | `WPWS` | Web Portal — Manage Workshop (admin): edit workshop, add/show voucher, rate workshop, filter by name/address/rating                            | `01_SRS/workshop/wp_workshop/`   |

## Voucher — [[01_SRS/voucher/voucher|hub]]

| Feature (slug / file) | Code   | Description                                                                                                                                                    | SRS                                                     |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| wa_saved_voucher      | `SV`   | Saved Voucher page (lists vouchers the user saved during the Workshop flow; separate page, connected to `WS` save-voucher action)                               | `01_SRS/voucher/wa_saved_voucher/`    |
| wp_user_voucher       | `WPUV` | Web Portal — Manage User Vouchers (admin): list saved vouchers of all users, view details, delete, filter by user/workshop/creation date/expiration date        | `01_SRS/voucher/wp_user_voucher/`      |

## Standalone

| Feature (slug / file)   | Code    | Description                                                                                                                                                                    | SRS                                                             |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| login                   | `LOGIN` | User login / authentication                                                                                                                                                    | [[01_SRS/login/epic]]                                           |
| registration            | `REG`   | User registration / sign-up (4-step onboarding)                                                                                                                                | [[01_SRS/registration/registration]]                            |
| my_vehicle              | `MV`    | My Vehicle management                                                                                                                                                          | [[01_SRS/my_vehicle/my_vehicle]]                                |
| homepage                | `HOME`  | Home page (feature grid for logged-in/guest users, banner, quick menu, feature config)                                                                                         | [[01_SRS/homepage/homepage]]                                    |
| tourguide               | `TG`    | Tour guide (feature hint popups shown on first web-app access, logged-in vs not-logged-in flows)                                                                               | [[01_SRS/tourguide/tourguide]]                                  |
| expert_call_appointment | `ECA`   | Find an Expert / expert call appointment — list, filter, book appointment / schedule call (Calendly), callback request + per-expert Calendly video call                         | [[01_SRS/expert_call_appointment/expert_call_appointment]]      |
| wp_advertisement        | `WPAD`  | Web Portal — Manage Advertisements (admin): Ad type (Advertisement schedule vs Banner), Target Pages assignment, media upload (image/video incl. heic/heif), Displayable toggle | [[01_SRS/wp_advertisement/wp_advertisement]]                    |
| user_management         | `UM`    | User management / accounts                                                                                                                                                     | [[01_SRS/user_management/]]                                     |

## Not started

These rows are reserved so their codes stay stable, but have no AC/TC yet:

- `UM` — `user_management`. No SRS folder either.
- `WPUV` — `wp_user_voucher`. SRS screenshots exist; AC/TC not written.

## Rules

- **Slug** — lowercase, and **identical to the leaf folder name**. Every feature lives at the same relative path under all three pillars:
  `01_SRS/<domain>/<slug>/<slug>.md`, `02_Acceptance_Criteria/<domain>/<slug>/<slug>.md`, `03_Testcases/<domain>/<slug>/<slug>.md`.
  A feature with no domain drops the `<domain>/` level: `01_SRS/<slug>/<slug>.md`. This is what you pass to the commands.
- **Platform prefix** — a slug under a shared domain carries `wa_` (Web App) or `wp_` (Web Portal). Never register a bare domain name as a slug; it would be ambiguous between the two platforms.
- **Domain hub** — a domain with 2+ sub-features has `01_SRS/<domain>/<domain>.md` listing them. Add a row to the hub table when adding a sub-feature.
- **One hop per level** — this file links to the **hub only**, never straight to a sub-feature; the hub is what links down to its sub-features. So the graph reads
  `features → accident → wa_my_accident`, not `features → wa_my_accident`.
  In the sub-feature tables the SRS column is therefore a plain path in backticks, **not** a wiki-link. Only the section heading carries the hub link. Standalone features have no hub, so they keep a direct wiki-link.
- **Code** — 2–6 UPPERCASE letters, **unique across the whole registry**. Used only in IDs: `AC-<CODE>-NN`, `BR-<CODE>-NN`, `TC-<CODE>-NNN` (e.g. `user_management` → `UM` → `TC-UM-001`).
- A code, once used in any ID, **must never change** (it would break traceability). To add a feature, append a new row here first.
