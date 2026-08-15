# Proof spine

## Main target

For one-dimensional BABP with branching parameter `lambda>0`, started from any finite nonempty particle set, prove local convergence to Bernoulli equilibrium of density

$$
q=\frac{\lambda}{1+\lambda}
$$

for every `lambda>0`.

The finite-window submartingale mechanism is classical after full-text comparison with Sudbury (1999). The genuinely open target is the all-parameter extension.

## E1. External stationary inputs

For every fixed `lambda>0`:

1. every weak limit point is stationary, by Jahnel--Köppl (2026), Theorem 2.5, whose `(L1)` and `(R1)--(R3)` hypotheses hold for nearest-neighbour BABP;
2. every stationary one-dimensional BABP law is a convex combination of the empty state and Bernoulli equilibrium, by Martinelli--Shapira--Toninelli (2025), Corollary 2.9, after `lambda=q/p` and the constant rescaling `L_project=p^{-1}L_MST`.

**Status:** checked external inputs.

## E2. Finite-window robust edge corrector

For bounded `phi:{0,1}^k->R`, the corrected right edge has exact statewise drift `D_{k,lambda}(u,z;phi)`.

If

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for every edge word `u` and exterior bit `z`, then the right/left edges satisfy the audited ballistic liminf/limsup bounds.

At

$$
\lambda=\frac1{40},\qquad k=10,
$$

there is an exact rational certificate with

$$
\min_{u,z}D_{10,1/40}(u,z;\phi)
=\frac{1033}{40000000}>0.
$$

**Status:** verified project claim `BABP-EDGE-001`, audit `d1ef2ca`.

**Historical correction:** Sudbury (1999), Section 3, uses the same mechanism. After reflection, his `m`-block/end-value/correction/local gain are the project `k`/`u,z`/`phi`/`D`. His Lemma 5 is the robust all-end-value condition and Lemma 7 is window nesting. Table 2 reports the same `m=8`, `0.0347` problem by trial and error. Thus the mechanism and arbitrary-window formulation are prior art; the exact `k=10`, `lambda=1/40` certificate is the project contribution.

## E3. Corrector to finite-seed convergence

The project has a self-contained proof that the statewise condition in E2 implies local convergence from every finite nonempty deterministic initial set. It applies the same corrector to the two populations bordering internal vacant gaps and proves uniform local nonescape.

**Status:** mathematically verified as `BABP-CONV-001` after reviews `abb05f6` and `1aeb5a5`.

**Novelty correction:** the implication is classical. Sudbury (1999), immediately before Theorem 7, says the Neuhauser--Sudbury (1993) stationary-state argument relied on a suitable submartingale and proceeds unchanged once Section 3 extends its parameter range. The project proof is retained as a self-contained modern proof, not a new criterion. Novelty of the particular tagged-gap architecture is unresolved until Neuhauser--Sudbury (1993), Section 5, is inspected.

Concrete verified range extension:

$$
\lambda=\frac1{40}=0.025
$$

lies below Sudbury's published `0.0347` range.

## E4. Exact infinite-front reduction

For fixed `lambda`, define

$$
v_k(\lambda)=\sup_\phi\min_{u,z}D_{k,\lambda}(u,z;\phi).
$$

Window nesting is exact: `v_{k+1}(lambda)>=v_k(lambda)`.

Student B's `003-front-gap.md` validates the infinite-front reduction. Let `Q_infinity` be the environment seen from the right edge and `I_lambda` its invariant laws. Cylinder functions form a core for the Feller generator. Finite LP duality plus compactness gives

$$
\boxed{
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1).
}
$$

The first-bit stationary balance gives

$$
\mu(\lambda-u_1)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\mu(01)\right).
$$

Therefore existence of a positive finite-window corrector at fixed `lambda` is equivalent to

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda.
$$

**Status:** Professor-checked for proof-spine use; not yet independently audited as a stable project theorem.

No parameter-monotonicity statement is used.

## E5. Physical front versus hostile invariant phases

Student B proves that every Cesaro invariant front law selected from the singleton has strictly positive current for every `lambda>0`.

Indeed, Martinelli--Shapira--Toninelli's all-parameter linear cardinality growth and reflection symmetry give

$$
\liminf_{t\to\infty}\frac{\mathbf E R_t}{t}>0,
$$

and the front compensator identifies every singleton Cesaro limit `mu_phys` with

$$
\mu_{\rm phys}(\lambda-u_1)>0.
$$

Thus the all-parameter finite-window route can fail only if `Q_infinity` has another invariant semi-infinite-tail law with nonpositive or smaller current.

Gap coordinates show a reversible coagulation/fragmentation bulk with iid geometric reference gaps and a single driven boundary at the moving front. At `lambda=0` there are many absorbing hard-core tails, so uniqueness at positive `lambda` cannot be inferred by continuity from zero.

A one-gap corrector `R+h(g_1)` cannot beat `lambda>1/3`; deeper correlations are necessary.

**Status:** this is the current target-relevant reduction.

## Current first unresolved edge

Exclude hostile invariant semi-infinite-tail phases for every `lambda>0`.

A sufficient statement is:

> **FRONT-UNIQUENESS.** The infinite right-front process has a unique invariant probability law for every fixed `lambda>0`.

Uniqueness is stronger than necessary. It is enough to prove positive current for every invariant front law, or that every invariant law lies in the closed convex hull of the singleton-selected Cesaro limit set.

Promising directions currently visible:

- a coupling that controls re-entry of untouched tail information under later left shifts;
- an entropy/current argument in gap coordinates using reversible bulk and positive boundary affinity, with a proof that no compensating flux can arrive from particle-index infinity;
- finite-tail boundary truncations as a falsification/calibration tool for a possible hostile phase.

**Owner:** Graduate Student B, assignment `students/student-b/assignment-004.md`.

## Opportunity-cost checkpoint

The `lambda=1/40` result is a genuine exact range extension but not a new mechanism. BABP remains active for one further substantial hostile-phase block because E4--E5 sharply localize the all-parameter obstruction. If that block produces no theorem-level narrowing, explicitly compare continuation against the noisy-East reserve at the next group meeting.

## Publication/provenance side question

Obtain Neuhauser--Sudbury (1993), Section 5, if conveniently available. It is needed only to settle attribution of the project's tagged-gap proof architecture, not for the all-parameter proof spine.