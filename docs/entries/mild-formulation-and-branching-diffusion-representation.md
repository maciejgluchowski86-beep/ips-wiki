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

For a [heat-reference terminal PDE](heat-reference-fully-nonlinear-pde.md), Duhamel's formula propagates data exactly along heat-semigroup edges and inserts the nonlinearity only at integration times. A mild solution is a function satisfying this integral equation, whether or not all derivatives needed for a classical pointwise formulation are already known. [Branching diffusions](branching-diffusions-and-duhamel-trees.md) randomize the time integrals and, for polynomial nonlinearities, replace products by offspring.

**References.** Lawrence C. Evans, *Partial Differential Equations*, second edition, American Mathematical Society, 2010. Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, arXiv:1603.01727. Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, arXiv:2201.03882. D. Blömker, M. Romito, and R. Tribe, arXiv:math/0505449. See [References](../meta/references.md).

## Heat semigroup on the line

For \(r>0\), let

$$
p_r(x)
=
\frac{1}{\sqrt{2\pi r}}\exp\left(-\frac{x^2}{2r}\right)
$$

be the one-dimensional heat kernel. Define

$$
(P_rh)(x)
=
\int_{\mathbb R}p_r(y-x)h(y)\,dy
=
\mathbb E[h(x+B_r)],
\tag{1}
$$

where \(B_r\sim N(0,r)\). The family \((P_r)_{r\geq0}\) is the heat semigroup: \(P_0=\operatorname{Id}\), \(P_rP_s=P_{r+s}\), and for smooth \(h\),

$$
\partial_rP_rh
=
\frac12\partial_x^2P_rh.
\tag{2}
$$

## Heat semigroup on the torus

Let

$$
\mathbb T
=
\mathbb R/(2\pi\mathbb Z).
$$

A function on \(\mathbb T\) is identified with a \(2\pi\)-periodic function on \(\mathbb R\). The periodic heat kernel is

$$
p_r^{\mathbb T}(x,y)
=
\sum_{k\in\mathbb Z}
 p_r(y-x+2\pi k),
\tag{3}
$$

and

$$
(P_r^{\mathbb T}h)(x)
=
\int_0^{2\pi}p_r^{\mathbb T}(x,y)h(y)\,dy.
\tag{4}
$$

Equivalently, \(P_r^{\mathbb T}h(x)=\mathbb E[h(x+B_r\bmod 2\pi)]\). It has the same semigroup and generator identities as on the line. When no ambiguity arises, the superscript \(\mathbb T\) is suppressed.

## Duhamel formula

Let \(u\) be sufficiently smooth and solve

$$
\partial_tu+\frac12\partial_x^2u+f(J_nu)=0
$$

on \([0,T)\), with terminal condition \(u(T,\cdot)=\phi\). For every \(t\in[0,T]\), its value \(u(t,\cdot)\) is

$$
P_{T-t}\phi
+
\int_t^T P_{s-t}\bigl[f(J_nu(s,\cdot))\bigr]\,ds.
\tag{5}
$$

The formula is identical on \(\mathbb R\) and \(\mathbb T\), using the corresponding heat semigroup.

## Proof

For fixed \(t\), differentiate \(P_{s-t}u(s,\cdot)\) in \(s\). By (2),

$$
\frac{d}{ds}P_{s-t}u(s,\cdot)
=
P_{s-t}\left(\partial_su+\frac12\partial_x^2u\right)
=
-P_{s-t}[f(J_nu(s,\cdot))].
$$

Integrating from \(s=t\) to \(s=T\) and using \(u(T,\cdot)=\phi\) gives (5).

## Definition: mild solution

A function \(u\) is a *mild solution* of the terminal problem on a class where the terms are defined if its value \(u(t,\cdot)\) equals the expression in (5) for every \(t\in[0,T]\). This definition only uses the heat semigroup and the nonlinear expression inside the time integral. If a mild solution has enough regularity to differentiate the identity, then it is a classical solution of the PDE.

The mild formulation is often the natural starting point for probabilistic constructions because every heat transfer remains exact while only the nonlinear time integral is randomized.

## Heat-kernel edges and derivative transfer

A *heat-kernel edge* of duration \(r\) is the operation \(h\mapsto P_rh\). Probabilistically it transports a spatial location by an independent Brownian increment of variance \(r\).

For sufficiently regular \(h\), [Gaussian integration by parts](gaussian-integration-by-parts-and-automatic-differentiation.md) gives

$$
\partial_xP_rh(x)
=
\mathbb E\left[h(x+B_r)\frac{B_r}{r}\right].
\tag{6}
$$

The factor \(B_r/r\) is an automatic-differentiation weight of short-time size \(r^{-1/2}\). Higher derivatives produce [Hermite-polynomial weights](hermite-polynomials-and-gaussian-chaos.md).

## From the mild equation to branching

If a nonlinearity contains a monomial \(a_k u^k\), a branching event can produce \(k\) conditionally independent descendants. Their product reproduces the monomial, while reciprocal lifetime and offspring probabilities supply the [importance-sampling compensators](importance-sampling-compensators.md). Iterating this construction yields a Duhamel tree.

HLOTW use marked particles and automatic differentiation for nonlinearities involving \((u,Du)\). Nguwi--Penent--Privault instead carry differential operators as codes, avoiding a Malliavin weight on every derivative transfer. The exact branching recursion is separate from its moment estimates: a compensated tree can be algebraically unbiased and still fail to belong to \(L^1\).
