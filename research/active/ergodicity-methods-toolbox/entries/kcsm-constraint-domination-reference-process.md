---
method_id: kcsm-constraint-domination-reference-process
title: KCSM constraint domination by a simpler reference process
category: kcsm-model-specific
targets:
  - spectral-gap
  - convergence
model_scope: FA-1f kinetically constrained spin dynamics on finite and infinite connected graphs, compared to oriented East reference dynamics
source_status: primary-checked
primary_source: Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto, Cristina Toninelli, Facilitated Spin Models: Recent and New Results, in Methods of Contemporary Mathematical Statistical Physics, Lecture Notes in Mathematics 1970 (2009), 307-340.
primary_pinpoint: Definition 3 and Remark 7 (constraint domination); Theorem 6.1 and Lemma 6.2 (FA-1f on a rooted graph compared with East); Theorem 6.3 (infinite bounded-degree graph consequence)
primary_url: https://arxiv.org/abs/0712.1934
application_source: Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto, Cristina Toninelli, Facilitated Spin Models: Recent and New Results.
application_pinpoint: Theorems 6.1 and 6.3
application_url: https://doi.org/10.1007/978-3-540-92796-9_8
wiki_candidate: yes
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
Thus a more constrained but simpler reference chain can provide a spectral-gap lower bound for the original model. Cancrini--Martinelli--Roberto--Toninelli call this **domination** in Definition 3 and Remark 7.

Their Theorem 6.1 makes the comparison concrete. Let \(G\) be a finite connected graph, choose a root \(r\) whose update is unconstrained, and run FA-1f elsewhere. Choose a rooted spanning tree \(T\). Requiring specifically that the parent of each vertex be vacant is more restrictive than requiring *some* neighbour to be vacant, so the FA-1f Dirichlet form dominates that of an oriented East-type process on \(T\). A recursive tree decomposition then gives
\[
\boxed{\operatorname{gap}(G,r,\mathrm{FA\!-\!1f})
\ge \operatorname{gap}(\mathbb Z,\mathrm{East}).}
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
The proof uses an invariant subspace for functions independent of one subtree and the Poincare inequality on its orthogonal complement. Repeating the split reduces the tree to one-dimensional paths, whose gaps are controlled by the standard East gap. The difficult graph geometry has therefore been replaced by a deliberately slower reference process whose relaxation is already understood.

## Representative IPS use

Theorem 6.1 gives the finite-graph FA-1f estimate above. Theorem 6.3 combines it with finite-subgraph approximation to show that on any infinite connected bounded-degree graph,
\[
\operatorname{gap}(G_\infty,\mathrm{FA\!-\!1f})
\ge \operatorname{gap}(\mathbb Z,\mathrm{East})>0.
\]
Hence equilibrium \(L^2\) relaxation of FA-1f follows uniformly from the simpler one-dimensional oriented reference model.

The paper also gives a related estimate on the nontrivial finite-volume ergodic component. The reusable idea is broader than the particular graph theorem: when legal moves of a KCSM contain the legal moves of a tractable constrained reference dynamics, Dirichlet-form monotonicity can import coercivity without analyzing the faster model directly.

## Limitations

Domination is one-sided. Making a process less constrained improves the gap, so an **unconstrained faster** heat-bath chain cannot by itself lower-bound the constrained gap; the useful reference must be slower while remaining tractable. A poor choice can therefore produce a uselessly tiny bound. The comparison also assumes compatible reversible measures and update variances.

This is distinct from generic canonical-path/Dirichlet-form comparison: no congestion routing is needed because the generator ordering is pointwise. It is also distinct from the live East distinguished-zero page, which uses a moving vacancy to screen non-equilibrium initial data, and from the Kob--Andersen renormalized-Glauber page, which builds mesoscopic auxiliary dynamics and path simulations. Here the entire proof interface is **constraint deletion plus spectral-gap monotonicity**.

## Sources

- Cancrini, Martinelli, Roberto, Toninelli, *Facilitated Spin Models: Recent and New Results*, Definition 3, Remark 7, Theorem 6.1, Lemma 6.2, and Theorem 6.3, https://arxiv.org/abs/0712.1934.
- Published chapter: https://doi.org/10.1007/978-3-540-92796-9_8.
