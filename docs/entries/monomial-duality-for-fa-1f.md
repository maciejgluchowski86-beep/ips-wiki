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

This entry records the [signed additive set process](signed-additive-set-process.md) appearing in [monomial duality for spin systems](monomial-duality-for-spin-systems.md) for the [FA-1f model](fa-1f-model.md). Write \(p=1-q\), where \(q\) is the vacancy density. The source-keeping empty update is omitted: \(\beta_i(\vn)=0\).

Only the rates listed below are nonzero. All omitted rates are zero, and signs attached to zero rates are irrelevant.

## Hard FA-1f

Assume \(N(i)\ne\vn\). The nonzero rates and signs at source site \(i\) are

$$
\delta_i(\vn)=p,
\qquad
\sigma_i^\delta(\vn)=+1,
$$

$$
\delta_i(N(i))=p,
\qquad
\sigma_i^\delta(N(i))=-1,
$$

and

$$
\beta_i(N(i))=1,
\qquad
\sigma_i^\beta(N(i))=+1.
$$

The site Feynman--Kac weight is

$$
V_i=2p.
$$

Thus \(V(A)=\sum_{i\in A}V_i=2p|A|\). If \(N(i)=\vn\), the hard FA-1f constraint at \(i\) is identically zero, so all dual rates and \(V_i\) are zero.

## Soft FA-1f

For [soft KCSM](soft-kcsm.md), the FA-1f constraint is

$$
c_i^\varepsilon(\eta)=1-(1-\varepsilon_i)\chi_{N(i)}(\eta),
\qquad \varepsilon_i\in[0,1].
$$

Assume \(N(i)\ne\vn\). The nonzero rates and signs are

$$
\delta_i(\vn)=p,
\qquad
\sigma_i^\delta(\vn)=+1,
$$

$$
\delta_i(N(i))=(1-\varepsilon_i)p,
\qquad
\sigma_i^\delta(N(i))=-1,
$$

and

$$
\beta_i(N(i))=1-\varepsilon_i,
\qquad
\sigma_i^\beta(N(i))=+1.
$$

The site Feynman--Kac weight is

$$
V_i^\varepsilon=2p-\varepsilon_i(1+p).
$$

If \(N(i)=\vn\), the only nonzero rate is

$$
\delta_i(\vn)=\varepsilon_i p,
\qquad
\sigma_i^\delta(\vn)=+1,
$$

and

$$
V_i^\varepsilon=-\varepsilon_i q.
$$

## Hard FA-1f with pure deaths

Add pure deaths at rates \(d_i\ge0\). By the [duality noise lemma](duality-noise-lemma.md), the dual rates and signs are exactly the hard FA-1f rates and signs above. Only the Feynman--Kac weight changes:

$$
V_i^d=2p-d_i
$$

when \(N(i)\ne\vn\), and

$$
V_i^d=-d_i
$$

when \(N(i)=\vn\).

## Soft FA-1f with pure deaths

With both softening and pure deaths, the dual rates and signs are exactly the soft FA-1f rates and signs above. Only the Feynman--Kac weight changes:

$$
V_i^{\varepsilon,d}=2p-\varepsilon_i(1+p)-d_i
$$

when \(N(i)\ne\vn\), and

$$
V_i^{\varepsilon,d}=-\varepsilon_i q-d_i
$$

when \(N(i)=\vn\).
