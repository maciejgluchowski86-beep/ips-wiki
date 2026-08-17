---
title: KCSM constraint domination by a simpler reference process
status: literature
audit: current
tags:
  - KCSM
  - spectral gap
  - comparison
---

# KCSM constraint domination by a simpler reference process

## Criterion

For heat-bath kinetically constrained spin models with common reversible product law \(\mu\), the constraints enter the Dirichlet form multiplicatively:
\[
\mathcal D(f)=\sum_x \mu\!\left(c_x\,\operatorname{Var}_x(f)\right).
\]
If a second process has constraints \(c'_x(\eta)\le c_x(\eta)\) for every site and configuration, then
\[
\mathcal D'(f)\le \mathcal D(f),
\qquad
\operatorname{gap}(L')\le \operatorname{gap}(L).
\]
Thus a more constrained but simpler reference chain can provide a spectral-gap lower bound for the original model. Cancrini--Martinelli--Roberto--Toninelli call this domination.

Their Theorem 6.1 makes the comparison concrete. Let \(G\) be a finite connected graph, choose a root \(r\) whose update is unconstrained, and run FA-1f elsewhere. Choose a rooted spanning tree \(T\). Requiring specifically that the parent of each vertex be vacant is more restrictive than requiring some neighbour to be vacant, so the FA-1f Dirichlet form dominates that of an oriented East-type process on \(T\). A recursive tree decomposition then gives
\[
\operatorname{gap}(G,r,\mathrm{FA\!-\!1f})
\ge \operatorname{gap}(\mathbb Z,\mathrm{East}).
\]

## Mechanism

The first step is pointwise: delete legal moves until the remaining constraint has a simple oriented structure. Because deleting legal moves only decreases the Dirichlet form, any lower bound on the slower reference chain is automatically a lower bound on the original chain.

The second step exploits the reference geometry. For the oriented process on a rooted tree, split the tree into subtrees \(A\) and \(B\) at a branching point. Lemma 6.2 proves
\[
\operatorname{gap}(T,r,\mathrm{East})
\ge
\min\{\operatorname{gap}(A,r,\mathrm{East}),
      \operatorname{gap}(B,r,\mathrm{East})\}.
\]
Repeating the split reduces the tree to one-dimensional paths, whose gaps are controlled by the standard East gap. The difficult graph geometry has been replaced by a deliberately slower reference process whose relaxation is already understood.

## Representative IPS use

Theorem 6.1 gives the finite-graph FA-1f estimate above. Theorem 6.3 combines it with finite-subgraph approximation to show that on any infinite connected bounded-degree graph,
\[
\operatorname{gap}(G_\infty,\mathrm{FA\!-\!1f})
\ge \operatorname{gap}(\mathbb Z,\mathrm{East})>0.
\]
Hence equilibrium \(L^2\) relaxation of FA-1f follows uniformly from the simpler one-dimensional oriented reference model.

## Limitations

Domination is one-sided. Making a process less constrained improves the gap, so an unconstrained faster heat-bath chain cannot by itself lower-bound the constrained gap; the useful reference must be slower while remaining tractable. The comparison also assumes compatible reversible measures and update variances.

This is distinct from [canonical-path comparison](dirichlet-form-canonical-path-comparison.md): no congestion routing is needed because the generator ordering is pointwise. It is also distinct from [East distinguished-zero screening](east-distinguished-zero-screening.md) and the [Kob--Andersen renormalized comparison](kclg-renormalized-glauber-comparison.md).

## Sources

- Cancrini, Martinelli, Roberto, Toninelli, *Facilitated Spin Models: Recent and New Results*, Definition 3, Remark 7, Theorem 6.1, Lemma 6.2, and Theorem 6.3, https://arxiv.org/abs/0712.1934.
- Published chapter: https://doi.org/10.1007/978-3-540-92796-9_8.
