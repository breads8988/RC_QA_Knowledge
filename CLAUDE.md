# RC QA Knowledge

QA knowledge base for **RepairCheck** — requirements (SRS), acceptance criteria, and test cases, written as Obsidian markdown and generated from Jira with `/gen-ac` and `/gen-tc`.

Read the business section first. Path conventions matter, but a correct-looking AC that misunderstands who the actor is or what a voucher does is worse than no AC at all.

---

# Part 1 — The business

## What the product is

**RepairCheck (RC)**, built by **MotionsCloud (MCS)**: a **multi-tenant SaaS for car accident and damage assistance**, sold to insurance companies and aimed at the **German market**.

A driver has an accident. Through RepairCheck they report the damage with photos, then find the help they need nearby — a repair workshop, a vehicle-diagnosis expert, or a lawyer for the legal side. The insurance company that owns the tenant manages that master data and sees the accident reports.

Full architecture: [[00_Project_Info/system-high-level-design]].

## Who uses it — and why the slug prefix matters

Three groups of people, three different applications. **This is what `wa_` and `wp_` encode** — the prefix is not cosmetic, it tells you the actor, the app, and the permission model:

| Prefix | App                       | Actor                                          | What they do                                                                    |
| ------ | ------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------- |
| `wa_`  | **Web App** (+ Android)   | **End user / Driver**                           | Report an accident, find a workshop / expert / lawyer, manage vehicles, save vouchers |
| `wp_`  | **Web Portal** (`/admin`) | **Client Admin** — staff of one insurance company | Manage that company's users, accident reports, workshops, lawyers, ads, vouchers  |
| —      | **SaaS Admin**            | **MCS Admin** — MotionsCloud staff              | Onboard tenant companies, global master data, feature flags, roles               |

So `workshop/wa_workshop` and `workshop/wp_workshop` are **not two views of one feature** — they are a driver searching for a garage versus a company admin editing the garage record. Different actor, different permissions, different failure modes. Never write one AC that covers both.

**Multi-tenancy:** MCS Admin creates Companies (tenants). Each Company gets its own Web Portal. Every end user belongs to a Company. All four apps talk to **one shared REST API**. Cross-tenant data leakage is therefore a standing risk on any feature that lists or filters records — worth a negative AC whenever a feature reads company-scoped data.

## Domain vocabulary

The product is German-market, and tickets and the UI mix German terms in:

| German                          | English                                    |
| ------------------------------- | ------------------------------------------ |
| *Unfallhilfe*                   | Accident assistance — the Report Accident flow |
| *Werkstatt* / *Werkstatt Finden* | Workshop (garage) / Find a Workshop         |
| *Experte* / *Experte für Fahrzeugdiagnose* | Expert / vehicle-diagnosis expert  |
| *Unfall Rechtsberatung*         | Accident legal advice — the Lawyer page     |

## Core entities

```
Company (tenant) ──▶ User ──▶ Vehicle
                          └─▶ Accident / Damage  (with photos + documents)

Master data, geo-located:  Workshop · Expert · Lawyer
Attached:                  Voucher · Advertisement / Banner · Pricing
```

Notes that shape test design:

- **Workshops, Experts and Lawyers are geo-located** — the API geocodes them to lat/long, and users filter by **distance and rating**. Boundary tests on distance radius and rating filters are usually in scope.
- **A Voucher is issued by a workshop and saved by a user.** The driver saves it (`wa_saved_voucher`); the company admin sees all users' saved vouchers (`wp_user_voucher`). Same object, two actors.
- **Accidents carry photos and documents** in file storage, so upload limits, formats (incl. heic/heif) and deletion behaviour are real test surface.

## What this vault covers today

17 features registered in [[00_Project_Info/features]] — **11 Web App** and **5 Web Portal**, plus `user_management` reserved but not started. **Android and SaaS Admin have no AC/TC yet.** If a ticket lands on one of those, the feature must be added to the registry first.

---

# Part 2 — How the vault is organised

Shared via GitHub, so **every path must be relative** — never write a machine-specific absolute path into a note.

## The three pillars mirror each other

A feature occupies the **same relative path** under all three pillars. This is the single most important structural rule; almost every past breakage came from violating it.

