# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

## Active programme

**General-domain Dirichlet strong-KPP uniqueness: critical-end ratio test.**

The two-published-source open-problem gate is confirmed for general-domain Dirichlet strong-KPP uniqueness of positive bounded solutions in the published regularity framework. For programme selection, the difference-quotient/spectral-gap cancellation route is refuted: the local strong-KPP sign is already used, and at a critical end the spectral margin can vanish as the relevant limit approaches the linearization at zero. The unresolved obstruction is comparison of positive solutions when both vanish along a critical end.

The sole surviving SEARCH target is the following. For a critical connected limit with a simple isolated principal mode and

$$
f(s)=as-Bs^2+O(s^3),
$$

derive the projected quadratic amplitude equation with a quantitative perturbation error and determine whether it yields either a scale-uniform bound or an asymptotic constant for the ratio $u/v$.

**Pre-committed failure condition.** If this mechanism fails already in the restricted simple-mode class, or yields only a local constant/kernel improvement without global ratio control, terminate Strong-KPP rather than moving it to reserve.

## Reserve programme

**Supercritical dissipative SQG critical-endpoint time/multi-shell cancellation.**

The candidate bridge is the Dong--Pavlović $L_t^\infty C^{1-\gamma}$ endpoint. The natural pointwise Riesz input-exchange pairing is refuted as a source of a vanishing high-frequency coefficient: fixed-shape near-diagonal low-high/high-low triads survive uniformly over dyadic scale. Genuine dissipation-time or multi-shell averaging is a distinct mechanism and remains open.

## Verified results

**None.**

## Reusable audited observations

Two observations from the terminated quadratic-Hessian programme survived hostile audit without becoming verified project theorems:

- the time-integrated first-moment norm of one centered heat-Hessian edge from $C^\alpha$ to $C^\beta$ has sharp cost $\asymp(\alpha-\beta)^{-1}$ on compact exponent ranges;
- the ordered-time derivative-cluster norm satisfies $\mathfrak P_m(\alpha,T)\leq 2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}$.

The classical local heat/Hermite cancellation remains reusable background mechanism evidence, not project novelty.

## Unresolved and closure

The Strong-KPP literature gate is closed. The live Strong-KPP gap is now the critical-end ratio/comparability problem above.

The quadratic-Hessian programme remains terminated; only the two audited observations above and previously audited programme-neutral material remain live from that programme. The Fresnel programme remains terminated as classical/low-payoff. The Navier--Stokes stochastic-cascade route is closed as a current programme and has been removed from reserve.

The IPS freeze is removed. Project-specific IPS wiki material duplicated or superseded by the paper remains delete-first curation debt. Generic definition and literature pages are not deletion candidates merely because the project-specific theorem layer is deprecated.

## Wiki frontier

§0 items 1--2 pass. The current PDE-reader frontier remains **§0 item 3: linear, semilinear, quasilinear, and fully nonlinear equations**.

The item-3 entry is integrated and linked from `docs/pde-reading-path.md`. Legacy migration remains incomplete. This sweep deletes eight FA-1f/BABP specialization pages for monomial duality, patch contributions, patch positivity, and patch critical density; rewrites the BABP out-of-equilibrium page as literature only; and repairs the FA-1f and BABP model pages. Remaining legacy IPS migration is incomplete, with the FA chronology/regeneration subtree still unaudited.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Broad novelty claims for cancellation before absolute values or representation-architecture dependence have substantial predecessors.
- The quadratic-Hessian programme failed the positive-PDE/open-problem viability gate and is terminated.
- The Fresnel programme is terminated as classical/low-payoff for the present objective.
- The elementary heat/Hermite cancellation alone does not control tree-depth moments.
- For SQG, pointwise Riesz input exchange improves deep high-high $\to$ low interactions but cannot produce a vanishing shell coefficient because fixed-shape near-diagonal low-high/high-low interactions retain ratio arbitrarily close to one uniformly over scale.
- For Navier--Stokes cascades, the published factor-$1/2$ nodewise symmetrization improves amplitude majorants but leaves the cascade law and explosion event unchanged. That route is no longer active or reserve.
- For Strong-KPP, the difference-quotient/spectral-gap cancellation route has zero margin at critical ends and is refuted as the required bridge.
- For Strong-KPP, local-cancellation-only or bounded-scale kernel improvements are dead ends unless they produce global ratio control on critical ends.

## Next cycle

Run at most two fresh read-only workers concurrently.

1. **Strong-KPP critical-mode asymptotics worker.** Derive or refute the stable projected quadratic amplitude law and a quantitative $u/v$ consequence on the restricted simple-critical-mode class.
2. **Strong-KPP global-bridge adversary.** Test whether the strongest such estimate actually restores finite global comparison/sliding on critical ends; actively seek counterexamples.

After either finishes, use the freed slot for a **Wiki Curator fifth sweep** treating the remaining FA chronology/regeneration subtree as a dependency graph.

No DEVELOP transition is automatic. The next Director decides: if the ratio bridge survives, consider DEVELOP; if the restricted-class mechanism fails or is nonresponsive, terminate Strong-KPP and promote SQG. Claude has no mathematical authority.
