# Graduate Student B assignment 004: exclude hostile invariant front phases

Work on branch `research/babp-finite-seed`.

Read first:

- `project-state.md`;
- `research/active/babp-finite-seed/state.md`;
- `research/active/babp-finite-seed/proof-spine.md`;
- `research/active/babp-finite-seed/meetings/006-sudbury-correction-and-front-reduction.md`;
- your `students/student-b/003-front-gap.md`, commits `5c357ef` and `1365840`.

The Sudbury full-text audit has changed the novelty accounting: finite-window robust submartingales and their use in finite-seed convergence are classical. The remaining scientifically important target is the all-parameter theorem.

Your validated fixed-parameter reduction is

$$
\lim_{k\to\infty}v_k(\lambda)
=
\inf_{\mu\in\mathcal I_\lambda}\mu(\lambda-u_1),
$$

with

$$
\mu(\lambda-u_1)
=
\frac{\lambda}{1+\lambda}
\left(\lambda-\frac12\mu(01)\right).
$$

Every singleton-selected Cesaro invariant front law has strictly positive current. Thus the remaining obstruction is an invariant semi-infinite-tail phase not selected from finite seeds.

## Main objective

Prove or refute that every invariant law of the infinite right-front process has strictly positive current for every fixed `lambda>0`.

A sufficient but stronger target is:

> **FRONT-UNIQUENESS:** `Q_infinity` has a unique invariant probability law for every `lambda>0`.

Do not force uniqueness if a weaker phase-selection or current theorem is more natural.

## Route A: entropy/current in gap coordinates

Make the reversible-bulk observation quantitative. The bulk gap process has iid geometric reversible reference law, while the moving front is the only driven boundary.

1. Define finite `n`-gap truncations with explicit far-boundary conditions. Choose at least two hostile boundary conditions, not only the equilibrium one.
2. Derive the exact stationary current/entropy-production identity. Identify the front affinity and every far-boundary flux term.
3. Determine what estimate would force any infinite-volume limit to have nonnegative, preferably positive, front current.
4. Prove a no-incoming-flux statement from particle-index infinity if possible. Do not discard a boundary term without a uniform estimate.
5. If the entropy route fails, isolate the exact sign-indefinite term and construct a state or invariant finite truncation showing why.

A theorem of the form “every invariant law has nonnegative current, and zero current is impossible at `lambda>0`” is enough; uniqueness is not required.

## Route B: coupling / phase selection

Try to couple two infinite-front configurations under the same graphical construction and prove convergence on every fixed prefix.

The known obstruction must be addressed explicitly: a run of outward births refreshes a prefix, but later left shifts can expose untouched tail information. Any coupling argument must control this return mechanism rather than assume it away.

Possible targets include:

- a weighted disagreement Lyapunov function with weights decaying into the tail;
- regeneration times at which the probability of subsequently exposing pre-regeneration tail information is summable;
- contraction of finite-prefix laws after averaging over a suitable front-current event;
- uniqueness within a class first, followed by a proof that every invariant law belongs to that class.

If you find a hostile invariant phase or a plausible construction of one, pursue that instead of defending the programme.

## Cheap falsification/calibration

Use finite-gap truncations to test whether different far-boundary conditions produce distinct limiting prefix laws or currents as truncation size grows. This computation is diagnostic only, but it should be done early enough to distinguish a uniqueness route from a phase-coexistence route.

Track at least:

- stationary front current;
- `P(g_1=1)`;
- sensitivity of the first few gaps to the far boundary;
- scaling in truncation length for several small positive `lambda`.

Do not promote numerical convergence to a theorem.

## Literature

Search specifically for invariant measures of environments seen from fronts, boundary-driven one-dimensional coagulation/fragmentation systems, and half-line interacting particle systems with shift/reset dynamics. The question is no longer general BABP literature; it is whether a theorem already controls this front process or suggests a usable uniqueness/current argument.

## Output

Commit the durable result to

`research/active/babp-finite-seed/students/student-b/004-hostile-front-phase.md`

plus any finite-state code/data needed for calibration.

End with one of the following substantive outcomes:

- a proof of positive current for every invariant front law;
- a proof of front uniqueness;
- a counterexample/hostile phase;
- a strictly narrower lemma whose proof would settle the issue and for which the other interfaces are established;
- or a documented failure showing why the available entropy/coupling mechanisms are not closing.

This is an opportunity-cost checkpoint. Do not respond to failure by merely increasing the corrector window.