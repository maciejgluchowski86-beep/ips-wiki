---
title: Patch critical density
status: proved here
tags:
  - patch
  - patch positivity
  - critical density
  - spin systems
---

# Patch critical density

For a spin system with the [patch positivity property](patch-positivity-property.md), the patch critical density is the smallest terminal one-density for which every affine end-patch contribution is nonnegative. It may depend on the source site.

**References.** None yet.

## Affine end contribution

Let

$$
P=\{i\}\times[s_-,t)\in\mathcal E_t
$$

be an end patch based at \(i\). Since its [patch contribution](patch-contribution.md) depends on the terminal configuration only through \(\xi(i)\), define its affine extension by

$$
C^r(P)
=
(1-r)C(0,P)+rC(1,P),
\qquad r\in[0,1].
$$

Equivalently, \(C^r(P)\) is obtained from the end-patch formula by replacing \(\xi(i)\) with \(r\).

## Definition

The patch critical density at site \(i\) is

$$
p_i^\star
=
\inf\left\{
r\in[0,1]:
C^r(P)\ge0
\text{ for every possible end patch }P\text{ based at }i
\right\}.
$$

The collection

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}
$$

is the patch critical density profile. For a translation-invariant model it is constant, and its common value is denoted by \(p^\star\).

Patch positivity implies \(C^1(P)\ge0\) for every end patch, so \(p_i^\star\in[0,1]\).

## Coefficient formula

Use the coefficient notation from [monomial duality for spin systems](monomial-duality-for-spin-systems.md). For every nonempty \(S\subseteq N(i)\), set

$$
r_i(S)
=
\begin{cases}
\displaystyle
\max\left\{
0,
\frac{c_i^0(S)}
{c_i^0(S)+c_i^1(S)}
\right\},
& c_i^0(S)+c_i^1(S)<0,
\\[1.2em]
0,
& c_i^0(S)+c_i^1(S)=0.
\end{cases}
$$

Then

$$
p_i^\star
=
\sup_{\vn\ne S\subseteq N(i)}r_i(S),
$$

with the convention that the supremum is \(0\) when there is no nonempty interaction target.

Under patch positivity, \(0\le r_i(S)\le1\), so the formula indeed defines a density.

## Derivation

Write

$$
a=c_i^0(\vn),
\qquad
b=c_i^1(\vn),
\qquad
u=c_i^0(S),
\qquad
v=c_i^1(S).
$$

The \(\mathsf{SE}\) and \(\mathsf{IE}\) end contributions are nonnegative for every \(r\in[0,1]\), so only the \(\mathsf{OE}\) row can impose a positive threshold. Its denominator is positive whenever the patch can occur, and its numerator is

$$
N_{i,S}(\Delta,r)
=
u-(u+v)\psi_i(\Delta,r).
$$

Suppose first that \(a+b>0\). Then

$$
\psi_i(\Delta,r)
=
\frac{a}{a+b}
+
\left(r-\frac{a}{a+b}\right)e^{-(a+b)\Delta},
$$

and hence

$$
N_{i,S}(\Delta,r)
=
N_{i,S}(\infty,r)
+
\left(
N_{i,S}(0,r)-N_{i,S}(\infty,r)
\right)e^{-(a+b)\Delta},
$$

where

$$
N_{i,S}(0,r)=u-(u+v)r
$$

and

$$
N_{i,S}(\infty,r)
=
\frac{bu-av}{a+b}.
$$

The patch-positivity criterion gives

$$
u+v\le0,
\qquad
bu-av\ge0.
$$

Thus the limiting numerator is already nonnegative, and the numerator is nonnegative for every patch length if and only if

$$
u-(u+v)r\ge0.
$$

If \(u+v<0\), this is equivalent to

$$
r\ge\frac{u}{u+v}.
$$

If \(u+v=0\), patch positivity forces \(u\ge0\), so this target imposes no positive threshold.

If \(a+b=0\), then \(\psi_i(\Delta,r)=r\). The degenerate patch-positivity criterion gives \(u+v\le0\) and \(v\le0\), and the same calculation yields the same threshold. Taking the positive part and then the supremum over nonempty targets proves the coefficient formula.
