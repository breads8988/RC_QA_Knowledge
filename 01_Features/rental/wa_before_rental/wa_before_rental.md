---
type: feature
code: BRE
domain: rental
platform: Web App
actor: Driver
entity:
  - "[[e_vehicle|Vehicle]]"
jira: [RC-127]
status: Draft
srs: "[[wa_before_rental_srs]]"
ac: "[[wa_before_rental_ac]]"
related: []
---

# Before Rental — Web App (`BRE`)

The pre-rental vehicle-condition flow: from "Ein Auto Mieten" (Rent a car) on the home page, the driver picks one of their rental vehicles, documents its existing damage (photo capture per zone, per-part damage entry, AI-estimated repair cost), then submits and schedules the rental period.

Open [[e_vehicle|Vehicle]] to see every other feature that touches the same records — its backlinks are the impact list.
