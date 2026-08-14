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
- canonical finite-tree raw signed measures and their mass identity;
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
- the canonical raw-measure theorem assumes exactly `phi'' in C^alpha`, `0<alpha<1`, for each fixed finite tree and no smallness condition;
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

The overview begins with the exact residual-variation identity and contains a dependency-ordered **shortest self-contained path to the capstone**. A reader with graduate probability and a first PDE course can follow that path without leaving the wiki.

The wiki is the durable mathematical record. Every `proved here` entry must state its hypotheses and scope locally.

## Hostile-referee repair: canonical raw signed measures

The load-bearing objection that `mu_tau^{t,x}` had previously been asserted rather than constructed is repaired.

The durable proved-here entry is

- `docs/entries/canonical-raw-signed-measures-for-finite-quadratic-hessian-trees.md`.

For `g=phi'' in C^alpha(T)`, `0<alpha<1`, and every fixed finite planar full binary tree `tau`, the raw mark space is defined recursively by

$$
\Omega_\bullet=\mathbb R,
\qquad
\Omega_{[\tau_1,\tau_2]}
=[0,T]\times\mathbb R\times\Omega_{\tau_1}\times\Omega_{\tau_2},
$$

with product Borel sigma-field and finite positive reference measure

$$
\nu_\bullet=\gamma,
\qquad
\nu_{[\tau_1,\tau_2]}
=ds\otimes\gamma\otimes\nu_{\tau_1}\otimes\nu_{\tau_2}.
$$

The canonical centered raw density is defined recursively using the same descendant marks in the shifted and unshifted terms. An `L^1`-valued Holder estimate with any strict loss `beta<eta` gives the one-edge bound

$$
\|K_rH\|_{\mathcal H^\beta}
\leq
C r^{-1+(\eta-\beta)/2}
\|H\|_{\mathcal H^\eta}.
$$

The time singularity is integrable. Induction on the fixed finite tree therefore proves

$$
\|\mu_\tau^{t,x}\|_{TV}<\infty.
$$

Because the raw density is `L^1` with respect to a finite positive measure, `mu_tau^{t,x}` is a genuine countably additive finite signed measure. Absolute integrability permits Fubini, and induction plus the centered Gaussian Hessian identity proves the mass identity

$$
\boxed{
\mu_\tau^{t,x}(\Omega_\tau)=F_\tau(t,x).
}
$$

No smallness condition is needed. No derivative of `phi''` beyond positive Holder regularity is used.

This finite-depth theorem is fully compatible with the Banach-scale lower bound. The correct reading of the `(cn/Delta)^n` result is: **finite `L^1` constants exist at every fixed finite depth, but a stepwise first-moment Holder-scale proof cannot keep them geometric as depth grows.** It is not a fixed-depth nonintegrability theorem.

The referee also identified an ambiguity in “decorated maximal-left-patch skeleton.” Lengths alone are insufficient. Throughout the PDE track, a decorated skeleton now records both each maximal-left-chain length and the ordered side-subtree attachment slots along that chain. With this definition there is an explicit bijection

$$
\tau
\longleftrightarrow
(m;\sigma_1,\ldots,\sigma_m)
$$

recursively between finite planar full binary trees and decorated patch skeletons. Tree indexing and decorated-skeleton indexing therefore refer to the same `Omega_tau`, `nu_tau`, and `mu_tau^{t,x}`.

No upstream theorem was weakened by this repair:

- C-prime, time-spine, and sparse retention already assume `phi in C^{2+alpha}`, hence `phi'' in C^alpha`;
- the raw-faithful obstruction uses one `C^infty` datum, and its comb measure is the restriction of the canonical right-comb measure to the chosen duration cylinder;
- the residual-variation theorem was already abstractly exact for arbitrary finite signed measures; the new theorem supplies the previously missing concrete finite measures.

## Self-containment pass

The final overview-to-capstone walk exposed and repaired several breaks.

1. **Signed-measure prerequisite.** Added
   `docs/entries/finite-signed-measures-pushforwards-and-conditional-barycenters.md`, status `standard fact`, covering Jordan decomposition, Radon--Nikodym densities, total variation, pushforward contraction, finite-measure conditional expectation, conditional Jensen, proposal-invariant first moments, and nonatomic small-set divisibility.
2. **Canonical raw measures.** Added the fixed-tree construction above, including measurable spaces, finite total variation, mass identity, and the precise tree/decorated-skeleton bijection.
3. **C-prime drift.** The C-prime page states the exact fixed-point radius, the correct overlap assumptions with the deterministic theorem, and its position as constant coarsening after the capstone theorem.
4. **Conditional-expectation drift.** The random-field conditional-expectation page points to residual signed variation rather than treating raw fluctuations as an unresolved binary fork.
5. **Joint-mark drift.** The joint centered-mark page records the later fixed-datum obstruction, the one-edge bridge failure, and the final residual-variation interpretation.
6. **Finite-patch drift.** The finite regrouping page now defines the full decorated patch data needed for the bijection and points to the canonical raw-measure theorem; the finite conditional-factorization page points to C-prime, raw-faithful failure, time-spine success, and the exact characterization.
7. **Foundational notation.** Old `u`/`nu` transcription errors in the heat-reference, mild-formulation, and Duhamel-tree pages were removed.
8. **Navigation.** The signed-measure and canonical raw-measure prerequisites are both in the PDE navigation and the shortest reading path.

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

finite Picard trees regroup exactly into maximal left-child patches. Every fixed finite tree also carries the canonical finite raw signed measure constructed above.

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
