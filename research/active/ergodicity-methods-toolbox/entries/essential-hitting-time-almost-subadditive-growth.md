---
method_id: essential-hitting-time-almost-subadditive-growth
title: Essential hitting times and almost-subadditive regeneration
category: lyapunov-regeneration
targets:
  - convergence
model_scope: Supercritical contact processes in stationary ergodic random environments, conditioned on survival
source_status: primary-checked
primary_source: Olivier Garet and Régine Marchand, Asymptotic shape for the contact process in random environment, Annals of Applied Probability 22 (2012), 1362-1410
primary_pinpoint: Section 2.6; Theorems 1-3; Theorem 22; Theorems 23-24; Corollary 16 and Lemma 19
primary_url: https://doi.org/10.1214/11-AAP796
application_source: same as primary source
application_pinpoint: Theorem 3 and Section 5
application_url: https://arxiv.org/abs/0910.1230
wiki_candidate: yes
---

# Essential hitting times and almost-subadditive regeneration

## Criterion

For a supercritical contact process in a stationary random environment, ordinary first-passage times are poorly adapted to the law conditioned on survival: after conditioning, the Markov and independence properties normally used in subadditive growth arguments are lost. Garet and Marchand replace the ordinary hitting time `t(x)` by the **essential hitting time** `sigma(x)`. It is obtained by repeatedly waiting for infections of `x` and checking the lifetime of the descendants born from that infection, stopping when an infection at `x` has infinite progeny. Section 2.6 explicitly interprets `sigma(x)` as a regeneration time.

The resulting space-time shift by `x` and time `sigma(x)` preserves the survival-conditioned law; Theorem 1 gives ergodicity for the relevant shifts. Exact subadditivity still fails, but Theorem 2 proves a uniform stretched-exponential tail for the defect

` sigma(x+y) - sigma(x) - sigma(y) after the regenerated shift. `

Corollary 16 gives uniform moments of its positive part. The paper proves the almost-subadditive ergodic Theorems 23-24 precisely to handle such defects. Applying them yields Theorem 22: `sigma(nx)/n` converges almost surely and in every finite `L^p` to a deterministic time constant. Theorem 3 upgrades directional convergence to an asymptotic shape theorem for the infected and coupled regions.

## Mechanism

The key move is to regenerate **at a successful infection lineage**, not at the first time a site is touched. At time `sigma(x)`, the infection at `x` has descendants forever, so translating space by `x` and time by `sigma(x)` produces a restart compatible with survival. This restores enough stationarity and ergodicity for long-range growth analysis.

The restart is not perfectly subadditive. Reaching `x`, regenerating there, and then regenerating at displacement `y` need not give the first essential hit of `x+y`. Section 4 bounds this failure quantitatively. Theorem 2 shows that the excess has a tail uniform in `x`, `y`, and the allowed environment; Corollary 16 supplies the moments required by the abstract almost-subadditive theorem.

Section 5 then applies Theorems 23-24 to `sigma(nx)`. A separate estimate controls `sigma(x)-t(x)`, so the deterministic asymptotic rate obtained for essential hitting times transfers back to ordinary infection growth. Uniform-in-direction arguments convert the directional limits into the compact asymptotic shape of Theorem 3.

## Representative IPS use

The primary application is the contact process on `Z^d` with stationary ergodic random infection rates, uniformly bounded in a supercritical interval. Conditioned on survival, Theorem 3 gives an almost-sure deterministic asymptotic shape not only for sites already infected but also for a coupled zone where the process from one infection has agreed with the process from full occupancy.

This is a long-time growth method rather than convergence to an invariant law. Its relevance to the ergodicity toolbox is the reusable survival-conditioned regeneration/subadditivity interface.

## Limitations

The construction needs a supercritical regime with uniform quantitative controls on extinction, growth, and reinfection times, plus ergodicity of the environment under suitable spatial shifts. The regenerated times are only almost subadditive, so the error estimates are load-bearing; a regeneration definition alone does not give a shape theorem.

This method is distinct from the live survival-conditioned renewal page for an asymmetric multitype contact process. There, fresh ancestor points with exponential tails are combined with steering to prove type takeover and complete convergence. Here the regeneration is designed to restore stationarity for passage times, and the decisive second step is an almost-subadditive ergodic theorem yielding deterministic linear growth and a shape.

## Sources

Primary source: Olivier Garet and Régine Marchand, *Asymptotic shape for the contact process in random environment*, Annals of Applied Probability 22 (2012), 1362-1410, DOI 10.1214/11-AAP796. Essential hitting times are defined in Section 2.6; Theorem 1 proves ergodicity of the regenerated shifts; Theorem 2 and Corollary 16 control the subadditivity defect; Theorems 23-24 are the almost-subadditive ergodic results; Theorem 22 gives directional convergence; and Theorem 3 is the asymptotic shape theorem. Stable preprint: https://arxiv.org/abs/0910.1230.