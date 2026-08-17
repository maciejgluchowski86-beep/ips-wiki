# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Active scientific direction

**Voter-model discordance on undirected heterogeneous configuration models.**

- Branch: `research/heterogeneous-voter-discordance`.
- Workspace: `research/active/heterogeneous-voter-discordance/`.
- Active student: persistent Graduate Student E.
- Initial bounded ensemble: configuration models whose empirical degree law converges to a fixed law supported on `{3,...,D}` for finite `D`.
- Source-level target: identify and prove the unequal-degree analogues of the regular-random-graph discordance profile and consensus-scale diffusion constant.
- Assignment: `research/active/heterogeneous-voter-discordance/students/student-e/assignment-001.md`.

Frank den Hollander, *Evolution of Discordance* (2025), Section 2.4, explicitly states that extending the regular discordance theorems to configuration models with unequal degrees remains open and that no conjectural analogues of the regular `theta_d` and `f_d(t)` are given there. Student E's first assignment must nevertheless check general finite-voter and configuration-model literature before treating any candidate formula as new.

### First structural edge

For a fixed undirected graph with degrees `d_x`, `m=|E|`, and stationary random-walk weights

$$
\pi_x=\frac{d_x}{2m},
$$

the conserved voter coordinate is

$$
B^\pi(\eta)=\sum_x\pi_x\eta_x,
$$

not the unweighted density. If `k_x` is the number of neighbours disagreeing with `x`, then

$$
\Gamma(B^\pi)(\eta)
=\frac1{4m^2}\sum_xd_xk_x
=\frac1{4m^2}
\sum_{\{x,y\}\in E:\eta_x\ne\eta_y}(d_x+d_y).
$$

Thus the consensus-scale bracket is driven by a degree-weighted discordant-edge observable. The raw discordant-edge profile and bracket-weighted profile coincide up to a constant only in the regular case. The first assignment must derive the exact local weak rootings, candidate profiles, and meeting-time constant, and determine which parts are already prior art.

## Most recently closed programme: voter discordance sharp concentration on random regular graphs

The regular-graph concentration programme closed at Group Meeting 004 on branch `research/voter-discordant-concentration` after a negative closest-prior-work audit.

`VOTER-CONC-001` is mathematically **verified** but **not a new project result under the standing novelty standard**.

The project proved the sharper deterministic inequality

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
$$

for every finite simple positive-degree regular graph. Correctness survived the Professor reconstruction and two independent hostile reviews.

However, Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), Proposition 4.1 proof (4.2) together with (5.5)--(5.6), already imply the theorem-level bound

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t),
$$

and source (5.8) then yields the same random-regular asymptotic concentration consequences. The project's factor `2` and quotient-genealogy proof are retained as verified technical mathematics, not a contribution claim.

Literal source Eq. (1.9) is false for unrestricted very-small times; the project counterexample `t_n=n^{-3}`, `C_n=log n` is verified. Priority of that narrow correction remains unresolved because a relevant Capannoli thesis was inaccessible to the novelty auditor. It is not being pursued as an active programme on opportunity-cost grounds.

Do not reopen the regular concentration programme to optimize the constant or repackage the immediate prior-work corollary.

## Earlier closed programme: residual positive-rates / noisy East

The noisy-East fixed-finite-wall programme is closed. Its corrected residual chamber and sharp frozen-exterior three-site factor remain useful diagnostic mathematics, but repeated attacks show the one-attack factor does not concatenate. No length-four rescue is allowed.

## Earlier closed programme: BABP finite seed

BABP closed without a new project result under the standing novelty standard. `BABP-EDGE-001` and `BABP-CONV-001` remain verified technical mathematics with their audit records, but neither is counted as a project contribution.

## Wiki freeze

The live wiki remains frozen. No `proved here` promotion follows from the closed voter-concentration programme because its central verified theorem is non-contributory under the standing novelty standard.

## Closed programmes and routes

Closed programmes not to be retried by renaming include:

- quadratic-Hessian;
- Fresnel integrability;
- Navier--Stokes stochastic cascade;
- Strong-KPP uniqueness;
- supercritical dissipative SQG;
- long-maturity marked branching;
- Gaussian bridge coarsening;
- 1D hard FA-1f finite-seed programme based on centered-transform / unnormalized patch-transfer routes;
- 1D BABP finite-seed programme based on finite-window submartingales and the unresolved invariant-front continuation;
- residual noisy-East programme based on fixed finite agreed-block walls and frozen-exterior crossing factors;
- random-regular voter-discordance sharp-concentration programme based on the variance-to-meeting reduction already implicit in Avena et al. (2024).

Broader mathematical problems may remain open. What is closed is the recorded programme/mechanism at its present expected value.
