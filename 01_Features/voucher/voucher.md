---
type: domain
domain: voucher
---

# Voucher — domain hub

Vouchers a driver saved, seen by the driver and by the company admin. `wa_` = Web App (Driver), `wp_` = Web Portal (Client Admin) — the prefix identifies the actor, so these are different features, not two views of one.

| Feature | Platform | Actor | Code | Entity |
| ------- | -------- | ----- | ---- | ------ |
| [[wa_saved_voucher]] | Web App | Driver | `SV` | Voucher |
| [[wp_user_voucher]] | Web Portal | Client Admin | `WPUV` | Voucher |

Each feature hub links down to its own SRS / AC / TC. To find what else touches these records, open [[e_voucher|Voucher]] and read the backlinks.
