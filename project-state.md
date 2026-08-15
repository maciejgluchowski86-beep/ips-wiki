# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Research architecture

The group has one persistent ChatGPT Professor directing persistent graduate-student sessions. At most two sessions are in flight at once. The Professor owns scientific direction, proof spines, audits, opportunity-cost judgments, and closure decisions. Students do specified autonomous technical work and persist with their scientific direction.

The repository is canonical technical memory. Conversation links are optional only; successor sessions must rely on repository handovers and exact transcript transfer when necessary.

## Active scientific direction

**1D BABP from a finite seed — committed programme.**

- Research branch: `research/babp-finite-seed`
- Workspace: `research/active/babp-finite-seed/`
- Positive target: for every `lambda>0`, prove local convergence of one-dimensional biased annihilating branching process started from a finite nonempty particle set to Bernoulli equilibrium of density `lambda/(1+lambda)`.
- Historical recorded range: Martinelli--Shapira--Toninelli (2025), Remark 5.4, records finite-seed convergence for `lambda>0.0347` after Sudbury.
- Verified project claim `BABP-EDGE-001`: at `lambda=1/40`, a ten-site statewise edge corrector has exact drift `1033/40000000>0` and yields the audited liminf/limsup ballistic bounds.
- New claimed project theorem `BABP-CONV-001`: for fixed `lambda>0`, existence of any bounded finite-window corrector with uniform statewise positive drift implies local convergence from every finite nonempty deterministic set to Bernoulli equilibrium.
- Concrete claimed corollary: combining `BABP-CONV-001` with verified `BABP-EDGE-001` gives finite-seed convergence at `lambda=1/40=0.025`, below the range recorded in the 2025 progress paper.
- Claim status: `BABP-CONV-001` is `claimed`, not `verified`; two independent hostile audits are requested.
- Current first unresolved issue: correctness audit of the corrector-to-convergence bridge.
- Downstream development problem, if the bridge survives: construct a positive statewise finite-window corrector for every `lambda>0`, e.g. prove the finite-window threshold tends to zero.
- Professor: persistent ChatGPT Professor.
- Graduate Student B: temporarily idle pending theorem audits.
- Graduate Student A: idle after bounded opportunity-cost reconnaissance.
- Two in-flight slots: independent audits 002 and 003 of `BABP-CONV-001`.
- Latest group meeting: `research/active/babp-finite-seed/meetings/004-corrector-to-convergence.md`.

## Verified edge result

For finite nonempty `B`, let `R=max B`, encode the first `k` sites behind `R` by `u` and the next exterior bit by `z`, and put

$$
H(B)=R(B)+\phi(u(B)).
$$

The exact statewise drift is

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda[1+\phi(T_+u)-\phi(u)]\\
&+u_1[-1+\phi(T_-^zu)-\phi(u)]\\
&+\sum_{j=1}^k n_j^z(u)[\lambda(1-u_j)+u_j]
[\phi(u^{(j)})-\phi(u)].
\end{aligned}
$$

At `lambda=1/40`, `k=10`, the verified rational certificate has

$$
\min_{u,z}D_{10,1/40}(u,z;\phi)
=\frac{1033}{40000000}>0.
$$

Therefore, for every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

Audit `d1ef2ca` independently verified this claim. It does not assert existence of limiting speeds.

## Claimed convergence bridge

Meeting 004 changed the theorem picture. The bridge does **not** use bare ballistic edge bounds as a sufficient hypothesis. It uses the full statewise inequality `D>=v` on every edge state.

For a tagged internal vacant gap, put the same corrector on the particles bordering its left and right sides. The corrected gap width has uniformly negative drift. Positive gaps are born at width one, do not split, and distinct positive gaps cannot merge in one dimension. Exponential tilting gives uniform lifetime and maximum-width tails; Poisson domination controls physical gap displacement; and a compensator sum over all gap nucleations yields

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

The Professor independently reconstructed these steps and found no use of the 2025 particle-number-growth theorem. The deterministic initial configuration is only required to be finite and nonempty.

The external stationary-limit inputs were also checked by the Professor:

