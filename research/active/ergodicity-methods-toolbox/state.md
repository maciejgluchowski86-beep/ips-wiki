# Programme state

## Direction

Title: post-toolbox FA-1f / positive-rates research state

Branch: `research/ergodicity-methods-toolbox`

Workspace: `research/active/ergodicity-methods-toolbox/`

Latest meeting: `meetings/025-fa-info-no-iterable-state-and-fa-quench-stop.md`, `state_narrowed: yes`.

The 74-method ergodicity toolbox collection and applicability assessment remain complete and frozen. `proof-spine.md` is now the **live problem-specific research spine**, not the frozen 74-method coverage map; the frozen inventory is audited through the 74 method pages, assessment files, validator, and earlier meeting history.

No `docs/` file or `mkdocs.yml` change is authorized by this research work.

## Current programme-level status

There is presently **no credible active proof architecture** in either of the two recently tested targets.

### Positive rates

The direct branch `research/positive-rates-conjecture` remains at `no-credible-route` for the present group. Its bounded restart set is exhausted:

1. uniform negative additive-Hamming drift is impossible at the hard point for every Markovian coupling;
2. mark-only deterministic-Boolean information percolation has a decomposition-independent pair-intersection obstruction;
3. ordinary and checkerboard Gray scalar/two-type splice closure are locally obstructed;
4. the principal-directed zero-boundary distinguished-zero transfer reduces to the old tail-shift defect.

Meeting 030's signed boundary-transmission restart bar remains operative. No positive-rates architecture is active.

### FA-1f Bernoulli quench

Target:

> For one-dimensional hard FA-1f with equilibrium vacancy density `q in (0,1)`, prove local convergence from every nondegenerate homogeneous Bernoulli initial law `mu_{q0}`, `q0>0`, to `mu_q`.

The hostile toolbox review retained two independent A/B architectures. Both have now failed their pre-registered first bounded gates:

1. `FA-SCREEN-001` — `STOP-SCALING-OBSTRUCTION` for the fixed-final-interval exterior-measurable vacancy-boundary implementation;
2. `FA-INFO-002` — `STOP-NO-ITERABLE-STATE` for the bounded state-adaptive likelihood/pair implementation.

Accordingly the FA quench also returns to **`no-credible-route` for the present group**. This is an expected-value judgment, not an impossibility theorem.

## FA-SCREEN-001 retained result

A literal distinguished vacancy is not an FA causal boundary. For a boundary ring, protected-side dependence occurs exactly when the exterior neighbour is occupied and the refresh coin differs from the boundary spin.

The decisive width-three theorem shows that every authorized active exterior-measurable vacancy/dimer endpoint has a uniform four-unit leakage/failure hazard

$$
\delta_3(q)=e^{-12}q^2(1-q)^2>0.
$$

Hence

$$
P(T>4n)\le(1-\delta_3(q))^n.
$$

At `q=1/10`, the exact verifier gives

$$
\delta_3(1/10)>\frac{81}{2000000000}.
$$

Even `O(s_t)` candidate endpoints cannot supply an `s_t -> infinity` fixed fresh relaxation interval. The obstruction is upstream of the known positive FA spectral gap.

Decisive files:

- `students/professor/001c-fa-screen-width3-scaling-obstruction.md`, commit `8076b527`;
- verifier `001b2-fa-screen-width3-hazard-verifier.py`, commit `71bef127`;
- Meeting 024.

Scope: not every imaginable moving/adaptive boundary theorem is ruled out. Do not enlarge the stopped marker automaton without a new bridge.

## FA-INFO-002 retained mathematics

Assignment stop rule was frozen before mathematics at commit `ef3dfcfe`.

### Exact adaptive transcript likelihood

For a predictable value-adaptive transcript

$$
Q=(i_1,b_1,\ldots,i_K,b_K),
$$

with repeated time-zero coordinates cached,

$$
\boxed{
L(Q)=
\prod_{j=1}^{K}
\left(\frac{q_0}{q}\right)^{1-b_j}
\left(\frac{1-q_0}{1-q}\right)^{b_j}.}
$$

The next query index is predictable from graphical marks and previously revealed bits, so it contributes no likelihood factor. The final random query set alone is not sufficient because set membership is value-biased.

For one terminal output `Y`, an exact two-copy identity is

$$
1+\chi^2(\Law_{q_0}(Y),\Law_q(Y))
=E\left[
L(Q)L(Q')\frac{\mathbf1_{\{Y=Y'\}}}{P_q(Y)}
\right].
$$

### Adaptive pruning is real

