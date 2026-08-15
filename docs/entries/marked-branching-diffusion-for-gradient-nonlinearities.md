---
title: Marked branching diffusion for gradient nonlinearities
status: literature
audit: current
tags:
  - PDE
  - branching process
  - Feynman-Kac formula
  - Malliavin calculus
  - Monte Carlo
---

# Marked branching diffusion for gradient nonlinearities

Henry-Labordère, Oudjane, Tan, Touzi, and Warin (HLOTW) give a branching-diffusion representation for semilinear parabolic PDEs whose nonlinearity is polynomial in the solution and its first spatial gradient. Branching represents products, while marked descendants carry automatic-differentiation weights for directional gradient factors.

**Source audit.** Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 55(1) (2019), 184--210, DOI 10.1214/17-AIHP880; arXiv:1603.01727. The discussion below follows Sections 2--3, including the abstract representation theorem and the explicit sufficient moment conditions in Assumption 3.10 and Theorem 3.12.

## Polynomial driver and marks

The driver is written as

$$
f(t,x,y,z)
=
\sum_{\ell\in L}c_\ell(t,x)y^{\ell_0}
\prod_{i=1}^m\bigl(b_i(t,x)\cdot z\bigr)^{\ell_i},
\tag{1}
$$

where $L\subseteq\mathbb N^{m+1}$ is at most countable, $\ell=(\ell_0,\ldots,\ell_m)$, and the offspring probabilities satisfy $p_\ell>0$ and $\sum_\ell|\ell|p_\ell<\infty$. A branch of type $\ell$ creates $|\ell|$ children: $\ell_0$ ordinary value marks and $\ell_i$ copies of directional-gradient mark $i$.

## Automatic differentiation

For the underlying diffusion $X_s^{t,x}$, HLOTW assume an automatic-differentiation formula of the form

$$
D_x\mathbb E[\varphi(X_s^{t,x})]
=
\mathbb E[\varphi(X_s^{t,x})\mathcal W(t,s,x)].
\tag{2}
$$

For constant invertible diffusion coefficient $\sigma_0$,

$$
\mathcal W(t,s,x)
=(\sigma_0^\top)^{-1}\frac{W_s-W_t}{s-t}.
\tag{3}
$$

A nonzero mark pairs this weight with the corresponding vector $b_i$. Variable-coefficient versions rely on Malliavin/Bismut formulas under their own regularity and nondegeneracy hypotheses; see [Malliavin and Bismut automatic differentiation](malliavin-and-bismut-automatic-differentiation.md).

## Lifetime density and moment cost

A particle lifetime is sampled from a positive density $\rho$. An internal branching factor contains the compensator

$$
\frac{c_{I_k}(T_k,X_{T_k}^k)}{p_{I_k}\rho(\Delta T_k)}
$$

and, for a gradient mark, an automatic-differentiation factor with short-time scale $(\Delta T_k)^{-1/2}$. Thus algebraic unbiasedness does not remove the short-time singularity from absolute moments.

One explicit $q$-moment quantity in Assumption 3.10 has the form

$$
\sup_{\ell\in L,\,r\in(0,T]}
C_{2,q}
\left(
\frac{\|c_\ell\|_\infty}
{p_\ell\sqrt r\,\rho(r)}
\right)^q.
\tag{4}
$$

Remark 3.11 explains that this criterion requires the coefficient-to-offspring ratios $\|c_\ell\|_\infty/p_\ell$ to be uniformly controlled and a lifetime density sufficiently singular near zero; for the displayed criterion, a lower bound of order $r^{-1/2}$ is the relevant balance. The alternative moment condition in Assumption 3.10 uses a stronger power requirement.

These conditions are sufficient conditions for the integrability needed by the representation. They impose a small-maturity or small-nonlinearity regime through the associated positive moment majorant; the paper itself describes this restriction explicitly.

## Representation theorem and uniform integrability

The abstract representation theorem requires local uniform integrability of the branching estimator family and of the companion family used to represent the gradient. Under those hypotheses, the branching expectation defines a continuous viscosity solution and its spatial gradient exists and is continuous. Section 3.2 supplies explicit sufficient conditions; Theorem 3.12 derives the required uniform integrability from Assumption 3.10 and gives an $L^2$ conclusion when the chosen moment exponent is at least two.

The [uniform-integrability](uniform-integrability-and-passage-to-expectations.md) condition is analytically distinct from finite-horizon [nonexplosion of the genealogy](age-dependent-branching-and-nonexplosion.md). A finite tree can still carry a nonintegrable product.

## Scope and uniqueness

The representation theorem constructs a viscosity solution under its branching, automatic-differentiation, and integrability hypotheses. Identification with a unique PDE solution additionally requires an appropriate comparison/uniqueness result in the solution class. The paper makes this distinction explicitly in later extensions.

The cited HLOTW theorem is a finite-horizon marked-branching representation under these integrability hypotheses. It does not state a general deterministic-interface or time-slab theorem that resets the moment condition at intermediate times.
