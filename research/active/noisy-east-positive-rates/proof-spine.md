# Proof spine

## Main target

Prove ergodicity for the remaining noisy-East region of simple one-sided one-dimensional positive-rate IPS, ultimately completing the positive-rates conjecture for simple IPS.

**Programme status:** closed at Group Meeting 002 for the present finite-wall route. The target itself remains open.

## E0. Source-corrected residual noisy-East set

On the normalized face

$$
r_{11}=0,
$$

write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The proved 2025 sufficient regions relevant here include

$$
c<a+b,
\qquad
c<\frac12,
\qquad
0<b\le a
$$

(the last from published Corollary 7.2). The 2026 long-lived-state criterion additionally covers, on their complement,

$$
b<\sqrt2(1-c).
$$

Therefore the unresolved normalized set used by this programme is

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
1>c>b>a>0=r_{11}.
$$

The 2026 prose summary of the earlier covered region reverses the `a,b` inequality relative to the published 2025 Corollary 7.2. The proof spine uses the actual theorem statement and proof.

**Correction to the earlier spine:** the assignment-001 path

$$
a=\varepsilon,
\qquad b=\frac\varepsilon2,
\qquad c=1-\varepsilon^2
$$

is not unresolved; `b<a` places it in Corollary 7.2. Earlier E2/E3 statements calling it a genuine residual path are superseded.

## E1. One-site wall mechanism

The 2026 long-lived-state theorem proves ergodicity if

$$
\delta(s)<\sqrt2\,\beta(s).
$$

On `R`, state one has `beta(1)=0`, while for state zero

$$
\beta(0)=1-c,
\qquad
\delta(0)=b,
$$

and `b>=sqrt(2)(1-c)`. Hence the one-site criterion does not cover `R`.

**Status:** established prior-work obstruction.

## E2. Two-site diagnostic

Student C's exact two-site killed excursion on the assignment-001 path satisfies

$$
\rho_2(\varepsilon)\to1,
\qquad
F_2(\varepsilon)\to1.
$$

The finite-state algebra and deterministic East-limit mechanism were independently checked. However, after E0's source correction this path is already in the 2025 covered region.

**Status:** correct diagnostic calculation, but not target evidence about the unresolved residual.

## E3. Earlier length-three diagnostic

On the same already-covered path, the frozen-exterior length-three one-attack factor tends to `9/10` after maximizing over all agreed words and exterior orientations.

**Status:** correct diagnostic calculation; not evidence about `R` after the source correction.

## E4. Exact three-site characterization on the true residual

For `r in R`, define

$$
R_3^{\rm adv}(r)
$$

as the frozen-exterior unconditional one-attack crossing probability maximized over all eight fully agreed three-site words and both exterior disagreement orientations.

Student C proved, and the Professor independently reconstructed,

$$
\boxed{
\sup_{\bar r\in\partial_E\mathcal R}
\limsup_{\substack{r\to\bar r\\r\in\mathcal R}}
R_3^{\rm adv}(r)
=\frac56.
}
$$

The proof uses exact symbolic elimination on the nonzero East edge and a seven-class singular perturbation at the East corner. The value is sharp along

$$
a=\frac\varepsilon2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2.
$$

**Status:** Professor-checked target-relevant local theorem. Not registered as a project contribution because it concerns a local diagnostic that does not itself imply ergodicity.

## E5. Fatal obstruction for the present finite-wall concatenation

At every strict point of `R`, freeze an exterior disagreement forever. For any fixed finite agreed block, eventual crossing occurs almost surely.

Reason: every excursion either crosses or regenerates almost surely, and from every regenerated agreed word there is a fixed positive probability, depending on the parameter point, of crossing before the next regeneration. Strong Markov iteration makes survival through infinitely many regenerations probability zero.

Therefore `R_3^adv<1` controls only one attacked excursion. It is not an iteratable adversarial crossing probability.

A legitimate block-renewal theorem would need a stronger episode-level estimate controlling:

- the stochastic lifetime and evolution of the exterior disagreement source;
- repeated attacks during that lifetime;
- multiple nearby disagreements;
- block overlap and dependence; and
- episode-duration tails sufficient for temporal coupling.

No such estimate follows from E4, and no concrete closing inequality has been obtained.

**Status:** structural obstruction to the present finite-wall route.

## Pre-committed stop rule and closure

Meeting 001 stated in advance that, even if E4 produced a uniform gap, the finite-wall route would be abandoned if the frozen-exterior statistic could not be upgraded to dynamic domination without an uncontrolled stronger quantity.

E5 triggers that condition. There will be no move to block length four.

The source-episode object required after E5 is not treated as a routine extension of this proof spine. Without an independently motivated quantitative closure it would simply rename the missing mechanism.

## Programme conclusion

The present noisy-East finite-wall programme is closed without a qualifying new project result.

A future return requires a genuinely different mechanism or a separately motivated episode-level theorem with an actual tractable estimate. The positive-rates/noisy-East target remains open.