At `q=1/10`, a fixed-coin one-ring FA map has all three predecessors globally essential, but the optimal exact adaptive evaluator uses only

$$
\frac{671}{500}
$$

bottom queries on average.

Thus FA-INFO is not stopped because adaptivity fails to prune.

### Raw transcript pair cost fails

Let

$$
\mathcal C_0
=\frac{(q_0-q)^2}{q(1-q)}.
$$

For the one-ring circuit S1, exhaustive dynamic programming over every exact predictable decision tree gives

$$
\frac{\mathcal C_1}{\mathcal C_0}
=\frac{807341}{648000}>1
\quad(q_0=1/20),
$$

and

$$
\frac{\mathcal C_1}{\mathcal C_0}
=\frac{17594}{10125}>1
\quad(q_0=1/5).
$$

So the exact positive transcript likelihood state is noncontractive already at S1.

### Fully averaged output cancels, but does not close

With vacancy indicators `V_j`, one equilibrium-coin ring satisfies

$$
E[V_0'\mid V_{-1},V_0,V_1]
=q+(V_0-q)(1-V_{-1})(1-V_1).
$$

For product input `q_0`, the exact one-site output chi-square contracts by factor `(1-q_0)^4`.

However the first adjacent composition S2 increases the sharp scalar statistic relative to S1 at both registered quenches:

$$
\frac{\mathcal X_2}{\mathcal X_1}
=\frac{15689521}{14440000}>1
\quad(q_0=1/20),
$$

$$
\frac{\mathcal X_2}{\mathcal X_1}
=\frac{58081}{40000}>1
\quad(q_0=1/5).
$$

### Shared-mark pair state also fails

For the same graphical block marks `W`, define

$$
\mathcal B
=E_W\left[
\left(E_{q_0}[\phi(Y)\mid W]-E_q[\phi(Y)\mid W]\right)^2
\right].
$$

This has the exact same-history two-copy representation

$$
\mathcal B
=E[(L(Q)-1)(L(Q')-1)\phi(Y)\phi(Y')].
$$

At `q_0=1/20`, `B_1/C_0=35921/32000>1`; moreover `B_2/B_1>1` for both registered quenches.

Thus conditioning on enough graphical information for local block composition loses the cancellation recovered by full averaging.

### Exact growing-correlation theorem

For a right-to-left staircase of `m` adjacent equilibrium-coin rings at sites `m-1,...,0`, with conditional mean vacancies

$$
M_m=V_m,
$$

$$
M_k=q+(V_k-q)(1-V_{k-1})(1-M_{k+1}),
$$

the coefficient of

$$
\prod_{j=-1}^{m}(V_j-q)
$$

in `M_0-q` is exactly

$$
\boxed{(-q)^{m-1}\ne0.}
$$

Thus exact adjacent composition creates genuinely new correlation order at every step. At S2, even two input laws with identical every proper marginal can have different terminal output.

### FA-INFO stop

The bounded test therefore separates:

- transcript/shared-history states: compositional enough, but noncontractive;
- fully averaged output state: contractive from the product input, but structurally nonclosed;
- exact repair: enlarging transcript/correlation hierarchy.

This is `STOP-NO-ITERABLE-STATE` under the frozen assignment. Do not respond by running a third block, increasing radius, or carrying the growing hierarchy.

Decisive files:

- `students/professor/002a-fa-info-adaptive-likelihood.md`, commit `ae910cd9`;
- `002b-fa-info-finite-circuit-closure.md`, commit `c5113b6e`;
- `002c-fa-info-shared-mark-pair.md`, commit `4d76c8c0`;
- final verifier `002-fa-info-finite-circuit-verifier.py`, commit `5bcf597c`;
- report `002-fa-info.md`, commit `e63191d7`;
- handoff `002-fa-info-handoff.md`, commit `db0ecdc7`;
- Meeting 025.

## Next-action status

There is **no automatic next research assignment** from the two stopped FA interfaces or the stopped positive-rates interfaces.

A future restart in either problem requires a materially new upstream theorem or architecture with its own bounded falsification test, not a larger instance of the stopped state spaces.

The next Professor action, when research resumes, should be a target-selection/opportunity-cost review rather than another variant of FA-SCREEN, FA-INFO, Gray, Hamming coupling, mark-only percolation, or the stopped positive-rates signed routes.

## Personnel and hygiene

The Professor remains the only operational executing session at this record. Student G is unavailable for input; Student F's prior assignment remains unexecuted/unavailable.

The frozen toolbox remains 74 source-audited methods. No research result here changes public wiki files or `mkdocs.yml`.
