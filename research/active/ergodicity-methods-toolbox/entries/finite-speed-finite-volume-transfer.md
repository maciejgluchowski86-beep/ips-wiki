---
method_id: finite-speed-finite-volume-transfer
title: Finite-speed transfer from finite-volume relaxation
category: finite-to-infinite
targets:
  - convergence
model_scope: Finite-range interacting particle systems where a local infinite-volume semigroup can be coupled to a growing finite-volume restriction
source_status: primary-checked
primary_source: Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto and Cristina Toninelli, "Kinetically Constrained Lattice Gases," Communications in Mathematical Physics 297 (2010), 299--344
primary_pinpoint: Theorem 4.2; Section 8, equations (8.1)--(8.2) and Lemma 8.1
primary_url: https://doi.org/10.1007/s00220-010-1038-3
application_source: same as primary source
application_pinpoint: Theorem 4.2 and Section 8
application_url: https://doi.org/10.1007/s00220-010-1038-3
wiki_candidate: yes
---

# Finite-speed transfer from finite-volume relaxation

## Criterion

Let \(P_t\) be an infinite-volume finite-range IPS semigroup and \(P_t^{\Lambda}\) a finite-volume version with boundary dynamics chosen so that useful relaxation estimates are available. For a local observable \(f\), choose a box \(\Lambda_t\) whose boundary is much farther from \(\operatorname{supp} f\) than information can typically travel by time \(t\). A graphical finite-speed estimate controls
\[
\|P_t f-P_t^{\Lambda_t}f\|_\infty,
\]
while a finite-volume inequality controls the relaxation of \(P_t^{\Lambda_t}f\). If both terms vanish for a box scale growing with \(t\), the finite-volume result transfers to the infinite system.

Cancrini--Martinelli--Roberto--Toninelli use this architecture explicitly for the two-dimensional Kob--Andersen kinetically constrained lattice gas. In Section 8, for a centered local \(f\), they choose a cube \(Q_{\widetilde L}\) with \(\widetilde L=a t\) and write
\[
\operatorname{Var}_{\mu}(P_t f)
\le 2\|P_t f-P_t^{Q_{\widetilde L}}f\|_\infty^2
 +2\operatorname{Var}_{\mu_{Q_{\widetilde L}}}(P_t^{Q_{\widetilde L}}f).
\tag{8.1}
\]
Their finite-speed estimate (8.2) makes the first term exponentially small for a suitable \(a\). Lemma 8.1 and the finite-volume coercive estimates control the second term. The result is Theorem 4.2:
\[
\operatorname{Var}_{\mu}(P_t f)
\le C(q)\frac{(\log t)^5}{t}\|f\|_\infty^2
\]
for every local \(f\).

## Mechanism

The graphical construction localizes **causal influence**. Couple the infinite process and the process restricted to a large box using the same clocks and marks inside the box. They agree on the support of \(f\) up to time \(t\) unless an influence path travels from the boundary to that support during the time interval. Finite-range clocks make such abnormally fast paths unlikely when the boundary is at distance proportional to \(t\).

This turns an infinite-volume question into a finite-volume one without taking an uncontrolled thermodynamic limit. The box size is chosen as a function of the observation time, and the two errors are balanced directly. In the Kob--Andersen proof, the difficult finite-volume estimate comes from boundary-source dynamics and a renormalized comparison argument; finite speed then imports that estimate into the infinite lattice.

The reusable interface is therefore:

1. a graphical restriction coupling with an explicit error \(\varepsilon(t,L)\);
2. a finite-volume relaxation estimate \(R(t,L)\);
3. a choice \(L=L(t)\to\infty\) for which \(\varepsilon(t,L(t))+R(t,L(t))\to0\).

## Representative IPS use

For the cooperative Kob--Andersen lattice gas, Theorem 4.1 proves diffusive finite-box relaxation up to logarithmic corrections for boxes with suitable particle reservoirs. Section 8 then passes from those finite boxes to the infinite-volume process exactly through the decomposition above. Theorem 4.2 gives diffusive-order decay, again with logarithmic corrections, of the infinite-volume time autocorrelation of every local bounded observable.

This is stronger as a method page than merely observing that an infinite graphical construction is a limit of finite ones: the source uses a quantitative common-clock restriction error in the actual relaxation proof.

## Limitations

Finite speed requires sufficiently local interactions or another quantitative control of influence propagation. The finite-volume dynamics must approximate the infinite process near the observable while still admitting estimates strong enough at the growing scale \(L(t)\). Boundary reservoirs or boundary conditions can make this compatibility nontrivial. The conclusion in the cited KCLG application is equilibrium variance/autocorrelation decay for local observables; it is not total-variation mixing of an infinite state space and does not by itself establish convergence from arbitrary nonequilibrium initial measures. Long-range systems require a different propagation estimate.

## Sources

Primary checked source: Cancrini, Martinelli, Roberto and Toninelli, *Kinetically Constrained Lattice Gases*, Comm. Math. Phys. 297 (2010), 299--344. Theorem 4.2 is the infinite-volume relaxation result; Section 8, especially equations (8.1)--(8.2) and Lemma 8.1, displays the finite-speed reduction to a box of size proportional to time and the finite-volume term that completes the proof.