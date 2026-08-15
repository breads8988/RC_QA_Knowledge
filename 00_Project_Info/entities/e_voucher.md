---
type: entity
name: Voucher
---

# Voucher

A discount **issued by a [[e_workshop|Workshop]] and saved by a [[e_user|User]]**. The driver collects it during the workshop flow and redeems it in person with a redemption code; the Client Admin sees the saved vouchers of all users of their company.

**Why it matters for testing:** the same record is read by two different actors through two different apps, and it expires — creation date, expiration date, and the expired-voucher state are recurring test conditions.

API module: `Workshops` (+ store voucher per user).

Source: [[00_Project_Info/system-high-level-design]] §3A, §3C, §4, §6; [[CLAUDE]].

> Features that read or write this record are the **backlinks** of this note.
