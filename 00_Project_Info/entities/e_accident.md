---
type: entity
name: Accident
---

# Accident / Damage

A damage report created by a driver through the Report Accident flow (*Unfallhilfe*), reported in steps and listed on My Accidents. Client Admins read the same records as Accident Reports in the Web Portal.

**Photos and documents live in file storage**, not in the database — so upload limits, accepted formats (including `heic` / `heif`) and deletion behaviour are real test surface. MCS Admin can delete damage photos and documents.

API module: `Accidents/Damages` (report steps, statuses, list per user).

Source: [[00_Project_Info/system-high-level-design]] §3A, §3D, §5, §6.

> Features that read or write this record are the **backlinks** of this note.
