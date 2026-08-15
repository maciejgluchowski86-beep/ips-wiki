# Literature and prior-work record

## Target literature

### Głuchowski--Menz (2025)

*Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems*, Journal of Statistical Physics 192 (2025), article 6.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The published theorem statements used by this programme cover, among other relevant regions,

$$
c<a+b,
\qquad
c<\frac12,
$$

and Corollary 7.2 covers

$$
0<b\le a
$$

under its stated order/positive-rate hypotheses. The direction `b<=a` is also used in the proof after the alternating-site state flip and application of Gray's weak-monotonicity theorem.

### Głuchowski--Menz (2026)

*Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*, Electronic Communications in Probability 31 (2026), DOI `10.1214/26-ECP767`, arXiv `2508.08459`.

The theorem gives ergodicity when, for some state `s`,

$$
\delta(s)<\sqrt2\,\beta(s).
$$

On the complement of the 2025 regions above, `a<b` and `c>=a+b>b`. Hence on `r11=0`, state zero has

$$
\beta(0)=1-c,
\qquad
\delta(0)=b,
$$

while state one has `beta(1)=0`. The 2026 theorem therefore additionally covers

$$
b<\sqrt2(1-c).
$$

### Source inconsistency and corrected residual set

The 2026 paper contains a prose summary of the 2025 covered region with the opposite `a,b` inequality from the published 2025 Corollary 7.2. No correction notice was found during assignment 002. For mathematical state, this programme follows the actual published theorem statement and proof.

Combining the complements of the proved sufficient regions gives the normalized unresolved set

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

Thus

$$
1>c>b>a>0=r_{11}
$$

throughout `R`.

The assignment-001 path

$$
a=\varepsilon,
\qquad b=\frac\varepsilon2,
\qquad c=1-\varepsilon^2
$$

is not unresolved: `b<a` places it in the 2025 Corollary 7.2 region. Earlier repository wording to the contrary is corrected in Meeting 002 and the Professor notes.

## Programme result from source comparison

Assignment 002's target-relevant calculations are performed on the true residual set above. The sharp frozen-exterior three-site East-boundary factor is `5/6`, but repeated attacks under a permanently present exterior disagreement penetrate every fixed finite block almost surely. Therefore the local one-attack statistic does not itself supply a block-renewal theorem.

The finite-wall programme closed at Group Meeting 002 under the pre-committed dynamic-exterior stop rule.

## Open-status record

The 2026 paper states that its criterion narrows the unresolved simple positive-rate systems to noisy versions of East. No later resolution was found in the programme's targeted successor search through 2026-08-16.

The broader positive-rates/noisy-East problem remains open; only the present finite-wall programme is closed.
