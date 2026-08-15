---
type: entity
name: Expert
---

# Expert (*Experte für Fahrzeugdiagnose*)

A vehicle-diagnosis expert. **Master data, geo-located** — filtered by **rating and distance**. Drivers book a call or appointment with one. MCS Admin maintains the global list with import/export and auto geocoding.

**Why it matters for testing:** boundary tests on the distance radius and the rating filter are usually in scope.

API modules: `Experts` (filter by rating & distance), `Geocoding`.

Source: [[00_Project_Info/system-high-level-design]] §3A, §3D, §4, §6.

> Features that read or write this record are the **backlinks** of this note.
