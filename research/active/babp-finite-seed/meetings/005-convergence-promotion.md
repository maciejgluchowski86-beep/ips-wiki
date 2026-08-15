# Group meeting 005: promotion of finite-seed convergence theorem

Date: 2026-08-15

Professor review of the two independent correctness reviews:

- `audits/002-convergence-review-a.md`, commit `abb05f6`;
- `audits/002-convergence-review-b.md`, commit `1aeb5a5`.

state_narrowed: yes

Evidence pointer: the two reviews above, repaired Professor proof `notes/professor-corrector-to-convergence-verification.md`, verified prerequisite `BABP-EDGE-001`, and stable theorem note `research/results/babp-finite-seed-convergence.md`.

## Promotion decision

`BABP-CONV-001` is promoted from `claimed` to `verified` for mathematical use.

The verified theorem is:

> Fix `lambda>0`. If one-dimensional nearest-neighbour BABP admits a bounded finite-window right-edge corrector with uniform statewise drift `D_{k,lambda}(u,z;phi)>=v>0` for every edge state `(u,z)`, then BABP started from every finite nonempty deterministic particle set converges locally to Bernoulli equilibrium of density `lambda/(1+lambda)`.

The hypothesis is the statewise corrector inequality. Bare liminf/limsup outer-edge velocity statements are not claimed to imply convergence.

Combining this theorem with verified `BABP-EDGE-001` proves finite-seed convergence at

$$
\lambda=\frac1{40}=0.025.
$$

Martinelli--Shapira--Toninelli (2025), Remark 5.4, records the previous finite-seed convergence range as `lambda>0.0347`, so the verified corollary lies strictly below that recorded range. No all-parameter theorem and no convergence rate is claimed.

## Independent-review reconciliation

Both fresh reviewers independently reconstructed the tagged-gap mechanism and passed the theorem. Review A identified two rigor points rather than theorem defects:

1. localize before applying Dynkin/optional stopping to the unbounded exponential test `exp(theta Z)`;
2. truncate the nucleation compensator to `|x|<=N` before passing to the infinite spatial sum by monotone convergence.

Both repairs are now incorporated in the Professor proof and stable theorem note.

Review B requested explicit convention matching when using Martinelli--Shapira--Toninelli. The stable proof states

$$
\lambda=\frac qp,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
$$

Thus no parameter normalization is hidden in the stationary-law citation.

## Stationary-limit theorem: direct source check

The convergence theorem no longer depends on unverified reconstructions of Mountford (1993) or Ramírez--Varadhan (1996).

Jahnel--Köppl (2026), Theorem 2.5, was checked directly. On `Z` it makes every weak limit point stationary under `(L1)` and `(R1)--(R3)` with an exponential influence profile. BABP satisfies the hypotheses in the present convention:

- use singleton update regions, giving bounded update diameter `(R1)`;
- each site flips at rate at most `2 max(1,lambda)`, giving `(L1)`;
- for `rho(r)=exp(-alpha r)`, `(R2)` follows from the triangle inequality;
- changing one coordinate affects flip rates only at its two nearest neighbours, with bounded oscillation, so `(R3)` holds.

The theorem does not require shift invariance or reversibility. Mountford and Ramírez--Varadhan remain historical provenance only.

Martinelli--Shapira--Toninelli (2025), Corollary 2.9, supplies the one-dimensional stationary-law classification after the explicit time rescaling above.

## Scope and novelty boundary

The proof uses no initial-state assumption beyond deterministic, finite, and nonempty. It uses no connectedness, parity, minimum particle number, or 2025 particle-number growth theorem.

A targeted successor search through 2026-08-15 found no later theorem removing the `0.0347` restriction. This supports significance, but publication-level closest-prior-work/priority verification remains pending. `verified` records mathematical correctness, not a claim such as “first proof”.

## E5 review and next bottleneck

Student B's commit `b9fdc55`, `students/student-b/002-edge-environment-dual.md`, gives a promising reduction of the finite-window problem to invariant laws of the infinite right-edge environment. The Professor checked the core algebra for proof-spine use.

For fixed `lambda`, the proposed identities are

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}
\int(\lambda-u_1)\,d\mu,
$$

and, from stationarity of the first bit,

$$
\mu(u_1=1)
=
\frac{\lambda}{1+\lambda}
\left(1+\frac12\mu(u_1=0,u_2=1)\right).
$$

Hence the proposed front reduction is

$$
\lim_{k\to\infty}v_k(\lambda)
=
\frac{\lambda}{1+\lambda}
\left(
\lambda-
\frac12\sup_{\mu\in\mathcal I_\lambda}\mu(01)
\right).
$$

The safe all-parameter target is therefore

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda
\qquad\text{for every fixed }\lambda>0.
$$

The infinite-front reduction is not yet independently audited. Also, an unconditional equivalence with the shorthand statement `lambda_k -> 0` requires care: window monotonicity is proved, but monotonicity/interval structure in the parameter `lambda` has not been proved. The next assignment works directly at each fixed `lambda`.

## Direction decision

**continue.**

The programme now has a verified finite-seed convergence theorem at `lambda=1/40`. Graduate Student B resumes on the all-parameter front problem. Graduate Student A is reactivated for a focused writeup and closest-prior-work audit. These are the two in-flight sessions.

Assignments:

- `students/student-b/assignment-003.md`;
- `students/student-a/assignment-writeup-001.md`.

## Wiki-freeze recommendation

The protocol trigger has fired: the first central theorem of this programme entered independent audit. The principal has been notified and controls the freeze decision.

Professor recommendation: **keep the live-wiki freeze in force for now**. Stabilize the focused manuscript and complete the closest-prior-work audit before considering a `proved here` BABP wiki update. No wiki page is changed by this meeting.

## Stable-main promotion

The theorem is stable enough for selective promotion to `main`; the exploratory research branch is not.

Promoted:

- `research/claim-registry.md`, with `BABP-EDGE-001` and `BABP-CONV-001` verified and audit commit pointers intact; main commit `f3df405ea87f2a1ca74eee1e18902a2ac4d3265e`;
- `research/results/babp-finite-seed-convergence.md`, repaired stable proof; main commit `a9dae6f2d22a721a83f726192619715a5886bb48`;
- `project-state.md`, recording the verified theorem, all-parameter bottleneck, and wiki-freeze recommendation; main commit `cb7f084728eefc7d8da91858731a3d87c663d4d0`.

The active student notes, exploratory LP/front calculations, meeting history, and failed routes remain on `research/babp-finite-seed`.