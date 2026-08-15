---
type: feature
code: WS
domain: workshop
platform: Web App
actor: Driver
entity:
  - "[[e_workshop|Workshop]]"
  - "[[e_voucher|Voucher]]"
jira: [RC-120]
status: Draft
srs: "[[wa_workshop_srs]]"
ac: "[[wa_workshop_ac]]"
tc: "[[wa_workshop_tc]]"
related: []
---

# Workshop — Web App (`WS`)

Driver-facing workshop search (*Werkstatt Finden*): nearby workshops on a map or list, filtered by radius and rating. From a workshop's card the driver views and saves a discount voucher with its redemption code, or requests an appointment / callback.

Entities above are the cross-feature wiring — open [[e_workshop|Workshop]] or [[e_voucher|Voucher]] and their backlinks list every other feature that touches the same records.
