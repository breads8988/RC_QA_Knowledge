# Vault conventions

**This file is the single source of truth for how this vault is structured.** Every other file — `CLAUDE.md`, `README.md`, the two skills — points here instead of restating these rules. When a rule changes, change it here and nowhere else.

For *what the product is* — actors, domain vocabulary, entities — read `CLAUDE.md` instead. That is the business layer; this is the structural layer.

The vault is shared via GitHub, so **every path must be relative**. Never write a machine-specific absolute path into a note.

---

## 1. One feature, one folder

Everything about a feature lives together:

```
01_Features/<domain>/<slug>/<slug>.md          ← feature hub: all metadata
01_Features/<domain>/<slug>/<slug>_srs.md      ← requirement note
01_Features/<domain>/<slug>/<slug>_ac.md       ← acceptance criteria
01_Features/<domain>/<slug>/<slug>_tc.md       ← test case register
01_Features/<domain>/<slug>/screens/*.png      ← every image: app screenshots and Figma exports
01_Features/<domain>/<domain>.md               ← domain hub, when the domain has 2+ features
```

- **A feature that belongs to no domain drops the `<domain>/` level:** `01_Features/login/login.md`.
- Domains in use: `accident`, `lawyer`, `voucher`, `workshop` — the four subjects that have both a Web App and a Web Portal feature. Everything else is standalone.
- **A folder is a feature if it contains `<name>_srs.md`.** A domain folder contains only feature folders. Scripts and skills use this to tell the two apart.
- `_ac.md` and `_tc.md` are **optional** (see §5); `<slug>.md` and `<slug>_srs.md` always exist.
- **One `screens/` folder, no `figma/`.** Where an image came from is not worth a second folder.

## 2. Slug and platform prefix

- **Slug** — lowercase, identical to the feature folder name. This is what you pass to `/gen-ac` and `/gen-tc`.
- A slug under a shared domain carries **`wa_`** (Web App, the driver) or **`wp_`** (Web Portal, the Client Admin). The prefix is not cosmetic — it identifies the actor and the permission model. See `CLAUDE.md` for who those actors are.
- **Never register a bare domain name as a slug.** `workshop` alone is ambiguous between the driver feature and the admin feature, and that ambiguity is what once made the graph unreadable.

## 3. Feature metadata

There is no registry file. **The feature hub is the source of truth** for its own metadata:

```yaml
---
type: feature
code: WS                       # ID prefix — AC-WS-01, BR-WS-01, TC-WS-001
domain: workshop               # omitted for a standalone feature
platform: Web App              # Web App | Web Portal | Android | SaaS Admin
actor: Driver                  # Driver | Client Admin | MCS Admin
entity:                        # links, not plain text — see §4
  - "[[e_workshop|Workshop]]"
  - "[[e_voucher|Voucher]]"
jira: [RC-120]                 # story tickets only, never the epic
status: Draft
srs: "[[wa_workshop_srs]]"
ac: "[[wa_workshop_ac]]"       # omit if the feature has no AC
tc: "[[wa_workshop_tc]]"       # omit if the feature has no TC
related: []                    # see §6 — normally empty
---
```

- **Code** — 2–6 uppercase letters, unique across the whole vault. Used only in IDs: `AC-<CODE>-NN`, `BR-<CODE>-NN`, `TC-<CODE>-NNN`.
- **A code already used in any ID must never change** — it would break traceability across hundreds of IDs. Reserved codes for features that have no folder yet are listed in `features.md`.
- `[[00_Project_Info/features.base|features.base]]` renders all of this as a live table (views: *All features*, *Impact by entity*, *Test coverage*). It is generated from the hubs — never edit a feature's data there.
- SRS / AC / TC notes carry a lighter header: `type`, `feature` (a link back to the hub), `code`, `jira`, `status`. TC registers add `tc_total`, `tc_automated`, `tc_pending`.

## 4. Entities, and finding impact across features

The domain tree groups features by *subject area*. It does **not** show impact: the `Voucher` record is touched by four features spread across two domains, so a voucher change puts all four at risk while the domain hubs show them as two unrelated trees.

**Entity notes are the second, orthogonal axis.** One note per record type in `00_Project_Info/entities/`:

`e_company` · `e_user` · `e_vehicle` · `e_accident` · `e_workshop` · `e_expert` · `e_lawyer` · `e_voucher` · `e_ad` · `e_pricing`

Every feature hub links to the entities it owns. That single link is the whole mechanism:

> **To answer "what else does this change put at risk?" — open the entity note and read its Backlinks.** Every feature that touches those records is listed there, automatically, including features in other domains.

