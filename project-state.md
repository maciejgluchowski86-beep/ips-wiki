# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE coding trees

The active research route studies probabilistic representations for terminal-value equations of the form

$$
\partial_tu+\frac12\partial_x^2u+f(u,\partial_xu,\ldots,\partial_x^nu)=0,
\qquad
u(T,\cdot)=\phi.
$$

The starting point is the coding-tree Feynman--Kac representation of Nguwi--Penent--Privault. The current public layer contains both the background construction and an independently audited negative chain describing when repeated Hessian genealogies force failure of absolute integrability.

Further representation comparisons and resummation statements remain under audit and must not be added as established results until separately approved.

## Current wiki phase

The background layer is organized into:

- `docs/entries/heat-reference-fully-nonlinear-pde.md`
- `docs/entries/mild-formulation-and-branching-diffusion-representation.md`
- `docs/entries/npp-coding-tree.md`
- `docs/entries/npp-coding-tree-feynman-kac-theorem.md`
- `docs/entries/directional-jet-radius.md`

The audited obstruction layer is organized into:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/integrable-regime-of-coding-tree.md`

The first three obstruction entries have status `proved here`. The integrable-regime note has status `observation`; it records a direct nonvacuous regime and a narrowly stated issue with the uniform offspring-probability estimate in the printed proof of Nguwi--Penent--Privault Proposition 4.3.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic or unaudited claims as theorems.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Use `Definition`, `Theorem`, `Proposition`, and `Proof` sections for formal mathematical statements.
- Verify literature citations against primary sources, preferably the current arXiv version when available.
- Keep the exact heat-semigroup transfer distinct from any later resummation of nonlinear or derivative chronology.
