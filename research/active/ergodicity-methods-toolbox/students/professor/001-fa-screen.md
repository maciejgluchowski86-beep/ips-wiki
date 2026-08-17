# Professor FA-SCREEN-001: two-sided causal screen, leakage first

Date: 2026-08-17

## Status

`STOP-SCALING-OBSTRUCTION`

The pre-registered finite graphical leakage/measurability gate was run before any spectral-gap estimate. The literal East distinguished-vacancy transfer fails locally. A killed vacancy/dimer boundary primitive can be made faithful, but every exterior-measurable width-at-most-three vacancy automaton has a uniform positive hazard of either losing its causal certificate or requiring a protected future mark. Consequently a fixed endpoint has an exponential age tail, and searching over `o(s_t)` (indeed `O(s_t)`) candidate endpoints cannot produce the `s_t -> infinity` final fresh relaxation window required by the registered `FA-SCREEN` bridge.

No equilibrium spectral-gap calculation was used.

## 1. Registered target

For a fixed local observation interval `A`, `FA-SCREEN` asked for `s_t -> infinity`, events `E_t`, times `tau_t<=t-s_t`, final finite intervals `I_t superset A`, and screen data `S_t` such that:

1. `P(E_t^c)->0`;
2. `|I_t|=o(s_t)` on success;
3. `E_t,S_t` are determined without revealing future graphical marks in `I_t x (tau_t,t]` which will drive relaxation;
4. conditional on the past and `S_t`, those interior marks are fresh and exterior influence enters only through boundary data compatible with finite-volume FA relaxation;
5. only after 1--4, the conditional law at `tau_t` may pay an `exp(C_q|I_t|)` `L^2` cost and the known positive finite-volume gap may be used.

Assignment `assignment-001-fa-screen.md` pre-registered leakage/measurability as the first gate and prohibited moving to the gap before it closed.

## 2. Exact one-ring leak of a single distinguished vacancy

Let site `0` be protected, site `1` the proposed right boundary vacancy, and site `2` exterior. At a site-1 ring, with protected neighbour `l`, current spin `x`, right neighbour `r`, and refresh coin `z`,

$$
U(l,x,r;z)=
\begin{cases}
z,&l=0\text{ or }r=0,\\
x,&l=r=1.
\end{cases}
$$

For the same screen-side data

$$
x=0,\qquad r=1,\qquad z=1,
$$

one has

$$
U(0,0,1;1)=1,
\qquad
U(1,0,1;1)=0.
$$

Thus the future path of the proposed distinguished vacancy is not measurable from the unscreened side: exactly the East property used by the source theorem is absent.

The complete one-ring truth table shows protected-side dependence iff

$$
r=1\quad\text{and}\quad z\ne x.
\tag{2.1}
$$

These are the two dangerous contexts `(x,r,z)=(0,1,1)` and `(1,1,0)`.

Checkpoint: `001a-fa-screen-local-leakage.md`; verifier `001a-fa-screen-local-leakage-verifier.py`.

## 3. Dimer: faithful only as a killed primitive

An adjacent `00` boundary dimer does remove the immediate dependence, but an outer refresh-to-1 is legal because the inner site is vacant and sends

$$
00\longrightarrow01
$$

without using protected information. The next inner refresh-to-1 is then the dangerous context (2.1). Therefore a failure-free dimer also leaks.

A dimer can remain **faithful** by declaring failure before/at every dangerous mark using only screen-side information. This is enough to pass the local measurability gate as a killed primitive, so the assignment did not stop at `STOP-LOCAL-SCREEN`; the next issue is whether such a killed primitive can live/hand off long enough.

## 4. Decisive width-three hazard

The final load-bearing argument is `001c-fa-screen-width3-scaling-obstruction.md` and its verifier `001b2-fa-screen-width3-hazard-verifier.py`.

A width-at-most-three vacancy screen is active when it certifies, from exterior-side data, at least one vacancy among sites `1,2,3`. This includes every single-vacancy/dimer finite automaton authorized by the assignment. There are seven active spin states.

From **every** active state, there is a four-unit exterior-only event using sites `1,2,3` which does the following:

1. by the end of phase 3 it reaches
   $$
   (\eta_1,\eta_2)=(0,1),
   $$
   with no site-1 ring during the whole third phase;
2. therefore site `0` is legal throughout phase 3, and its unrevealed rate-one refresh marks can leave it either `0` or `1` with positive conditional probability;
3. phase 4 contains a site-1 refresh-to-1 while `(eta_1,eta_2)=(0,1)`.

The phase-4 output is

$$
1\quad\text{if }\eta_0=0,
\qquad
0\quad\text{if }\eta_0=1.
$$

Hence, conditional on the same complete exterior screen history, the adjacent boundary trajectory depends on a protected future mark. A faithful exterior-measurable screen must fail or cease using that endpoint.

