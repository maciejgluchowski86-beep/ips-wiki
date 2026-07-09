---
title: East out of equilibrium
status: standard fact
tags:
  - East model
  - out of equilibrium
  - oriented KCSM
---

# East out of equilibrium

This entry records convergence-to-equilibrium theorems for the [East model](east-model.md) started from non-stationary initial configurations.

**References.** Cancrini, Martinelli, Schonmann, and Toninelli, *Facilitated oriented spin models: some non equilibrium results*, Theorem 3.1; Hartarsky and Toninelli, *Kinetically constrained models*, Theorem 7.6.

## One-dimensional theorem

Take \(\Lambda=\Z\), \(N(i)=\{i+1\}\), and

$$
c_i(\eta)=1-\eta(i+1).
$$

Let \((P_t)_{t\ge0}\) be the East semigroup and let \(\mu_q\) be the Bernoulli product measure with vacancy density \(q\).

**Theorem.** Let \(\eta\in\{0,1\}^{\Z}\). Assume that \(\eta\) has infinitely many vacancies to the right of \(\supp(f)\). Then there exists \(m>0\), and for each local function \(f\) there exist \(C_f<\infty\) and \(t_0=t_0(\eta,f)\) such that, for all \(t>t_0\),

$$
\left|P_t f(\eta)-\mu_q(f)\right|
\le
C_f\exp(-mt).
$$

This is Cancrini--Martinelli--Schonmann--Toninelli, Theorem 3.1, translated to the convention \(N(i)=\{i+1\}\).

## Higher-dimensional theorem

For the \(d\)-dimensional East model on \(\Z^d\), take

$$
N(i)=\{i+e_1,\ldots,i+e_d\}.
$$

For \(x\in\Z^d\), write

$$
x+\N^d=\{x+y:y\in\N^d\},
\qquad
\Delta_x^d=x-(\N^d\setminus\{0\}).
$$

**Theorem.** Fix \(x\in\Z^d\) and an initial configuration \(\eta\) such that \(\eta\) is not identically equal to \(1\) on \(x+\N^d\). Then there exists \(m=m(\eta,q)>0\), and for every local function \(f\) with

$$
\supp(f)\subseteq \Delta_x^d,
$$

there exists \(C=C(f,\eta,q)<\infty\) such that, for all sufficiently large \(t\),

$$
\left|P_t f(\eta)-\mu_q(f)\right|
\le
C\exp(-mt).
$$

This is Hartarsky--Toninelli, *Kinetically constrained models*, Theorem 7.6, recording the result proved in dimension one by Cancrini--Martinelli--Schonmann--Toninelli and in all dimensions by Marêché.
