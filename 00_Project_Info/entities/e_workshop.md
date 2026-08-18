---
type: entity
name: Workshop
---

# Workshop (*Werkstatt*)

A repair garage. **Master data, geo-located** — the API geocodes the address to lat/long, and drivers find workshops by **distance and rating** (*Werkstatt Finden*). Client Admins manage their company's workshops in the Web Portal; MCS Admin maintains the global list with import/export.

A Workshop issues [[e_voucher|Vouchers]].

**Why it matters for testing:** boundary tests on the distance radius and the rating filter are usually in scope.

API modules: `Workshops` (+ store voucher per user), `Geocoding`.

Source: [[00_Project_Info/system-high-level-design]] §3A, §3C, §3D, §4, §6.

> Features that read or write this record are the **backlinks** of this note.
