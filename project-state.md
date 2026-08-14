# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The active PDE route studies probabilistic representations for nonlinear parabolic equations. The public layer contains background on the Nguwi--Penent--Privault coding tree and HLOTW marked branching, the independently audited repeated-Hessian obstruction chain, the audited representation-level dichotomy benchmark, and the audited positive route for the quadratic Hessian equation on the torus.

The PDE part of the wiki is required to be self-contained for a reader with measure-theoretic probability, basic functional analysis, and a first graduate PDE course. Concepts beyond that background must be defined locally or linked to a prerequisite article.

## PDE prerequisite layer

The prerequisite layer includes the heat/Duhamel and classical Feynman--Kac formulas; branching-Duhamel trees, age-dependent branching nonexplosion, and importance-sampling compensators; uniform integrability; Gaussian, Malliavin, and Bismut automatic differentiation; Hermite chaos and Holder cancellation; spatial/parabolic Holder and Besov spaces; the bounded parabolic Hessian Duhamel operator; random fields, conditional expectations, and fluctuations in function spaces; spatial jets and Faà di Bruno; viscosity solutions; elementary measure-theoretic tools; parabolic maximum-principle, Schauder, and interior Holder theory; Aronson--Nash cautions; the `H^{-1}` method; weak parabolic solutions; and Ito/backward-Kolmogorov representations.

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

write `z=v_{xx}`. Four logically distinct statements are now recorded.

1. `docs/entries/finite-depth-duhamel-patch-regrouping.md` and `docs/entries/conditional-factorization-for-finite-pde-patches.md` have status `proved here`: finite Picard expansions regroup exactly into maximal left-spine patches, with finite conditional factorization when the centered Gaussian marks remain unexposed.
2. `docs/entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md` has status `proved here`: under the explicit Schauder smallness condition, the semi-implicit iteration stays in the Holder/ellipticity ball, contracts in `H^{-1}` with ratio at most `1/3`, converges to the unique small solution, and gives the implicit self-consistent diffusion representation.
3. `docs/entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md` has status `proved here` (Theorem C-prime): after all continuous branch-time and Gaussian/Hermite variables inside each finite decorated skeleton are integrated out, the deterministic skeleton profiles form an absolutely convergent Catalan series in
   $$
   X_{\alpha,T}=C^{\alpha/2,\alpha}([0,T]\times\mathbb T)
   $$
   whenever
   $$
   4|\lambda|C_{\mathcal D}(\alpha,T)M<1,
   \qquad
   M=\|P_\cdot\phi''\|_{X_{\alpha,T}}.
   $$
   A data-only sufficient condition is
   $$
   4|\lambda|C_{\mathcal D}(\alpha,T)
   (1+\mathbb E|Z|^\alpha)
   \|\phi''\|_{C^\alpha}<1.
   $$
   Sampling only the countable decorated skeleton with any full-support proposal and weighting by its reciprocal probability gives an unbiased `L^1` estimator. The proof uses absolute convergence to justify both the nonlinear Cauchy product and the expectation/skeleton-sum interchange.
4. `docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture`: it retains the raw continuous marks inside each patch and asks for `L^1` of that genuinely random estimator.

Two corrections are permanent for statement 3. A fixed skeleton profile satisfies only its deterministic tree/Duhamel recursion; the **sum** of the skeleton profiles satisfies the nonlinear Hessian mild equation. Also, one must not define the interior average as `E[H | S]` for the unresolved raw infinite-patch functional, because ordinary conditional expectation already requires `H in L^1`. The theorem defines deterministic interior-averaged profiles directly, equivalently as limits of conditional expectations of integrable finite cutoffs, and samples the discrete skeleton first.

For statement 4, deterministic Holder/Hermite growth is no longer the main issue. Raw pathwise Holder control fails already for one centered Hessian edge, and the same high-frequency translation mechanism defeats a fixed same-regularity Besov norm; lowering the exponent only creates a descending regularity ladder. C-prime proves that the interior-average/conditional-mean part is summable. The remaining obstruction is the centered raw fluctuation around that interior average. Its `L^1` function-space amplitude does not close under the next Hessian edge in any fixed Holder or same-regularity Besov space currently considered.

Never conflate finite signed exactness, deterministic convergence, the skeleton-only `L^1` representation, and the full random-patch `L^1` conjecture.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Verify literature citations against primary sources when possible.
- Keep exact Duhamel/semigroup transfer distinct from importance-sampling randomization and from later patch resummation.
- Distinguish divergence-form Aronson--Nash estimates from nondivergence equations and their adjoints; ellipticity alone does not provide a universal adjoint `L^infty` estimate.
