---
title: Duality noise lemma
status: observation
audit: current
tags:
  - duality
  - noise
  - Feynman-Kac
---

# Duality noise lemma

Suppose a duality function $H$ satisfies the generator relation

$$
\cL_\eta H(y,\eta)=\cD_yH(y,\eta)+V(y)H(y,\eta).
$$

Let $\mathcal N$ be another Markov generator on the $\eta$-space such that

$$
\mathcal N_\eta H(y,\eta)=-r(y)H(y,\eta)
$$

for some $r(y)\ge0$. Then, for every $\varepsilon\ge0$,

$$
(\cL+\varepsilon\mathcal N)_\eta H(y,\eta)
=
\cD_yH(y,\eta)+(V(y)-\varepsilon r(y))H(y,\eta).
$$

Thus, at the generator level, adding such a perturbation leaves the dual generator unchanged and subtracts $\varepsilon r$ from the Feynman--Kac potential. Any corresponding semigroup statement still requires the usual Feynman--Kac hypotheses for the processes involved.

## Monomial examples

For the [monomial](monomials.md)

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i),
$$

pure deaths act diagonally. If

$$
\mathcal N^0 f(\eta)
=
\sum_{i\in\Lambda}d_i\left(f(\eta^{i,0})-f(\eta)\right),
\qquad d_i\ge0,
$$

then

$$
\mathcal N^0\chi_A=-\left(\sum_{i\in A}d_i\right)\chi_A.
$$

For the conjugate monomial

$$
\bar\chi_A(\eta)=\prod_{i\in A}(1-\eta(i)),
$$

pure births act diagonally. If

$$
\mathcal N^1 f(\eta)
=
\sum_{i\in\Lambda}b_i\left(f(\eta^{i,1})-f(\eta)\right),
\qquad b_i\ge0,
$$

then

$$
\mathcal N^1\bar\chi_A=-\left(\sum_{i\in A}b_i\right)\bar\chi_A.
$$

These identities are checked one site at a time and are the only content asserted here.
