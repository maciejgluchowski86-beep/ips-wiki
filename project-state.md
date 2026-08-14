# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The active PDE route studies probabilistic representations for nonlinear parabolic equations. The public layer contains background on the Nguwi--Penent--Privault coding tree and HLOTW marked branching, the independently audited repeated-Hessian obstruction chain, the audited representation-level dichotomy benchmark, and the audited deterministic positive route for a quadratic Hessian equation on the torus.

The PDE part of the wiki is required to be self-contained for a reader with measure-theoretic probability, basic functional analysis, and a first graduate PDE course. Concepts beyond that background must be defined locally or linked to a prerequisite article. Lecture-notes style prerequisite entries are explicitly acceptable.

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
- `docs/entries/weak-parabolic-solutions-on-the-torus.md`
- `docs/entries/ito-diffusions-and-backward-kolmogorov-representation.md`

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

## Quadratic Hessian route

For the forward torus equation

$$
\partial_tv
=
\frac12\partial_x^2v
+\lambda(\partial_x^2v)^2,
\qquad
v(0)=\phi,
$$

write `z=v_{xx}`. Three statements are kept separate.

1. `docs/entries/finite-depth-duhamel-patch-regrouping.md` has status `proved here`. At every finite Picard depth, maximal left-spine chains give an exact signed reindexing of the finite binary Duhamel-tree expansion. Finite patch-factorization / compensator identities are algebraic and do not imply infinite-depth moment bounds.
2. `docs/entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md` has status `proved here`. With a uniform Schauder constant over the coefficient class `3/8 <= a <= 5/8` and `[a]_{C^{alpha/2,alpha}} <= 1/8`, the smallness condition
   $$
   |\lambda|C_{\mathrm{Sch}}(\alpha,T)\|\phi\|_{C^{2+\alpha}}\leq\frac18
   $$
   preserves the Hölder ball. The semi-implicit profiles contract in `H^{-1}` with ratio at most `1/3`, converge to the unique bounded weak profile in the small class `|lambda z| <= 1/8`, and give the implicit self-consistent diffusion representation. The iteration coefficient lies in `[3/8,5/8]`; the nonlinear/difference ellipticity coefficient lies in `[1/4,3/4]`. The torus mean is
   $$
   m(t)=m(0)+\lambda\int_0^t\frac1{2\pi}\int_{\mathbb T}z(s,x)^2\,dx\,ds.
   $$
3. `docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` has status `conjecture`. The full infinite random patch-first `L^1` estimator is not proved. A smooth high-frequency counterexample shows that even one spatially varying Hessian Duhamel insertion is not bounded from side-profile `L^infty` to output `L^infty`; hence no proof may rely only on products of side-profile sup norms.

Never conflate the three statements. In particular, deterministic convergence and finite signed exactness do not establish the conjectural random-patch `L^1` estimate.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Verify literature citations against primary sources when possible.
- Keep exact Duhamel/semigroup transfer distinct from importance-sampling randomization and from later patch resummation.
- Distinguish divergence-form Aronson--Nash estimates from nondivergence equations and their adjoints; ellipticity alone does not provide a universal adjoint `L^infty` estimate.