Rules for the `entity` value:

- Declare only the entity the feature takes as its **subject** — the records it reads or writes as its actual job. Use `entity: []` when there is none (pure-UI features).
- **Do not** declare an entity a feature merely branches on. Almost every screen behaves differently for a logged-in vs. guest user; if that counted, every feature would list `User` and the axis would carry no information. `homepage` lists `Ad` (it renders banners), not `User` (it only checks session state).
- One entity is normal; two happens when a feature genuinely owns both (`registration` creates a `User` **and** registers a `Vehicle`). More than two usually means the feature is too broad — check whether it should be split.
- **The `e_` prefix is required.** An entity note called `Voucher.md` would collide with the `voucher` domain hub — Obsidian resolves link targets case-insensitively — and every impact edge would silently point at the wrong note. Link with a display alias: `"[[e_voucher|Voucher]]"`.

Both skills do this — `/gen-ac` at step 3b, `/gen-tc` at step 4b — and both report what they checked. When a hub has an empty `entity` they say so rather than guessing, because an empty value silently shrinks every future impact search.

## 5. Traceability

```
Jira ticket  ──▶  AC-<CODE>-NN / BR-<CODE>-NN  ──▶  TC-<CODE>-NNN
  (the why)         (the what — definition of done)     (the how to verify)
```

AC are **optional** — write them when the ticket is ambiguous, high-risk, or needs stakeholder sign-off. For a small clear ticket go straight to TCs and set the `AC` column to `—`. Coverage rule: every business rule and every Critical/High AC needs ≥1 TC.

## 6. Linking discipline

Obsidian builds its graph from links alone, **including links written in frontmatter**. The rules exist so the graph stays a set of readable feature clusters instead of a hairball:

| Direction | How | Who maintains it |
| --------- | --- | ---------------- |
| Feature hub → its SRS / AC / TC | frontmatter `srs:` / `ac:` / `tc:` | the skills, automatically |
| SRS / AC / TC → its feature hub | frontmatter `feature:` | the skills, automatically |
| Feature hub → entity | frontmatter `entity:` | **the one human decision**, once per feature |
| Feature ↔ feature | nothing — they meet at the shared entity note | automatic |
| Domain hub → its features | a body table of wiki-links | on feature creation |
| Feature hub → feature hub (`related:`) | only for a real dependency that shares **no** entity | rare, by hand, with the reason written in the body |
| Inside AC / TC prose | the other feature's **code** in backticks (`WS`, `AA`) — never a wiki-link | — |

- **An AC or TC note never links sideways.** It links up to its hub and nowhere else. Cross-feature impact belongs in the analysis, cited by code.
- Codes beat wiki-links in prose: short, stable, searchable with `Cmd+Shift+F`, and they survive a file moving.

### Never link to a folder

`[[01_Features/accident/wa_my_accident/]]` — with a trailing slash — does not resolve. Obsidian links point at notes, not folders, so this renders as a dead grey node. Always link the note. **Verify the target file exists before writing the link**, or run `python scripts/check_links.py`, which checks every wiki-link, embed and backtick path in the vault and exits non-zero if any is unresolved.

## 7. Templates

`04_Templates/` holds the output formats. Read them from the vault at generation time — never hardcode a copy into a skill.

| File                    | Used by            |
| ----------------------- | ------------------ |
| `feature_hub_template.md` | creating a feature |
| `srs_template.md`       | creating a feature |
| `ac_template.md`        | `/gen-ac`          |
| `testcases_template.md` | `/gen-tc`          |
| `bug_template.md`       | manual bug reports |

## 8. Writing

- **All note content in English** — body text, table cells, headers, and Type / Priority / Status values. The vault is shared on GitHub. German product terms stay German where the UI uses them; gloss them on first use. A verbatim stakeholder quote may stay in its original language **only if an English gloss follows it in parentheses** — the quote is evidence, the gloss is the content.
- Test cases stay **high-level**: one scenario, 3–5 steps, no click-by-click. The Cucumber automation layer writes the detailed steps.
- Never fabricate UI you have not seen in a screenshot, and never invent a business rule — flag the assumption instead.
- Never modify `.obsidian/` config as part of a content task.

## 9. Generated folders — do not edit

`docs/` is a symlink tree built by `scripts/build-docs-tree.sh` for MkDocs; `site/` is the built HTML. Both are gitignored **and** excluded from Obsidian's index via `userIgnoreFilters` in `.obsidian/app.json` — without that exclusion every note appears twice in the graph.
