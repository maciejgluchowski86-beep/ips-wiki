# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

## Active programme

**No active scientific programme.** The 1D FA-1f Bernoulli-quench candidate was never nominated and is now closed after Gate-6 **REJECT**.

## Reserve programme

**None.**

## Verified results

**None.**

## Reusable audited observations

Two observations from the terminated quadratic-Hessian programme survived hostile audit without becoming verified project theorems:

- the time-integrated first-moment norm of one centered heat-Hessian edge from $C^\alpha$ to $C^\beta$ has sharp cost $\asymp(\alpha-\beta)^{-1}$ on compact exponent ranges;
- the ordered-time derivative-cluster norm satisfies $\mathfrak P_m(\alpha,T)\leq 2A_{\alpha,T}4^m(1+A_{\alpha,T})^{m-1}$.

The classical local heat/Hermite cancellation remains reusable background mechanism evidence, not project novelty. As a classical calibration, two first-derivative Gaussian marks admit an exact conditional-coarsening $L^1$ ratio

$$
\kappa=\frac{\pi}{2e},
$$

and independent clusters tensorize as $\kappa^n$. This is not a project theorem.

## Unresolved and closure

Seven previously nominated programmes are terminated: quadratic-Hessian, Fresnel integrability, Navier--Stokes stochastic cascade, Strong-KPP uniqueness, supercritical dissipative SQG, long-maturity marked branching, and Gaussian bridge coarsening. Separately, the screened 1D FA-1f Bernoulli-quench candidate is closed at Gate 6 and was never nominated. There is no active programme, no reserve, and no verified project result.

The IPS freeze remains removed. Project-specific IPS wiki material duplicated or superseded by the paper remains delete-first curation debt. Generic definition and literature pages are not deletion candidates merely because a project-specific theorem layer is deprecated.

## Wiki frontier

Section 0 item 6 is integrated as the audited prerequisite [Regularity, well-posedness, and a priori estimates](docs/entries/regularity-well-posedness-and-a-priori-estimates.md). The PDE vocabulary layer is complete.

The PDE-reader frontier is now **§1: heat equation and heat kernel**, beginning the heat-equation layer.

Legacy migration remains incomplete. The next curation priority is the PDE reading path beginning with §1 heat equation and heat kernel, then recently changed PDE entries, potentially stranded SQG-era background entries, and other duplicate, obsolete, scaffolding, or terminated-programme material.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- The quadratic-Hessian programme failed the positive-PDE/open-problem viability gate and is terminated.
- The Fresnel programme is terminated as classical/low-payoff for the present objective.
- For Navier--Stokes cascades, the published factor-$1/2$ nodewise symmetrization improves amplitude majorants but leaves the cascade law and explosion event unchanged.
- For Strong-KPP, the cancellation route has zero margin at critical ends, while critical-mode projection is not stable enough under connected-limit detuning: $\delta A$ dominates $\kappa A^2$ whenever $A\ll|\delta|$.
- For SQG, actual smooth scale-covariant solutions can have normalized comparable-frequency coefficients with nonzero $C_t^\eta$ variation scaling as $N^{\gamma\eta}$; this exactly cancels the $N^{-\gamma\eta}$ zero-mass-kernel gain, and no explicit equation-generated packet exclusion was found.
- Deterministic HLOTW time-slab restarting gives no strict first-moment maturity gain: value-only positive majorants consume exactly the same blow-up budget, while restarted gradient kernels are weakly worse.
- Two first-derivative Gaussian marks admit the exact $L^1$ coarsening factor $\pi/(2e)$, tensorizing to $\kappa^n$, but this is an instance of classical conditional-expectation contraction and fails the novelty gate.
- For the 1D FA-1f Bernoulli-quench sibling-cancellation candidate, the two sibling coins give only a double zero: the first rate weighting still cancels, but at three generations $D_q^3 f(\{0\})/a=1-4q+2q^2\to1$, restoring the critical scaling; Gate 6 therefore rejects this mechanism.
- Procedural: unresolved target/mechanism/obstruction/novelty questions are pre-nomination screening work, not reasons to promote a candidate into the active scientific slot.

## Next cycle

Run exactly two fresh read-only workers, with no more than two concurrent.

1. **Pre-nomination candidate screener.** Search for at most two fresh serious candidates. Run all seven preregistered gates explicitly for each: precise positive target, exact two-published-source open-problem documentation plus successor check, obstruction interface, smallest local gain calculation, first composition/scaling test, non-retrospective adversarial family, and alternate-terminology novelty search. Recommend at most one for later Director consideration only if all seven gates PASS. UNRESOLVED is not PASS. Do not nominate or enter DEVELOP. Do not reopen the closed FA-1f sibling-cancellation/block candidate; a genuinely different FA-1f representation must enter as a new candidate with a new complete seven-gate screen.
2. **Wiki Curator, eleventh sweep.** Continue legacy migration from the new §1 heat-equation/heat-kernel frontier, auditing a coherent batch of at most about twelve existing directly coupled pages. Apply KEEP/REWRITE/DEMOTE/DELETE, identify the first missing atomic heat-equation prerequisite if necessary, verify dependencies and sources, and promote no project-specific mathematics.
