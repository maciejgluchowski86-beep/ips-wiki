# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The active PDE route studies probabilistic representations for nonlinear parabolic equations. The public layer contains background on the Nguwi--Penent--Privault coding tree and HLOTW marked branching, the independently audited repeated-Hessian obstruction chain, the audited representation-level dichotomy benchmark, and the audited deterministic positive route for a quadratic Hessian equation on the torus.

The PDE part of the wiki is required to be self-contained for a reader with measure-theoretic probability, basic functional analysis, and a first graduate PDE course. Concepts beyond that background must be defined locally or linked to a prerequisite article. Lecture-notes style prerequisite entries are explicitly acceptable.

## PDE prerequisite layer

The prerequisite layer now includes the heat/Duhamel and classical Feynman--Kac formulas; branching-Duhamel trees, age-dependent branching nonexplosion, and importance-sampling compensators; uniform integrability; Gaussian, Malliavin, and Bismut automatic differentiation; Hermite chaos and Holder cancellation; spatial/parabolic Holder and Besov spaces; random fields, conditional expectations, and fluctuations in function spaces; spatial jets and Faà di Bruno; viscosity solutions; elementary measure-theoretic tools; parabolic maximum-principle, Schauder, and interior Holder theory; Aronson--Nash cautions; the `H^{-1}` method; weak parabolic solutions; and Ito/backward-Kolmogorov representations.

`docs/entries/directional-jet-radius.md` continues to consolidate directional Taylor radius, Gevrey-1/2 / ultra-analytic derivative bounds, entire extension, order, and type.

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

For

$$
\partial_tv
=
\frac12\partial_x^2v
+\lambda(\partial_x^2v)^2,
\qquad
v(0)=\phi,
$$

write `z=v_{xx}`. Three statements remain separate.

1. `docs/entries/finite-depth-duhamel-patch-regrouping.md` and `docs/entries/conditional-factorization-for-finite-pde-patches.md` have status `proved here`: finite Picard expansions regroup exactly into maximal left-spine patches, and the finite patch-first randomization factorizes conditionally when the patch skeleton exposes branch times/types but leaves the centered Gaussian spatial marks unexposed.
2. `docs/entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md` has status `proved here`: under the explicit Schauder smallness condition, the semi-implicit iteration stays in the Holder/ellipticity ball, contracts in `H^{-1}` with ratio at most `1/3`, converges to the unique small solution, and gives the implicit self-consistent diffusion representation.
3. `docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture`.

For statement 3, Hermite centering and commutator clustering give one Holder gain per derivative cluster. A length-`m` patch has at most `2^m` commutator terms, not `2^{m-1}`: the latter only counts ordered compositions, while the innermost cluster has one additional terminal choice. The correction remains geometric and does not alter the conclusion that deterministic patches with uniformly controlled spatial `C^alpha` side profiles have geometric, not factorial, growth.

The direct pathwise random-Holder route has failed. For

$$
\widehat K_rf(x,Z)
=
\frac{He_2(Z)}r
\bigl(f(x+\sqrt r Z)-f(x)\bigr),
$$

the expected sup norm gains `r^{alpha/2}`, but the pathwise `C^alpha` seminorm does not; uniformly on the `C^alpha` unit ball its expected size remains of order `r^{-1}`. Thus recursive `L^p(Omega;C^alpha)` bounds for raw edge fields cannot supply the deterministic Holder cancellation.

The live formulation uses the conditional mean given the exposed patch skeleton. Averaging the fresh Gaussian and descendant randomness first restores the deterministic heat-derivative operator, and finite-depth patch factorization gives products of conditional mean side fields. The current regularity problem is to propagate suitable Holder/comparable bounds for these conditional means, uniformly in birth time and position. Writing a raw side field as

$$
Y_P=m_P+R_P,
\qquad
m_P=\mathbb E[Y_P\mid\mathcal G_P],
\qquad
\mathbb E[R_P\mid\mathcal G_P]=0,
$$

the centered fluctuation `R_P` is the likely next absolute-moment obstruction. Conditional-mean regularity alone does not prove `L^1` for the full estimator.

Never conflate finite signed exactness, deterministic convergence, and the random-patch `L^1` conjecture.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Verify literature citations against primary sources when possible.
- Keep exact Duhamel/semigroup transfer distinct from importance-sampling randomization and from later patch resummation.
- Distinguish divergence-form Aronson--Nash estimates from nondivergence equations and their adjoints; ellipticity alone does not provide a universal adjoint `L^infty` estimate.
