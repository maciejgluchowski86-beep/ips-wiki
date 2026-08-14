---
title: Gaussian integration by parts and automatic differentiation
status: standard fact
tags:
  - probability
  - PDE
  - heat semigroup
  - Malliavin calculus
  - automatic differentiation
---

# Gaussian integration by parts and automatic differentiation

Gaussian integration by parts transfers derivatives from a payoff onto an explicit random weight. For the heat semigroup this gives exact formulas for spatial derivatives without differentiating the terminal function pointwise. Branching representations use these weights to encode gradient or Hessian factors along diffusion edges.

**References.** David Nualart, *The Malliavin Calculus and Related Topics*, second edition, Springer, 2006. Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, arXiv:1603.01727. See [References](../meta/references.md).

## Gaussian integration by parts

Let \(Z\sim N(0,1)\). For every continuously differentiable \(\varphi\) for which the expectations below are finite,

$$
\mathbb E[Z\varphi(Z)]
=
\mathbb E[\varphi'(Z)].
\tag{1}
$$

Indeed, with the standard normal density

$$
\gamma(z)
=
\frac1{\sqrt{2\pi}}e^{-z^2/2},
$$

one has \(\gamma'(z)=-z\gamma(z)\), so ordinary integration by parts gives (1).

## First derivative of the heat semigroup

For the heat semigroup

$$
(P_th)(x)
=
\mathbb E[h(x+\sqrt t\,Z)],
$$

formula (1) gives

$$
\partial_xP_th(x)
=
\frac1{\sqrt t}
\mathbb E[h(x+\sqrt t\,Z)Z]
=
\mathbb E\left[h(x+B_t)\frac{B_t}{t}\right].
\tag{2}
$$

The factor \(B_t/t\) is an *automatic-differentiation weight*. Its typical size is \(t^{-1/2}\), because \(B_t\) has size \(t^{1/2}\).

The same identity holds on the torus for periodic \(h\), by applying the real-line formula to the periodic lift of \(h\).

## Higher derivatives

Repeated Gaussian integration by parts gives

$$
\partial_x^kP_th(x)
=
 t^{-k/2}
\mathbb E\left[
 h(x+\sqrt t\,Z)He_k(Z)
\right],
\tag{3}
$$

where \(He_k\) is the probabilists' [Hermite polynomial](hermite-polynomials-and-gaussian-chaos.md). In particular,

$$
\partial_x^2P_th(x)
=
\frac1t
\mathbb E\left[
 h(x+\sqrt t\,Z)(Z^2-1)
\right].
\tag{4}
$$

The natural short-time scale of a \(k\)-th derivative weight is therefore \(t^{-k/2}\).

## Definition

Let \(X_s^{t,x}\) be a diffusion started from \(x\) at time \(t\). An *automatic-differentiation weight* for its transition operator is a random vector \(\mathcal W(t,s,x)\) such that

$$
D_x\mathbb E[\varphi(X_s^{t,x})]
=
\mathbb E\left[
\varphi(X_s^{t,x})\mathcal W(t,s,x)
\right]
\tag{5}
$$

for an appropriate class of test functions \(\varphi\).

For constant nondegenerate diffusion coefficient \(\sigma_0\),

$$
X_s^{t,x}
=
x+\sigma_0(W_s-W_t)
$$

and one may take

$$
\mathcal W(t,s,x)
=
(\sigma_0^\top)^{-1}
\frac{W_s-W_t}{s-t}.
\tag{6}
$$

For variable nondegenerate diffusions, [Malliavin integration by parts and the Bismut--Elworthy--Li formula](malliavin-and-bismut-automatic-differentiation.md) provide analogues of (5). Their precise hypotheses depend on the diffusion coefficients; the HLOTW construction assumes such a formula rather than deriving it from the branching argument itself.

## Why the singularity matters

Suppose a branching lifetime has density \(\rho(s)\). A gradient-marked branch contributes both an importance-sampling factor \(1/\rho(s)\) and an automatic-differentiation factor of size \(s^{-1/2}\). Moment estimates therefore contain combinations such as

$$
\frac1{\sqrt s\,\rho(s)}.
$$

This is the origin of the lifetime-density condition in the [HLOTW marked branching construction](marked-branching-diffusion-for-gradient-nonlinearities.md). Treating several derivative transfers edge by edge can create nonintegrable products of these short-time singularities; composition before taking absolute values can behave very differently, which is why Hermite-chaos identities matter in later patch calculations.