# FA-SCREEN-001c: decisive width-three vacancy-screen scaling obstruction

Date: 2026-08-17

## Verdict of this checkpoint

The pre-registered single-vacancy/dimer-derived **exterior-measurable finite boundary screen** cannot supply the final `s_t -> infinity` fresh relaxation window required by `FA-SCREEN`, even if it is allowed every width-at-most-three vacancy state and may search over sublinearly many candidate endpoints before the relaxation window begins.

The obstruction is an exact local hazard. It is stronger and more carefully scoped than 001b: the load-bearing argument uses only **active screen states containing a certified vacancy** and does not assume that an exterior `11` state is itself dangerous.

## 1. Active vacancy screens

Fix a right endpoint of the protected interval and relabel it as site `0`. Sites `1,2,3` are on the screen/exterior side. A width-at-most-three screen state is called active when it certifies at least one vacancy among sites `1,2,3` using only screen-side data.

This covers the authorized family:

- a distinguished boundary vacancy;
- an adjacent-vacancy dimer;
- any finite automaton obtained from those by remembering the first three boundary/exterior spins and their graphical marks.

If such an exterior-measurable automaton loses every certified vacancy, it cannot certify an `11...1` state by passing through the final inner-vacancy fill: that fill is exactly a dangerous event whose legality can depend on site `0`. Thus continuing beyond loss of the last certified vacancy would already fail the 001a measurability gate. The faithful automaton must instead fail or change the protected endpoint.

## 2. Four-phase exterior forcing from every active width-three state

Write the current screen-side state as

$$
(x_1,x_2,x_3)\in\{0,1\}^3,
\qquad 0\in\{x_1,x_2,x_3\}.
$$

Use four consecutive unit phases. In every phase, require no rings at site `3`; require either no rings at sites `1,2` or exactly the single prescribed ring below. The prescriptions through phase 3 are:

1. if `(x_1,x_2)=(0,1)`: no prescribed ring in phases 1--3;
2. if `(x_1,x_2)=(0,0)`: only in phase 3, refresh site `2` to `1`;
3. if `(x_1,x_2)=(1,0)`: in phase 2 refresh site `1` to `0`, then in phase 3 refresh site `2` to `1`;
4. if `(x_1,x_2,x_3)=(1,1,0)`: in phase 1 refresh site `2` to `0`, in phase 2 refresh site `1` to `0`, then in phase 3 refresh site `2` to `1`.

Every pre-final refresh above is legal using a **screen-side vacancy**:

- site `2 -> 0` in case 4 is legal because `x_3=0`;
- site `1 -> 0` is used only when `x_2=0`;
- site `2 -> 1` is used only when `x_1=0`.

Thus none of these transitions consults site `0`.

At the end of phase 3, in every one of the seven active states,

$$
(x_1,x_2)=(0,1),
\tag{2.1}
$$

and site `1` has had **no ring throughout phase 3**. Consequently site `0` has a vacant right neighbour throughout phase 3 and is legal at every one of its own hidden rate-one rings.

Because the screen is forbidden to reveal site-0 future marks, conditional on the complete prescribed exterior history there are protected mark realizations of positive probability for which `eta_0` equals `0` at the end of phase 3 and others for which it equals `1`: for example, exactly one site-0 ring with refresh coin `0` or `1`, followed by no later site-0 ring.

In phase 4 require exactly one site-1 ring, no rings at sites `2,3`, and refresh coin `1`. Until this ring, site `1=0` and site `2=1`. Its output is therefore

$$
1\quad\text{if }\eta_0=0,
\qquad
0\quad\text{if }\eta_0=1.
\tag{2.2}
$$

Hence on the prescribed **exterior-only** event the adjacent boundary trajectory genuinely depends on an unrevealed protected future mark. A faithful exterior-measurable screen must declare failure (or cease using this endpoint) before the phase-4 mark.

This removes the possible objection that the protected endpoint may have had a known initial value. Phase 3 manufactures fresh hidden uncertainty at site `0` using the actual FA refresh rule.

## 3. Uniform positive hazard

Each unit phase specifies either no rings on sites `1,2,3`, or exactly one ring at one prescribed site and no rings at the other two. Its Poisson factor is `e^{-3}`. Across four phases the factor is `e^{-12}`.

