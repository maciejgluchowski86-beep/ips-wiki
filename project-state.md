# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

Broad Fresnel search has produced a one-dimensional finite-total-variation cancellation criterion, but no new PDE theorem and no result solving the documented characterization problem. Run one focused viability cycle before either DEVELOP or termination.

## Active programme

**Fresnel integrability / oscillatory Feynman representations.**

The target is an explicit pair $(X,P)$ with all of the following properties:

- $X\subset \mathrm{Fr}$;
- $X$ is genuinely outside $M^{\infty,1}$ and the relevant classical symbol criteria;
- the extra amplitudes yield a new substantive PDE/Feynman result $P$; and
- $P$ solves an explicitly stated open problem supported by two published sources.

Strict enlargement of $M^{\infty,1}$ alone is insufficient.

## Reserve programme

**Quadratic-Hessian programme**, restricted to three potentially distinctive claims:

- fixed-datum raw-faithful impossibility;
- Gevrey-$1/2$-type necessity;
- same-PDE $L^1$/non-$L^1$ architecture dichotomy.

Do not develop the broader conceptual framing unless the Fresnel search fails or one of these exact claims acquires an important application. Do not develop this reserve during the present cycle.

## Verified results

**None.**

Do not promote the finite-total-variation theorem from the SEARCH dispatch. No project-specific theorem has completed the autonomous verification protocol.

## Claims under investigation

1. Candidate one-dimensional theorem for
   $$
   V(\mathbb R)=\{f:\operatorname{Var}_{\mathbb R} f<\infty\},
   \qquad
   V(\mathbb R)\subset \mathrm{Fr}(\mathbb R).
   $$
   Explicitly avoid the notation $BV(\mathbb R)$ until conventions are fixed.
2. Candidate incomparability of $V(\mathbb R)$ and $M^{\infty,1}(\mathbb R)$.
3. Whether a multidimensional cancellation class produces a genuinely new PDE/path-integral theorem.
4. Whether that theorem addresses an explicitly posed open problem satisfying the final literature gate.

## Unresolved objections

1. The finite-variation argument may be classical Dirichlet/nonstationary-phase machinery under another name.
2. The notation $BV(\mathbb R)$ is ambiguous for the intended finite-total-variation amplitude class.
3. $M^{\infty,1}\subsetneq \mathrm{Fr}$ already follows from $L^1\subset \mathrm{Fr}$, so strict inclusion alone has no novelty force.
4. No positive PDE consequence has been obtained from the new class.
5. No narrower theorem currently solves the published full-characterization problem.
6. The older nested-projector and newer arbitrary-projector infinite-dimensional definitions have not been proved equivalent.
7. Projector independence remains an additional infinite-dimensional obstruction.

## Literature anchors

These are search and novelty anchors, not proofs of project-specific claims.

- Mazzucchi (2009), especially p. 34. Older confirmation of the finite-dimensional Fresnel-integrability characterization problem.
- Mazzucchi--Nicola--Trapasso, *Journal of Functional Analysis* **289** (2025), 111009, especially the abstract and pp. 1--3. Primary current anchor for the Fresnel-integrability characterization problem and the $M^{\infty,1}$ sufficient class.
- Nicola--Trapasso, *Communications in Mathematical Physics* **376** (2020), Theorem 1.3. Principal warning that $M^{\infty,1}$ already yields Feynman--Trotter kernel convergence.
- Drago--Mazzucchi--Pinamonti, *Journal of Differential Equations* **464** (2026), 114193, Definition 13 and Remark 14, together with the magnetic projection-dependence discussion. Anchor for the arbitrary-projector definition, sequence independence requirement, and infinite-dimensional obstruction.

The final success gate still requires exact published source locations for the chosen open problem, a later-literature check for a solution, and a concrete positive PDE result.

## Wiki frontier

§0 item 1 now passes. The first failure is **§0 item 2: initial, terminal, boundary, and initial-boundary value problems**.

This integration creates `docs/entries/initial-terminal-and-boundary-value-problems.md` and links §0 item 2 of `docs/pde-reading-path.md`. The next PDE-wiki reader should restart from §0 item 1 as the target reader and stop at the next unexplained prerequisite.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Naive patchwise Gaussian-bridge coarsening does not remove the known right-comb obstruction because the obstruction trees have one-edge maximal-left patches, where that bridge coarsening is effectively identity.
- Repeated simulation/evidence refinement without a new analytic question is not a research route; computation is for falsification and structural discovery, then analysis must resume.
- Broad novelty claims for “cancellation before absolute values” or for the derivative-weight integrability obstruction are dead: both mechanisms have substantial predecessors.
- The residual-signed-variation identity is standard measure theory and cannot carry standalone novelty.
- Strictly enlarging $M^{\infty,1}$ as a function class is not by itself a research endpoint: $L^1\subset \mathrm{Fr}$ already gives discontinuous examples outside $M^{\infty,1}$.

The finite-total-variation mechanism is not dead yet.

## Next cycle

Run exactly four fresh read-only workers.

1. **Finite-variation proof auditor.** Independently prove or refute $V(\mathbb R)\subset \mathrm{Fr}(\mathbb R)$; give the cutoff-independent tail estimate with constants; audit representatives/Stieltjes integration; prove or refute incomparability with $FM$ and $M^{\infty,1}$; distinguish $V$ from standard $BV=L^1\cap V$.
2. **Classical novelty killer.** Search classical oscillatory-integral, Fourier-analysis, Fresnel-transform, and bounded-variation literature for this exact criterion or stronger versions under alternate terminology. Give exact published source locations and determine whether anything potentially novel remains.
3. **Fresnel PDE-pair developer/adversary.** Choose one concrete multidimensional class $X$, not a menu. Attempt to prove $X\subset \mathrm{Fr}$, produce an explicit element outside $M^{\infty,1}$ and the relevant Hörmander/symbol classes, and derive one concrete new Schrödinger, time-slicing, or projector-independent Feynman theorem. Identify an explicitly posed open problem with two published sources that this theorem would solve. If any component fails, report the earliest fatal obstruction and recommend termination.
4. **PDE-wiki reader.** After the item-2 entry is integrated, restart `docs/pde-reading-path.md` from §0 item 1 as the target reader and stop at the next unexplained prerequisite.

After collecting the four dispatches verbatim, launch a fresh Director session. A single later Integrator may make only the repository changes justified by that Director. Claude has no mathematical authority.
