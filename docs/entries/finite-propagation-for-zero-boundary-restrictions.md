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

Let $(P_t)_{t\ge0}$ be the semigroup of a uniformly bounded finite-range spin system on a [polynomial-growth lattice](polynomial-growth-lattice.md). For $R\Subset\Lambda$, let $P_t^{R,0}$ be the zero-boundary semigroup on $R$.

## Lemma

Let $A\Subset\Lambda$, and let $f$ be supported on $A$. For every $a>0$, there are $v<\infty$ and $C_A<\infty$ such that

$$
\|(P_t-P_t^{R,0})f\|_\infty
\le
C_Ae^{-at}\|f\|_\infty
\tag{1}
$$

for every $t\ge0$ and every $R\Subset\Lambda$ containing $B(A,vt)$. The speed $v$ may depend on $a$, but not on $t$ or $R$.

## Proof

Choose $\ell<\infty$ such that $c_i$ depends only on $B(i,\ell)$, and put

$$
\overline c=\sup_{i,\eta}c_i(\eta),
\qquad
m=\sup_i|B(i,\ell)|.
$$

Construct the process using rate-$\overline c$ candidate clocks and acceptance marks. Explore backward from $A$ at time $t$, adding $B(i,\ell)$ whenever a candidate clock at $i$ is encountered. If this influence cluster stays in $R$, the infinite-volume and zero-boundary processes, coupled with the same clocks and marks in $R$, agree on $A$ at time $t$.

To leave $B(A,r)$, the cluster must contain a chronological dependency path of length at least $n=\lceil r/\ell\rceil$. There are at most $|A|m^k$ spatial paths of length $k$, while the expected number of time-ordered $k$-tuples of rings along a fixed path is $(\overline c t)^k/k!$. Hence for every $\theta>0$,

$$
\mathbb P(\text{influence cluster leaves }B(A,r))
\le
|A|\exp\bigl(m\overline c\,t e^\theta-\theta n\bigr).
$$

Set $r=vt$ and choose $v$ so large that

$$
\frac{\theta v}{\ell}-m\overline c e^\theta\ge a.
$$

The graphical coupling then gives (1).

In the patch convergence proof this lemma controls the [spatial-confinement](undoing-duality-under-confined-interactions.md) error $\rho_A(T,R)$.
