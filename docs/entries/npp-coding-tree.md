---
title: Nguwi-Penent-Privault coding tree
status: definition
tags:
  - PDE
  - Feynman-Kac formula
  - branching process
  - coding tree
  - importance sampling
---

# Nguwi-Penent-Privault coding tree

The Nguwi--Penent--Privault construction rewrites the [heat-reference PDE](heat-reference-fully-nonlinear-pde.md) as an infinite system indexed by differential *codes*. A random [branching tree](branching-diffusions-and-duhamel-trees.md) samples the product terms in this system. Reciprocal lifetime and offspring-selection probabilities are inserted into a [multiplicative importance-sampling functional](importance-sampling-compensators.md) so that conditioning on the first branch exactly recovers the code-indexed Duhamel equations.

**References.** Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882. For a multidimensional deep-learning implementation, see the same authors, *A deep branching solver for fully nonlinear partial differential equations*, arXiv:2203.03234; see [References](../meta/references.md).

Throughout, fix \(f\in C^\infty(\mathbb R^{n+1})\). For any smooth \(g:\mathbb R^{n+1}\to\mathbb R\), define the substitution operator

$$
g^*(v)(t,x)=g(J_nv(t,x)).
$$

The [jet and total-derivative conventions](spatial-jets-total-derivative-and-faa-di-bruno.md) used here agree with the heat-reference PDE entry.

## Definition

The Nguwi--Penent--Privault code set \(\mathcal C\) consists of

$$
\operatorname{Id},
\qquad
\partial_x^k\quad(k\geq1),
\qquad
\left(a\,\partial_{z_0}^{\lambda_0}\cdots\partial_{z_n}^{\lambda_n}f\right)^*,
$$

where \(a\in\mathbb R\setminus\{0\}\) and each \(\lambda_j\) is a nonnegative integer. A code is therefore an operator acting on the unknown function \(u\), rather than a numerical mark attached to a particle.

## Definition

The *mechanism* \(\mathcal M\) assigns to every code \(c\in\mathcal C\) a finite family \(\mathcal M(c)\) of finite ordered tuples of codes. Its operational defining property is that the Duhamel equation for \(c(u)\) can be written as

$$
c(u)(t,x)
=
P_{T-t}[c(u)(T,\cdot)](x)
+
\sum_{Z\in\mathcal M(c)}
\int_t^T
P_{s-t}\left[
\prod_{z\in Z}z(u)(s,\cdot)
\right](x)\,ds.
\tag{1}
$$

In particular,

$$
\mathcal M(\operatorname{Id})=\{(f^*)\}.
$$

For codes of the form \(g^*\) and \(\partial_x^k\), Nguwi--Penent--Privault Definition 2.2 gives the explicit tuples by applying the [multivariate Faà di Bruno formula](spatial-jets-total-derivative-and-faa-di-bruno.md) to derivatives of \(f(J_nu)\) and \(g(J_nu)\). Scalar combinatorial coefficients are absorbed into the coefficient \(a\) allowed in the code set. Equation (1) is the reason for the mechanism: each tuple \(Z\) is exactly one product term that a branching event must reproduce.

## Definition

Choose a strictly positive probability density \(\rho\) on \(\mathbb R_+\), and write

$$
\overline F(r)=\int_r^\infty \rho(s)\,ds.
$$

For every code \(c\), let \(I_c\) be sampled uniformly from the finite set \(\mathcal M(c)\), and write

$$
q_c(Z)=\mathbb P(I_c=Z),
\qquad Z\in\mathcal M(c).
$$

A random coding tree \(\mathcal T_{t,x,c}\) starts from one particle at time \(t\), position \(x\), and code \(c\). Each particle evolves along an independent Brownian path and receives an independent lifetime with density \(\rho\). If its lifetime reaches beyond \(T\), the branch stops at \(T\). If it dies before \(T\), a tuple \(Z=(c_1,\ldots,c_m)\) is sampled from \(\mathcal M(c)\), and \(m\) children are born at the death position with codes \(c_1,\ldots,c_m\). Descendants repeat the same construction independently conditional on their birth data.

Let \(\mathcal K^\circ\) be the particles that die before \(T\) and \(\mathcal K^\partial\) the particles alive at the terminal horizon. For a particle \(k\), let \(c_k\) be its code, \(\tau_k\) its lifetime, \(I_{c_k}\) its sampled offspring tuple when \(k\in\mathcal K^\circ\), \(T_{k^-}\) its birth time, and \(X_T^k\) its position at time \(T\) when \(k\in\mathcal K^\partial\).

## Definition

The multiplicative functional of the coding tree is

$$
H(\mathcal T_{t,x,c})
=
\prod_{k\in\mathcal K^\circ}
\frac{1}{q_{c_k}(I_{c_k})\rho(\tau_k)}
\prod_{k\in\mathcal K^\partial}
\frac{c_k(u)(T,X_T^k)}{\overline F(T-T_{k^-})}.
\tag{2}
$$

The terminal factor in (2) is explicit from the data. If \(c_k=\partial_x^m\), then

$$
c_k(u)(T,y)=\phi^{(m)}(y).
$$

If \(c_k=g^*\), then

$$
c_k(u)(T,y)=g(J_n\phi(y)).
$$

Thus the unknown solution does not appear at terminal leaves.

## Proposition

The factors \(1/\rho\), \(1/q_c\), and \(1/\overline F\) in (2) are [importance-sampling compensators](importance-sampling-compensators.md). Conditioning on the first branch cancels the auxiliary lifetime law and offspring-selection law and reproduces the Duhamel recursion (1), provided the relevant expectations are integrable.

## Proof

Suppose first that a particle with code \(c\) survives from its birth time \(s\) to \(T\). This event has probability \(\overline F(T-s)\), which cancels the terminal denominator in (2). The remaining expectation is precisely the heat-semigroup transfer of the terminal value \(c(u)(T,\cdot)\).

If the particle dies after elapsed time \(r<T-s\) and samples \(Z\in\mathcal M(c)\), the joint sampling factor is

$$
\rho(r)\,dr\; q_c(Z).
$$

Multiplication by the internal-node factor in (2) cancels both \(\rho(r)\) and \(q_c(Z)\). Conditional independence of the descendant subtrees turns their joint contribution into the product of their expectations. Summing over \(Z\in\mathcal M(c)\) and integrating \(r\) therefore gives the nonlinear Duhamel term in (1).

This cancellation establishes the recursion satisfied by the expectation. It does not by itself justify taking absolute expectations or exchanging all sums, products, and integrals. Those requirements are part of the [Nguwi--Penent--Privault Feynman-Kac theorem](npp-coding-tree-feynman-kac-theorem.md).