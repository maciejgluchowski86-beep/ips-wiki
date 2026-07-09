---
title: East out of equilibrium
status: standard fact
tags:
  - East model
  - out of equilibrium
  - oriented KCSM
---

# East out of equilibrium

This entry records convergence-to-equilibrium theorems for the [East model](east-model.md) started away from \(\mu_q\).

**References.** Cancrini, Martinelli, Schonmann, and Toninelli, *Facilitated oriented spin models: some non equilibrium results*, Theorems 3.1--3.2; Marêché, *Exponential convergence to equilibrium for the \(d\)-dimensional East model*, Theorem 2.2; Hartarsky and Toninelli, *Kinetically constrained models*, Theorem 7.6.

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

## One-dimensional product initial laws

**Theorem.** Let \(\nu=\mu_{q_0}\) be a Bernoulli product initial law with \(q_0\in(0,1)\). Then there exists \(m>0\), and for each local function \(f\) there exists \(C_f<\infty\), such that for all \(t>0\),

$$
\int\left|P_t f(\eta)-\mu_q(f)\right|\,\nu(d\eta)
\le
C_f\exp(-mt).
$$

Moreover, for \(\nu\)-almost every \(\eta\), there exists \(t_0=t_0(\eta,f)\) such that for all \(t>t_0\),

$$
\left|P_t f(\eta)-\mu_q(f)\right|
\le
C_f\exp(-mt).
$$

This is Cancrini--Martinelli--Schonmann--Toninelli, Theorem 3.2, rewritten with \(q_0\) as the initial vacancy density.

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

## Higher-dimensional product initial laws

For \(r\ge0\), set

$$
Q_+(r)=\{0,\ldots,\lfloor r\rfloor\}^d,
\qquad
Q_-(r)=-Q_+(r)\setminus\{0\}.
$$

Assume that \(\nu\) satisfies condition \((C_+)\): there are constants \(a,A>0\) such that, for every \(\ell\ge0\),

$$
\nu\left(\eta(y)=1\text{ for every }y\in Q_+(\ell)\right)
\le
A\exp(-a\ell).
$$

**Theorem.** If \(\nu\) satisfies \((C_+)\), then there exist constants \(\chi=\chi(q)>0\), \(c_1=c_1(q,\nu)>0\), and \(C_1=C_1(q,\nu)<\infty\) such that, for all \(t\ge0\) and all local functions \(f\) with

$$
\supp(f)\subseteq Q_-(\chi t^{1/d}),
$$

one has

$$
\int\left|P_t f(\eta)-\mu_q(f)\right|\,\nu(d\eta)
\le
C_1\|f\|_\infty\exp(-c_1t).
$$

This is Marêché, Theorem 2.2. Bernoulli product laws \(\mu_{q_0}\) with \(q_0>0\) satisfy \((C_+)\).
