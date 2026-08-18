---
type: entity
name: Ad
---

# Advertisement / Banner

Promotional media shown to drivers in the Web App. Managed by Client Admins in the Web Portal (ad type: Advertisement schedule vs Banner, Target Pages assignment, media upload, Displayable toggle) and also by MCS Admin.

**Why it matters for testing:** media upload accepts image **and video**, including `heic` / `heif`, so format and size handling is real test surface.

API module: `Advertisements`.

Source: [[00_Project_Info/system-high-level-design]] §3A, §3C, §3D, §4, §6.

> Features that read or write this record are the **backlinks** of this note.
