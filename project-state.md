# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Research architecture

The group has one persistent ChatGPT Professor directing persistent graduate-student sessions. At most two sessions are in flight at once. The Professor owns scientific direction, proof spines, audits, opportunity-cost judgments, and closure decisions.

The repository is canonical technical memory. Conversation links are optional only; successor sessions must rely on repository handovers and exact transcript transfer when necessary.

## Active scientific direction

**1D BABP from a finite seed — committed programme.**

- Research branch: `research/babp-finite-seed`
- Workspace: `research/active/babp-finite-seed/`
- Main target: prove finite-seed local convergence for every `lambda>0`.
- Verified theorem `BABP-CONV-001`: for any fixed `lambda>0`, a bounded finite-window edge corrector with uniform statewise positive drift implies local convergence from every finite nonempty deterministic initial particle set to Bernoulli equilibrium.
- Verified certificate `BABP-EDGE-001`: at `lambda=1/40`, `k=10`, the minimum statewise drift is exactly `1033/40000000>0`.
- Verified concrete consequence: at `lambda=1/40=0.025`, BABP from every finite nonempty deterministic seed converges locally to Bernoulli equilibrium of density `1/41`.
- Martinelli--Shapira--Toninelli (2025), Remark 5.4, records the previous finite-seed convergence range as `lambda>0.0347`.
- The convergence theorem was independently accepted in commits `abb05f6` and `1aeb5a5`; the edge certificate was independently audited in `d1ef2ca`.
- Stable theorem proof: `research/results/babp-finite-seed-convergence.md`.
- Latest group meeting: `research/active/babp-finite-seed/meetings/005-convergence-promotion.md`, `state_narrowed: yes`.

## Verified theorem mechanism

Use particle variables with rates

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x.
$$

The theorem hypothesis is the statewise finite-window corrector inequality

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for every edge state. It is stronger than the resulting outer-edge liminf/limsup ballistic bounds.

Applied to the two populations bordering an internal vacant gap, the same corrector gives a corrected gap width with uniformly negative drift. Positive gaps are born at width one, do not split, and distinct positive gaps cannot merge. After localization, exponential tilting gives uniform lifetime and maximum-width tails. Poisson boundary displacement and a compensator sum, first truncated to a finite spatial region and then passed to the limit by monotone convergence, give

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Jahnel--Köppl (2026), Theorem 2.5, applies directly: BABP has bounded single-site rates and nearest-neighbour influence, so every weak limit point is stationary. Martinelli--Shapira--Toninelli (2025), Corollary 2.9, after the explicit rescaling `lambda=q/p`, `L_project=p^{-1}L_MST`, classifies stationary laws as

$$
\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

The empty-window estimate forces `alpha=0`. The 2025 particle-number growth theorem is not used.

## Current proof-spine bottleneck

The remaining target is all `lambda>0`.

Student B's commit `b9fdc55`, `research/active/babp-finite-seed/students/student-b/002-edge-environment-dual.md`, proposes an exact infinite-front interpretation of the finite-window LP. For fixed `lambda`, let `I_lambda` be the invariant laws of the environment seen from the right edge. The proposed reduction is

$$
\lim_{k\to\infty}v_k(\lambda)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\sup_{\mu\in\mathcal I_\lambda}\mu(01)\right).
$$

The safe next mathematical target is the **front-gap lemma**

$$
\sup_{\mu\in\mathcal I_\lambda}\mu(01)<2\lambda
\qquad\text{for every fixed }\lambda>0.
$$

The front reduction is currently a research claim, not an independently audited theorem. Monotonicity in window size is proved; parameter monotonicity in `lambda` is not, so shorthand equivalence with `lambda_k -> 0` should not be used without an additional argument.

## Current work

- Graduate Student B: validate and attack the invariant-front/front-gap reduction, assignment `students/student-b/assignment-003.md`.
- Graduate Student A: focused writeup plus closest-prior-work/successor audit, assignment `students/student-a/assignment-writeup-001.md`.

Publication-level novelty checking remains pending. A targeted successor search through 2026-08-15 found no later theorem removing the `0.0347` restriction, but the verified status refers to mathematical correctness, not a priority claim.

## Wiki-freeze review

The protocol trigger has fired because the programme's first central theorem entered independent audit. The principal controls whether the live-wiki freeze is lifted.

Professor recommendation: **keep the wiki frozen for now**. Stabilize the focused manuscript and complete the closest-prior-work audit first. If the principal later lifts the freeze, a concise `proved here` BABP update can be considered under the wiki quality rules.

## Main promotion

The following stable surface has been promoted to `main`:

- `research/claim-registry.md` with `BABP-EDGE-001` and `BABP-CONV-001` verified;
- `research/results/babp-finite-seed-convergence.md`;
- this `project-state.md`.

The exploratory active workspace, student calculations, meeting history, and unresolved front-process work remain on `research/babp-finite-seed`.

## Most recently closed programme

**1D hard FA-1f from a finite seed** was closed at Group Meeting 002 on expected-value grounds. The broader problem remains open. The two project mechanisms closed there were the centered positive transform and the unnormalized patch-transfer route; both reduced to the same conservative dynamics.

The principal also supplied prior negative tractability evidence from extensive earlier ChatGPT work on 1D FA-1f off-equilibrium convergence. Cancellation/duality is not a preferred or required organizing mechanism.

## Closed programmes and routes

Closed programmes not to be retried by renaming:

- quadratic-Hessian;
- Fresnel integrability;
- Navier--Stokes stochastic cascade;
- Strong-KPP uniqueness;
- supercritical dissipative SQG;
- long-maturity marked branching;
- Gaussian bridge coarsening;
- 1D hard FA-1f finite-seed programme based on the centered transform / unnormalized patch-transfer routes.

Closed screened routes:

- 1D FA-1f Bernoulli-quench sibling cancellation;
- strongly non-harmonic Wigner--Fokker--Planck via unweighted Moyal/skew cancellation;
- 2D FA-1f relaxation logarithm via local signed-move cancellation;
- 2D FA-1f nearest-vacancy annular/electrical-capacity observable;
- general bootstrap-percolation sharpness from bare inclusion--exclusion/Bonferroni overlap subtraction.

Broader mathematical problems may remain open. What is closed is the recorded programme or mechanism.

## Stable claims

`research/claim-registry.md` is the status index.

- `BABP-EDGE-001`: `verified`, audit `d1ef2ca`.
- `BABP-CONV-001`: `verified`, independent correctness reviews `abb05f6` and `1aeb5a5`.

No all-parameter BABP convergence claim is currently registered.