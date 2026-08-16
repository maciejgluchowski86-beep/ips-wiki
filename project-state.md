# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Simple means one-dimensional, homogeneous, binary, one-sided nearest-neighbour, in the formulation of Głuchowski--Menz, *Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*.
- The Professor continues to direct methods, proof-spine changes, audits, and stopping of individual routes, but does **not** pivot to another scientific target on opportunity-cost grounds.
- Principal's verbatim starting note: `research/active/positive-rates-conjecture/principal-starting-note.md`.
- Initial setup meeting: `research/active/positive-rates-conjecture/meetings/000-principal-reset.md`, `state_narrowed: no`.
- Requested new persistent agents: Students F and G; their first assignments are already committed on the active branch.

Write

$$
r_{xy}=P_0(1\mid xy).
$$

Positive rates are

$$
r_{11}<1,\qquad r_{10}<1,\qquad r_{01}>0,\qquad r_{00}>0.
$$

After the proved time-scaling/state-symmetry reductions and the 2026 long-lived-state criterion, the source-corrected unresolved normalized chamber on `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

is

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

This residual chamber is the present working localization, not a substitute for the fixed full target.

### Anti-circularity instruction

The principal identified the expected failure mode as repeated reformulation of the same PRC obstruction in equivalent language. The active `state.md` and `proof-spine.md` therefore require every substantial block to produce a genuinely one-way reduction, a new target-relevant estimate, a material obstruction, or a finite/local reduction with quantitative error. Merely changing spin convention, dual variables, density-profile language, invariant-measure language, or finite/infinite-volume notation does not count as progress. If the Professor cannot state exactly what became strictly easier, narrower, or impossible, the meeting is marked `state_narrowed: no`.

### Starting technical lead

The principal recalls an earlier monomial-duality construction based on the last successful interaction leaving a finite interval, its active spacetime ancestry trail, and undoing duality elsewhere. The recollection suggests an early boundary-modified spin system, a late confined spin system, a positive exponential trail factor, and a Duhamel estimate reducing ergodicity to a qualitative eventual-density premise. This recollection is intentionally preserved verbatim and is **not yet a verified reduction**. Student F is asked to recover/test it; Student G independently attacks the same fixed target, especially the density/finite-box interface.

## Closed route inside the fixed target

The previous branch `research/noisy-east-positive-rates` closed the **fixed finite agreed-block / frozen-exterior wall route**, not the positive-rates conjecture itself.

Inherited negative knowledge:

- the one-site long-lived-state criterion fails in the true residual chamber;
- the exact three-site frozen-exterior one-attack factor has sharp East-boundary supremum `5/6`;
- repeated attacks from a permanently frozen exterior disagreement cross every fixed finite agreed block almost surely;
- therefore one-attack fixed-wall factors do not concatenate into ergodicity.

Do not restart that route by increasing block length or refining the same statistic.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically **verified** but **not a new project result under the standing novelty standard**.

The project proved

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t)
$$

for every finite simple positive-degree regular graph. Correctness survived the Professor reconstruction and two independent hostile reviews.

The closest-prior-work audit found that Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), Proposition 4.1 proof (4.2) together with (5.5)--(5.6), already imply the theorem-level bound with constant `4`, and their (5.8) then yields the same random-regular asymptotic concentration consequences. The factor `2` and quotient-genealogy proof are retained as verified technical mathematics, not a contribution claim.

Literal source Eq. (1.9) is false for unrestricted very-small times; the verified counterexample is `t_n=n^{-3}`, `C_n=log n`. Priority of that narrow correction remains unresolved and is not an active task.

## Superseded unstarted direction

The branch `research/heterogeneous-voter-discordance` was initialized after the voter-concentration closure but is **shelved by principal direction before substantive student work**. It is neither a failed theorem programme nor an active reserve that can displace the fixed positive-rates target.

## Earlier closed programme: BABP finite seed

BABP closed without a new project result under the standing novelty standard. `BABP-EDGE-001` and `BABP-CONV-001` remain verified technical mathematics with their audit records, but neither is counted as a project contribution.

## Wiki freeze

The live wiki remains frozen during active research. No new `proved here` material is promoted without the usual verification and novelty requirements.

## Closed programmes and routes

Closed programmes/routes not to be retried by renaming include:

- quadratic-Hessian;
- Fresnel integrability;
- Navier--Stokes stochastic cascade;
- Strong-KPP uniqueness;
- supercritical dissipative SQG;
- long-maturity marked branching;
- Gaussian bridge coarsening;
- 1D hard FA-1f finite-seed programme based on centered-transform / unnormalized patch-transfer routes;
- 1D BABP finite-seed programme based on finite-window submartingales and the unresolved invariant-front continuation;
- the **fixed finite-wall** noisy-East route based on frozen-exterior crossing factors;
- random-regular voter-discordance sharp concentration based on the variance-to-meeting reduction already implicit in Avena et al. (2024).

The positive-rates conjecture itself is explicitly active despite the closure of the earlier fixed-wall route.
