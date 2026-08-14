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
   the semi-implicit iteration stays in the Hölder/ellipticity ball, contracts in `H^{-1}` with ratio at most `1/3`, converges to the unique small solution, and gives the implicit self-consistent diffusion representation.
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

The centered raw fluctuation is the only remaining obstruction between C-prime and conjecture C. Four routes are now settled enough to serve as the canonical map.

1. **Fixed pathwise Hölder / same-regularity Besov.** A raw centered Hessian edge has the expected sup-norm gain, but its pathwise same-regularity Hölder seminorm does not. The corresponding fixed Besov operator has the same high-frequency translation obstruction.
2. **Decreasing Banach scale.** `docs/entries/banach-scale-obstruction-for-raw-pde-patches.md`, status `proved here`, shows that the optimal time-integrated first-moment norm from `C^alpha` to `C^(alpha-delta)` costs order `1/delta`. If
   $$
   \delta_k=\alpha_{k-1}-\alpha_k>0,
   \qquad
   \sum_{k=1}^n\delta_k\leq\Delta,
   $$
   then every **stepwise first-moment Banach-scale proof** pays at least
   $$
   c^n\prod_{k=1}^n\delta_k^{-1}
   \geq
   c^n\left(\frac n\Delta\right)^n.
   $$
   Uniform loss is optimal; geometric and other nonuniform budgets are worse. Chronological ordering does not restore a hidden factorial gain.
3. **Condition all patch interiors.** Theorem C-prime proves absolute summability and an unbiased `L^1` estimator, but only after all continuous interior patch variables have been averaged out. This gives integrability without the full randomness required by C.
4. **Joint centered marks.** `docs/entries/joint-centered-mark-dichotomy-for-raw-pde-patches.md`, status `proved here`, forms several centered Gaussian marks before the first absolute moment and therefore genuinely lies outside the stepwise Banach-scale theorem. A two-mark block has a finite no-intermediate-loss estimate. At block length `m`, however, retaining all Gaussian marks gives the sharp uniform scale
   $$
   c_{\alpha,T}^m m!
   \leq
   \mathfrak R_m(\alpha,T)
   \leq
   C_{\alpha,T}^m m!.
   $$
   If the internal Gaussian bridge coordinates are signedly averaged first, a bare derivative chain collapses to an `He_{2m}` endpoint weight and the time-simplex coefficient becomes geometric; for full spatially varying patches the earlier commutator/cluster estimate gives the corresponding geometric bound. This favorable branch is only a **partially averaged estimator** because the bridge marks are no longer retained.

The joint-mark theorem really evades the `(n/Delta)^n` theorem rather than contradicting it: the latter assumes a first-moment Banach norm after every centered edge, while the joint block takes no such intermediate norm. The new factorial obstruction replaces the derivative-loss ladder.

Both sharp lower-bound mechanisms use depth-dependent high frequencies. The Banach-scale test has `N ~ exp(c/delta)`; the retained-block test has `N_m ~ sqrt(m/T) exp(m/alpha)`. Neither supplies one fixed smooth datum that realizes the worst-case norm at all generations. Therefore neither theorem disproves conjecture C.

## Canonical proved/open fork

**Condition or signedly average interior variables before the absolute value.** The deterministic/Hermite cancellations become strong enough to give geometric growth; C-prime proves the fully interior-averaged version in `L^1`, and the bridge-averaged joint-mark construction gives a partially averaged geometric variant.

**Retain the interior marks as genuinely random variables.** Fixed Hölder/Besov norms fail, the stepwise loss budget gives `(n/Delta)^n`, and all-order joint retained-mark blocks have factorial `m!` uniform growth.

The recurring tradeoff is therefore: every currently controlled route has either favorable absolute moments or full continuous interior randomness, but not both.

## Current strategic status of conjecture C

Conjecture C remains status `conjecture`. No proof or disproof has been audited.

The active next mathematical direction is now to test whether C itself is false rather than continuing only to search for another uniform first-moment proof architecture. Do not pre-empt that outcome in the wiki. A genuine disproof must overcome the generation-dependent-frequency caveat and tie non-`L^1` to one fixed smooth datum, or obtain a fixed-datum divergence argument by another mechanism.

If C is true, a proof must preserve structure discarded by all four settled routes: frequency together with genealogy, correlations between patches, a martingale/square-function mechanism, or cancellation across several centered marks that survives while those marks themselves remain random.

Never conflate finite signed exactness, deterministic convergence, the skeleton-only `L^1` representation, the Banach-scale proof barrier, the joint retained-mark factorial barrier, partial bridge averaging, and the full random-patch `L^1` conjecture.

## General conventions

- Public entries must state proof status explicitly and must not present heuristic, conjectural, or unaudited claims as theorems.
- Every proved-here entry must state its full hypotheses locally; cross-links may supply definitions and proofs of prerequisites, not missing assumptions.
- Define every piece of notation before use and keep terminology aligned with the cited PDE literature.
- Verify literature citations against primary sources when possible.
- Keep exact Duhamel/semigroup transfer distinct from importance-sampling randomization and from later patch resummation.
- Distinguish divergence-form Aronson--Nash estimates from nondivergence equations and their adjoints; ellipticity alone does not provide a universal adjoint `L^infty` estimate.
