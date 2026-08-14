---
title: Finite-depth Duhamel patch regrouping
status: proved here
tags:
  - PDE
  - Duhamel formula
  - branching tree
  - patch
  - Hessian
---

# Finite-depth Duhamel patch regrouping

For the quadratic Hessian equation on the torus, every finite Picard expansion of the mild equation is a finite sum over planar binary Duhamel trees. Grouping consecutive left-child vertices into maximal chains gives an exact signed reorganization of this finite expansion. The point of the regrouping is that all Hessian transfers along one chain may be composed before absolute values are taken. No assertion about an infinite random-patch estimator is part of this theorem.

The construction uses the [heat semigroup and Duhamel formula](mild-formulation-and-branching-diffusion-representation.md), the deterministic [binary Duhamel tree](branching-diffusions-and-duhamel-trees.md), and the distinction between signed exactness and moment control explained in [Importance-sampling compensators](importance-sampling-compensators.md). Its place in the larger programme is summarized in the [PDE branching-representations overview](../pde-branching-representations.md).

**References.** None: the finite-depth regrouping below is proved here.

## Quadratic Hessian mild equation

Fix a horizon \(T>0\), a parameter \(\lambda\in\mathbb R\), and smooth periodic data \(\phi\in C^\infty(\mathbb T)\), where

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Consider

$$
\partial_tv
=
\frac12\partial_x^2v
+\lambda(\partial_x^2v)^2,
\qquad
v(0,\cdot)=\phi,
\qquad
0\leq t\leq T.
\tag{1}
$$

Write

$$
z=\partial_x^2v.
$$

For a smooth solution,

$$
\partial_tz
=
\frac12\partial_x^2z
+\lambda\partial_x^2(z^2),
\qquad
z(0,\cdot)=\phi''.
\tag{2}
$$

Hence

$$
z(t)
=
P_t\phi''
+\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
\tag{3}
$$

Define

$$
\mathcal B(f,g)(t)
=
\lambda\int_0^t
\partial_x^2P_{t-s}[f(s)g(s)]\,ds.
\tag{4}
$$

Then (3) is \(z=L+\mathcal B(z,z)\), where \(L(t)=P_t\phi''\). The theorem below is algebraic: it does not assume convergence of an infinite Picard sequence or existence of a solution of (1).

## Finite Duhamel trees

Set

$$
z^{[0]}=L,
\qquad
z^{[N+1]}
=L+\mathcal B(z^{[N]},z^{[N]}).
\tag{5}
$$

Expanding (5) gives a finite sum indexed by rooted planar binary trees of height at most \(N\). A leaf contributes \(L\). If \(\tau\) has left and right subtrees \(\tau_L,\tau_R\), its contribution is

$$
V_\tau
=
\mathcal B(V_{\tau_L},V_{\tau_R}).
\tag{6}
$$

The planar convention records which child continues a patch; it does not change the product in (4).

## Definition: Duhamel patch

A *patch* is a maximal chain of internal vertices obtained by repeatedly following the left child. Every internal vertex belongs to exactly one patch. The right child of each vertex is a side subtree; if that right child is internal, it begins another patch.

Contracting every maximal left chain to one vertex gives the *patch skeleton*. A *decorated patch skeleton* records, for each contracted chain, both its length and the ordered side-subtree attachment slots from the root of the chain to its bottom vertex. This ordered attachment data is part of the definition: a contracted patch graph decorated only by chain lengths need not determine the original planar tree.

Equivalently, if the root maximal-left chain has length \(m\) and successive right subtrees \(\sigma_1,\ldots,\sigma_m\), the decoration at the root is

$$
(m;D(\sigma_1),\ldots,D(\sigma_m)),
$$

with the same rule applied recursively. The explicit inverse, and hence the full bijection with finite planar full binary trees, is proved in [Canonical raw signed measures for finite quadratic-Hessian trees](canonical-raw-signed-measures-for-finite-quadratic-hessian-trees.md).

## Complete contribution of one patch

Suppose a patch has length \(m\geq1\), successive right-subtree contributions \(b_1,\ldots,b_m\), and leftmost terminal contribution \(G\). For

