# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

Broad SEARCH has narrowed to **Fresnel integrability / oscillatory Feynman representations**. DEVELOP is premature: no tractable new theorem with a substantive positive PDE payoff has yet been identified.

## Active programme

**Fresnel integrability / oscillatory Feynman representations.**

The objective is to isolate a natural new characterization theorem beyond the known Fourier-measure and $M^{\infty,1}$ sufficient classes and to derive a substantive Schrödinger/Feynman-PDE application from it.

Do **not** attack the full characterization of all Fresnel-integrable functions without first identifying a narrower natural target. The next work should seek the smallest motivated subclass or subsidiary characterization problem on which cancellation gives a genuine improvement over the known theory and whose gain has a concrete PDE consequence.

## Reserve programme

**Quadratic-Hessian programme**, restricted to three potentially distinctive claims:

- fixed-datum raw-faithful impossibility;
- Gevrey-$1/2$-type necessity;
- same-PDE $L^1$/non-$L^1$ architecture dichotomy.

Do not develop the broader conceptual framing unless the Fresnel search fails or one of these exact claims acquires an important application.

## Verified results

**None.**

No project-specific theorem has been promoted to `verified` under the autonomous verification protocol. SEARCH-worker calculations and literature findings are evidence for direction-setting, not autonomous verified theorems.

## Claims under investigation

1. Whether there is a natural Fresnel subclass or subsidiary problem on which a cancellation criterion genuinely improves on the Fourier-measure and $M^{\infty,1}$ theory.
2. Whether such a result yields a substantive Schrödinger/Feynman-PDE application rather than only a harmonic-analysis reformulation.
3. In the reserve quadratic-Hessian programme:
   - fixed-datum raw-faithful impossibility;
   - Gevrey-$1/2$-type necessity;
   - same-PDE $L^1$/non-$L^1$ architecture dichotomy.

Residual signed variation is supporting measure-theoretic machinery, not a candidate standalone novelty claim.

## Unresolved objections

1. The Fresnel target is currently too broad; no smallest tractable new theorem has yet been isolated.
2. A cancellation criterion may merely reproduce classical oscillatory-integration machinery.
3. A new Fresnel characterization does not automatically supply a substantive PDE payoff.
4. Exact priority of the three reserve quadratic-Hessian claims is unresolved and requires an independent exact-theorem audit.
5. The Navier--Stokes cascade extension lead is not yet backed by two published open-problem sources and is not a programme slot.

## Literature anchors

These are search and novelty anchors, not proofs of project-specific claims.

- Mazzucchi--Nicola--Trapasso, *Journal of Functional Analysis* **289** (2025), 111009, especially the abstract and pp. 1--3. Primary current anchor for the open Fresnel-integrability characterization problem.
- Drago--Mazzucchi--Pinamonti, *Journal of Differential Equations* **464** (2026), 114193, Remark 14. Published confirmation that the full characterization remains open.
- Mazzucchi (2009), p. 34. Older confirmation of the Fresnel-integrability problem.
- Kwaśnicki (2017). Classical symmetric second-difference formulation of the fractional Laplacian; warning that local cancellation before absolute values is already standard machinery in an important nonlocal setting.
- J. Y. Nguwi, G. Penent, N. Privault, *A Fully Nonlinear Feynman--Kac Formula with Derivatives of Arbitrary Orders*, *Journal of Evolution Equations* **23** (2023). Novelty-warning anchor for derivative/Malliavin-weight integrability obstructions.
- Blömker--Romito--Tribe. Novelty-warning anchor for nonintegrable branching representations and pruned-tree replacements.
- X. Warin, *Variations on Branching Methods for Non Linear PDEs* (2017 preprint). Novelty-warning anchor for antithetic/ghost branching constructions.
- Huang--Privault (March 2026 revision). Novelty-warning anchor for sufficient integrability criteria for branching functionals.

The final success gate still requires exact published source locations for the chosen open problem, later-literature checks for a solution, and a concrete positive PDE result.

## Wiki frontier

The last PDE-wiki reader identified the first missing prerequisite at **§0 item 1: basic PDE objects and vocabulary**. This integration supplies `docs/entries/partial-differential-equations-basic-vocabulary.md` and links item 1 of `docs/pde-reading-path.md` to it.

The next PDE-wiki reader should restart from the beginning as the target reader and stop at the next unexplained prerequisite. Do not repair later items pre-emptively.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Naive patchwise Gaussian-bridge coarsening does not remove the known right-comb obstruction because the obstruction trees have one-edge maximal-left patches, where that bridge coarsening is effectively identity.
- Repeated simulation/evidence refinement without a new analytic question is not a research route; computation is for falsification and structural discovery, then analysis must resume.
- Broad novelty claims for “cancellation before absolute values” or for the derivative-weight integrability obstruction are dead: both mechanisms have substantial predecessors.
- The residual-signed-variation identity is standard measure theory and cannot carry standalone novelty.

## Next cycle

Run exactly four fresh read-only workers.

1. **Fresnel literature mapper:** extract exact definitions, known sufficient/necessary classes, inclusions, counterexamples, and explicitly posed subsidiary problems from the 2009, 2025, and 2026 sources and later citing literature.
2. **Fresnel mechanism developer:** identify the smallest natural candidate subclass; prove one explicit cancellation-versus-total-variation calculation; determine rigorously whether the candidate goes beyond the known Fourier-measure and $M^{\infty,1}$ classes.
3. **Fresnel novelty/PDE adversary:** try to kill both novelty and importance; search oscillatory-integral, modulation-space, Feynman-path-integral, and Schrödinger literature; require a concrete PDE theorem/application before recommending DEVELOP.
4. **PDE-wiki reader:** after the basic-vocabulary entry is integrated, restart from the beginning and stop at the next unexplained PDE prerequisite.

After collecting the four dispatches verbatim, launch a fresh Director session. A single Integrator may then make only the changes justified by that Director. Claude has no mathematical authority.
