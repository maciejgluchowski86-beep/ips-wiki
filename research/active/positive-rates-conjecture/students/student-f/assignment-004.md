# Student F assignment 004: two-generation live episode with reinfection

Work on branch `research/positive-rates-conjecture`.

The scientific target remains fixed: prove the positive rates conjecture for simple IPS.

Read first:

- updated `state.md` and `proof-spine.md`;
- `meetings/003-live-source-contraction.md`;
- your Assignment 003 report and verifier;
- Student G's Assignment 001 report for the direct transient density / `11` estimates;
- the two closed-route records: the old frozen-wall closure and Meeting 002's cellwise-scaffold closure.

Student G is still completing Assignment 002. Do not wait for it.

## What is now established

For a rightmost disagreement `j` with `j-1` agreed, under the true common-uniform coupling,

$$
\mathbb P(\text{first child at }j-1\text{ before source death at }j\mid\mathcal F)
\le1-\delta(a,b,c)<1
$$

uniformly over the evolving common right-hand environment. The finite-slab regeneration probability `delta_T` is also established.

This is not enough to iterate. Once the child exists, it is not rightmost; it can die while the parent remains alive and then be reinfected. The next state is genuinely different.

The East-boundary degeneration of the one-source gap is also established. Along `a=eps^2, b=eps, c=1-eps^2`, first-child creation is much faster than parent death. Do not treat this alone as fatal: the target is pointwise in strict positive-rate parameters, and the post-birth child has a fast killing mechanism not used in the one-source estimate.

## Decisive objective

Analyze the **entire two-generation parent-child episode after the first child is born**, including all child deaths and reinfections by the still-live parent.

A concrete formulation is as follows. At a stopping time, let `j` be the rightmost disagreement and suppose its first child at `j-1` has just been created while `j-2` is still agreed. Define

- `sigma_2`: first creation of a disagreement at `j-2` (a grandchild);
- `tau_2`: first time at which both `j` and `j-1` are coupled, after which the entire half-line `k>=j-1` is permanently coupled.

You may refine these stopping times if a better renewal state is needed. The important point is that reinfection of `j-1` by a live parent must be included exactly, not suppressed by a frozen or one-shot approximation.

Try to prove a bound of the form

$$
\mathbb P(\sigma_2<\tau_2\mid\text{post-first-child state})
\le1-\delta_2(a,b,c)
$$

with `delta_2>0` for every strict residual parameter point, uniformly over the admissible common environment to the right. A stronger restart statement is preferable.

If such a uniform-over-environment bound is too strong, identify the smallest actual-environment quantity needed and prove a conditional estimate for it rather than replacing it by an unquantified assumption.

## The structured zero-born child is the first test

When a child is created from an agreed zero, its disagreement orientation matches the parent. In that state its own update has a large coalescence probability (`1-a` in the simplest local configuration). This is the concrete mechanism that might compensate for the near-East degeneration of the parent-childless gap.

Analyze this state first and compute the exact near-East asymptotic. Determine whether the probability of producing a grandchild before the parent-child episode retreats has a nontrivial limit below one, tends to one, or depends on a further state variable.

Do not stop at this favorable state if the general episode can enter other states with positive probability.

## Finite-state / controlled-chain freedom

This is a suitable place for exact finite-state computation if useful. You may:

- construct the exact local coupled CTMC for `(j-2,j-1,j)` plus the necessary right-boundary state;
- formulate a worst-case switching / controlled Markov chain for the common right environment;
- solve hitting probabilities symbolically or by rational certificates;
- search for a nonnegative Lyapunov/superharmonic function certifying the desired hitting bound;
- use the one-source result after parent death, when the surviving child becomes rightmost;
- exploit Student G's `11` suppression only if it enters through an explicit weighted/conditional term.

A computer-assisted certificate is acceptable if the mathematical reduction and parameter dependence are explicit and auditable.

## Composition requirement

A positive two-generation number is not sufficient by itself.

If you obtain `delta_2>0`, identify the **restart state** after successful retreat/elimination and determine whether repeated spatial progress can be represented by a finite family of episode states with a common contraction mechanism. At minimum, test the next composition step or exhibit a finite-state renewal kernel that would make iteration legitimate.

If two-generation contraction fails, give the smallest explicit residual parameter/state obstruction and state exactly which live-episode mechanism it closes.

## East-boundary discipline

The theorem does not require a contraction constant uniform over the closure `c=1`. Do not reject a valid parameter-dependent contraction merely because it tends to zero as the East boundary is approached.

However, explicitly compute the near-East scaling. If the two-generation quantity again tends to one, determine whether this is caused by the same `d/q` scale separation or by a new mechanism. If it stays bounded away from one, record the compensating post-birth mechanism precisely.

## Anti-circularity requirement

The output must include reinfection and at least two generations. The following do not count:

- another first-child calculation;
- freezing the parent after child birth;
- assuming the child cannot be reinfected;
- another marginal zero / no-`11` estimate;
- a finite-state representation with no hitting-probability or drift conclusion.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/004-two-generation-episode.md`

with supporting verifier/certificate code beside it if useful.

End with one of:

- `two-generation regeneration proved with restart state: ...`;
- `two-generation contraction proved but composition remains at: ...`;
- `live-episode route fails at two generations because: ...`;
- `new finite-state renewal mechanism found: ...`;
- `unresolved after substantive work; exact blocker: ...`.
