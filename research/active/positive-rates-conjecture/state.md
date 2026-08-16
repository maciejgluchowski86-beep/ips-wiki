# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** The Professor directs methods, subroutes, audits, and anti-stagnation decisions, but does not pivot to another scientific problem on opportunity-cost grounds.

Target, in the terminology of Głuchowski--Menz, *Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*:

> Every simple IPS with positive rates is ergodic.

A simple IPS is one-dimensional, homogeneous, binary, one-sided and nearest-neighbour, with neighbourhood `N_j={j,j+1}`. Write

$$
r_{xy}=P_0(1\mid xy),\qquad x,y\in\{0,1\}.
$$

Positive rates are

$$
r_{11}<1,\qquad r_{10}<1,\qquad r_{01}>0,\qquad r_{00}>0.
$$

The 2025 time-scaling/state-symmetry reductions and the 2026 long-lived-state theorem reduce the still-unproved normalized chamber on the face `r11=0` to the noisy-East region. With

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

use the source-corrected residual set from the previous programme:

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

The reduction is a working localization of the target, not a replacement target: the programme is judged by progress toward the full simple-IPS PRC.

## Closed route retained as negative knowledge

The previous `research/noisy-east-positive-rates` programme closed the **fixed finite agreed-block / frozen-exterior wall route**. Its useful conclusions remain valid:

- the true residual chamber above;
- the one-site long-lived-state criterion fails throughout it;
- the exact three-site one-attack statistic has sharp East-boundary limit `5/6`;
- under a permanently frozen exterior disagreement, repeated attacks cross every fixed finite agreed block almost surely;
- therefore one-attack fixed-wall factors do not concatenate into ergodicity.

Do not restart that route by increasing block length, changing the one-attack statistic, or renaming the uncontrolled dynamic exterior as another fixed-wall calculation.

## Principal starting lead

The exact principal note is preserved in `principal-starting-note.md` and is intentionally not cleaned up. It recalls an earlier monomial-duality construction based on the **last successful interaction leaving a finite interval**, revealing its ancestry trail and undoing duality elsewhere. The recollection suggests a decomposition into an early boundary-modified spin system, a late confined spin system, and a positive exponential trail factor, followed by a Duhamel estimate that may reduce ergodicity to an eventual high-density statement.

This recollection is **not yet a verified reduction**. The first research block must recover the exact identity and determine the strongest correct one-way implication it yields.

## Anti-circularity rule

The principal identified the main expected failure mode as repeatedly reformulating the PRC in equivalent language without reducing its difficulty. The programme therefore uses the following stricter notion of progress.

A substantial block counts as target progress only if it does at least one of the following:

1. proves a new one-way implication from a demonstrably weaker or more tractable property to ergodicity;
2. proves a new estimate for the actual noisy-East dynamics that was not already encoded in an equivalent representation;
3. eliminates a materially distinct route by counterexample or obstruction;
4. converts an infinite-volume statement to a finite-volume/local statement with a quantitative error estimate that can be attacked independently; or
5. proves the target in a genuinely new residual subregion by a mechanism that plausibly scales to the full chamber.

The following do **not** count by themselves:

- changing spin convention;
- replacing convergence by uniqueness of an invariant measure without a nontrivial implication;
- restating disagreement extinction in dual, genealogical, patch, density-profile, or finite-box notation;
- introducing a new representation without extracting a new bound;
- proving an equivalent criterion whose verification is as hard as the original statement;
- returning to larger fixed-wall blocks.

Every meeting note must state the previous bottleneck in one sentence and say exactly what has become strictly easier, narrower, or impossible. If that sentence cannot be written, use `state_narrowed: no`.

## Initial active questions

1. Can the principal's last-successful-interaction construction be reconstructed exactly and turned into a rigorous theorem of the form
   $$
   \text{qualitative high-density property}\Longrightarrow\text{ergodicity},
   $$
   where the premise is strictly weaker than convergence and independently testable?
2. If yes, can the high-density premise be proved in the true residual chamber by large-box approximation, one-sided finite propagation, regeneration, comparison, or another mechanism that does not already assume ergodicity?
3. If the old reduction does not survive reconstruction, what genuinely different estimate on the residual dynamics replaces it?

## Personnel

The prior live student sessions were lost with the browser state; their committed work remains canonical memory.

Requested new persistent agents for this fixed direction:

- Graduate Student F: broad first attack centered on recovering/testing the principal's old last-interaction reduction, with freedom to abandon it if a stronger route appears.
- Graduate Student G: independent broad attack on the same fixed target, emphasizing a genuinely new high-density/finite-box or regeneration estimate and hostile detection of equivalent reformulations.

They are not narrow specialist roles. Both may use literature, computation, duality, coupling, finite-volume analysis, patch ideas, or other methods as useful.

## Wiki

Keep the live wiki frozen during research. The fixed target does not change the existing verification/novelty rules for public `proved here` material.
