---
title: Vacancy-gap route for one-dimensional FA-1f
status: heuristic
tags:
  - FA-1f
  - out of equilibrium
  - gaps
  - coagulation-fragmentation
  - coarse graining
---

# Vacancy-gap route for one-dimensional FA-1f

This entry records a geometric reformulation of the remaining Bernoulli-quench problem. It is complementary to the [coarse chronology contraction route](coarse-chronology-contraction-route-for-fa-1f.md). No new convergence theorem is claimed.

## A weaker target than finite-time sign positivity

For the Bernoulli initial laws under consideration, the current stationary-limit classification reduces every subsequential stationary limit to

$$
\lambda\mu_q+(1-\lambda)\delta_{\mathbf 1}.
$$

Consequently, the finite-time sign target \(\rho_t\ge q\) is much stronger than necessary. A purely geometric sufficient statement is tightness of the distance to the nearest vacancy. For example, it would suffice to prove

$$
\lim_{L\to\infty}\limsup_{t\to\infty}
\mathbb P_{\mu_{q_0}}
\bigl(\eta_t(x)=1\text{ for every }x\in[-L,L]\bigr)=0.
$$

Indeed, under \(\lambda\mu_q+(1-\lambda)\delta_{\mathbf 1}\), the probability that \([-L,L]\) is completely occupied tends to \(1-\lambda\) as \(L\to\infty\). Thus the displayed tightness statement rules out any trap component.

This target does not ask for a sign at any finite time. It asks only that activity cannot coarsen into vacancy-free regions whose typical size diverges.

## Exact gap geometry

Write the vacancy sites in increasing order as \(\cdots<X_{-1}<X_0<X_1<\cdots\), and define the occupied gaps

$$
G_k=X_{k+1}-X_k-1\in\mathbb N_0.
$$

The FA-1f transitions have a simple interpretation in these variables.

* If \(G_k=n\ge1\), the occupied site immediately to the right of \(X_k\) can refresh to a vacancy at rate \(q\). This inserts a vacancy and replaces the gap \(n\) by \((0,n-1)\). The symmetric update at the other end gives \((n-1,0)\).
* A vacancy \(X_k\) may refresh to occupied at rate \(p\) only when at least one adjacent gap is zero. Removing \(X_k\) merges its neighboring gaps \(a,b\) into the single gap \(a+b+1\).

Thus the two-sided FA-1f dynamics is a local coagulation-fragmentation process on the ordered vacancy gaps: positive gaps fragment at their ends by vacancy creation, while zero gaps permit vacancy deletion and coagulation of neighboring gaps.

Under the Palm version of a Bernoulli vacancy field of density \(r\), the gaps are i.i.d. geometric,

$$
\mathbb P(G_k=n)=r(1-r)^n.
$$

The equilibrium value is \(r=q\). The unresolved Bernoulli quench therefore becomes a convergence/tightness problem for a coagulation-fragmentation dynamics started from an i.i.d. geometric gap field.

## Why one-ring drift estimates are misleading

An isolated vacancy corresponds locally to positive gaps on both sides. It cannot disappear. A neighboring occupied site first refreshes to a vacancy, creating a zero gap. Subsequent updates can then return to the separated-vacancy set with the vacancy displaced, can coalesce two vacancies, or can leave two separated vacancies. In particular, the effective motion only appears after an entire adjacent-vacancy excursion is averaged.

This explains the recurring high-\(q\) obstruction in one-step Lyapunov estimates: they charge the creation of a zero gap immediately but stop before the same zero gap has been resolved. The natural embedded chain should instead be observed at return times to a coarse class such as configurations with no adjacent vacancies in the region under consideration.

## Relation with CBSEP

The effective excursion moves are the same geometric moves that make the coalescing and branching simple symmetric exclusion process useful: branching and coalescing are literal FA-1f moves, while a nearest-neighbor vacancy displacement is realized in FA-1f by a branching step followed by coalescence. This suggests using CBSEP as an auxiliary coarse process, but only after chronology has been averaged over the full local excursion.

A useful finite target would be a minorization or contraction statement for the FA return kernel on a mesoscopic interval. Starting from a separated-vacancy state, let \(\tau\) be the first return after a nontrivial local excursion to the separated-vacancy class. One would like to identify a coarse kernel \(K\) such that either

$$
P_{\mathrm{FA}}(\eta_\tau\in\cdot\mid\eta_0)
\ge \varepsilon K(\eta_0,\cdot)
$$

on suitable block states, or the corresponding transfer operator contracts the non-equilibrium component in a norm adapted to gap tails. A CBSEP-type \(K\) would be particularly useful because its mobile-vacancy geometry is much better behaved than the microscopic FA chronology.

## Proposed proof architecture

The global problem should be split into two genuinely geometric statements.

1. **Gap tightness.** Show that, starting from an i.i.d. geometric gap field with any parameter \(q_0>0\), the occupied gap containing a fixed site is tight uniformly for large times. A block construction based on the excursion kernel is the natural target.
2. **Regional mixing.** Once a mesoscopic region is crossed by a mobile vacancy and experiences enough rings, show that its dependence on the incoming state contracts. This is the role of the coarse chronology/projection argument.

The first statement excludes the absorbing component. The second should be useful for quantitative convergence, but the qualitative Bernoulli convergence problem may already follow from the first together with the stationary-limit classification.

## Immediate finite computations

The next simulations should be done in gap variables rather than in the signed dual alone. On intervals containing one or two isolated vacancies:

* enumerate the return kernel to the no-adjacent-vacancy class;
* record probabilities of displacement, coalescence and genuine branching after the excursion;
* test whether the return kernel is monotone or contractive in any natural gap order;
* compare it numerically with a CBSEP edge kernel after optimizing a time rescaling;
* test whether repeated return-kernel steps preserve a uniform exponential tail of gap lengths.

These tests directly probe the mechanism required to rule out escape to the all-occupied state. Failure of coefficientwise sign positivity would not invalidate this route.
