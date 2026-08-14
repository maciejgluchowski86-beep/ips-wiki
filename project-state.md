# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and manuscripts

The wiki is article-first. Source pages live under `docs/entries/`.

There are now two independent manuscript trees:

- `paper/`: the facilitated-spin-system paper. The repository-level `main.tex` remains its Overleaf entry point. Do not edit this manuscript as part of the PDE track unless explicitly requested.
- `pde-paper/`: the standalone manuscript **Cancellation before absolute values in branching representations with derivative weights**. Its entry point is `pde-paper/main.tex`; it has its own preamble, bibliography, and section tree.

The current PDE manuscript draft has the abstract, introduction, and preliminaries written in full. Later sections contain the audited theorem statements and explicit proof placeholders; proofs are to be inserted from the proved-here wiki records rather than reconstructed from memory.

Its narrative spine is:

1. formal signed exactness does not imply `L^1`;
2. the NPP repeated-Hessian obstruction, Gevrey-1/2 necessity, and the NPP/HLOTW benchmark show that integrability depends on representation architecture;
3. finite Hessian patches permit cancellation before absolute values;
4. complete interior averaging gives Theorem C-prime;
5. for one fixed arbitrarily small smooth datum, every raw-faithful estimator has infinite first moment;
6. the remaining problem is formulated through coarsenings of the intrinsic signed patch measures.

The deterministic self-consistent iteration is included only as an auxiliary small-solution/uniqueness result and must not be presented as a principal theorem of the manuscript.

## Current research route: PDE branching representations

The canonical public wiki entry point is

- `docs/pde-branching-representations.md`.

A fresh reader should start there. It motivates the programme, gives the dependency-ordered reading map, states the settled negative coding-tree chain and representation-level dichotomy, and explains the quadratic-Hessian representation programme.

The PDE wiki is the durable mathematical record. Every `proved here` entry must state its load-bearing hypotheses and logical scope locally rather than rely on chat context.

## Settled negative coding-tree chain

