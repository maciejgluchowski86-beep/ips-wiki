# Project state

This file records the current state of the IPS wiki and the standalone PDE manuscript.

## Repository and manuscripts

There are two independent manuscript trees.

- `paper/`: facilitated-spin-system paper. The repository-level `main.tex` remains its Overleaf entry point. Do not edit it as part of the PDE track unless explicitly requested.
- `pde-paper/`: standalone manuscript **Cancellation before absolute values in branching representations with derivative weights**. Its entry point is `pde-paper/main.tex`.

The PDE manuscript is now a complete mathematical draft. It contains full proofs of every audited result included in the paper:

- repeated-Hessian coding-tree obstruction;
- Gevrey-1/2 necessity;
- NPP/HLOTW representation-level dichotomy;
- finite Hessian patch regrouping;
- auxiliary deterministic semi-implicit iteration;
- Theorem C-prime;
- fixed-datum raw-faithful obstruction;
- exact residual-signed-variation characterization;
- failure of naive patchwise Gaussian-bridge coarsening;
- target-uniform time-spine representation;
- sparse full-state retention at a fixed target.

There are no proof placeholders or TODO markers in `pde-paper/`. The deterministic self-consistent iteration remains auxiliary and should not be presented as a principal representation theorem.

Every principal theorem statement now carries its own load-bearing hypotheses and scope rather than inheriting them from surrounding prose. In particular:

- the coding-tree negative theorem states lifetime/mechanism positivity and does not assume uniform lower bounds;
- the representation dichotomy states the HLOTW positive-time lifetime-density extension inside the theorem;
- the deterministic theorem states its Schauder smallness condition and uniqueness class `|lambda v_xx| <= 1/8`;
- C-prime states `4a<1` and its fixed-point ball;
- the raw obstruction is explicitly for raw-faithful conditional-barycenter schemes, not all unbiased estimators;
- the residual characterization is exact for skeleton-preserving coarsenings when the skeleton label is retained, with cross-skeleton coarsening scoped separately;
- sparse full-state retention is explicitly pointwise/fixed-target and may depend on `(t,x)`;
- the time-spine theorem is one target-uniform geometric rule under `4a<1` and `b C(a)<1`.

The C-prime/deterministic overlap statement has the additional load-bearing assumption

$$
|\lambda z_*|\leq\frac18
$$

on the C-prime profile itself. The deterministic uniqueness theorem alone does not identify the two solutions without this assumption.

## Canonical PDE wiki entry point

- `docs/pde-branching-representations.md`

The overview now begins with the exact residual-variation identity and contains a dependency-ordered **shortest self-contained path to the capstone**. A reader with graduate probability and a first PDE course can follow that path without leaving the wiki.

The wiki is the durable mathematical record. Every `proved here` entry must state its hypotheses and scope locally.

## Self-containment pass

The final overview-to-capstone walk exposed and repaired several breaks.

1. **Signed-measure prerequisite.** Added
   `docs/entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md`, status `standard fact`, covering Jordan decomposition, Radon--Nikodym densities, total variation, pushforward contraction, finite-measure conditional expectation, conditional Jensen, proposal-invariant first moments, and nonatomic small-set divisibility.
2. **C-prime drift.** The C-prime page now states the exact fixed-point radius, the correct overlap assumptions with the deterministic theorem, and its position as constant coarsening after the capstone theorem.
3. **Conditional-expectation drift.** The random-field conditional-expectation page now points to residual signed variation rather than treating raw fluctuations as an unresolved binary fork.
4. **Joint-mark drift.** The joint centered-mark page now records the later fixed-datum obstruction, the one-edge bridge failure, and the final residual-variation interpretation.
5. **Finite-patch drift.** The finite regrouping and finite conditional-factorization pages no longer end with the obsolete statement that arbitrary retained marks are simply the unresolved conjecture. They point to C-prime, raw-faithful failure, time-spine success, and the exact characterization.
6. **Foundational notation.** Old `u`/`nu` transcription errors in the heat-reference, mild-formulation, and Duhamel-tree pages were removed.
7. **Navigation.** The new signed-measure prerequisite is in the PDE navigation and the heat-reference path is correct.

No missing analytic lemma was found in the quadratic-Hessian chain after these repairs. The Hölder/Hermite cancellation, Hessian Duhamel estimate, lacunary smoothness, disjoint-genealogy lower bound, Brownian confinement/heat-kernel positivity, and nonatomic small-set facts are all available inside the wiki at the level used downstream.

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

For a countable skeleton family with the skeleton label retained, the canonical coarsened estimator satisfies

$$
\mathbb E|Y|
=
\sum_\tau
\|(C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}.
$$

Thus summability of residual signed variation is **necessary and sufficient** for `L^1` in the coarsened conditional-barycenter class. Conditional Jensen proves necessity for any auxiliary estimator with the same coarsened conditional barycenter; the canonical Radon--Nikodym estimator attains equality.

If `C_1` is coarser than `C_2`, residual variation cannot increase. Identity gives full raw total variation; constant coarsening gives the absolute skeleton mass.

If the skeleton label itself is coarsened, the same invariant applies after enlarging the raw state to include the skeleton label, but the per-skeleton sum is no longer the correct formula.

## Counterintuitive consequences

The retained variable type is not the invariant.

1. There are explicit families for which identity retention has divergent variation, but a coarsening which retains the **entire Gaussian vector** on a small nonnull slab and collapses its complement has summable residual variation.
2. There are explicit families for which complete averaging is summable while retaining **only a one-dimensional time coordinate** leaves residual variation equal to one on every skeleton and therefore diverges.
3. At every fixed target `(t,x)` in the C-prime regime, nonatomicity of finite raw patch measures lets one retain the complete raw marked state on sets of summably small total-variation mass and collapse the complements. Hence the fixed-target existential problem for nonconstant retained randomness is closed.

Do not infer from item 3 that one target-uniform architecture has been constructed.

## Structured hierarchy

The known structured points fit the exact theorem with no inconsistency.

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
  then the residual variations are summable uniformly in the target.
- **C-prime / constant:** residual variation is `|F_tau(t,x)|`, summable throughout `4a<1`.

Naive patchwise Gaussian-bridge coarsening fails on the obstruction family because right combs consist entirely of one-edge maximal-left patches, so the one-edge bridge map generates the same retained sigma-field as identity.

## Status of Conjecture C

`docs/entries/l1-random-patch-conjecture-for-quadratic-hessian-pde.md` remains status `conjecture`, but its meaning is sharpened.

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
- The manuscript thesis is exact: **cancellation before absolute values is removal of signed variation by conditional averaging; `L^1` is summability of the variation which survives.**
