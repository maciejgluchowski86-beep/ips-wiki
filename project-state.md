# Project state

This file records the current state of the IPS wiki and the standalone PDE manuscript.

## Repository and manuscripts

There are two independent manuscript trees.

- `paper/`: facilitated-spin-system paper. The repository-level `main.tex` remains its Overleaf entry point. Do not edit it as part of the PDE track unless explicitly requested.
- `pde-paper/`: standalone manuscript **Cancellation before absolute values in branching representations with derivative weights**. Its entry point is `pde-paper/main.tex`.

The PDE manuscript contains full proofs of the audited coding-tree obstruction, Gevrey-1/2 necessity, representation-level dichotomy, finite Hessian patch regrouping, auxiliary deterministic iteration, Theorem C-prime, fixed-datum raw-faithful obstruction, time-spine coarsening theorem, and the exact residual-signed-variation characterization.

The deterministic self-consistent iteration remains auxiliary.

## Canonical PDE wiki entry point

- `docs/pde-branching-representations.md`

The wiki is the durable mathematical record. Every `proved here` entry must state its hypotheses and scope locally.

## Coding-tree chain

The following are `proved here`:

- `docs/entries/repeated-hessian-obstruction-for-coding-trees.md`
- `docs/entries/finite-directional-radius-obstruction.md`
- `docs/entries/gevrey-half-necessity-for-coding-trees.md`
- `docs/entries/representation-level-dichotomy.md`

The repeated-Hessian genealogy gives a lower bound of order `c^m D_m/m!`; lifetime and mechanism proposal factors cancel. Integrability forces a Gevrey-1/2 directional jet. On the benchmark

$$
\partial_tu+\frac12u_{xx}+\eta(e^{(u_x)^4}-1)=0,
$$

the raw NPP functional is non-`L^1` at every positive horizon while an explicit HLOTW estimator is `L^2` for short time. This is Act I: exactness does not determine absolute integrability.

## Quadratic Hessian chain

For

$$
\partial_tv
=
\frac12v_{xx}+\lambda(v_{xx})^2,
\qquad
z=v_{xx},
$$

finite Picard trees regroup exactly into maximal left-child patches.

Let

$$
X_{\alpha,T}=C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
\qquad
M=\|P_\cdot\phi''\|_X,
\qquad
 a=|\lambda|C_{\mathcal D}(\alpha,T)M.
$$

If

$$
4a<1,
$$

Theorem C-prime gives absolute summability of the deterministic interior-averaged skeleton profiles and an unbiased skeleton-only `L^1` estimator.

The fixed-datum raw-faithful obstruction uses right-oriented combs and the smooth lacunary Hessian datum

$$
g_\varepsilon(x)
=
\varepsilon\left[
\cos x+
\sum_{m\ge m_0}(m!)^{-1/2}\cos(K^mx)
\right].
$$

The length-`m` comb has total variation at least

$$
\varepsilon(C|\lambda|\varepsilon)^m
\frac{m^m}{\sqrt{m!}},
$$

so every estimator retaining the canonical raw conditional barycenter has infinite first moment. The datum can be scaled into the C-prime regime.

## Exact coarsening characterization

`docs/entries/residual-signed-variation-characterization-for-coarsened-patches.md` is `proved here` and is the capstone theorem.

For one skeleton, write

$$
\mu_\tau=R_\tau\nu_\tau
$$

with `nu_tau` finite positive. For a skeleton-preserving coarsening `C_tau`,

$$
\boxed{
\|(C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}
=
\int
\left|
\mathbb E_{\nu_\tau}
[R_\tau\mid\sigma(C_\tau)]
\right|d\nu_\tau.
}
$$

This residual signed variation is intrinsic; the conditional-expectation formula is only a representation of the total variation of the pushforward signed measure.

For a countable skeleton family, the canonical coarsened estimator satisfies

$$
\mathbb E|Y|
=
\sum_\tau
\|(C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}.
$$

Thus summability of residual signed variation is **necessary and sufficient** for `L^1` in the coarsened conditional-barycenter class. Conditional Jensen proves necessity for any auxiliary estimator with the same coarsened conditional barycenter; the canonical Radon--Nikodym estimator attains equality.

If `C_1` is coarser than `C_2`, residual variation cannot increase. Identity gives full raw total variation; constant coarsening gives the absolute skeleton mass.

The theorem is exact for the manuscript's skeleton-preserving class. If the skeleton label itself is coarsened, the same invariant applies after the enlarged pushforward, but the per-skeleton sum is no longer the correct formula.

## Counterintuitive consequences

The retained variable type is not the invariant.

1. There are explicit families for which identity retention has divergent variation, but a coarsening which retains the **entire Gaussian vector** on a small nonnull slab and collapses its complement has summable residual variation.
2. There are explicit families for which complete averaging is summable while retaining **only a one-dimensional time coordinate** leaves residual variation equal to one on every skeleton and therefore diverges.
3. At every fixed target `(t,x)` in the C-prime regime, nonatomicity of finite raw patch measures lets one retain the complete raw marked state on sets of summably small total-variation mass and collapse the complements. Hence the fixed-target existential problem for nonconstant retained randomness is closed.

Do not infer from item 3 that one target-uniform architecture has been constructed.

## Structured hierarchy as a sanity check

The previous three points fit the exact theorem with no inconsistency.

- **Raw-faithful / identity:** residual variation is the full raw total variation; the fixed-datum right-comb subseries diverges.
- **Time-spine:** retain the actual branch times on one root maximal-left patch and average all other continuous variables. If
  $$
  4a<1,
  \qquad
  bC(a)<1,
  $$
  with
  $$
  b=|\lambda|K_{\mathrm{time}}M,
  \qquad
  C(a)=\frac{1-\sqrt{1-4a}}{2a},
  $$
  then the residual variations are summable.
- **C-prime / constant:** residual variation is `|F_tau(t,x)|`, summable throughout `4a<1`.

Naive patchwise Gaussian-bridge coarsening fails on the obstruction family because right combs consist entirely of one-edge maximal-left patches, so the one-edge bridge map generates the same retained sigma-field as identity.

## Status of Conjecture C

`docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture`, but its meaning is now sharpened.

The **fixed-target existential relaxation** is solved affirmatively throughout the full C-prime regime by sparse full-state retention. The remaining conjecture asks for one structured, target-uniform coarsening architecture with nondecorative continuous retained information and quantitative `L^1` control for every `(t,x)` in the full C-prime regime.

The time-spine theorem proves such a structured architecture on its stronger small-data subregime.

## Remaining structural problems

- non-sparse full-regime coarsenings with a fixed geometric description;
- target-uniform function-space control;
- optimization of residual variation under information/computational constraints;
- more global Gaussian coarsenings beyond the failed patchwise bridge map;
- cross-skeleton coarsening.

## General conventions

- Keep signed exactness, positive proposal randomization, intrinsic signed measures, coarsening, and conditional-barycenter requirements distinct.
- Do not define unresolved non-`L^1` objects by ordinary conditional expectation.
- The manuscript thesis is now exact: **cancellation before absolute values is removal of signed variation by conditional averaging; `L^1` is summability of the variation which survives.**
