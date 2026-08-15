---
title: Gaussian integration by parts and automatic differentiation
status: standard fact
audit: current
tags:
  - probability
  - PDE
  - heat semigroup
  - automatic differentiation
---

# Gaussian integration by parts and automatic differentiation

Gaussian integration by parts transfers derivatives from a payoff to explicit centered Gaussian weights. For heat kernels this gives exact spatial-derivative formulas without differentiating the payoff pointwise.

**References.** David Nualart, *The Malliavin Calculus and Related Topics*, 2nd ed., Springer, 2006. Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Ann. Inst. H. Poincaré Probab. Statist.* 55(1) (2019), 184--210. See [References](../meta/references.md).

## Gaussian integration by parts

If $Z\sim N(0,1)$ and $\varphi$ is continuously differentiable with the relevant expectations finite, then

$$
\mathbb E[Z\varphi(Z)]=\mathbb E[\varphi'(Z)].
\tag{1}
$$

This follows from ordinary integration by parts against the density $(2\pi)^{-1/2}e^{-z^2/2}$.

## Heat-semigroup derivative

For

$$
(P_th)(x)=\mathbb E[h(x+\sqrt t\,Z)],
$$

one obtains

$$
\partial_xP_th(x)
=
\frac1{\sqrt t}\mathbb E[h(x+\sqrt t\,Z)Z]
=
\mathbb E\left[h(x+B_t)\frac{B_t}{t}\right].
\tag{2}
$$

The weight $B_t/t$ is centered and has moment size of order $t^{-1/2}$.

Repeated integration by parts gives

$$
\partial_x^kP_th(x)
=
t^{-k/2}\mathbb E\left[h(x+\sqrt t\,Z)He_k(Z)\right],
\tag{3}
$$

where $He_k$ is the probabilists' [Hermite polynomial](hermite-polynomials-and-gaussian-chaos.md). In particular,

$$
\partial_x^2P_th(x)
=
\frac1t\mathbb E[h(x+\sqrt t\,Z)(Z^2-1)].
$$

The same identities apply to periodic functions by lifting them to the real line.

## Automatic-differentiation weights

For a diffusion $X_s^{t,x}$, an **automatic-differentiation weight** is a random vector $\mathcal W(t,s,x)$ satisfying

$$
D_x\mathbb E[\varphi(X_s^{t,x})]
=
\mathbb E[\varphi(X_s^{t,x})\mathcal W(t,s,x)]
\tag{4}
$$

for a specified class of payoffs. For constant invertible diffusion matrix $\sigma_0$,

$$
X_s^{t,x}=x+\sigma_0(W_s-W_t),
$$

and one may take

$$
\mathcal W(t,s,x)
=(\sigma_0^\top)^{-1}\frac{W_s-W_t}{s-t}.
\tag{5}
$$

Variable-coefficient analogues are provided by Malliavin/Bismut formulas under additional regularity and nondegeneracy hypotheses; see [Malliavin and Bismut automatic differentiation](malliavin-and-bismut-automatic-differentiation.md).

## Short-time singularity

A gradient weight has natural size $(s-t)^{-1/2}$. If a branching time with density $\rho$ is sampled as well, a marked internal factor can contain both $1/\rho(s-t)$ and a derivative weight. Moment estimates must therefore balance the lifetime law against this short-time singularity. The exact algebraic identity does not by itself provide that integrability.
