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

For a spin system with the [patch positivity property](patch-positivity-property.md), the patch critical density is the smallest terminal one-density for which every end-patch contribution is nonnegative.

**References.** None yet.

## Definition

Use the [end-patch contribution](patch-contribution.md) \(C(p,P)\), which is affine in the terminal one-density \(p\). The patch critical density at site \(i\) is

$$
p_i^\star
=
\inf\left\{
p\in[0,1]:
C(p,P)\ge0
\text{ for every possible end patch }P\text{ based at }i
\right\}.
$$

The patch critical density profile is

$$
\mathbf p^\star=(p_i^\star)_{i\in\Lambda}.
$$

For a translation-invariant model the profile is constant, and its common value is denoted by \(p^\star\).

## Coefficient formula

In the coefficient notation of [monomial duality for spin systems](monomial-duality-for-spin-systems.md),

$$
p_i^\star
=
\max\left\{
0,
\sup_{\substack{
\vn\ne S\subseteq N(i)\\
c_i^0(S)+c_i^1(S)<0
}}
\frac{c_i^0(S)}
{c_i^0(S)+c_i^1(S)}
\right\}.
$$

Under patch positivity, every ratio contributing to the supremum is at most \(1\), so \(p_i^\star\in[0,1]\). The inner supremum is defined to be \(0\) when its index set is empty.

## Proof

The \(\mathsf{IE}\) end contribution is nonnegative for every \(p\in[0,1]\). For an \(\mathsf{OE}\) end patch with initial interaction target \(S\), the denominator is positive and the numerator is

$$
c_i^0(S)
-
\left(c_i^0(S)+c_i^1(S)\right)\psi_i(\Delta,p).
$$

Patch positivity gives

$$
c_i^0(S)+c_i^1(S)\le0,
$$

so this numerator is nondecreasing in \(p\). If

$$
c_i^0(\vn)+c_i^1(\vn)>0,
$$

then, as a function of the patch length, the numerator interpolates between

$$
c_i^0(S)
-
\left(c_i^0(S)+c_i^1(S)\right)p
$$

and

$$
\frac{
c_i^1(\vn)c_i^0(S)-c_i^0(\vn)c_i^1(S)
}{
c_i^0(\vn)+c_i^1(\vn)
}.
$$

The second expression is nonnegative by patch positivity. Hence the contribution is nonnegative for every patch length exactly when the first expression is nonnegative. If \(c_i^0(S)+c_i^1(S)<0\), this is equivalent to

$$
p
\ge
\frac{c_i^0(S)}
{c_i^0(S)+c_i^1(S)}.
$$

If \(c_i^0(S)+c_i^1(S)=0\), patch positivity gives \(c_i^0(S)\ge0\), so this target imposes no restriction. When \(c_i^0(\vn)+c_i^1(\vn)=0\), the same conclusion follows directly from \(\psi_i(\Delta,p)=p\). Taking the supremum over nonempty targets proves the formula.
