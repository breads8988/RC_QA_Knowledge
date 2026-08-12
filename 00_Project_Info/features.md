# Feature Registry

Maps each **feature** to its short **code**. `/gen-ac` and `/gen-tc` read this to keep IDs stable across runs. Define a feature here **once**, before generating AC/TC for it.

Rows are grouped by **domain**, matching the folder tree. `wa_` = Web App, `wp_` = Web Portal.

> **Rules for this file — code immutability, the Entity column, how impact is found — are in [[00_Project_Info/conventions]] §3–§4.** Read that before adding a row.

**Entity** must be one of: `Company` · `User` · `Vehicle` · `Accident` · `Workshop` · `Expert` · `Lawyer` · `Voucher` · `Ad` · `Pricing` · `—`
Declare only the records the feature reads or writes **as its job** — not one it merely branches on (see conventions §3).

## Accident — [[01_SRS/accident/accident|hub]]

| Feature (slug / file) | Code   | Entity          | Description                                                                                                                                   | SRS                                                             |
| ----------------------- | ------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| wa_my_accident          | `MA`   | `Accident`      | My Accidents page (reported/saved accidents list, report-accident final submission, delete accident)                                          | `01_SRS/accident/wa_my_accident/`               |
| wa_accident_assistant   | `AA`   | `Accident`      | Accident Assistance / Unfallhilfe — Report Accident flow entry, Overview, Step 1 Accident details (location, incident type, parties involved)  | `01_SRS/accident/wa_accident_assistant/` |
| wp_accident_report      | `WPAR` | `Accident`      | Web Portal — Accident Report (admin): filtered/curated view of accident data saved via the app-side `MA` and `AA` flows                        | `01_SRS/accident/wp_accident_report/`       |

## Lawyer — [[01_SRS/lawyer/lawyer|hub]]

| Feature (slug / file) | Code    | Entity          | Description                                                                                                                     | SRS                                       |
| --------------------- | ------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| wa_lawyer             | `LAW`   | `Lawyer`        | Lawyer page / accident legal advice ("Unfall Rechtsberatung") — list lawyers, filter by rating, request appointment              | `01_SRS/lawyer/wa_lawyer/`     |
| wp_lawyer             | `WPLAW` | `Lawyer`        | Web Portal — Manage Lawyers (admin): add/edit/delete lawyer, filter, import/export lawyers                                       | `01_SRS/lawyer/wp_lawyer/`     |

## Workshop — [[01_SRS/workshop/workshop|hub]]

| Feature (slug / file) | Code   | Entity          | Description                                                                                                                                   | SRS                                           |
| --------------------- | ------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| wa_workshop           | `WS`   | `Workshop` `Voucher` | Workshop Web app & voucher (nearby-workshop map/list search, voucher redemption code, save voucher, request appointment/callback)              | `01_SRS/workshop/wa_workshop/`   |
| wp_workshop           | `WPWS` | `Workshop` `Voucher` | Web Portal — Manage Workshop (admin): edit workshop, add/show voucher, rate workshop, filter by name/address/rating                            | `01_SRS/workshop/wp_workshop/`   |

## Voucher — [[01_SRS/voucher/voucher|hub]]

| Feature (slug / file) | Code   | Entity          | Description                                                                                                                                                    | SRS                                                     |
| --------------------- | ------ | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| wa_saved_voucher      | `SV`   | `Voucher`       | Saved Voucher page (lists vouchers the user saved during the Workshop flow; separate page, connected to `WS` save-voucher action)                               | `01_SRS/voucher/wa_saved_voucher/`    |
| wp_user_voucher       | `WPUV` | `Voucher`       | Web Portal — Manage User Vouchers (admin): list saved vouchers of all users, view details, delete, filter by user/workshop/creation date/expiration date        | `01_SRS/voucher/wp_user_voucher/`      |

## Standalone

| Feature (slug / file) | Code    | Entity          | Description                                                                                                                                                                    | SRS                                                             |
| ----------------------- | ------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| login                   | `LOGIN` | `User`          | User login / authentication                                                                                                                                                    | [[01_SRS/login/login]]                                           |
| registration            | `REG`   | `User` `Vehicle` | User registration / sign-up (4-step onboarding)                                                                                                                                | [[01_SRS/registration/registration]]                            |
| my_vehicle              | `MV`    | `Vehicle`       | My Vehicle management                                                                                                                                                          | [[01_SRS/my_vehicle/my_vehicle]]                                |
| homepage                | `HOME`  | `Ad`            | Home page (feature grid for logged-in/guest users, banner, quick menu, feature config)                                                                                         | [[01_SRS/homepage/homepage]]                                    |
| tourguide               | `TG`    | —               | Tour guide (feature hint popups shown on first web-app access, logged-in vs not-logged-in flows)                                                                               | [[01_SRS/tourguide/tourguide]]                                  |
| expert_call_appointment | `ECA`   | `Expert`        | Find an Expert / expert call appointment — list, filter, book appointment / schedule call (Calendly), callback request + per-expert Calendly video call                         | [[01_SRS/expert_call_appointment/expert_call_appointment]]      |
| wp_advertisement        | `WPAD`  | `Ad`            | Web Portal — Manage Advertisements (admin): Ad type (Advertisement schedule vs Banner), Target Pages assignment, media upload (image/video incl. heic/heif), Displayable toggle | [[01_SRS/wp_advertisement/wp_advertisement]]                    |
| user_management         | `UM`    | `User`          | User management / accounts                                                                                                                                                     | [[01_SRS/user_management/]]                                     |

## Not started

These rows are reserved so their codes stay stable, but have no AC/TC yet:

- `UM` — `user_management`. No SRS folder either.
- `WPUV` — `wp_user_voucher`. SRS screenshots exist; AC/TC not written.

> **Needs confirmation.** `tourguide` is currently `—` and `homepage` is `Ad`, both derived from the descriptions above rather than from the code. If tour-guide state is persisted per user, `tourguide` should become `User`. A BA or dev should confirm these two.
