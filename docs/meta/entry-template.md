---
title: Entry template
---

# Entry template

Use this template for a new wiki article.

```markdown
---
title: <Title>
status: definition | standard fact | proved here | conditional | heuristic | open | obsolete
tags:
  - <tag>
  - <tag>
---

# <Title>

<Purpose paragraph. State what this entry fixes and which later entries use it.>

**Status.** <Mathematical status.>

**Links.** Related entries: [<entry>](<entry>.md).

**Main references.** <References or "None yet".>

!!! definition "<Name>"
    <Definition.>

!!! convention "<Name>"
    <Convention, if needed.>

!!! remark "<Name>"
    <Clarification, warning, project-specific usage, or relation to neighboring entries.>
```

## Rules

- Use one article per concept.
- Use ordinary Markdown links for cross-links.
- Use TeX delimiters `\(...\)` and `\[...\]` for math.
- Do not silently upgrade a heuristic claim into a standard fact.
- Prefer separate short pages to long survey-style entries.
