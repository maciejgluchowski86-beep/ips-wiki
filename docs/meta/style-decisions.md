---
title: Style decisions
---

# Style decisions

This page records durable style choices for the public IPS wiki.

## Current defaults

- Write entries as mathematical reference articles, not as commentary about the wiki.
- Prefer Wikipedia-style linking: link relevant words or phrases in the prose at their first natural use.
- Do not maintain a top-level "Related pages" list on ordinary entries; such lists scale poorly.
- Keep visible metadata minimal: references are useful; proof status should be clear from the text or front matter.
- Prefer short entries with explicit mathematical scope.
- Separate definitions, conventions, standard facts, and proof-dependent claims.
- Do not present heuristic or project-specific claims as standard literature.
- Keep notation close to the research repo conventions when possible.
- Use `\varepsilon`, not `\epsilon`.
- Use TeX delimiters `\(...\)` for inline math and `$$...$$` for displayed math.
- Do not put private strategy, raw scratch work, credentials, personal data, or unpublished claims without proof status into this public repository.

## Linking convention

- Link a concept the first time it is mathematically useful in an entry.
- Avoid linking every repeated occurrence of the same term.
- Prefer semantic links such as `[local functions](local-functions.md)` over navigation lists.
- Use short index/navigation pages only for deliberate curated paths, not as substitutes for inline links.

## Current mathematical conventions

- A spin system is two-state and uses single-site flip updates.
- A finite-state product process with more than two single-site states, or with more general update maps, is called an interacting particle system.
- The site space should be specified either as a graph or as a lattice with neighbourhoods.
- Infinite-volume generators are first interpreted on local functions.
