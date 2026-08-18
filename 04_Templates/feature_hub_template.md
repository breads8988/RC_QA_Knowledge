# Feature Hub — Template

The hub is a feature's **entry point and its only metadata store**. One per feature, at `01_Features/<domain>/<slug>/<slug>.md` (standalone features drop the `<domain>/` level).

Everything else about the feature is derived from it: `00_Project_Info/features.base` builds its tables from these properties, and the `entity` links are what connect this feature to every other feature that touches the same records.

Rules for `code`, `entity`, `platform` and `actor` are in [[00_Project_Info/conventions]] §3–§4. Read them before filling this in — a wrong `entity` silently breaks impact analysis for every future ticket.

---

```markdown
---
type: feature
code: <CODE>                   # 2–6 uppercase letters, unique in the vault, NEVER changes
domain: <domain>               # omit this line entirely for a standalone feature
platform: <Web App | Web Portal | Android | SaaS Admin>
actor: <Driver | Client Admin | MCS Admin>
entity:                        # links to 00_Project_Info/entities/ — [] if the feature owns no record
  - "[[e_<entity>|<Entity>]]"
jira: [RC-<n>]                 # story tickets only, never the epic
status: <Draft | Not started | Reviewed>
srs: "[[<slug>_srs]]"
ac: "[[<slug>_ac]]"            # omit until the AC spec exists
tc: "[[<slug>_tc]]"            # omit until the TC register exists
related: []                    # only for a real dependency that shares NO entity
---

# <Feature name> (`<CODE>`)

<Two to four lines: what the feature does, for which actor. No UI detail you have
not seen in a screenshot, no business rule the ticket does not state.>

Open [[e_<entity>|<Entity>]] to see every other feature that touches the same records — its backlinks are the impact list.
```

## When `related:` is justified

Almost never. Two features that share a record already meet at the entity note — adding a `related:` link between them duplicates that edge and has to be maintained by hand.

Use it only when a real dependency exists and the two features share **no** entity, and write the reason in the body:

```markdown
related:
  - "[[homepage]]"

## Related features

| Feature | Code | Why |
| ------- | ---- | --- |
| [[homepage]] | `HOME` | The tour-guide popups are anchored to home-page elements; a layout change there breaks them. |
```
