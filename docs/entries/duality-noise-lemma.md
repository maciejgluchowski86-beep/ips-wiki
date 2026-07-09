---
title: Duality noise lemma
status: proved here
tags:
  - duality
  - noise
  - Feynman-Kac
---

# Duality noise lemma

Let \((\eta_t)\) have generator \(\cL\), and suppose \(H\) has the [duality](duality.md) relation

$$
\cL_\eta H(y,\eta)=\cD_yH(y,\eta)+V(y)H(y,\eta).
$$

Let \(\mathcal N\) be another Markov generator on the \(\eta\)-space. In this context, \(\mathcal N\) is called noise for \(H\) if

$$
\mathcal N_\eta H(y,\eta)=-r(y)H(y,\eta)
$$

for some \(r(y)\ge0\). Then, for every \(\varepsilon\ge0\),

$$
(\cL+\varepsilon\mathcal N)_\eta H(y,\eta)
=
\cD_yH(y,\eta)+(V(y)-\varepsilon r(y))H(y,\eta).
$$

Thus \(\cL\) and \(\cL+\varepsilon\mathcal N\) have the same dual process. The perturbation only decreases the Feynman--Kac potential from \(V\) to \(V-\varepsilon r\).

## Monomial examples

For the monomial

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i),
$$

pure deaths are noise. If

$$
\mathcal N^0 f(\eta)
=
\sum_{i\in\Lambda}d_i\eta(i)\left(f(\eta^{i,0})-f(\eta)\right),
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

pure births are noise. If

$$
\mathcal N^1 f(\eta)
=
\sum_{i\in\Lambda}b_i(1-\eta(i))\left(f(\eta^{i,1})-f(\eta)\right),
\qquad b_i\ge0,
$$

then

$$
\mathcal N^1\bar\chi_A=-\left(\sum_{i\in A}b_i\right)\bar\chi_A.
$$

## Proof

The result follows by adding the eigenfunction identity for \(\mathcal N\) to the duality identity for \(\cL\). The monomial examples follow by checking one site at a time.
