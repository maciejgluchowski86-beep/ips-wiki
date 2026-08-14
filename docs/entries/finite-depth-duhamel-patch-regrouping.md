---
title: Finite-depth Duhamel patch regrouping
status: observation
audit: current
tags:
  - PDE
  - Duhamel formula
  - branching tree
  - patch
---

# Finite-depth Duhamel patch regrouping

A finite Duhamel expansion indexed by planar binary trees can be reindexed by maximal left-child chains. This is a finite combinatorial observation: it changes the indexing of the same finite sum and makes no assertion about convergence, integrability, or an infinite-depth random estimator.

## Maximal-left patch decomposition

Let \(\tau\) be a finite rooted planar full binary tree. A *patch* is a maximal chain of internal vertices obtained by repeatedly following the left child. A patch begins at the root or at an internal vertex that is a right child. Every internal vertex belongs to exactly one such chain.

Contract each patch to one vertex. To retain enough information to reconstruct the planar tree, decorate each contracted patch by

- its length; and
- the ordered right subtrees attached at the successive vertices of the chain, from top to bottom.

Call the result the *decorated patch skeleton*.

## Observation

The map
\[
\tau
\longmapsto
\text{decorated patch skeleton of }\tau
\]
is a bijection between finite rooted planar full binary trees and recursively decorated patch skeletons of the preceding form.

Consequently, if a finite Duhamel or Picard expansion has the form
\[
\sum_{\tau\in\mathcal T_N} V_\tau
\tag{1}
\]
for a finite family \(\mathcal T_N\) of planar binary trees, the same sum may be indexed uniquely by decorated patch skeletons. Any nested contribution along one maximal left chain may be grouped as one block before the finite sum is evaluated.

## Proof

Starting from the root and from every internal vertex that is a right child, follow left children until the chain terminates. These chains are disjoint and cover all internal vertices, so the decomposition is unique.

For the inverse map, replace each decorated patch vertex by a left chain of the recorded length and reattach the recorded right subtrees in their recorded order. Applying this operation recursively reconstructs exactly one planar tree. The two constructions are inverse.

Since \(\mathcal T_N\) in (1) is finite, replacing each tree by its decorated skeleton is only a reindexing of a finite sum. No interchange of an infinite series, limiting operation, or absolute value is involved.

The observation is useful when several consecutive signed operators are to be kept inside one finite block before an estimate is applied. Any analytic gain from doing so is a separate question.
