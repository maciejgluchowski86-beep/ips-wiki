# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

## Active programme

**Supercritical dissipative SQG critical-endpoint dissipation-time/multi-shell cancellation.**

The candidate bridge is the Dong--Pavlović $L_t^\infty C^{1-\gamma}$ endpoint. The pointwise Riesz input-exchange pairing is refuted as a source of a vanishing high-frequency coefficient: fixed-shape near-diagonal low-high/high-low triads survive uniformly over dyadic scale. The live SEARCH question is whether integrating dissipation in time and/or grouping multiple neighboring shells before absolute values yields a scale-summable gain at the $L_t^\infty C^{1-\gamma}$ endpoint. SQG has not yet passed its replacement local-mechanism test.

## Reserve programme

**None.**

## Verified results

**None.**

## Reusable audited observations

Two observations from the terminated quadratic-Hessian programme survived hostile audit without becoming verified project theorems:

- the time-integrated first-moment norm of one centered heat-Hessian edge from $C^\alpha$ to $C^\beta$ has sharp cost $\asymp(\alpha-\beta)^{-1}$ on compact exponent ranges;
- the ordered-time derivative-cluster norm satisfies $\mathfrak P_m(\alpha,T)\leq 2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}$.

The classical local heat/Hermite cancellation remains reusable background mechanism evidence, not project novelty.

## Unresolved and closure

Strong-KPP is terminated under the pre-registered gate.

Exact critical-cylinder quadratic amplitude selection works but does not extend through qualitative connected-limit perturbations because the projected detuning term requires control comparable to

$$
|\lambda_1-a|=o(A),
$$

which the framework does not supply.

Fixed-scale estimates linearize at vanishing critical ends and cannot determine relative solution amplitudes; nonlinear selection occurs on diverging scales $A^{-1/2}$.

SQG is now the sole active programme.

The quadratic-Hessian programme remains terminated; only the two audited observations above and previously audited programme-neutral material remain live from that programme. The Fresnel programme remains terminated as classical/low-payoff. The Navier--Stokes stochastic-cascade route is closed as a current programme and has been removed from reserve.

The IPS freeze is removed. Project-specific IPS wiki material duplicated or superseded by the paper remains delete-first curation debt. Generic definition and literature pages are not deletion candidates merely because the project-specific theorem layer is deprecated.

## Wiki frontier

§0 items 1--2 pass. The current PDE-reader frontier remains **§0 item 3: linear, semilinear, quasilinear, and fully nonlinear equations**.

The item-3 entry is integrated and linked from `docs/pde-reading-path.md`. The fifth sweep deleted 13 deprecated FA research/scaffold entries, rewrote `front-growth-and-vacancy-density-for-fa-1f.md` as literature, removed the chronology route from public navigation/reference pages, and legacy migration remains incomplete. The next migration priority is legacy PDE `status: proved here`.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Broad novelty claims for cancellation before absolute values or representation-architecture dependence have substantial predecessors.
- The quadratic-Hessian programme failed the positive-PDE/open-problem viability gate and is terminated.
- The Fresnel programme is terminated as classical/low-payoff for the present objective.
- The elementary heat/Hermite cancellation alone does not control tree-depth moments.
- For SQG, pointwise Riesz input exchange improves deep high-high $\to$ low interactions but cannot produce a vanishing shell coefficient because fixed-shape near-diagonal low-high/high-low interactions retain ratio arbitrarily close to one uniformly over scale.
- For Navier--Stokes cascades, the published factor-$1/2$ nodewise symmetrization improves amplitude majorants but leaves the cascade law and explosion event unchanged. That route is no longer active or reserve.
- For Strong-KPP, the difference-quotient/spectral-gap cancellation route has zero margin at critical ends and is refuted as the required bridge.
- For Strong-KPP, critical-mode projection is not stable enough under connected-limit detuning: $\delta A$ dominates $\kappa A^2$ whenever $A\ll|\delta|$, while bounded windows lose the nonlinear amplitude-selection term.

## Next cycle

Run at most two fresh read-only workers concurrently.

1. **SQG dissipation-time/multi-shell cancellation worker.** Starting from the near-diagonal low-high/high-low interactions that defeated pointwise Riesz input exchange, perform the smallest explicit Duhamel/time-integrated and adjacent-shell grouping calculation at the supercritical $C^{1-\gamma}$ endpoint. Determine whether cancellation before absolute values yields a coefficient that actually decays or is summable in scale. Exhibit the load-bearing dyadic/time integrals explicitly.
2. **SQG endpoint global-bridge adversary.** Independently derive the quantitative shell/time summability needed to close the published endpoint criterion, test the strongest plausible multi-shell estimate against near-diagonal adversarial configurations, and check adjacent commutator/paraproduct literature for an existing equivalent mechanism.

After either finishes, the freed slot may start a **Wiki Curator sixth sweep**, beginning with legacy PDE `status: proved here` pages. Never exceed two concurrent workers.

No DEVELOP transition is automatic. SQG remains at SEARCH until a replacement local mechanism survives the gate. Claude has no mathematical authority.
