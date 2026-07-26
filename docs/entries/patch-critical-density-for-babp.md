---
title: Patch critical density for BABP
status: proved here
tags:
  - BABP
  - patch
  - critical density
  - KCSM
---

# Patch critical density for BABP

For the [biased annihilating branching process](babp-model.md) at a site with \(N(i)\ne\vn\), the [patch critical density](patch-critical-density.md) equals the equilibrium density \(p=1-q\) of ones:

$$
p_i^\star=p.
$$

Thus a translation-invariant BABP has

$$
p^\star=p.
$$

## Proof

The purpose is to evaluate the general coefficient formula. Every nonempty target is a singleton \(\{j\}\), and its two spin-rate coefficients are

$$
c_i^0(\{j\})=-p,
\qquad
c_i^1(\{j\})=-q.
$$

Since their sum is \(-1\), every singleton gives the same threshold:

$$
\frac{c_i^0(\{j\})}
{c_i^0(\{j\})+c_i^1(\{j\})}
=
\frac{-p}{-p-q}
=
p.
$$

Taking the supremum over the singleton targets proves \(p_i^\star=p\). If \(N(i)=\vn\), there are no nonempty targets and the coefficient formula gives \(p_i^\star=0\).
