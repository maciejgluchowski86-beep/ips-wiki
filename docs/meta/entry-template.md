---
title: Entry template
---

# Entry template

Use this template only for material that has passed the live-wiki admission gate in [Wiki quality and pruning](wiki-quality-and-pruning.md). Drafts and research scratch work stay outside `docs/` until reviewed.

```markdown
---
title: <Title>
status: definition | standard fact | proved here | observation | literature | conditional | conjecture | heuristic | open
audit: current
tags:
  - <tag>
  - <tag>
---

# <Title>

<Mathematical opening paragraph. State the object or property directly. Link prerequisite concepts inline at their first natural use.>

**References.** <References or "None yet".>

## Definition

<Definition, when applicable.>

## Basic facts

<Essential facts, with hypotheses and accurate status.>

## Why it appears here

<One concise mathematical sentence when the connection is not already obvious.>
```

## Rules

- Use one article per concept and link rather than repeat definitions.
- `status` describes the mathematical role of the content; `audit: current` records that the page has passed the current live-wiki quality gate.
- `proved here` is reserved for a project-specific result whose underlying theorem is `verified` under the current autonomous verification protocol. Legacy uses of `proved here` do not confer verification.
- Use `standard fact` only after the statement and hypotheses have been source-checked. Long standard proofs may be omitted or clearly marked as proof sketches.
- Use `literature` when substantive claims are attributed to and checked against cited sources.
- Use `conditional` only when the unresolved hypothesis is explicitly named or linked.
- Use `observation`, `conjecture`, `open`, and `heuristic` only when the weaker status itself has been checked and the page remains useful to the live reference layer.
- Do not create new `obsolete` pages. Delete obsolete material from the live wiki; Git history is the archive.
- Keep entries focused, nonduplicative, and useful to the reading path or reference layer.
- Use Wikipedia-style inline links through relevant words and phrases. Do not add top-level related-page lists to ordinary entries.
- Keep notation close to repository conventions. Write indicators as \(\ind(X)\), use `\varepsilon`, and use `\(...\)` for inline mathematics and `$$...$$` for displayed mathematics.
- Do not put private strategy, raw scratch work, worker dispatches, tentative proof attempts, or unaudited project claims into `docs/`.
