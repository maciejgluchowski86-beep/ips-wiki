---
title: FA-1f out of equilibrium
status: standard fact
tags:
  - FA-1f
  - out of equilibrium
  - convergence
---

# FA-1f out of equilibrium

This entry records proven convergence-to-equilibrium theorems for the [FA-1f model](fa-1f-model.md) started away from the invariant Bernoulli product measure \(\mu_q\).

**References.** Blondel, Cancrini, Martinelli, Roberto, and Toninelli, *Fredrickson-Andersen one spin facilitated model out of equilibrium*, Theorem 2.1 and Remarks 2.3--2.4.

## Setup

Let \(\Lambda\) be an infinite connected graph or lattice with finite neighbour sets \(N(i)\). Let \(d(\cdot,\cdot)\) be the graph distance and let

$$
B(i,r)=\{j\in\Lambda:d(i,j)\le r\}.
$$

The graph has \((k,D)\)-polynomial growth if

$$
\sup_{i\in\Lambda}|B(i,r)|\le k r^D
\qquad\text{for all }r\ge1.
$$

The FA-1f process has vacancy density \(q\), occupied density \(p=1-q\), invariant measure \(\mu_q\), and constraint

$$
c_i(\eta)=1-\chi_{N(i)}(\eta).
$$

For \(i\in\Lambda\), define the distance to the nearest vacancy by

$$
\xi^i(\eta)=\inf\{d(i,j):\eta(j)=0\},
$$

with the convention \(\xi^i(\eta)=\infty\) if there is no vacancy.

## Polynomial-growth theorem

**Theorem.** Assume \(q>1/2\) and assume \(\Lambda\) has \((k,D)\)-polynomial growth. Let \(f\) be local with \(\mu_q(f)=0\). Let \(\nu\) be an initial law such that, for some \(\theta_0>1\),

$$
\kappa:=\sup_{i\in\Lambda}\E_\nu\left[\theta_0^{\xi^i(\eta)}\right]<\infty.
$$

Then there is a constant

$$
c=c(q,k,D,\kappa,|\supp(f)|)<\infty
$$

such that, for every \(t\ge2\),

$$
\left|\E_\nu[f(\eta_t)]\right|
\le
c\|f\|_\infty
\begin{cases}
\exp(-t/c), & D=1,\\
\exp\left(-\left(t/(c\log t)\right)^{1/D}\right), & D>1.
\end{cases}
$$

For a general local function \(f\), apply the theorem to \(f-\mu_q(f)\).

## Product initial laws

If \(\nu=\mu_{q_0}\) is a Bernoulli product initial law with vacancy density \(q_0>0\), then the hypothesis on \(\xi^i\) holds for a suitable \(\theta_0>1\). Therefore the theorem applies to every non-degenerate product initial law \(\mu_{q_0}\) with \(q_0>0\).

The original paper writes this as a Bernoulli product law of occupied density \(p'=1-q_0<1\).
