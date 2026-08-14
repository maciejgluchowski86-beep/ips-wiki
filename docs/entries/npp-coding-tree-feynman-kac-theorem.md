---
title: Nguwi-Penent-Privault coding-tree Feynman-Kac theorem
status: standard fact
tags:
  - PDE
  - Feynman-Kac formula
  - coding tree
  - integrability
  - branching process
---

# Nguwi-Penent-Privault coding-tree Feynman-Kac theorem

Nguwi--Penent--Privault Theorem 4.2 identifies the expectation of the [coding-tree](npp-coding-tree.md) functional with the solution and its coded derivatives. The theorem assumes a smooth PDE solution in advance and imposes \(L^1\) integrability of the tree functional for every code, not only for the root code \(\operatorname{Id}\).

**References.** Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882, Assumption (A) and Theorem 4.2. For later integrability criteria for coded branching functionals, see Qiao Huang and Nicolas Privault, *Stability analysis of a branching diffusion solver for semilinear heat equations*, arXiv:2502.17853; see [References](../meta/references.md).

Fix the [heat-reference PDE](heat-reference-fully-nonlinear-pde.md)

$$
\partial_tu+\frac12\partial_x^2u+f(J_nu)=0,
\qquad
u(T,\cdot)=\phi,
\tag{1}
$$

and let

$$
p_\eta(x)
=
\frac{1}{\sqrt{2\pi\eta}}\exp\left(-\frac{x^2}{2\eta}\right),
\qquad \eta>0.
$$

## Definition

Nguwi--Penent--Privault Assumption (A) consists of the following three hypotheses.

1. The functions satisfy \(f\in C^\infty(\mathbb R^{n+1})\) and \(\phi\in C^\infty(\mathbb R)\).
2. Equation (1) admits a unique solution \(u\in C^{1,\infty}([0,T]\times\mathbb R)\), and this solution satisfies the Duhamel formulation

$$
u(t,x)
=
\int_{\mathbb R}p_{T-t}(y-x)\phi(y)\,dy
+
\int_t^T\int_{\mathbb R}
p_{s-t}(y-x)f(J_nu(s,y))\,dy\,ds.
\tag{2}
$$

3. For every \(\eta>0\), the terminal derivatives and all jet derivatives of the nonlinearity, evaluated along the solution jet, have the Gaussian-weighted integrability required in the code calculations:

$$
\phi^{(k)}
\in
\bigcap_{p=1}^{n+1}L^p\bigl(\mathbb R,p_\eta(x)\,dx\bigr)
\qquad(k\geq0),
\tag{3}
$$

and, for every tuple \(\lambda=(\lambda_0,\ldots,\lambda_n)\) of nonnegative integers,

$$
\partial_{z_0}^{\lambda_0}\cdots\partial_{z_n}^{\lambda_n}f(J_nu)
\in
\bigcap_{p=1}^{n+1}
L^p\bigl([0,T]\times\mathbb R,p_\eta(x)\,dx\,ds\bigr).
\tag{4}
$$

The role of (3)--(4) is to justify the differentiations, Gaussian convolutions, and finite product manipulations used to derive the code-indexed Duhamel system. Assumption (A) is not an existence theorem for (1): existence and uniqueness of the smooth solution are already included in item 2.

## Theorem

Assume Assumption (A). Let \(\mathcal C\) be the Nguwi--Penent--Privault code set and let \(H(\mathcal T_{t,x,c})\) be the multiplicative coding-tree functional. Suppose that

$$
\mathbb E\left[\left|H(\mathcal T_{t,x,c})\right|\right]<\infty
\qquad
\text{for every }(t,x)\in[0,T]\times\mathbb R
\text{ and every }c\in\mathcal C.
\tag{5}
$$

Define

$$
u_c(t,x)
=
\mathbb E\bigl[H(\mathcal T_{t,x,c})\bigr].
$$

Then the family \((u_c)_{c\in\mathcal C}\) solves the code-indexed integral system

$$
u_c(t,x)
=
P_{T-t}[c(u)(T,\cdot)](x)
+
\sum_{Z\in\mathcal M(c)}
\int_t^T
P_{s-t}\left[
\prod_{z\in Z}u_z(s,\cdot)
\right](x)\,ds.
\tag{6}
$$

If the solution of the system (6) is unique, then

$$
c(u)(t,x)
=
u_c(t,x)
=
\mathbb E\bigl[H(\mathcal T_{t,x,c})\bigr]
$$

for every code \(c\). In particular,

$$
u(t,x)
=
\mathbb E\bigl[H(\mathcal T_{t,x,\operatorname{Id}})\bigr].
\tag{7}
$$

## Integrability scope

Condition (5) is an all-code \(L^1\) hypothesis. Finiteness of the expectation only for the identity-rooted tree is not the hypothesis of Theorem 4.2, because the proof conditions on the first branching event and recursively invokes expectations rooted at descendant codes.

The theorem also separates two logically different uniqueness assumptions. Assumption (A) contains uniqueness of the smooth solution of the original PDE, while the final identification \(u_c=c(u)\) additionally uses uniqueness of the infinite code-indexed system (6).

Theorem 4.2 is therefore a conditional representation theorem: it applies on any horizon for which its all-code integrability and code-system uniqueness hypotheses hold. Nguwi--Penent--Privault then give additional sufficient conditions over a sufficiently small time interval. Huang--Privault develop later sufficient criteria for integrability of multiplicative weighted progeny and uniqueness under uniform integrability.
