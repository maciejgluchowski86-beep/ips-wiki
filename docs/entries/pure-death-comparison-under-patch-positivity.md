---
title: Pure-death comparison under patch positivity
status: proved here
tags:
  - patch positivity
  - pure deaths
  - comparison
  - invariant measures
---

# Pure-death comparison under patch positivity

Removing an environment-independent pure-death component from a patch-positive spin system increases its evolved [monomial](monomials.md) moments from every [high-density measure](high-density-measure.md). The comparison passes to unique [invariant measures](invariant-measure.md).

## Pure-death comparison

Let \(\cL\) and \(\cL'\) be uniformly bounded finite-range [spin-system](spin-system.md) generators satisfying

$$
\cL=\cL'+\mathcal D_{\mathbf a},
$$

where

$$
\mathcal D_{\mathbf a}f(\eta)
=
\sum_{i\in\Lambda}
a_i\left(f(\eta^{i,0})-f(\eta)\right),
\qquad
a_i\ge0.
$$

Thus \(\cL'\) is obtained from \(\cL\) by decreasing its pure-death rates. Let \(P_t\) and \(P_t'\) be the corresponding semigroups.

**Lemma.** Suppose that \(\cL\) has the [patch positivity property](patch-positivity-property.md). Then \(\cL'\) also has patch positivity and has the same [patch critical density](patch-critical-density.md) \(\mathbf p^\star\). Moreover, for every \(\nu\in\mathcal M_\star\), every \(A\Subset\Lambda\), and every \(t\ge0\),

$$
\nu\left(P_t\chi_A\right)
\le
\nu\left(P_t'\chi_A\right).
\tag{1}
$$

### Proof

Pure-death removal changes only the empty-neighbour death coefficient:

$$
c_i^{\prime\,1}(\vn)=c_i^1(\vn)-a_i.
$$

All nonempty-neighbour coefficients and the dual interaction rates are unchanged. For \(\vn\ne S\subseteq N(i)\), write

$$
D_{i,S}
=
c_i^1(\vn)c_i^0(S)
-c_i^0(\vn)c_i^1(S).
$$

For the reduced-death system,

$$
D_{i,S}'
=
D_{i,S}-a_i c_i^0(S).
$$

If \(c_i^0(S)\le0\), then \(D_{i,S}'\ge D_{i,S}\ge0\). If \(c_i^0(S)>0\), patch positivity gives \(c_i^1(S)\le-c_i^0(S)<0\), and therefore \(D_{i,S}'\ge0\) directly. Hence \(\cL'\) has patch positivity. Its critical density is unchanged because the critical-density formula depends only on the nonempty-neighbour coefficients.

The two systems have the same successful-interaction skeleton. Removing deaths increases the site Feynman--Kac weight and the corresponding function \(\psi_i\) in every [patch contribution](patch-contribution.md). Inspection of the four contribution formulas gives

$$
0\le C(P)\le C'(P)
$$

for every bulk patch.

For an end patch \(P\) based at \(i=i(P)\), write its affine contribution around the common critical density as

$$
\begin{aligned}
C(z,P)
&=
C(p_i^\star,P)+b(P)(z-p_i^\star),
\\
C'(z,P)
&=
C'(p_i^\star,P)+b'(P)(z-p_i^\star).
\end{aligned}
$$

The end-patch formulas and patch positivity give

$$
0\le C(p_i^\star,P)\le C'(p_i^\star,P),
\qquad
0\le b(P)\le b'(P).
\tag{2}
$$

Indeed, the consistency normalizers are unchanged, while pure-death removal increases both \(\psi_i\) and the coefficient of its terminal value. For an \(\mathsf{OE}\)-patch the latter coefficient is nonnegative because

$$
-c_i^0(S)-c_i^1(S)\ge0.
$$

Distinct end patches are based at distinct sites. Consequently, for every end-patch family \(\mathcal E\),

$$
\nu\left[
\prod_{P\in\mathcal E}C(\eta(i(P)),P)
\right]
=
\sum_{\mathcal Q\subseteq\mathcal E}
\nu\left(
\chi_{\{i(P):P\in\mathcal Q\}}^\star
\right)
\prod_{P\in\mathcal Q}b(P)
\prod_{P\in\mathcal E\setminus\mathcal Q}
C(p_{i(P)}^\star,P).
\tag{3}
$$

Every term in (3) is nonnegative when \(\nu\in\mathcal M_\star\), and (2) orders it by the corresponding primed term. Combining this coefficientwise end-patch comparison with the bulk comparison, the [patch representation](patch-representation-of-spin-systems.md) gives (1) skeleton by skeleton.

## Invariant-measure comparison

**Corollary.** Under the hypotheses of the lemma, suppose additionally that the two spin systems have unique invariant measures \(\pi\) and \(\pi'\). Then

$$
\pi(\chi_A)\le\pi'(\chi_A)
\qquad
\text{for every }A\Subset\Lambda.
\tag{4}
$$

### Proof

Apply (1) with the all-one measure \(\mu_{\mathbf1}\in\mathcal M_\star\), and average over \(t\in[0,T]\). The resulting Cesàro measures satisfy

$$
\frac1T\int_0^T
\mu_{\mathbf1}\left(P_t\chi_A\right)\,dt
\le
\frac1T\int_0^T
\mu_{\mathbf1}\left(P_t'\chi_A\right)\,dt.
$$

Every subsequential weak limit of either family of Cesàro measures is invariant. Uniqueness therefore implies convergence to \(\pi\) and \(\pi'\), respectively. Letting \(T\to\infty\) proves (4).

The order in (4) compares all joint occupation probabilities. It does not by itself imply stochastic domination.
