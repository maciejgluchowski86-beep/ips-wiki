# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

## Active programme

**Navier--Stokes stochastic-cascade cancellation search.**

Before any transition to DEVELOP, identify a respected published subsidiary open problem or criterion in the stochastic-cascade or majorizing-kernel literature, document it in at least two published sources with exact locations and a successor check, and show that a precise cancellation gain could plausibly affect that criterion. Do not attack global regularity wholesale without this bridge.

## Reserve programme

**Supercritical dissipative SQG global regularity.**

## Verified results

**None.**

## Claims under investigation

Three PDE problems now have adequate published open-problem documentation for the SEARCH-stage gate:

- three-dimensional incompressible Navier--Stokes global regularity;
- supercritical dissipative SQG global regularity;
- strong-KPP uniqueness on arbitrary domains.

This clears only the open-problem documentation component. It does not establish a project theorem or justify a transition to DEVELOP. Strong-KPP is not an active or reserve programme because no signed-cancellation interface has been identified.

A classical local heat/Hermite cancellation is established as reusable mechanism evidence. For the heat semigroup and a Lipschitz function \(f\),
\[
\partial_{xx}P_r f(x)
=
\frac1r\mathbb E[(Z^2-1)f(x+\sqrt r\,Z)]
\]
can be centered to give
\[
\|\partial_{xx}P_r f\|_\infty
\le
\sqrt{\frac2\pi}\bigl(4e^{-1/2}-1\bigr)
r^{-1/2}\operatorname{Lip}(f).
\]
Thus cancellation changes the naive nonintegrable \(r^{-1}\) short-time majorant into an integrable \(r^{-1/2}\) one. This is classical, not novelty and not a project theorem.

## Unresolved and closure

The quadratic-Hessian programme is terminated because it did not establish a qualifying positive PDE/open-problem application. Its remaining legacy dependency cluster awaits one final curation sweep before the live wiki is cleanly separated into reusable material and pruned programme-specific pages.

The Fresnel programme is terminated as classical/low-payoff for the present objective. No further Fresnel development is active.

IPS treatment is frozen pending the author's policy answer about applying the autonomous verification bar to already published work. No further IPS curation changes should be made meanwhile.

## Wiki frontier

§0 items 1--2 pass. The current PDE-reader frontier remains **§0 item 3: linear, semilinear, quasilinear, and fully nonlinear equations**.

The item-3 entry is integrated and linked from `docs/pde-reading-path.md`. Legacy migration remains incomplete. When a Wiki Curator sweep is due, it replaces the ordinary PDE-reader slot for that cycle.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Broad novelty claims for cancellation before absolute values or representation-architecture dependence have substantial predecessors.
- The quadratic-Hessian programme failed the positive-PDE/open-problem viability gate and is terminated pending a future independently established target and fresh verification.
- The Fresnel programme is terminated as classical/low-payoff for the present objective.
- The elementary heat/Hermite cancellation alone does not control tree-depth moments.

## Next cycle

Run exactly three fresh read-only workers.

1. **Navier--Stokes cascade open-problem scout.** Identify the smallest respected published subsidiary open problem or criterion in the Le Jan--Sznitman/cascade/majorizing-kernel literature that could plausibly be affected by cancellation before modulus. Give two published sources with exact locations and a successor check. If none exists, test post-2023 fully nonlinear branching integrability or time-explosion literature as fallback.
2. **Navier--Stokes cancellation method scout.** Derive the smallest exact Fourier/cascade pairing or conditional averaging that strictly improves the standard absolute majorant, then test quantitatively whether it closes any criterion found by the first worker. Do not attack global regularity without that bridge.
3. **Wiki Curator.** Review `skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md`, `time-spine-coarsening-for-quadratic-hessian-patches.md`, and their directly dependent quadratic-Hessian pages, especially the deferred canonical-raw/raw-obstruction/self-consistent cluster and the random-patch conjecture. Do not review IPS pages.

After collecting the dispatches verbatim, launch a fresh Director session. A single later Integrator may make only the repository changes justified by that Director. Claude has no mathematical authority.
