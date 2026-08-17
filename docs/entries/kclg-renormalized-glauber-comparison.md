---
title: Renormalization and long-range Glauber comparison for KCLG
status: literature
audit: current
tags:
  - KCLG
  - Kob-Andersen
  - spectral gap
---

# Renormalization and long-range Glauber comparison for KCLG

## Criterion

For cooperative kinetically constrained lattice gases, direct comparison with unconstrained Kawasaki dynamics can be useless because a legal microscopic path may require a rare coordinated pattern of vacancies. Cancrini--Martinelli--Roberto--Toninelli instead build a **renormalized constrained dynamics** whose effective good states are abundant, prove coercivity for an auxiliary long-range Glauber model, and compare back to the original conservative process.

In their auxiliary AGL model, a site refresh is allowed when a path of sufficiently many renormalized good blocks connects it to the appropriate boundary. Theorem 5.5 states that there are \(\rho_1<1\) and \(A<\infty\) such that, if the single-block good-event probability \(\rho>\rho_1\), then on any rectangle

$$
\operatorname{gap}(L^{\mathrm{agl}}_{\Lambda,N})\ge \frac12
$$

provided the allowed path length satisfies

$$
N\ge A\bigl(\log \max(L_1,L_2)\bigr)^2.
$$

Theorem 5.6 then transfers this to an auxiliary Kawasaki-plus-Glauber process with

$$
\operatorname{gap}(L^{\mathrm{akg}}_{Q_L})^{-1}
\le C L^2(\log L)^4.
$$

Path comparison from the renormalized dynamics to legal Kob--Andersen exchanges gives the same upper order for the KA relaxation time, up to logarithms.

## Mechanism

The key move is to change the state description before comparing Dirichlet forms. Partition the lattice into mesoscopic blocks and declare a block ``good'' when its internal vacancy structure permits the rearrangements needed by the kinetic constraint. At a suitable scale these effective good blocks have high probability even when individual vacancies are sparse.

On this renormalized field, define a long-range constrained Glauber chain (AGL). Its nonconservative refreshes are analytically easier: a block can be resampled once a good path to the boundary exists. A multiscale/bisection argument proves an order-one Poincare inequality for AGL despite the long-range constraint. Next define AKG, which combines conservative exchanges with Glauber sources, and use explicit legal paths to replace each allowed AGL refresh by a sequence of AKG moves. A second path comparison replaces those renormalized moves by legal exchanges of the original KA process.

Thus the auxiliary nonconservative model is not claimed to approximate the physical dynamics trajectory-wise. It is a coercive intermediary whose variance estimate can be transported through carefully constructed legal paths.

## Representative IPS use

For the two-dimensional Kob--Andersen model in a square of side \(L\) with particle reservoirs, Theorem 4.1 gives, for every positive vacancy density \(q\),

$$
C(q)^{-1}L^2
\le
\operatorname{gap}(L^{\mathrm{KA}}_{Q_L}(q))^{-1}
\le
C(q)L^2(\log L)^4.
$$

Hence cooperative kinetic constraints do not change the diffusive power of the finite-volume relaxation scale, though the proof loses logarithms. Theorem 4.2 combines the finite-volume coercivity with finite propagation and spectral arguments to prove, for local \(f\),

$$
\operatorname{Var}_{\mu}(P_t f)
\le
C(q)\frac{(\log t)^5}{t}\,\|f\|_\infty^2.
$$

This gives quantitative equilibrium relaxation in a model where microscopic legal-path probabilities are themselves too small for a naive comparison.

## Limitations

The proof is highly model-specific. One must identify mesoscopic good events with high probability and explicitly realize auxiliary refreshes by legal conservative paths. The renormalization scale and path congestion can become very large at high density, and the constants depend strongly on \(q\).

The method is not merely the generic [canonical-path comparison](dirichlet-form-canonical-path-comparison.md) already represented elsewhere in the toolbox: the decisive step is first to **manufacture an auxiliary high-density good-block process** for which a useful Poincare inequality exists. Without that renormalized state space, direct paths in the original vacancy field are exponentially unlikely.

The AGL gap theorem itself uses a constrained [bisection argument](block-dynamics-bisection-variance.md), so there is overlap with block dynamics, but here bisection is only one component of a larger KCLG-specific bridge from nonconservative long-range refreshes back to cooperative conservative motion.

This entry does not provide a generic nonreversible sector or hypocoercive theorem. In the literature search that produced it, located sector-condition IPS sources were primarily fluctuation/CLT or hydrodynamic tools rather than direct relaxation criteria.

## Sources

- Cancrini, Martinelli, Roberto, Toninelli, *Kinetically Constrained Lattice Gases*, Theorems 4.1, 4.2, 5.5 and 5.6 and Sections 5--8, https://doi.org/10.1007/s00220-010-1038-3.
