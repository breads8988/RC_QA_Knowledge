---
type: domain
domain: workshop
---

# Workshop — domain hub

Two features act on the same workshop records through different actors. `wa_` = Web App (Driver), `wp_` = Web Portal (Client Admin) — they are **not** two views of one feature.

| Feature | Platform | Actor | Code | Entity |
| ------- | -------- | ----- | ---- | ------ |
| [[wa_workshop]] | Web App | Driver | `WS` | Workshop, Voucher |
| [[wp_workshop]] | Web Portal | Client Admin | `WPWS` | Workshop, Voucher |

Each feature hub links down to its own SRS / AC / TC. To find what else touches these records, open [[e_workshop|Workshop]] or [[e_voucher|Voucher]] and read the backlinks.
