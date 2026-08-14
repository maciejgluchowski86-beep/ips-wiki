---
title: Hermite polynomials and Gaussian chaos
status: standard fact
tags:
  - probability
  - Gaussian analysis
  - Hermite polynomial
  - Wiener chaos
  - PDE
---

# Hermite polynomials and Gaussian chaos

Hermite polynomials are the orthogonal polynomials of Gaussian measure. They appear automatically when derivatives are transferred through a heat kernel: a \(k\)-th spatial derivative produces the \(k\)-th Hermite polynomial. Their \(L^2\) normalization explains why composing derivative transfers can have a very different scale from multiplying edgewise absolute moments.

**References.** Svante Janson, *Gaussian Hilbert Spaces*, Cambridge University Press, 1997. David Nualart, *The Malliavin Calculus and Related Topics*, second edition, Springer, 2006. See [References](../meta/references.md).

## Definition

The *probabilists' Hermite polynomials* are

$$
He_k(z)
=
(-1)^k e^{z^2/2}
\frac{d^k}{dz^k}e^{-z^2/2},
\qquad k\geq0.
\tag{1}
$$

The first few are

$$
He_0(z)=1,
\qquad
He_1(z)=z,
\qquad
He_2(z)=z^2-1,
\qquad
He_4(z)=z^4-6z^2+3.
$$

This wiki always uses the probabilists' normalization; the physicists' Hermite polynomials have a different scaling.

## Orthogonality

If \(Z\sim N(0,1)\), then

$$
\mathbb E[He_m(Z)He_n(Z)]
=
 n!\,\ind(m=n).
\tag{2}
$$

Consequently,

$$
\lVert He_n(Z)\rVert_{L^2}
=
\sqrt{n!}.
\tag{3}
$$

Equation (2) follows by repeated Gaussian integration by parts, or from the generating function

$$
\exp\left(tz-\frac{t^2}{2}\right)
=
\sum_{n=0}^\infty He_n(z)\frac{t^n}{n!}.
\tag{4}
$$

## Heat-kernel derivative formula

For bounded measurable \(G\), Gaussian integration by parts gives

$$
\partial_x^nP_tG(x)
=
 t^{-n/2}
\mathbb E\left[
G(x+\sqrt t\,Z)He_n(Z)
\right].
\tag{5}
$$

Cauchy--Schwarz and (3) imply

$$
\left|
\partial_x^nP_tG(x)
\right|
\leq
 t^{-n/2}\sqrt{n!}\,
\bigl(P_t|G|^2(x)\bigr)^{1/2}.
\tag{6}
$$

In particular, if \(G\) is bounded,

$$
\lVert\partial_x^nP_tG\rVert_\infty
\leq
 t^{-n/2}\sqrt{n!}\,\lVert G\rVert_\infty.
\tag{7}
$$

The same formulas hold for periodic \(G\) by applying them to its periodic lift.

## Example: the second-order absolute moment

For \(He_2(Z)=Z^2-1\),

$$
h_2
:=
\mathbb E|He_2(Z)|
=
4\varphi(1)
=
2\sqrt{\frac{2}{\pi e}},
\tag{8}
$$

where \(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\). To see this, symmetry and \(\mathbb E(Z^2-1)=0\) give

$$
\mathbb E|Z^2-1|
=
4\int_1^\infty(z^2-1)\varphi(z)\,dz,
$$

and integration by parts gives the value \(4\varphi(1)\).

## Gaussian and Wiener chaos

Let \(Z_1,Z_2,\ldots\) be independent standard Gaussian variables. The *\(k\)-th Gaussian chaos* is the closed subspace of \(L^2\) spanned by products

$$
\prod_i He_{\alpha_i}(Z_i)
$$

with only finitely many nonzero \(\alpha_i\) and total degree \(\sum_i\alpha_i=k\). In a Brownian setting these orthogonal subspaces are usually called *Wiener chaoses*. The Wiener-chaos decomposition expresses square-integrable Gaussian functionals as an orthogonal sum of their chaos components.

For one Gaussian variable, the \(k\)-th chaos is simply the one-dimensional span of \(He_k(Z)\).

## Why composition changes the scale

A single \(2m\)-th derivative transfer has the \(L^2\) factor \(\sqrt{(2m)!}\). If an ordered \(m\)-fold time integral contributes the simplex factor \(1/m!\), the resulting scale is

$$
\frac{\sqrt{(2m)!}}{m!}
=
\sqrt{\binom{2m}{m}}
\sim
\frac{2^m}{(\pi m)^{1/4}}.
\tag{9}
$$

Thus a composed derivative chain can have geometric growth even though treating the constituent second-derivative weights separately produces products of singular absolute moments. Formula (9) is only a statement about the composed Gaussian derivative operator. If spatially varying multiplication operators are inserted between derivative transfers, the semigroup derivatives no longer collapse automatically to a single Hermite polynomial.