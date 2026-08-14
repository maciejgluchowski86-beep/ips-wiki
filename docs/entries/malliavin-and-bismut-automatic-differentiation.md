---
title: Malliavin and Bismut automatic differentiation
status: standard fact
tags:
  - probability
  - stochastic calculus
  - Malliavin calculus
  - Bismut formula
  - diffusion
  - PDE
---

# Malliavin and Bismut automatic differentiation

Automatic-differentiation formulas for diffusions transfer a derivative with respect to the starting point from the payoff onto a stochastic weight. For Brownian motion this is ordinary Gaussian integration by parts. For a nonconstant uniformly nondegenerate diffusion, the Bismut--Elworthy--Li formula is a standard way to obtain the corresponding weight and is the mechanism used in marked branching representations such as HLOTW.

**References.** David Nualart, *The Malliavin Calculus and Related Topics*, second edition, Springer, 2006. Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, second edition, Springer, 1991. Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, arXiv:1603.01727. See [References](../meta/references.md).

## Diffusion flow and its Jacobian

Consider an \(d\)-dimensional diffusion

$$
dX_s^{t,x}
=
\mu(s,X_s^{t,x})\,ds
+
\sigma(s,X_s^{t,x})\,dW_s,
\qquad
X_t^{t,x}=x.
\tag{1}
$$

Assume the coefficients are regular enough that the solution depends differentiably on the starting point. Its spatial Jacobian is

$$
Y_s^{t,x}
:=
D_xX_s^{t,x}.
\tag{2}
$$

Differentiating the SDE formally and then using standard stochastic-flow theory gives the linear matrix SDE

$$
\begin{aligned}
dY_s
={}&
D_x\mu(s,X_s)Y_s\,ds\\
&+
\sum_j
D_x\sigma_j(s,X_s)Y_s\,dW_s^j,
\qquad
Y_t=I,
\end{aligned}
\tag{3}
$$

where \(\sigma_j\) denotes the \(j\)-th diffusion column.

## Bismut--Elworthy--Li formula

Suppose in addition that \(\sigma\) is uniformly nondegenerate, so that \(\sigma^{-1}\) is defined with suitable bounds. For a bounded measurable payoff \(\varphi\), a standard Bismut--Elworthy--Li formula has the form

$$
D_x\mathbb E[\varphi(X_s^{t,x})]
=
\mathbb E\left[
\varphi(X_s^{t,x})
\mathcal W(t,s,x)
\right],
\tag{4}
$$

with stochastic weight

$$
\mathcal W(t,s,x)
=
\frac1{s-t}
\int_t^s
\left(
\sigma(r,X_r^{t,x})^{-1}
Y_r^{t,x}
\right)^\top
 dW_r.
\tag{5}
$$

The exact matrix convention depends on whether gradients are represented as row or column vectors. Formula (4), rather than the convention in (5), is the invariant content used by the branching representation.

When \(\mu=0\) and \(\sigma=\sigma_0\) is constant, one has \(Y_r=I\), and (5) reduces to

$$
\mathcal W(t,s,x)
=
(\sigma_0^\top)^{-1}
\frac{W_s-W_t}{s-t},
\tag{6}
$$

which is exactly the Gaussian weight derived in [Gaussian integration by parts and automatic differentiation](gaussian-integration-by-parts-and-automatic-differentiation.md).

## Why the weight has a short-time singularity

The stochastic integral in (5) has typical size of order \((s-t)^{1/2}\). The prefactor \((s-t)^{-1}\) therefore gives

$$
|\mathcal W(t,s,x)|
\sim
(s-t)^{-1/2}
$$

at the level of moments. This short-time singularity is the source of the lifetime-density balance in the [HLOTW marked branching construction](marked-branching-diffusion-for-gradient-nonlinearities.md).

## Malliavin integration by parts

Malliavin calculus views a sufficiently regular random variable \(F=F(W)\) as differentiable with respect to perturbations of the driving Brownian path. Its *Malliavin derivative* \(D_rF\) is a random process describing the first-order response to a perturbation of the noise near time \(r\).

The adjoint of the Malliavin derivative is the *divergence* or *Skorokhod integral* \(\delta\). In its basic form, Malliavin integration by parts says

$$
\mathbb E\left[
\langle DF,u\rangle_{L^2}
\right]
=
\mathbb E[F\,\delta(u)]
\tag{7}
$$

for processes \(u\) in the domain of \(\delta\). For adapted square-integrable \(u\), \(\delta(u)\) agrees with the ordinary Ito integral

$$
\delta(u)
=
\int u_r\,dW_r.
$$

The Bismut weight is obtained by choosing a process \(u\) whose Malliavin perturbation reproduces a perturbation of the starting point. Formula (7) then moves the derivative from the payoff to the stochastic integral, producing (4).

## Scope

The precise hypotheses for (4)--(5) vary across versions of the theorem. Smoothness of the stochastic flow, nondegeneracy of \(\sigma\), and moment bounds for the Jacobian are typical assumptions. The PDE wiki will state the hypotheses of the cited branching theorem when a variable-coefficient Bismut weight is actually used.

For the explicit dichotomy benchmark, the diffusion coefficient is constant and none of this machinery is needed beyond the elementary Gaussian formula (6). This entry is included so that the general HLOTW literature discussion does not rely on undefined Malliavin or Bismut terminology.