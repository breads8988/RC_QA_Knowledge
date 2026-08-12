# RC QA Knowledge

QA knowledge base for **RepairCheck** — requirements (SRS), acceptance criteria, and test cases, written as Obsidian markdown and generated from Jira with `/gen-ac` and `/gen-tc`.

> **Structural conventions — paths, slugs, the registry, linking, templates — live in [[00_Project_Info/conventions]]. Read that file before writing any path, ID, or link.** It is the single source of truth; this file deliberately does not repeat it.
>
> This file is the **business layer**: what the product is, who uses it, what the words mean. Read it first. A correct-looking AC that misunderstands who the actor is, or what a voucher does, is worse than no AC at all.

---

## What the product is

**RepairCheck (RC)**, built by **MotionsCloud (MCS)**: a **multi-tenant SaaS for car accident and damage assistance**, sold to insurance companies and aimed at the **German market**.

A driver has an accident. Through RepairCheck they report the damage with photos, then find the help they need nearby — a repair workshop, a vehicle-diagnosis expert, or a lawyer for the legal side. The insurance company that owns the tenant manages that master data and sees the accident reports.

Full architecture: [[00_Project_Info/system-high-level-design]].

## Who uses it — and why the slug prefix matters

Three groups of people, three different applications. **This is what `wa_` and `wp_` encode** — the prefix tells you the actor, the app, and the permission model:

| Prefix | App                       | Actor                                             | What they do                                                                          |
| ------ | ------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `wa_`  | **Web App** (+ Android)   | **End user / Driver**                             | Report an accident, find a workshop / expert / lawyer, manage vehicles, save vouchers |
| `wp_`  | **Web Portal** (`/admin`) | **Client Admin** — staff of one insurance company | Manage that company's users, accident reports, workshops, lawyers, ads, vouchers      |
| —      | **SaaS Admin**            | **MCS Admin** — MotionsCloud staff                | Onboard tenant companies, global master data, feature flags, roles                    |

So `workshop/wa_workshop` and `workshop/wp_workshop` are **not two views of one feature** — they are a driver searching for a garage versus a company admin editing the garage record. Different actor, different permissions, different failure modes. Never write one AC that covers both.

**Multi-tenancy:** MCS Admin creates Companies (tenants). Each Company gets its own Web Portal. Every end user belongs to a Company. All four apps talk to **one shared REST API**. Cross-tenant data leakage is therefore a standing risk on any feature that lists or filters records — worth a negative AC whenever a feature reads company-scoped data.

## Domain vocabulary

The product is German-market, and tickets and the UI mix German terms in:

| German                                     | English                                        |
| ------------------------------------------ | ---------------------------------------------- |
| *Unfallhilfe*                              | Accident assistance — the Report Accident flow |
| *Werkstatt* / *Werkstatt Finden*           | Workshop (garage) / Find a Workshop            |
| *Experte* / *Experte für Fahrzeugdiagnose* | Expert / vehicle-diagnosis expert              |
| *Unfall Rechtsberatung*                    | Accident legal advice — the Lawyer page        |

## Core entities

```
Company (tenant) ──▶ User ──▶ Vehicle
                          └─▶ Accident / Damage  (with photos + documents)

Master data, geo-located:  Workshop · Expert · Lawyer
Attached:                  Voucher · Advertisement / Banner · Pricing
```

These same names are the values of the registry's **Entity** column, which is how cross-feature impact is found — see [[00_Project_Info/conventions]] §3–§4.

Notes that shape test design:

- **Workshops, Experts and Lawyers are geo-located** — the API geocodes them to lat/long, and users filter by **distance and rating**. Boundary tests on distance radius and rating filters are usually in scope.
- **A Voucher is issued by a workshop and saved by a user.** The driver saves it (`wa_saved_voucher`); the company admin sees all users' saved vouchers (`wp_user_voucher`). Same object, two actors.
- **Accidents carry photos and documents** in file storage, so upload limits, formats (incl. heic/heif) and deletion behaviour are real test surface.

## What this vault covers today

17 features registered in [[00_Project_Info/features]] — **11 Web App** and **5 Web Portal**, plus `user_management` reserved but not started. **Android and SaaS Admin have no AC/TC yet.** If a ticket lands on one of those, the feature must be added to the registry first.

---

## Working in this vault

Rules for the agent specifically. Everything structural is in [[00_Project_Info/conventions]].

- **Never fabricate.** No UI element you have not seen in a screenshot. No business rule the ticket does not state. No `TC-` / `AC-` / `BR-` ID you have not read in a file. Flag the assumption or say the coverage is unverified instead — a plausible invention is the most expensive thing you can add here, because it looks researched.
- **Report what you checked, not just what you found.** "No regression impact, isolated change" is a valid finding; silence is not.
- **Surface drift rather than patching around it.** A blank Entity cell, a slug that does not match its folder, a link that does not resolve — name it in the report. These are cheap to fix when named and expensive when they accumulate.
- **Verify before asserting.** Check a file exists before linking to it; check a code against the registry before using it in an ID.
- Never modify `.obsidian/` config as part of a content task.
