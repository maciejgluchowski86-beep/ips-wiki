---
title: Mild formulation and branching-diffusion representation
status: standard fact
audit: current
tags:
  - PDE
  - Duhamel formula
  - branching diffusion
  - diffusion semigroup
---

# Mild formulation and branching-diffusion representation

A mild formulation separates linear propagation from the forcing or nonlinearity through a variation-of-constants identity. Branching diffusions are one possible randomization of repeated nonlinear Duhamel integrals, but the generic mild identity is much broader than any one branching theorem.

**Prerequisite.** For the constant-coefficient heat operator and the notation $P_t$, see [Heat equation and Gaussian heat kernel](heat-equation-and-gaussian-heat-kernel.md).

**References.** Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010, for the heat equation and Duhamel principle. Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* **55** (2019), no. 1, 184--210, especially Sections 2--3, Assumption 3.10, and Theorem 3.12. See [References](../meta/references.md).

## Duhamel identity

Let $(P_{t,s})_{0\leq t\leq s\leq T}$ be the transition family associated with a linear backward operator $L_t$. Consider a terminal problem

$$
\partial_tu+L_tu+F(t,x)=0,
\qquad
u(T,\cdot)=g,
$$

where the displayed terms are defined in the function class under consideration. Variation of constants gives the identity

$$
u(t,\cdot)
=P_{t,T}g
+\int_t^T P_{t,s}[F(s,\cdot)]\,ds.
\tag{1}
$$

When $F$ is itself a function of the unknown solution and its derivatives, for example

$$
F(s,x)=f(s,x,u(s,x),Du(s,x)),
$$

formula (1) becomes a nonlinear integral equation. A **mild solution** is a function satisfying that integral equation in a stated function class, with all terms well defined. The definition does not by itself assert that such a solution exists or is unique.

For $L=\frac12\Delta$ on $\mathbb R^d$, the transition operator in (1) is precisely the Gaussian convolution from the [heat-kernel entry](heat-equation-and-gaussian-heat-kernel.md):

$$
(P_rh)(x)=\int_{\mathbb R^d}p_r(x-y)h(y)\,dy.
$$

If a solution is smooth enough, (1) follows by differentiating $P_{t,s}u(s,\cdot)$ with respect to $s$ and integrating from $t$ to $T$. Conversely, recovering a classical PDE from a mild solution requires enough regularity to justify the corresponding differentiations.

## Derivative transfer

For the heat operators and sufficiently integrable $h$, [Gaussian integration by parts](gaussian-integration-by-parts-and-automatic-differentiation.md) gives

$$
D P_rh(x)
=\mathbb E\left[h(x+B_r)\frac{B_r}{r}\right].
\tag{2}
$$

The stochastic weight has moment size of order $r^{-1/2}$. More general nondegenerate diffusions may admit Bismut--Elworthy--Li or Malliavin automatic-differentiation formulas under additional hypotheses; see [Malliavin and Bismut automatic differentiation](malliavin-and-bismut-automatic-differentiation.md).

## Algebraic branching of polynomial terms

Suppose a term in the nonlinear source is a monomial $c\,u_1\cdots u_m$. Sampling the time integral and creating conditionally independent descendants for the factors can turn the product into a branching expectation. Iterating this construction produces a [Duhamel tree](branching-diffusions-and-duhamel-trees.md). Gradient factors can be attached to marked descendants carrying automatic-differentiation weights.

This algebra explains why polynomial nonlinearities are naturally compatible with branching. It does not show that the resulting random product is integrable, that the genealogy is harmless on the required horizon, or that an infinite iteration may be interchanged with expectation.

## Scope of the HLOTW theorem

The cited Henry-Labordère--Oudjane--Tan--Touzi--Warin theorem is a specific branching representation, not a theorem for arbitrary nonlinear mild equations. Their driver has polynomial dependence on the pair $(u,Du)$, with coefficient fields and offspring rules satisfying the assumptions stated in their Sections 2--3. The terminal datum entering their explicit estimates is bounded (and in the differentiable setting is controlled through its Lipschitz constant). Their variable-coefficient automatic-differentiation result uses bounded continuous diffusion coefficients with bounded continuous spatial derivatives and uniform ellipticity, as in Assumption 3.6.

Most importantly, the representation theorem requires the branching estimator and the companion gradient estimator to satisfy the paper's integrability conditions. Assumption 3.10 gives explicit sufficient moment conditions, and the authors describe these conditions as a **small-maturity or small-nonlinearity restriction**. Under Assumptions 3.1, 3.6, and 3.10, Theorem 3.12 establishes the required uniform integrability and concludes that the branching expectation is a viscosity solution; when its moment exponent is at least two, it also obtains an $L^2$ bound. The paper's branching/nonexplosion and moment hypotheses therefore cannot be dropped merely because the formal Duhamel recursion is valid.

The more detailed [HLOTW literature entry](marked-branching-diffusion-for-gradient-nonlinearities.md) records the polynomial driver, automatic-differentiation weights, and explicit moment conditions. This page should be read downstream of the basic heat equation, Duhamel identity, and mild-solution notion, rather than as their introduction.
