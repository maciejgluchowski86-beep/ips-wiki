---
title: Bernoulli product measure
status: definition
tags:
  - Bernoulli measure
  - product measure
  - spin systems
---

# Bernoulli product measure

A Bernoulli product measure is the law of independent \(\{0,1\}\)-valued spins with prescribed one-site densities.

**References.** Liggett, *Interacting Particle Systems*; Liggett, *Stochastic Interacting Systems*.

## Definition

Let \(\Lambda\) be a countable [lattice](lattice-and-graph.md), let

$$
\Omega=\{0,1\}^\Lambda,
$$

and fix a one-density profile

$$
\mathbf p=(p_i)_{i\in\Lambda}\in[0,1]^\Lambda.
$$

The Bernoulli product measure with profile \(\mathbf p\) is

$$
\mu_{\mathbf p}
=
\bigotimes_{i\in\Lambda}
\left((1-p_i)\delta_0+p_i\delta_1\right).
$$

Thus the coordinate spins are independent and

$$
\mu_{\mathbf p}(\eta(i)=1)=p_i.
$$

If \(p_i=p\) at every site, the measure is homogeneous and is denoted by \(\mu_p\).

## Monomial moments

For every \(A\Subset\Lambda\), the [monomial](monomials.md)

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i)
$$

satisfies

$$
\mu_{\mathbf p}(\chi_A)
=
\prod_{i\in A}p_i.
$$

More generally, if \(g_i:\{0,1\}\to\mathbb R\) for \(i\in A\), then independence gives

$$
\int_\Omega
\prod_{i\in A}g_i(\eta(i))\,
\mu_{\mathbf p}(d\eta)
=
\prod_{i\in A}
\left((1-p_i)g_i(0)+p_i g_i(1)\right).
$$

The factor on the right is the value at \(p_i\) of the unique affine extension of \(g_i\) from \(\{0,1\}\) to \([0,1]\).

## Coordinatewise order

For profiles \(\mathbf p,\mathbf q\in[0,1]^\Lambda\), write \(\mathbf p\le\mathbf q\) when \(p_i\le q_i\) for every \(i\). In that case,

$$
\mu_{\mathbf p}\le_{\mathrm{st}}\mu_{\mathbf q}.
$$

Indeed, if \((U_i)_{i\in\Lambda}\) are independent uniform random variables, then

$$
\eta_{\mathbf p}(i)=\mathbf 1_{\{U_i\le p_i\}},
\qquad
\eta_{\mathbf q}(i)=\mathbf 1_{\{U_i\le q_i\}}
$$

gives a coupling with \(\eta_{\mathbf p}\le\eta_{\mathbf q}\) coordinatewise.

## KCSM convention

For [kinetically constrained spin models](kinetically-constrained-spin-model.md), \(q\) denotes the density of zeros and \(p=1-q\) the density of ones. The homogeneous measure denoted by \(\mu_q\) in the KCSM entries is therefore the Bernoulli product measure with one-density \(p=1-q\).
