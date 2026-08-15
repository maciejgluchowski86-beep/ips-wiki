# Proof spine — archived at BABP programme closure

## Original target

For one-dimensional BABP with branching parameter `lambda>0`, started from any finite nonempty particle set, prove local convergence to Bernoulli equilibrium of density

$$
q=\frac{\lambda}{1+\lambda}
$$

for every `lambda>0`.

Programme status: **closed at Group Meeting 006**. The all-parameter problem remains open. This file records the mathematical spine reached before closure so a future return does not rediscover it.

## E1. External stationary inputs

For every fixed `lambda>0`:

1. every weak limit point is stationary, by Jahnel--Köppl (2026), Theorem 2.5;
2. every stationary one-dimensional BABP law is a convex combination of the empty state and Bernoulli equilibrium, by Martinelli--Shapira--Toninelli (2025), Corollary 2.9, after `lambda=q/p` and constant time rescaling.

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

**Mathematical status:** verified as `BABP-EDGE-001`, audit `d1ef2ca`.

**Research-contribution status:** not a project result under the standing novelty standard. Sudbury (1999) already defines the same robust finite-window method for arbitrary `m`; Lemma 7 gives free window extension. The ten-site certificate is a correct larger-window instance of that method.

## E3. Corrector to finite-seed convergence

The project has a self-contained proof that the statewise condition in E2 implies local convergence from every finite nonempty deterministic initial set. It applies the same corrector to the two populations bordering internal vacant gaps and proves uniform local nonescape.

**Mathematical status:** verified as `BABP-CONV-001` after reviews `abb05f6` and `1aeb5a5`.

**Research-contribution status:** not a new theorem-level implication. Sudbury (1999), immediately before Theorem 7, states that the Neuhauser--Sudbury (1993) finite-seed argument relies on a suitable submartingale and proceeds unchanged once Section 3 extends its parameter range. The tagged-gap proof is retained as a useful self-contained proof, with no novelty claim for its architecture pending inspection of Neuhauser--Sudbury (1993), Section 5.

The concrete `lambda=1/40` convergence statement is mathematically valid but is not counted as a project result because its only new input is the larger-window instance in E2.

## E4. Infinite-front reduction

For fixed `lambda`, define

$$
v_k(\lambda)=\sup_\phi\min_{u,z}D_{k,\lambda}(u,z;\phi).
$$

Window nesting is exact: `v_{k+1}(lambda)>=v_k(lambda)`.

Student B's `003-front-gap.md`, commits `5c357ef` and `1365840`, establishes for research-branch use an infinite-front reduction. Let `Q_infinity` be the environment seen from the right edge and `I_lambda` its invariant laws. Cylinder functions form a core for the Feller generator. Finite LP duality plus compactness gives

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1).
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

**Status:** Professor-checked for proof-spine use; not independently audited or promoted as a stable theorem.

This is structurally different from merely increasing `k` and would be relevant if the programme is ever reopened because it converts the all-window question into an invariant-front question.

## E5. Physical front versus hostile invariant phases

Student B shows that every Cesaro invariant front law selected from the singleton has strictly positive current for every `lambda>0`, using the all-parameter linear cardinality growth theorem and reflection symmetry.

Thus the all-parameter finite-window route can fail only if `Q_infinity` has another invariant semi-infinite-tail law with smaller or nonpositive current.

Gap coordinates show a reversible coagulation/fragmentation bulk with iid geometric reference gaps and a driven moving-front boundary. At `lambda=0` there are many absorbing hard-core tails, so uniqueness at positive `lambda` cannot be inferred by continuity from zero.

A nearest-gap-only corrector cannot improve the old `1/3` obstruction; deeper correlations are necessary.

## Unresolved structural theorem at closure

The only remaining BABP target that would satisfy the standing novelty standard is a genuine structural statement about the full finite-window mechanism, for example:

- prove positive current for **every** invariant front law for every `lambda>0`, equivalently show the finite-window method reaches all positive parameters; or
- prove that such positivity fails below a genuine positive floor, establishing a structural limitation of the mechanism.

A sufficient but stronger statement for the positive direction is:

> **FRONT-UNIQUENESS.** The infinite right-front process has a unique invariant probability law for every fixed `lambda>0`.

No proof was found. The obvious reset coupling is circular because later left shifts can re-expose untouched tail information. The entropy/current idea requires a nontrivial no-incoming-flux theorem from particle-index infinity.

## Closure decision

The programme was closed rather than sent into another hostile-phase variant. After the principal's standing novelty ruling, the verified ten-site witness and convergence statement no longer count as project results. The remaining structural theorem is substantially harder and presently lacks a concrete proof mechanism.

Student A's reconnaissance ranks the residual positive-rates/noisy-East problem above this continuation because it has stronger group-specific leverage and a cheap finite two-site wall falsification test.

`students/student-b/assignment-004.md`, if present, is superseded and should not be executed.

## Reopen condition

Do not reopen BABP merely to increase `k`, sharpen a numerical threshold, or try another finite-window coordinate representation. A future return requires a genuinely new idea for the structural E4--E5 phase-selection problem or comparable all-parameter theorem.