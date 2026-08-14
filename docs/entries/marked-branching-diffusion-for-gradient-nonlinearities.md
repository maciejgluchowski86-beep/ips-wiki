---
title: Marked branching diffusion for gradient nonlinearities
status: literature
tags:
  - PDE
  - branching process
  - Feynman-Kac formula
  - Malliavin calculus
  - Monte Carlo
---

# Marked branching diffusion for gradient nonlinearities

The branching representation of Henry-Labordère, Oudjane, Tan, Touzi, and Warin treats semilinear equations whose nonlinearity is polynomial in the solution and its first spatial gradient. As in the [mild branching-diffusion picture](mild-formulation-and-branching-diffusion-representation.md), branching turns monomials into products over independent descendants. Gradient factors are handled differently from the [Nguwi--Penent--Privault coding tree](npp-coding-tree.md): descendants carry finitely many gradient marks, and a marked particle receives an automatic-differentiation weight obtained from Malliavin integration by parts.

**References.** Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, arXiv:1603.01727, especially Sections 2--3, Theorem 3.5, Assumption 3.10, Remark 3.11, Theorem 3.12, and Proposition 4.1; see [References](../meta/references.md).

## Polynomial driver class

For a diffusion in \(\mathbb R^d\), let \(m\geq0\), let \(L\subseteq\mathbb N^{m+1}\), and write \(\ell=(\ell_0,\ldots,\ell_m)\) and \(|\ell|=\sum_{i=0}^m\ell_i\). The paper considers nonlinearities of the form

$$
f(t,x,y,z)
=
\sum_{\ell\in L}
c_\ell(t,x)y^{\ell_0}
\prod_{i=1}^m
\bigl(b_i(t,x)\cdot z\bigr)^{\ell_i}.
\tag{1}
$$

This is equation (2.1) in the paper. Since \(L\subseteq\mathbb N^{m+1}\), the index family is at most countable; the polynomial cases motivating the construction correspond to finitely many nonzero monomials. The branching law assigns probabilities \((p_\ell)_{\ell\in L}\) with

$$
p_\ell>0,
\qquad
\sum_{\ell\in L}|\ell|p_\ell<\infty.
$$

When a particle branches with type \(\ell\), it produces \(|\ell|\) children. Exactly \(\ell_i\) of them receive mark \(i\), for \(i=0,\ldots,m\). Mark \(0\) represents an ordinary factor of \(u\); mark \(i\geq1\) represents the directional gradient factor \(b_i\cdot Du\).

## Gradient marks and automatic differentiation

Let \(X_s^{t,x}\) be the underlying diffusion. The automatic-differentiation hypothesis in Assumption 3.2 asks for a measurable weight \(\mathcal W\) such that, for bounded measurable \(\varphi\),

$$
\partial_x\mathbb E\bigl[\varphi(X_s^{t,x})\bigr]
=
\mathbb E\bigl[
\varphi(X_s^{t,x})
\mathcal W(t,s,x,\Delta W)
\bigr].
\tag{2}
$$

For constant nondegenerate diffusion coefficient \(\sigma_0\), the basic example is

$$
\mathcal W(t,s,x,\Delta W)
=
(\sigma_0^\top)^{-1}
\frac{W_s-W_t}{s-t}.
\tag{3}
$$

Brownian scaling makes the typical size of (3) proportional to \((s-t)^{-1/2}\). For a particle \(k\) with mark \(\theta_k\), the factor entering the branching functional is

$$
\mathcal W_k
=
\ind(\theta_k=0)
+
\ind(\theta_k\neq0)
\,b_{\theta_k}(T_{k^-},X_{T_{k^-}}^k)
\cdot
\mathcal W(T_{k^-},T_k,X_{T_{k^-}}^k,\Delta W^k).
\tag{4}
$$

Thus the mark does not ask the tree to propagate a new differential code. It determines whether the corresponding descendant carries an automatic-differentiation weight. For general nondegenerate diffusions, the paper obtains \(\mathcal W\) from a Bismut--Elworthy--Li/Malliavin integration-by-parts formula.

## Lifetime density and the short-time singularity

Branching lifetimes have a strictly positive density \(\rho\). An internal branching factor contains the importance-sampling denominator

$$
\frac{c_{I_k}(T_k,X_{T_k}^k)}{p_{I_k}\rho(\Delta T_k)}
$$

as well as the mark factor \(\mathcal W_k\). The gradient weight has the short-time scale \((\Delta T_k)^{-1/2}\), so absolute moments depend sensitively on the lifetime law near zero.

The compensation is an integrability balance, not an algebraic cancellation of \(\mathcal W_k\) by \(\rho\). In the explicit criterion of Assumption 3.10, one of the relevant quantities has the form

$$
\sup_{\ell\in L,\,r\in(0,T]}
C_{2,q}
\left(
\frac{\lVert c_\ell\rVert_\infty}{p_\ell}
\sqrt{\frac{1}{r\rho(r)}}
\right)^q.
\tag{5}
$$

Remark 3.11 notes that controlling this expression requires the ratios \(\lVert c_\ell\rVert_\infty/p_\ell\) to be uniformly bounded and, for this criterion, a density satisfying

$$
\rho(r)\geq C r^{-1/2}
$$

near zero. Their alternative \(q\)-moment criterion requires a still stronger power singularity. A lifetime distribution that puts sufficient mass near zero offsets the Malliavin-weight singularity in the moment estimates.

## Integrability and viscosity representation

Theorem 3.5 states the operative representation assumption abstractly. Besides the branching and automatic-differentiation hypotheses, it requires local uniform integrability of the family of tree estimators \(\psi^{s,y}\) and of the companion family used for the gradient formula, \(\widetilde\psi^{s,y}\mathcal W\). Under these hypotheses,

$$
u(t,x)=\mathbb E[\psi^{t,x}]
$$

is a continuous viscosity solution of the semilinear PDE, and \(Du\) exists and is continuous.

Section 3.2 then gives explicit sufficient conditions. Assumption 3.10 is described in the paper as a small-maturity or small-nonlinearity restriction; Theorem 3.12 uses it to obtain the required uniform integrability. When the moment exponent satisfies \(q\geq2\), the theorem also gives \(\psi^{t,x}\in L^2\).

## Uniqueness scope

Theorem 3.5 produces a viscosity solution from the branching expectation; uniqueness is a separate PDE comparison question. When uniqueness in the relevant class of bounded viscosity solutions is assumed or otherwise known, the probabilistic representation identifies that unique solution. Proposition 4.1 makes this distinction explicit in one of the paper's extensions by assuming uniqueness of the bounded viscosity solution in addition to the integrability hypotheses.

The structural contrast with the Nguwi--Penent--Privault construction is therefore specific. The marked branching scheme encodes a polynomial dependence on \((u,Du)\) using finitely many kinds of gradient marks and Malliavin weights. The coding-tree construction instead propagates an infinite differential code class capable of tracking derivatives of arbitrary order.