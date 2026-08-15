# Professor verification: residual correction, sharp three-site boundary factor, and finite-wall stop

Date: 2026-08-16

Source under review:

- `students/student-c/002-uniform-three-site-wall.md`, commit `c458f9f`;
- `students/student-c/002-uniform-three-site-wall-verifier.py`, commit `39a37ee`.

This note records the Professor's independent checks of the source-level residual set, the sharp `5/6` East-boundary theorem for the frozen-exterior one-attack statistic, and the repeated-attack obstruction.

## 1. Source correction: the assignment-001 path was not unresolved

On the normalized face

$$
r_{11}=0,
$$

write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The published 2025 paper, *Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems*, gives the following sufficient regions relevant on this face:

- `c<a+b`;
- `c<1/2`;
- Corollary 7.2: `0<b<=a` together with the positive-rate/order hypotheses.

The last inequality was rechecked in the published version and in its proof via the alternating-site state flip and Gray's weak-monotonicity theorem. Therefore the assignment-001 path

$$
a=\varepsilon,\qquad b=\frac\varepsilon2,\qquad c=1-\varepsilon^2
$$

lies on an already-proved side because `b<a`. The two-site and three-site finite-state calculations on that path remain algebraically correct, but the previous repository description of it as a genuine residual path was false.

The 2026 long-lived-state theorem gives ergodicity when

$$
\delta(s)<\sqrt2\,\beta(s).
$$

On the complement of the 2025 regions we have `a<b` and `c>=a+b>b`, so for state zero

$$
\beta(0)=1-c,
\qquad
\delta(0)=b.
$$

State one has `beta(1)=0` on `r11=0`. Thus the remaining normalized unresolved set obtained from the proved theorem statements is

$$
\boxed{
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
}
$$

In particular

$$
1>c>b>a>0=r_{11}
$$

throughout `R`.

The 2026 paper's prose summary of the earlier region reverses the `a,b` inequality relative to the published 2025 Corollary 7.2. For programme state, theorem statements and their proofs take precedence over that summary sentence.

## 2. Independent check of the sharp `5/6` theorem

For `r in R`, let

$$
R_3^{\rm adv}(r)
$$

be the maximum unconditional one-attack crossing probability for the frozen-exterior three-site killed excursion, over all eight fully agreed words and both exterior disagreement orientations.

I independently reconstructed the 24-state killed chain from the canonical coupling.

### Fixed nonzero East edge

At

$$
a=0,\qquad c=1,\qquad 0<b\le1,
$$

the 24-state hitting system is nonsingular. Direct symbolic elimination gives rational functions for the eight one-attack factors. After the Mobius change of variables

$$
b=\frac{x}{1+x},\qquad x\ge0,
$$

the correctly signed denominator and every numerator of

$$
\frac56-F_w(0,b,1)
$$

have nonnegative coefficients, with the required strict positivity. In particular all eight factors are at most `5/6`. The all-one word satisfies

$$
\lim_{b\downarrow0}F_{111}(0,b,1)=\frac56.
$$

Copy-label exchange gives the same values for the opposite exterior orientation.

### Singular corner

For sequences in `R` with `b->0`, set

$$
\alpha=\frac ab,
\qquad
\gamma=\frac{1-c}{b}.
$$

The residual inequalities force

$$
0\le\alpha\le1,
\qquad
0\le\gamma\le\frac1{\sqrt2}
$$

after compactification. Reconstructing the 26-state transition matrix and eliminating the zero-order transient states gives the same seven-class effective generator recorded by Student C.

For the maximizing all-one word the limiting factor satisfies the exact identity

$$
\frac56-L_{111}(\alpha,\gamma)
=
\frac{\gamma}{3D(\alpha,\gamma)}P(\alpha,\gamma),
$$

where `D` and `P` have strictly positive coefficients on the compact rectangle. Hence

$$
L_{111}(\alpha,\gamma)\le\frac56,
$$

with equality exactly at `gamma=0`. The differences `L_111-L_w` for the other words ending in one also have positive-coefficient numerators; words ending in zero have attack probability `(1-alpha)b` and vanish in the corner limit.

Therefore every sequence in `R` approaching the East edge has adversarial limsup at most `5/6`. The genuine residual sequence

$$
a=\frac\varepsilon2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2
$$

has `alpha=1/2` and `gamma=epsilon->0`, so it attains the bound. Thus

$$
\boxed{
\sup_{\bar r\in\partial_E\mathcal R}
\limsup_{\substack{r\to\bar r\\r\in\mathcal R}}
R_3^{\rm adv}(r)=\frac56.
}
$$

This is valid target-relevant mathematics, but it is a local diagnostic statistic rather than an ergodicity theorem and is not registered as a project contribution.

## 3. Repeated attacks: the one-attack factor cannot concatenate

Fix any strict point of the chamber `c>b>a>0` and hold one exterior disagreement forever. For any fixed finite agreed block, eventual crossing occurs with probability one.

First, from every transient block state there is a finite positive-probability update sequence to a fully agreed state: update from right to left and use the common-zero part of the canonical coupling. Strict positive rates and `c<1` make the required probabilities positive. Since the transient block state space is finite, every excursion is absorbed by crossing or regeneration almost surely.

Second, from every fully agreed word there is a finite positive-probability path that crosses before the next regeneration: create an all-one agreed word, make a boundary attack, then propagate the off-diagonal state from right to left. Every required probability is strictly positive in `c>b>a>0`. Because there are finitely many agreed words, for fixed `r` there is a common lower bound `p(r)>0` on crossing before the next regeneration.

At successive regeneration times the strong Markov property therefore gives

$$
\mathbf P(\text{survive }n\text{ regenerations without crossing})
\le(1-p(r))^n\longrightarrow0.
$$

So a permanently adversarial exterior has eventual crossing probability one for every fixed block length.

Consequently a theorem whose only local input is `R_3^adv<1` cannot yield disagreement extinction. A valid argument would have to introduce a strictly stronger episode-level object controlling the stochastic lifetime and evolution of the exterior source, repeated attacks, overlaps, and episode duration. No such domination has been proved or reduced to the `5/6` statistic.

## 4. Direction consequence

Meeting 001 pre-committed to abandon the finite-wall route even in the uniform-gap case if the frozen-exterior statistic could not be upgraded to a rigorous dynamic domination without an uncontrolled stronger quantity.

The repeated-attack proposition triggers that condition. The required source-episode process is not a technical repair of the one-attack argument; it is a new stochastic object for which the present finite-state calculation supplies no closing estimate. There will be no move to block length four.

The finite-wall route is therefore closed. Since this route was the concrete tractability reason for selecting the noisy-East programme and no comparably concrete alternative mechanism is presently available, the Professor closes the noisy-East programme on expected-value grounds rather than relabeling the episode process as another wall variant.

A future return to noisy East requires a genuinely new mechanism or a separately motivated episode-level theorem with an actual quantitative closure, not another fixed-block calculation.
