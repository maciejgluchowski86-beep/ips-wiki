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

The starting point is the coding-tree Feynman--Kac representation of Nguwi--Penent--Privault. The current mathematical investigation concerns integrability of the raw coding-tree functional and possible patch-style resummations of derivative chronologies.

New resummation statements are still under audit. Public wiki entries must not label them `proved here` or state them as established theorems until that audit is complete.

## Current wiki phase

The public background layer is organized into the following entries:

- `docs/entries/heat-reference-fully-nonlinear-pde.md`
- `docs/entries/mild-formulation-and-branching-diffusion-representation.md`
- `docs/entries/npp-coding-tree.md`
- `docs/entries/npp-coding-tree-feynman-kac-theorem.md`
- `docs/entries/directional-jet-radius.md`

These pages define the PDE and jet notation, Duhamel and branching-diffusion background, the Nguwi--Penent--Privault coding construction and Theorem 4.2, and the one-variable analytic growth notions used to diagnose jet-direction derivative growth.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic or unaudited claims as theorems.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Use `Definition`, `Theorem`, `Proposition`, and `Proof` sections for formal mathematical statements.
- Verify literature citations against primary sources, preferably the current arXiv version when available.
- Keep the exact heat-semigroup transfer distinct from any later resummation of nonlinear or derivative chronology.
