# Meeting 024: FA vacancy-boundary screen stops at a local age obstruction

Date: 2026-08-17

`state_narrowed: yes`.

## Inputs

The Professor executed the first FA Bernoulli-quench block because no graduate-student session was operational. The assignment was committed before work began:

- `students/professor/assignment-001-fa-screen.md`, commit `64535479`.

Durable checkpoints:

- literal marker/dimer leakage, `001a-fa-screen-local-leakage.md`, commit `12447442`;
- exact one-ring verifier, commit `0a8fcef9`;
- intermediate fixed-boundary scaling note `001b-fa-screen-fixed-boundary-scaling.md`, commit `75480249`;
- corrected decisive width-three theorem `001c-fa-screen-width3-scaling-obstruction.md`, commit `8076b527`;
- decisive width-three verifier `001b2-fa-screen-width3-hazard-verifier.py`, commit `71bef127`;
- final report `001-fa-screen.md`, commit `f3650cd5`;
- handoff `001-fa-screen-handoff.md`, commit `a271ea7e`.

The earlier positive-rates lane is closed at its bounded restart tests by direct-programme Meeting 034 on branch `research/positive-rates-conjecture`. No positive-rates architecture is active.

## Ruling

**FA-SCREEN-001 ends `STOP-SCALING-OBSTRUCTION`.**

The literal East distinguished-vacancy mechanism fails FA's two-sided legality test in one ring. A dimer can be made locally faithful only by becoming a killed screen. More generally, every authorized exterior-measurable width-at-most-three vacancy/dimer boundary automaton has a uniform positive local hazard of either failure or protected-future leakage. The resulting endpoint age is exponentially tailed, so sublinearly many spatial candidates cannot supply the `s_t -> infinity` final fresh interval required by the registered fixed-final-interval `FA-SCREEN` bridge.

The obstruction is upstream of equilibrium relaxation; the positive FA spectral gap is not used.

This is **not** a theorem against every possible FA causal screen. A genuinely moving/adaptive-boundary relaxation theorem would be a new architecture, not a continuation of the stopped finite boundary automaton.

## 1. Exact single-marker leakage

With site `0` protected and site `1` the proposed boundary, a ring at site `1` has output

$$
U(l,x,r;z)=z
$$

when `l=0` or `r=0`, and otherwise leaves `x` unchanged.

For fixed screen-side data `(x,r,z)=(0,1,1)`,

$$
U(0,0,1;1)=1,
\qquad
U(1,0,1;1)=0.
$$

Thus the marker path is not measurable from the unscreened side. The full truth table gives protected dependence exactly when

$$
r=1,\qquad z\ne x.
$$

This is the local distinction from East which the hostile review demanded be tested before any tail estimate.

## 2. Dimer and the correct local primitive

An exterior `00` dimer can evolve to `01` by an outer refresh-to-1 which is legal independently of the protected side. The next inner refresh-to-1 is dangerous. Therefore a failure-free dimer leaks.

However the dimer may declare failure using only its exterior data at the dangerous mark. That produces a legitimate **killed** screen primitive, so the correct question is lifetime/scaling rather than local impossibility.

## 3. Width-three hazard theorem

The decisive proof restricts to the actual active vacancy-screen states: one of the first three exterior sites is certified vacant. There are seven states.

From each such state, an exterior-only four-phase event moves the first two exterior spins to `(0,1)` by the end of phase 3, with no site-1 ring in phase 3. Site `0` is therefore legal throughout that phase. Its protected refresh marks are hidden from the screen and can leave `eta_0` equal to either `0` or `1` with positive conditional probability.

A prescribed site-1 refresh-to-1 in phase 4 then has output depending on that hidden protected value. Thus the same complete exterior screen history has two positive-probability protected continuations with different boundary trajectories. A faithful exterior-measurable screen must fail or cease using that endpoint.

The forcing event has probability at least

$$
\boxed{
\delta_3(q)=e^{-12}q^2(1-q)^2>0.
}
$$

Therefore a fixed active endpoint has age tail

$$
\boxed{
P(T>4n)\le(1-\delta_3(q))^n.
}
$$

At `q=1/10`, exact rational bounds in the verifier give

$$
\delta_3(1/10)>\frac{81}{2000000000}.
$$

The smallness of the constant is irrelevant to the qualitative obstruction.

## 4. Intermediate-checkpoint correction

The earlier 001b note used a convenient two-site forcing sequence from all four exterior pairs, including `11`. That is broader than needed: an exterior `11` pair can be temporarily harmless if the protected endpoint is already known occupied and frozen.

The final 001c theorem removes this issue. It uses only active states containing a certified exterior vacancy and deliberately holds the adjacent exterior site vacant for an entire phase, so actual hidden protected refreshes create both possible endpoint values before the final dangerous mark. Meeting 024 relies on 001c, not on an overbroad reading of 001b.

## 5. Why search/handoff does not defeat the registered bridge

`FA-SCREEN` fixes a final interval `I_t` and requires all marks in

$$
I_t\times(\tau_t,t]
$$

to remain unrevealed by the screen while `t-\tau_t>=s_t`.

The screen may search and hand off before `tau_t`. But a post-`tau_t` handoff triggered by a mark at a site later absorbed into final `I_t` uses precisely a mark that the freshness condition declares protected. An endpoint change also means the standard fixed-volume relaxation stage begins only after the last change.

Hence the selected final endpoint must have valid age at least `s_t`.

Because `I_t` contains fixed `A` and has sublinear width, even allowing `C s_t` possible endpoints gives

$$
P(\exists\text{ valid endpoint of age }s_t)
\le
C s_t(1-\delta_3(q))^{\lfloor s_t/4\rfloor}
\to0.
$$

A two-sided bracket is no easier.

Thus the registered vacancy-boundary screen cannot have success probability tending to one.

## 6. Scope and anti-loop ruling

Stopped:

> the fixed-final-interval `FA-SCREEN` implementation built from exterior-measurable single-vacancy/dimer finite boundary automata of width at most three.

Not stopped:

- a materially different theorem for relaxation behind a genuinely moving/adaptive boundary;
- the independently surviving `FA-INFO` state-adaptive reveal architecture.

Do not respond to this failure by enlarging the marker automaton to width 4, 8, 16, adding front phases, or introducing an occupied-barrier hierarchy without a separately stated bridge. That would violate the pre-registered stop condition.

## 7. Direction judgment

The toolbox hostile review left two independent FA architectures. `FA-SCREEN` has now failed its first bounded gate in its registered fixed-final-interval vacancy-boundary implementation. The remaining PASS architecture is `FA-INFO`: a quench-specific adaptive reveal process which may prune a nominal neighbour once another revealed neighbour is known vacant.

This mechanism is genuinely different from the stopped screen because it does not require an exterior-measurable long-lived boundary. The final synthesis already specified a bounded first experiment: compute the exact minimal adaptive decision tree on one/two finite space-time blocks and test a two-copy information statistic, without identifying it with the conservative transformed dual or demanding mark-only ancestor extinction.

Therefore **FA-INFO becomes the queued next bounded experiment**, not a full proof-program reopening. It should receive its own durable assignment and stop rule before execution.

No `docs/` or `mkdocs.yml` files are changed by this meeting.
