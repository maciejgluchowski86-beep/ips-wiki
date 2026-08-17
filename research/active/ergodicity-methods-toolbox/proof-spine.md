# Coverage spine

This file replaces a theorem proof spine by a coverage map for the literature-compilation direction. It records method families that should eventually be represented in the toolbox and is revised after each literature batch.

Status labels below mean only toolbox coverage status: **accepted staged** means source-audited by the Professor but not yet promoted to the live wiki; **assigned** means currently delegated; **uncovered** means still to be sourced.

## A. Coupling and influence

- basic/common graphical coupling and coupling inequalities — G wave 1 in flight;
- attractive/monotone coupling and extremal invariant measures — G wave 1 in flight;
- Dobrushin influence matrices and contraction — G wave 1 in flight;
- path coupling and local metric contraction — G wave 1 in flight;
- maximal/local coupling and block coupling — uncovered;
- disagreement percolation / domination by branching or contact processes — G wave 1 in flight;
- coupling from the past / backward ancestor clans — G wave 1 in flight;
- information-percolation and history-cluster methods — uncovered;
- censoring and monotone update comparison — uncovered.

## B. Duality, graphical ancestry, and extinction

- self-/additive duality: extinction of a finite dual implies loss of memory — G wave 1 in flight;
- ancestor-cluster finiteness and clan-of-ancestors constructions — G wave 1 in flight;
- oriented-percolation comparison and subcritical dependency cones — G wave 1 in flight;
- complete-convergence/extremal-law arguments in attractive systems — G wave 1 in flight;
- regeneration/distinguished-particle or distinguished-vacancy constructions — **accepted staged** for East distinguished-zero screening; broader variants uncovered.

## C. Functional inequalities and semigroup decay

- Poincare/spectral-gap inequalities — **accepted staged**;
- logarithmic Sobolev and modified logarithmic Sobolev inequalities — **accepted staged**;
- entropy dissipation / approximate tensorization — represented inside accepted LSI/mLSI entry; standalone block/approximate factorization architecture **assigned F wave 2**;
- Dirichlet-form comparison and comparison of generators — **accepted staged**;
- canonical paths / congestion bounds — **accepted staged** with Dirichlet comparison;
- block dynamics, bisection, multiscale variance decomposition — **accepted staged**;
- Lu--Yau / martingale conditional-variance recursion — **assigned F wave 2**;
- moving-particle / long-jump comparison for conservative IPS — **assigned F wave 2**;
- bounded-perturbation / Holley--Stroock transfer of coercive inequalities — **assigned F wave 2**;
- finite-volume criteria uniform in boundary conditions — **assigned F wave 2**;
- nonreversible hypocoercive/coercive variants with genuine IPS applications — uncovered.

## D. Spatial mixing to dynamical mixing

- Dobrushin uniqueness and elementary influence contraction — G wave 1 in flight;
- Dobrushin-Shlosman spatial mixing to uniform LSI/Glauber relaxation — **accepted staged**;
- strong/weak spatial mixing finite-size criteria — partly represented by Dobrushin-Shlosman; broader finite-size criteria **assigned F wave 2**;
- disagreement percolation as a Gibbs-to-dynamics bridge — G wave 1 in flight / later deduplication needed;
- spectral independence / local-to-global influence bounds for Glauber dynamics — **assigned F wave 2**;
- finite-volume boundary-condition comparison leading to spectral gap or mixing — **assigned F wave 2**.

## E. Recurrence, Lyapunov, and regeneration

- Foster-Lyapunov drift plus minorization/Harris recurrence — uncovered;
- small/petite-set regeneration and Nummelin splitting with IPS-like application — uncovered;
- front/interface Lyapunov functions and extinction of disagreement — uncovered;
- renewal structures and regeneration blocks — uncovered;
- coupling/drift in Wasserstein or weighted metrics — uncovered.

## F. KCSM- and model-specific relaxation mechanisms

- distinguished zero / oriented vacancy methods for East — **accepted staged**;
- constrained Poincare inequalities and legal-path/canonical-path estimates — partly represented by accepted gap/comparison entries; specialized variants uncovered;
- block renormalization and bisection for KCSM — **accepted staged**;
- bootstrap-percolation-assisted positive-gap criteria — represented in accepted Poincare/block entries;
- comparison with unconstrained refresh dynamics — uncovered as a dedicated method;
- model-specific dual, interface, defect-particle, persistence, or front representations implying ergodicity/gap — uncovered beyond East distinguished zero.

## G. Finite-volume to infinite-volume transfer

- uniform finite-volume spectral gap/log-Sobolev estimates plus exhaustion/finite propagation — partly represented in accepted analytic entries; dedicated transfer entry uncovered;
- mixing in boxes with controlled boundary conditions — **assigned F wave 2** in finite-size criterion;
- exhaustion and projective/compactness arguments for invariant laws — uncovered;
- coupling/ancestor estimates uniform in volume — G wave 1 may cover pieces;
- criteria turning local relaxation into uniqueness and convergence — uncovered as a dedicated synthesis.

## H. Accepted first-wave analytic coverage

Meeting 002 source-audited and accepted six staged entries:

1. Poincare inequality and spectral-gap method;
2. logarithmic Sobolev and modified logarithmic Sobolev methods;
3. Dirichlet-form and canonical-path comparison;
4. block dynamics and bisection variance decomposition;
5. Dobrushin--Shlosman spatial mixing to dynamical relaxation;
6. East distinguished-zero screening.

Shared sources are not by themselves duplication. Distinct entries are retained when they expose different proof interfaces: e.g. a functional inequality versus a spatial hypothesis producing it. Cross-link and trim common setup at live-wiki integration.

## I. Coverage discipline

The toolbox is an inventory, not a ranking. Overlap between families is expected, but each live entry should expose a distinct reusable proof interface and identify related methods rather than repeat their derivations. A method that is highly model-specific is retained if it has a rigorous source and a clear reusable mechanism.

Later assignments should preferentially fill uncovered families. Repeatedly adding variants inside already dense Poincare/LSI/block-dynamics territory is lower priority unless the proof mechanism is genuinely different.
