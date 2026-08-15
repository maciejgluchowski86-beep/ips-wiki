# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an already-established arbitrary-size method does not count as a new project result merely because the computation is exact or the numerical constant is better. A qualifying result must add structural mathematics: a theorem across a genuine regime, a qualitative mechanism, a structural success/failure theorem, or a proof/refutation of the target problem.

## Most recently closed programme: residual positive-rates / noisy East

Branch: `research/noisy-east-positive-rates`.

Workspace: `research/active/noisy-east-positive-rates/`.

Latest meeting: `meetings/002-three-site-gap-and-wall-closure.md`, `state_narrowed: yes`.

**Decision: close the present noisy-East finite-wall programme.** The positive-rates/noisy-East problem itself remains open.

### Source-corrected residual set

On `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the normalized unresolved set obtained from the actual proved 2025/2026 criteria is

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

The assignment-001 path

$$
a=\varepsilon,
\qquad b=\frac\varepsilon2,
\qquad c=1-\varepsilon^2
$$

was incorrectly labeled as residual in earlier state files. Published Głuchowski--Menz (2025), Corollary 7.2, already covers it because `b<a`. The earlier two-site limits to one and the `9/10` length-three value on that path remain correct finite-state diagnostics but are not evidence about the unresolved set.

### Assignment-002 result on the true residual

For the frozen-exterior length-three one-attack statistic,

$$
R_3^{\rm adv}(r),
$$

maximized over all agreed three-site words and both exterior disagreement orientations, Student C proved and the Professor independently reconstructed

$$
\sup_{\bar r\in\partial_E\mathcal R}
\limsup_{\substack{r\to\bar r\\r\in\mathcal R}}
R_3^{\rm adv}(r)
=\frac56.
$$

The value is sharp along the genuine residual sequence

$$
a=\frac\varepsilon2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2.
$$

No project claim is registered from this finite-state local theorem.

### Why the wall route closes despite the `5/6` gap

At every strict residual parameter point, a permanently frozen exterior disagreement eventually penetrates every fixed finite agreed block almost surely under repeated attacks. Thus `R_3^adv<1` controls one attacked excursion only and cannot concatenate into disagreement extinction.

A valid proof would require a strictly stronger dynamic source-episode estimate controlling exterior-disagreement lifetime, repeated attacks, overlap, and episode duration. No such domination follows from the `5/6` calculation and no concrete closing inequality is known.

Meeting 001 pre-committed to abandon the finite-wall route in exactly this circumstance rather than respond by increasing block length. There will be no length-four rescue.

The programme therefore closes without a qualifying new project result. A future return to noisy East requires a genuinely new mechanism or a separately motivated episode theorem with a concrete quantitative closure.

## Next direction selected

Reopen Graduate Student A's opportunity-cost list. The next target is the explicit sharp-concentration problem for discordant edges in the voter model on random regular graphs: extend concentration to the natural `sqrt(t/n)` fluctuation scale uniformly through all sublinear times `t=o(n)`.

The published Avena--Baldasso--Hazra--den Hollander--Quattropani paper states this strengthening as expected but beyond its current method. The first research block should attack the load-bearing integrated-drift/coalescing-walk covariance obstruction and should have an early structural exit criterion. It must not be organized as a sequence of slightly longer time-window bounds.

A new branch/workspace should be initialized for this genuinely new direction, with a new persistent graduate student.

## Earlier closed programme: BABP finite seed

BABP closed without a new project result under the standing novelty standard. Retained verified mathematics:

- `BABP-EDGE-001`: exact ten-site `lambda=1/40` certificate, audit `d1ef2ca`;
- `BABP-CONV-001`: verified self-contained corrector-to-convergence proof, reviews `abb05f6` and `1aeb5a5`.

Neither is a project contribution because Sudbury's finite-window method is already arbitrary-window and the convergence implication is classical.

## Wiki freeze

The principal controls the freeze decision. Professor recommendation remains **keep the live wiki frozen**. No noisy-East `proved here` update is warranted.

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
