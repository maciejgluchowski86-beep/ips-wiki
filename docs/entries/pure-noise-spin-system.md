---
title: Pure noise spin system
status: definition
tags:
  - spin systems
  - noise
  - Bernoulli refresh
---

# Pure noise spin system

A pure noise spin system is a [spin system](spin-system.md) with no interaction between sites. Each site refreshes spontaneously from a Bernoulli law.

Let \(q_i^{\mathrm{noise}}\in[0,1]\), let \(p_i^{\mathrm{noise}}=1-q_i^{\mathrm{noise}}\), and let \(\lambda_i\ge0\). The pure noise generator is

$$
\mathcal L^{\mathrm{noise}} f(\eta)
=
\sum_{i\in\Lambda}\lambda_i
\left(E_i^{q_i^{\mathrm{noise}}}f(\eta)-f(\eta)\right).
$$

Equivalently, the site \(i\) flip rate is

$$
\lambda_i\left(q_i^{\mathrm{noise}}\eta(i)+p_i^{\mathrm{noise}}(1-\eta(i))\right).
$$

Thus pure noise has only empty-neighbour spin-rate coefficients:

$$
 c_i^0(\vn)=\lambda_i p_i^{\mathrm{noise}},
\qquad
 c_i^1(\vn)=\lambda_i q_i^{\mathrm{noise}}.
$$

A pure-noise perturbation of another spin system means adding \(\mathcal L^{\mathrm{noise}}\) to its generator. This changes only the empty-neighbour coefficients \(c_i^0(\vn)\) and \(c_i^1(\vn)\), and leaves all nonempty-neighbour coefficients unchanged.