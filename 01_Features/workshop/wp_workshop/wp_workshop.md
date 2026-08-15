---
type: feature
code: WPWS
domain: workshop
platform: Web Portal
actor: Client Admin
entity:
  - "[[e_workshop|Workshop]]"
  - "[[e_voucher|Voucher]]"
jira: [RC-104]
status: Draft
srs: "[[wp_workshop_srs]]"
ac: "[[wp_workshop_ac]]"
tc: "[[wp_workshop_tc]]"
related: []
---

# Manage Workshop — Web Portal (`WPWS`)

Admin-facing management of the same workshop records the driver searches: edit a workshop, add and show its vouchers, rate it, and filter the list by name, address or rating.

Entities above are the cross-feature wiring — open [[e_workshop|Workshop]] or [[e_voucher|Voucher]] and their backlinks list every other feature that touches the same records.
