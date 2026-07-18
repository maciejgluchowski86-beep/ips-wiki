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
- Write indicators in function form as \(\ind(X)\), not with the event in a subscript.
- Use `\varepsilon`, not `\epsilon`.
- Use TeX delimiters `\(...\)` for inline math and `$$...$$` for displayed math.
- Do not put private strategy, raw scratch work, credentials, personal data, or unpublished claims without proof status into this public repository.

## Mathematical prose around displays

- Do not leave isolated bridge fragments such as "with", "Thus", or "and" between displayed formulas.
- Prefer a full sentence that introduces one display containing the whole aligned calculation, or put the connective inside the display using an aligned environment.
- Avoid splitting one definition across several displays when a single aligned display is clearer.

## Linking convention

- Link a concept the first time it is mathematically useful in an entry.
- Avoid linking every repeated occurrence of the same term.
- Prefer semantic links such as `[local functions](local-functions.md)` over navigation lists.
- Use short index/navigation pages only for deliberate curated paths, not as substitutes for inline links.

## Subset convention

- Prefer the non-strict subset command ending in `eq` for subset, possibly equal.
- Prefer the strict subset command ending in `neq` for strict subset.
- Prefer `\Subset` for finite subsets in the countable-lattice setting.
- Avoid the bare ambiguous subset command in polished entries.

## Current mathematical conventions

- The default index object is a lattice \(\Lambda\). A graph is an alternative description of neighbourhoods on \(\Lambda\).
- The single-site state space is denoted by \(\mathcal S\), not \(E\).
- The neighbour set \(N(i)\) does not contain \(i\). The enlarged set \(N_*(i)=N(i)\cup\{i\}\) does contain \(i\).
- Orientation is defined using reachability through neighbour sets: \(i\to j\) means there is a chain from \(i\) to \(j\) with each next site in the previous site's neighbour set.
- An oriented lattice is one where \(i\to j\) and \(i\ne j\) imply not \(j\to i\). Do not introduce extra predecessor/successor notation unless a later page genuinely needs it.
- For KCSM, \(0\) is the facilitating or vacant state, \(q\) is the density of zeros, and \(p=1-q\).
- A spin system is two-state and uses single-site flip updates.
- A finite-state product process with more than two single-site states, or with more general update maps, is called an interacting particle system.
- Infinite-volume generators are first interpreted on local functions.
- For an IPS semigroup, use \(P_t\), with \(P_t=e^{t\cL}\) only as formal generator notation when appropriate.
- Distinguish unique invariant measure, ergodicity, and uniform exponential ergodicity.
