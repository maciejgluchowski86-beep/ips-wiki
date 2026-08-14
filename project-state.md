# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

## Active programme

**Supercritical dissipative SQG cancellation search.**

Before any transition to DEVELOP, identify a respected subsidiary SQG open problem or criterion explicitly documented in at least two published sources, give exact locations and a successor check, and isolate a concrete signed-cancellation or conditional-averaging mechanism capable of affecting that criterion quantitatively. Do not attack global regularity wholesale without this bridge.

## Reserve programme

**Navier--Stokes stochastic-cascade multi-generation cancellation.**

The nodewise factor-$1/2$ symmetrization is already known. It improves amplitude majorants but does not alter the cascade split kernel, exponential lifetimes, genealogy, or explosion event. Reactivate this reserve only after both the two-published-source gate for the same subsidiary criterion and a quantitative multi-generation cancellation gain that changes an integrability or uniqueness criterion have been established.

## Verified results

**None.**

## Claims under investigation

Three PDE problems have adequate published open-problem documentation for the SEARCH-stage gate:

- three-dimensional incompressible Navier--Stokes global regularity;
- supercritical dissipative SQG global regularity;
- strong-KPP uniqueness on arbitrary domains.

This clears only the open-problem documentation component. It does not establish a project theorem or justify a transition to DEVELOP. Strong-KPP is not an active or reserve programme because no signed-cancellation interface has been identified.

A classical local heat/Hermite cancellation remains reusable mechanism evidence. For the heat semigroup and a Lipschitz function $f$,
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
Thus cancellation changes the naive nonintegrable $r^{-1}$ short-time majorant into an integrable $r^{-1/2}$ one. This is classical, not novelty and not a project theorem.

## Unresolved and closure

The quadratic-Hessian programme is terminated because it did not establish a qualifying positive PDE/open-problem application. Its final legacy dependency cluster remains unresolved pending an independent audit of the strict-regularity-loss one-edge $L^1$ estimate and the ordered-time derivative-cluster estimate. Legacy `status: proved here` labels in that cluster are not current verification and must not be treated as such.

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
- For Navier--Stokes cascades, the published factor-$1/2$ nodewise symmetrization improves amplitude majorants but leaves the cascade law and explosion event unchanged; the general-data averaging challenge found in the latest search does not yet meet the two-published-source gate.

## Next cycle

Run exactly three fresh read-only workers, strictly sequentially in this priority order.

1. **SQG open-problem bridge scout.** Identify the smallest respected published subsidiary criterion for supercritical dissipative SQG, with two published exact sources and successor check, and isolate where signed cancellation could enter.
2. **SQG cancellation method scout.** Derive the smallest exact cancellation or conditional-averaging gain and test it quantitatively against worker 1's criterion.
3. **QH reusable-extract/dependency hostile auditor.** Independently audit the one-edge strict-regularity-loss $L^1$ estimate and ordered-time derivative-cluster bound; then produce one coherent dependency-safe KEEP/REWRITE/DEMOTE/DELETE disposition for the remaining QH legacy cluster, explicitly including `banach-scale-obstruction-for-raw-pde-patches.md` and all inbound links.

After collecting the dispatches verbatim, launch a fresh Director session. A single later Integrator may make only the repository changes justified by that Director. Claude has no mathematical authority.
