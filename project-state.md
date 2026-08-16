# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Active scientific direction

**Corrected sharp concentration of voter-model discordant edges on random regular graphs.**

- Branch: `research/voter-discordant-concentration`.
- Workspace: `research/active/voter-discordant-concentration/`.
- Persistent Graduate Student D: idle while correctness reviews run.
- Latest meeting: `research/active/voter-discordant-concentration/meetings/002-genealogical-variance-claim.md`, `state_narrowed: yes`.
- Central claim: `VOTER-CONC-001`, status `claimed`.
- Two independent correctness reviews are in flight; novelty/closest-prior-work audit follows if correctness survives.

### Claimed deterministic variance inequality

For every finite simple `d`-regular graph `G`, every `u in (0,1)`, and every `t>=0`, let `Dcal_t` be the voter-model discordant-edge density. If `pi` is uniform on vertices and `tau_meet` is the meeting time of two independent rate-one continuous-time simple random walks, then

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
}
$$

Student D's proof is in commit `e73fd25`, `students/student-d/002-four-walk-cancellation.md`. The Professor independently reconstructed the argument in `notes/professor-assignment-002-verification.md` and accepts it at `claimed`, not `verified`, status.

The mechanism is genealogical. Conditional on the Harris arrows at observation time, vertices are partitioned into ancestral clusters carrying independent Bernoulli initial labels. The discordant-edge count is a weighted cut statistic on the quotient multigraph. Its conditional variance is controlled by the second moment of cluster sizes, hence by a stationary two-walk meeting probability. The variance of its conditional mean is controlled by cross-interaction of two ancestral edge families and source Eq. (5.6), again reducing to the same two-walk meeting probability.

### Claimed random-regular consequence

Using the meeting estimates in Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), equations (5.7)--(5.8), the claimed deterministic inequality gives, for every deterministic `t_n=o(n)`,

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}\left(\frac{1+t_n}{n}\right).
$$

Hence for every `C_n->infinity`,

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0.
$$

For deterministic `t_n>=1`, `t_n=o(n)`, the stronger variance bound `O_P(t_n/n)` yields the source's proposed `C_n sqrt(t_n/n)` scale.

### Small-time source correction

Literal source Eq. (1.9) is false because it quantifies over arbitrary `t_n=o(n)`, including `t_n->0`, while the Bernoulli initial condition fluctuates on scale `n^{-1/2}`. The explicit counterexample is

$$
t_n=n^{-3},\qquad C_n=\log n.
$$

Thus the corrected all-sublinear scale is `sqrt((1+t_n)/n)`. The claimed theorem recovers the original source scale from time one onward.

### Verification and novelty status

`VOTER-CONC-001` is **not verified**. The two independent hostile review assignments are:

- `research/active/voter-discordant-concentration/audits/assignment-001-review-a.md`;
- `research/active/voter-discordant-concentration/audits/assignment-002-review-b.md`.

If both correctness reviews survive, a separate closest-prior-work audit is required before publication-level novelty or contribution claims.

Under the principal's standing novelty rule, this theorem is structurally eligible if it survives: it is a deterministic graph inequality and full-regime consequence, not a larger-window or better-constant instantiation.

No uniform-in-time process-supremum concentration theorem is claimed; the random-regular result is sequence-wise quenched-in-environment-probability.

## Wiki freeze review trigger

The first central theorem of the active programme has entered independent audit, so `CHATGPT.md` requires the Professor to raise the wiki freeze for principal review. Professor recommendation remains **keep the live wiki frozen** until correctness and novelty audits are complete. No `proved here` page is being promoted now.

## Most recently closed programme: residual positive-rates / noisy East

The noisy-East finite-wall programme closed at Group Meeting 002 on branch `research/noisy-east-positive-rates`.

On `r11=0`, with `a=r00`, `b=r01`, `c=r10`, the corrected unresolved normalized set is

$$
\mathcal R=\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

The three-site frozen-exterior one-attack factor has sharp East-boundary supremum `5/6`, but repeated attacks from a persistent exterior disagreement cross every fixed finite block almost surely. The pre-committed dynamic-exterior stop condition was triggered. No length-four rescue is allowed.

The broader noisy-East problem remains open; a future return requires a genuinely new mechanism or a separately motivated episode-level theorem with quantitative closure.

## Earlier closed programme: BABP finite seed

BABP closed without a new project result under the standing novelty standard. `BABP-EDGE-001` and `BABP-CONV-001` remain verified technical mathematics with their audit records, but neither is counted as a project contribution.

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