---
title: Pure noise spin system
status: definition
tags:
  - spin systems
  - noise
  - Bernoulli refresh
---

# Pure noise spin system

A pure noise spin system is a [spin system](spin-system.md) with no interaction between sites. Each site refreshes spontaneously from a prescribed Bernoulli law.

Let \(r=(r_i)_{i\in\Lambda}\) with \(r_i\in[0,1]\). The pure noise generator is

$$
\mathcal N^r f(\eta)
=
\sum_{i\in\Lambda}
\left((1-r_i)f(\eta^{i,0})+r_i f(\eta^{i,1})-f(\eta)\right).
$$

Equivalently, the site \(i\) flip rate is

$$
(1-r_i)\eta(i)+r_i(1-\eta(i)).
$$

Thus pure noise has only empty-neighbour spin-rate coefficients:

$$
 c_i^0(\vn)=r_i,
\qquad
 c_i^1(\vn)=1-r_i.
$$

A pure-noise perturbation of another spin system means adding \(\mathcal N^r\) to its generator. This changes only the empty-neighbour coefficients \(c_i^0(\vn)\) and \(c_i^1(\vn)\), and leaves all nonempty-neighbour coefficients unchanged.
