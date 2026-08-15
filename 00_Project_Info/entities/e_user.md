---
type: entity
name: User
---

# User

An end user (driver) account. Belongs to one Company, owns Vehicles, reports Accidents, saves Vouchers. Client Admins manage the users of their own Company from the Web Portal; MCS Admin sees users across all tenants.

API modules: `Auth` (login, signup, reset password, session check) and `Users/Profile`.

**Declaring rule:** only features whose actual job is reading or writing user records list this entity. Almost every screen branches on logged-in vs guest — that is not enough to declare `User` (see [[00_Project_Info/conventions]] §3).

Source: [[00_Project_Info/system-high-level-design]] §3A, §4, §6.

> Features that read or write this record are the **backlinks** of this note.
