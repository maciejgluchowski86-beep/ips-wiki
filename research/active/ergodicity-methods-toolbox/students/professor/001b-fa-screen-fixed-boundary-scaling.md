# FA-SCREEN-001b: fixed-boundary causal screens have an exponential survival obstruction

Date: 2026-08-17

## Scope

This note concerns the local screen class pre-registered in `assignment-001-fa-screen.md`: a right boundary primitive whose state is determined from boundary/exterior spins and graphical marks, while protected future interior marks are not revealed. The single-vacancy and dimer rules in 001a are the first examples. A finite boundary automaton of width at most three may remember additional exterior-side state, but it may not decide a transition by consulting a protected future clock/coin or the protected-side legality of a boundary ring.

The conclusion is **not** that every conceivable FA screening theorem is impossible. It is an obstruction to the fixed-final-interval/exterior-measurable boundary implementation of `FA-SCREEN` which was the first-priority bridge in the toolbox synthesis.

## 1. Boundary sensitivity

Let site `0` be protected and site `1` the adjacent exterior boundary site. Couple two possible protected continuations by using identical graphical marks on sites `1,2,...`, but fix the protected neighbour seen by site `1` to `0` in one continuation and `1` in the other until the first boundary discrepancy.

As long as site `1` has not differed, the two exterior evolutions agree. At a site-1 ring with pre-ring state `x=eta_1`, right neighbour `r=eta_2`, and refresh coin `z`, the two outputs differ exactly when

$$
r=1,\qquad z\ne x.
\tag{1.1}
$$

This is the exact dangerous-mark criterion from 001a.

For an exterior-measurable screen, a ring of type (1.1) cannot be classified using the hidden protected neighbour. Therefore, unless the protected endpoint has already been moved so that site `1` is no longer the adjacent exterior site, the screen must declare failure before/at such a mark if it is to retain a boundary datum independent of protected future marks.

## 2. Uniform three-unit forcing event

The dangerous situation can be forced from every common pair `(eta_1,eta_2)` using only clocks/coins at sites `1,2`. Divide a three-unit block into three unit phases.

### Case `eta_2=1`

Require no rings at sites `1,2` in the first two phases. In the third phase require exactly one ring at site `1`, no ring at site `2`, and coin `1-eta_1`. This is a dangerous mark.

### Case `(eta_1,eta_2)=(0,0)`

Require an idle first phase. In phase two require exactly one site-2 ring, no site-1 ring, with coin `1`; it is legal because site `1` is vacant and gives `eta_2=1`. In phase three require exactly one site-1 ring, no site-2 ring, with coin `1`. This is dangerous.

### Case `(eta_1,eta_2)=(1,0)`

In phase one require exactly one site-1 ring, no site-2 ring, with coin `0`; it is legal because site `2` is vacant, so the common state becomes `(0,0)`. Then use the preceding two phases: site 2 refreshes to `1`, followed by the dangerous site-1 refresh to `1`.

Every specified one-ring/no-ring phase has Poisson factor `e^{-2}`. Writing `p=1-q`, the least coin factor over the three cases is `q p^2`. Thus, conditional on every pre-block exterior state and on no earlier failure,

$$
\boxed{
\Pr(\text{danger forced during next 3 units}\mid\mathcal F)
\ge \delta(q):=e^{-6}q(1-q)^2>0.
}
\tag{2.1}
$$

No assumption on site `3` or the farther exterior is used: whenever site `2` is updated in the forcing sequence, site `1=0` already makes that update legal.

The exact truth-table/state check is in `001b-fa-screen-fixed-boundary-scaling-verifier.py`.

## 3. Exponential survival tail

Let `T` be the lifetime of any exterior-measurable fixed-endpoint screen which declares failure whenever the next boundary event would require the protected neighbour to determine the boundary trajectory. Apply (2.1) at times `0,3,6,...` and use the strong Markov/independent-increments property of the graphical construction. No independence of the screen states is required; only the uniform conditional lower bound is used. Then

