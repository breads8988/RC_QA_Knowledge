# Feature Registry — retired

The hand-written table that used to live here is gone. **Each feature now carries its own metadata** in the frontmatter of its hub note (`01_Features/<domain>/<slug>/<slug>.md`):

```yaml
type: feature
code: WS                 # ID prefix — AC-WS-01, BR-WS-01, TC-WS-001. Immutable.
domain: workshop
platform: Web App
actor: Driver
entity: ["[[e_workshop|Workshop]]", "[[e_voucher|Voucher]]"]
jira: [RC-120]
status: Draft
```

**To see all features as a table, open [[00_Project_Info/features.base|features.base]]** — it builds the list from those properties, so it can never drift out of date. It has three views: *All features*, *Impact by entity*, *Test coverage*.

Rules for adding a feature, and for the `code` and `entity` values, are in [[00_Project_Info/conventions]] §3.

## Reserved codes

Codes reserved so they stay stable, for features with no folder yet:

| Code | Slug | Note |
| ---- | ---- | ---- |
| `UM` | `user_management` | No folder, no AC/TC. Web Portal / SaaS Admin user management. |

## Open questions

Carried over from the old registry — **not** decided during the restructure:

- **`tourguide` entity.** Recorded as `—` (pure UI). If tour-guide progress is persisted per user, the feature owns `User` and its hub must link [[00_Project_Info/entities/e_user|User]]. Needs a BA or dev to confirm.
- **`homepage` entity.** Recorded as `Ad` because the page renders banners. Confirm that it does not also own `User` data beyond checking session state.
