# Programme state

## Direction

Title: residual positive-rates conjecture / noisy East

Branch: `research/noisy-east-positive-rates`

Professor lineage: persistent ChatGPT Professor

Graduate Student C: idle after programme closure

Graduate Students A and B: idle with prior lineages

Workspace: `research/active/noisy-east-positive-rates/`

Latest group meeting: `meetings/002-three-site-gap-and-wall-closure.md`

## Outcome

**Programme closed on expected-value grounds.**

The target remains mathematically open. What is closed is the present finite-wall route and, absent another concrete mechanism, this active programme.

No qualifying new project result is registered under the standing novelty standard.

## Source-corrected residual set

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

Using the proved sufficient regions in Głuchowski--Menz (2025), including Corollary 7.2, together with the 2026 long-lived-state theorem, the unresolved normalized set is

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Hence throughout `R`,

$$
1>c>b>a>0=r_{11}.
$$

The assignment-001 path

$$
a=\varepsilon,\qquad b=\frac\varepsilon2,\qquad c=1-\varepsilon^2
$$

was previously mislabeled as a genuine residual path. It is already covered by the published 2025 Corollary 7.2 because `b<a`. Its exact two-site and three-site calculations remain valid diagnostics, but they do not probe the unresolved set.

The 2026 paper contains a prose summary of the earlier covered region with the opposite `a,b` inequality. Programme state follows the published 2025 theorem statement and proof.

## Assignment-002 theorem about the local diagnostic

For `r in R`, let

$$
R_3^{\rm adv}(r)
$$

be the frozen-exterior unconditional one-attack crossing probability for a three-site agreed block, maximized over all eight agreed words and both exterior disagreement orientations.

Student C proved and the Professor independently reconstructed

$$
\sup_{\bar r\in\partial_E\mathcal R}
\limsup_{\substack{r\to\bar r\\r\in\mathcal R}}
R_3^{\rm adv}(r)
=\frac56.
$$

The bound is sharp along the genuine residual sequence

$$
a=\frac\varepsilon2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2.
$$

This is a useful exact characterization of the local one-attack statistic, not a new ergodicity theorem and not a registered project contribution.

## Structural obstruction to concatenation

At any strict residual point, if an exterior disagreement is frozen forever, repeated attacks cross every fixed finite agreed block almost surely.

Thus a one-attack inequality `R_3^adv<1` does not concatenate into disagreement extinction. A valid proof would require a stronger episode-level quantity controlling the stochastic lifetime/evolution of the exterior source, repeated attacks, overlaps, and episode duration. No such estimate has been obtained or reduced to the `5/6` theorem.

Meeting 001 pre-committed to abandon the finite-wall route if this dynamic-exterior upgrade required an uncontrolled stronger quantity. That condition is now met. Do not move to block length four.

## Closure boundary

Do not reopen this programme merely by:

- increasing the fixed block length;
- changing the frozen-exterior one-attack statistic;
- refining its constants; or
- renaming the uncontrolled source-episode process as another wall variant.

A future noisy-East programme requires a genuinely new mechanism or a separately motivated episode-level theorem with a concrete quantitative closure.

## Research delta

Latest meeting `state_narrowed`: yes.

Evidence pointer: `students/student-c/002-uniform-three-site-wall.md`, its exact verifier, `notes/professor-uniform-three-site-review.md`, and `meetings/002-three-site-gap-and-wall-closure.md`.

What narrowed:

- the true residual set was source-corrected;
- the earlier diagnostic path was shown to be already covered;
- the full East-boundary frozen-exterior three-site statistic was characterized sharply by `5/6`;
- repeated attacks proved that this statistic is not an iteratable block-renewal quantity;
- the finite-wall route was closed under the pre-committed stop rule.

Consecutive no-narrowing meetings: 0.

## Direction

`close`.
