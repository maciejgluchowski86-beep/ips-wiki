---
title: Parity duality with branching-annihilating particles
status: literature
audit: current
tags:
  - duality
  - branching-annihilating particles
  - voter models
---

# Parity duality with branching-annihilating particles

## Criterion

For a cancellative spin system \(X\in\{0,1\}^{\mathbb Z^d}\), the natural duality may preserve not occupation itself but parity. If \(Y\) is the finite-particle dual, the relation has the form
\[
\mathbb P\bigl(|X_tY_0|\text{ is odd}\bigr)
=
\mathbb P\bigl(|X_0Y_t|\text{ is odd}\bigr).
\]
The dual particles may random-walk, branch, and annihilate on collision, with total particle number conserved modulo two. Memory is therefore not removed by extinction alone: on the survival event the dual may grow without bound while parity tests against the primal become asymptotically unbiased.

Sturm--Swart's Theorem 3 treats several voter-type models with parity-preserving duals. If \(\alpha<1\) and the dual survives, the odd upper invariant law \(\nu_X^{1/2}\) is the unique homogeneous coexisting invariant law of \(X\). If additionally \(\alpha>0\) and \(Y\) is not stable, every homogeneous coexisting initial law converges weakly to \(\nu_X^{1/2}\). Theorem 12 supplies an extinction-versus-unbounded-growth statement for the parity-preserving branching dual under the paper's hypotheses.

## Mechanism

A finite dual configuration tests a cylinder event of the primal through the parity of its overlap. Large dual size alone is not always enough. The paper develops a local block norm that counts many spatially separated opportunities to change overlap parity. When the branching-annihilating dual survives and is not trapped in a tight finite-particle regime, extinction versus unbounded growth drives this norm large. Local nonsingularity of the primal then makes overlap parity asymptotically fair.

This identifies the parity expectations of any subsequential homogeneous coexisting invariant law, and those parity functions determine the relevant law. The mechanism is distinct from [finite-dual extinction](duality-extinction-finite-ancestor-process.md), because here the useful branch of the dual survives and grows, and from [voter coalescing-walk duality](voter-coalescing-random-walk-duality.md), because the dual branches and annihilates rather than merely coalescing.

## Representative IPS use

For the one-dimensional rebellious voter model, the dual is the asymmetric double branching annihilating random walk. Particles random-walk, branch into two additional particles, and annihilate pairwise on collision. Theorem 3 uses survival/nonstability of this reaction system to classify the unique homogeneous coexisting invariant law and to prove convergence from homogeneous coexisting starts. A separate [supercritical block construction](supercritical-block-construction-complete-convergence.md) in the same paper supplies a survival regime; that is a distinct proof interface.

## Limitations

Parity duality is special to cancellative systems. The invariant-law conclusion is intentionally qualified: the models retain absorbing constant states, so Theorem 3 does not assert a globally unique invariant measure. It classifies homogeneous coexisting laws, and convergence requires additional survival, nonstability and local nonsingularity hypotheses. Proving extinction versus unbounded growth for a parity-preserving branching process can itself be difficult.

## Sources

- Sturm and Swart, *Voter models with heterozygosity selection*, Ann. Appl. Probab. 18 (2008), 59--99, Section 2.1, equations (1.8) and (2.4)--(2.8), Theorem 3, Theorem 12 and Section 3.5, https://doi.org/10.1214/07-AAP444.
- Open preprint: https://arxiv.org/abs/math/0701555.
