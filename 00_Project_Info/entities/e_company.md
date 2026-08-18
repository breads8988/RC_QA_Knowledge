---
type: entity
name: Company
---

# Company (tenant)

The insurance company that owns a tenant. **MCS Admin** creates Companies; each Company gets its own Web Portal, and every end user belongs to exactly one Company.

**Why it matters for testing:** all four apps share one REST API, so any feature that lists or filters company-scoped records can leak data across tenants. A negative AC/TC for cross-tenant access is usually in scope.

Source: [[00_Project_Info/system-high-level-design]] §1, §6.

> Features that read or write this record are the **backlinks** of this note.
