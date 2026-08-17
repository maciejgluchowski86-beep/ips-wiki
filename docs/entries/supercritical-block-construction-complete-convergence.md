---
title: Supercritical block construction and complete convergence
status: literature
audit: current
tags:
  - block construction
  - oriented percolation
  - complete convergence
---

# Supercritical block construction and complete convergence

## Criterion

A block construction replaces a microscopic process by a coarse process on a space-time lattice. Choose a spatial scale \(L\), a time scale \(T\), and a local good event saying that a prescribed particle pattern is present throughout an enlarged block and seeds neighboring blocks at the next coarse time. If the resulting good-block variables can be coupled from below by oriented site percolation with parameter \(p>p_c\), then supercritical percolation supplies indefinitely propagating occupied blocks and control of large surviving clusters.

Sturm--Swart implement this for the asymmetric double branching annihilating random walk, the interface/dual of the rebellious voter model. Their Theorem 5 states that for every \(p<1\), for sufficiently small model parameter \(\alpha\) one can choose \(L,T\) so that a coarse good-set process \((\chi_n)\) can be coupled to oriented percolation \((W_n)\) with
\[
W_n\subset \chi_n\qquad\text{for every }n\ge0.
\]
Section 4.2 chooses \(p>p_c\). This supercritical comparison is a principal input into Theorem 4, which gives complete convergence of the rebellious voter model to a mixture of its two absorbing states and its nontrivial coexisting invariant law.

## Mechanism

The microscopic process need not be monotone. Instead, one identifies a local event whose probability can be made close to one and whose dependencies have finite range on the coarse lattice. A large occupied seed in one block is likely to create suitable seeds in neighboring future blocks. After arranging finite-range dependence, a domination theorem replaces the dependent good-block field by an independent oriented percolation with slightly smaller parameter.

This creates a robust macroscopic survival skeleton. In the Sturm--Swart proof it yields extinction-versus-unbounded-growth and asymptotic overlap properties for surviving interface processes. Combined with duality, those properties identify the nonabsorbing limit and establish complete convergence.

The proof interface is opposite to [subcritical dynamical disagreement percolation](dynamical-disagreement-space-time-percolation.md). There, a dominating space-time process must die so that two copies agree. Here, a coarse process must dominate a surviving oriented percolation so that a persistent active phase can be controlled.

## Representative IPS use

The rebellious voter model is a one-dimensional spin-flip system with two absorbing constant states. Its interface is a parity-preserving branching-annihilating particle system. Section 2.3 defines coarse intervals and good blocks, Theorem 5 proves oriented-percolation domination, and Section 4.2 uses it in the proof of Theorem 4. Thus the block construction feeds directly into a complete-convergence theorem from arbitrary initial laws.

## Limitations

A useful block construction requires a seed event that propagates with probability close to one and has sufficiently local dependence after enlarging the block. Establishing these estimates is often the main model-specific work. Complete convergence also needs ingredients beyond percolation survival; in the cited application it uses duality and intersection information for surviving dual/interface processes. The method is usually qualitative or coarse quantitative rather than a sharp relaxation-rate tool.

## Sources

- Sturm and Swart, *Voter models with heterozygosity selection*, Ann. Appl. Probab. 18 (2008), 59--99, Theorem 5 and Section 2.3 for the block comparison, Theorem 4 and Section 4.2 for complete convergence, https://doi.org/10.1214/07-AAP444.
- Open preprint: https://arxiv.org/abs/math/0701555.
