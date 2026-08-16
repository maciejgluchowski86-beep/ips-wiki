# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional, homogeneous, binary, one-sided nearest-neighbour IPS with positive rates is ergodic.

The target is fixed by the principal. The proof spine may change; the target does not.

## E0. Source reductions already established

For a simple IPS write

$$
r_{xy}=P_0(1\mid xy).
$$

Positive rates are

$$
r_{11}<1,\quad r_{10}<1,\quad r_{01}>0,\quad r_{00}>0.
$$

Time-scaling and state symmetry reduce the unresolved problem to the face `r11=0`. With

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the currently unproved normalized chamber is

$$
\boxed{
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
}
$$

This is inherited from the source-corrected previous programme. It must be source-checked again before any theorem depending sensitively on a boundary case.

## E1. Known wall mechanism and its limit

The 2026 long-lived-state theorem proves ergodicity if, for some state `s`,

$$
\delta(s)<\sqrt2\,\beta(s).
$$

On `R`, the relevant one-site criterion fails. The previous programme then analyzed fixed agreed blocks. Its strongest target-relevant local result was the exact three-site frozen-exterior one-attack bound with East-boundary supremum `5/6`.

However, under a permanently frozen exterior disagreement, repeated attacks cross every fixed finite block almost surely. Therefore the one-attack fixed-wall quantity is not an iteratable renewal parameter.

**Status:** route closed. No block-length escalation.

## E2. Principal's earlier last-successful-interaction route

The principal recalls a different construction in the monomial-duality process. For a finite interval `R`, consider the last successful interaction whose influence exits `R`; reveal that interaction and the active spacetime ancestry trail leading to it, then undo duality for the remaining randomness.

The recollection suggests three pieces:

1. a **late piece** confined to `R` by one-sidedness, contributing a product-function evaluation under a spin system with the exterior of `R` fixed;
2. an **early piece** represented by the original spin system with a modified boundary rule;
3. the revealed trail, producing a positive exponential factor.

A Duhamel expansion with naive estimates was remembered as giving a partial implication of the form

$$
\text{eventual high density of the appropriate state}
\Longrightarrow
\text{ergodicity}.
$$

The exact note is in `principal-starting-note.md`.

**Status:** unverified recollection. Do not cite it as a theorem and do not silently choose the spin convention or meaning of "high density".

## E3. Active edge: reconstruct a genuine one-way reduction

Recover E2 from first principles or from surviving committed material. The required output is not another equivalent representation. It must identify an exact statement

$$
Q\Longrightarrow\text{ergodicity}
$$

with all of the following:

- a precise definition of `Q`;
- the exact finite interval/boundary dynamics appearing in the decomposition;
- a rigorous identity or inequality before absolute values are taken;
- a quantitative error term in the interval size/time horizon;
- proof that `Q` is logically and technically weaker than the original convergence statement, not merely a rephrasing;
- an independently plausible route to proving `Q` in the residual chamber.

If the remembered Duhamel route fails, record the first false identity or uncontrolled term. That is useful narrowing.

## E4. Conditional next edge if E3 survives: prove the qualitative premise

The intended payoff of E3 is to replace exact convergence by a qualitative density statement that can be attacked using finite boxes. Candidate forms include, but are not limited to:

- a uniform lower bound on the density of the state that kills the bad Duhamel contributions after some burn-in;
- a finite-box probability that a macroscopic fraction of sites are in that state, with errors uniform in boundary condition;
- a one-sided regeneration event whose frequency implies such a density bound;
- a domination statement that is strictly weaker than convergence to an invariant law.

No particular form is assumed. The student must derive the form from the exact E3 inequality rather than inventing a convenient condition first.

## E5. Alternative structural routes remain allowed

The principal's note is a starting point, not a prescribed proof. A student may replace E2--E4 with a stronger route if it yields an actual new estimate on the residual dynamics. Plausible assets include:

- one-sided finite propagation;
- canonical coupling and disagreement geometry;
- East-model front/regeneration information;
- finite-volume comparison with controlled boundary errors;
- signed monomial duality and conditional averaging;
- the canonical patch representation in `paper/`;
- perturbation in the positive-rate noise;
- invariant-measure or density identities that do not presuppose ergodicity.

The requirement is an irreversible mathematical gain, not a new vocabulary.

## Anti-circularity checkpoint

Before promoting any new edge to the spine, answer explicitly:

1. What was the previous unresolved mathematical statement?
2. What new implication, estimate, or obstruction has been proved?
3. Why is the new statement strictly easier to verify or strictly narrower?
4. Could one recover the old statement from the new one by definitions alone? If yes, it is not progress.
5. What concrete calculation or theorem would falsify the proposed route next?

Equivalent changes of spin convention, dual variables, density profiles, invariant-law language, or finite/infinite-volume notation are not new spine edges.

## Current direction

Attack E3 in parallel from two flexible agents. Reassess only proof routes, never the fixed scientific target.