$$
\boxed{
\Pr(T>3n)\le (1-\delta(q))^n.
}
\tag{3.1}
$$

At the stress value `q=1/10`, the verifier supplies the fully rational bound

$$
e^{-6}>\frac1{500},
\qquad
\delta(1/10)>\frac{81}{500000}.
\tag{3.2}
$$

Hence the lifetime has an explicit exponential tail already at one target density in the all-density problem.

## 4. Why outward handoff does not repair the final relaxation window

The `FA-SCREEN` bridge fixes a final random interval `I_t` and requires `E_t,S_t` to be determined **without revealing any protected future marks in**

$$
I_t\times(\tau_t,t],
$$

with `t-\tau_t>=s_t`.

A search or sequence of handoffs may occur **before** `tau_t`. But if after `tau_t` a boundary site is absorbed into the final protected interval because of a clock/coin at that site, that clock/coin is now a protected interior mark used to determine the screen, contradicting the registered freshness condition. A predetermined outward expansion independent of such marks is not an implementation of the local vacancy/dimer handoff, and in any case would make the final protected width grow by the prescribed displacement.

Therefore, for the finite local automata tested here, the final `s_t`-long relaxation stage must contain an `s_t`-long interval during which each selected endpoint is fixed and its exterior boundary datum remains protected-independent. Equation (3.1) applies to that final stage regardless of how many failed candidates were explored earlier.

## 5. Spatial search cannot compensate under sublinear width

Suppose `A` is fixed and on screen success the final interval satisfies `|I_t|<=m_t`, where `m_t=o(s_t)`. Every possible right endpoint is then within `O(m_t)` lattice sites of `A`. For each fixed endpoint, (3.1) bounds the probability that its exterior-measurable boundary primitive survives the final `s_t` units by

$$
(1-\delta(q))^{\lfloor s_t/3\rfloor}.
$$

Allowing the construction to choose the best endpoint after inspecting all admissible **exterior** screen data only multiplies this by the number of candidate endpoints. Thus

$$
\Pr(\text{some admissible right endpoint survives }s_t)
\le C(1+m_t)(1-\delta(q))^{\lfloor s_t/3\rfloor}
\longrightarrow0.
\tag{5.1}
$$

The conclusion remains true with any polynomial number of candidate endpoints; the `o(s_t)` requirement is more than enough. A two-sided bracket is no easier, since success requires at least one viable endpoint on each side.

If `|I_t|/s_t->0` is only asserted on `E_t` rather than through a deterministic `m_t`, fix any `epsilon>0`. For all sufficiently large `t`, the portion of `E_t` with `|I_t|<=epsilon s_t` is the relevant asymptotic screen event; the same union bound has only `O(s_t)` candidate endpoints and still tends to zero exponentially.

## 6. Consequence for the registered bridge

For every `q in (0,1)`, and in particular for `q=1/10`, no fixed-final-interval screen assembled from the authorized exterior-measurable single-vacancy/dimer finite boundary primitives can satisfy simultaneously

- a fresh relaxation window `s_t->infinity`;
- protected future-mark measurability as in conditions 3--4;
- sublinear final width;
- and screen probability tending to one.

This is the `STOP-SCALING-OBSTRUCTION` case of the pre-registered assignment.

The obstruction occurs **upstream of the spectral gap**. No finite-volume FA relaxation estimate is used.

## 7. What is not ruled out

A future reopening would require a materially different object, for example:

1. a relaxation theorem for a genuinely moving/adaptive boundary which does not condition on marks later counted as protected interior marks; or
2. the reserve quench-specific adaptive information-history architecture, in which protected causal information is revealed selectively rather than insisting on an exterior-measurable regeneration boundary.

Neither is a continuation of the present finite boundary automaton, so the assignment's stop rule forbids escalating to them inside this block.