The following entries have status `proved here`:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/representation-level-dichotomy.md`

The repeated-Hessian theorem gives non-`L^1` of a composite-code NPP tree when even terminal jet derivatives beat the `m!` simplex scale. Finite directional radius on positive measure implies failure of the all-code NPP integrability hypothesis. Conversely, finite absolute expectation forces a Gevrey-1/2 directional derivative bound almost everywhere. The dichotomy benchmark shows that a raw NPP representation can fail at every positive horizon while an explicit HLOTW marked-branching estimator for the same PDE is `L^2` on a positive interval.

## Quadratic Hessian positive chain

For

$$
\partial_tv
=
\frac12\partial_x^2v
+\lambda(\partial_x^2v)^2,
\qquad
v(0)=\phi,
$$

write `z=v_{xx}`.

1. `docs/entries/finite-depth-duhamel-patch-regrouping.md` and `docs/entries/conditional-factorization-for-finite-pde-patches.md`, status `proved here`: finite Picard trees regroup exactly into maximal left-spine patches, and finite patch randomizations factor conditionally when centered Gaussian marks remain unexposed. These are finite signed identities, not infinite-depth moment estimates.
2. `docs/entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md`, status `proved here`: a small semi-implicit uniformly parabolic iteration contracts in `H^{-1}` and gives the deterministic small solution and its implicit self-consistent diffusion representation. This is the weakest major result in the current chain and is auxiliary in the manuscript.
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
   implies absolute convergence of the deterministic interior-averaged skeleton profiles. Sampling only the decorated skeleton gives an unbiased `L^1` estimator.

Two permanent C-prime corrections: a fixed skeleton profile satisfies only its deterministic tree recursion; the **sum** satisfies the nonlinear Hessian mild equation. Also, do not define the interior average as `E[H | S]` for an unresolved nonintegrable infinite functional. C-prime defines each interior-averaged profile directly by deterministic Duhamel integrals, equivalently through conditional expectations of integrable finite cutoffs.

## Four audited routes through the raw fluctuation

1. **Fixed pathwise Hölder / same-regularity Besov.** A raw centered Hessian edge does not close at the same pathwise regularity.
2. **Decreasing Banach scale.** `docs/entries/banach-scale-obstruction-for-raw-pde-patches.md`, status `proved here`, gives the sharp one-edge first-moment cost `1/delta`. Every stepwise first-moment scale with total loss at most `Delta` pays at least
   $$
   c^n\left(\frac n\Delta\right)^n.
   $$
   This is a proof-architecture barrier, not by itself an estimator-divergence theorem.
3. **Condition all patch interiors.** C-prime gives a proved `L^1` representation after all continuous interior variables are averaged out.
4. **Joint centered marks.** `docs/entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md`, status `proved here`, genuinely escapes the stepwise Banach-scale hypothesis. A two-mark block gains integrability with no intermediate loss, but the all-order canonical retained-mark block has sharp uniform scale
   $$
   c^m m!\leq\mathfrak R_m\leq C^m m!.
   $$
   Signed Gaussian bridge averaging reduces the coefficient to geometric growth, but changes the raw marked object by integrating bridge coordinates.

## Fixed-datum raw-barycenter obstruction

`docs/entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md`, status `proved here`, removes the generation-dependent-frequency caveat for a precise estimator class.

Choose

$$
N_m=K^m,
\qquad
b_m=(m!)^{-1/2},
$$

inside one smooth Hessian datum

$$
g_\varepsilon(x)
=
\varepsilon\left[
\cos x+
\sum_{m\ge m_0}b_m\cos(N_mx)
\right].
$$

For every fixed derivative order `k`, `sum b_m N_m^k < infinity`, so this is one `C^infty` datum. On a disjoint length-`m` comb, terminal Fourier projections isolate frequency `1` on the side leaves and `N_m` on the distinguished leaf. Restricting each centered Hessian duration to

$$
N_m^{-2}\leq r_j\leq\frac{h}{4m}
$$

produces one logarithmic factor per edge and gives

$$
\|\nu_m\|_{\mathrm{TV}}
\gtrsim
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}},
$$

which is not summable.

The theorem applies to the **raw-barycenter-retaining / raw-faithful class**. On each raw comb cylinder, if `Q_m` is any positive proposal dominating the intrinsic signed comb measure `nu_m`, an assumed integrable estimator is required to satisfy

$$
\mathbb E_Q[Y\mid\text{raw marks}]
=
\frac{d\nu_m}{dQ_m}.
$$

Conditional Jensen gives

$$
\mathbb E_Q|Y|
\geq
\sum_m\|\nu_m\|_{\mathrm{TV}}
=\infty.
$$

This covers arbitrary lifetime, genealogy, and Gaussian proposals, arbitrary dependence among proposal variables, and auxiliary conditionally unbiased randomness. It is proposal invariant because the lower bound is the total variation of the intrinsic signed measure.

The datum may be scaled by arbitrarily small `varepsilon`; hence the obstruction occurs inside the C-prime small-data regime. This same-data contrast is a principal theorem-level point of the PDE manuscript.

## Coarsening formulation and remaining open problem

For a finite decorated skeleton `tau`, let `mu_tau` be its intrinsic signed measure on the canonical raw interior-mark space and let

$$
\overline\mu_\tau
=
(\mathcal C_\tau)_\#\mu_\tau
$$

for a measurable coarsening `C_tau`. The canonical coarsened importance sampler has first moment

$$
\sum_\tau\|\overline\mu_\tau\|_{\mathrm{TV}}.
$$

The open problem is whether there is a **nonconstant** coarsening which retains nontrivial continuous interior information and makes this sum finite in the C-prime regime.

The endpoints are settled:

- identity coarsening: impossible for the fixed smooth datum by the raw-faithful obstruction;
- constant coarsening: exactly C-prime, with total variation `|F_tau(t,x)|` and finite sum under the C-prime smallness condition;
- Gaussian-bridge coarsening: natural intermediate candidate; for bare chains it replaces the product of `He_2` scores by one `He_{2m}` endpoint score and changes factorial retained-mark growth into geometric growth.

For every deterministic coarsening,

$$
|F_\tau(t,x)|
\leq
\|(\mathcal C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}
\leq
\|\mu_\tau\|_{\mathrm{TV}}.
$$

Hence the constant coarsening is **total-variation optimal skeleton by skeleton** within deterministic coarsenings. This does not imply that every nonconstant coarsening diverges.

Decorative randomness must be discussed explicitly: appending unused Gaussian marks to the C-prime estimator leaves an `L^1` estimator with random variables in the simulation state, so mere presence of randomness is not the correct retention notion. Antithetic and partially averaged constructions can use marks nontrivially while changing the raw conditional barycenter and therefore lie outside the negative theorem.

## Exact status of Conjecture C

`docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture`.

A **strong raw-barycenter reading is false**. The **literal mark-dependent reading remains open** for non-barycentric retained randomness. Do not state that the negative theorem proves all continuous marks must be integrated out.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Every proved-here entry must state its full hypotheses locally; cross-links may supply definitions and proofs of prerequisites, not missing assumptions.
- Define every project-specific symbol before use.
- Keep exact Duhamel/semigroup transfer distinct from proposal randomization, raw marked integrands, coarsening, and later patch averaging.
- Do not write ordinary conditional expectations of unresolved non-`L^1` objects. For negative results, formulate conditional-barycenter properties under an assumed `L^1` candidate and derive a contradiction.
