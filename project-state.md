# Project state

This file records the current state of the IPS wiki and the active PDE manuscript.

## Repository and manuscripts

There are two independent manuscript trees.

- `paper/`: facilitated-spin-system paper. The repository-level `main.tex` remains its Overleaf entry point. Do not edit it as part of the PDE track unless explicitly requested.
- `pde-paper/`: standalone manuscript **Cancellation before absolute values in branching representations with derivative weights**. Its entry point is `pde-paper/main.tex`; it has its own preamble, bibliography, and sections.

The PDE manuscript now contains full proofs of every audited result currently included: repeated-Hessian obstruction, Gevrey-1/2 necessity, the NPP/HLOTW representation-level dichotomy, finite Hessian patch regrouping, the auxiliary deterministic iteration, Theorem C-prime, the fixed-datum raw-faithful obstruction, and the coarsening hierarchy. The former `coarsening-open-problem.tex` section has been replaced by `coarsening-hierarchy.tex`.

The deterministic self-consistent iteration remains auxiliary and should not be presented as a principal theorem.

## Canonical PDE wiki entry point

- `docs/pde-branching-representations.md`

The wiki is the durable mathematical record. Every `proved here` entry must state its load-bearing hypotheses and scope locally.

## Settled coding-tree chain

The following are `proved here`:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/representation-level-dichotomy.md`

The repeated-Hessian genealogy gives a lower bound of order `c^m D_m/m!`; proposal and lifetime factors cancel their reciprocal compensators. Integrability forces a Gevrey-1/2 directional jet. The benchmark

$$
\partial_tu+\frac12u_{xx}+\eta(e^{(u_x)^4}-1)=0
$$

has a raw NPP functional which is non-`L^1` at every positive horizon while an explicit HLOTW estimator is `L^2` for short time. This establishes representation dependence of absolute integrability.

## Quadratic Hessian positive chain

For

$$
\partial_tv
=
\frac12v_{xx}+\lambda(v_{xx})^2,
\qquad
z=v_{xx},
$$

finite Picard trees regroup exactly into maximal left-child patches.

Theorem C-prime uses

$$
X_{\alpha,T}=C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
\qquad
M=\|P_\cdot\phi''\|_{X_{\alpha,T}},
\qquad
 a=|\lambda|C_{\mathcal D}(\alpha,T)M.
$$

If

$$
4a<1,
$$

the deterministic interior-averaged skeleton profiles are absolutely summable. Sampling only the decorated skeleton gives an unbiased `L^1` estimator.

Permanent C-prime corrections: a fixed skeleton profile satisfies only its tree recursion; the sum satisfies the nonlinear mild equation. Do not define C-prime by conditioning an unresolved non-`L^1` infinite raw estimator.

## Raw-faithful fixed-datum obstruction

`docs/entries/raw-marked-l1-obstruction-for-quadratic-hessian-pde.md` is `proved here`.

The obstruction may be realized on **right-oriented combs**. Put

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

For every fixed derivative order `k`, `sum b_m N_m^k < infinity`; hence one fixed `C^infty` datum contains every required scale. On the length-`m` right comb, restricting every Hessian duration to

$$
N_m^{-2}\le r_j\le\frac h{4m}
$$

gives one logarithm per retained centered edge and

$$
\|\mu_m\|_{\mathrm{TV}}
\gtrsim
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}}.
$$

The sum diverges. If an assumed `L^1` estimator has the canonical raw signed contribution as conditional barycenter after the raw marks are exposed, conditional Jensen gives infinite first moment. The theorem is invariant under lifetime, genealogy, and Gaussian proposal changes, arbitrary dependence among proposal variables, and auxiliary conditionally unbiased randomness.

The datum can be scaled into the C-prime regime, so the same small smooth datum has an `L^1` C-prime representation and no raw-faithful `L^1` representation.

## Coarsening hierarchy

`docs/entries/time-spine-coarsening-for-quadratic-hessian-patches.md` is `proved here`.

### Naive Gaussian-bridge coarsening fails

Patches are maximal left-child chains. In a right comb every left child is terminal and the continuing child is right, so every patch has length one. A one-edge Gaussian bridge map has no bridge coordinate to remove: the normalized endpoint Gaussian is the original Gaussian mark. Therefore naive patchwise Gaussian-bridge coarsening is the identity, up to an invertible coordinate change, on the obstruction combs and preserves their divergent total variation.

### Time-spine coarsening succeeds

For each non-leaf tree, retain the ordered branch times on its **root maximal-left patch**, average all Gaussian/Brownian marks on that patch, and average every continuous variable in the attached side subtrees.

Let `K_time(alpha,T)` be the optimal geometric base for the absolute time-integral of one deterministic maximal-left patch. The derivative-cluster/commutator estimate gives

$$
K_{\mathrm{time}}(\alpha,T)<\infty.
$$

Put

$$
b=|\lambda|K_{\mathrm{time}}M,
\qquad
C(a)=\sum_{n\ge0}C_na^n
=
\frac{1-\sqrt{1-4a}}{2a},
\quad C(0)=1.
$$

If

$$
4a<1,
\qquad
bC(a)<1,
$$

then

$$
\sum_{\tau}
\|(\mathcal C_\tau^{\mathrm{time}})_\#\mu_\tau\|_{\mathrm{TV}}
\le
\frac{M}{1-bC(a)}
<\infty.
$$

Thus the canonical coarsened importance sampler is unbiased and `L^1`, while the actual branch-time vector on one maximal-left spine remains random and affects the estimator.

If

$$
\theta
=
\frac{K_{\mathrm{time}}}{C_{\mathcal D}},
$$

the additional condition is exactly

$$
\frac\theta2
\left(1-\sqrt{1-4a}\right)<1.
$$

For `theta <= 2` it is automatic under `4a<1`; for `theta > 2` it is equivalent to

$$
a<\frac{\theta-1}{\theta^2}.
$$

Do not replace this by an unjustified universal numerical strengthening.

### Current three-level hierarchy

- raw-faithful / identity: non-`L^1` for the fixed smooth datum;
- time-spine coarsening: `L^1` under the additional condition above, with genuine continuous branch-time randomness;
- complete interior averaging / C-prime: `L^1` under the full Catalan condition `4a<1`.

Complete averaging is therefore **not necessary** for integrability. The fixed-datum theorem proves only that some departure from the raw conditional barycenter is necessary.

## Status of Conjecture C

`docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture` because it asks for retained continuous interior randomness throughout the full C-prime regime `4a<1`.

It is now **proved on the stronger time-spine subregime** `4a<1` and `bC(a)<1`.

The remaining problem is quantitative: whether a nonconstant coarsening with genuine continuous interior randomness can be made `L^1` on the entire C-prime regime. Naive patchwise Gaussian-bridge coarsening is ruled out by the one-edge-patch observation.

## General conventions

- State theorem/proof status explicitly.
- Define project-specific symbols before use.
- Keep deterministic Duhamel identities, positive proposal randomization, intrinsic signed measures, raw-faithfulness, and coarsening distinct.
- Do not write ordinary conditional expectations of unresolved non-`L^1` objects.
- The manuscript should preserve the narrative: exactness is signed; probabilistic representation requires absolute moments; cancellation before absolute values is structural.
