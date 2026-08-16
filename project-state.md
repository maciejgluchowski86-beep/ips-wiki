# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/004-two-generation-regeneration-and-depth-obstruction.md`, `state_narrowed: yes`.
- Student F: `students/student-f/assignment-005.md`, all-depth disagreement-stack contraction or obstruction.
- Student G: still finishing `students/student-g/assignment-002.md`; its return will be folded into the next meeting.

On the normalized face `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the source-corrected unresolved chamber remains

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

The frozen-exterior finite-wall route and the cellwise last-exit/scaffold positivity route remain closed.

### Direct transient inputs

Student G proved on the original dynamics the transport--dissipation identity

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

plus boundary-uniform transient zero-density, finite-box concentration, and adjacent-`11` suppression

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
$$

Student F proved the coupling drift

$$
\mathcal L^{\rm coup}D_i
\le
-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i,
$$

where `J_i` is the high-risk state with a right disagreement and agreed left spin one. Marginal `11` bounds do not yet control this term proportionally to disagreement.

### Meeting 004: two-generation live regeneration

Put

$$
q:=1-c+a>0.
$$

Student F proved and the Professor checked the structural local fact that **every disagreement site** has predictable coalescence intensity at least `q`, regardless of disagreement orientation and regardless of whether its right neighbour is agreed or disagreed.

Consequently a disagreeing site coalesces before the next rate-one ring immediately to its left with conditional probability at least

$$
p:=\frac q{1+q}.
$$

After a rightmost parent has created its first child, with the prospective grandchild site still agreed, this gives the genuine environment-uniform two-generation regeneration bound

$$
\boxed{
\mathbb P(\text{parent and child clear before grandchild creation}\mid\mathcal F)
\ge
p^2
=
\left(\frac{1-c+a}{2-c+a}\right)^2>0.
}
$$

The full coupling still contains arbitrary child deaths and reinfections outside the successful subevent; reinfection is not suppressed in the model.

### East-boundary diagnostic

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

the crude universal two-generation event is only `O(epsilon^4)`. However F's exact 24-state controlled post-birth calculation gives structured regeneration gaps of order `epsilon` even against a state-feedback right-boundary adversary. This confirms a genuine fast post-birth killing mechanism, while still giving no uniform gap at the excluded East boundary.

### Finite-depth result and composition obstruction

The ordered-clearing argument extends to any finite **active-span depth** `m`:

$$
\mathbb P(\text{clear the depth-}m\text{ episode before a new disagreement crosses its left boundary}\mid\mathcal F)
\ge p^m.
$$

The exponent must be active-span depth, not merely current disagreement count, because internal agreed gaps can themselves be infected.

These certified gaps are summable in depth:

$$
\sum_{m\ge1}p^m<\infty.
$$

Therefore finite-depth positive regeneration numbers do not by themselves force extinction of an ancestry stack whose depth keeps increasing.

### Current proof direction

Finite-depth escalation stops. Do not compute depth three, four, etc. as separate episodes.

The current bottleneck is **all-depth disagreement-stack composition**. The next accepted result must control arbitrary ancestry depth structurally, for example through a weighted Lyapunov/supermartingale, a finite multi-type domination with spectral radius below one, a disagreement-weighted `J_i` estimate closing the coupling drift, a finite summary/restart state dominating deeper stacks, or a rigorous obstruction to a materially defined class of such mechanisms.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard; the project factor-`2` variance bound and quotient-genealogy proof remain verified technical mathematics.

## Wiki freeze

The live wiki remains frozen during active research.
