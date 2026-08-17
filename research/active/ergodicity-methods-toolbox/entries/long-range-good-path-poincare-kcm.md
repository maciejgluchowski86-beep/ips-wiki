---
method_id: long-range-good-path-poincare-kcm
title: Long-range good-path Poincare inequalities for KCM
category: kcsm-model-specific
targets:
  - spectral-gap
  - convergence
model_scope: Product-measure KCM after block renormalisation, with likely good states and rare super-good mobile droplets connected by oriented paths
source_status: primary-checked
primary_source: Fabio Martinelli and Cristina Toninelli, Towards a universality picture for the relaxation to equilibrium of kinetically constrained models, Annals of Probability 47 (2019), 324-361.
primary_pinpoint: Theorem 2 and Lemma 2.5; Definition 3.1, Theorem 3.2, Proposition 3.4 and Corollary 3.9
primary_url: https://doi.org/10.1214/18-AOP1262
application_source: Fabio Martinelli and Cristina Toninelli, Towards a universality picture for the relaxation to equilibrium of kinetically constrained models, Annals of Probability 47 (2019), 324-361.
application_pinpoint: Section 4 and Theorem 4.4, with the good/super-good construction and legal-path estimates in Section 5
application_url: https://arxiv.org/abs/1701.00107
wiki_candidate: yes
---

# Long-range good-path Poincare inequalities for KCM

## Criterion

Martinelli--Toninelli develop a constrained Poincare principle designed for situations where the useful facilitating event is **nonlocal but very likely**. Their Theorem 2 considers product variables with constraints supported in an exterior region. If the supports and failure probabilities satisfy the weighted smallness condition (2.1), then every local function obeys a Poincare inequality of the form
\[
\operatorname{Var}(f)
\le 4\sum_x\mu\!\left(c_x\operatorname{Var}_x(f)\right),
\]
with the appropriate product of the chosen constraints. The proof begins from the martingale/exterior decomposition of Lemma 2.5 rather than from geometric block bisection.

The KCM form appears in Section 3. A renormalised site is **good** with probability \(p_1\) close to one and **super-good** with small probability \(p_2\); the latter represents a mobile critical droplet. Definition 3.1 calls a path good if all its vertices are good, and super-good if it additionally contains a super-good site. Proposition 3.4 states that, when
\[
\max\{p_2,(1-p_1)\log^2(1/p_2)\}
\]
is sufficiently small, the event \(\Gamma_x\) that suitable super-good paths of length at most \(p_2^{-2}\) emanate from the oriented neighbours of x gives
\[
\operatorname{Var}(f)
\le 4\sum_x\mu\!\left(1_{\Gamma_x}\operatorname{Var}_x(f)\right).
\tag{GP}
\]
Theorem 3.2 and Corollary 3.9 then bound the right-hand side by local constrained Dirichlet forms plus the cost of moving the super-good state.

## Mechanism

A rare mobile droplet is too unlikely to be required immediately next to every site: that would give a useless constraint. The method instead asks only that the surrounding coarse environment be good and that a super-good droplet occur **somewhere along a long oriented path**. For suitable path length this composite event has probability near one even when an individual droplet is rare.

The proof has two stages. First, the exterior martingale decomposition turns the high-probability long-range event into the constrained Poincare inequality `(GP)`. Second, a map from good to super-good block states is iterated along the selected path, effectively transporting the droplet from its remote location to the neighbourhood of x. Cauchy--Schwarz and change-of-measure estimates quantify the transport cost. After renormalisation, microscopic legal paths implement those coarse moves and Corollary 3.9 compares the resulting terms with the original KCM Dirichlet form.

The characteristic design principle is therefore to **trade locality for probability**: replace an extremely rare short-range facilitating event by a long-range event that is likely, then pay an explicit path-transport cost.

## Representative IPS use

Sections 4--5 apply the architecture to FA-kf models and the Gravner--Griffeath KCM. Good blocks contain enough vacancies for motion, while super-good blocks contain the critical bootstrap droplet. Theorem 4.4 obtains near-optimal upper bounds on the characteristic relaxation/infection scales by combining the long-range constrained Poincare inequality with model-specific legal-path congestion estimates.

The technique is especially useful in low-vacancy cooperative KCM, where demanding the critical droplet at a prescribed nearby location would lose its exponentially small equilibrium probability.

## Limitations

The method needs a product or sufficiently factorised equilibrium structure for the exterior variance decomposition, a directional/exterior ordering of the constraints, and quantitative control of both good-path percolation and the cost of converting/moving a good block into a super-good one. A likely long-range event alone does not prove relaxation: its coarse move must be realizable by legal microscopic KCM moves with controlled congestion.

This page is distinct from generic canonical-path comparison. Canonical paths enter later to estimate the microscopic implementation cost; the proof interface isolated here is the **long-range constrained Poincare inequality** that makes a rare mobile droplet usable at all. It is also distinct from the live block-bisection page, whose recursion splits geometry across scales instead of replacing rare local constraints by likely nonlocal path events.

## Sources

- Martinelli, Toninelli, *Towards a universality picture for the relaxation to equilibrium of kinetically constrained models*, Theorem 2 and Lemma 2.5; Definition 3.1, Theorem 3.2, Proposition 3.4 and Corollary 3.9, https://doi.org/10.1214/18-AOP1262.
- Author preprint: https://arxiv.org/abs/1701.00107.