The prescribed pre-final rings are all legal from certified **exterior** vacancies. The verifier checks all seven active width-three states exhaustively.

## 5. Uniform hazard and exponential age tail

Each of the four phases specifies either no rings on sites `1,2,3`, or exactly one ring at one prescribed site and no rings at the other two. Thus the Poisson factor is `e^{-12}`. With `p=1-q`, the worst coin product is `q^2p^2`, giving

$$
\boxed{
\delta_3(q)=e^{-12}q^2(1-q)^2>0.
}
\tag{5.1}
$$

For every active screen state, conditional on all past allowed screen information,

$$
P(\text{forced protected-mark dependence in next 4 units})\ge\delta_3(q).
$$

Therefore the lifetime `T` of a fixed active endpoint satisfies

$$
\boxed{
P(T>4n)\le(1-\delta_3(q))^n.
}
\tag{5.2}
$$

No independence of screen states is assumed; this is a uniform conditional hazard plus independent graphical increments.

At `q=1/10`, exact rational bounds give

$$
e^{-12}>\frac1{200000},
\qquad
\boxed{
\delta_3(1/10)>\frac{81}{2000000000}.
}
\tag{5.3}
$$

The numerical size is irrelevant; strict positivity is enough.

### Correction to an intermediate checkpoint

The earlier note `001b-fa-screen-fixed-boundary-scaling.md` used a convenient two-site forcing sequence from all four pairs `(eta_1,eta_2)`, including `11`. The final proof does **not** rely on treating `11` as automatically dangerous: if the protected endpoint were already known occupied and frozen, that would be too strong. Checkpoint 001c fixes this by restricting to the actual active vacancy-screen states and by inserting a full phase with `eta_1=0`, which creates genuine hidden protected-side randomness before the dangerous mark. The final status relies on 001c, not on the overbroad reading of 001b.

## 6. Why handoff before the final gap stage does not cure the age obstruction

The local automaton is free to die, restart, or hand off while it searches for a final screen. But the registered bridge fixes a final interval `I_t` and requires all future marks in

$$
I_t\times(\tau_t,t]
$$

to remain unrevealed by the screen, with `t-\tau_t>=s_t`.

If after `tau_t` an outward handoff is triggered by a clock/coin at a site subsequently absorbed into the final `I_t`, that mark has been used to choose the screen but is now a forbidden protected future mark. An endpoint change also destroys the advertised `s_t`-long fixed finite-volume relaxation stage unless `tau_t` is restarted after the last change.

Thus earlier handoffs may be used to **search**, but the selected final endpoint must have valid age at least `s_t`. Equation (5.2) controls exactly that age.

This is the place where the present result is deliberately narrower than a hypothetical new theorem for a genuinely moving/adaptive boundary with its own relaxation estimate.

## 7. Spatial search cannot compensate

Because `I_t` contains fixed `A` and has sublinear width, there are at most `O(s_t)` possible right endpoints, and under the stated condition actually `o(s_t)`.

For every fixed endpoint,

$$
P(\text{valid final age }s_t)
\le
(1-\delta_3(q))^{\lfloor s_t/4\rfloor}.
$$

Even if the algorithm selects the best endpoint after inspecting all permitted exterior data, a union bound gives

$$
\boxed{
P(\exists\text{ admissible right endpoint of age }s_t)
\le
C s_t(1-\delta_3(q))^{\lfloor s_t/4\rfloor}
\longrightarrow0.
}
\tag{7.1}
$$

A two-sided bracket is no easier. Thus conditions 1--4 cannot be supplied by this screen family while `s_t->infinity` and `|I_t|=o(s_t)`.

## 8. Ruling and exact scope

The assignment therefore ends

> **`STOP-SCALING-OBSTRUCTION`.**

Stopped:

> the fixed-final-interval `FA-SCREEN` bridge built from exterior-measurable single-vacancy/dimer finite boundary automata of width at most three, with the exact protected-future freshness demanded by conditions 3--4.

Not stopped:

- every conceivable causal-screen theorem for FA-1f;
- a materially different moving-boundary relaxation theorem whose conditioning does not consume marks later declared protected;
- the independent reserve architecture of quench-specific state-adaptive information histories.

The latter two are new architectures and are not authorized as enlargements inside FA-SCREEN-001.

## 9. Strategic consequence

The finite graphical leakage gate did its intended job. The problem is not lack of a better equilibrium estimate: the proposed physical regeneration boundary loses freshness at a positive local hazard before the spectral gap becomes relevant.

The only other toolbox architecture which survived hostile review independently is `FA-INFO`, a state-adaptive causal reveal process. It does not require a long-lived exterior-measurable vacancy boundary and is therefore not refuted by the present argument. Any continuation should be a separately pre-registered bounded decision-tree test of that object, not a wider dimer/marker automaton.
