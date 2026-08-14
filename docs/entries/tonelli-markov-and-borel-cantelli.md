---
title: Tonelli, Markov, and Borel-Cantelli
status: standard fact
audit: current
tags:
  - probability
  - measure theory
  - integrability
---

# Tonelli, Markov, and Borel-Cantelli

Several PDE branching arguments on this wiki reduce to elementary measure-theoretic steps: Tonelli's theorem exchanges nonnegative integrals, Markov's inequality turns an integral bound into a measure estimate, and the first Borel--Cantelli lemma converts summable exceptional-set measures into an almost-everywhere eventual statement. These results are part of standard measure-theoretic probability; they are recorded here to make the proof dependencies explicit.

**References.** Any graduate measure-theoretic probability text contains these results. The formulations below are for a general measure space and therefore apply both to probability measures and to Lebesgue measure.

## Tonelli's theorem

Let $(X,\mu)$ and $(Y,\nu)$ be sigma-finite measure spaces, and let $f:X\times Y\to[0,\infty]$ be measurable. Then

$$
\int_{X\times Y}f\,d(\mu\otimes\nu)
=
\int_X\left(\int_Yf(x,y)\,d\nu(y)\right)d\mu(x)
=
\int_Y\left(\int_Xf(x,y)\,d\mu(x)\right)d\nu(y),
\tag{1}
$$

with the value $+\infty$ allowed.

The permission to take the value $+\infty$ is often the important point. For example, if $A_m\subseteq X$ are measurable, then Tonelli applied to

$$
f(y,m)=\ind(A_m)(y)
$$

gives

$$
\int_X\sum_{m\geq1}\ind(A_m)(y)\,d\mu(y)
=
\sum_{m\geq1}\mu(A_m).
\tag{2}
$$

No prior summability assumption is needed.

## Markov's inequality

If $F\geq0$ is measurable and $a>0$, then

$$
\mu\{F>a\}
\leq
\frac1a\int F\,d\mu.
\tag{3}
$$

For a probability measure this is the usual probabilistic Markov inequality. The same estimate applies to Lebesgue measure on a bounded set and is often used to turn integral derivative bounds into exceptional-set estimates.

## First Borel--Cantelli lemma

Let $(A_m)$ be measurable events in a probability space. If

$$
\sum_{m=1}^\infty\mathbb P(A_m)<\infty,
$$

then

$$
\mathbb P(A_m\text{ infinitely often})=0.
\tag{4}
$$

Independence is not required for this direction.

The same statement holds on a finite-measure space after normalizing the measure. Equivalently, if $B$ has finite measure and

$$
\sum_m|A_m|<\infty,
\qquad A_m\subseteq B,
$$

then almost every point of $B$ belongs to only finitely many $A_m$.

## Two reusable patterns

**Positive-measure limsup.** If every point of a set $E_0$ of positive measure belongs to infinitely many $A_m$, then the left side of (2) is infinite on $E_0$, so

$$
\sum_m|A_m|=\infty.
$$

This is a generic way to turn pointwise recurrence of exceptional events into divergence of their total measure.

**Almost-everywhere eventual bound.** If Markov's inequality gives

$$
|A_m|\leq2^{-m},
$$

then the exceptional measures are summable, and Borel--Cantelli implies that almost every point lies in only finitely many $A_m$. Hence any property holding outside $A_m$ at level $m$ holds eventually for almost every point.