```
01_SRS/<domain>/<slug>/<slug>.md          ← requirement + screenshots
01_SRS/<domain>/<slug>/*.png              ← screens
01_SRS/<domain>/<slug>/figma/*.png        ← Figma exports
02_Acceptance_Criteria/<domain>/<slug>/<slug>.md
03_Testcases/<domain>/<slug>/<slug>.md
```

- **The note's file name always equals its leaf folder name.** `workshop/wa_workshop/wa_workshop.md`, never `workshop/wa_workshop/workshop.md`.
- A feature that belongs to no domain drops the `<domain>/` level: `01_SRS/login/login.md`.
- Domains in use: `accident`, `lawyer`, `voucher`, `workshop` — these are the four areas where the same subject has both a Web App and a Web Portal feature. Everything else is standalone.
- **Never register a bare domain name as a slug.** `workshop` alone is ambiguous between the driver feature and the admin feature.

## Feature registry

[[00_Project_Info/features]] is the single source of truth mapping **slug → short code**. `/gen-ac` and `/gen-tc` read it to keep IDs stable.

- Resolve **both** the code and the target path from a registry row. The `##` section a row sits under gives its domain; a row under `## Standalone` has none.
- Codes are 2–6 uppercase letters, unique across the whole registry. **A code already used in any ID must never change** — it would break traceability across hundreds of `AC-` / `BR-` / `TC-` IDs.
- Add the row *before* generating AC or TC for a new feature.

## Traceability

```
Jira ticket  ──▶  AC-<CODE>-NN / BR-<CODE>-NN  ──▶  TC-<CODE>-NNN
  (the why)         (the what — definition of done)     (the how to verify)
```

AC are **optional** — write them when the ticket is ambiguous, high-risk, or needs stakeholder sign-off. For a small clear ticket, go straight to TCs and set the `AC` column to `—`. Coverage rule: every business rule and every Critical/High AC needs ≥1 TC.

## Linking discipline (this is what keeps the graph readable)

Obsidian builds its graph from wiki-links alone — there is no index file it reads. The tree shape is purely a consequence of who links to whom, so it only survives if everyone follows the same rule:

**One hop per level.**

```
features.md  →  domain hub  →  feature SRS note  →  its AC / TC
```

- `00_Project_Info/features.md` links to **domain hubs and standalone features only** — never straight to a sub-feature. In the sub-feature tables the SRS column is a plain path in backticks, not a wiki-link.
- A domain with 2+ sub-features has a hub at `01_SRS/<domain>/<domain>.md` listing them. Add a row to the hub when adding a sub-feature.
- An AC or TC note links **up to its own SRS note only** (`[[01_SRS/<domain>/<slug>/<slug>]]` in the header's `SRS ref` row). Never link it to `features.md`, to a hub, or to a sibling feature.
- Cross-feature references go in prose using the other feature's code (`WS`, `AA`), **not** a wiki-link.

### Never link to a folder

`[[01_SRS/accident/wa_my_accident/]]` — with a trailing slash — does not resolve. Obsidian links point at notes, not folders, so this renders as a dead grey node. Always link the note: `[[01_SRS/accident/wa_my_accident/wa_my_accident]]`. Verify the target file exists before writing the link.

## Templates

`04_Templates/` holds the output formats. Read them from the vault at generation time — never hardcode a copy into a skill.

| File                    | Used by            |
| ----------------------- | ------------------ |
| `ac_template.md`        | `/gen-ac`          |
| `testcases_template.md` | `/gen-tc`          |
| `bug_template.md`       | manual bug reports |

## Writing

- **All note content in English** — body text, table cells, headers, and Type / Priority / Status values. The vault is shared on GitHub. German product terms stay in German where the UI uses them; gloss them on first use.
- Test cases stay **high-level**: one scenario, 3–5 steps, no click-by-click. The Cucumber automation layer writes the detailed steps.
- Never fabricate UI you have not seen in a screenshot, and never invent a business rule — flag the assumption instead.
- Never modify `.obsidian/` config as part of a content task.

## Generated / ignored

`docs/` is a symlink tree built by `scripts/build-docs-tree.sh` for MkDocs, and `site/` is the built HTML. Both are gitignored **and** excluded from Obsidian's index via `userIgnoreFilters` in `.obsidian/app.json` — without that exclusion every note appears twice in the graph. Do not edit anything under those two folders.
