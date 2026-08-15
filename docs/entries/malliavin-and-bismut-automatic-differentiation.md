---
title: Malliavin and Bismut automatic differentiation
status: standard fact
audit: current
tags:
  - probability
  - stochastic calculus
  - Malliavin calculus
  - Bismut formula
  - diffusion
  - PDE
---

# Malliavin and Bismut automatic differentiation

Malliavin integration by parts and Bismut--Elworthy--Li formulas provide stochastic weights for derivatives of diffusion semigroups. Different versions require different smoothness, ellipticity, and integrability hypotheses. This page records the common identity used by probabilistic PDE representations and treats the constant-coefficient case explicitly; it does not assert a single universal variable-coefficient theorem.

**References.** David Nualart, *The Malliavin Calculus and Related Topics*, 2nd ed., Springer, 2006. Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed., Springer, 1991. Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Ann. Inst. H. Poincaré Probab. Statist.* 55(1) (2019), 184--210. See [References](../meta/references.md).

## Diffusion flow

For

$$
dX_s^{t,x}=\mu(s,X_s^{t,x})\,ds+\sigma(s,X_s^{t,x})\,dW_s,
\qquad X_t^{t,x}=x,
$$

regular coefficients may generate a stochastic flow differentiable in $x$. Its Jacobian is $Y_s^{t,x}=D_xX_s^{t,x}$. Under hypotheses permitting differentiation of the SDE, $Y$ solves the corresponding linearized matrix SDE.

## The automatic-differentiation identity

The variable-coefficient statement used in branching representations is the existence of an integrable random weight $\mathcal W(t,s,x)$ such that

$$
D_x\mathbb E[\varphi(X_s^{t,x})]
=
\mathbb E[\varphi(X_s^{t,x})\mathcal W(t,s,x)]
\tag{1}
$$

for the payoff class in question. Bismut--Elworthy--Li formulas construct such weights for nondegenerate diffusions under regularity assumptions on the coefficients and suitable moment bounds on the flow Jacobian. The exact formula and hypotheses must be checked in the theorem being applied.

For the constant-coefficient diffusion

$$
X_s^{t,x}=x+\sigma_0(W_s-W_t),
$$

with invertible matrix $\sigma_0$, ordinary Gaussian integration by parts gives the exact formula

$$
\mathcal W(t,s,x)
=(\sigma_0^\top)^{-1}\frac{W_s-W_t}{s-t}.
\tag{2}
$$

No Malliavin machinery is needed for (2).

## Malliavin integration by parts

For a sufficiently regular Wiener functional $F$, the Malliavin derivative $DF$ is an $L^2$-valued random variable. The adjoint of $D$ is the divergence operator $\delta$. For $u$ in the domain of $\delta$,

$$
\mathbb E[\langle DF,u\rangle_{L^2}]
=
\mathbb E[F\,\delta(u)].
\tag{3}
$$

When $u$ is adapted and square-integrable, $\delta(u)$ agrees with the Itô integral $\int u_r\,dW_r$. A Bismut formula chooses $u$ so that the Malliavin perturbation corresponds to a perturbation of the starting point, thereby moving the derivative from the payoff to a stochastic integral.

## Short-time scale

In standard nondegenerate settings, the stochastic weight in (1) has first or higher moments of order $(s-t)^{-1/2}$ as $s\downarrow t$. This is the scale relevant for [marked branching representations](marked-branching-diffusion-for-gradient-nonlinearities.md).

## Scope for the wiki

Whenever a variable-coefficient Bismut weight is used later, the relevant external theorem must supply the regularity, nondegeneracy, and integrability needed for (1). The wiki does not infer those hypotheses from the schematic identity. For constant diffusion coefficients, use the elementary Gaussian formula (2).
