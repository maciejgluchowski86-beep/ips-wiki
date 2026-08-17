---
title: Aldous interchange-process spectral-gap reduction
status: literature
audit: current
tags:
  - exclusion process
  - spectral gap
  - interchange process
---

# Aldous interchange-process spectral-gap reduction

## Criterion

Let \(G=(V,E)\) be a finite connected weighted graph with symmetric edge conductances \(c_{xy}\ge0\). The continuous-time random walk jumps from \(x\) to \(y\) at rate \(c_{xy}\). The interchange process places one distinctly labeled particle at every vertex and transposes the labels at \(x,y\) at rate \(c_{xy}\). Caputo--Liggett--Richthammer Theorem 1.1 proves the exact identity

$$
\boxed{\lambda_1^{\mathrm{IP}}(G)=\lambda_1^{\mathrm{RW}}(G)}.
$$

This is stronger than transferring a comparison constant: the many-particle interchange relaxation time is exactly the one-particle random-walk relaxation time for every finite connected weighted graph.

A principal consequence is symmetric exclusion. For every \(k\in\{1,\ldots,|V|-1\}\), Section 4.1.1 gives

$$
\boxed{\lambda_1^{\mathrm{EP},k}(G)=\lambda_1^{\mathrm{RW}}(G)}.
\tag{A}
$$

Thus estimating the exclusion spectral gap reduces completely to the graph random-walk gap.

## Mechanism

One inequality is immediate from projection. Random walk is obtained from interchange by following a single labeled particle, so the random-walk spectrum is contained in the interchange spectrum and

$$
\lambda_1^{\mathrm{IP}}\le \lambda_1^{\mathrm{RW}}.
$$

The hard direction proves that no slower mode hides in the huge permutation state space. Caputo--Liggett--Richthammer use a recursive removal of vertices combined with an electrical-network reduction of conductances. The decisive ``octopus'' inequality controls the Dirichlet-form change caused by this reduction and permits induction on the number of vertices. The result forces every nonconstant interchange mode to relax at least at the random-walk rate.

For exclusion there are two complementary inclusions. The \(k\)-particle exclusion chain is itself a quotient of interchange, hence its spectrum is contained in the interchange spectrum. Conversely, if \(f\) is a random-walk eigenfunction, then

$$
g(\zeta)=\sum_{x\in\zeta} f(x)
$$

is an exclusion eigenfunction with the same eigenvalue. Theorem 1.1 therefore sandwiches the exclusion gap between equal random-walk and interchange gaps, giving `(A)`.

## Representative IPS use

Symmetric simple exclusion on a finite graph is a conservative interacting particle system with hard-core interaction. Equation (4.1) says its relaxation scale is independent of particle number: once the conductance geometry of the underlying graph is understood, the spectral gap follows with no additional many-particle loss.

For example, on a box or torus the random-walk gap has diffusive order \(L^{-2}\); the theorem transfers exactly that order to every nontrivial exclusion sector. On irregular weighted graphs, effective resistance, Cheeger inequalities, eigenvalue estimates, or explicit graph spectral calculations can be applied at the one-particle level and inherited unchanged by exclusion.

## Limitations

The theorem is specific to the interchange/exclusion algebra with **symmetric** edge rates and a uniform reversible law on each finite sector. It does not say that arbitrary conservative IPS have their one-particle gap, nor does it extend automatically to asymmetric exclusion, zero-range dynamics, kinetic constraints, or interacting Gibbs weights.

The equality concerns the first nonzero eigenvalue only. Logarithmic Sobolev and modified logarithmic Sobolev constants can depend strongly on particle number and state-space size even when the spectral gap does not. Consequently `(A)` gives sharp \(L^2\) relaxation but is not by itself a sharp total-variation mixing theorem from worst initial states.

This method is distinct from [canonical-path comparison](dirichlet-form-canonical-path-comparison.md). Canonical paths bound one Dirichlet form by another with congestion loss. Aldous' theorem identifies an exact hidden spectral reduction: the many-particle gap itself is the graph random-walk gap.

## Sources

- Caputo, Liggett, Richthammer, *Proof of Aldous' spectral gap conjecture*, Theorem 1.1 and Section 4.1.1, equation (4.1), https://doi.org/10.1090/S0894-0347-10-00659-4.
- Open primary version with identical theorem numbering: https://arxiv.org/abs/0906.1238.
