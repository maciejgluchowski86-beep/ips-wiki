---
title: Conditional factorization for finite PDE patches
status: standard fact
audit: current
tags:
  - PDE
  - patch
  - conditional expectation
  - conditional independence
  - factorization
---

# Conditional factorization for finite PDE patches

Finite patch randomizations often expose combinatorial or temporal data first and leave the marks inside distinct child pieces fresh. The relevant factorization is ordinary conditional independence: once the exposed sigma-field is fixed, independent fresh seeds may be averaged separately, provided the products being conditioned are integrable.

## Finite conditional factorization

Let \((\Omega,\mathcal F,\mathbb P)\) be a probability space and let \(\mathcal G\subseteq\mathcal F\) be a sigma-field. Suppose \(Y_1,\ldots,Y_k\) are conditionally independent given \(\mathcal G\), each \(Y_j\) is integrable, and
\[
\prod_{j=1}^k |Y_j|\in L^1(\mathbb P).
\]
Then
\[
\mathbb E\!\left[
\prod_{j=1}^k Y_j
\,\middle|\,
\mathcal G
\right]
=
\prod_{j=1}^k
\mathbb E[Y_j\mid\mathcal G]
\qquad\text{a.s.}
\tag{1}
\]

For bounded \(Y_j\), (1) is the defining product identity for conditional independence, first for indicator functions and then for bounded measurable functions. The integrable form follows by truncation together with conditional dominated convergence.

This is the finite factorization used when a patch skeleton, branch times, or other common data are exposed while distinct child patches retain independent auxiliary seeds. The hypothesis is about the sigma-field actually conditioned on: revealing a mark whose centering is needed later destroys its freshness.

## Random fields evaluated at a parent location

Let \(Y_j(x)\), \(x\in E\), be jointly measurable random fields. Assume that, conditional on \(\mathcal G\), the seeds generating the fields are independent. Let \(X\) be an \(E\)-valued random variable such that, conditional on \(\mathcal G\), \(X\) is independent of those seeds. If
\[
\prod_{j=1}^k |Y_j(X)|\in L^1,
\]
then conditioning first on \((\mathcal G,X)\) gives
\[
\mathbb E\!\left[
\prod_{j=1}^k Y_j(X)
\,\middle|\,
\mathcal G,X
\right]
=
\prod_{j=1}^k
\mathbb E[Y_j(X)\mid\mathcal G,X].
\tag{2}
\]
Thus a random parent position may be exposed before the child seeds are averaged, provided it does not reveal those seeds.

## Fresh centered Gaussian marks

The same point appears in heat-semigroup derivative weights. Let \(r>0\), let \(Z\sim N(0,1)\), and write \(He_2(z)=z^2-1\). For bounded Borel \(f\),
\[
\widehat K_r f(x,Z)
=
\frac{He_2(Z)}{r}
\bigl(f(x+\sqrt r\,Z)-f(x)\bigr)
\tag{3}
\]
is integrable and
\[
\mathbb E[\widehat K_r f(x,Z)]
=
\partial_{xx}P_r f(x).
\tag{4}
\]
The subtraction is legitimate because \(\mathbb E He_2(Z)=0\).

More generally, if \(F\) is a random bounded field with
\[
\mathbb E\|F\|_\infty<\infty
\]
and \(Z\) is independent of \(F\) conditional on \(\mathcal G\), then
\[
\mathbb E[
\widehat K_r F(x,Z)
\mid
\mathcal G,F]
=
\partial_{xx}P_r F(x)
\tag{5}
\]
and the tower property may then be applied. Equation (5) requires the Gaussian mark to remain fresh at the conditioning stage where its mean-zero factor is used.

These statements are finite conditional-expectation identities. They do not by themselves give an infinite-depth branching representation or any depth-uniform moment estimate.
