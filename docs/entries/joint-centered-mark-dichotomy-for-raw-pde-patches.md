---
title: Joint centered-mark identities for Gaussian derivative weights
status: observation
audit: current
tags:
  - PDE
  - Gaussian analysis
  - Hermite polynomial
  - cancellation
  - conditional expectation
---

# Joint centered-mark identities for Gaussian derivative weights

Two elementary calculations show what can be gained by postponing an absolute value across more than one centered Gaussian derivative mark. The first is an integrable two-mark mixed-difference estimate. The second identifies the conditional score obtained when independent Gaussian increments are averaged at fixed total displacement.

Throughout, \(He_2(z)=z^2-1\).

## Two-mark mixed-difference gain

Fix \(0<\alpha<1\), let \(Z_1,Z_2\) be independent standard Gaussian variables, and for \(h\in\mathbb R\) write
\[
(\Delta_h f)(x)=f(x+h)-f(x).
\]
For \(r_1,r_2>0\), define
\[
\widehat{\mathcal K}_{r_1,r_2}f(x)
=
\frac{He_2(Z_1)}{r_1}
\frac{He_2(Z_2)}{r_2}
\Delta_{\sqrt{r_2}Z_2}
\Delta_{\sqrt{r_1}Z_1}f(x).
\tag{1}
\]

For \(f\in C^\alpha\),
\[
\|\Delta_{h_2}\Delta_{h_1}f\|_\infty
\le
2[f]_{C^\alpha}
\min\{|h_1|^\alpha,|h_2|^\alpha\}.
\tag{2}
\]
Indeed, apply the \(C^\alpha\) increment bound either before or after the second difference. Since
\[
\min\{a,b\}\le\sqrt{ab},
\]
(2) gives
\[
\mathbb E
\|\widehat{\mathcal K}_{r_1,r_2}f\|_\infty
\le
C_\alpha [f]_{C^\alpha}
r_1^{-1+\alpha/4}
r_2^{-1+\alpha/4},
\tag{3}
\]
where one may take
\[
C_\alpha
=
2\left(
\mathbb E\bigl[|He_2(Z)|\,|Z|^{\alpha/2}\bigr]
\right)^2.
\]
Both short-time exponents in (3) are strictly larger than \(-1\). Hence, for
\[
\Sigma_2(T)
=
\{(r_1,r_2)\in(0,\infty)^2:r_1+r_2<T\},
\]
\[
\int_{\Sigma_2(T)}
\mathbb E
\|\widehat{\mathcal K}_{r_1,r_2}f\|_\infty
\,dr_1dr_2
\le
C_\alpha [f]_{C^\alpha}
T^{\alpha/2}
\frac{\Gamma(\alpha/4)^2}
{\Gamma(1+\alpha/2)}.
\tag{4}
\]

The gain comes from forming the mixed difference before taking the first absolute moment. No intermediate loss of Hölder exponent is introduced between the two centered marks.

## Gaussian bridge conditional-score identity

Let \(m\ge1\), let \(Z_1,\ldots,Z_m\) be independent standard Gaussians, and let \(r_1,\ldots,r_m>0\). Set
\[
Y=\sum_{j=1}^m\sqrt{r_j}\,Z_j,
\qquad
R=\sum_{j=1}^m r_j,
\qquad
Z=\frac{Y}{\sqrt R}.
\tag{5}
\]
Then \(Z\sim N(0,1)\), and
\[
\boxed{
\mathbb E\left[
\left.
\prod_{j=1}^m\frac{He_2(Z_j)}{r_j}
\right|Y
\right]
=
\frac{He_{2m}(Z)}{R^m}.
}
\tag{6}
\]

To verify (6), test both sides against a bounded smooth function \(F(Y)\). Repeated Gaussian integration by parts gives
\[
\mathbb E\left[
F(Y)
\prod_{j=1}^m\frac{He_2(Z_j)}{r_j}
\right]
=
\mathbb E[F^{(2m)}(Y)].
\tag{7}
\]
On the other hand, the one-dimensional Hermite identity for \(Y=\sqrt R\,Z\) gives
\[
\mathbb E\left[
F(Y)\frac{He_{2m}(Z)}{R^m}
\right]
=
\mathbb E[F^{(2m)}(Y)].
\tag{8}
\]
Equations (7)--(8) identify the conditional expectations.

Formula (6) is a conditional averaging identity: the \(m-1\) Gaussian bridge coordinates orthogonal to the total displacement \(Y\) have been averaged before an absolute value is taken. It is a local mechanism, not an infinite-tree moment estimate.
