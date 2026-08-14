---
title: Entry template
---

# Entry template

Use this template for a new public wiki article.

```markdown
---
title: <Title>
status: definition | standard fact | proved here | observation | literature | conditional | conjecture | heuristic | open | obsolete
tags:
  - <tag>
  - <tag>
---

# <Title>

<Mathematical opening paragraph. State the object or property directly. Link prerequisite concepts inline at their first natural use. Avoid saying what the page does for the wiki.>

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
- Use Wikipedia-style inline links through relevant words and phrases.
- Do not add a top-level "Related pages" list to ordinary entries; such lists scale poorly.
- Keep visible metadata minimal: references are useful; proof status should be clear from the text or front matter.
- Prefer short entries with explicit mathematical scope.
- Separate definitions, conventions, standard facts, and proof-dependent claims.
- Do not present heuristic or project-specific claims as standard literature.
- Keep notation close to the research repo conventions when possible.
- Write indicators in function form as \(\ind(X)\), not with the event in a subscript.
- Use `\varepsilon`, not `\epsilon`.
- Use TeX delimiters `\(...\)` for inline math and `$$...$$` for displayed math.
- Do not put private strategy, raw scratch work, credentials, personal data, or unpublished claims without proof status into this public repository.
- Use `observation` for a checked mathematical or bibliographic observation that is neither being presented as a theorem proved here nor attributed as a standard fact from the literature.
- Use `literature` for an expository entry whose substantive claims are attributed to and checked against cited sources.
- Use `conjecture` for a mathematically precise open statement that is actively proposed as true. Record known obstructions and failed proof routes explicitly when they delimit the conjecture.
- Prefer separate short pages to long survey-style entries.
- Keep public entries free of private scratch work and unpublished claims without proof status.
