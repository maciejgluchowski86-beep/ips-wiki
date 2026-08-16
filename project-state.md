# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/003-live-source-contraction.md`, `state_narrowed: yes`.
- Student F: `students/student-f/assignment-004.md`, two-generation parent-child live episode including reinfection.
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

The older frozen-exterior finite-wall route and the cellwise last-exit/scaffold positivity route are closed.

### Reusable direct estimates

Student G proved on the original dynamics the transport--dissipation identity

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

plus a boundary-uniform transient zero-density bound, finite-box concentration, and adjacent-`11` suppression

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
$$

Student F's earlier hidden-interaction / `L^-` insertion algebra remains correct technical mathematics, but the cellwise scaffold iteration built from it fails at two-cell composition.

### Meeting 003: first true live-source contraction

Under the actual common-uniform coupling, suppose `j` is a rightmost disagreement, the whole half-line strictly right of `j` is coupled, and `j-1` is still agreed. Let `tau` be source death and `sigma` creation of the first left child. Put

$$
d=b-a,
\qquad
q=1-c+a,
\qquad
D=(b+q)(1+q)-a(1-c).
$$

Student F proved and the Professor checked that, conditional on every evolving common right-hand history,

$$
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F)
\le1-\delta,
\qquad
\delta=\frac{q(d+2q)}D>0.
}
$$

For every `T>0`, a finite-slab regeneration event has probability at least

$$
\boxed{
\delta_T
=
\frac{1-c+a}{1+a}(1-e^{-(1+a)T})>0.
}
$$

This is genuinely different from the frozen-wall statistic: the source runs on its true clock and may disappear.

F also derived the local disagreement drift

$$
\boxed{
\mathcal L^{\rm coup}D_i
\le
-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i,
}
$$

where `J_i` is the high-risk state with a right disagreement and agreed left spin one. The existing marginal `11` estimate controls `E J_i` only through an additive error, so a weighted/conditional occupation estimate is still missing.

### East-boundary diagnostic

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

the one-source childless gap satisfies `delta~2 epsilon^2 -> 0`, and even an all-zero/no-`11` local environment transmits a first child before the simplest competing local changes with probability

$$
\frac{1-\varepsilon}{1+3\varepsilon}\to1.
$$

This rules out a **residual-uniform first-generation** contraction based only on zero-rich/no-`11` snapshots. It does not close the live-episode route: the target is pointwise on strict positive-rate parameters, and the post-first-child dynamics includes additional killing/reinfection mechanisms.

### Current proof direction

Analyze the entire two-generation parent-child episode after the first child is born, including every child death and reinfection while the parent survives. Let `sigma_2` be creation of a grandchild at `j-2` and `tau_2` elimination of both parent and child so that the half-line from `j-1` rightward is permanently coupled.

The next desired statement is a parameter-point contraction

$$
\mathbb P(\sigma_2<\tau_2)\le1-\delta_2(a,b,c),
\qquad \delta_2>0,
$$

or an exact obstruction. A positive number alone is insufficient: any surviving route must identify a restart state / finite renewal kernel that makes spatial composition legitimate.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard; the project factor-`2` variance bound and quotient-genealogy proof remain verified technical mathematics.

## Wiki freeze

The live wiki remains frozen during active research.
