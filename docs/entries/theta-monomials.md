---
title: Theta monomials
status: definition
tags:
  - monomials
  - spin systems
  - duality
---

# Theta monomials

Theta monomials are one-parameter deformations of the ordinary [monomials](monomials.md) on \(\{0,1\}^\Lambda\). They are useful when changing basis for [spin-system](spin-system.md) generators and in variants of finite-set [duality](duality.md).

For \(\theta\in\R\), define

$$
u_\theta(x)=x+\theta(1-x)=\theta+(1-\theta)x,
\qquad x\in\{0,1\}.
$$

For \(A\Subset\Lambda\), set

$$
\chi_A^\theta(\eta)=\prod_{i\in A}u_\theta(\eta(i)).
$$

The barred convention is

$$
\bar\chi_A^\theta(\eta)=\chi_A^\theta(1-\eta)
=
\prod_{i\in A}\left(1-\eta(i)+\theta\eta(i)\right).
$$

Thus \(\chi_A^\theta\) assigns value \(1\) to state \(1\), while \(\bar\chi_A^\theta\) assigns value \(1\) to state \(0\). The case \(\theta=0\) gives the ordinary occupied-site monomial and its vacancy analogue.

## Special cases

$$
\chi_A^0=\chi_A,
\qquad
\bar\chi_A^0=\prod_{i\in A}(1-\eta(i)),
\qquad
\chi_A^1=\bar\chi_A^1=1.
$$

Also

$$
\chi_A^{-1}=\prod_{i\in A}(2\eta(i)-1),
\qquad
\bar\chi_A^{-1}=\prod_{i\in A}(1-2\eta(i)).
$$

## Basis property

If \(\theta\ne1\) and \(\Delta\Subset\Lambda\), then

$$
\{\chi_A^\theta:A\subseteq\Delta\}
$$

is a basis for functions depending only on \(\Delta\), hence for [local functions](local-functions.md) with dependence set contained in \(\Delta\). The one-site inversion identities are

$$
\eta(i)=\frac{u_\theta(\eta(i))-\theta}{1-\theta},
\qquad
1-\eta(i)=\frac{1-u_\theta(\eta(i))}{1-\theta}.
$$

The same statement holds for the barred basis by replacing \(\eta\) with \(1-\eta\).

## Algebraic identities

The empty product is

$$
\chi_\varnothing^\theta=\bar\chi_\varnothing^\theta=1.
$$

The one-site square identity is

$$
u_\theta^2=(1+\theta)u_\theta-\theta.
$$

Consequently,

$$
\chi_A^\theta\chi_B^\theta
=
\sum_{C\subseteq A\cap B}
(1+\theta)^{|C|}(-\theta)^{|A\cap B|-|C|}
\chi_{(A\triangle B)\cup C}^\theta.
$$

The same identity holds with every \(\chi^\theta\) replaced by \(\bar\chi^\theta\).

If \(i\notin A\), then

$$
\chi_A^\theta(\eta^i)=\chi_A^\theta(\eta),
\qquad
\bar\chi_A^\theta(\eta^i)=\bar\chi_A^\theta(\eta).
$$

If \(i\in A\), the flip identities are

$$
\begin{aligned}
\chi_A^\theta(\eta^i)-\chi_A^\theta(\eta)
&=
(1+\theta)\chi_{A\setminus\{i\}}^\theta(\eta)-2\chi_A^\theta(\eta),
\\
\bar\chi_A^\theta(\eta^i)-\bar\chi_A^\theta(\eta)
&=
(1+\theta)\bar\chi_{A\setminus\{i\}}^\theta(\eta)-2\bar\chi_A^\theta(\eta).
\end{aligned}
$$

These identities parallel the replacement identities for ordinary [monomials](monomials.md) and can be used in the same style of generator calculation as [monomial duality for spin systems](monomial-duality-for-spin-systems.md).
