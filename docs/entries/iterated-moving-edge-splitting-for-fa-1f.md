---
title: Iterated moving-edge splitting for one-dimensional FA-1f
status: proved here
tags:
  - FA-1f
  - CBSEP
  - chronology
  - graphical construction
  - regeneration
---

# Iterated moving-edge splitting for one-dimensional FA-1f

This entry amplifies the [moving-edge CBSEP resampling](moving-edge-cbsep-resampling-for-fa-1f.md). A single tagged vacancy can be followed through successive complete FA branch/coalescence excursions until one excursion ends with two adjacent vacancies. The number of excursions, the elapsed time, and the spatial displacement all have exponential tails depending only on the equilibrium vacancy density. The construction is uniform over the exterior FA history.

Use vacancy variables, with vacancy state \(1\), equilibrium vacancy density \(q\in(0,1)\), and \(p=1-q\).

## Iterated construction

Start at a stopping time \(\sigma_0\) at which a tagged site \(X_0\) is vacant. Choose either orientation and start the moving-edge resampling from \(X_0\), as in [moving-edge CBSEP resampling](moving-edge-cbsep-resampling-for-fa-1f.md). Let \(\sigma_1\) be its terminal time. Conditional on the graphical history up to \(\sigma_0\), its terminal edge has the law

$$
\pi_e(11)=\frac{q}{2-q},
\qquad
\pi_e(10)=\pi_e(01)=\frac{p}{2-q}.
\tag{1}
$$

If the output is \(11\), stop. If the output is a singleton, tag its unique vacant endpoint, choose the same orientation relative to that endpoint, and start a fresh moving-edge resampling. Continue recursively.

The auxiliary stopping coins used in distinct excursions are independent. The strong Markov property of the graphical construction gives fresh proposal processes after every \(\sigma_j\). Therefore the indicators that the successive outputs are \(11\) are i.i.d. Bernoulli with parameter

$$
s=\frac{q}{2-q}.
\tag{2}
$$

Let

$$
G=\inf\{j\ge1:\text{the }j\text{-th output is }11\}.
$$

Then

$$
\mathbb P(G>m)=(1-s)^m
=\left(\frac{2p}{2-q}\right)^m.
\tag{3}
$$

At the stopping time

$$
\tau_{\rm split}=\sigma_G
\tag{4}
$$

the physical FA configuration contains two adjacent vacancies. No assumption has been made on the configuration outside the successive moving edges.

## Time tail

For every unsuccessful excursion, the internal branch time is an independent exponential variable of rate \(q\), and after the branch the first coalescence time is an independent exponential variable of rate \(2p\). The successful excursion stops at its branch time. Hence \(\tau_{\rm split}-\sigma_0\) is stochastically dominated by

$$
\sum_{j=1}^{G}(E_j+F_j),
\tag{5}
$$

where \((E_j)\) are i.i.d. \({\rm Exp}(q)\), \((F_j)\) are i.i.d. \({\rm Exp}(2p)\), and these families are independent of the geometric variable \(G\). In particular, there exist constants \(c_t,C_t>0\), depending only on \(q\), such that

$$
\mathbb P(\tau_{\rm split}-\sigma_0>u)
\le C_t e^{-c_tu},
\qquad u\ge0.
\tag{6}
$$

Only the existence of such constants is used below. It follows immediately from the moment-generating functions in (5), choosing a sufficiently small positive exponential parameter.

## Spatial tail

During one moving-edge excursion, let \(N_j\) be the number of shifts caused by occupation of the tagged vacancy before the internal branch. The moving-edge buffer estimate gives, conditionally on the entire past,

$$
\mathbb P(N_j\ge m\mid\mathcal F_{\sigma_{j-1}})\le p^m.
\tag{7}
$$

The terminal singleton of an unsuccessful excursion differs by at most one further lattice step from the position reached before its branch. Consequently, if

$$
R=\max_{\sigma_0\le u\le\tau_{\rm split}}|X(u)-X_0|
$$

denotes the maximal displacement of the tagged moving edge before the successful split, then

$$
R\le G+\sum_{j=1}^{G}N_j.
\tag{8}
$$

The geometric tail (3), the conditional geometric bound (7), and an exponential-moment argument therefore give constants \(c_x,C_x>0\), depending only on \(q\), such that

$$
\mathbb P(R\ge m)\le C_xe^{-c_xm},
\qquad m\ge0.
\tag{9}
$$

Thus for every \(\varepsilon>0\) there are deterministic \(T,W<\infty\), depending only on \(q,\varepsilon\), for which a tagged vacancy produces an adjacent vacant pair before time \(T\), without its moving edge leaving the spatial interval of radius \(W\) around its initial position, with probability at least \(1-\varepsilon\).

## What the lemma does and does not provide

The amplification in (3)--(9) is a consequence of repeated complete chronology averages. It does not select a favorable deterministic word of FA updates. Each trial integrates all update counts and orders up to the moving-edge regeneration time, and failure returns the construction to the same singleton coarse state from which the strong Markov property starts the next trial.

The lemma supplies a robust local branching mechanism for every \(q>0\), even when the one-shot double-vacancy probability \(q/(2-q)\) is very small. It does not yet produce two long-lived independent descendants: after \(\tau_{\rm split}\), one of the adjacent vacancies may subsequently become occupied. A global block construction therefore needs an additional separation or persistence argument before the two outputs can be used as independent daughter seeds.
