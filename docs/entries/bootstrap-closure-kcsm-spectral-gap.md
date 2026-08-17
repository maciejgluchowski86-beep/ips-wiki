---
title: Bootstrap-percolation closure to KCSM spectral gap
status: literature
audit: current
tags:
  - KCSM
  - bootstrap percolation
  - spectral gap
---

# Bootstrap-percolation closure to KCSM spectral gap

## Criterion

For a kinetically constrained spin model (KCSM), associate to a finite block a deterministic bootstrap emptying rule using the same local constraints. Cancrini--Martinelli--Roberto--Toninelli call a block internally spanned when, with occupied boundary outside the block, there exists a sequence of legal KCSM moves that connects the given configuration to the completely empty configuration inside the block (Definition 3.4).

Their Theorem 3.3 gives a scale criterion: there is a universal \(\varepsilon_0>0\) such that if, at some block scale \(\ell\), one can choose an \(\varepsilon_0\)-good block event satisfying their coarse constraint conditions, then the infinite-volume generator has
\[
\operatorname{gap}(L)>0.
\]
Corollary 3.5 makes the bootstrap interface explicit. If
\[
\mu(\Lambda_0\text{ is internally spanned})\longrightarrow1
\qquad (\ell\to\infty),
\]
and the corresponding finite-block chain with the stated empty boundary condition is ergodic, then the KCSM has positive spectral gap. Thus a deterministic high-probability emptying statement can be converted into exponential \(L^2(\mu)\) relaxation of the stochastic dynamics.

## Mechanism

Bootstrap percolation supplies more than a static threshold. Internal spanning produces an actual legal path along which vacancies can be propagated through a block. On a sufficiently large scale, the event that a block possesses such a path has probability close to one under the product equilibrium law.

The proof does not compare the original process directly with the monotone bootstrap automaton. Instead it promotes internally spanned blocks to **good states of a coarse constrained dynamics**. Theorem 3.3 proves a Poincare inequality for this auxiliary scale-dependent constrained process by a multiscale argument. The legal emptying paths then allow its coarse moves to be implemented by legal moves of the microscopic KCSM, transferring the variance estimate back to the original Dirichlet form.

The reusable pattern is therefore
\[
\text{bootstrap closure with high probability}
\Rightarrow
\text{coarse mobile block}
\Rightarrow
\text{legal microscopic implementation}
\Rightarrow
\text{Poincare inequality}.
\]
This separates the deterministic geometry from the stochastic coercivity step.

## Representative IPS use

For FA-1f, Theorem 6.3 observes that a large block is internally spanned unless it is completely occupied, so Corollary 3.5 gives a positive spectral gap for every vacancy density \(q>0\). Theorem 6.7 applies the same transfer to FA-\(j\)f and Modified Basic models in their ergodic regime, using bootstrap-percolation results to verify that internal spanning tends to probability one.

The point of the method is not the exact small-\(q\) asymptotics of those gaps. It is the general bridge by which a deterministic bootstrap result certifies stochastic relaxation.

## Limitations

Internal spanning must be compatible with **legal KCSM moves**, and the finite-block dynamics under the chosen boundary condition must itself be ergodic. Merely knowing that the bootstrap critical density is below the working density is not automatically enough unless it yields the high-probability good-block condition required by Theorem 3.3.

The conclusion is a positive spectral gap relative to the reversible product law, hence exponential \(L^2\) relaxation in that ergodic component. It is not uniqueness of all invariant measures: KCSM can retain blocked configurations supporting other stationary laws. Quantitative gap asymptotics require substantially sharper information than the qualitative internal-spanning limit.

This method overlaps with block bisection at the coercivity stage, but the distinctive interface here is the **bootstrap/legal-path certificate** furnishing the good coarse blocks; the live generic block-dynamics page starts after such a good-block event has already been supplied.

## Sources

- Cancrini, Martinelli, Roberto, Toninelli, *Kinetically constrained spin models*, Definition 3.4, Theorem 3.3 and Corollary 3.5; FA applications in Theorems 6.3 and 6.7, https://doi.org/10.1007/s00440-007-0072-3.
- Author preprint: https://arxiv.org/abs/math/0610106.
