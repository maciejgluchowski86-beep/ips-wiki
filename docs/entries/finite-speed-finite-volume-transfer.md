---
title: Finite-speed transfer from finite-volume relaxation
status: literature
audit: current
tags:
  - finite volume
  - finite propagation
  - KCLG
---

# Finite-speed transfer from finite-volume relaxation

## Criterion

Let \(P_t\) be an infinite-volume finite-range IPS semigroup and \(P_t^{\Lambda}\) a finite-volume version with boundary dynamics chosen so that useful relaxation estimates are available. For a local observable \(f\), choose a box \(\Lambda_t\) whose boundary is much farther from \(\operatorname{supp} f\) than information can typically travel by time \(t\). A graphical finite-speed estimate controls
\[
\|P_t f-P_t^{\Lambda_t}f\|_\infty,
\]
while a finite-volume inequality controls the relaxation of \(P_t^{\Lambda_t}f\). If both terms vanish for a box scale growing with \(t\), the finite-volume result transfers to the infinite system.

Cancrini--Martinelli--Roberto--Toninelli use this architecture explicitly for the two-dimensional Kob--Andersen kinetically constrained lattice gas. In Section 8, for a centered local \(f\), they choose a cube of side proportional to \(t\) and write
\[
\operatorname{Var}_{\mu}(P_t f)
\le 2\|P_t f-P_t^{Q_{\widetilde L}}f\|_\infty^2
 +2\operatorname{Var}_{\mu_{Q_{\widetilde L}}}(P_t^{Q_{\widetilde L}}f).
\]
Their finite-speed estimate makes the first term exponentially small, while Lemma 8.1 and the finite-volume coercive estimates control the second. Theorem 4.2 gives
\[
\operatorname{Var}_{\mu}(P_t f)
\le C(q)\frac{(\log t)^5}{t}\|f\|_\infty^2.
\]

## Mechanism

The graphical construction localizes causal influence. Couple the infinite process and the process restricted to a large box using the same clocks and marks inside the box. They agree on the support of \(f\) up to time \(t\) unless an influence path travels from the boundary to that support. Finite-range clocks make such abnormally fast paths unlikely when the boundary is at distance proportional to \(t\).

The reusable interface is therefore a restriction error \(\varepsilon(t,L)\), a finite-volume relaxation estimate \(R(t,L)\), and a choice \(L=L(t)\) for which both vanish. The thermodynamic limit is never taken independently of the dynamical time scale.

## Representative IPS use

For the cooperative Kob--Andersen lattice gas, finite-box coercivity with suitable reservoirs is transferred in Section 8 to the infinite-volume process exactly through this decomposition, giving quantitative equilibrium variance/autocorrelation decay for every local bounded observable.

This differs from [finite-volume coercivity plus semigroup exhaustion](finite-volume-coercivity-exhaustion-uniqueness.md): both couple volume to time, but here the restriction error comes from a common graphical finite-speed coupling and the conclusion is quantitative local-observable relaxation, whereas the Zitt method uses continuous-spin semigroup locality plus Gibbs compactness to prove uniqueness.

## Limitations

Finite speed requires local interactions or another quantitative control of influence propagation. The finite-volume dynamics must approximate the infinite process near the observable while admitting estimates strong enough at the growing scale. Boundary reservoirs or boundary conditions can make this compatibility nontrivial. The cited conclusion is equilibrium variance/autocorrelation decay for local observables, not total-variation mixing of an infinite state space or convergence from arbitrary nonequilibrium initial laws.

## Sources

- Cancrini, Martinelli, Roberto and Toninelli, *Kinetically Constrained Lattice Gases*, Theorem 4.2 and Section 8, especially equations (8.1)--(8.2) and Lemma 8.1, https://doi.org/10.1007/s00220-010-1038-3.
