---
title: Finite propagation for zero-boundary restrictions
status: standard fact
audit: current
tags:
  - spin systems
  - finite propagation
  - graphical construction
  - zero boundary
---

# Finite propagation for zero-boundary restrictions

A local observable cannot distinguish an infinite-volume finite-range spin system from a sufficiently distant zero boundary unless its backward influence cluster reaches that boundary. Taking the boundary at distance proportional to time makes this error exponentially small, with any prescribed exponential rate after choosing the proportionality constant sufficiently large.

Let $(P_t)_{t\ge0}$ be the semigroup of a uniformly bounded finite-range spin system. Let

$$
\overline c
=
\sup_{i\in\Lambda,\eta}c_i(\eta)
<\infty,
$$

and put

$$
m
=
\sup_{i\in\Lambda}|N(i)\cup\{i\}|
<\infty.
$$

For $R\Subset\Lambda$, let $P_t^{R,0}$ be the zero-boundary semigroup on $R$. No polynomial-growth assumption is needed for this lemma.

## Lemma

Let $f$ be supported on $A\Subset\Lambda$. For every $a>0$, there are $v<\infty$ and $C_A<\infty$ such that

$$
\|(P_t-P_t^{R,0})f\|_\infty
\le
C_Ae^{-at}\|f\|_\infty
\tag{1}
$$

for every $t\ge0$ and every finite $R$ containing

$$
B(A,\lceil vt\rceil).
$$

The speed $v$ may depend on $a$, but not on $t$ or on $R$.

## Proof

Construct the process from rate-$\overline c$ candidate clocks at each site and independent acceptance marks. Explore the graphical construction backward from the sites in $A$ at time $t$. Whenever a candidate clock at a site $i$ is encountered, add the sites in

$$
N(i)\cup\{i\}
$$

to the set of spins whose earlier values must be determined. This gives the backward influence cluster of $A$ at time $t$.

Couple the infinite-volume process and the zero-boundary process by using the same clocks and acceptance marks inside $R$. If the backward influence cluster stays inside $R$, the two processes see exactly the same graphical information needed to determine the spins on $A$ at time $t$. Hence they agree on the support of $f$ at that time.

To leave $B(A,n)$, the influence cluster must contain a chronological dependency path with at least $n$ candidate clocks. For a path of length $k$, there are at most

$$
|A|m^k
$$

possible spatial sequences. Along any fixed spatial path, the expected number of chronologically ordered $k$-tuples of rate-$\overline c$ clock rings in $[0,t]$ is

$$
\frac{(\overline c t)^k}{k!}.
$$

Therefore

$$
\mathbb P\bigl(\text{influence cluster leaves }B(A,n)\bigr)
\le
|A|\sum_{k\ge n}\frac{(m\overline c t)^k}{k!}.
\tag{2}
$$

For every $\theta>0$,

$$
\sum_{k\ge n}\frac{x^k}{k!}
\le
e^{-\theta n}\sum_{k\ge0}\frac{(xe^\theta)^k}{k!}
=
\exp(xe^\theta-\theta n).
$$

Applying this to (2) gives

$$
\mathbb P\bigl(\text{influence cluster leaves }B(A,n)\bigr)
\le
|A|\exp\bigl(m\overline c\,t e^\theta-\theta n\bigr).
\tag{3}
$$

Take

$$
n=\lceil vt\rceil
$$

and choose $v$ so that

$$
\theta v-m\overline c e^\theta>a.
$$

After increasing the multiplicative constant to cover bounded values of $t$, (3) is at most $C_Ae^{-at}$.

On the coupling event that the influence cluster stays inside $R$, the two processes give the same value of $f$. Thus

$$
|P_tf(\eta)-P_t^{R,0}f(\eta)|
\le
2\|f\|_\infty
\mathbb P(\text{influence cluster leaves }R)
$$

uniformly in $\eta$. This proves (1).

## Consequences used by the patch paper

For fixed $t$ and local $f$, zero-boundary semigroups converge uniformly to the infinite-volume semigroup along any exhaustion whose boundary recedes from the dependence set of $f$. This is the approximation used to pass positivity of the finite-volume centered-monomial semigroup to infinite volume in [centered-moment order preservation](monomial-monotonicity-for-high-density-measures.md).

Taking $f=\chi_A$ and $a=\varepsilon$ gives a linearly growing region $R_T$ with

$$
\|(P_T-P_T^{R_T,0})\chi_A\|_\infty
\le
C_Ae^{-\varepsilon T},
$$

which is the [spatial-confinement](undoing-duality-under-confined-interactions.md) error used in the common invariant-limit proof. Polynomial growth enters only after this step, to control $|R_T|$.
