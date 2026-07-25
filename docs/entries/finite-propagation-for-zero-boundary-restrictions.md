---
title: Finite propagation for zero-boundary restrictions
status: standard fact
tags:
  - spin systems
  - finite propagation
  - graphical construction
  - zero boundary
---

# Finite propagation for zero-boundary restrictions

A local observable cannot distinguish an infinite-volume finite-range spin system from a sufficiently distant zero boundary except on the event that its backward influence cluster reaches that boundary. Taking the boundary at distance proportional to time makes this error exponentially small, with an arbitrarily prescribed exponential rate if the proportionality constant is large enough.

Let \((P_t)_{t\ge0}\) be the semigroup of a uniformly bounded finite-range spin system on a [polynomial-growth lattice](polynomial-growth-lattice.md). For \(R\Subset\Lambda\), let \(P_t^{R,0}\) be its [zero-boundary semigroup](undoing-duality-under-confined-interactions.md#modified-and-zero-boundary-systems).

## Lemma

Let \(A\Subset\Lambda\), and let \(f\) be supported on \(A\). For every \(a>0\), there are \(v<\infty\) and \(C_A<\infty\) such that

$$
\left\|(P_t-P_t^{R,0})f\right\|_\infty
\le
C_Ae^{-at}\|f\|_\infty
\tag{1}
$$

for every \(t\ge0\) and every \(R\Subset\Lambda\) containing \(B(A,vt)\). The speed \(v\) may depend on \(a\), but not on \(t\) or \(R\).

## Proof

Choose \(\ell<\infty\) such that \(c_i\) depends only on \(B(i,\ell)\), and put

$$
\overline c=\sup_{i,\eta}c_i(\eta),
\qquad
m=\sup_i|B(i,\ell)|.
$$

Both constants are finite. Construct the process using rate-\(\overline c\) Poisson clocks and acceptance marks. Explore backward from \(A\) at time \(t\), adding \(B(i,\ell)\) whenever a candidate clock at \(i\) is encountered. If this influence cluster stays in \(R\), the infinite-volume process and the zero-boundary process, coupled with the same clocks and marks in \(R\), agree on \(A\) at time \(t\).

To leave \(B(A,r)\), the cluster must contain a chronological dependency path of at least \(n=\lceil r/\ell\rceil\) clock rings. There are at most \(|A|m^k\) spatial paths of length \(k\), while the expected number of time-ordered \(k\)-tuples of rings along a fixed path is \((\overline c t)^k/k!\). Hence, for every \(\theta>0\),

$$
\mathbb P\bigl(\text{the influence cluster leaves }B(A,r)\bigr)
\le
|A|\sum_{k\ge n}\frac{(m\overline c t)^k}{k!}
\le
|A|\exp\bigl(m\overline c\,t e^\theta-\theta n\bigr).
\tag{2}
$$

Set \(r=vt\), and choose \(v\) so large that

$$
\frac{\theta v}{\ell}-m\overline c\,e^\theta\ge a.
$$

The probability in (2) is then at most \(|A|e^{-at}\). The graphical coupling gives

$$
\left|(P_t-P_t^{R,0})f(\eta)\right|
\le
2\|f\|_\infty\,
\mathbb P\bigl(\text{the influence cluster leaves }R\bigr),
$$

uniformly in \(\eta\). Since \(B(A,vt)\subseteq R\), this proves (1).
