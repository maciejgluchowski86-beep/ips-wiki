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

This entry records a geometric reformulation of the remaining Bernoulli-quench problem. It is complementary to the [chronology-averaged sign route](chronology-averaged-sign-route-for-fa-1f.md). No new convergence theorem is claimed.

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
\tag{1}
$$

Indeed, under \(\lambda\mu_q+(1-\lambda)\delta_{\mathbf 1}\), the probability that \([-L,L]\) is completely occupied tends to \(1-\lambda\) as \(L\to\infty\). Thus (1) rules out any trap component.

This target does not ask for a sign at any finite time. It asks only that activity cannot coarsen into vacancy-free regions whose typical size diverges.

## What front propagation already gives

The classical front law of large numbers of Blondel, Deshayes and Toninelli and the cutoff/front results of Ertul require the equilibrium vacancy density to be above a threshold. In that regime the proofs also establish a stronger ``zeros lemma'', controlling the production of vacancies behind the moving front.

More recently, Martinelli, Shapira and Toninelli proved that for every \(q>0\), starting from finitely many vacancies, the leftmost and rightmost vacancies have linearly growing span. This all-density result removes the need to prove vacancy mobility from scratch. See [front growth and vacancy density for FA-1f](front-growth-and-vacancy-density-for-fa-1f.md).

The span theorem does not imply (1): two extreme vacancies can be separated by order \(t\) while the interval between them is almost completely occupied. Indeed, the same paper still formulates convergence to equilibrium from a single vacancy as an open conjecture. The missing geometric input is therefore not propagation of the front but **densification behind it**, or equivalently an all-density analogue of the high-density zeros lemma.

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

This explains the recurring high-\(q\) obstruction in one-step Lyapunov estimates: they charge the creation of a zero gap immediately but stop before the same zero gap has been resolved. The natural embedded chain should instead be observed after complete local branch/coalescence excursions.

## Exact chronology-averaged local resampling

The [moving-edge CBSEP resampling](moving-edge-cbsep-resampling-for-fa-1f.md) implements precisely such an excursion. Starting from a nonempty edge, a stopped sequence of actual FA updates produces the CBSEP heat-bath distribution on that edge. In the moving version, an exterior vacancy that would delete the tagged vacancy causes the tag to move to that exterior vacancy, and the desired local branch still occurs after an exponential time of rate \(q\). The displacement before branching has an exponential tail.

This supplies a local mechanism for the missing all-density zeros lemma: a vacancy is not merely propagated; complete local chronologies repeatedly create branch/coalescence opportunities whose output has already averaged the competing update orders.

The remaining problem is global. These local regenerations must be concatenated into a spacetime construction which leaves enough regenerated vacancies behind the fronts while preserving the unused Poisson randomness. An adaptive choice of the next edge can reveal information about neighboring clocks, so a valid construction should be formulated using stopping lines or predetermined spacetime blocks.

## Relation with the 2013 convergence proof

Blondel, Cancrini, Martinelli, Roberto and Toninelli reduce their high-density convergence theorem to control of the nearest-vacancy distance. Their Theorem 2.1 assumes \(q>1/2\), and Remark 2.2 explicitly states that extending the result to \(q\le1/2\) requires more precise control of that distance.

Their finite-volume part does not intrinsically require the one-step Lyapunov argument used to obtain this control. Thus an all-density replacement for the persistence-of-zeros estimate can be inserted into the same general architecture: finite speed reduces a local observable to a large finite interval, vacancy-gap control keeps the process in the favorable nonempty components of mesoscopic blocks, and the finite-volume spectral-gap estimates give relaxation inside those components.

For qualitative convergence from Bernoulli data, the stationary-limit classification makes the target even weaker: (1) alone excludes the absorbing component. A quantitative zeros lemma would additionally recover an all-density version of the 2013 relaxation argument.

## Current target

The established and missing parts can therefore be separated as follows.

1. **Established all-density mobility.** Finite vacancy sets develop linearly growing span.
2. **Established local chronology averaging.** A complete FA edge excursion gives an exact CBSEP resampling, with exponentially localized moving-edge corrections.
3. **Missing all-density densification.** Prove that these local excursions can be concatenated so that vacancy-free gaps do not diverge behind the moving extremes.

The third statement is the genuinely new step. It should be proved directly at the level of complete update chronologies rather than by coefficientwise sign estimates or deterministic update words.
