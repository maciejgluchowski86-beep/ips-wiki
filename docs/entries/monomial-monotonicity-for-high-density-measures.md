---
title: Monomial monotonicity for high-density measures
status: proved here
tags:
  - patch positivity
  - high-density measure
  - centered moments
  - monotonicity
---

# Monomial monotonicity for high-density measures

For a uniformly bounded finite-range spin system with the [patch positivity property](patch-positivity-property.md), the semigroup preserves the order induced by moments centered at the [patch critical density](patch-critical-density.md). Ordinary [monomial](monomials.md) monotonicity and preservation of the [high-density class](high-density-measure.md) follow from this stronger statement.

**References.** None yet.

## Theorem

Let \(\nu_0\) and \(\nu_1\) be probability measures such that

$$
\nu_0\left(\chi_B^\star\right)
\le
\nu_1\left(\chi_B^\star\right)
\qquad
\text{for every }B\Subset\Lambda.
$$

Then, for every \(A\Subset\Lambda\) and \(t\ge0\),

$$
\nu_0\left(P_t\chi_A^\star\right)
\le
\nu_1\left(P_t\chi_A^\star\right),
\tag{1}
$$

and

$$
\nu_0\left(P_t\chi_A\right)
\le
\nu_1\left(P_t\chi_A\right).
\tag{2}
$$

In particular,

$$
\mu\in\mathcal M_\star
\quad\Longrightarrow\quad
\mu P_t\in\mathcal M_\star,
\tag{3}
$$

and every \(\mu\in\mathcal M_\star\) satisfies

$$
\mu_{\mathbf p^\star}\left(P_t\chi_A\right)
\le
\mu\left(P_t\chi_A\right).
\tag{4}
$$

There is no corresponding all-one upper bound for an arbitrary measure in \(\mathcal M_\star\) without an additional upper bound on its centered moments.

## Proof

Use the coefficient notation from [monomial duality for spin systems](monomial-duality-for-spin-systems.md). For \(S\subseteq N(i)\), put

$$
d_i(S)
=
c_i^0(S)
-p_i^\star\left(c_i^0(S)+c_i^1(S)\right),
$$

and, for \(S\ne\vn\), put

$$
b_i(S)
=
-c_i^0(S)-c_i^1(S).
$$

Patch positivity and the definition of \(p_i^\star\) give

$$
d_i(S)\ge0
\quad(S\subseteq N(i)),
\qquad
b_i(S)\ge0
\quad(\vn\ne S\subseteq N(i)).
\tag{5}
$$

For nonempty \(S\), these are precisely the sign condition and threshold inequality in the patch-positivity and critical-density criteria. For \(S=\vn\), write

$$
r_i=c_i^0(\vn)+c_i^1(\vn).
$$

If \(r_i>0\), patch positivity gives \(p_i^\star\le c_i^0(\vn)/r_i\), and hence \(d_i(\vn)\ge0\). If \(r_i=0\), then \(d_i(\vn)=0\).

A direct generator calculation gives

$$
\cL\chi_A^\star
=
\sum_{i\in A}
\Bigg[
-r_i\chi_A^\star
+
\sum_{S\subseteq N(i)}
d_i(S)\chi_S\chi_{A\setminus\{i\}}^\star
+
\sum_{\vn\ne S\subseteq N(i)}
b_i(S)\chi_S\chi_A^\star
\Bigg].
\tag{6}
$$

No new dual process is needed to read the signs in this formula. For finite \(B\) and \(S\),

$$
\chi_S\chi_B^\star
=
\left(
\prod_{j\in S\cap B}(1-p_j^\star)
\right)
\sum_{R\subseteq S}
\left(
\prod_{j\in S\setminus R}p_j^\star
\right)
\chi_{R\cup(B\setminus S)}^\star.
\tag{7}
$$

All coefficients in (7) are nonnegative. Thus, after expanding the products in (6), the generator matrix in the centered-monomial basis has nonnegative off-diagonal entries. Its only a priori negative term is the diagonal term \(-\sum_{i\in A}r_i\).

In finite volume, the exponential of this Metzler matrix has nonnegative entries. The usual finite-volume approximation, using finite range and uniformly bounded rates, gives the same conclusion in infinite volume. Therefore every finite signed measure \(\lambda\) satisfying

$$
\lambda\left(\chi_B^\star\right)\ge0
\qquad(B\Subset\Lambda)
$$

also satisfies

$$
\lambda\left(P_t\chi_A^\star\right)\ge0.
\tag{8}
$$

Apply (8) to \(\lambda=\nu_1-\nu_0\) to obtain (1). Since

$$
\chi_A
=
\sum_{B\subseteq A}
\left(\prod_{i\in A\setminus B}p_i^\star\right)
\chi_B^\star,
$$

the same order implies (2). Taking \(\lambda=\mu\) proves (3). Finally, the nonempty centered moments of \(\mu_{\mathbf p^\star}\) vanish, so (4) follows from (2).

## Product-profile corollaries

If

$$
\mathbf p^\star\le\mathbf p\le\mathbf q,
$$

then

$$
\mu_{\mathbf p}\left(P_t\chi_A\right)
\le
\mu_{\mathbf q}\left(P_t\chi_A\right).
$$

More generally, suppose that two mixing laws admit a coupling \((\mathbf p,\mathbf q)\) with this coordinatewise order almost surely. Averaging the product-profile inequality gives the same comparison for the corresponding mixtures.

The reflected comparison below the critical profile is also a consequence. If

$$
\mathbf q\le\mathbf p,
\qquad
\mathbf q+\mathbf p\ge2\mathbf p^\star,
$$

then

$$
\left|q_i-p_i^\star\right|
\le
p_i-p_i^\star
\qquad(i\in\Lambda).
$$

Hence

$$
\mu_{\mathbf q}\left(\chi_B^\star\right)
\le
\mu_{\mathbf p}\left(\chi_B^\star\right)
$$

for every finite \(B\), and therefore

$$
\mu_{\mathbf q}\left(P_t\chi_A\right)
\le
\mu_{\mathbf p}\left(P_t\chi_A\right).
$$

This comparison may again be averaged under any coupling satisfying the two displayed profile inequalities almost surely.
