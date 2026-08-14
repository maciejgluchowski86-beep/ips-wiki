# Project state

This file records the current state of the IPS wiki. Keep it short and overwrite it when the wiki structure or active research route changes.

## Repository and paper

The wiki is article-first. Source pages live under `docs/entries/`; the canonical IPS paper remains under `paper/`, with repository-level `main.tex` serving as the Overleaf entry point. Do not edit the paper as part of the PDE research track unless explicitly requested.

## Current research route: PDE branching representations

The canonical public entry point is

- `docs/pde-branching-representations.md`.

A fresh reader should start there. It motivates the programme, gives the dependency-ordered reading map, states the settled negative coding-tree chain and representation-level dichotomy, and explains the quadratic-Hessian representation programme.

The PDE wiki is the durable research record. Every `proved here` entry must state its load-bearing hypotheses and logical scope locally rather than rely on chat context.

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
2. `docs/entries/self-consistent-patch-iteration-for-quadratic-hessian-pde.md`, status `proved here`: a small semi-implicit uniformly parabolic iteration contracts in `H^{-1}` and gives the deterministic small solution and its implicit self-consistent diffusion representation.
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

Choose exponentially separated frequencies and factorially decaying coefficients,

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

The theorem applies to the **raw-barycenter-retaining class**. On each raw comb cylinder, if `Q_m` is any positive proposal dominating the intrinsic signed comb measure `nu_m`, an assumed integrable estimator is required to satisfy

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

The datum may be scaled by arbitrarily small `varepsilon`; hence the obstruction occurs inside the C-prime small-data regime.

## Exact status of Conjecture C

`docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture`.

A **strong raw-barycenter reading is false**: one cannot keep the canonical raw signed marked contribution as the conditional barycenter and rescue it by importance sampling or auxiliary conditionally unbiased randomness.

The **literal mark-dependent reading remains open**. An estimator may still sample and use continuous interior marks while changing the raw conditional barycenter. Antithetic/ghost coupling, partial bridge or Rao--Blackwell averaging, control variates across raw states, and coupled multi-sample constructions lie outside the negative theorem.

The current quadratic-Hessian endpoint is therefore a three-way split:

- complete interior averaging: C-prime is proved `L^1`;
- canonical raw-barycenter retention: proved impossible in `L^1` for one fixed arbitrarily small smooth datum;
- non-barycentric retained randomness: open.

Do **not** state that the negative theorem proves all continuous marks must be integrated out. It does not prove that C-prime is minimal or optimal among every possible estimator. It proves that some departure from raw-barycenter retention is necessary; C-prime is the fully averaged endpoint currently proved.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Every proved-here entry must state its full hypotheses locally; cross-links may supply definitions and proofs of prerequisites, not missing assumptions.
- Define every project-specific symbol before use.
- Keep exact Duhamel/semigroup transfer distinct from proposal randomization, raw marked integrands, and later patch averaging.
- Do not write ordinary conditional expectations of unresolved non-`L^1` objects. For negative results, formulate conditional-barycenter properties under an assumed `L^1` candidate and derive a contradiction.
