---
title: Style decisions
---

# Style decisions

This page records durable style choices for the public IPS wiki.

## Current defaults

- Write entries as mathematical reference articles, not as commentary about the wiki.
- Keep visible metadata minimal: related pages and references are useful; proof status should be clear from the text or front matter.
- Prefer short entries with explicit mathematical scope.
- Separate definitions, conventions, standard facts, and proof-dependent claims.
- Use Markdown links between entries, for example `[ergodicity](../entries/ergodicity.md)`.
- Do not present heuristic or project-specific claims as standard literature.
- Keep notation close to the research repo conventions when possible.
- Use `\varepsilon`, not `\epsilon`.
- Use TeX delimiters `\(...\)` for inline math and `$$...$$` for displayed math.
- Do not put private strategy, raw scratch work, credentials, personal data, or unpublished claims without proof status into this public repository.

## Current mathematical conventions

- A spin system is two-state and uses single-site flip updates.
- A finite-state product process with more than two single-site states, or with more general update maps, is called an interacting particle system.
- The site space should be specified either as a graph or as a lattice with neighbourhoods.
- Infinite-volume generators are first interpreted on local functions.
