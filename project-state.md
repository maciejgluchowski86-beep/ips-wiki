# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The active PDE route studies probabilistic representations for nonlinear parabolic equations. The public layer contains background on the Nguwi--Penent--Privault coding tree and HLOTW marked branching, the independently audited repeated-Hessian obstruction chain, and the audited representation-level dichotomy benchmark.

The PDE part of the wiki is now required to be self-contained for a reader with measure-theoretic probability, basic functional analysis, and a first graduate PDE course. Concepts beyond that background must be defined locally or linked to a prerequisite article. Lecture-notes style prerequisite entries are explicitly acceptable.

## PDE prerequisite layer

The current prerequisite layer includes:

- `docs/entries/mild-formulation-and-branching-diffusion-representation.md`
- `docs/entries/branching-diffusions-and-duhamel-trees.md`
- `docs/entries/importance-sampling-compensators.md`
- `docs/entries/gaussian-integration-by-parts-and-automatic-differentiation.md`
- `docs/entries/hermite-polynomials-and-gaussian-chaos.md`
- `docs/entries/spatial-jets-total-derivative-and-faa-di-bruno.md`
- `docs/entries/viscosity-solutions.md`
- `docs/entries/tonelli-markov-and-borel-cantelli.md`
- `docs/entries/parabolic-maximum-principle-and-schauder-estimates.md`
- `docs/entries/aronson-nash-gaussian-bounds.md`
- `docs/entries/h-minus-one-energy-method.md`

`docs/entries/directional-jet-radius.md` already defines the directional Taylor radius, Gevrey-1/2 / ultra-analytic derivative bound, entire extension, order, and type, so those notions remain consolidated there rather than duplicated.

## Audited obstruction and comparison results

The obstruction layer remains:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/integrable-regime-of-coding-tree.md`

The first three entries have status `proved here`. The integrable-regime note has status `observation`.

The audited comparison layer remains:

- `docs/entries/dichotomy-benchmark.md`
- `docs/entries/representation-level-dichotomy.md`

The dichotomy entry has status `proved here`. Its HLOTW half proves the required singular-lifetime endpoint extension rather than treating the Gamma density as a literal instance of published Assumption 3.1. Only the HLOTW expectation is identified there with a viscosity solution.

## Second-order quadratic route: current status

For the torus equation

$$
\partial_tu+\frac12\partial_x^2u+\lambda(\partial_x^2u)^2=0,
$$

the repaired deterministic route uses the direct `v`-level maximum principle plus Hölder/Schauder control of `z=v_{xx}`, a smallness condition of the form

$$
|\lambda|C_{\mathrm{Sch}}(\alpha,T)\|\phi\|_{C^{2+\alpha}}\leq\frac18,
$$

and the `H^{-1}` contraction estimate with ellipticity window `[3/8,5/8]` and contraction factor at most `1/3`. The torus mean must be evolved separately when reconstructing `v` from `z`.

What survives as audited project mathematics is the deterministic self-consistent patch iteration, its limiting self-consistent diffusion representation, and the exact finite-level patch-factorization / first-branch identities.

The full random spatially varying patch `L^1` estimate is **conjectural**. A proposed bound by the sup norms of side profiles is false, with a smooth counterexample. Never assign `proved here` status to all-horizon random-patch `L^1` integrability unless a new independent proof is supplied and audited.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Verify literature citations against primary sources when possible.
- Keep exact Duhamel/semigroup transfer distinct from importance-sampling randomization and from later patch resummation.
- Distinguish divergence-form Aronson--Nash estimates from nondivergence equations and their adjoints; ellipticity alone does not provide a universal adjoint `L^infty` estimate.
