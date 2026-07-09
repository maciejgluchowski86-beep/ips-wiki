---
title: Monomial duality for FA-1f
status: proved here
tags:
  - duality
  - FA-1f
  - monomials
  - KCSM
---

# Monomial duality for FA-1f

This entry records the specialization of [monomial duality for spin systems](monomial-duality-for-spin-systems.md) to the [FA-1f model](fa-1f-model.md). The resulting dual process is the [signed additive set process](signed-additive-set-process.md) determined by the coefficients below.

The notation is that of the general monomial duality entry. Thus

$$
a_i^\delta(S)=c_i^0(S),
\qquad
a_i^\beta(S)=-c_i^0(S)-c_i^1(S),
$$

and the nonnegative rates and signs are obtained from these signed coefficients. The convention \(\beta_i(\vn)=0\) is in force.

## Hard FA-1f

For hard FA-1f on a site with \(N(i)\ne\vn\), the only nonzero signed coefficients are

$$
a_i^\delta(\vn)=p,
\qquad
a_i^\delta(N(i))=-p,
$$

and

$$
a_i^\beta(\vn)=-1,
\qquad
a_i^\beta(N(i))=1.
$$

All other coefficients vanish. Therefore the source-killing rates are \(p\) for \(S=\vn\) and \(p\) for \(S=N(i)\), with signs \(+1\) and \(-1\), respectively. The only nonzero source-keeping rate is \(1\) for \(S=N(i)\), with sign \(+1\).

The Feynman--Kac potential is

$$
V(A)=\sum_{i\in A}V_i,
\qquad
V_i=2p.
$$

If \(N(i)=\vn\), the hard FA-1f constraint is identically zero at \(i\), so the site contributes no rates and no potential.

## Soft FA-1f

For [soft KCSM](soft-kcsm.md), the FA-1f constraint is replaced by

$$
c_i^\varepsilon(\eta)=1-(1-\varepsilon_i)\chi_{N(i)}(\eta).
$$

For \(N(i)\ne\vn\), the nonzero signed coefficients are

$$
a_i^\delta(\vn)=p,
\qquad
a_i^\delta(N(i))=-(1-\varepsilon_i)p,
$$

and

$$
a_i^\beta(\vn)=-1,
\qquad
a_i^\beta(N(i))=1-\varepsilon_i.
$$

Consequently,

$$
V_i^\varepsilon=2p-\varepsilon_i(1+p),
\qquad
V^\varepsilon(A)=\sum_{i\in A}V_i^\varepsilon.
$$

If \(N(i)=\vn\), then \(c_i^\varepsilon\equiv\varepsilon_i\). The only nonzero source-killing rate is \(\varepsilon_i p\) for \(S=\vn\), and

$$
V_i^\varepsilon=-\varepsilon_i q.
$$

## Adding pure deaths

Add pure deaths at rates \(d_i\ge0\):

$$
\mathcal N_d^0 f(\eta)=\sum_{i\in\Lambda}d_i\eta(i)\left(f(\eta^{i,0})-f(\eta)\right).
$$

By the [duality noise lemma](duality-noise-lemma.md), this perturbation does not change the dual process. It only subtracts \(d_i\) from the site potential. Thus, for \(N(i)\ne\vn\),

$$
V_i^{d}=2p-d_i
$$

for hard FA-1f with pure deaths, and

$$
V_i^{\varepsilon,d}=2p-\varepsilon_i(1+p)-d_i
$$

for soft FA-1f with pure deaths. If \(N(i)=\vn\), the soft-death potential is \(-\varepsilon_i q-d_i\).
