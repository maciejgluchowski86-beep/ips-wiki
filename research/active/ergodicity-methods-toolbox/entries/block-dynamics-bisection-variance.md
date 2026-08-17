---
method_id: block-dynamics-bisection-variance
title: Block dynamics and bisection variance decomposition
category: functional-inequality
targets:
  - spectral-gap
  - convergence
model_scope: Reversible spin and kinetically constrained systems admitting overlapping-block decompositions
source_status: primary-checked
primary_source: Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto, and Cristina Toninelli, Kinetically constrained spin models, Probability Theory and Related Fields 140 (2008), 459-504.
primary_pinpoint: Theorem 4.2 and its proof, especially equations (4.1), (4.8)-(4.10), pp. 471-476 of the published article; Theorem 3.3 for the renormalized application
primary_url: https://arxiv.org/abs/math/0610106
application_source: Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto, and Cristina Toninelli, Kinetically constrained spin models, Probability Theory and Related Fields 140 (2008), 459-504.
application_pinpoint: Theorem 6.1 for East and Theorem 6.3 for FA-1f
application_url: https://arxiv.org/abs/math/0610106
wiki_candidate: yes
---

# Block dynamics and bisection variance decomposition

## Criterion

A typical bisection argument controls the inverse finite-volume gap recursively. In Cancrini--Martinelli--Roberto--Toninelli, a large box at scale \(k\) is covered by two overlapping smaller boxes. An auxiliary two-block dynamics has inverse gap at most \((1-\sqrt{\varepsilon_k})^{-1}\), where \(\varepsilon_k\) is the probability of a bad configuration in the overlap. If \(\gamma_k\) is the worst inverse spectral gap at scale \(k\), their equations (4.8)-(4.10) yield
\[
\gamma_k\le
\frac{1}{1-\sqrt{\varepsilon_k}}
\left(1+\frac1{s_k}\right)\gamma_{k-1}.
\]
Here \(s_k\) counts alternative placements of the overlap used for averaging. If
\[
\prod_k
(1-\sqrt{\varepsilon_k})^{-1}(1+s_k^{-1})<\infty,
\]
then the inverse gaps stay uniformly bounded and the infinite-volume dynamics has a positive spectral gap.

## Mechanism

Start from the Poincare inequality for an auxiliary block chain that resamples one subblock freely and the other only when the overlap is in a good state. This decomposes the variance into conditional block variances. Each conditional variance is then bounded by the already-known Poincare inequality at the smaller scale. Because the two blocks overlap, a local Dirichlet contribution in the overlap can be counted twice. Rather than accept that loss at every scale, one shifts the decomposition through \(s_k\) possible overlap positions and averages, producing the factor \(1+1/s_k\).

The second loss, \((1-\sqrt{\varepsilon_k})^{-1}\), is the price for the auxiliary block constraint failing. If bad-overlap probabilities decrease sufficiently fast with scale, both losses are summable multiplicatively. This is the central reusable idea: prove relaxation on a large system by a recursive variance decomposition whose scale losses form a convergent product.

## Representative IPS use

Cancrini--Martinelli--Roberto--Toninelli use the construction first for a general auxiliary KCSM (Theorem 4.2), then renormalize a concrete constrained spin model onto blocks. Theorem 3.3 says that a sufficiently probable good block event with a suitable legal-move property implies a positive infinite-volume spectral gap. For East, Theorem 6.1 adapts the same bisection recursion to prove positive gap for every vacancy density \(q>0\) and to sharpen its small-\(q\) asymptotics. For FA-1f, Theorem 6.3 obtains positive gap for every \(q>0\) via the internally-spanned-block criterion.

## Limitations

This is not an automatic consequence of using larger blocks. One needs a good event whose failure probability decays fast enough, legal dynamics connecting good boundary configurations to the original constrained moves, and smaller-scale Poincare constants that can actually be inserted into the recursion. The geometry of overlaps can be model-specific. Near a bootstrap-percolation threshold, the block scale needed before \(\varepsilon_k\) becomes small may be enormous, yielding poor quantitative constants. The argument is designed around reversibility and variance; entropy or nonreversible analogues require additional work.

## Sources

- Cancrini, Martinelli, Roberto, Toninelli, *Kinetically constrained spin models*, Theorem 4.2 and equations (4.1), (4.8)-(4.10), https://arxiv.org/abs/math/0610106.
- Same paper, Theorem 3.3, Theorem 6.1 (East) and Theorem 6.3 (FA-1f), for KCSM applications of the multiscale recursion.
