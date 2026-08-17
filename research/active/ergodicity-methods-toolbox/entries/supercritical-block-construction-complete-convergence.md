---
method_id: supercritical-block-construction-complete-convergence
title: Supercritical block construction and complete convergence
category: graphical-duality
targets:
  - convergence
model_scope: Interacting particle systems admitting a coarse space-time block process that dominates supercritical oriented percolation
source_status: primary-checked
primary_source: Anja Sturm and Jan M. Swart, "Voter models with heterozygosity selection," Annals of Applied Probability 18 (2008), 59--99
primary_pinpoint: Theorem 5; Theorem 4; Section 2.3; Section 4.2
primary_url: https://doi.org/10.1214/07-AAP444
application_source: same as primary source
application_pinpoint: Theorem 4 and Section 4.2
application_url: https://arxiv.org/abs/math/0701555
wiki_candidate: yes
---

# Supercritical block construction and complete convergence

## Criterion

A **block construction** replaces the microscopic process by a coarse process on a space-time lattice. Choose a spatial scale \(L\), a time scale \(T\), and a local good event saying that a prescribed particle pattern is present throughout an enlarged block and seeds neighboring blocks at the next coarse time. If the resulting good-block variables can be coupled from below by oriented site percolation with parameter \(p>p_c\), then supercritical percolation supplies indefinitely propagating occupied blocks and quantitative control of large surviving clusters.

Sturm--Swart implement this for the asymmetric double branching annihilating random walk (ADBARW), the interface/dual of the rebellious voter model. Their Theorem 5 states that for every \(p<1\), for sufficiently small model parameter \(\alpha\) one can choose \(L,T\) so that the coarse good-set process \((\chi_n)\) is coupled to oriented percolation \((W_n)\) with parameter \(p\) and

\[
W_n\subset \chi_n\qquad\text{for every }n\ge0.
\]

Section 4.2 chooses \(p>p_c\). The resulting supercritical comparison is a principal input into Theorem 4: for small \(\alpha\), the rebellious voter model has coexistence and survival, and from an arbitrary initial law its distribution converges to the complete-convergence mixture

\[
\rho_0\delta_{\mathbf0}+\rho_1\delta_{\mathbf1}+
(1-\rho_0-\rho_1)\nu^{1/2}_X,
\]

where \(\rho_q\) is the probability of eventual absorption in the constant state \(q\).

## Mechanism

The microscopic process need not itself be monotone. Instead, one identifies a local event whose probability can be made close to one and whose dependencies have finite range on the coarse lattice. A large occupied seed in one block is likely to create suitable seeds in neighboring future blocks. After arranging finite-range dependence, a domination theorem replaces the dependent good-block field by an independent oriented percolation with a slightly smaller parameter.

This creates a robust macroscopic survival skeleton. Supercritical percolation then does more than merely show positive survival probability: it supplies repeated large occupied regions and comparison with its upper invariant process. In the Sturm--Swart proof this yields, for the ADBARW, extinction versus unbounded growth and asymptotic overlap properties for independently evolving copies. Combined with the model's duality, those properties identify the only possible nonabsorbing limit and establish complete convergence.

The proof interface is therefore opposite to **subcritical disagreement domination**. There, a dominating space-time process must die so that two copies agree. Here, a coarse process must dominate a **surviving** oriented percolation so that a persistent active phase can be controlled and its long-time law identified.

## Representative IPS use

The rebellious voter model is a one-dimensional spin-flip system with two absorbing constant states. Its interface is the ADBARW, a parity-preserving branching-annihilating particle system. Section 2.3 defines coarse intervals and good blocks for the ADBARW. Theorem 5 proves the oriented-percolation domination, and Section 4.2 uses it to prove Theorem 4. Thus the block construction is not merely a survival heuristic: it feeds directly into a complete-convergence theorem for a spin system from arbitrary initial laws.

## Limitations

A useful block construction requires a seed event that both propagates with probability close to one and has sufficiently local dependence after enlarging the block. Establishing these estimates is often the main model-specific work. The conclusion also needs additional ingredients beyond percolation survival: complete convergence in the cited application uses duality and information about intersections of surviving dual/interface processes. Supercritical domination alone therefore does not automatically identify all invariant laws. Finally, the spatial and temporal scales may be large and parameter-dependent, so the method is usually qualitative or coarse quantitative rather than a sharp relaxation-rate tool.

## Sources

Primary checked source: Sturm and Swart, *Voter models with heterozygosity selection*, Ann. Appl. Probab. 18 (2008), 59--99. Theorem 5 and Section 2.3 give the block comparison with oriented percolation; Theorem 4 and Section 4.2 use a choice \(p>p_c\) in the complete-convergence proof.