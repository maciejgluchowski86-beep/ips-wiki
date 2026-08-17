---
method_id: parity-duality-branching-annihilating
title: Parity duality with branching-annihilating particles
category: graphical-duality
targets:
  - uniqueness
  - convergence
model_scope: Cancellative voter-type spin systems whose finite-particle dual is a parity-preserving branching-annihilating process
source_status: primary-checked
primary_source: Anja Sturm and Jan M. Swart, "Voter models with heterozygosity selection," Annals of Applied Probability 18 (2008), 59--99
primary_pinpoint: Section 2.1; equations (1.8) and (2.4)--(2.8); Theorem 3; Theorem 12; Section 3.5
primary_url: https://doi.org/10.1214/07-AAP444
application_source: same as primary source
application_pinpoint: Theorem 3 and Section 3.5
application_url: https://arxiv.org/abs/math/0701555
wiki_candidate: yes
---

# Parity duality with branching-annihilating particles

## Criterion

For a cancellative spin system \(X\in\{0,1\}^{\mathbb Z^d}\), the natural duality may preserve not occupation itself but **parity**. If \(Y\) is the finite-particle dual, the relation has the form
\[
\mathbb P\bigl(|X_tY_0|\text{ is odd}\bigr)
=
\mathbb P\bigl(|X_0Y_t|\text{ is odd}\bigr).
\]
The dual particles may random-walk, branch, and annihilate on collision, with total particle number conserved modulo two. Memory is therefore not removed by extinction alone: on the survival event the dual may grow without bound while parity tests against the primal become asymptotically unbiased.

Sturm--Swart's Theorem 3 treats the neutral Neuhauser--Pacala, affine voter and rebellious voter models with their parity-preserving duals. If \(\alpha<1\) and the dual \(Y\) survives, the odd upper invariant law \(\nu_X^{1/2}\) is the unique homogeneous **coexisting** invariant law of \(X\). If additionally \(\alpha>0\) and \(Y\) is not stable, every homogeneous coexisting initial law converges weakly to \(\nu_X^{1/2}\). The symmetric statement classifies homogeneous nonzero invariant laws of \(Y\) under the corresponding hypotheses.

The load-bearing growth input is an extinction-versus-unbounded-growth property for the parity-preserving branching dual. Theorem 12 proves such a statement under the paper's nonstability and local branching assumptions. Together with parity duality, it forces finite parity observables to converge to those of the odd upper invariant law.

## Mechanism

A finite dual configuration tests a cylinder event of the primal through the parity of its overlap. Section 2.2 rewrites convergence of the primal as the requirement that, conditional on dual survival,
\[
\mathbb P\bigl(|X_{t_0}Y_{t-t_0}|\text{ is odd}\mid Y\text{ survives}\bigr)
\longrightarrow \tfrac12.
\]
Large dual size by itself is not always enough; the paper develops a local block norm that counts many spatially separated opportunities to change overlap parity. When the branching-annihilating dual survives and is not trapped in a tight finite-particle regime, extinction-versus-unbounded-growth drives this norm large. Local nonsingularity of the primal then makes the parity of the overlap asymptotically fair.

This identifies all parity expectations of any subsequential homogeneous coexisting invariant law. Because those parity functions determine the relevant law, the limit must equal \(\nu_X^{1/2}\).

The mechanism is distinct from the live **finite-dual extinction** page: here the useful branch of the dual explicitly **survives and grows**. It is also distinct from voter coalescing-walk duality: voter lineages only merge, whereas this dual creates offspring and annihilates particles while preserving parity.

## Representative IPS use

For the one-dimensional rebellious voter model, the dual is the asymmetric double branching annihilating random walk (ADBARW). Particles random-walk, branch into two additional particles, and annihilate pairwise on collision. Theorem 3 uses the survival/nonstability properties of this reaction system to classify the unique homogeneous coexisting invariant law of the spin model and to prove convergence from homogeneous coexisting starts. The same paper later proves the needed survival regime for small \(\alpha\) by a separate supercritical block construction; that percolation step is a different proof interface.

## Limitations

Parity duality is special to cancellative systems and does not provide ordinary moment duality for arbitrary spin dynamics. The invariant-law conclusion is intentionally qualified: the models retain absorbing constant states, so Theorem 3 does not assert a globally unique invariant measure. It classifies homogeneous coexisting laws, and convergence requires additional survival, nonstability and local nonsingularity hypotheses. Proving extinction versus unbounded growth for a parity-preserving branching process can itself be difficult, and the paper warns that plain particle-number growth is insufficient in some parity arguments; spatially distributed branching opportunities must be controlled.

## Sources

Primary checked source: Sturm and Swart, *Voter models with heterozygosity selection*, Ann. Appl. Probab. 18 (2008), 59--99. Section 2.1 gives the interface and parity-duality framework; equations (2.4)--(2.8) show how survival/growth enters invariant-law identification; Theorem 12 supplies extinction versus unbounded growth; Theorem 3 and its proof in Section 3.5 give the uniqueness and convergence conclusions.