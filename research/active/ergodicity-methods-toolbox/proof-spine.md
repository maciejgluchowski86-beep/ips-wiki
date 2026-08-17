# Proof spine

This file is the **live problem-specific research spine** after completion of the 74-method toolbox assessment. It is no longer the frozen 74-method coverage map. The toolbox inventory itself remains frozen and auditable through the live method pages, assessment files, validator, and earlier meeting history.

## Main target

For one-dimensional hard FA-1f with equilibrium vacancy density

$$
q\in(0,1),
$$

and nondegenerate homogeneous Bernoulli initial vacancy density

$$
q_0>0,
$$

prove local convergence

$$
\mu_{q_0}P_t(f)\longrightarrow\mu_q(f)
$$

for every local function `f`.

The all-ones configuration is absorbing, so no route may require worst-case convergence over the full state space.

## E0. Current architecture status

The hostile toolbox review retained exactly two independent A/B architectures for this target:

1. `FA-SCREEN` — a two-sided East-inspired causal screen;
2. `FA-INFO` — a quench-specific state-adaptive causal-information history.

Both have now failed their pre-registered first bounded gates.

- Meeting 024: `FA-SCREEN-001` ends `STOP-SCALING-OBSTRUCTION` for the registered fixed-final-interval exterior-measurable vacancy-boundary implementation.
- Meeting 025: `FA-INFO-002` ends `STOP-NO-ITERABLE-STATE` for the registered bounded adaptive likelihood/pair implementation.

Therefore there is presently **no credible active FA proof architecture for the group**. This is an expected-value judgment, not an impossibility theorem for the target.

Do not automatically enlarge either stopped state space.

## E1. Downstream equilibrium relaxation is not the blocker

One-dimensional FA-1f has positive equilibrium coercivity for every `q>0` in the relevant ergodic component. A successful causal localization theorem could therefore use the known gap downstream.

Neither stopped bounded route reaches that stage. The obstruction remains nonequilibrium memory erasure.

## E2. FA-SCREEN local leakage theorem

At a proposed right boundary, let the protected neighbour be `l`, the boundary spin `x`, its exterior neighbour `r`, and the refresh coin `z`. The ring output is

$$
U(l,x,r;z)=
\begin{cases}
z,&l=0\text{ or }r=0,\\ x,&l=r=1.\end{cases}
$$

Protected-side dependence occurs exactly when

$$
\boxed{r=1,\qquad z\ne x.}
$$

Thus a literal East distinguished vacancy is not measurable from the unscreened side in FA-1f.

## E3. FA-SCREEN width-three age obstruction

For every active exterior-measurable vacancy/dimer boundary state of width at most three, an exterior-only four-unit event forces protected-future dependence with probability at least

$$
\boxed{\delta_3(q)=e^{-12}q^2(1-q)^2>0.}
$$

Hence a fixed endpoint has

$$
P(T>4n)\le(1-\delta_3(q))^n.
$$

At `q=1/10`, the exact verifier gives

$$
\delta_3(1/10)>\frac{81}{2000000000}.
$$

The registered final protected interval needs an endpoint of age at least `s_t`; even `O(s_t)` candidates cannot beat the exponential tail. Therefore the fixed-final-interval screen cannot have success probability tending to one while `s_t->infinity` and final width is sublinear.

This stops the registered marker implementation before any spectral-gap argument.

Decisive pointer: `students/professor/001c-fa-screen-width3-scaling-obstruction.md` and Meeting 024.

## E4. Exact adaptive transcript likelihood

FA-INFO uses an actual value-adaptive decision tree. At a ring with old-site value `X`, neighbours `L,R`, and refresh coin `z`,

$$
F_z(X,L,R)=
\begin{cases}
z,&L=0\text{ or }R=0,\\ X,&L=R=1.\end{cases}
$$

An exact evaluator may stop after revealing a vacancy in one neighbour, or immediately when `X=z`. Repeated time-zero coordinates are cached.

For transcript

$$
Q=(i_1,b_1,\ldots,i_K,b_K),
$$

with predictable next-index choice,

$$
\boxed{
L(Q)=
\prod_{j=1}^{K}
\left(\frac{q_0}{q}\right)^{1-b_j}
\left(\frac{1-q_0}{1-q}\right)^{b_j}.}
$$

Value-dependent querying therefore does **not** break the product likelihood ratio. But it does break any formula depending only on the final random query set: set membership is value-biased.

For one terminal output `Y`, the sharp exact two-copy identity is

$$
1+\chi^2(\Law_{q_0}(Y),\Law_q(Y))
=E\left[
L(Q)L(Q')\frac{\mathbf1_{\{Y=Y'\}}}{P_q(Y)}
\right].
$$

This exact likelihood theorem is retained independent of the stop decision.

## E5. Adaptive pruning is real but raw likelihood expands

At the registered stress density

$$
q=\frac1{10},
$$

a fixed-coin one-ring map has three globally essential predecessors, while the optimal adaptive evaluator uses only

$$
\boxed{\frac{671}{500}}
$$

queries on average.

Let

