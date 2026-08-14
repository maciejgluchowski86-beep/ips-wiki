---
title: Exponential relaxation under confined late interactions
status: conditional
audit: current
tags:
  - patch
  - ergodicity
  - spin systems
  - convergence to equilibrium
---

# Exponential relaxation under confined late interactions

This page records a conditional convergence statement for the modified system from [undoing duality under confined interactions](undoing-duality-under-confined-interactions.md). Its probabilistic identification with a patch term depends on the unverified confined-interaction identity.

## Assumptions

Assume the original spin system is uniformly bounded and finite range and that $\Lambda$ has [polynomial growth](polynomial-growth-lattice.md).

For every $R\Subset\Lambda$, assume the zero-boundary semigroup $P_t^{R,0}$ has a unique invariant measure $\nu_R$ and there is a rate $\gamma_1>0$, independent of $R$, such that for every bounded $f$ on $\{0,1\}^R$,

$$
\sup_{\eta\in\{0,1\}^R}
\left|P_t^{R,0}f(\eta)-\nu_R(f)\right|
\le C_R^0e^{-\gamma_1t}\|f\|_\infty
$$

for some $C_R^0<\infty$.

For exterior sites, define

$$
\gamma_2
=
\inf_{i\in\Lambda}
\left(c_i^0(\mathbf0)+c_i^1(\mathbf0)\right)
$$

and assume $\gamma_2>0$. Put $\gamma=\min(\gamma_1,\gamma_2)$. The modified generator $\cL_R$ then has the product invariant measure

$$
\mu_R
=
\nu_R\otimes
\bigotimes_{i\notin R}
\operatorname{Ber}\left(
\frac{c_i^0(\mathbf0)}{c_i^0(\mathbf0)+c_i^1(\mathbf0)}
\right).
$$

Assume also the local finite-propagation approximation used in the project: for each finite $A$, fixed $T$, and every $a>0$, there are local approximants $g_s$ to $g=P_T\chi_A$, supported in balls of radius $O(1+s)$, such that

$$
\|g-g_s\|_\infty\le C_{A,T,a}e^{-as}.
\tag{1}
$$

Finally, assume the conditional confined-interaction identity

$$
\mathbb E_A\left[W_t^\xi\ind(E_{T,t}^R)\right]
=
\left(P_{t-T}^RP_T\chi_A\right)(\xi).
\tag{2}
$$

## Conditional lemma

Under these assumptions, for every $A\Subset\Lambda$, $T<\infty$, $R\Subset\Lambda$, and $0<\gamma'<\gamma$, there is $C_{A,R,T,\gamma'}<\infty$ such that, for $t\ge T$,

$$
\sup_{\xi\in\{0,1\}^\Lambda}
\left|
\mathbb E_A\left[W_t^\xi\ind(E_{T,t}^R)\right]
-
\mu_R(P_T\chi_A)
\right|
\le
C_{A,R,T,\gamma'}e^{-\gamma'(t-T)}.
\tag{3}
$$

The analytic part of the current argument combines the product relaxation of the modified process, polynomial volume growth, and (1), then uses (2) to identify the result with the patch term. Equation (3) is therefore conditional on both the stated analytic hypotheses and the unresolved confined-interaction identity.
