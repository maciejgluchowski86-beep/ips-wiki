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

## Durable theorem records

- Treat every `proved here` entry as an independently citable durable record, not as a summary of a conversation or of a neighboring page.
- State all load-bearing hypotheses locally in the entry: domains, horizons, regularity classes, parameter ranges, sampling assumptions, and the exact object to which the theorem applies. Cross-links may define standard notation or prove prerequisites, but they must not hide a hypothesis needed to know whether the theorem applies.
- Define every project-specific symbol before its first use. If a standard symbol has a convention that matters to the theorem, state that convention locally or link its definition at first use.
- State logical boundaries locally. In particular, if a theorem proves a conditional, finite-depth, skeleton-averaged, or deterministic statement while a stronger neighboring statement remains open, say exactly what the theorem does and does not prove.
- A reader arriving from the navigation page with no chat history should be able to reconstruct the theorem statement, proof dependencies, and status from the wiki alone.

## Self-contained PDE entries

- The PDE part of the wiki assumes measure-theoretic probability, basic functional analysis, and a first graduate PDE course, but no prior familiarity with branching representations, Malliavin methods, viscosity solutions, advanced parabolic regularity, Gaussian chaos, Gevrey classes, or the NPP/HLOTW literature.
- The canonical entry point is `docs/pde-branching-representations.md`; it should remain synchronized with the settled theorem chain and the current open endpoint.
- Every notion beyond the assumed background must be defined in the entry where it is first used or linked to a prerequisite entry that defines it.
- Lecture-notes style entries are welcome when a concept needs development: motivate the object, define it, state the usable result, prove it when elementary or cite an appropriate source, and explain why it enters the PDE research route.
- The negative coding-tree results and the representation-level dichotomy are settled audited results and should have complete prerequisite paths.
- For the quadratic Hessian equation, keep four layers distinct: finite signed patch exactness/factorization; the deterministic self-consistent theorem; the proved skeleton-averaged `L^1` representation (Theorem C-prime); and the conjectural full random-patch `L^1` representation that retains continuous interior marks.
- State the proved/open fork plainly when relevant: averaging every patch interior first gives the small-data skeleton-only `L^1` theorem; retaining the interior marks leaves the centered raw fluctuation as the open obstruction.
- Do not write `E[H | S]` for an unresolved infinite patch functional unless `H in L^1` has already been established. For C-prime, define the interior-averaged skeleton profile directly by deterministic Duhamel integrals, equivalently through conditional expectations of integrable finite cutoffs.
- When discussing Gaussian kernel bounds, distinguish divergence-form Aronson--Nash theory from nondivergence equations and their adjoints. Do not infer a universal adjoint \(L^\infty\) estimate from ellipticity alone.

## Mathematical prose around displays

- Do not leave isolated bridge fragments such as "with", "Thus", or "and" between displayed formulas.
- Prefer a full sentence that introduces one display containing the whole aligned calculation, or put the connective inside the display using an aligned environment.
- Avoid splitting one definition across several displays when a single aligned display is clearer.

## Linking convention

- Link a concept the first time it is mathematically useful in an entry.
- Avoid linking every repeated occurrence of the same term.
- Prefer semantic links such as `[local functions](../entries/local-functions.md)` over navigation lists.
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
