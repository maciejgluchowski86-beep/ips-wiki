# Student F assignment 003: direct dynamic disagreement/regeneration episode

Work on branch `research/positive-rates-conjecture`.

The scientific target remains fixed: prove the positive rates conjecture for simple IPS.

Read first:

- updated `state.md` and `proof-spine.md`;
- `meetings/002-cellwise-insertion-composition-fails.md`;
- your Assignment 001 and 002 reports only as reusable mathematics, not as a route that must be rescued;
- Student G's Assignment 001 report for the direct transient density/no-`11` estimates;
- the final closure meeting on `research/noisy-east-positive-rates` so the fixed-wall obstruction is not recreated.

Student G is still finishing Assignment 002 independently. Do not wait for it.

## Route boundary

The cellwise last-exit/scaffold insertion mechanism is closed by Assignment 002. Do not respond by grouping three cells, increasing a cell size, or introducing a new name for a cluster of `Psi_Delta` transfers unless you first prove a genuinely new cancellation estimate that is not just the failed sign condition at a coarser scale.

The older frozen-exterior finite-wall route also remains closed.

## Objective

Attack the **actual dynamic lifetime and propagation of a disagreement source** under the canonical coupling of two copies of the residual noisy-East system.

The key distinction from the closed wall route is that the exterior disagreement must evolve according to the true coupled dynamics and may disappear. The key distinction from the closed scaffold route is that no nonnegative sign is demanded cell by cell along a dual predecessor chain.

Produce one irreversible estimate about a live disagreement episode.

A strong outcome would be a finite-time/slab contraction statement of the following general kind: after a burn-in or on a suitable dynamically defined good event, a disagreement entering a block from the right has probability strictly less than one of producing a surviving disagreement on the left **before the source episode dies**, with the source evolution included in the same probability space. The exact statement and observable are yours to choose.

## Promising handles, not requirements

Student G proved on the original dynamics:

- a boundary-uniform positive zero-density after fixed burn-in;
- finite-box high-probability versions via one-sided propagation;
- suppression of adjacent `11` pairs, with a mesoscopic no-`11` regime near the East boundary.

Possible uses include:

- a regeneration event built from an actual stretch of zeros/no-`11` geometry;
- an oriented disagreement path estimate whose killing rate is enhanced on those events;
- a Lyapunov function for the coupled process involving disagreement plus a local bad-environment term such as adjacent `11`;
- a state-dependent branching/influence process that is subcritical after averaging over the true environment;
- a time-slab coarse graining in which good blocks are proved from the dynamics, not assumed.

You may abandon these if a better direct mechanism appears.

## Anti-circularity / falsification requirement

Do not count any of the following as progress by themselves:

- defining a disagreement process without estimating it;
- saying a source should die because zeros are dense;
- another one-attack probability with the source frozen;
- another finite-box density estimate with no coupling consequence;
- an equivalent uniqueness or duality criterion.

For every proposed episode quantity, identify the exact inequality that would imply a contraction or regeneration statement. Test it on the smallest nontrivial local states or by exact finite-state computation before investing in a large construction.

If the direct density/no-`11` information is fundamentally insufficient, produce an explicit live-source configuration or finite-state obstruction showing why. That would be useful narrowing.

## Suggested first calculation

Under the canonical common-uniform update coupling, write the exact local transition probabilities for the pair state at site `i` as a function of the two pair states at `(i,i+1)`. From this, try to identify a local or short-range nonnegative observable `W` that penalizes both disagreement and the environmental patterns that sustain it. Check whether its generator has a negative drift after a fixed burn-in, on the no-`11` sector, or after averaging over a time slab using G's estimates.

This suggestion is intentionally concrete but not mandatory. A different live-source mechanism is acceptable if it yields a proved estimate.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/003-live-disagreement-episode.md`

with supporting code beside it if useful.

End with one of:

- `live-source contraction proved: ...`;
- `new regeneration estimate proved: ...`;
- `direct density-to-disagreement bridge fails because: ...`;
- `new structural route with first proved lemma: ...`;
- `unresolved after substantive work; exact blocker: ...`.
