---
title: Centered-moment order preservation
status: proved here
audit: current
tags:
  - patch positivity
  - centered moments
  - monotonicity
  - moment order
---

# Centered-moment order preservation

Let a spin system be [patch positive](patch-positivity-property.md), with [patch threshold profile](patch-critical-density.md) $\mathbf p^\star$. Use the centered monomials, order $\preceq_*$, and cone $\mathcal M_*$ from [centered-moment order and cones](high-density-measure.md).

## Theorem

For probability measures $\mu$ and $\nu$,

$$
\mu\preceq_*\nu
\quad\Longrightarrow\quad
\mu P_t\preceq_*\nu P_t
\qquad(t\ge0).
\tag{1}
$$

No assumption that $\mu$ or $\nu$ belongs to $\mathcal M_*$ is required. In particular,

$$
\mu\in\mathcal M_*
\quad\Longrightarrow\quad
\mu P_t\in\mathcal M_*.
\tag{2}
$$

Moreover,

$$
\mu\preceq_*\nu
\quad\Longrightarrow\quad
(\mu P_t)(\chi_A)\le(\nu P_t)(\chi_A)
$$

for every finite $A$.

## Centered-monomial generator

For $S\subseteq N(i)$ set

$$
h_i(S)
=
c_i^0(S)-p_i^\star\bigl(c_i^0(S)+c_i^1(S)\bigr),
$$

and for nonempty $S$ set

$$
b_i(S)=-c_i^0(S)-c_i^1(S).
$$

Patch positivity and the threshold formula imply

$$
h_i(S)\ge0,
\qquad
b_i(S)\ge0.
$$

A direct calculation gives

$$
\cL\chi_A^*
=
\sum_{i\in A}
\left[
-r_i\chi_A^*
+
\sum_{S\subseteq N(i)}
 h_i(S)\chi_S\chi_{A\setminus\{i\}}^*
+
\sum_{\substack{S\subseteq N(i)\\S\ne\vn}}
 b_i(S)\chi_S\chi_A^*
\right].
\tag{3}
$$

For finite $B,S$,

$$
\chi_S\chi_B^*
=
\left(\prod_{j\in S\cap B}(1-p_j^\star)\right)
\sum_{R\subseteq S}
\left(\prod_{j\in S\setminus R}p_j^\star\right)
\chi_{R\cup(B\setminus S)}^*.
\tag{4}
$$

All coefficients in (4) are nonnegative. In finite volume, the matrix of $\cL$ in the centered-monomial basis therefore has nonnegative off-diagonal entries, and so does its exponential. Finite propagation passes the conclusion to infinite volume, proving (1).

## Product-profile comparisons

If

$$
\mathbf p^\star\le\mathbf p\le\mathbf q,
$$

then

$$
(\mu_{\mathbf p}P_t)(\chi_A)
\le
(\mu_{\mathbf q}P_t)(\chi_A).
$$

More generally, if $\mathbf q\le\mathbf p$ and $\mathbf q+\mathbf p\ge2\mathbf p^\star$, then the same inequality holds. These are centered-moment comparisons, not stochastic-domination statements.
