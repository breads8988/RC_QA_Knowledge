# Vault conventions

**This file is the single source of truth for how this vault is structured.** Every other file — `CLAUDE.md`, `README.md`, `features.md`, the two skills — points here instead of restating these rules. When a rule changes, change it here and nowhere else.

For *what the product is* — actors, domain vocabulary, entities — read `CLAUDE.md` instead. That is the business layer; this is the structural layer.

The vault is shared via GitHub, so **every path must be relative**. Never write a machine-specific absolute path into a note.

---

## 1. The three pillars mirror each other

A feature occupies the **same relative path** under all three pillars. This is the most important structural rule; almost every past breakage came from violating it.

```
01_SRS/<domain>/<slug>/<slug>.md          ← requirement note
01_SRS/<domain>/<slug>/*.png              ← screens
01_SRS/<domain>/<slug>/figma/*.png        ← Figma exports
02_Acceptance_Criteria/<domain>/<slug>/<slug>.md
03_Testcases/<domain>/<slug>/<slug>.md
```

- **The note's file name always equals its leaf folder name.** `workshop/wa_workshop/wa_workshop.md`, never `workshop/wa_workshop/workshop.md`.
- A feature that belongs to no domain drops the `<domain>/` level: `01_SRS/login/login.md`.
- Domains in use: `accident`, `lawyer`, `voucher`, `workshop` — the four subjects that have both a Web App and a Web Portal feature. Everything else is standalone.

## 2. Slug and platform prefix

- **Slug** — lowercase, identical to the leaf folder name. This is what you pass to `/gen-ac` and `/gen-tc`.
- A slug under a shared domain carries **`wa_`** (Web App, the driver) or **`wp_`** (Web Portal, the Client Admin). The prefix is not cosmetic — it identifies the actor and the permission model. See `CLAUDE.md` for who those actors are.
- **Never register a bare domain name as a slug.** `workshop` alone is ambiguous between the driver feature and the admin feature, and that ambiguity is what once made the graph unreadable.

## 3. Feature registry

`features.md` maps **slug → short code**. `/gen-ac` and `/gen-tc` read it to keep IDs stable.

- Resolve **both** the code and the target path from a registry row. The `##` section a row sits under gives its domain; a row under `## Standalone` has none.
- **Code** — 2–6 uppercase letters, unique across the whole registry. Used only in IDs: `AC-<CODE>-NN`, `BR-<CODE>-NN`, `TC-<CODE>-NNN`.
- **A code already used in any ID must never change** — it would break traceability across hundreds of IDs.
- Add the row *before* generating AC or TC for a new feature. Fill every column in the same edit.

### The Entity column

The domain tree groups features by *subject area*. It does **not** show impact: the `Voucher` entity is touched by four features spread across two domains (`workshop` and `voucher`), so changing voucher logic puts all four at risk while the hub shows them as two unrelated trees.

The **Entity** column is the second, orthogonal axis that makes impact findable. Valid values, from `system-high-level-design.md` §6:

`Company` · `User` · `Vehicle` · `Accident` · `Workshop` · `Expert` · `Lawyer` · `Voucher` · `Ad` · `Pricing`

Rules for filling it:

- Declare only the entity the feature takes as its **subject** — the records it reads or writes as its actual job. Use `—` when there is none (pure-UI features).
- **Do not** declare an entity a feature merely branches on. Almost every screen behaves differently for a logged-in vs. guest user; if that counted, every row would list `User` and the column would carry no information. `homepage` lists `Ad` (it renders banners), not `User` (it only checks session state).
- One entity is normal; two happens when a feature genuinely owns both (`registration` creates a `User` **and** registers a `Vehicle`). More than two usually means the feature is too broad — check whether it should be split.

## 4. Finding impact across features

To answer *"what else does this change put at risk?"*:

1. Read this feature's **Entity** values from its registry row.
2. **Search** `features.md` for each entity — every other row listing it shares those records, and is often in a **different domain**, so the hub will not reveal it.
3. Read the **domain hub** (`01_SRS/<domain>/<domain>.md`) for the sibling on the other platform. A `wa_` feature and its `wp_` twin act on the same records through different actors, so admin-side changes routinely break the driver-side view and vice versa.
4. Open those features' AC/TC files and cite **real** IDs. Never invent a `TC-` / `BR-` ID to make a cross-reference look researched.

Both skills do this — `/gen-ac` at step 3b, `/gen-tc` at step 4b — and both report what they checked. When a registry row has a blank Entity cell they say so rather than guessing, because a blank cell silently shrinks every future impact search.

## 5. Traceability

```
Jira ticket  ──▶  AC-<CODE>-NN / BR-<CODE>-NN  ──▶  TC-<CODE>-NNN
  (the why)         (the what — definition of done)     (the how to verify)
```

AC are **optional** — write them when the ticket is ambiguous, high-risk, or needs stakeholder sign-off. For a small clear ticket go straight to TCs and set the `AC` column to `—`. Coverage rule: every business rule and every Critical/High AC needs ≥1 TC.

## 6. Linking discipline

Obsidian builds its graph from wiki-links alone — there is no index file it reads. The tree shape is purely a consequence of who links to whom, so it only survives if everyone follows the same rule:

**One hop per level.**

```
features.md  →  domain hub  →  feature SRS note  →  its AC / TC
```

- `features.md` links to **domain hubs and standalone features only** — never straight to a sub-feature. In the sub-feature tables the SRS column is a plain path in backticks, not a wiki-link.
- A domain with 2+ sub-features has a hub at `01_SRS/<domain>/<domain>.md` listing them. Add a row to the hub when adding a sub-feature.
- An AC or TC note links **up to its own SRS note only** (`[[01_SRS/<domain>/<slug>/<slug>]]` in the header's `SRS ref` row). Never link it to `features.md`, to a hub, or to a sibling feature.
- Cross-feature references go in prose using the other feature's code (`WS`, `AA`), **not** a wiki-link.

This restricts the **graph**, not your thinking. Cross-feature impact analysis is required (§4) — it just travels over **search** rather than backlinks. A code in backticks is plain searchable text, and `Cmd+Shift+F` for `WS` finds every mention instantly. Codes beat wiki-links here: short, stable, and they survive a file moving.

### Never link to a folder

`[[01_SRS/accident/wa_my_accident/]]` — with a trailing slash — does not resolve. Obsidian links point at notes, not folders, so this renders as a dead grey node. Always link the note: `[[01_SRS/accident/wa_my_accident/wa_my_accident]]`. Verify the target file exists before writing the link.

## 7. Templates

`04_Templates/` holds the output formats. Read them from the vault at generation time — never hardcode a copy into a skill.

| File                    | Used by            |
| ----------------------- | ------------------ |
| `ac_template.md`        | `/gen-ac`          |
| `testcases_template.md` | `/gen-tc`          |
| `bug_template.md`       | manual bug reports |

## 8. Writing

- **All note content in English** — body text, table cells, headers, and Type / Priority / Status values. The vault is shared on GitHub. German product terms stay German where the UI uses them; gloss them on first use.
- Test cases stay **high-level**: one scenario, 3–5 steps, no click-by-click. The Cucumber automation layer writes the detailed steps.
- Never fabricate UI you have not seen in a screenshot, and never invent a business rule — flag the assumption instead.
- Never modify `.obsidian/` config as part of a content task.

## 9. Generated folders — do not edit

`docs/` is a symlink tree built by `scripts/build-docs-tree.sh` for MkDocs; `site/` is the built HTML. Both are gitignored **and** excluded from Obsidian's index via `userIgnoreFilters` in `.obsidian/app.json` — without that exclusion every note appears twice in the graph.
