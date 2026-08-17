---
title: Block and approximate factorization of entropy
status: literature
audit: current
tags:
  - ergodicity methods
  - functional inequalities
  - entropy
---

# Block and approximate factorization of entropy

## Criterion

For a probability law \(\mu\) on spins \([q]^V\), approximate tensorization of entropy is the inequality

\[
\operatorname{Ent}_\mu(f)
\le C_1\sum_{v\in V}\mu[\operatorname{Ent}_v(f)],
\qquad f\ge0,
\]

where \(\operatorname{Ent}_v\) is entropy under resampling the spin at \(v\) conditional on all others. Chen--Liu--Vigoda Definition 2.2 introduces the coarser \(\ell\)-uniform block factorization

\[
\frac{\ell}{n}\operatorname{Ent}(f)
\le
C\binom n\ell^{-1}
\sum_{|S|=\ell}\mu[\operatorname{Ent}_S(f)].
\]

Their Lemma 2.3 shows that, for a \(b\)-marginally bounded Gibbs measure on a graph of maximum degree \(\Delta\), linear-size block factorization with \(\ell=\lceil\theta n\rceil\), \(\theta\le b^2/(12\Delta)\), implies single-site approximate tensorization with
\(C_1=18C\log(1/b)/b^4\). A volume-uniform factorization constant therefore yields a volume-uniform modified log-Sobolev/entropy-decay estimate and optimal-order Glauber mixing.

## Mechanism

The proof architecture separates two tasks. First prove that entropy dissipates when a **large random block** is refreshed. This may be much easier than controlling every single-site conditional entropy, because a macroscopic update destroys long dependency chains. Second, use locality of the Gibbs interaction and marginal lower bounds to "shatter" a large-block update into many nearly independent small components. Lemma 2.3 turns the resulting large-block inequality into approximate single-site tensorization.

The block inequality itself can be obtained in several ways. In Chen--Liu--Vigoda, Lemma 2.7 identifies block factorization exactly with global entropy contraction of an associated weighted simplicial complex, while Lemma 2.5 derives it from [spectral independence](spectral-independence-local-to-global.md) plus marginal bounds. Thus spectral independence is one sufficient input, not the definition of the factorization method.

Once approximate tensorization holds, entropy dissipation for heat-bath Glauber dynamics is immediate: the generator's entropy production is the sum of single-site conditional entropies. This gives an [mLSI-type](log-sobolev-modified-log-sobolev.md) exponential decay of relative entropy and, using standard finite-state comparisons, rapid total-variation mixing. The variance analogue gives the corresponding Poincare/spectral-gap architecture; Fact A.3 makes this equivalence explicit.

## Representative IPS use

Chen--Liu--Vigoda use this chain to prove optimal \(O(n\log n)\) Glauber mixing on bounded-degree graphs for the hard-core model and more generally antiferromagnetic two-spin systems throughout the tree-uniqueness regime, together with applications to colorings and matchings. The key advance over an influence-to-gap argument is entropic: spectral information is first upgraded to block entropy contraction and then to approximate tensorization, which is strong enough for optimal mixing.

This entry intentionally overlaps the spectral-independence page at one interface and the LSI/mLSI page at another. Its distinct method is the intermediate **factorization theorem**: establish a conditional entropy decomposition, then let general semigroup machinery convert that decomposition into relaxation.

## Limitations

Approximate tensorization is strong; it can fail near phase coexistence or when conditional marginals become very small. The reduction from block to single-site factorization in Lemma 2.3 uses bounded degree, locality, and a uniform marginal lower bound. A block entropy inequality with constants deteriorating with \(n\) may give little useful mixing information. In constrained or conservative IPS, single-site heat-bath updates may not preserve the state space, so the relevant conditional blocks and entropy production must be redesigned rather than imported verbatim. Finally, proving block factorization can be as difficult as proving mixing unless one has an independent mechanism such as spatial mixing, spectral independence, or a recursive block estimate.

## Sources

- Chen, Liu, Vigoda, *Optimal Mixing of Glauber Dynamics: Entropy Factorization via High-Dimensional Expansion*, Definitions 2.1--2.2, Lemmas 2.3, 2.5, 2.7, Theorem 2.9, and Appendix A, https://doi.org/10.1137/21M1443340; preprint https://arxiv.org/abs/2011.02075.
