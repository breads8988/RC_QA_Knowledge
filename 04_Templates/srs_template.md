# SRS Note — Template

One per feature, at `<hub folder>/<slug>_srs.md`. It holds the written requirement and the feature's screenshots.

Most SRS notes in this vault are **screens-only stubs**: the images exist, the written requirement does not. That is an honest state — say so in the note rather than letting a reader mistake screenshots for a specification.

---

## Screens-only stub (what `/gen-ac` and `/gen-tc` create)

```markdown
---
type: srs
feature: "[[<slug>]]"
code: <CODE>
jira: [RC-<n>]
status: Screens only
---

# SRS — <Feature name>

**Source tickets:** `RC-<n>` (child of Epic `RC-<n>` — <epic name>)

> **Screens only.** This note anchors the feature's screenshots. The written requirement text has not been produced yet — do not treat the images as a specification.

## Screens

![[01_Features/<domain>/<slug>/screens/<file>.png]]
```

## Written SRS

When the requirement text is written, set `status: Draft`, drop the screens-only warning, and add the sections below above `## Screens`:

```markdown
## Purpose

<What problem this solves, for which actor.>

## Scope

<In scope / out of scope, as two short lists.>

## Functional requirements

| ID | Requirement | Source |
| -- | ----------- | ------ |
| FR-<CODE>-01 | <observable behaviour> | `RC-<n>` |

## Constraints and dependencies

<Platform limits, external services (e.g. Calendly, geocoding), records it depends on.>
```

- Embed images with the **full vault path** (`01_Features/<domain>/<slug>/screens/<file>.png`), not a relative one — `scripts/check_links.py` can only verify full paths.
- Every image lives in `screens/`. There is no `figma/` folder.
- Never describe UI you have not seen in a screenshot, and never invent a requirement the ticket does not state.
