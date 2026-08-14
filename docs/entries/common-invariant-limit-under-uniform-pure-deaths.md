---
title: Common invariant limit under uniform pure deaths
status: conditional
audit: current
tags:
  - spin systems
  - invariant measures
  - local functions
  - patch positivity
  - pure death
---

# Common invariant limit under uniform pure deaths

This page records the project common-limit theorem only as a **conditional statement**. The theorem has not completed the current verification protocol, and several of its patch prerequisites remain unverified.

## Assumptions

Let $\Lambda$ be a [polynomial-growth lattice](polynomial-growth-lattice.md) with exponent $D$, and let $\cL$ be the generator of a uniformly bounded finite-range spin system. Assume that there is $\varepsilon>0$ such that

$$
c_i^1(\xi)\ge\varepsilon
\qquad
\text{for every }i\in\Lambda
\text{ and }\xi\in\{0,1\}^{\Lambda}.
\tag{1}
$$

In addition to the standard existence assumptions for the spin-system semigroup, assume all of the following project-specific prerequisites:

1. the conditional Feynman--Kac duality in [monomial duality for spin systems](monomial-duality-for-spin-systems.md) is valid with the required nonexplosion and integrability;
2. the conditional [patch factorization](patch-factorization.md), [patch contribution](patch-contribution.md) identities, and [patch representation of spin systems](patch-representation-of-spin-systems.md) are valid;
3. the conditional [patch positivity property](patch-positivity-property.md) and the associated critical profile $\mathbf p^\star$ are valid for the contribution formulas being used;
4. after removing a uniform pure-death rate $\varepsilon$, the coefficientwise bulk and end contribution comparisons required by [pure-death comparison under patch positivity](pure-death-comparison-under-patch-positivity.md) hold, including the project identity that a terminal-$\mathsf O$ patch of lifetime $\Delta$ gains the factor $e^{-\varepsilon\Delta}$;
5. the conditional [undoing duality under confined interactions](undoing-duality-under-confined-interactions.md) identity and the finite-propagation estimate used to control confinement errors are valid; and
6. the full-patch limiting argument used by the project is justified, including local finiteness, integrability of the relevant nonnegative comparison weights, and the limiting/Fatou steps.

These prerequisites are named here because they are not currently verified project theorems.

## Conditional theorem

Under (1) and prerequisites 1--6, the current project argument gives an [invariant probability measure](invariant-measure.md) $\pi$ such that for every local function $f$ there is $K_f<\infty$ with

$$
\sup_{\nu\in\mathcal M_-}
\left|
\nu(P_tf)-\pi(f)
\right|
\le
K_f(1+t)^D e^{-\varepsilon t/2}.
\tag{2}
$$

Consequently, conditionally on the same prerequisites, $\nu P_t$ converges weakly to $\pi$ for every $\nu\in\mathcal M_-$. In particular this applies to $\mathcal M_\star\subseteq\mathcal M_-$ whenever the corresponding high-density classes are defined from the same valid critical profile.

The project identifies the limiting monomial moments by

$$
\pi(\chi_A)
=
\mathbb E_A\left[
\prod_{P\in\mathcal P}C(P)\,
\ind\left(|\mathcal P|<\infty\right)
\right],
\qquad A\Subset\Lambda,
\tag{3}
$$

with the integrand set to zero on $\{|\mathcal P|=\infty\}$. Formula (3) is part of the same unverified full-patch limiting argument and is not asserted independently.

## Conditional uniqueness corollary

If the same prerequisites hold and

$$
\mathbf p^\star\le\frac12\mathbf1,
$$

so that the project high-density calculation gives every probability measure in $\mathcal M_-$, then (2) yields, conditionally,

$$
\sup_{\xi\in\{0,1\}^{\Lambda}}
\left|P_tf(\xi)-\pi(f)\right|
\le
K_f(1+t)^D e^{-\varepsilon t/2}
$$

for every local $f$, and hence uniqueness of the invariant measure. This corollary inherits every unresolved prerequisite listed above.
