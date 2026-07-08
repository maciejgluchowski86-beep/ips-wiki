---
title: Entry template
---

# Entry template

Use this template for a new public wiki article.

```markdown
---
title: <Title>
status: definition | standard fact | proved here | conditional | heuristic | open | obsolete
tags:
  - <tag>
  - <tag>
---

# <Title>

<Mathematical opening paragraph. State the object or property directly. Avoid saying what the page does for the wiki.>

**Related pages.** [<entry>](<entry>.md), [<entry>](<entry>.md).

**References.** <References or "None yet".>

## Definition

<Definition.>

## Basic facts

<Standard facts, with hypotheses.>

## Conventions

<Conventions, only if needed.>
```

## Rules

- Use one article per concept.
- Use ordinary Markdown links for cross-links.
- Use `\(...\)` for inline math.
- Use `$$...$$` for displayed math.
- Do not use raw `\[...\]` display blocks in entries.
- Do not silently upgrade a heuristic claim into a standard fact.
- Prefer separate short pages to long survey-style entries.
- Keep public entries free of private scratch work and unpublished claims without proof status.
