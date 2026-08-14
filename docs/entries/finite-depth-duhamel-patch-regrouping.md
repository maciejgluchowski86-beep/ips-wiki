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

The construction uses the [heat semigroup and Duhamel formula](mild-formulation-and-branching-diffusion-representation.md), the deterministic [binary Duhamel tree](branching-diffusions-and-duhamel-trees.md), and the distinction between signed exactness and moment control explained in [Importance-sampling compensators](importance-sampling-compensators.md).

**References.** None: the finite-depth regrouping below is proved here.

## Quadratic Hessian mild equation

Let

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z)
$$

and consider the forward-time equation

$$
\partial_tv
=
\frac12\partial_x^2v
+\lambda(\partial_x^2v)^2,
\qquad
v(0,\cdot)=\phi.
\tag{1}
$$

Write

$$
z=\partial_x^2v.
$$

For a smooth solution, differentiating (1) twice gives

$$
\partial_tz
=
\frac12\partial_x^2z
+\lambda\partial_x^2(z^2),
\qquad
z(0,\cdot)=\phi''.
\tag{2}
$$

Hence the mild equation for \(z\) is

$$
z(t)
=
P_t\phi''
+\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
\tag{3}
$$

Define the bilinear Duhamel operator

$$
\mathcal B(f,g)(t)
=
\lambda\int_0^t
\partial_x^2P_{t-s}[f(s)g(s)]\,ds.
\tag{4}
$$

Then (3) is \(z=L+\mathcal B(z,z)\), where \(L(t)=P_t\phi''\).

## Finite Duhamel trees

Set

$$
z^{[0]}=L,
\qquad
z^{[N+1]}
=L+\mathcal B(z^{[N]},z^{[N]}).
\tag{5}
$$

Expanding (5) algebraically gives a finite sum indexed by rooted planar binary trees of height at most \(N\). A leaf contributes \(L\). If a tree \(\tau\) has left and right subtrees \(\tau_L,\tau_R\), its contribution is defined recursively by

$$
V_\tau
=
\mathcal B(V_{\tau_L},V_{\tau_R}).
\tag{6}
$$

The planar convention records which child will continue a patch; it does not change the product in (4).

## Definition: Duhamel patch

A *patch* of a finite planar binary tree is a maximal chain of internal vertices obtained by repeatedly following the left child. Every internal vertex belongs to exactly one patch. The right child of each vertex is a side subtree; if that right child is itself internal, it is the root of another patch.

Contracting every maximal left chain to one vertex gives the *patch skeleton*. The skeleton records the incidence of the patches, while the length of each contracted chain records the number of consecutive Hessian events in that patch.

## Complete contribution of one patch

Suppose a patch has length \(m\geq1\), its successive right-subtree contributions are the smooth side profiles \(b_1,\ldots,b_m\), and the leftmost terminal contribution is \(G\). For fixed ordered times

$$
0<s_1<\cdots<s_m<t,
$$

define recursively

$$
\Xi_1
=
b_1(s_1)P_{s_1}G,
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

The complete signed contribution of the patch is

$$
\mathcal P_m[b_1,\ldots,b_m;G](t)
=
\lambda^m
\int_{0<s_1<\cdots<s_m<t}
\partial_x^2P_{t-s_m}\Xi_m
\,ds_1\cdots ds_m.
\tag{9}
$$

For \(m=0\), set \(\mathcal P_0[G](t)=P_tG\). Equations (7)--(9) are not estimates: they are the iterated Duhamel integral obtained by following the left spine and leaving every right child as a side factor.

## Theorem: exact finite-depth regrouping

For every finite depth \(N\), the expansion of \(z^{[N]}\) may be reorganized uniquely by its patch skeletons. Replacing every maximal left-spine chain by its complete contribution (7)--(9) gives exactly the same signed function \(z^{[N]}\).

In particular, composing all Hessian transfers inside a patch before taking absolute values is an exact finite-level operation. It neither discards nor adds a Duhamel-tree term.

## Proof

Every finite planar binary tree has a unique decomposition into maximal left-child chains: starting from any internal vertex that is either the root or a right child, follow left children until the chain ends. Distinct starting vertices generate disjoint chains and every internal vertex belongs to one of them. Thus finite binary trees are in bijection with their patch skeletons together with the lengths of the contracted chains and the side subtrees attached along each chain.

For a fixed tree, recursively expanding (6) along one maximal left chain gives exactly (7)--(9). The inequalities

$$
0<s_1<\cdots<s_m<t
$$

are the chronological constraints already present in the nested Duhamel integrals. No exchange of an infinite sum or conditionally convergent series occurs.

Finally, for fixed \(N\) only finitely many planar binary trees occur in (5). Reindexing this finite sum by the preceding bijection therefore leaves the sum unchanged. This proves the theorem.

## Finite-level patch factorization

The same decomposition can be randomized patch first. Conditional on a finite patch skeleton, assign independent random seeds to distinct side patches and sample the continuous data inside each patch from any positive proposal density. The reciprocal proposal factors are [importance-sampling compensators](importance-sampling-compensators.md). Conditional independence then gives products of conditional expectations across the side patches, while the compensators recover the signed integrals (7)--(9).

This finite-level factorization is an exact bookkeeping statement. It does not imply that an infinite-depth patch functional belongs to \(L^1\). In particular, the [Hermite composition identity](hermite-polynomials-and-gaussian-chaos.md) for a bare derivative chain does not survive unchanged when spatially varying multiplication operators occur between Hessian transfers. The corresponding infinite random-patch statement is recorded in the [\(L^1\) random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md).
