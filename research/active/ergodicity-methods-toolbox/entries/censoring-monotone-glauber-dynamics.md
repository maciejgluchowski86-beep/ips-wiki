---
method_id: censoring-monotone-glauber-dynamics
title: Censoring inequalities for monotone Glauber dynamics
category: coupling
targets:
  - mixing
  - convergence
model_scope: Finite monotone spin systems with single-site or block heat-bath updates, started from an extremal or suitably ordered initial law.
source_status: primary-checked
primary_source: Yuval Peres and Peter Winkler, "Can extra updates delay mixing?", Communications in Mathematical Physics 323 (2013), 1007-1016.
primary_pinpoint: Theorem 1.1 and the paragraph immediately following it; Theorem 1.2 for block-to-single-site mixing.
primary_url: https://doi.org/10.1007/s00220-013-1776-0
application_source: Yuval Peres and Peter Winkler, same paper.
application_pinpoint: Theorem 1.2 and the Ising-model-on-trees application described in the introduction.
application_url: https://arxiv.org/abs/1112.0603
wiki_candidate: yes
---

# Censoring inequalities for monotone Glauber dynamics

## Criterion

Let $\pi$ be a monotone spin-system measure on a finite partially ordered configuration space, and perform heat-bath updates at sites $v_1,\ldots,v_m$. Start from the maximal configuration. Let $\mu$ be the law after all updates and let $\nu$ be the law obtained after deleting any subsequence of those updates. Peres--Winkler Theorem 1.1 proves

$$
\mu\preceq \nu,
\qquad
\|\mu-\pi\|_{\rm TV}\le \|\nu-\pi\|_{\rm TV}.
$$

Thus censoring updates cannot make this monotone dynamics mix faster when it starts from the top state. By spin reversal there is the corresponding statement from the minimal state. The paper also notes the more general initial-law form: it is enough that the density $\mu_0/\pi$ be increasing; after uncensored updates that property is preserved, while censoring keeps the resulting law stochastically farther in the appropriate order.

Theorem 1.2 turns this comparison into a block-to-single-site tool. If an appropriate block dynamics contracts expected Hamming distance by a fixed factor, censoring lets one simulate its useful block refreshes using ordinary single-site updates and deduce an $O(n\log n)$ single-site mixing bound.

## Mechanism

A heat-bath update replaces one coordinate by its conditional equilibrium distribution. Monotonicity permits all such updates to be coupled by the same random variables so that order is preserved. Starting above equilibrium, an update locally removes information about the ordered initial state. The censoring theorem says this intuitive one-step effect remains valid under arbitrary compositions: inserting updates pushes the law downward in stochastic order while also decreasing total-variation distance to $\pi$.

This makes deliberately simplified schedules legitimate upper bounds. One can delete inconvenient updates, retain only updates arranged into analytically convenient blocks or epochs, and prove mixing for the censored chain. Since the original chain has at least as many useful updates, its total-variation distance is no larger. The method is therefore not itself a contraction estimate; it transfers a contraction proved for a structured update schedule back to the actual Glauber dynamics.

## Representative IPS use

Peres--Winkler use the theorem to complete the block-dynamics route for the ferromagnetic Ising model on regular trees. When block dynamics contracts Hamming distance, Theorem 1.2 yields $O(n\log n)$ mixing for random single-site Glauber dynamics. The same comparison principle is useful whenever a monotone spin system has a tractable block schedule but the real dynamics chooses sites randomly.

A second use is schedule comparison. On bipartite graphs, systematic alternation between the two bipartition classes cannot improve the mixing time by more than the logarithmic loss established in the paper relative to random-site updates.

## Limitations

The order hypotheses are essential. The theorem is designed for monotone spin systems and ordered initial laws; it is not a generic statement that extra Markov-chain updates help. Counterexamples exist outside this setting, including proper-coloring dynamics. Even within an attractive system, starting from an arbitrary nonordered initial distribution does not automatically satisfy the theorem's hypotheses.

Censoring also does not create a useful mixing estimate by itself. A structured censored schedule still needs an independent contraction, block-mixing, or spatial-mixing argument. Finally, the theorem concerns finite-volume Glauber-type chains; infinite-volume ergodicity requires a separate uniform-in-volume passage.

## Sources

- Peres and Winkler, *Communications in Mathematical Physics* 323 (2013), Theorems 1.1-1.2. DOI: https://doi.org/10.1007/s00220-013-1776-0. Preprint: https://arxiv.org/abs/1112.0603.
