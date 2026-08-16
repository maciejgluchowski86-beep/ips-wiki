---
title: Patch positivity property
status: proved here
audit: current
tags:
  - duality
  - spin systems
  - patch
  - positivity
---

# Patch positivity property

A spin system is **patch positive** when

$$
C(P)\ge0
$$

for every possible full patch shape $P$. The canonical paper gives an exact coefficient criterion.

Put

$$
r_i=c_i^0(\vn)+c_i^1(\vn).
$$

## Coefficient criterion

At a site $i$ with $r_i=0$, patch positivity holds exactly when

$$
c_i\equiv0.
$$

At a site with $r_i>0$, patch positivity holds exactly when, for every nonempty $S\subseteq N(i)$,

$$
c_i^0(S)+c_i^1(S)\le0,
\tag{1}
$$

and

$$
c_i^1(\vn)c_i^0(S)
\ge
c_i^0(\vn)c_i^1(S).
\tag{2}
$$

The first inequality is forced by $\mathsf{OO}$ patches. For $\mathsf{OI}$ and $\mathsf{OE}$ patches, the relevant numerator is

$$
c_i^0(S)
-
\bigl(c_i^0(S)+c_i^1(S)\bigr)\psi_i(\Delta,1).
$$

Under (1), this is minimized in the long-patch limit, where nonnegativity is exactly (2). Incoming-initial patch contributions are automatically nonnegative.

## Consequence for local rates

Patch positivity implies that $c_i^1$ and $c_i^0+c_i^1$ are coordinatewise nonincreasing as $1$'s are added to the neighbourhood of $i$. This is weaker than patch positivity: coordinatewise monotonicity alone does not imply (1)-(2).

For a fixed neighbourhood configuration with positive total flip intensity, the local rates can be viewed as a Bernoulli refresh. Replacing $0$-neighbours by $1$-neighbours cannot increase either the refresh intensity or the $1\to0$ transition rate. The full flip rate $c_i^0$ itself need not be monotone.

Patch positivity controls full-patch factors. Nonnegativity of end factors additionally depends on the terminal calm-state density and is encoded by the [patch threshold profile](patch-critical-density.md).
