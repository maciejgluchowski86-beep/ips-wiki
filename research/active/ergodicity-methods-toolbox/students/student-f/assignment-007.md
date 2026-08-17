# Student F Assignment 007: source-led analytic and nonlocal-dynamics breadth

Read before working: root `project-state.md`, `README.md`, `CHATGPT.md`; `research/active/ergodicity-methods-toolbox/state.md`, `proof-spine.md`, Meeting 015, `entry-template.md`, your `006-handoff.md`, and the live toolbox hub `docs/ergodicity-methods.md`.

## Objective

Wave seven is narrower and source-led. The toolbox is already broad enough that generic keyword searches have diminishing value. Inspect the named primary source families below and create an entry only when the proof interface survives as genuinely distinct from the 67 live methods.

Do **not** force four entries. A source may support zero, one, or more pages depending on whether its load-bearing object is already represented.

## Targets

1. **Asymptotic strong Feller plus weak irreducibility as a uniqueness criterion.** Start with Hairer--Mattingly, *Ergodicity of the 2D Navier--Stokes equations with degenerate stochastic forcing*, Ann. Math. 164 (2006), 993--1032, DOI `10.4007/annals.2006.164.993`. Isolate the abstract asymptotic-strong-Feller/accessible-point criterion and its use for degenerate stochastic Navier--Stokes. It must be distinguished explicitly from the live Hairer-2002 asymptotic **coupling** page and from the live classical-Harris small-set page.

2. **Hörmander/Malliavin noise propagation for semilinear SPDE unique ergodicity.** Start with Hairer--Mattingly, *A Theory of Hypoellipticity and Unique Ergodicity for Semilinear Stochastic PDEs*, Electron. J. Probab. 16 (2011), 658--738, DOI `10.1214/EJP.v16-875`. The possible interface is bracket generation -> quantitative Malliavin covariance control -> smoothing/asymptotic strong Feller. Keep this separate from target 1 only if the primary theorem chain makes the Malliavin/Hörmander verification architecture reusable in its own right; otherwise record a merge/negative taxonomy result.

3. **Swendsen--Wang / FK cluster-dynamics comparison.** Start with Mario Ullrich, *Comparison of Swendsen--Wang and heat-bath dynamics*, Random Structures & Algorithms 42 (2013), 520--535, DOI `10.1002/rsa.20431`, and inspect the companion random-cluster comparison if useful. The target is a nonlocal cluster-update proof interface in which the Edwards--Sokal/FK joint representation or an operator comparison transfers a single-spin/single-bond gap to Swendsen--Wang dynamics. Do not reduce it to the live generic canonical-path page merely because a comparison inequality appears.

4. **Entropic Ricci curvature for interacting spin/particle chains.** Start with Erbar--Henderson--Menz--Tetali, *Ricci curvature bounds for weakly interacting Markov chains*, Electron. J. Probab. 22 (2017), paper 40/49 as given by the source, DOI `10.1214/17-EJP49`. Inspect the perturbative curvature criterion and its Ising/Curie--Weiss/hard-core applications. Create a page only if the entropy-geodesic/curvature object is genuinely distinct from the live discrete Bochner--Bakry--Emery entropy method and from Wasserstein coupling contraction.

## Closed searches

Do not reopen the generic full-Cheeger positive-spin search or the generic spectral-profile/evolving-set IPS search. Each has now failed two bounded waves. Likewise do not reopen artificial Nummelin, generic nonreversible sector/hypocoercivity, or a generic fully-unconstrained-refresh KCSM search absent a named new source.

## Entry standard

For every surviving target, create one staged entry under `research/active/ergodicity-methods-toolbox/entries/` using the current template. Check the actual primary theorem/proposition/lemma and exact hypotheses. State the criterion, mechanism, interacting-process application, and limitations self-containedly. A shared source or theorem chain does not justify two pages unless the proof interfaces are genuinely separable.

## Durability

Commit each finished entry immediately as its own substantive commit. Do not edit `docs/` or `mkdocs.yml`.

At completion, commit `students/student-f/007-handoff.md` listing entry commits, source pinpoints, merge/rejection decisions, and any newly exposed source-led gaps. Mechanical validation remains structural only.
