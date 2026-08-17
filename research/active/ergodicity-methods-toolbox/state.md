# Programme state

## Direction

Title: FA-1f Bernoulli-quench method tests after the frozen ergodicity toolbox audit

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

The 74-method toolbox collection and applicability assessment remain complete and frozen. The research loop is now using the two FA-1f architectures which survived hostile review.

Latest meeting: `meetings/024-fa-screen-vacancy-boundary-scaling-obstruction.md`, `state_narrowed: yes`.

No public toolbox entry, `docs/` file, or `mkdocs.yml` change is authorized by this research work.

## Frozen inventory

The inventory remains **74 source-audited live methods**. The previously verified structural/publication gates remain unchanged: validator 74/74 with zero failures, strict site build clean, public-doc additions-only gate clean, and control/format scan clean as reported by the orchestrator.

No further breadth collection or taxonomy work is active.

## Positive-rates bounded set: closed

The direct positive-rates branch `research/positive-rates-conjecture` has returned to `no-credible-route` for the present group. Meeting 034 there records that all bounded toolbox-derived PASS tests failed in their registered direct forms:

1. uniform negative additive-Hamming drift is impossible at the hard point for **every** Markovian coupling;
2. optimized mark-only Boolean-map information percolation has a decomposition-independent nondecaying pair-intersection lower bound;
3. both ordinary and checkerboard Gray scalar/two-type splice closures are locally incompatible with the hard-point rates;
4. the principal-directed `pi_N` distinguished-zero transfer stopped at the old tail-shift defect.

Meeting 030's signed boundary-transmission restart bar remains in force. No positive-rates proof architecture is active, and larger edge states, state-adaptive positive-rates histories, generic coupling/norm engineering, common-coupling occupation, tail shift, Bellman/Foster, reversible/filter variants and longer coefficient searches are not automatically reopened.

## FA-1f target

Current scientific target:

> For one-dimensional hard FA-1f with equilibrium vacancy density `q in (0,1)`, prove local convergence from every nondegenerate homogeneous Bernoulli initial law `mu_{q0}`, `q0>0`, to the Bernoulli equilibrium law `mu_q`.

The earlier published high-vacancy theorem and known positive equilibrium gap are background. The unresolved regime is the all-density Bernoulli quench. Worst-case convergence is impossible because all ones is absorbing.

The hostile review retained two independent architectures:

1. `FA-SCREEN`: an East-inspired two-sided physical causal screen;
2. `FA-INFO`: a quench-specific state-adaptive causal information history.

## FA-SCREEN-001: stopped as `STOP-SCALING-OBSTRUCTION`

Assignment:

`students/professor/assignment-001-fa-screen.md`, commit `64535479`.

Final report:

`students/professor/001-fa-screen.md`, commit `f3650cd5`.

Handoff:

`students/professor/001-fa-screen-handoff.md`, commit `a271ea7e`.

### Local leakage

A literal distinguished vacancy fails in one ring. If site `0` is protected and site `1` is the proposed boundary, a site-1 ring depends on the protected neighbour exactly when its right neighbour is occupied and the refresh coin differs from the current boundary spin.

An adjacent `00` dimer can postpone this: an exterior refresh sends `00 -> 01` without protected information. The next inner refresh-to-1 is dangerous. Thus a dimer is faithful only as a **killed** boundary primitive which declares failure before protected-side legality is needed.

### Width-three hazard theorem

The decisive checkpoint is

`students/professor/001c-fa-screen-width3-scaling-obstruction.md`, commit `8076b527`,

with exact finite verifier

`001b2-fa-screen-width3-hazard-verifier.py`, commit `71bef127`.

For every active width-at-most-three exterior-measurable vacancy state, there is a four-unit event using only the first three exterior sites which first holds the adjacent boundary site vacant for a whole phase, allowing hidden protected refreshes to make the protected endpoint take either spin value, and then applies a dangerous boundary refresh. Its probability is at least

$$
\delta_3(q)=e^{-12}q^2(1-q)^2>0.
$$

Therefore a fixed active endpoint has exponential age tail

$$
P(T>4n)\le(1-\delta_3(q))^n.
$$

At `q=1/10`, the verifier gives the exact rational lower bound

$$
\delta_3(1/10)>\frac{81}{2000000000}.
$$

### Scaling consequence

The registered `FA-SCREEN` bridge fixes a final interval `I_t` and demands that all marks in `I_t x (tau_t,t]` remain unrevealed by the screen while `t-tau_t>=s_t`. Searches/handoffs may occur before `tau_t`, but the chosen final endpoint must have valid age at least `s_t`.

Even allowing `C s_t` candidate endpoints,

$$
P(\exists\text{ valid endpoint of age }s_t)
\le C s_t(1-\delta_3(q))^{\lfloor s_t/4\rfloor}
\to0.
$$

Hence the fixed-final-interval screen built from exterior-measurable single-vacancy/dimer finite boundary automata cannot simultaneously have `s_t->infinity`, sublinear width, exact protected-future freshness, and success probability tending to one.

The positive FA spectral gap is never reached; the obstruction is upstream.

### Scope boundary

Not ruled out:

- every imaginable FA causal screen;
- a materially different moving/adaptive-boundary relaxation theorem whose conditioning does not consume marks later declared protected;
- `FA-INFO`.

Do not respond by merely enlarging the vacancy-marker automaton to more sites/phases.

## Queued next architecture: FA-INFO

`FA-INFO` is the only independent PASS architecture remaining from the FA hostile review. It tracks the **minimal causal information revealed under the Bernoulli quench**, allowing short-circuit evaluation of the facilitation OR: once one neighbour is revealed vacant, the other neighbour need not be revealed merely to establish legality.

It is not the conservative centered dual and is not a mark-only ancestor process. A Miller--Peres/Ising theorem cannot simply be quoted; the required second-moment or likelihood comparison must be derived for the actual adaptive reveal rule.

Meeting 024 authorizes only the already-specified bounded first experiment: an exact one/two-block adaptive decision-tree test with a pair-level information statistic and an anti-circularity check. This is not yet a full proof-program reopening.

## Personnel and durability

The Professor is currently the only operational executing session. Student G's session is unavailable for input; Student F's prior assignment remains unexecuted/unavailable. Durable assignments/checkpoints are therefore mandatory before and during substantial work.

## Anti-loop conclusions

- equilibrium gap/entropy work is downstream and must not replace a quench-memory theorem;
- no exogenous boundary facilitation signal may substitute for the actual FA boundary;
- no wider vacancy-marker hierarchy follows automatically from `FA-SCREEN-001`;
- state-adaptive histories must be proved for their actual reveal algorithm, not identified with the conservative transformed dual;
- product-background disagreement probabilities are not iteratable under path conditioning without an independent screen/reveal theorem;
- the all-ones trap forbids any claimed full-state worst-case mixing theorem.
