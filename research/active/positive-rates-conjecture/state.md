# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** The Professor may close or redirect proof routes but does not pivot to another scientific problem.

Target:

> Every simple one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with source-corrected residual chamber

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Latest meeting: `meetings/004-two-generation-regeneration-and-depth-obstruction.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-005.md`, all-depth disagreement-stack contraction or obstruction;
- Student G: still finishing `students/student-g/assignment-002.md`; its independent return will be folded into the next meeting.

## Closed proof routes

The following mechanisms are closed and must not be revived by finite-size escalation:

1. fixed finite agreed-block / frozen-exterior wall crossing;
2. cellwise last-exit/scaffold insertion positivity, which fails at two-cell composition.

The principal's hidden-interaction algebra and one-cell regional kernel remain correct technical mathematics but no longer form an active closing route.

## Reusable direct estimates

Student G proved on the original normalized dynamics the transport--dissipation identity

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

plus boundary-uniform transient zero-density, finite-box concentration, and adjacent-`11` suppression

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
$$

Student F proved the exact coupling drift

$$
\mathcal L^{\rm coup}D_i
\le
-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i,
$$

where `J_i` is the high-risk state with a right disagreement and agreed left spin one. Marginal `11` control does not close this inequality because it produces an additive error.

## Live-disagreement results

Put

$$
q:=1-c+a>0.
$$

Meeting 004 verifies the stronger local fact:

> Every disagreement site has predictable coalescence intensity at least `q`, regardless of disagreement orientation and regardless of whether its right neighbour is agreed or disagreed.

If `T_i` is the next coalescence time of a disagreeing site and `R_{i-1}` the next rate-one ring immediately to its left, then

$$
\boxed{
\mathbb P(T_i<R_{i-1}\mid\mathcal F)
\ge
p:=\frac q{1+q}.
}
$$

This gives a genuine two-generation regeneration theorem. After a rightmost parent `j` has created its first child at `j-1`, while `j-2` remains agreed, let `sigma_2` be grandchild creation at `j-2` and `tau_2` elimination of both parent and child. Then, uniformly over the actual evolving common right environment and all post-first-child local states,

$$
\boxed{
\mathbb P(\tau_2<\sigma_2\mid\mathcal F)
\ge
\left(\frac{1-c+a}{2-c+a}\right)^2>0.
}
$$

Reinfection is retained in the full process; the proof isolates a positive-probability subevent on which the child coalesces before the grandchild clock and the parent then coalesces before the child can be reinfected.

## Near-East diagnostic

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

the crude universal two-generation gap is order `epsilon^4`, but F's exact 24-state controlled calculation on structured post-birth states shows a much larger robust gap: order `epsilon` (`(9/2)epsilon+O(epsilon^2)` when the prospective grandchild spin is zero, and `epsilon+O(epsilon^2)` when it is one). Thus post-birth killing is a genuine compensation mechanism, although no residual-uniform East-boundary gap is claimed.

## Finite-depth clearing and its limit

Meeting 004 accepts F's ordered-clearing argument with one correction: the exponent must be the **active-span depth**, not merely the current number of disagreement sites. If a finite live episode occupies an active span of depth at most `m` between a coupled left boundary and coupled right tail, then

$$
\mathbb P(\text{complete clearing before a new disagreement crosses the left boundary}\mid\mathcal F)
\ge p^m.
$$

Internal agreed gaps can be infected, so current disagreement count alone is not a safe stage count.

This finite-depth theorem does not close the target. Since `sum_m p^m<infinity`, the certified depth-dependent clearing gaps are summable and do not force extinction of an ancestry stack whose depth keeps increasing.

## Current bottleneck: all-depth composition

Do not compute depth three, four, etc. as separate episodes.

The next required gain is one theorem controlling arbitrary ancestry depth, for example:

- a weighted disagreement-stack Lyapunov/supermartingale with negative drift;
- a finite multi-type branching or renewal domination with spectral radius `<1`;
- a disagreement-weighted bound on `J_i` that closes the coupling drift;
- a finite summary state dominating arbitrary stack depth;
- or a rigorous obstruction showing that such all-depth contractions cannot hold in a natural class.

Student F is assigned to this structural problem. Student G completes its already-running weighted/regional bridge attempt before rerouting.

## Anti-circularity rule

Finite-depth escalation is now explicitly prohibited as a substitute for composition. The next accepted progress must control arbitrary depth structurally or eliminate a materially defined all-depth mechanism.

## Wiki

Keep the live wiki frozen during research.
