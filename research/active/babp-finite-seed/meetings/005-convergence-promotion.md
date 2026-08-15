# Group meeting 005: promotion of finite-seed convergence theorem

Date: 2026-08-15

Professor review of the two independent correctness reviews:

- `audits/002-convergence-review-a.md`, commit `abb05f6`;
- `audits/002-convergence-review-b.md`, commit `1aeb5a5`.

state_narrowed: yes

Evidence pointer: the two reviews above, the repaired Professor proof `notes/professor-corrector-to-convergence-verification.md`, verified prerequisite `BABP-EDGE-001`, and the stable theorem note `research/results/babp-finite-seed-convergence.md`.

## Promotion decision

`BABP-CONV-001` is promoted from `claimed` to `verified` for mathematical use.

The theorem is:

> Fix `lambda>0`. If one-dimensional nearest-neighbour BABP admits a bounded finite-window right-edge corrector with a uniform statewise drift lower bound `D_{k,lambda}(u,z;phi)>=v>0` for every edge state `(u,z)`, then BABP started from every finite nonempty deterministic particle set converges locally to Bernoulli equilibrium of density `lambda/(1+lambda)`.

The registered hypothesis is the statewise corrector inequality. Bare liminf/limsup outer-edge velocity statements are not claimed to imply convergence.

Combining this theorem with verified `BABP-EDGE-001` proves finite-seed convergence at

$$
\lambda=\frac1{40}=0.025.
$$

Martinelli--Shapira--Toninelli (2025), Remark 5.4, records the previous finite-seed convergence range as `lambda>0.0347`, so the concrete verified corollary lies strictly below that recorded range.

No all-parameter theorem and no convergence rate is claimed.

## Independent-review reconciliation

Both fresh reviewers independently reconstructed the tagged-gap mechanism and passed the theorem. Review A identified two rigor points rather than theorem defects:

1. localize before applying Dynkin/optional stopping to the unbounded exponential test `exp(theta Z)`;
2. truncate the compensator sum to `|x|<=N` before passing to the infinite spatial sum by monotone convergence.

These are now part of the Professor proof and stable theorem note, rather than remaining reviewer comments.

Review B requested explicit convention matching when using Martinelli--Shapira--Toninelli. The stable proof now states the project generator and the exact scalar rescaling

$$
\lambda=q/p,
\qquad
L_{\mathrm{project}}=p^{-1}L_{\mathrm{MST}}.
$$

Thus there is no hidden parameter normalization in the stationary-law input.

## Stationary-limit theorem: direct source check

The convergence theorem no longer depends on an unverified reconstruction of Mountford (1993) or Ramírez--Varadhan (1996).

I independently checked Jahnel--Köppl (2026), Theorem 2.5. It states on `Z` that every weak limit point is stationary for IPS satisfying `(L1)` and `(R1)--(R3)` with `rho(r)=exp(-alpha r)` for some `alpha>0`, and explicitly does not require shift invariance or reversibility.

BABP satisfies the hypotheses directly in the present convention:

- use singleton update regions, so `(R1)` holds;
- each site flips at rate at most `2 max(1,lambda)`, so `(L1)` holds;
- for `rho(r)=exp(-alpha r)`, `(R2)` follows from the triangle inequality;
- changing a coordinate affects flip rates only at its two nearest neighbours, with uniformly bounded oscillation, so the influence kernel has finite range and `(R3)` holds for every `alpha>0`.

Therefore every weak subsequential limit of BABP is stationary for every fixed `lambda>0`. Mountford and Ramírez--Varadhan remain historical provenance only; their full hypotheses were not independently source-checked by Review B and are not needed in the verified proof.

Martinelli--Shapira--Toninelli (2025), Corollary 2.9, supplies the one-dimensional stationary-law classification after the explicit time-rescaling above.

## Scope and novelty boundary

The proof uses no initial-state assumption beyond deterministic, finite, and nonempty. It uses no connectedness, parity, minimum particle number, or 2025 particle-number growth estimate.

A targeted successor search through 2026-08-15 found no later theorem removing the `0.0347` finite-seed restriction. This supports the significance of the result, but publication-level closest-prior-work/novelty verification remains a separate pending task under `CHATGPT.md`. The registry therefore verifies the mathematics, not a priority claim such as “first proof”.

## E5 review and next bottleneck

Student B's commit `b9fdc55`, `students/student-b/002-edge-environment-dual.md`, gives a promising reduction of the finite-window problem to invariant laws of the infinite right-edge environment.

I checked the core algebra for proof-spine use:

- finite-window LP duality gives the worst stationary occupation measure of the controlled boundary-bit problem;
- the infinite front generator is the natural environment seen from the right edge;
- the compactness argument plausibly identifies `lim_k v_k(lambda)` with the worst invariant front drift;
- stationarity of the first bit gives

$$
\mu(u_1=1)
=rac{\lambda}{1+\lambda}
\left(1+\frac12\mu(u_1=0,u_2=1)\right),
$$

and therefore

$$
\lim_{k\to\infty}v_k(\lambda)
=rac{\lambda}{1+\lambda}
\left(\lambda-rac12\sup_{\mu\in\mathcal I_\lambda}\mu(01)\right).
$$

The safe all-parameter target is consequently the front-gap estimate

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda
\qquad\text{for every fixed }\lambda>0.
$$

One wording in `002-edge-environment-dual.md` should not yet be treated as established: an unconditional equivalence with the shorthand statement `lambda_k -> 0` requires care about the parameter dependence of the positivity sets `v_k(lambda)>0`. Monotonicity in the window size is proved, but monotonicity in `lambda` has not been proved. The next assignment should formulate the all-parameter objective directly as positive worst invariant front drift for every fixed `lambda`, avoiding this unnecessary threshold-parametrization issue.

## Direction decision

**continue.**

The programme now has a verified finite-seed convergence theorem at `lambda=1/40`. The next mathematical objective is the all-parameter extension through the infinite front process, while a second session begins a focused manuscript/novelty pass.

Graduate Student B resumes development on E5. Graduate Student A is reactivated for a bounded writeup and closest-prior-work task. These are the two in-flight sessions.

Assignments:

- `students/student-b/assignment-003.md`;
- `students/student-a/assignment-writeup-001.md`.

## Wiki-freeze recommendation

The protocol trigger has fired: the first central theorem of this programme entered independent audit. The principal has been notified and controls the freeze decision.

My recommendation is **keep the live-wiki freeze in force for now**. The verified theorem should first be stabilized as a focused research note/manuscript and receive a dedicated closest-prior-work audit. If the principal later lifts the freeze, a concise `proved here` update to the BABP out-of-equilibrium material would then be appropriate under the wiki quality rules. No wiki page should be changed automatically by this meeting.

## Stable-main promotion

The mathematical theorem and its verification record are now stable enough for selective promotion to `main`. I do not recommend merging the entire active branch or its exploratory workspace.

Promote only the stable surface:

- `research/claim-registry.md` with `BABP-EDGE-001` and `BABP-CONV-001` marked `verified` and audit pointers intact;
- `research/results/babp-finite-seed-convergence.md`, the repaired theorem proof;
- `project-state.md`, updated to record the verified result, current all-parameter bottleneck, and wiki-freeze recommendation.

The active student notes, exploratory LP/front calculations, meeting history, and failed routes remain on `research/babp-finite-seed` until they mature or the programme closes.