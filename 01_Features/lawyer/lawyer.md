---
type: domain
domain: lawyer
---

# Lawyer — domain hub

Accident legal advice — the driver's list and the admin's master data. `wa_` = Web App (Driver), `wp_` = Web Portal (Client Admin) — the prefix identifies the actor, so these are different features, not two views of one.

| Feature | Platform | Actor | Code | Entity |
| ------- | -------- | ----- | ---- | ------ |
| [[wa_lawyer]] | Web App | Driver | `LAW` | Lawyer |
| [[wp_lawyer]] | Web Portal | Client Admin | `WPLAW` | Lawyer |

Each feature hub links down to its own SRS / AC / TC. To find what else touches these records, open [[e_lawyer|Lawyer]] and read the backlinks.
