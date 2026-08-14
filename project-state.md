# Project state

This file records the current state of the IPS wiki and the standalone PDE manuscript.

## Repository and manuscripts

There are two independent manuscript trees.

- `paper/`: facilitated-spin-system paper. The repository-level `main.tex` remains its Overleaf entry point. Do not edit it as part of the PDE track unless explicitly requested.
- `pde-paper/`: standalone manuscript **Cancellation before absolute values in branching representations with derivative weights**. Its entry point is `pde-paper/main.tex`.

The PDE manuscript is now a **complete mathematical draft** in the following precise sense: every theorem, proposition, lemma, and corollary included as a proved result has a proof in the source; there are no proof placeholders, TODO markers, or proof-sketch substitutes. The final subsection of `coarsening-hierarchy.tex` contains explicitly labeled open structural problems, not unfinished arguments.

A full current-source PDF compile was not independently reconstructed through the GitHub connector during the final audit. The newly inserted derivative-cluster subsection was compiled successfully in an isolated LaTeX smoke test. GitHub Actions builds the wiki, not the PDE PDF. Thus “complete mathematical draft” is a statement about proof/content completeness, not a claim that the exact current remote manuscript was end-to-end typeset in the audit environment.

## Section-by-section PDE status

1. `pde-paper/sections/introduction.tex` — complete exposition; no proof content deferred. Scope now distinguishes fixed-target coarsening statements from target-uniform architectures and identifies the time-only failure as an abstract signed-measure example.
2. `pde-paper/sections/preliminaries.tex` plus `sections/canonical-raw-measures.tex` — complete. Constructs the canonical raw measurable spaces and finite signed measures, proves fixed-tree `L^1`, the mass identity, and the tree/decorated-patch bijection.
3. `pde-paper/sections/coding-tree-obstructions.tex` — complete proofs of repeated-Hessian nonintegrability, the integrated derivative bound, and Gevrey-1/2 necessity.
4. `pde-paper/sections/representation-dichotomy.tex` — complete proof of the NPP/HLOTW benchmark, including the positive-time extension of the lifetime-density regularity used for the chosen HLOTW law.
5. `pde-paper/sections/quadratic-hessian-patches.tex` — complete proof of finite patch regrouping and the auxiliary deterministic semi-implicit iteration, including invariant ball, `H^{-1}` contraction, uniqueness, and the implicit diffusion formula.
6. `pde-paper/sections/skeleton-averaged-representation.tex` — complete proof of Theorem C-prime, Catalan absolute summability, fixed-point uniqueness in its stated ball, unbiased `L^1` skeleton sampling, and the deterministic-overlap corollary.
7. `pde-paper/sections/raw-faithful-obstruction.tex` — complete fixed-datum right-comb total-variation obstruction and proposal-invariance proof. Its signed comb measures are the canonical finite-tree measures restricted to the comb cylinders.
8. `pde-paper/sections/coarsening-hierarchy.tex` — complete proof of the residual-variation characterization, abstract coordinate-retention examples, sparse fixed-target retention, failure of naive patchwise Gaussian bridges, the explicit derivative-cluster bound, and the target-uniform time-spine representation corollary. The final “What remains open” subsection is intentionally open.

## Canonical raw signed measures

For `g=phi'' in C^alpha(T)`, `0<alpha<1`, every fixed finite planar full binary tree `tau` has a recursively defined standard-Borel raw space `Omega_tau`, finite positive reference measure `nu_tau`, and canonical centered raw density `R_tau^{t,x}`. The strict-loss `L^1`-valued Holder estimate

$$
\|K_rH\|_{\mathcal H^\beta}
\leq
C r^{-1+(\eta-\beta)/2}
\|H\|_{\mathcal H^\eta},
\qquad 0<\beta<\eta<1,
$$

is integrable in the edge duration and gives, for every fixed tree,

$$
\|\mu_\tau^{t,x}\|_{TV}<\infty.
$$

The measure is genuinely countably additive and satisfies

$$
\boxed{
\mu_\tau^{t,x}(\Omega_\tau)=F_\tau(t,x).
}
$$

No smallness condition is used at fixed depth. The correct interpretation of the Banach-scale `(cn/Delta)^n` lower bound is that the finite-depth constants in a stepwise first-moment Holder proof cannot remain geometric as depth grows; it is not fixed-depth nonintegrability.

A decorated maximal-left-patch skeleton records both each patch length and the ordered side-subtree attachment slots. With this definition it is in bijection with the original planar binary tree and simply reindexes the same `Omega_tau`, `nu_tau`, and `mu_tau^{t,x}`.

## Derivative clusters and the absolute-time patch bound

The previous compressed proof of `K_time<infinity` has been replaced by an explicit cluster expansion. For

