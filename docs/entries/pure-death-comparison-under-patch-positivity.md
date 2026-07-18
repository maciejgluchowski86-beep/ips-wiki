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

Removing an environment-independent pure-death component from a patch-positive spin system increases its evolved [monomial](monomials.md) moments. The comparison passes to unique [invariant measures](invariant-measure.md).

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
a_i\bigl(f(\eta^{i,0})-f(\eta)\bigr),
\qquad
a_i\ge0.
$$

Thus \(\cL'\) is obtained from \(\cL\) by decreasing its pure-death rates. Let \(P_t\) and \(P_t'\) be the corresponding semigroups.

**Lemma.** Suppose that \(\cL\) has the [patch positivity property](patch-positivity-property.md). Then \(\cL'\) also has patch positivity and has the same [patch critical density](patch-critical-density.md) \(\mathbf p^\star\). Moreover, for every [high-density measure](high-density-measure.md) \(\nu\), every \(A\Subset\Lambda\), and every \(t\ge0\),

$$
\nu\bigl(P_t\chi_A\bigr)
\le
\nu\bigl(P_t'\chi_A\bigr).
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
-
c_i^0(\vn)c_i^1(S).
$$

For the reduced-death system,

$$
D_{i,S}'
=
D_{i,S}-a_i c_i^0(S).
$$

If \(c_i^0(S)\le0\), then \(D_{i,S}'\ge D_{i,S}\ge0\). If \(c_i^0(S)>0\), patch positivity gives \(c_i^1(S)\le-c_i^0(S)<0\), and therefore \(D_{i,S}'\ge0\) directly. Hence \(\cL'\) has patch positivity. Its critical density is unchanged because the critical-density formula depends only on the nonempty-neighbour coefficients.

The two systems have the same successful-interaction skeleton. Removing deaths increases the site Feynman--Kac weight from \(V_i\) to \(V_i+a_i\), and increases the corresponding function \(\psi_i\) in every [patch contribution](patch-contribution.md). Inspection of the four contribution formulas therefore gives

$$
0\le C(P)\le C'(P)
$$

for every bulk patch, and

$$
0\le C(\mathbf p,P)\le C'(\mathbf p,P)
$$

for every end patch whenever \(\mathbf p\ge\mathbf p^\star\). The [patch representation](patch-representation-of-spin-systems.md) now gives (1) skeleton by skeleton for Bernoulli product measures. Averaging over the mixing profile proves the result for every high-density measure.

## Invariant-measure comparison

**Corollary.** Under the hypotheses of the lemma, suppose additionally that the two spin systems have unique invariant measures \(\pi\) and \(\pi'\). Then

$$
\pi(\chi_A)\le\pi'(\chi_A)
\qquad
\text{for every }A\Subset\Lambda.
\tag{2}
$$

### Proof

Apply (1) with the all-one product measure \(\mu_{\mathbf1}\), and average over \(t\in[0,T]\). The resulting Cesàro measures satisfy

$$
\frac1T\int_0^T
\mu_{\mathbf1}\bigl(P_t\chi_A\bigr)\,dt
\le
\frac1T\int_0^T
\mu_{\mathbf1}\bigl(P_t'\chi_A\bigr)\,dt.
$$

Every subsequential weak limit of either family of Cesàro measures is invariant. Uniqueness therefore implies convergence to \(\pi\) and \(\pi'\), respectively. Letting \(T\to\infty\) proves (2).

The order in (2) compares all joint occupation probabilities. It does not by itself imply stochastic domination.
