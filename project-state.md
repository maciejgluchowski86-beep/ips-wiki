# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Active scientific direction

**Sharp concentration of voter-model discordant edges on random regular graphs.**

- Branch: `research/voter-discordant-concentration`.
- Workspace: `research/active/voter-discordant-concentration/`.
- Active student: persistent Graduate Student D.
- Target source: Avena--Baldasso--Hazra--den Hollander--Quattropani, *Discordant edges for the voter model on regular random graphs* (ALEA 2024).
- Target: resolve the source's proposed sharp concentration regime for the discordant-edge density on the intrinsic `sqrt(t/n)` scale throughout sublinear times, subject to Student D's exact source transcription and very-small-time check.
- Current first edge: derive the exact semimartingale decomposition, identify the integrated centered-drift covariance estimate carrying the sharp theorem, and determine whether the source's weak-dependence/coalescing-walk method can plausibly prove it.
- Assignment: `research/active/voter-discordant-concentration/students/student-d/assignment-001.md`.

The first block is deliberately diagnostic. A modest extension of the existing polynomial time window is not a project result. The programme wants the sharp theorem, a structural correction/refutation of its literal formulation, or a precise reason the visible route is not tractable.

## Most recently closed programme: residual positive-rates / noisy East

The noisy-East finite-wall programme closed at Group Meeting 002 on branch `research/noisy-east-positive-rates`.

The meeting records `state_narrowed: yes` because three material questions were resolved.

### Source correction

On `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the actual unresolved normalized set obtained from the proved 2025/2026 criteria is

$$
\mathcal R=\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

The earlier assignment-001 path

$$
a=\varepsilon,\qquad b=\frac\varepsilon2,\qquad c=1-\varepsilon^2
$$

is already covered by published Głuchowski--Menz (2025), Corollary 7.2, because `b<a`. Earlier repository labels calling it a genuine residual path were incorrect and have been corrected explicitly on the research branch.

### Exact local characterization on the true residual

For the frozen-exterior three-site one-attack factor,

$$
\sup_{\bar r\in\partial_E\mathcal R}
\limsup_{\substack{r\to\bar r\\r\in\mathcal R}}
R_3^{\rm adv}(r)=\frac56,
$$

sharply. This is useful diagnostic mathematics, not a registered project contribution.

### Concatenation obstruction and closure

With an exterior disagreement held forever, repeated attacks penetrate every fixed finite agreed block almost surely. Therefore the one-attack `5/6` factor is not an iteratable adversarial block-renewal quantity.

Meeting 001 had pre-committed to close the finite-wall route if a uniform local gap required an uncontrolled stronger dynamic-exterior quantity to concatenate. That condition was met. There will be no length-four rescue.

The broader noisy-East problem remains open. A future return requires a genuinely new mechanism or a separately motivated episode-level theorem with a concrete quantitative closure.

No noisy-East project claim is registered from the finite-state diagnostics.

## Earlier closed programme: BABP finite seed

BABP closed without a new project result under the standing novelty standard. `BABP-EDGE-001` and `BABP-CONV-001` remain verified technical mathematics with their audit records, but neither is counted as a project contribution.

## Wiki freeze

The principal controls the freeze decision. Professor recommendation remains **keep the live wiki frozen**. No new `proved here` update is warranted from the closed noisy-East programme.

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
- residual noisy-East programme based on fixed finite agreed-block walls and frozen-exterior crossing factors.

Broader mathematical problems may remain open. What is closed is the recorded programme/mechanism at its present expected value.
