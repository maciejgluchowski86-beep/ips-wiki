---
title: Front growth and vacancy density for one-dimensional FA-1f
status: literature
audit: current
tags:
  - FA-1f
  - East
  - out of equilibrium
  - front
  - vacancies
  - convergence
---

# Front growth and vacancy density for one-dimensional FA-1f

This entry records what is known about propagation and the law behind a moving front in one-dimensional [FA-1f](fa-1f-model.md), with the [East model](east-model.md) as the main benchmark. The distinction between motion of an extreme vacancy and relaxation of the environment behind it is relevant to [out-of-equilibrium convergence](fa-1f-out-of-equilibrium.md).

Throughout, \(q\in(0,1)\) is the equilibrium vacancy density and \(\mu_q\) is the Bernoulli product equilibrium law.

## East: equilibrium far behind the front

For the one-dimensional East model, the law behind the front is understood for every \(q>0\). Blondel, *Front progression for the East model* (Stochastic Processes and their Applications 123, 2013; arXiv:1212.4435), proves that the process seen from the front has a unique invariant law \(\widetilde\mu\), and that its tail approaches equilibrium exponentially in the distance from the front. In the notation of Hartarsky and Toninelli, *Kinetically constrained models*, Theorem 7.11, there are \(C,m>0\) such that

$$
\left\|\widetilde\mu-\mu_q\right\|_{[x,\infty)}
\le Ce^{-mx}.
\tag{1}
$$

Here total variation is taken between the marginals on the indicated half-line. Thus the invariant front law can differ from equilibrium close to the front, but the discrepancy is exponentially localized near it.

The finite-time statement behind (1) is stronger. Blondel's Theorem 4.7 shows that, after enough time, the configuration on a block a distance \(L\) behind the front is exponentially close in \(L\) to the equilibrium product law, under a spacing condition on suitable vacancies; the front dynamics itself generates that condition after an initial burn-in period.

The basic mechanism is the **distinguished zero** of Aldous--Diaconis and Cancrini--Martinelli--Schonmann--Toninelli. For East, the distinguished zero moves monotonically in the oriented direction. If the interval behind it initially has equilibrium law, then, conditional on the entire distinguished-zero path, that interval still has exactly equilibrium law at every later time. In the notation of Cancrini et al., *Facilitated oriented spin models: some non equilibrium results*, Lemma 3.5, if \(V_t\) is the interval swept out behind the distinguished zero \(\xi_t\), then

$$
\mathcal L\left(\eta_t|_{V_t}\mid (\xi_s)_{0\le s\le t}\right)
=\mu_q|_{V_t}.
\tag{2}
$$

Conditionally on the path, the region behind the zero is therefore an ordinary East process with a moving vacant boundary; whenever the boundary moves, one fresh Bernoulli equilibrium spin is appended. Spectral-gap contraction can then be iterated along the growing intervals. This is the core reason that the East front leaves an equilibrium wake.

The exact conditional identity (2) uses orientation essentially. Clock rings and coin tosses behind the distinguished zero cannot affect the future legality of the rings that move the distinguished zero.

## High-vacancy FA-1f: an analogous front law

Blondel, Deshayes and Toninelli, *Front evolution of the Fredrickson--Andersen one spin facilitated model* (Electronic Journal of Probability 24, 2019; arXiv:1803.08761), develop an analogue of this program for two-sided FA-1f when \(q\) is above a threshold \(\bar q<1\). They consider a configuration completely occupied on one half-line, with the boundary vacancy as the front. In this regime they prove a law of large numbers and central limit theorem for the front and convergence of the process seen from the front to an invariant law.

Their proof also contains an explicit relaxation-behind-the-front input. Far enough behind the front, local observables are close to equilibrium; this is then used to couple two processes seen from the front and obtain uniqueness of the invariant front law. Ertul's later cutoff proof uses a related ``zeros lemma'', guaranteeing vacancies on a dense collection of mesoscopic intervals behind the moving fronts.

The FA proof cannot use the distinguished-zero identity (2). The papers explicitly point out that the East construction relies on orientation and is unavailable for two-sided FA-1f. Instead, the high-vacancy FA argument has two separate ingredients:

1. a comparison with a supercritical threshold contact process, which produces sufficiently many vacancies behind the front;
2. a non-equilibrium relaxation theorem for FA-1f once the configuration has sufficiently good vacancy spacing.

The second ingredient ultimately uses the nearest-vacancy estimates of Blondel, Cancrini, Martinelli, Roberto and Toninelli, *Fredrickson--Andersen one spin facilitated model out of equilibrium*. Their elementary exponential-moment estimate for the nearest-vacancy distance requires \(q>1/2\). The contact-process comparison used for the front theorem imposes the stronger threshold \(q>\bar q\).

Thus the published FA front proof already separates the two problems that arise in the all-density question: **produce vacancies behind the front**, then **relax the resulting region toward equilibrium**.

## All-density growth from finitely many vacancies

Martinelli, Shapira and Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems* (arXiv:2510.20461, 2025), prove an all-density propagation result for initial configurations with finitely many vacancies.

Let

$$
X^+(t)=\sup\{x:\eta_x(t)=0\},
\qquad
X^-(t)=\inf\{x:\eta_x(t)=0\},
$$

and set

$$
Y(t)=\max\{|X^+(t)|,|X^-(t)|\},
\qquad
D(t)=X^+(t)-X^-(t).
$$

Their Theorem 6.2 states that, for every \(q>0\), there are positive constants \(b,c\) such that for every initial configuration with finitely many vacancies, almost surely for all sufficiently large \(t\),

$$
b^{-1}t\le Y(t)\le ct,
\qquad
c^{-1}t\le D(t)\le ct.
\tag{3}
$$

The proof contains exponential hitting-time estimates for the extremal process. Equation (3) establishes linear mobility for every \(q>0\), but does not control the number or spacing of vacancies inside \([X^-(t),X^+(t)]\).

## Why linear growth alone is insufficient

A bound such as

$$
D(t)\ge ct
$$

only constrains the two extremal vacancies. It is compatible with configurations having vacancies only near \(X^-(t)\) and \(X^+(t)\) and an occupied interval of order \(t\) between them. Therefore it does not imply

$$
\lim_{L\to\infty}\limsup_{t\to\infty}
\mathbb P_\nu
\bigl(\eta_x(t)=1\text{ for all }x\in[-L,L]\bigr)=0.
\tag{4}
$$

The same 2025 paper still formulates convergence to equilibrium for every \(q>0\), even from a single initial vacancy, as an open conjecture. Hence the all-density span theorem cannot itself contain the missing behind-front equilibrium statement.

The lack of attractiveness prevents obtaining it by deleting all but one vacancy from a denser initial configuration.

## Finite-volume relaxation is available at every fixed density

The high-density nearest-vacancy estimate is not the only possible way to obtain the relaxation part of the front argument. Modern one-dimensional general-KCM bisection gives finite-volume spectral-gap control on arbitrary irreducible components for every fixed facilitating density.

Hartarsky and Toninelli, Theorem 4.8, give for a one-dimensional finite-range general KCM

$$
T_{\mathrm{rel}}
\le
(2/q)^{C\log\min\{|\Lambda|,2/q\}}.
\tag{5}
$$

In particular, at fixed \(q>0\), the bound is uniform in \(|\Lambda|\) once the interval is large. The result applies after restricting to an irreducible component; the same chapter discusses FA-1f on a segment conditioned to contain a vacancy.
