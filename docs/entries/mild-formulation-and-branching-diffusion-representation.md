---
title: Mild formulation and branching-diffusion representation
status: standard fact
tags:
  - PDE
  - Duhamel formula
  - branching diffusion
  - Malliavin weight
  - heat semigroup
---

# Mild formulation and branching-diffusion representation

For a [heat-reference terminal PDE](heat-reference-fully-nonlinear-pde.md), Duhamel's formula propagates data exactly along heat-semigroup edges and inserts the nonlinearity only at integration times. Classical branching-diffusion representations randomize these time integrals and, for polynomial nonlinearities, replace products by offspring. Derivative nonlinearities require an additional mechanism for transferring spatial derivatives.

**References.** Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, arXiv:1603.01727; Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882; D. Blömker, M. Romito, and R. Tribe, *A probabilistic representation for the solutions to some non-linear PDEs using pruned branching trees*, arXiv:math/0505449; see [References](../meta/references.md).

## Definition

For \(r>0\), let

$$
p_r(x)=\frac{1}{\sqrt{2\pi r}}\exp\left(-\frac{x^2}{2r}\right)
$$

be the one-dimensional heat kernel, and define the heat semigroup

$$
(P_rh)(x)
=
\int_{\mathbb R}p_r(y-x)h(y)\,dy
=
\mathbb E[h(x+B_r)],
$$

where \(B_r\) is a centered Gaussian random variable of variance \(r\).

## Theorem

Let \(u\) be sufficiently smooth to justify the following operations and suppose

$$
\partial_tu+\frac12\partial_x^2u+f(J_nu)=0,
\qquad
u(T,\cdot)=\phi.
$$

Then \(u\) satisfies the mild or Duhamel equation

$$
u(t,\cdot)
=
P_{T-t}\phi
+
\int_t^T P_{s-t}\bigl[f(J_nu(s,\cdot))\bigr] \, ds.
\tag{1}
$$

## Proof

For fixed \(t\), differentiate \(P_{s-t}u(s,\cdot)\) with respect to \(s\). The heat-semigroup generator gives

$$
\frac{d}{ds}P_{s-t}u(s,\cdot)
=
P_{s-t}\left(\partial_su+\frac12\partial_x^2u\right)
=
-P_{s-t}[f(J_nu(s,\cdot))].
$$

Integrating from \(s=t\) to \(s=T\) and using \(u(T,\cdot)=\phi\) yields (1).

## Definition

A *heat-kernel edge* of duration \(r\) is the operation \(h\mapsto P_rh\). Probabilistically, it transports a spatial location by an independent Brownian increment of variance \(r\). In a branching representation, an edge remains a single exact heat transfer; branching randomizes the nonlinear products appearing in the Duhamel integrand.

For example, if a nonlinearity contains a monomial \(a_k u^k\), a branching event can produce \(k\) independent descendants and attach the coefficient \(a_k\), together with the reciprocal sampling probabilities needed for unbiasedness. The expectation of the product of descendant values then reproduces the corresponding product in the Duhamel equation.

## Definition

For sufficiently regular \(h\), Gaussian integration by parts gives the first-derivative transfer

$$
\partial_xP_rh(x)
=
\mathbb E\left[h(x+B_r)\frac{B_r}{r}\right].
\tag{2}
$$

The random factor \(B_r/r\) is a Malliavin or automatic-differentiation weight. Since \(B_r\) has size \(r^{1/2}\), the weight in (2) has the natural scale \(r^{-1/2}\).

## Known integrability limitation

Henry-Labordère--Oudjane--Tan--Touzi--Warin use marked particles and Malliavin integration by parts to represent polynomial nonlinearities involving \((u,Du)\). Their representation requires non-explosion and integrability conditions. Nguwi--Penent--Privault explicitly identify a further obstruction to extending the same repeated integration-by-parts mechanism to nonlinearities involving higher spatial derivatives: repeated Malliavin-type weights can fail to be integrable when several derivative transfers occur over short random lifetimes.

This is a limitation of the repeated-weight branching construction, not a statement that every probabilistic representation with derivative nonlinearities must fail. The [Nguwi--Penent--Privault coding tree](npp-coding-tree.md) avoids putting a Malliavin weight on every derivative transfer by carrying differential operators as codes instead.

When an unpruned tree functional is not integrable, Blömker--Romito--Tribe provide an earlier, different response in the semilinear setting: truncate or prune the branching tree and study convergence of the resulting approximate representations. This historical pruning construction is distinct from the coding-tree mechanism.
