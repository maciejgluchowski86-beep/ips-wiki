---
title: Nguwi-Penent-Privault coding-tree Feynman-Kac theorem
status: literature
audit: current
tags:
  - PDE
  - Feynman-Kac formula
  - coding tree
  - integrability
  - branching process
---

# Nguwi-Penent-Privault coding-tree Feynman-Kac theorem

Nguwi--Penent--Privault Theorem 4.2 identifies expectations of the [coding-tree](npp-coding-tree.md) functional with the coded quantities of a smooth solution, subject to explicit assumptions. The result is conditional: existence and uniqueness of a smooth solution of the original PDE are already part of Assumption (A), absolute integrability is required for every code, and the final identification of all coded expectations additionally uses uniqueness of the infinite code-indexed system.

**Primary source.** Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882v3: Assumption (A) in Section 1, Definition 4.1, and Theorem 4.2. See [References](../meta/references.md).

Consider

$$
\partial_tu+\frac12\partial_x^2u+f(u,\partial_xu,\ldots,\partial_x^nu)=0,
\qquad
u(T,\cdot)=\phi.
\tag{1}
$$

Let

$$
p_\eta(x)=\frac{1}{\sqrt{2\pi\eta}}e^{-x^2/(2\eta)},
\qquad \eta>0.
$$

## Assumption (A)

The source assumes:

1. $f\in C^\infty(\mathbb R^{n+1})$ and $\phi\in C^\infty(\mathbb R)$.
2. Equation (1) admits a unique solution $u\in C^{1,\infty}([0,T]\times\mathbb R)$, written in Duhamel form as

$$
\begin{aligned}
u(t,x)
={}&\int_{\mathbb R}p_{T-t}(y-x)\phi(y)\,dy\\
&+\int_t^T\int_{\mathbb R}
p_{s-t}(y-x)
 f\bigl(u(s,y),\partial_yu(s,y),\ldots,\partial_y^nu(s,y)\bigr)
\,dy\,ds.
\end{aligned}
\tag{2}
$$

3. For every $\eta>0$, the terminal derivatives and the derivatives of $f$ evaluated along the solution jet satisfy the Gaussian-weighted integrability conditions

$$
\phi^{(k)}\in\bigcap_{p=1}^{n+1}L^p(\mathbb R,p_\eta(x)\,dx),
\qquad k\ge0,
\tag{3}
$$

and, for every $\lambda=(\lambda_0,\ldots,\lambda_n)\in\mathbb N^{n+1}$,

$$
\partial_{z_0}^{\lambda_0}\cdots\partial_{z_n}^{\lambda_n}f
\bigl(u,\partial_xu,\ldots,\partial_x^nu\bigr)
\in
\bigcap_{p=1}^{n+1}
L^p([0,T]\times\mathbb R,p_\eta(x)\,dx\,ds).
\tag{4}
$$

These hypotheses are the source's assumptions for the code calculations; in particular, item 2 is not derived by the coding-tree theorem.

## Theorem 4.2

Let $\mathfrak C$ be the Nguwi--Penent--Privault code set and $H(\mathcal T_{t,x,c})$ the multiplicative functional from Definition 4.1. Under Assumption (A), fix $T>0$ such that

$$
\mathbb E\left[|H(\mathcal T_{t,x,c})|\right]<\infty,
\qquad
(t,x)\in[0,T]\times\mathbb R,
\quad c\in\mathfrak C.
\tag{5}
$$

Thus the hypothesis is an all-code $L^1$ condition, not merely integrability of the identity-rooted estimator. Define

$$
u_c(t,x)=\mathbb E[H(\mathcal T_{t,x,c})].
$$

Then Theorem 4.2 states that $(u_c)_{c\in\mathfrak C}$ solves the code-indexed integral system

$$
\begin{aligned}
u_c(t,x)
={}&P_{T-t}[c(u)(T,\cdot)](x)\\
&+\sum_{Z\in\mathcal M(c)}
\int_t^T P_{s-t}\left[\prod_{z\in Z}u_z(s,\cdot)\right](x)\,ds,
\end{aligned}
\tag{6}
$$

with terminal condition $u_c(T,x)=c(u)(T,x)$.

Moreover, if the solution $(u_c)_{c\in\mathfrak C}$ of (6) is unique, then

$$
c(u)(t,x)=u_c(t,x)=\mathbb E[H(\mathcal T_{t,x,c})]
\tag{7}
$$

for every code $c$. Taking $c=\operatorname{Id}$ gives

$$
u(t,x)=\mathbb E[H(\mathcal T_{t,x,\operatorname{Id}})].
\tag{8}
$$

## Two uniqueness interfaces

The source therefore uses two distinct uniqueness statements.

- **Original PDE:** Assumption (A)(ii) presupposes a unique smooth solution $u$ of (1) satisfying the Duhamel formula.
- **Code-indexed system:** the additional uniqueness condition in Theorem 4.2 is what identifies the expectation family solving (6) with the already existing coded family $c(u)$.

Neither condition should be silently replaced by the other.

## Integrability scope

The first-branch calculation in the coding-tree construction explains why the reciprocal lifetime, offspring, and survival factors reproduce (6), but it does not establish (5). Nguwi--Penent--Privault Proposition 4.3 gives an additional sufficient small-time criterion under stronger boundedness and lifetime-density assumptions. Theorem 4.2 itself should be read with the all-code integrability condition (5) and the two uniqueness interfaces above kept explicit.