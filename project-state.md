# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

## Active programme

**Supercritical dissipative SQG endpoint temporal-modulus closure test.**

The candidate global bridge remains the Dong--Pavlović $L_t^\infty C^{1-\gamma}$ endpoint, but the mechanism has **not** survived the SEARCH gate and DEVELOP is not authorized.

Established for this search:

- pointwise Riesz input-exchange cancellation is refuted as a source of a vanishing high-frequency coefficient;
- exact dissipation-time integration under the bare $L_t^\infty C^{1-\gamma}$ bound gives a scale-independent critical coefficient;
- every fixed finite-neighbor shell grouping is refuted as a universal bridge by an isolated comparable-frequency packet with a nonzero $O(1)$ normalized contribution at arbitrarily high scale;
- the Dong--Pavlović bridge needs a vanishing high-frequency gain, not necessarily shell summability;
- the sole remaining SEARCH question is whether actual SQG dynamics forces temporal coherence strictly better than the natural $N^\gamma$ dissipation-scale variation, or otherwise imposes a constraint that explicitly excludes the isolated comparable-frequency packet.

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

SQG is the sole active programme. Dissipation-time cancellation and every fixed finite-shell cancellation route are closed under the bare endpoint norm. Only the actual-solution temporal-modulus question remains unresolved: a useful $C_t^\eta$ estimate for the relevant normalized coefficient must improve on the scale-covariant $N^{\gamma\eta}$ variation, or some other equation-generated constraint must exclude the isolated packet.

The quadratic-Hessian programme remains terminated; only the two audited observations above and previously audited programme-neutral material remain live from that programme. The Fresnel programme remains terminated as classical/low-payoff. The Navier--Stokes stochastic-cascade route is closed as a current programme and has been removed from reserve.

The IPS freeze is removed. Project-specific IPS wiki material duplicated or superseded by the paper remains delete-first curation debt. Generic definition and literature pages are not deletion candidates merely because the project-specific theorem layer is deprecated.

## Wiki frontier

§0 items 1--2 pass. The current PDE-reader frontier remains **§0 item 3: linear, semilinear, quasilinear, and fully nonlinear equations**.

The item-3 entry is integrated and linked from `docs/pde-reading-path.md`. The sixth sweep removes the four remaining legacy PDE `status: proved here` pages and rewrites the sole IPS `proved here` page as a definition, leaving zero live `proved here` entries. Legacy migration remains incomplete. The next priority is the PDE reading path and the remaining unaudited PDE/background entries.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Broad novelty claims for cancellation before absolute values or representation-architecture dependence have substantial predecessors.
- The quadratic-Hessian programme failed the positive-PDE/open-problem viability gate and is terminated.
- The Fresnel programme is terminated as classical/low-payoff for the present objective.
- The elementary heat/Hermite cancellation alone does not control tree-depth moments.
- For SQG, pointwise Riesz input exchange fails on fixed-shape near-diagonal packets: the normalized contribution remains nonvanishing uniformly over dyadic scale.
- For SQG, exact Duhamel dissipation and every fixed finite-neighbor shell grouping fail to yield $g_j\to0$ under the bare $L_t^\infty C^{1-\gamma}$ norm. Ordinary scale-covariant time Hölder regularity cannot supply the missing gain; only temporal regularity strictly better than $N^{\gamma\eta}$ scaling, or another explicit packet-excluding mechanism, could do so.
- For Navier--Stokes cascades, the published factor-$1/2$ nodewise symmetrization improves amplitude majorants but leaves the cascade law and explosion event unchanged. That route is no longer active or reserve.
- For Strong-KPP, the difference-quotient/spectral-gap cancellation route has zero margin at critical ends and is refuted as the required bridge.
- For Strong-KPP, critical-mode projection is not stable enough under connected-limit detuning: $\delta A$ dominates $\kappa A^2$ whenever $A\ll|\delta|$, while bounded windows lose the nonlinear amplitude-selection term.

## Next cycle

Run exactly two fresh read-only workers concurrently.

1. **SQG nonlinear packet embedding worker.** Starting from the adversary's fixed comparable-frequency packet, construct or rigorously perturb to an actual smooth SQG solution and use SQG scaling to test the normalized near-diagonal coefficient on times $t\sim N^{-\gamma}$. Determine whether its physical-time $C^\eta$ modulus necessarily scales like $N^{\gamma\eta}$, so that the zero-mass kernel gain $N^{-\gamma\eta}$ is cancelled. This worker must either rigorously exclude a scale-improving modulus or identify the precise obstruction to the packet embedding.
2. **SQG temporal-modulus hostile auditor and literature adversary.** Independently derive the strongest time regularity forced by $L_t^\infty C^{1-\gamma}$ for actual SQG solutions near a candidate singular time. A useful result must give $o(N^{\gamma\eta})$, or another explicit scale-decaying effect, for the relevant normalized coefficient; ordinary parabolic scale covariance does not count. Check adjacent critical Besov/commutator/paraproduct literature for an existing theorem. If no mechanism excludes the isolated packet, recommend termination of SQG rather than another finite-shell variant.

No Wiki Curator is needed in the next cycle immediately after this sweep. No DEVELOP transition is automatic. Claude has no mathematical authority.
