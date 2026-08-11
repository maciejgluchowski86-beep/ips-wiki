---
title: Front growth and vacancy density for one-dimensional FA-1f
status: standard fact
tags:
  - FA-1f
  - out of equilibrium
  - front
  - vacancies
  - convergence
---

# Front growth and vacancy density for one-dimensional FA-1f

This entry records what is known about propagation of vacancies in one-dimensional [FA-1f](fa-1f-model.md), and distinguishes motion of an extreme vacancy from control of vacancy gaps behind it. This distinction is relevant to [out-of-equilibrium convergence](fa-1f-out-of-equilibrium.md).

Throughout, \(q\in(0,1)\) is the equilibrium vacancy density.

## High-density front results

Blondel, Deshayes and Toninelli, *Front evolution of the Fredrickson--Andersen one spin facilitated model* (Electronic Journal of Probability 24, 2019; arXiv:1803.08761), consider configurations that are completely occupied on one half-line and define the front as the leftmost vacancy. For \(q\) above a threshold ̅\(q<1\), they prove a law of large numbers and a central limit theorem for the front, together with convergence of the environment seen from the front to an invariant law.

Ertul, *Cutoff for the Fredrickson--Andersen one spin facilitated model* (ALEA 19, 2022; arXiv:2103.00019), strengthens the high-density front analysis and uses it to obtain finite-volume cutoff. A further ingredient in that proof is a ``zeros lemma'': behind a propagating front one obtains, with high probability, vacancies on a sufficiently dense collection of mesoscopic intervals. The proof uses a coupling with a supercritical threshold contact process and therefore again requires \(q\) above a threshold.

Thus the classical front theorems contain two logically different ingredients:

1. displacement of an extreme vacancy on a linear spatial scale;
2. production of sufficiently many vacancies behind that extreme.

The second property is what is needed for uniform control of vacancy gaps.

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

Their Theorem 6.2 states that, for every \(q>0\), there exist positive constants \(b,c\) such that for every initial configuration with finitely many vacancies, almost surely for all sufficiently large \(t\),

$$
b^{-1}t\le Y(t)\le ct,
\qquad
c^{-1}t\le D(t)\le ct.
\tag{1}
$$

The proof contains exponential hitting-time estimates for the extremal process. In particular, their Lemma 6.4 bounds the time needed for \(Y(t)\) to reach distance \(n\) between two linear multiples of \(n\), up to exponentially small error.

Equation (1) establishes linear mobility for every \(q>0\). It does not control the number or spacing of vacancies inside \([X^-(t),X^+(t)]\).

## Why linear front growth does not imply vacancy-gap tightness

A bound such as

$$
D(t)\ge ct
$$

only constrains the two extremal vacancies. It is compatible with configurations having vacancies only near \(X^-(t)\) and \(X^+(t)\) and an occupied interval of order \(t\) between them. Therefore it does not imply a bound of the form

$$
\lim_{L\to\infty}\limsup_{t\to\infty}
\mathbb P_\nu
\bigl(\eta_x(t)=1\text{ for all }x\in[-L,L]\bigr)=0.
\tag{2}
$$

This is not merely a logical possibility. The same 2025 paper formulates convergence to equilibrium for every \(q>0\), even from a single initial vacancy, as an open conjecture. Hence their all-density finite-seed span theorem cannot by itself yield (2).

The lack of attractiveness is also relevant. Starting a process from a Bernoulli vacancy field and deleting all but one vacancy does not give an ordered comparison between the two FA-1f evolutions.

## Consequence for the Bernoulli-quench problem

For one-dimensional FA-1f, every stationary measure is of the form

$$
\lambda\mu_q+(1-\lambda)\delta_{\mathbf 1}.
$$

Consequently, for Bernoulli initial data with positive vacancy density, the geometric statement (2) is enough to exclude the absorbing component from every subsequential stationary limit.

The literature therefore removes one part of this task: **all-density linear vacancy mobility is already known.** What remains is an all-density analogue of the high-density zeros lemma, namely a statement that propagation also leaves vacancies with tight gaps behind the moving extremes.

A possible route to that missing statement is the [moving-edge CBSEP resampling](moving-edge-cbsep-resampling-for-fa-1f.md). It gives an exact local resampling only after averaging a complete FA branch/coalescence chronology. Such a construction could replace the high-density contact-process comparison by an all-density coarse process, provided the local regenerations can be concatenated without conditioning away the unused graphical randomness.
