# Project state

This file is the compact mutable state for the autonomous PDE/probability research programme. It records current useful state only. Git history is the archive.

## Stage

**SEARCH**

## Active programme

**Long-maturity marked-branching representations by time-slab conditional averaging.**

The setting is the Henry-Labordère--Oudjane--Tan--Touzi--Warin semilinear class

$$
-\partial_t u-Lu=f(t,x,u,Du),
$$

with $f$ polynomial in $(u,Du)$. The existing marked-branching construction provides a positive short-time module, but its one-shot representation theorem is subject to an integrability/non-explosion condition that restricts the usable regime to small maturity or small nonlinearity.

The first SEARCH gate is an exact two-slab $L^1$ theorem. It must:

- construct the exact two-slab estimator, including the independent replicas required by polynomial products and all Malliavin/gradient weights;
- prove unbiasedness without inserting the unknown interface solution as data;
- make conditional averaging at the deterministic slab interface a genuine computable representation operation;
- derive an explicit first-moment recursion; and
- exhibit a parameter regime in which two slabs are integrable although the corresponding one-shot HLOTW criterion fails.

Warin's nested methods are evidence that time decomposition is structurally relevant, but they are also the main novelty hazard. The target is an exact unbiased representation theorem, not generic nested Monte Carlo. The novelty and open-problem status of this formulation are **unverified**. DEVELOP is not authorized until both the mechanism and literature gates pass.

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

SQG is terminated. Genuine smooth SQG solutions, after exact scaling, attain $N^{\gamma\eta}$ temporal variation of the normalized comparable-frequency coefficient; this exactly cancels the $N^{-\gamma\eta}$ zero-mass-kernel gain, and no explicit packet-excluding mechanism was found.

Five programmes are now terminated: quadratic-Hessian, Fresnel, Navier--Stokes cascade, Strong-KPP, and SQG. There is still no verified project result.

The active two-slab branching candidate remains in SEARCH. It fails immediately if either:

1. the exact $L^1$ recursion gives no strict enlargement after interface norms are accounted for; or
2. the exact unbiased two-slab theorem is already contained in, or subsumed by, the existing literature.

Its exact novelty/open-problem status has not yet passed the final literature audit.

The IPS freeze remains removed. Project-specific IPS wiki material duplicated or superseded by the paper remains delete-first curation debt. Generic definition and literature pages are not deletion candidates merely because the project-specific theorem layer is deprecated.

## Wiki frontier

§0 items 1--2 pass. The current PDE-reader frontier remains **§0 item 3: linear, semilinear, quasilinear, and fully nonlinear equations**.

The item-3 entry is integrated and linked from `docs/pde-reading-path.md`. The sixth sweep left zero live `status: proved here` entries. Legacy migration remains incomplete. The next priority is the PDE reading path and the remaining unaudited PDE/background entries.

SQG termination creates no new archive page. Programme termination together with incomplete legacy migration triggers another Wiki Curator sweep under the repository rules.

## Dead ends

Keep this section sparse; record only failures expensive enough that forgetting them risks repeating work.

- Broad novelty claims for cancellation before absolute values or representation-architecture dependence have substantial predecessors.
- The quadratic-Hessian programme failed the positive-PDE/open-problem viability gate and is terminated.
- The Fresnel programme is terminated as classical/low-payoff for the present objective.
- The elementary heat/Hermite cancellation alone does not control tree-depth moments.
- For Navier--Stokes cascades, the published factor-$1/2$ nodewise symmetrization improves amplitude majorants but leaves the cascade law and explosion event unchanged.
- For Strong-KPP, the cancellation route has zero margin at critical ends, while critical-mode projection is not stable enough under connected-limit detuning: $\delta A$ dominates $\kappa A^2$ whenever $A\ll|\delta|$.
- For SQG, actual smooth scale-covariant solutions can have normalized comparable-frequency coefficients with nonzero $C_t^\eta$ variation scaling as $N^{\gamma\eta}$; this exactly cancels the $N^{-\gamma\eta}$ zero-mass-kernel gain, and no explicit equation-generated packet exclusion was found.

## Next cycle

Run exactly two fresh read-only workers concurrently.

1. **Marked-branching two-slab mechanism and novelty worker.** Derive the exact two-slab marked estimator for the HLOTW polynomial-$(u,Du)$ class. Make unbiasedness, independent-copy structure, Malliavin weights, conditioning, and the first-moment recursion explicit. Determine whether there is a strict admissible-maturity gain over the one-shot criterion. In parallel, aggressively check HLOTW successors, Warin's nested methods, and later branching-integrability literature for an existing exact theorem. If the construction is tautological, gives no strict $L^1$ gain, or is already subsumed, recommend immediate termination.
2. **Wiki Curator, seventh sweep.** Because programme termination is itself a pruning trigger and legacy migration remains incomplete, review one coherent batch of at most about twelve pages, beginning with the next unaudited PDE-reading-path material and extending where directly coupled to the new branching programme, especially branching/nonexplosion, marked-gradient, Malliavin-weight, and uniform-integrability entries. Return exact KEEP/REWRITE/DEMOTE/DELETE actions, statuses, `audit: current` decisions, inbound links, and dependency-safe repairs.

No DEVELOP transition is automatic. Claude has no mathematical or editorial authority.