$$
\mathcal C_0=\frac{(q_0-q)^2}{q(1-q)}.
$$

Nevertheless the optimal exact raw transcript second moment gives

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

So the positive transcript likelihood is directly compositional but noncontractive.

## E6. Fully averaged output cancellation exists

With vacancy indicators `V_j`, one equilibrium-coin ring satisfies

$$
\boxed{
E[V_0'\mid V_{-1},V_0,V_1]
=q+(V_0-q)(1-V_{-1})(1-V_1).}
$$

For product input `q_0`, the terminal one-site chi-square contracts by exactly

$$
\boxed{(1-q_0)^4.}
$$

Thus the FA channel genuinely forgets more information than the raw adaptive transcript bound detects.

However the next constrained update needs a three-site centered statistic, so the scalar output state is not closed.

## E7. First adjacent composition breaks scalar iteration

For S2, a ring at site `1` precedes the terminal ring at site `0`.

At both registered stress quenches, the exact terminal output chi-square remains below the original one-bit baseline but **increases relative to S1**:

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

Therefore the one-ring cancellation is not an iterable scalar block coefficient.

## E8. Shared-graphical-history pair state fails

Let

$$
\phi(Y)=\frac{\mathbf1_{\{Y=0\}}-q}{\sqrt{q(1-q)}}
$$

and condition on the block graphical marks `W`. Define

$$
\mathcal B
=E_W\left[
\left(E_{q_0}[\phi(Y)\mid W]-E_q[\phi(Y)\mid W]\right)^2
\right].
$$

Equivalently, for two independent reference initial fields driven by the same `W`,

$$
\mathcal B
=E[(L(Q)-1)(L(Q')-1)\phi(Y)\phi(Y')].
$$

This is the natural exact shared-history pair object for the adaptive evaluator.

At `q_0=1/20`, already

$$
\frac{\mathcal B_1}{\mathcal C_0}
=\frac{35921}{32000}>1.
$$

And adjacent composition increases it at both registered quenches:

$$
\frac{\mathcal B_2}{\mathcal B_1}
=\frac{31388053}{28736800}>1,
$$

$$
\frac{\mathcal B_2}{\mathcal B_1}
=\frac{1631729}{1339400}>1.
$$

Thus conditioning on enough graphical information for local pair composition loses the cancellation recovered only after full averaging.

## E9. Universal chi-square channel compression also fails the predecessor cost

The exact chi-square strong-data-processing coefficients are

$$
\eta_1=(1-q)^2,
\qquad
\eta_2=(1-q)^3(1+q^2).
$$

At `q=1/10`, both are strictly below one. But they act on the full predecessor-vector divergence. For the product perturbations used in the bounded test, the resulting S1 and S2 bounds are all larger than the one-bit baseline.

Thus neither the adaptive transcript nor the strongest universal one-output chi-square coefficient yields the missing bounded state.

## E10. Exact growing-correlation theorem

For a right-to-left staircase of `m` adjacent equilibrium-coin rings at sites

$$
m-1,m-2,\ldots,0,
$$

let

$$
M_m=V_m,
$$

$$
M_k=q+(V_k-q)(1-V_{k-1})(1-M_{k+1}).
$$

Then the coefficient of the full centered monomial

$$
\prod_{j=-1}^{m}(V_j-q)
$$

in `M_0-q` is exactly

$$
\boxed{(-q)^{m-1}\ne0.}
$$

Hence exact adjacent composition creates genuinely new correlation order at every step.

At S2, two positive four-site laws can have identical every proper marginal but different terminal output. Therefore even the full collection of lower-order local marginals does not close the next output.

This is the structural reason `FA-INFO-002` returns `STOP-NO-ITERABLE-STATE` rather than `UNRESOLVED-BOUNDED`.

## E11. Current stop rules

Do not restart FA by:

- enlarging the stopped vacancy-marker automaton;
- running S3/S4 adaptive blocks after the registered S1/S2 closure failure;
- carrying the full growing transcript/correlation hierarchy;
- replacing memory erasure by stronger equilibrium gap/entropy work;
- reverting to mark-only information percolation or the conservative centered dual;
- treating product-background disagreement probabilities as iterable under path conditioning without a new decoupling theorem.

A future FA restart requires a materially new upstream theorem or bounded architecture not equivalent to FA-SCREEN or FA-INFO.

## E12. Positive-rates status retained

The positive-rates branch is independently at `no-credible-route` after its bounded toolbox-derived tests:

- uniform negative additive-Hamming drift is impossible for every Markovian coupling at the hard point;
- mark-only Boolean-map information percolation has a pair obstruction;
- ordinary and checkerboard Gray scalar splice closure fail;
- the principal's zero-boundary distinguished-zero transfer reduces to tail shift.

Meeting 030's signed boundary-transmission restart bar remains unchanged.

## Next action

There is no automatic continuation assignment from either stopped target. The next research action should be a **target-selection/opportunity-cost review**, not a larger instance of a stopped architecture.

No public `docs/` or `mkdocs.yml` edits are authorized by this proof spine.