- Jahnel--Köppl (2026), Theorem 2.5, applies to BABP because its updates are single-site, rates per site are uniformly bounded, and influences have finite nearest-neighbour range; hence every weak limit point is stationary.
- Martinelli--Shapira--Toninelli (2025), Corollary 2.9, classifies every stationary one-dimensional BABP law as a mixture of the empty state and Bernoulli equilibrium.

The empty-window estimate forces the empty mixture coefficient to vanish. This gives the claimed general implication `(EC) => finite-seed convergence` and the concrete `lambda=1/40` corollary.

Because this theorem is substantially stronger than the verified edge result, the existing audit does not cover it. It is registered separately as `BABP-CONV-001` with status `claimed`.

## Historical provenance status

The accessible Sudbury (1999) record confirms the `0.0347` finite-seed convergence threshold, hunted-submartingale method, and edge-speed bounds. Its full body has not been obtained, so literal identity with the present `k=8` LP remains unverified.

This provenance question is not load-bearing for either current project claim. The claimed `lambda=1/40` convergence theorem stands or falls on the new gap proof plus the checked external stationary-limit inputs.

## Most recently closed programme

**1D hard FA-1f from a finite seed** was closed at Group Meeting 002 on expected-value grounds. The open problem itself remains worthwhile.

Two distinct project mechanisms were settled:

1. the exact centered `h`-transform to a positive finite-set process is correct but is an invertible finite-volume similarity with no demonstrated simplification;
2. the exact unnormalized successful-skeleton transfer restores real consistency-probability losses on restricted routing sectors, but after complete branching its centered coefficient matrix satisfies

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B),
$$

where `Q_t` is the same E1 Markov semigroup. Thus the full `h`-weighted transfer is conservative.

The principal also supplied prior negative tractability evidence from extensive earlier ChatGPT work on 1D FA-1f off-equilibrium convergence. Cancellation/duality is not a preferred or required organizing mechanism.

## Canonical prior work: patch construction

The principal's manuscript `paper/`, *Patch representations and convergence for facilitated spin systems*, is authoritative for the patch construction and its proofs and supersedes the deprecated IPS wiki layer on those points.

The patch construction remains a research asset, not a mandatory template. The active BABP mechanism is the finite-state edge corrector and internal-gap control.

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

## Reusable lessons

- Wrong-norm or wrong-weight cancellation is usually fatal when the critical conversion restores the lost scale.
- Test a strict local gain under the first nontrivial composition and in the controlling quantity.
- Substantial prior model-assisted effort without a route is real tractability evidence.
- Recent progress/survey papers with explicit open problems are useful target sources; do not force duality, cancellation, or patches into a target.
- The BABP programme is a positive example of obstruction-first work: reconstructing a historical numerical barrier exposed an improvable finite-state optimization problem.
- A theorem consequence must be audited separately from a computational certificate. `BABP-EDGE-001` is verified; `BABP-CONV-001` is not yet.
- The distinction between a statewise generator inequality and its asymptotic corollary can be mathematically decisive: the new gap proof needs the former.

## Group-meeting homeostasis

Meeting 003: `state_narrowed: yes`.

Meeting 004: `state_narrowed: yes`, because the statewise edge corrector was shown to control internal gaps and produced a complete claimed convergence proof at `lambda=1/40`.

Three-consecutive-no backstop is not active.

## Stable claim promotion

`research/claim-registry.md` is the status index.

- `BABP-EDGE-001`: `verified`, audit `d1ef2ca`.
- `BABP-CONV-001`: `claimed`. Pending audits:
  - `research/active/babp-finite-seed/audits/002-corrector-to-convergence-request.md`;
  - `research/active/babp-finite-seed/audits/003-corrector-to-convergence-request.md`.

Do not promote the convergence theorem until both independent reviews have returned and their objections, if any, have been resolved by the Professor.

## Opportunity cost

The residual simple positive-rates/noisy-East problem remains the strongest reserve target from Student A's reconnaissance. BABP remains preferred while its theorem audits are pending because it has one verified nontrivial result and a complete claimed open-problem theorem.

## Wiki

The wiki is frozen except for correctness repairs and prerequisites genuinely required by active research. Deprecated IPS wiki material does not override the canonical patch paper.