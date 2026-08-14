# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The active PDE route studies probabilistic representations for nonlinear parabolic equations. The canonical public entry point is

- `docs/pde-branching-representations.md`.

A fresh reader should start there. It motivates the programme, gives the dependency-ordered reading map, states the settled negative chain and representation-level dichotomy, and explains the current quadratic-Hessian fork.

The PDE part of the wiki is required to be self-contained for a reader with measure-theoretic probability, basic functional analysis, and a first graduate PDE course. Concepts beyond that background must be defined locally or linked to a prerequisite article. Because the wiki is the durable research record, every `proved here` entry must state its own load-bearing hypotheses and may not rely on chat context or an unstated convention from a neighboring page.

## PDE prerequisite layer

The prerequisite layer includes the heat/Duhamel and classical Feynman--Kac formulas; branching-Duhamel trees, age-dependent branching nonexplosion, and importance-sampling compensators; uniform integrability; Gaussian, Malliavin, and Bismut automatic differentiation; Hermite chaos and Holder cancellation; spatial/parabolic Holder and Besov spaces; the bounded parabolic Hessian Duhamel operator; random fields, conditional expectations, and fluctuations in function spaces; spatial jets and Faà di Bruno; viscosity solutions; elementary measure-theoretic tools; parabolic maximum-principle, Schauder, and interior Holder theory; Aronson--Nash cautions; the `H^{-1}` method; weak parabolic solutions; and Ito/backward-Kolmogorov representations.

`docs/entries/directional-jet-radius.md` consolidates directional Taylor radius, Gevrey-1/2 / ultra-analytic derivative bounds, entire extension, order, and type.

## Settled negative chain and dichotomy

The following project-level entries have status `proved here` and now state their full hypotheses locally:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/representation-level-dichotomy.md`

The repeated-Hessian theorem gives non-`L^1` of a composite-code NPP tree when the even terminal jet derivatives beat the `m!` simplex scale. Finite directional radius on positive measure implies failure of the all-code NPP integrability hypothesis. Conversely, finite absolute expectation forces a Gevrey-1/2 directional derivative bound almost everywhere. The dichotomy benchmark shows that the raw NPP representation can fail at every positive horizon while an explicit HLOTW marked-branching estimator for the same PDE is `L^2` on a positive interval.

`docs/entries/integrable-regime-of-coding-tree.md` remains status `observation`; it records nonvacuity rather than another obstruction theorem.

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

write `z=v_{xx}`. Four logically distinct statements are recorded.

1. `docs/entries/finite-depth-duhamel-patch-regrouping.md` and `docs/entries/conditional-factorization-for-finite-pde-patches.md` have status `proved here`. Finite Picard expansions regroup exactly into maximal left-spine patches, and finite patch randomizations factor conditionally when centered Gaussian spatial marks remain unexposed. These are finite signed identities, not infinite-depth moment estimates.
2. `docs/entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md` has status `proved here`. Under
   $$
   |\lambda|C_{\mathrm{Sch}}(\alpha,T)
   \|\phi\|_{C^{2+\alpha}}
   \leq\frac18,
   $$
   the semi-implicit iteration stays in the Holder/ellipticity ball, contracts in `H^{-1}` with ratio at most `1/3`, converges to the unique small solution, and gives the implicit self-consistent diffusion representation.
3. `docs/entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md` has status `proved here` and is Theorem C-prime. Put
   $$
   X_{\alpha,T}=C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
   \qquad
   M=\|P_\cdot\phi''\|_{X_{\alpha,T}}.
   $$
   If
   $$
   4|\lambda|C_{\mathcal D}(\alpha,T)M<1,
   $$
   then the deterministic interior-averaged profiles of finite decorated binary skeletons form an absolutely convergent Catalan series in `X_{alpha,T}`. Sampling only the countable decorated skeleton with any full-support proposal and weighting by its reciprocal probability gives an unbiased `L^1` estimator. Absolute convergence justifies both the nonlinear Cauchy product and the expectation/skeleton-sum interchange.
4. `docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture`. It is now stated concretely on the explicit C-prime small-data regime and asks whether one may retain the continuous Gaussian/Hermite, branch-time, and descendant marks inside patches while preserving `L^1` and unbiasedness.

Two corrections are permanent for C-prime. A fixed skeleton profile satisfies only its deterministic tree/Duhamel recursion; the **sum** of skeleton profiles satisfies the nonlinear Hessian mild equation. Also, one must not define the interior average as `E[H | S]` for an unresolved raw infinite-patch functional, because ordinary conditional expectation already requires `H in L^1`. C-prime defines each interior-averaged profile directly by deterministic Duhamel integrals, equivalently through conditional expectations of integrable finite cutoffs.

## Canonical proved/open fork

The current fork should always be stated this way.

**Condition all patch interiors first.** Integrate out the continuous branch-time, Brownian, Gaussian/Hermite, and descendant variables attached to a finite decorated skeleton before sampling the skeleton. Under the C-prime Catalan smallness condition, the resulting skeleton profiles are absolutely summable and give a proved unbiased `L^1` skeleton-only estimator.

**Retain the interior marks.** The centered raw fluctuation survives. Direct pathwise Holder control fails already for one centered Hessian edge; a fixed same-regularity Besov norm has the same high-frequency translation obstruction, and lowering regularity creates a descending ladder. Controlling this fluctuation is precisely the open content of conjecture C.

Never conflate finite signed exactness, deterministic convergence, the skeleton-only `L^1` representation, and the full random-patch `L^1` conjecture.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Every proved-here entry must state its full hypotheses locally; cross-links may supply definitions and proofs of prerequisites, not missing assumptions.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Verify literature citations against primary sources when possible.
- Keep exact Duhamel/semigroup transfer distinct from importance-sampling randomization and from later patch resummation.
- Distinguish divergence-form Aronson--Nash estimates from nondivergence equations and their adjoints; ellipticity alone does not provide a universal adjoint `L^infty` estimate.
