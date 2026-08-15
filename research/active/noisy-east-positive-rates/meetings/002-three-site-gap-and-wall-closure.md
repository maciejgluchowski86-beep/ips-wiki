# Group meeting 002: sharp three-site gap, source correction, and wall-route closure

Date: 2026-08-16

Professor review of Graduate Student C assignment 002:

- `students/student-c/002-uniform-three-site-wall.md`, commit `c458f9f`;
- `students/student-c/002-uniform-three-site-wall-verifier.py`, commit `39a37ee`;
- independent Professor reconstruction `notes/professor-uniform-three-site-review.md`.

state_narrowed: yes

Evidence pointer: the Student C report and exact verifier above, together with `notes/professor-uniform-three-site-review.md`. The source correction is grounded in the published 2025 Corollary 7.2 and the 2026 long-lived-state theorem.

## Source correction

The previous programme record mislabeled the assignment-001 path as lying in the unresolved noisy-East region.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The published 2025 Corollary 7.2 covers `0<b<=a`. Combining the complements of the relevant 2025 sufficient regions with the 2026 long-lived-state criterion gives the actual unresolved set

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

Thus the assignment-001 path

$$
a=\varepsilon,\qquad b=\frac\varepsilon2,\qquad c=1-\varepsilon^2
$$

is already covered by the 2025 theorem because `b<a`. Its finite-state calculations remain correct as calculations, but they are diagnostics on a proved parameter path and cannot be used as evidence about the unresolved residual.

The 2026 paper contains a prose summary of the 2025 covered region with the opposite `a,b` inequality. The programme now follows the published 2025 theorem statement and proof rather than that inconsistent summary sentence.

## Sharp length-three characterization

For the true residual set, define `R_3^adv(r)` as the frozen-exterior unconditional one-attack crossing probability maximized over all eight fully agreed three-site words and both exterior disagreement orientations.

Student C proves, and the Professor independently reconstructed,

$$
\boxed{
\sup_{\bar r\in\partial_E\mathcal R}
\limsup_{\substack{r\to\bar r\\r\in\mathcal R}}
R_3^{\rm adv}(r)=\frac56.
}
$$

The proof has two exact pieces.

For fixed nonzero East-edge points `(a,b,c)=(0,b,1)`, exact elimination of the 24-state chain and polynomial positivity after a Mobius change of variables give every one-attack factor at most `5/6`.

At the singular corner, write

$$
\alpha=\frac ab,
\qquad
\gamma=\frac{1-c}{b}.
$$

The residual inequalities compactify these ratios to

$$
0\le\alpha\le1,
\qquad
0\le\gamma\le\frac1{\sqrt2}.
$$

The exact seven-class stochastic-complement reduction gives for the maximizing all-one word

$$
\frac56-L_{111}(\alpha,\gamma)
=
\frac{\gamma P(\alpha,\gamma)}{3D(\alpha,\gamma)}
\ge0,
$$

where `P,D` have positive coefficients. The all-one word dominates the other nonvanishing words. Equality is attained when `gamma=0`; the genuine residual sequence

$$
a=\frac\varepsilon2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2
$$

therefore gives the sharp `5/6` limit.

This solves the bounded assignment-002 characterization. It is not registered as a project result: it is a theorem about an artificial one-attack diagnostic and does not by itself imply any new ergodicity statement.

## The pre-committed dynamic-exterior condition fails

The uniform `5/6` gap does not concatenate.

At any strict residual parameter point, if an exterior disagreement is held forever, repeated attacks penetrate every fixed finite agreed block almost surely. After each regeneration there is a uniformly positive, state-dependent probability of crossing before the next regeneration; the strong Markov property makes survival through infinitely many regenerations probability zero.

Therefore replacing the true exterior by a permanently adversarial off-diagonal state turns the eventual block-crossing probability into one. The one-attack statistic `R_3^adv` cannot be the sole hypothesis of a valid block-renewal theorem.

A valid proof would need a strictly stronger episode-level object that controls the random lifetime and evolution of the exterior disagreement source, the number and timing of repeated attacks, overlaps, and episode duration. Assignment 002 does not reduce that object to the `5/6` theorem and has no uniform episode estimate.

Meeting 001 explicitly pre-committed to close the finite-wall route in exactly this situation: a local frozen-exterior gap exists but cannot be upgraded to dynamic domination without introducing an uncontrolled stronger quantity.

## Direction decision

**close the finite-wall route and close the present noisy-East programme.**

There will be no length-four calculation.

This is an opportunity-cost decision, not a theorem that all finite or spacetime block methods fail. The programme's concrete tractability advantage was the finite-wall mechanism. That mechanism is now understood well enough to know that its one-attack contraction is not the relevant iteratable quantity, while the required source-episode process is a new unresolved stochastic problem with no closing estimate currently in hand.

Keeping the same programme alive by renaming that uncontrolled episode process would defeat the pre-committed stop rule. A future return to noisy East requires a genuinely new mechanism or a separately motivated episode theorem with an actual quantitative closure.

The programme closes without a qualifying new project result under the standing novelty standard. The exact `5/6` characterization and the repeated-attack obstruction are retained as useful negative/diagnostic mathematics.

## Next scientific direction

Reopen the opportunity-cost list from Graduate Student A's reconnaissance. The next candidate is the explicit open concentration problem for discordant edges in the voter model on random regular graphs, where the published authors ask for sharp `sqrt(t/n)` concentration throughout sublinear times `t=o(n)`.

Before substantial development, initialize that as a genuinely new programme and give a new persistent student a bounded first task aimed at the load-bearing integrated-drift/correlation obstruction, not at a sequence of quantitative time-window extensions.

Graduate Student C becomes idle with the noisy-East lineage.

## Wiki

Keep the live-wiki freeze in force. There is no new noisy-East theorem suitable for `proved here` promotion.