$$
H_\alpha=(\mathbb E|Z|^{2\alpha})^{1/2},
\qquad
D_{\alpha,T}=\frac{2T^{\alpha/2}}{\alpha},
\qquad
A_{\alpha,T}=H_\alpha D_{\alpha,T},
$$

one obtains, for every patch length `m`,

$$
\boxed{
\mathfrak P_m(\alpha,T)
\leq
2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}.
}
$$

The proof uses only the established Hermite Holder estimate and multiplication commutator. With derivative gaps

$$
r_j=s_{j+1}-s_j,
\qquad s_{m+1}=t,
$$

the map from branch times to `r_1,...,r_m` has unit Jacobian and `s_1=t-sum r_j`; there is no extra initial-time integration factor. Expanding

$$
K_R^{(k)}M_B
=
M_BK_R^{(k)}+[K_R^{(k)},M_B]
$$

produces exactly

$$
2\binom{m-1}{q-1}
$$

terms with `q` consecutive derivative clusters. A cluster of length `ell` has integrated factor

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2}
\leq
H_\alpha4^\ell R^{-1+\alpha/2}.
$$

Consequently

$$
K_{\mathrm{time}}(\alpha,T)
\leq
K_{\mathrm{cl}}(\alpha,T)
:=
4\max\{1+A_{\alpha,T},2A_{\alpha,T}\}
<\infty.
$$

This analytic proposition has **no smallness assumption**. Smallness enters only in the immediately following target-uniform time-spine representation corollary through

$$
4a<1,
\qquad
bC(a)<1,
$$

where

$$
a=|\lambda|C_{\mathcal D}M,
\qquad
b=|\lambda|K_{\mathrm{time}}M.
$$

Do not merge these two logical statements.

## Exact coarsening characterization and scope

For a fixed target, if

$$
\mu_\tau=R_\tau\nu_\tau
$$

and `C_tau` is a skeleton-preserving coarsening, then

$$
\boxed{
\|(C_\tau)_\#\mu_\tau\|_{TV}
=
\int
\left|
\mathbb E_{\nu_\tau}
[R_\tau\mid\sigma(C_\tau)]
\right|d\nu_\tau.
}
$$

With the skeleton label retained, summability of these residual variations is necessary and sufficient for `L^1` in the associated conditional-barycenter class. This is pointwise in `(t,x)` for the quadratic-Hessian application.

Permanent scope distinctions:

- Sparse full-state retention is a **fixed-target** construction and may depend on `(t,x)`. It proves that the complete raw coordinates remain observable on small nonnull pieces; it does not prove that every retained coordinate changes the estimator value.
- The time-spine rule is a **target-uniform architecture** under its additional smallness condition.
- The examples in which the whole Gaussian vector can survive on small pieces and in which retaining only a time coordinate fails are **abstract signed-measure examples**. The time-only example is not a quadratic-Hessian counterexample.
- If the skeleton label itself is coarsened, the one-measure residual-variation identity still applies on the enlarged state, but the separate per-skeleton sum need not be the invariant.

## Main proved quadratic-Hessian hierarchy

Let

$$
M=\|P_\cdot\phi''\|_{X_{\alpha,T}},
\qquad
 a=|\lambda|C_{\mathcal D}(\alpha,T)M.
$$

- **Raw-faithful / identity:** for one fixed arbitrarily small smooth datum, a right-comb subseries of canonical raw total variations diverges.
- **Time-spine:** under `4a<1` and `b C(a)<1`, one fixed geometric rule retains the root-spine branch-time vector and has summable residual variation uniformly over targets.
- **C-prime / constant:** under `4a<1`, complete interior averaging gives an absolutely summable skeleton expansion and an unbiased `L^1` estimator.
- **Sparse full-state:** at each fixed target in the C-prime regime, there are nonconstant coarsenings retaining the complete raw state on summably small nonnull pieces.

## Remaining open problems

These are genuine open directions, not manuscript gaps:

1. a non-sparse geometrically defined coarsening throughout the full C-prime regime;
2. a target-uniform structured representation on that full regime with quantitative function-space control;
3. optimization of residual variation under information or computational constraints;
4. natural/global Gaussian coarsenings beyond the failed patchwise bridge map;
5. cross-skeleton coarsenings in which the skeleton label itself is also averaged.

## General conventions

- Keep signed exactness, positive proposal randomization, intrinsic signed measures, coarsening, and conditional-barycenter requirements distinct.
- Do not define unresolved non-`L^1` objects by ordinary conditional expectation.
- Keep fixed-target existence statements separate from target-uniform architecture statements.
- The manuscript thesis is: **cancellation before absolute values is removal of signed variation by conditional averaging; `L^1` is summability of the variation which survives.**
