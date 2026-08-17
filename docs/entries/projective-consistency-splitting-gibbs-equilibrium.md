---
title: Projective consistency of finite-volume Gibbs marginals
status: literature
audit: current
tags:
  - projective limits
  - Gibbs measures
  - loss networks
---

# Projective consistency of finite-volume Gibbs marginals

## Criterion

Let \(V_n\) be the depth-\(n\) ball of a rooted Cayley tree and \(W_n\) its outer sphere. Martin--Rozikov--Suhov define finite-volume hard-core distributions \(\mu^{(n)}\) by equation (2.1), with boundary activities on \(W_n\). The family is called compatible when, for every admissible configuration \(\sigma_{n-1}\) on \(V_{n-1}\),

\[
\sum_{\omega_n\in\Omega_{W_n}}
 \mu^{(n)}(\sigma_{n-1}\vee\omega_n)
 \mathbf 1_{\{\sigma_{n-1}\vee\omega_n\text{ admissible}\}}
 =\mu^{(n-1)}(\sigma_{n-1}).
\tag{2.2}
\]

This is exact projective consistency, not convergence along a subsequence. Once (2.2) holds, the paper invokes the extension theorem to obtain a **unique** probability measure \(\mu\) on the infinite configuration space having the \(\mu^{(n)}\) as its cylinder marginals.

Proposition 1 makes the criterion constructive: compatibility is equivalent to explicit recursive equations (2.3a)--(2.3b) for the two ratios of boundary activities \(z_{1,x},z_{2,x}\). Proposition 2 then identifies every law constructed from such a solution as a Gibbs measure for the hard-core specification.

## Mechanism

The infinite law is built algebraically rather than by a thermodynamic limit. Tree geometry makes the outside of a vertex decompose into independent descendant subtrees once its spin is fixed. Summing the depth-\(n\) distribution over the new boundary layer therefore factorizes into one contribution from each child. Equality with the prescribed depth-\(n-1\) marginal holds exactly when the boundary messages satisfy the recursion of Proposition 1.

The message recursion has two roles. First, it enforces consistency at **every** depth, so there is no need to prove tightness or choose an accumulation point. Second, it reduces the construction of an infinite equilibrium law to a finite-dimensional fixed-point problem for boundary ratios. Having obtained compatible cylinder probabilities, projective extension supplies the infinite measure, and the local Gibbs equations identify its specification.

This differs from finite-volume semigroup exhaustion and from the live \(N/V\) compactness method. Those constructions compare increasingly large dynamics or extract weakly convergent subsequences. Here the finite laws already agree exactly under every restriction map; the infinite object is assembled from those marginals.

## Representative IPS use

The paper's model is a three-state nearest-neighbour hard-core **loss network**. Calls arrive at each site according to Poisson processes and have exponential holding times; acceptance depends on neighbouring states. The authors focus on splitting Gibbs measures because these are reversible equilibrium distributions for that continuous-time interacting process.

For translation-invariant boundary messages, Theorem 1 proves that for every activity \(\lambda>0\) and every tree order \(k\ge1\) there is a unique translation-invariant splitting Gibbs measure. Thus the projective construction produces a distinguished reversible equilibrium law once the boundary recursion has been solved.

The theorem does not say that this law is the unique Gibbs measure of every kind. The same paper studies periodic splitting solutions, so the scope of the uniqueness statement must remain the translation-invariant splitting class.

## Limitations

Exact consistency is a strong structural property. It is especially transparent on trees, where boundary-message recursions close under marginalization; finite-volume invariant or Gibbs laws on a general lattice normally do **not** form an exactly projective family under restriction. In such settings tightness, DLR compactness, or dynamical exhaustion may be necessary instead.

Projective extension proves existence of an infinite law, not convergence of the dynamics to that law. Reversibility is supplied by the model's Gibbs/loss-network structure rather than by the extension theorem itself. Nor does consistency imply global Gibbs uniqueness: different solutions of the boundary recursion can produce distinct splitting phases. The method is therefore a construction interface; classification and ergodicity require additional arguments about the recursion or the dynamics.

## Sources

- Martin, Rozikov, Suhov, *A Three State Hard-Core Model on a Cayley Tree*, Section 2, equations (2.1)--(2.3), Proposition 1 and Proposition 2, https://doi.org/10.2991/jnmp.2005.12.3.7.
- The same paper, Abstract and Section 1 for the loss-network dynamics and reversibility of splitting Gibbs measures; Theorem 1 for uniqueness inside the translation-invariant splitting class, https://doi.org/10.2991/jnmp.2005.12.3.7.
