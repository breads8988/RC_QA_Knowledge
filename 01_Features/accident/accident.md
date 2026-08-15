---
type: domain
domain: accident
---

# Accident — domain hub

Reporting and reading accident / damage records. `wa_` = Web App (Driver), `wp_` = Web Portal (Client Admin) — the prefix identifies the actor, so these are different features, not two views of one.

| Feature | Platform | Actor | Code | Entity |
| ------- | -------- | ----- | ---- | ------ |
| [[wa_accident_assistant]] | Web App | Driver | `AA` | Accident |
| [[wa_my_accident]] | Web App | Driver | `MA` | Accident |
| [[wp_accident_report]] | Web Portal | Client Admin | `WPAR` | Accident |

Each feature hub links down to its own SRS / AC / TC. To find what else touches these records, open [[e_accident|Accident]] and read the backlinks.
