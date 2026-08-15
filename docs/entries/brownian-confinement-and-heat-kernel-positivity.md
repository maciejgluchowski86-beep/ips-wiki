---
title: Brownian confinement and heat-kernel positivity
status: standard fact
audit: current
tags:
  - probability
  - Brownian motion
  - heat kernel
  - PDE
  - lower bound
---

# Brownian confinement and heat-kernel positivity

This entry records two elementary positivity tools used in probabilistic PDE estimates: Brownian motion has positive probability to remain in a fixed bounded interval for a fixed finite time, and a Gaussian heat kernel has a uniform positive lower bound on compact spacetime sets separated from time zero.

**Prerequisite.** The normalization, positivity, periodization, and convolution properties of the kernel are fixed in [Heat equation and Gaussian heat kernel](heat-equation-and-gaussian-heat-kernel.md).

**References.** For Brownian passage times and confinement in a finite interval, see Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed., Springer, 1991, §2.8, especially the finite-interval passage-time computations. For the heat equation and its Gaussian kernel, see §4.3 of the same book. See [References](../meta/references.md).

## Brownian confinement

Let $(B_s)_{s\geq0}$ be standard one-dimensional Brownian motion with $B_0=0$. For every $t>0$ and $R>0$,

$$
\mathbb P\left(
\sup_{0\leq s\leq t}|B_s|<R
\right)>0.
\tag{1}
$$

Equivalently, if

$$
\tau_R
=\inf\{s\geq0:|B_s|\geq R\}
$$

is the first exit time from $(-R,R)$, then

$$
\mathbb P(\tau_R>t)>0.
\tag{2}
$$

The passage-time formulas for Brownian motion on a finite interval give (2) directly. Brownian scaling also gives

$$
\mathbb P(\tau_R>t)
=\mathbb P\left(\tau_1>\frac{t}{R^2}\right),
\tag{3}
$$

so the confinement probability depends on the fixed parameters through the ratio $t/R^2$.

## Strict and uniform heat-kernel positivity

For the normalization $\partial_tu=\frac12\partial_x^2u$, the Euclidean kernel is

$$
p_t(x,y)
=\frac1{\sqrt{2\pi t}}
\exp\left(-\frac{(y-x)^2}{2t}\right),
\qquad t>0.
\tag{4}
$$

It is continuous and strictly positive for every $t>0$ and $x,y\in\mathbb R$. The periodic kernel on $\mathbb T=\mathbb R/(2\pi\mathbb Z)$ is the periodization

$$
p_t^{\mathbb T}(x,y)
=\sum_{k\in\mathbb Z}p_t(x,y+2\pi k),
\tag{5}
$$

and is again continuous and strictly positive for every positive time.

Let $0<t_0\leq t_1<\infty$ and let $K,L\subset\mathbb R$ be compact. Continuity and strict positivity on the compact set $[t_0,t_1]\times K\times L$ imply

$$
\inf_{\substack{t\in[t_0,t_1]\\x\in K,\ y\in L}}
p_t(x,y)>0.
\tag{6}
$$

The same conclusion holds on the torus. The condition $t\geq t_0>0$ matters: for spatially separated points there is no positive lower bound of this form as $t\downarrow0$.

## Positive heat transfer

Let $\psi:\mathbb R\to\mathbb R$ be continuous and not identically zero. Since $|\psi|$ is bounded below by a positive number on some nonempty open interval and the heat kernel is strictly positive,

$$
P_t|\psi|(x)>0
\qquad
\text{for every }t>0,\ x\in\mathbb R.
\tag{7}
$$

If $K\subset\mathbb R$ is compact and $0<t_0\leq t_1$, continuity of $(t,x)\mapsto P_t|\psi|(x)$ then gives

$$
\inf_{\substack{x\in K\\t\in[t_0,t_1]}}
P_t|\psi|(x)>0.
\tag{8}
$$

Thus confinement and heat-kernel positivity provide constants depending only on the chosen finite horizon and compact regions.

## Application to a branching lineage

In a branching representation, a distinguished lineage is often built by concatenating independent Brownian increments between successive branch times. Conditional on the branch times, concatenating these increments gives the law of one Brownian path over the total elapsed time, so (1) supplies a fixed confinement probability for that lineage. If terminal heat transfers have remaining times in $[t_0,t_1]$ and spatial arguments in fixed compact sets, (6)--(8) supply fixed positive terminal factors. These constants do not depend on how many branch times were used to describe the selected lineage, which is the feature needed in [disjoint genealogical lower bounds](disjoint-event-lower-bounds-for-compensated-branching-estimators.md).
