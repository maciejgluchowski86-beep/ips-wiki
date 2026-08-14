# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The active research route studies probabilistic representations for terminal-value equations of the form

$$
\partial_tu+\frac12\partial_x^2u+f(u,\partial_xu,\ldots,\partial_x^nu)=0,
\qquad
u(T,\cdot)=\phi.
$$

The public layer now contains background on the Nguwi--Penent--Privault coding tree and HLOTW marked branching, the independently audited repeated-Hessian obstruction chain, and an audited representation-level dichotomy benchmark comparing the absolute-moment behavior of the two constructions for the same terminal-value PDE.

## Current wiki phase

The general background layer is organized into:

- `docs/entries/heat-reference-fully-nonlinear-pde.md`
- `docs/entries/mild-formulation-and-branching-diffusion-representation.md`
- `docs/entries/npp-coding-tree.md`
- `docs/entries/npp-coding-tree-feynman-kac-theorem.md`
- `docs/entries/directional-jet-radius.md`

The branching-literature layer is organized into:

- `docs/entries/marked-branching-diffusion-for-gradient-nonlinearities.md`
- `docs/entries/antithetic-and-ghost-branching-schemes.md`

The audited obstruction layer is organized into:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/integrable-regime-of-coding-tree.md`

The audited comparison layer is organized into:

- `docs/entries/dichotomy-benchmark.md`
- `docs/entries/representation-level-dichotomy.md`

The dichotomy entry has status `proved here`. Its HLOTW half does not treat the Gamma density as a literal instance of published Assumption 3.1: it records the endpoint inconsistency in the paper and proves that the HLOTW Theorems 3.5/3.12 argument extends to the chosen density, which is continuous and positive on `(0,T]` and has the required integrable `t^{-1/2}` singularity at zero. The comparison is between constructions for the same PDE and terminal data; only the HLOTW expectation is identified there with a viscosity solution.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic or unaudited claims as theorems.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Use `Definition`, `Theorem`, `Proposition`, and `Proof` sections for formal mathematical statements.
- Verify literature citations against primary sources, preferably the current arXiv version when available.
- Keep exact heat-semigroup transfer distinct from later resummation or variance-reduction schemes.
