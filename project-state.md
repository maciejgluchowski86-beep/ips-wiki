# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The active PDE route studies probabilistic representations for nonlinear parabolic equations. The canonical public entry point is

- `docs/pde-branching-representations.md`.

A fresh reader should start there. It motivates the programme, gives the dependency-ordered reading map, states the settled negative chain and representation-level dichotomy, and explains the current quadratic-Hessian fork.

The PDE part of the wiki is required to be self-contained for a reader with measure-theoretic probability, basic functional analysis, and a first graduate PDE course. Concepts beyond that background must be defined locally or linked to a prerequisite article. Because the wiki is the durable research record, every `proved here` entry must state its own load-bearing hypotheses and may not rely on chat context or an unstated convention from a neighboring page.

## Settled negative chain and dichotomy

The following project-level entries have status `proved here`:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/representation-level-dichotomy.md`

The repeated-Hessian theorem gives non-`L^1` of a composite-code NPP tree when the even terminal jet derivatives beat the `m!` simplex scale. Finite directional radius on positive measure implies failure of the all-code NPP integrability hypothesis. Conversely, finite absolute expectation forces a Gevrey-1/2 directional derivative bound almost everywhere. The dichotomy benchmark shows that the raw NPP representation can fail at every positive horizon while an explicit HLOTW marked-branching estimator for the same PDE is `L^2` on a positive interval.

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

write `z=v_{xx}`. The settled positive chain is:

1. `docs/entries/finite-depth-duhamel-patch-regrouping.md` and `docs/entries/conditional-factorization-for-finite-pde-patches.md`, status `proved here`: finite Picard expansions regroup exactly into maximal left-spine patches, and finite patch randomizations factor conditionally when centered Gaussian spatial marks remain unexposed. These are finite signed identities, not infinite-depth moment estimates.
2. `docs/entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md`, status `proved here`: under
   $$
   |\lambda|C_{\mathrm{Sch}}(\alpha,T)
   \|\phi\|_{C^{2+\alpha}}
   \leq\frac18,
   $$
   the semi-implicit iteration stays in the Holder/ellipticity ball, contracts in `H^{-1}` with ratio at most `1/3`, converges to the unique small solution, and gives the implicit self-consistent diffusion representation.
3. `docs/entries/skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md`, status `proved here` (Theorem C-prime): with
   $$
   X_{\alpha,T}=C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
   \qquad
   M=\|P_\cdot\phi''\|_{X_{\alpha,T}},
   $$
   the condition
   $$
   4|\lambda|C_{\mathcal D}(\alpha,T)M<1
   $$
   implies absolute convergence of the deterministic interior-averaged skeleton profiles and gives an unbiased `L^1` estimator after sampling only the countable decorated skeleton.
4. `docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md`, status `conjecture`: retain the continuous Gaussian/Hermite, branch-time, and descendant marks inside the patches while preserving `L^1` and unbiasedness.

Two permanent corrections for C-prime: a fixed skeleton profile satisfies only its deterministic tree/Duhamel recursion; the **sum** satisfies the nonlinear Hessian mild equation. Also, do not define the interior average as `E[H | S]` for an unresolved raw infinite-patch functional, since ordinary conditional expectation already requires `H in L^1`. C-prime defines each interior-averaged profile directly by deterministic Duhamel integrals, equivalently through conditional expectations of integrable finite cutoffs.

## Current fluctuation barriers

The centered raw fluctuation is the only remaining obstruction between C-prime and conjecture C. Three negative facts are now settled.

1. A fixed pathwise Holder norm does not close even for one centered Hessian edge.
2. A fixed same-regularity Besov norm has the same high-frequency translation obstruction.
3. `docs/entries/banach-scale-obstruction-for-raw-pde-patches.md`, status `proved here`, rules out the decreasing-Hölder-exponent repair for any **stepwise first-moment Banach-scale argument**.

For the raw edge

$$
\widehat K_r f(x,Z)
=
\frac{He_2(Z)}r
\left[f(x+\sqrt r Z)-f(x)\right],
$$

the optimal time-integrated first-moment norm from `C^alpha` to `C^(alpha-delta)` is of order `1/delta`. If

$$
\delta_k=\alpha_{k-1}-\alpha_k>0,
\qquad
\sum_{k=1}^n\delta_k\leq\Delta,
$$

then every stepwise first-moment proof that takes a Banach norm after each centered edge incurs at least

$$
c^n\prod_{k=1}^n\delta_k^{-1}
\geq
c^n\left(\frac n\Delta\right)^n.
$$

The uniform budget `delta_k=Delta/n` is optimal; geometric and other nonuniform budgets are worse. Chronological ordering does not restore a hidden `1/n!`: the corresponding Dirichlet time integral contains `prod Gamma(delta_k/2)` and has the same product `prod delta_k^{-1}` singularity.

This is a proof-architecture barrier, not a disproof of conjecture C. The sharp one-edge lower bound is saturated by frequencies `N ~ exp(c/delta)`. Under the optimal depth-`n` budget, the saturating frequency grows like `exp(c n/Delta)`, so the test datum changes with depth. No fixed smooth terminal datum is shown to realize the worst-case operator norms at every generation.

The result rules out the bare Nash--Moser-style **loss budget by itself**. It does not rule out every genuine Nash--Moser smoothing/telescoping construction, because such a scheme can retain frequency information and compensate smoothing errors rather than applying a uniform Banach-space operator bound at each generation.

## Canonical proved/open fork

**Condition all patch interiors first.** Integrate out the continuous branch-time, Brownian, Gaussian/Hermite, and descendant variables attached to a finite decorated skeleton before sampling the skeleton. Under the C-prime Catalan smallness condition, the resulting skeleton profiles are absolutely summable and give a proved unbiased `L^1` skeleton-only estimator.

**Retain the interior marks.** The centered raw fluctuation survives. Fixed Holder and same-regularity Besov spaces fail, and the proved Banach-scale obstruction shows that merely spending a bounded amount of regularity across generations yields the supergeometric `(n/Delta)^n` cost.

A successful proof of C must therefore preserve more structure before taking absolute values: retain frequency, retain frequency together with genealogy, exploit a multiscale martingale/square-function mechanism, or allow cancellation across several centered Gaussian/Hermite marks before taking a first-moment norm.

Never conflate finite signed exactness, deterministic convergence, the skeleton-only `L^1` representation, the Banach-scale proof barrier, and the full random-patch `L^1` conjecture.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Every proved-here entry must state its full hypotheses locally; cross-links may supply definitions and proofs of prerequisites, not missing assumptions.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Verify literature citations against primary sources when possible.
- Keep exact Duhamel/semigroup transfer distinct from importance-sampling randomization and from later patch resummation.
- Distinguish divergence-form Aronson--Nash estimates from nondivergence equations and their adjoints; ellipticity alone does not provide a universal adjoint `L^infty` estimate.
