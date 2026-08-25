---
type: domain
domain: rental
---

# Rental — domain hub

The rental vehicle-condition flow, split by which side of the rental period the driver is documenting. `wa_` = Web App (Driver) — no Web Portal counterpart exists yet.

| Feature | Platform | Actor | Code | Entity |
| ------- | -------- | ----- | ---- | ------ |
| [[wa_before_rental]] | Web App | Driver | `BRE` | Vehicle |
| [[wa_after_rental]] | Web App | Driver | `ARE` | Vehicle |

Each feature hub links down to its own SRS / AC / TC. To find what else touches these records, open [[e_vehicle|Vehicle]] and read the backlinks.