Writing `p=1-q`, the worst coin product among the seven active initial states is `q^2p^2`, attained by the state `(1,1,0)`. Therefore, from every active width-three state,

$$
\boxed{
\Pr(\text{protected-mark dependence forced within 4 units}\mid\mathcal F)
\ge
\delta_3(q):=e^{-12}q^2(1-q)^2>0.
}
\tag{3.1}
$$

The finite state logic is exhaustively checked by `001b2-fa-screen-width3-hazard-verifier.py`.

For a fully rational stress bound take `q=1/10`. Since

$$
e<\frac{49}{18}<\frac{11}{4},
\qquad
\left(\frac{11}{4}\right)^{12}<200000,
$$

we obtain

$$
\boxed{
\delta_3(1/10)>
\frac{81}{2000000000}>0.
}
\tag{3.2}
$$

The size of this constant is irrelevant; strict positivity is enough.

## 4. Exponential lifetime of every faithful active endpoint

Let `T` be the time for which a fixed protected endpoint can be maintained by such an active exterior-measurable vacancy screen without failure. At the start of each four-unit block, either the screen has already failed/lost its certified vacancy, or it is in one of the seven active states. In the latter case (3.1) gives a uniform conditional probability at least `delta_3(q)` that the next block forces protected-mark dependence.

Thus

$$
\boxed{
\Pr(T>4n)\le(1-\delta_3(q))^n.
}
\tag{4.1}
$$

No independence of successive screen states is assumed; this is iteration of a uniform conditional hazard using independent graphical increments.

## 5. Why handoff cannot occur during the final `FA-SCREEN` relaxation window

The registered bridge chooses a final interval `I_t` and a time `tau_t<=t-s_t`, and requires the screen event/data to be determined without revealing protected future marks in

$$
I_t\times(\tau_t,t].
\tag{5.1}
$$

The vacancy automaton may search, die, restart, or hand off **before** `tau_t`. But an outward handoff after `tau_t` that is triggered by a clock/coin at a site subsequently absorbed into the final `I_t` uses a mark that (5.1) requires to remain unrevealed. An inward handoff does not give an `s_t`-long finite-volume relaxation interval after the last change; to use the downstream gap one must restart `tau_t` after the final endpoint change.

Therefore the final relaxation stage of this registered fixed-final-interval bridge requires an endpoint which survives without such a handoff for at least `s_t` time units. Earlier failed candidates do not help this final-age requirement.

This is exactly the feature which distinguishes the present `FA-SCREEN` bridge from a materially different theorem for an adaptively moving boundary.

## 6. Searching sublinearly many endpoints cannot beat the hazard

On screen success, `I_t` contains the fixed observation set `A` and has width `o(s_t)`. Hence the possible right endpoints lie in a spatial set of size `O(s_t)` and in fact `o(s_t)` under the registered width condition.

For each fixed endpoint, (4.1) gives

$$
\Pr(\text{endpoint has a valid final age }s_t)
\le
(1-\delta_3(q))^{\lfloor s_t/4\rfloor}.
$$

The endpoint may be chosen after examining all permitted exterior screen data; a union bound is still valid. Even allowing `C s_t` candidate endpoints gives

$$
\boxed{
\Pr(\exists\text{ admissible endpoint with age }s_t)
\le
C s_t(1-\delta_3(q))^{\lfloor s_t/4\rfloor}
\longrightarrow0.
}
\tag{6.1}
$$

A two-sided bracket is no easier because it requires both sides to survive.

Thus no spatial search compatible with `|I_t|=o(s_t)` can turn this local vacancy-screen primitive into a high-probability causal screen.

## 7. Pre-registered ruling

This is the assignment's **`STOP-SCALING-OBSTRUCTION`** outcome.

The obstruction is upstream of any spectral-gap argument. The known positive finite-volume FA gap is never invoked.

Precisely what is stopped is:

> the fixed-final-interval `FA-SCREEN` implementation built from exterior-measurable single-vacancy/dimer finite boundary automata of width at most three, with exact protected-future freshness as registered in conditions 3--4.

What is **not** proved:

- no theorem against every possible FA causal screen;
- no theorem against a genuinely moving-boundary relaxation estimate whose conditioning does not consume future marks later declared protected;
- no theorem against the independent reserve architecture of state-adaptive quench information histories.

Either of those would be a new architecture and requires a separate Professor direction ruling rather than an enlargement of this stopped boundary automaton.
