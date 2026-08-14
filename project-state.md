# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

The present PDE manuscript contains a substantial candidate body of mathematics, but the new programme-level success gate has not been met. In particular, the project has not yet identified and verified a respected explicitly stated open problem from at least two published sources that the final results solve.

## Active programme

Search broadly for a natural PDE/probability application of **local signed cancellation / cancellation before absolute values**. The motivating mechanism is to delay the first absolute value until a useful structural or conditional averaging has removed signed variation. IPS patches motivated this idea, but the final application need not resemble spin-system patches.

The current quadratic-Hessian programme under `pde-paper/` is a **candidate method-development body**, not the privileged final problem. It may become the main application, supporting machinery for another problem, a shorter auxiliary paper, or be abandoned if a better nail is found.

The search is deliberately broad: branching and Feynman--Kac representations, derivative/Malliavin weights, parametrix or cascade expansions, BSDE-type representations, elliptic or parabolic problems, and other stochastic PDE representations are in scope when the cancellation mechanism is mathematically natural and the application is not contrived or too obscure to matter.

## Reserve programme

**None.**

A reserve programme should be created only after an independent Director identifies a second candidate worth preserving. Maintain one active programme and at most one reserve.

## Verified results

**None have yet been promoted to `verified` under the new autonomous verification protocol.**

The current manuscript states complete proofs of several results and has undergone earlier informal/referee-style audits, but those audits do not substitute for the new requirement of two independent hostile correctness audits plus a separate novelty/open-problem audit. Existing manuscript and wiki claims are therefore evidence to recheck, not authoritative premises.

## Claims under investigation

The current `pde-paper/` manuscript, **Cancellation before absolute values in branching representations with derivative weights**, contains the following principal claimed components that may be reused if they survive fresh audit:

- repeated-Hessian nonintegrability and a Gevrey-type necessity result for a coding-tree architecture;
- an example where two exact branching architectures for the same PDE have different moment behavior;
- canonical finite-tree raw signed measures for the quadratic-Hessian Duhamel expansion;
- exact finite-depth patch regrouping;
- a fully interior-averaged, Catalan-summable `L^1` skeleton representation in a small-data regime;
- a fixed smooth datum for which the canonical raw-faithful total variation has a divergent right-comb subseries;
- residual signed variation as the exact first-moment invariant for skeleton-preserving coarsenings at a fixed target;
- an explicit derivative-cluster estimate giving a finite absolute-time patch constant without PDE smallness;
- a target-uniform time-spine `L^1` representation under an additional smallness condition.

Do not use this list as proof of correctness or novelty. Read and audit the actual source when one of these claims becomes load-bearing.

## Unresolved objections

1. **Programme-level importance is unresolved.** The current manuscript has not been tied to a documented respected open problem meeting the final success criterion.
2. **Novelty review is incomplete.** The present bibliography is too narrow for a final priority claim. Adjacent work on branching-PDE integrability, pruning, derivative weights, and alternative stochastic representations must be searched systematically.
3. **Current central proofs require fresh hostile audits.** Earlier work identified the right-comb total-variation argument and external-theorem interfaces as especially delicate.
4. **The PDE wiki is not yet readable from the user's baseline.** Its advanced research overview begins after substantial PDE vocabulary has already been assumed.

## Literature anchors

These are starting points only; they do **not** establish the final open-problem requirement.

- J. Y. Nguwi, G. Penent, N. Privault, *A Fully Nonlinear Feynman--Kac Formula with Derivatives of Arbitrary Orders*, Journal of Evolution Equations 23 (2023). Relevant to coding-tree representations and derivative weights.
- P. Henry-Labordère, N. Oudjane, X. Tan, N. Touzi, X. Warin, *Branching Diffusion Representation of Semilinear PDEs and Monte Carlo Approximation*, Ann. Inst. H. Poincaré Probab. Statist. 55 (2019). Relevant to marked branching representations and automatic-differentiation weights.
- X. Warin, *Variations on Branching Methods for Non Linear PDEs* (2017 preprint). Relevant to antithetic/ghost branching constructions.
- Standard deterministic background already cited in the manuscript includes Evans, Friedman, and Lieberman.

The first SEARCH cycle must expand this substantially, including later work and alternate terminology. Every candidate open problem must be backed by exact published source locations and checked against subsequent literature.

## Wiki frontier

The pedagogical entry point is `docs/pde-reading-path.md`.

Target reader: a mathematically mature probability researcher with graduate probability and analysis but no dependable PDE vocabulary. The reader may not yet know what distinguishes elliptic, parabolic, and hyperbolic equations, the main solution notions, Schauder estimates, or Malliavin calculus.

The first frontier is therefore **basic PDE classification and problem/solution vocabulary**, before the current pages on mild formulations, Feynman--Kac, branching, Hölder spaces, or Malliavin/Bismut weights.

Build the wiki by the reader-failure algorithm in `CHATGPT.md`: stop at the first unexplained concept, repair that prerequisite, and repeat. Link definitions instead of duplicating them.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Naive patchwise Gaussian-bridge coarsening does not remove the known right-comb obstruction because the obstruction trees have one-edge maximal-left patches, where that bridge coarsening is effectively identity.
- Repeated simulation/evidence refinement without a new analytic question is not a research route; computation is for falsification and structural discovery, then analysis must resume.

## Next cycle

Run a **SEARCH** cycle with up to four fresh read-only ChatGPT workers, using the standard worker header in `CLAUDE.md`:

1. **Open-problem scout:** find respected explicitly stated open problems where local signed cancellation could plausibly matter; require exact published source locations and check later literature for solutions.
2. **Method scout:** find natural settings where a smallest explicit joint-cancellation calculation beats the naive absolute-value estimate.
3. **Novelty killer:** attack novelty of the current quadratic-Hessian programme and leading candidate applications through adjacent and later literature.
4. **PDE-wiki reader:** follow `docs/pde-reading-path.md` from the target-reader baseline and report the first missing prerequisite.

After collecting concise dispatches verbatim, launch a fresh **Director** ChatGPT to choose the next stage/programme. Then launch a single **Integrator** ChatGPT to make any justified repository changes and rewrite this file in place. Claude must not make the mathematical choice itself.
