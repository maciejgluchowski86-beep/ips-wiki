---
title: Brownian confinement and heat-kernel positivity
status: standard fact
tags:
  - probability
  - Brownian motion
  - heat kernel
  - PDE
  - lower bound
---

# Brownian confinement and heat-kernel positivity

Lower bounds for branching representations often require two elementary positivity facts. A Brownian path has positive probability to remain in a fixed spatial window for a fixed finite time, and the heat kernel is strictly positive. On compact spacetime sets away from time zero, strict positivity becomes a uniform positive lower bound.

These facts allow one to restrict a branching genealogy to a spatially controlled event without paying a depth-dependent zero factor, and then to lower-bound terminal heat transfers uniformly over the allowed branch positions.

**References.** These are standard Brownian-motion and heat-kernel facts; see, for example, Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*. The explicit Gaussian heat kernel also appears throughout the heat-semigroup entries of this wiki.

## Brownian confinement

Let \((B_s)_{s\geq0}\) be standard one-dimensional Brownian motion with \(B_0=0\). For every \(t>0\) and \(R>0\),

$$
\mathbb P\left(
\sup_{0\leq s\leq t}|B_s|<R
\right)
>0.
\tag{1}
$$

Equivalently, if

$$
\tau_R
=
\inf\{s\geq0:|B_s|\geq R\}
$$

is the first exit time from \((-R,R)\), then

$$
\mathbb P(\tau_R>t)>0.
\tag{2}
$$

One may prove this from the standard exit-time law for Brownian motion, from the killed heat kernel on an interval, or from the support of Wiener measure. Brownian scaling gives

$$
\mathbb P(\tau_R>t)
=
\mathbb P\left(
\tau_1>\frac{t}{R^2}
\right),
\tag{3}
$$

so only the ratio \(t/R^2\) matters.

For lower-bound arguments, the important point is simply that the number in (1) is strictly positive and depends only on the fixed window and time horizon, not on a later genealogy depth parameter.

## Concatenating Brownian increments along a lineage

Suppose a distinguished particle moves as Brownian motion until a branch time, after which one chosen child starts an independent Brownian increment from the parent's position. Repeating this operation along one lineage produces the same law as one Brownian path run for the total elapsed time.

More precisely, let

$$
0=s_0<s_1<\cdots<s_m
$$

and let \(B^{(1)},\ldots,B^{(m)}\) be independent standard Brownian motions. Define a continuous process by using \(B^{(j)}\) on the interval \([s_{j-1},s_j]\), translated to start from the endpoint of the previous piece. The resulting concatenated process has independent Gaussian increments with the correct variances and therefore has the law of standard Brownian motion on \([0,s_m]\).

Thus the confinement probability in (1) may be applied to a distinguished branching lineage even when the lineage is represented by independent Brownian pieces between successive branchings.

## The Gaussian heat kernel

For the heat equation with generator \(\frac12\partial_x^2\), the kernel on \(\mathbb R\) is

$$
p_t(x,y)
=
\frac1{\sqrt{2\pi t}}
\exp\left(
-\frac{(y-x)^2}{2t}
\right),
\qquad t>0.
\tag{4}
$$

It is continuous and strictly positive for every

$$
t>0,
\qquad
x,y\in\mathbb R.
$$

The heat semigroup is

$$
P_tf(x)
=
\int_{\mathbb R}p_t(x,y)f(y)\,dy
=
\mathbb E_x[f(B_t)].
\tag{5}
$$

The periodic heat kernel on \(\mathbb T\) is obtained by periodizing (4),

$$
p_t^{\mathbb T}(x,y)
=
\sum_{k\in\mathbb Z}
p_t(x,y+2\pi k),
\tag{6}
$$

and is again continuous and strictly positive for every \(t>0\).

## Uniform positivity on compact spacetime sets

Let

$$
0<t_0\leq t_1<\infty
$$

and let \(K,L\subset\mathbb R\) be compact. Since the function

$$
(t,x,y)
\longmapsto
p_t(x,y)
$$

is continuous and strictly positive on the compact set

$$
[t_0,t_1]\times K\times L,
$$

it has a strictly positive minimum there. Thus

$$
\inf_{\substack{t\in[t_0,t_1]\\x\in K,\ y\in L}}
p_t(x,y)
>0.
\tag{7}
$$

If \(B\subset\mathbb R\) is merely bounded, one may replace it by its compact closure in (7). The same statement holds on the torus.

The restriction \(t\geq t_0>0\) matters: no uniform lower bound of this form is available as \(t\downarrow0\) for spatially separated points.

## Positive heat transfer of a nonzero function

Let \(\psi:\mathbb R\to\mathbb R\) be continuous and not identically zero. Then

$$
P_t|\psi|(x)>0
\qquad
\text{for every }t>0,\ x\in\mathbb R.
\tag{8}
$$

Indeed, continuity and nontriviality imply that \(|\psi|\) is bounded below by a positive number on some nonempty open interval, and the strictly positive heat kernel assigns that interval positive mass from every starting point.

Moreover, if \(K\subset\mathbb R\) is compact and \(0<t_0\leq t_1\), then continuity of \((t,x)\mapsto P_t|\psi|(x)\) and (8) give

$$
\inf_{\substack{x\in K\\t\in[t_0,t_1]}}
P_t|\psi|(x)
>0.
\tag{9}
$$

This is the uniform side-branch lower bound used in many selected-genealogy arguments.

## Standard lower-bound pattern

Suppose a selected branching genealogy is restricted so that every distinguished branch position remains in a compact set \(K\), while every terminal transfer has a remaining heat time in \([t_0,t_1]\) with \(t_0>0\). Then:

1. Brownian confinement supplies a fixed positive probability for the spatial restriction;
2. equation (9) supplies a fixed positive lower bound for terminal factors of the form \(P_r|\psi|(z)\);
3. equation (7) supplies a fixed positive kernel lower bound for reaching a bounded target region.

All three constants depend on the chosen finite horizon and compact regions, but not on the number of branchings in the selected genealogy. This depth-uniformity is what makes the estimates useful in an infinite series of [disjoint genealogical lower bounds](disjoint-event-lower-bounds-for-compensated-branching-estimators.md).