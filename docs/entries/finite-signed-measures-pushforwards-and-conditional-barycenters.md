---
title: Finite signed measures, pushforwards, and conditional barycenters
status: standard fact
audit: current
tags:
  - measure theory
  - probability
  - signed measure
  - total variation
  - conditional expectation
  - importance sampling
  - PDE
---

# Finite signed measures, pushforwards, and conditional barycenters

Signed random contributions are often easier to compare at the level of finite signed measures than at the level of one particular sampling proposal. Pushforward and conditional expectation describe exactly how total variation changes when information is forgotten.

## Signed measures and total variation

Let $(\Omega,\mathcal F)$ be a measurable space. A finite signed measure has a Jordan decomposition $\mu=\mu^+-\mu^-$. Its total-variation measure is $|\mu|=\mu^++\mu^-$ and

$$
\|\mu\|_{\mathrm{TV}}=|\mu|(\Omega).
\tag{1}
$$

Equivalently,

$$
\|\mu\|_{\mathrm{TV}}
=
sup\left\{\sum_{j=1}^m|\mu(A_j)|:
\Omega=\bigsqcup_{j=1}^mA_j\right\},
\tag{2}
$$

where the supremum is over finite measurable partitions. Hence $|\mu(\Omega)|\leq\|\mu\|_{\mathrm{TV}}$.

If $\mu\ll\nu$ for a finite positive measure $\nu$ and $R=d\mu/d\nu$, then

$$
\|\mu\|_{\mathrm{TV}}=\int|R|\,d\nu.
\tag{3}
$$

## Pushforward

For a measurable map $\mathcal C:\Omega\to Y$, define

$$
(\mathcal C_\#\mu)(B)=\mu(\mathcal C^{-1}(B)).
$$

Total mass is preserved, while total variation is contractive:

$$
\|\mathcal C_\#\mu\|_{\mathrm{TV}}
\leq
\|\mu\|_{\mathrm{TV}}.
\tag{4}
$$

This follows by pulling a finite partition of $Y$ back to one of $\Omega$. If $\mathcal C$ is a measurable bijection onto its image with measurable inverse, equality holds. If $\mathcal C$ is constant, the pushforward has one atom of signed mass $\mu(\Omega)$ and therefore variation $|\mu(\Omega)|$.

Thus strict contraction is possible only when positive and negative mass that were distinguished in the raw space are merged in the retained space.

## Conditional barycenter

Let $\mu=R\nu$ with $\nu$ finite positive and $R\in L^1(\nu)$. For a sub-sigma-field $\mathcal G\subseteq\mathcal F$, conditional Jensen gives

$$
\int\left|\mathbb E_\nu[R\mid\mathcal G]\right|\,d\nu
\leq
\int|R|\,d\nu.
\tag{5}
$$

If $\mathcal G_1\subseteq\mathcal G_2$, the tower property yields

$$
\int\left|\mathbb E_\nu[R\mid\mathcal G_1]\right|\,d\nu
\leq
\int\left|\mathbb E_\nu[R\mid\mathcal G_2]\right|\,d\nu.
\tag{6}
$$

When $\mathcal G=\sigma(\mathcal C)$, the density of the pushed-forward signed measure with respect to the pushed-forward reference measure is represented by this conditional barycenter. Formula (5) is therefore the density form of (4).

Strictness in (5) is a separate question. Equality holds, for example, when the sign of $R$ is already $\mathcal G$-measurable; a strict contraction requires cancellation inside at least some conditional fibers.

## Importance sampling and first absolute moments

Let $Q$ be a probability measure dominating $\mu$. The canonical importance-sampling weight $W=d\mu/dQ$ satisfies

$$
\mathbb E_QW=\mu(\Omega),
\qquad
\mathbb E_Q|W|=\|\mu\|_{\mathrm{TV}}.
\tag{7}
$$

Thus changing the positive proposal does not change the first absolute moment associated with a fixed signed measure.

If an estimator $Y$ uses extra auxiliary randomness and satisfies

$$
\mathbb E_Q[Y\mid U]=W(U),
$$

then conditional Jensen implies

$$
\mathbb E_Q|Y|\geq\mathbb E_Q|W|.
\tag{8}
$$

Conditionally unbiased auxiliary randomization cannot beat the total-variation cost of the retained signed measure. A genuine $L^1$ improvement must therefore change the retained signed measure by an exact coarsening or cancellation operation, rather than merely resample the same measure.

## Nonatomic positive measures

A finite positive measure $\lambda$ is nonatomic if it has no atom of positive mass. The standard divisibility theorem implies that if $\lambda(A)>0$ and $0<\varepsilon<\lambda(A)$, then some measurable $B\subseteq A$ satisfies $0<\lambda(B)\leq\varepsilon$; in fact every value in $[0,\lambda(A)]$ can be attained.

If $\mu=R\nu$ and $\nu$ is nonatomic, then $|\mu|=|R|\nu$ is nonatomic as well. This is useful when signed measures are built from continuous time or Gaussian coordinates.

## Use in probabilistic representations

A raw marked contribution may define a signed measure $\mu$ on all sampled variables. Retaining only a coarser state corresponds to a pushforward $\mathcal C_\#\mu$, whose total variation is the exact $L^1$ cost of its canonical Radon--Nikodym estimator. Equations (4)--(8) separate two questions: whether an exact coarsening truly removes signed variation, and whether any resulting gain is preserved when several contributions are composed.

**Further reading.** These statements are standard consequences of the Jordan decomposition, Radon--Nikodym theorem, conditional Jensen inequality, and the divisibility theorem for nonatomic finite measures. See also [Importance-sampling compensators](importance-sampling-compensators.md) and [Total variation, bounded variation, and derivative singularities](total-variation-bounded-variation-and-derivative-singularities.md).
