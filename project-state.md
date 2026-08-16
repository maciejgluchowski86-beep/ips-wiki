# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Active scientific direction

**Corrected sharp concentration of voter-model discordant edges on random regular graphs.**

- Branch: `research/voter-discordant-concentration`.
- Workspace: `research/active/voter-discordant-concentration/`.
- Active student: persistent Graduate Student D.
- Latest meeting: `research/active/voter-discordant-concentration/meetings/001-sharp-concentration-reduction.md`, `state_narrowed: yes`.
- Current assignment: `students/student-d/assignment-002.md`.

### Source correction

Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), Eq. (1.9), is false literally at very small times. It quantifies over every `t_n=o(n)`, including `t_n->0`, while Bernoulli initial conditions have nondegenerate `n^{-1/2}` fluctuations. The explicit counterexample

$$
t_n=n^{-3},\qquad C_n=\log n
$$

leaves the voter configuration unchanged with probability tending to one while the source threshold is `(log n)/n^2=o(n^{-1/2})`.

The active target is therefore

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0
$$

for fixed `d>=3`, `u in (0,1)`, every `t_n=o(n)`, and every `C_n->infinity`.

This source correction has been independently reconstructed by the Professor but is not yet promoted to a stable project claim. The substantive programme target is the corrected theorem.

### Current mathematical reduction

For normalized discordance `Dcal`, the exact Dynkin martingale satisfies

$$
\frac d{dt}\langle M\rangle_t\le4/n,
$$

so its variance is at most `4t/n` on every fixed regular graph.

The remaining drift is a signed spatial average of two-spin observables on edges and length-two wedges. Its covariance is represented exactly by four coalescing ancestral lineages in the generic case. A sufficient integrated-drift estimate is

$$
\mathbf E\left[
\left(\int_0^t\widetilde h_s\,ds\right)^2
\right]=O_{\mathbb P}(t/n).
$$

The first route now being tested is the variance identity

$$
\frac d{dt}\operatorname{Var}(\mathcal D_t)
=2\operatorname{Cov}(\mathcal D_t,L\mathcal D_t)
+\mathbf E\Gamma(\mathcal D)(\eta_t),
$$

with the second term at most `4/n`. A bound

$$
\operatorname{Cov}(\mathcal D_t,L\mathcal D_t)\le C/n
$$

would close the corrected variance scale. At `u=1/2` this is a particularly clean signed simultaneous four-walk sum.

### Published-method obstruction

The source's Section 5 sample-and-discard architecture pays sampling error `K^{-1/2}` and, when interacting dual families are discarded at unit cost, bad-family fraction of natural size `K(t/n)`. Their balance is `(t/n)^{1/3}`, not the desired `(t/n)^{1/2}`. Routine tuning of `K` or the polynomial time window therefore cannot close the sharp target.

This does not rule out a qualitatively different signed use of the same four-walk duality. Assignment 002 tests exactly that cancellation/corrector possibility.

### Opportunity-cost rule

If the next substantial block yields only absolute cross-meeting estimates whose time growth is too large for `O((1+t)/n)`, with no cancellation, corrector, or alternative structural mechanism, the next meeting must reassess continuation rather than incrementally refine Section 5.

## Most recently closed programme: residual positive-rates / noisy East

The noisy-East finite-wall programme closed at Group Meeting 002 on branch `research/noisy-east-positive-rates`.

On `r11=0`, with `a=r00`, `b=r01`, `c=r10`, the corrected unresolved normalized set is

$$
\mathcal R=\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

The three-site frozen-exterior one-attack factor has sharp East-boundary supremum `5/6`, but repeated attacks from a persistent exterior disagreement cross every fixed finite block almost surely. The pre-committed dynamic-exterior stop condition was therefore triggered. No length-four rescue is allowed.

The broader noisy-East problem remains open; a future return requires a genuinely new mechanism or a separately motivated episode-level theorem with quantitative closure.

## Earlier closed programme: BABP finite seed

BABP closed without a new project result under the standing novelty standard. `BABP-EDGE-001` and `BABP-CONV-001` remain verified technical mathematics with their audit records, but neither is counted as a project contribution.

## Wiki freeze

The principal controls the freeze decision. Professor recommendation remains **keep the live wiki frozen**. No new `proved here` update is warranted.

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
