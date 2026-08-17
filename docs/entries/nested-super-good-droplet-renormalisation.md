---
title: Nested super-good-droplet renormalisation
status: literature
audit: current
tags:
  - KCSM
  - renormalisation
  - mobile droplets
---

# Nested super-good-droplet renormalisation

## Criterion

A Matryoshka-type KCM argument builds a sequence of increasingly large constrained state spaces in which mobility at scale \(n\) is certified by the presence of a mobile core from scale \(n-1\), surrounded by an environment that lets that core move. Hartarsky--Martinelli--Toninelli implement this explicitly for FA-2f.

Definition 4.2 introduces nested rectangles \(\Lambda^{(n)}\) whose side lengths increase gradually with n. Definition 4.3 defines the event \(SG^\omega(R)\) recursively: a class-n rectangle R is super-good if it contains a class-\((n-1)\) super-good core and the strips between that core and the boundary satisfy directional traversability conditions. Remark 4.4 shows that the FA-2f chain restricted to such a super-good event is irreducible.

Let \(\gamma^\omega(R)\) denote the inverse spectral gap of this restricted chain. The two scale-extension estimates are Lemmas 4.9 and 4.10. In schematic form they bound
\[
\gamma(\Lambda^{(n+1)})
\lesssim e^{O(\log^2(1/q))}\,\gamma(\Lambda^{(n,+)}),
\qquad
\gamma(\Lambda^{(n,+)})
\lesssim q^{-O(1)}\,\gamma(\Lambda^{(n)}).
\]
Iterating these nested extensions yields Proposition 4.7,
\[
\max_\omega \gamma^\omega(\Lambda^{(n)})
\le \exp\!\bigl(O(\log^2(1/q))\,n\bigr),
\]
up to the final mobile-droplet scale.

## Mechanism

The essential object is not a static good block but a **good object containing a smaller good object**. At the smallest scale one has a microscopic infected seed. At the next scale that seed is allowed to move inside a traversable rectangle. The same rectangle then serves as the mobile core of a larger rectangle, and so on.

This recursive geometry solves a problem that a one-shot block estimate cannot: the critical droplet is rare, so repeatedly demanding independent fresh droplets at every scale would multiply prohibitive probability costs. Instead, one preserves a single mobile core and surrounds it by relatively inexpensive traversable material. The Poincare argument follows the same nesting. Auxiliary block chains first equilibrate the position of the core inside a slightly enlarged rectangle; a second comparison restores the exact next-scale geometry. Lemmas 4.9 and 4.10 quantify those two moves, and their product can be iterated because the output event at scale n is exactly the input event at scale \(n+1\).

The reusable interface is therefore a matched pair:
\[
\text{nested mobility events }SG_n
\quad+\quad
\text{recursive gap estimate }\gamma_{n+1}\le C_n\gamma_n.
\]
If \(\prod_n C_n\) remains below the dominant physical scale, microscopic mobility propagates to the macroscopic droplet scale.

## Representative IPS use

For two-dimensional FA-2f, the final super-good square is called a mobile droplet. Proposition 4.7 proves that the FA-2f dynamics conditioned on such a droplet relaxes at a cost that is subleading compared with the exponentially rare probability of creating the droplet. Section 5 then treats these droplets as effective mobile objects and uses their controlled internal relaxation in the sharp upper bound for the infection time of the origin.

This is the archetypal use of the nested construction: the rare-event probability determines the leading time scale, while the Matryoshka-type Poincare induction proves that manipulating the droplet does not introduce a larger hidden dynamical cost.

## Limitations

The construction is strongly model-geometric. One must invent nested events whose probabilities remain controlled, prove legal mobility of the smaller core through each surrounding layer, and obtain scale-extension inequalities whose accumulated loss is acceptable. A recursive definition by itself has no content unless the restricted dynamics is irreducible and the one-scale Poincare comparisons are quantitative.

The method uses block and bisection arguments internally, but it is distinct from the generic live block-dynamics page: the load-bearing input is the **nested super-good event hierarchy**, engineered so the same rare mobile droplet survives through every scale rather than being resampled independently. The term “Matryoshka” is later expository terminology; the primary paper formulates the mechanism as recursively defined super-good rectangles and mobile droplets.

## Sources

- Hartarsky, Martinelli, Toninelli, *Sharp threshold for the FA-2f kinetically constrained model*, Definitions 4.2--4.3, Remark 4.4, Proposition 4.7, Lemmas 4.9--4.10, https://doi.org/10.1007/s00440-022-01169-2.
- Author preprint: https://arxiv.org/abs/2012.02557.
