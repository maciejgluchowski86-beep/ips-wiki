# Programme state

## Direction

Title: 1D BABP from a finite seed

Branch: `research/babp-finite-seed`

Professor lineage: persistent ChatGPT Professor

Active graduate-student lineage: Graduate Student B

Second active session: Graduate Student A, writeup/closest-prior-work task

Workspace: `research/active/babp-finite-seed/`

Latest group meeting: `meetings/005-convergence-promotion.md`

## Target

For every `lambda>0`, prove that one-dimensional biased annihilating branching process started from a finite nonempty particle set converges locally to Bernoulli equilibrium of density

$$
q=\frac{\lambda}{1+\lambda}.
$$

The programme is committed.

## Verified results

### `BABP-EDGE-001`

At

$$
\lambda=\frac1{40},\qquad k=10,
$$

there is a bounded rational right-edge corrector with uniform statewise drift

$$
D_{10,1/40}(u,z;\phi)
\ge\frac{1033}{40000000}>0
$$

for all `2^11` edge states. Consequently, from every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t
\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

Verified by independent audit `d1ef2ca`.

### `BABP-CONV-001`

For fixed `lambda>0`, if some finite-window corrector satisfies

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for every edge state, then BABP started from every finite nonempty deterministic set converges locally to Bernoulli equilibrium.

The proof puts the same statewise corrector on the two populations bordering each internal vacant gap. The corrected gap width has negative drift; after localization, exponential tilting gives uniform lifetime and width tails. Poisson boundary displacement plus a finite-spatial-truncation compensator sum yields

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Jahnel--Köppl (2026), Theorem 2.5, applies directly to BABP and makes every weak limit point stationary. Martinelli--Shapira--Toninelli (2025), Corollary 2.9, after the explicit time rescaling `lambda=q/p`, classifies every stationary law as `alpha delta_empty+(1-alpha)pi_q`. The nonescape estimate forces `alpha=0`.

This theorem was independently accepted in:

- `audits/002-convergence-review-a.md`, commit `abb05f6`;
- `audits/002-convergence-review-b.md`, commit `1aeb5a5`.

Combining it with `BABP-EDGE-001` proves finite-seed convergence at

$$
\lambda=\frac1{40}=0.025,
$$

below the `0.0347` range recorded in Martinelli--Shapira--Toninelli (2025), Remark 5.4.

Stable proof: `research/results/babp-finite-seed-convergence.md`.

## Current bottleneck

The remaining scientific target is all `lambda>0`.

Student B's `students/student-b/002-edge-environment-dual.md`, commit `b9fdc55`, reduces the finite-window optimization to invariant laws of the infinite environment seen from the right edge. Its core proposed identity is

$$
\lim_{k\to\infty}v_k(\lambda)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12
\sup_{\mu\in\mathcal I_\lambda}\mu(u_1=0,u_2=1)\right).
$$

The safe next theorem target is therefore

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda
\qquad\text{for every fixed }\lambda>0.
$$

This front-process reduction is not yet an independently audited project theorem. The Professor checked its main algebra for proof-spine use. The note's shorthand equivalence with `lambda_k -> 0` should not be used without separately proving the relevant monotonicity in the parameter `lambda`; monotonicity in window size alone is known.

## Literature and novelty status

Martinelli--Shapira--Toninelli (2025), Remark 5.4, records finite-seed convergence down to `lambda>0.0347`. A targeted successor search through 2026-08-15 found no later theorem removing that restriction. Publication-level closest-prior-work/novelty audit remains pending and is part of Student A's writeup assignment.

## Current work

Graduate Student B: `students/student-b/assignment-003.md`, validate and attack the invariant-front/front-gap reduction for all parameters.

Graduate Student A: `students/student-a/assignment-writeup-001.md`, prepare a focused theorem note/manuscript skeleton and perform a source-specific closest-prior-work audit.

## Wiki freeze

The first central theorem has completed independent correctness audit, so the protocol trigger for principal review has fired. The principal controls whether the live-wiki freeze is lifted.

Professor recommendation: keep the wiki frozen until the focused manuscript and novelty audit are complete. No automatic wiki edit.

## Research delta

Latest meeting `state_narrowed`: yes

Evidence pointer: `audits/002-convergence-review-a.md`, `audits/002-convergence-review-b.md`, `notes/professor-corrector-to-convergence-verification.md`, `research/results/babp-finite-seed-convergence.md`, and `meetings/005-convergence-promotion.md`.

Consecutive no-narrowing meetings: 0

Stagnation consultation: none.

## Direction

`continue`.