$$
0<s_1<\cdots<s_m<t,
$$

define

$$
\Xi_1=b_1(s_1)P_{s_1}G,
\tag{7}
$$

and, for \(2\leq r\leq m\),

$$
\Xi_r
=
b_r(s_r)
\partial_x^2P_{s_r-s_{r-1}}\Xi_{r-1}.
\tag{8}
$$

The complete signed contribution is

$$
\mathcal P_m[b_1,\ldots,b_m;G](t)
=
\lambda^m
\int_{0<s_1<\cdots<s_m<t}
\partial_x^2P_{t-s_m}\Xi_m
\,ds_1\cdots ds_m.
\tag{9}
$$

For \(m=0\), set \(\mathcal P_0[G](t)=P_tG\). Equations (7)--(9) are the nested Duhamel integral along the left spine, not an estimate.

## Theorem: exact finite-depth regrouping

For every integer \(N\geq0\), the expansion of \(z^{[N]}\) on \([0,T]\) may be reorganized uniquely by its decorated patch skeletons. Replacing every maximal left-spine chain by its complete contribution (7)--(9) gives exactly the same signed function \(z^{[N]}\).

In particular, composing all Hessian transfers inside a patch before taking absolute values is an exact finite-level operation. It neither discards nor adds a Duhamel-tree term.

## Proof

Every finite planar binary tree has a unique decomposition into maximal left-child chains: starting from any internal vertex that is either the root or a right child, follow left children until the chain ends. Distinct starting vertices generate disjoint chains and every internal vertex belongs to one of them. Recording the length of each chain together with the ordered right subtree at every position gives exactly the decorated skeleton defined above. Conversely, each decorated skeleton reconstructs the tree by building each left chain and reattaching its ordered side subtrees. Thus the encoding is bijective.

For a fixed tree, recursively expanding (6) along one maximal left chain gives exactly (7)--(9). The inequalities

$$
0<s_1<\cdots<s_m<t
$$

are the chronological constraints already present in the nested Duhamel integrals. No exchange of an infinite sum or conditionally convergent series occurs.

For fixed \(N\), only finitely many planar binary trees occur in (5). Reindexing this finite sum by the preceding bijection therefore leaves the signed expansion unchanged.

## Finite-level patch factorization

The finite patch decomposition may be randomized patch first by assigning independent auxiliary random seeds to distinct side patches conditional on a fixed finite decorated patch skeleton. If the data inside a patch are sampled from positive proposal laws, reciprocal densities are [importance-sampling compensators](importance-sampling-compensators.md), and their algebraic cancellation recovers the signed patch integrals (7)--(9).

This statement concerns finite signed exactness and conditional factorization. A compensated finite-patch random variable still requires an absolute-moment estimate before it may be used as an ordinary expectation, and nothing here alone implies an infinite-depth \(L^1\) theorem. The exact finite conditional statement is isolated in [Conditional factorization for finite PDE patches](conditional-factorization-for-finite-pde-patches.md).

The missing fixed-tree absolute-moment step is supplied by [Canonical raw signed measures for finite quadratic-Hessian trees](canonical-raw-signed-measures-for-finite-quadratic-hessian-trees.md): if \(\phi''\in C^\alpha\) for some \(\alpha>0\), every fixed finite tree carries a genuine finite canonical raw signed measure whose total mass is its deterministic Duhamel profile. What can fail at infinite depth is summability of those finite total variations.

The later results separate the possible infinite-depth outcomes. [Theorem C-prime](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) completely averages every continuous interior variable and is \(L^1\) under the Catalan smallness condition. The [raw-barycenter obstruction](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) shows that retaining the canonical raw signed contribution as a conditional barycenter is non-\(L^1\) for one fixed smooth datum. The [time-spine theorem](time-spine-coarsening-for-quadratic-hessian-patches.md) gives a structured target-uniform intermediate representation on a stronger regime, and the [residual signed variation characterization](residual-signed-variation-characterization-for-coarsened-patches.md) gives the exact abstract criterion for skeleton-preserving coarsenings. The remaining [random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md) concerns structured target-uniform coarsenings on the full C-prime regime.
