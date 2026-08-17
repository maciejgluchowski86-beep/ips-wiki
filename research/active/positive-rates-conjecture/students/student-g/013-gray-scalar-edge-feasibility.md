# Assignment 013: scalar Gray splice-edge feasibility at the hard point

Date: 2026-08-17

## Verdict

`STOP-SCALAR-EDGE-OBSTRUCTION`

The direct scalar/two-type Gray splice-edge architecture is locally impossible at

\[
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right).
\]

The obstruction occurs **before** no-crossing, permanent coalescence, protected edge pairs, or Gray's spatial edge-density argument. Exact hybrid identity plus scalar closure for the two extremal half-line orientations already forces eventwise flip inequalities which the generator violates in both relevant gauges:

- ordinary gauge:
  \[
  1\le a+(1-c),
  \]
  false because `1>1/5000`;
- checkerboard/repulsive gauge:
  \[
  b\le a+(1-c),
  \]
  false because `1/100>1/5000`.

The proof is decomposition-independent over every genuine local random-map grand coupling. It does not assume the common-uniform coupling, Hamming contraction, a global source order, or arbitrary-source splice closure.

A construction evading the theorem must abandon exact scalar Gray hybrid identity or carry additional interface/source information beyond one scalar splice boundary. Assignment 013 pre-registers that enlargement as the stopping point, so no larger edge-state hierarchy is pursued.

Durable checkpoints:

- source-order reconstruction and attractive/repulsive sanity check: `013a-gray-scalar-order-gate.md`, commit `89174ccf`;
- order-free ordinary scalar closure obstruction: `013b-gray-order-free-scalar-closure.md`, commit `e144fc82`;
- checkerboard scalar closure obstruction: `013c-gray-checkerboard-scalar-closure.md`, commit `4bb63d54`;
- exact Boolean/rational verifier, strengthened through commit `f5a104d1`.

## A. What is load-bearing in Gray's object

The checked Gray mechanism has five ingredients.

1. **Hybrid identity.** A half-line process is exactly one source copy on one side of a scalar edge and the other source copy on the other side.
2. **Scalar closure.** A local graphical event sends such a hybrid to another hybrid of the same two source copies with one scalar edge.
3. **Protection.** While a suitable left/right edge pair stays separated, the hybrid identities protect the interval between them from exterior changes.
4. **No crossing and permanent coalescence.** Ordered edges cannot pass through one another; after meeting they can be represented by one edge.
5. **Positive-rate density argument.** Once the edge geometry exists, strict positivity gives a local chance for nearby edges to coalesce and the spatial ergodic argument rules out a positive density of eternal distinct edges.

Attraction supplies a common graphical construction in which the extremal source copies remain ordered, and monotone local events make the mixed boundary output equal one of the two source outputs. The repulsive theorem first alternates the meanings of zero and one, reducing to the same mechanism in checkerboard variables.

For Assignment 013, however, one should not assume source order in order to prove failure. The faithful first gate is even weaker: take Gray's two extremal source copies and require only exact scalar closure of the two half-line orientations at their first local boundary event. If that already fails, no later edge property can exist.

## B. Why a common local event is a deterministic Boolean rule

A Gray/Harris grand coupling is one common graphical construction for all initial configurations. After conditioning on the mark of a local event at site `i`, the event must specify, consistently for every marginal having local input `(x,y)`, the updated value at `i`. Thus one event is represented by a deterministic Boolean rule

\[
F:\{0,1\}^2\to\{0,1\}.
\]

Different Poisson event types may have different rules and arbitrary nonnegative rates; no rate-one/common-uniform representation is assumed.

This is not the restriction to a pairwise coupling chosen separately for one source pair. If the output assigned to a configuration with local input `(x,y)` were allowed to depend on which other initial states happened to be included in the coupled family, there would be no projectively consistent grand random map and hence no common Gray graphical construction. Assignment 013 explicitly requires the same event to act consistently on all source and hybrid configurations.

Therefore it is enough to derive necessary inequalities event by event and sum them against arbitrary nonnegative event rates.

## C. Exact extremal scalar-closure condition

At time zero let the two source copies in ordinary variables be

\[
X\equiv0,\qquad Y\equiv1.
\]

Place a splice boundary between sites `i` and `i+1`.

For the increasing half-line hybrid, site `i` has local context `(0,1)`, while the source copies see `(0,0)` and `(1,1)`. After one common event, the hybrid can still be a scalar splice of the two updated sources only if its new value equals one of the two source values at `i`:

\[
F(0,1)\in\{F(0,0),F(1,1)\}.
\]

For the decreasing half-line orientation the mixed context is `(1,0)`, giving

\[
F(1,0)\in\{F(0,0),F(1,1)\}.
\]

Hence every scalar-closure event satisfies

\[
\boxed{
F(0,1),F(1,0)\in\{F(0,0),F(1,1)\}.
}
\tag{C}
\]

No arbitrary source pair is used. These are exactly the two extremal half-line boundary states which the Gray architecture must contain.

The verifier enumerates all 16 Boolean maps and finds exactly ten satisfying `(C)`.

## D. Two eventwise flip inequalities

For one deterministic event put

\[
v_{xy}=1_{\{F(x,y)\ne x\}}.
\]

Condition `(C)` implies

\[
\boxed{v_{11}\le v_{00}+v_{10}},
\tag{I1}
\]

\[
\boxed{v_{00}\le v_{01}+v_{11}}.
\tag{I2}
\]

### Proof of `(I1)`

If `v_11=0` there is nothing to prove. Otherwise `F(1,1)=0`. If `v_00=1` the right side is already at least one. If `v_00=0`, then `F(0,0)=0`; the two diagonal outputs coincide, so `(C)` forces `F(1,0)=0`. Since input `10` has self spin one, `v_10=1`.

### Proof of `(I2)`

If `v_00=0` there is nothing to prove. Otherwise `F(0,0)=1`. If `v_11=1` the right side is already at least one. If `v_11=0`, then `F(1,1)=1`; the diagonal outputs coincide, so `(C)` forces `F(0,1)=1`, hence `v_01=1`.

Now let `q_F>=0` be arbitrary Poisson rates of common event rules. The marginal flip rates are

\[
\lambda_{xy}=\sum_F q_F v_{xy}(F).
\]

Summing `(I1)`--`(I2)` yields the same inequalities for `lambda`.

This step is exact and is the load-bearing local theorem.

## E. Ordinary gauge is impossible at `P_h`

On the normalized face `r_11=0`, the actual flip-rate vector in context order `(00,01,10,11)` is

\[
\lambda=(a,b,1-c,1).
\]

By `(I1)`, ordinary scalar Gray closure requires

\[
1\le a+(1-c).
\tag{O}
\]

At `P_h`,

\[
a+(1-c)=\frac1{10000}+\frac1{10000}=\frac1{5000},
\]

so `(O)` fails.

Thus there is no ordinary scalar-splice grand coupling at the hard point even before no-crossing is imposed.

This is stronger and cleaner than the initial order-based observation in checkpoint 013a.

## F. Checkerboard/repulsive gauge is also impossible

Gray handles repulsive systems by alternating the labels of zero and one. Set

\[
\zeta_i=\eta_i\oplus(i\bmod2).
\]

A flip remains a flip, while the local contexts are permuted.

At even `i`, transformed `(z,w)` corresponds to original `(z,1-w)`, giving transformed flip rates

\[
\lambda^{\mathrm{even}}=(b,a,1,1-c).
\]

Apply `(I2)`:

\[
b\le a+(1-c).
\tag{K}
\]

At odd `i`, transformed `(z,w)` corresponds to original `(1-z,w)`, giving

\[
\lambda^{\mathrm{odd}}=(1-c,1,a,b).
\]

Apply `(I1)` and obtain the same condition `(K)`.

At `P_h`,

\[
b=\frac1{100},
\qquad
 a+(1-c)=\frac1{5000},
\]

so `(K)` fails at both checkerboard site types.

Therefore the direct repulsive/checkerboard scalar Gray splice is also locally impossible.

Notice that no global order-preservation assertion is used in this final checkerboard proof. The obstruction is again only exact extremal hybrid identity plus scalar closure.

## G. Anti-overstrengthening sanity checks

The local test must admit Gray's known regimes.

### G1. Attractive representative

Take

\[
(a,b,c)=\left(\frac14,\frac12,0\right).
\]

The event decomposition

- constant `1` at rate `a`;
- `x OR y` at rate `b-a`;
- constant `0` at rate `1`;
- `x AND y` at rate zero

has the correct flip rates. Every listed Boolean rule satisfies `(C)`; in fact they are monotone. Hence the scalar-closure definition admits this attractive Gray architecture.

More generally the standard attractive decomposition by constant `1`, OR, constant `0`, AND is nonnegative whenever

\[
a\le b,
\qquad
\delta_1\le\delta_0.
\]

### G2. Repulsive representative

Take

\[
(a,b,c)=\left(\frac12,\frac14,\frac12\right).
\]

After checkerboard relabeling the transformed process is attractive at both parities. Equivalently the original-variable decomposition by constant maps together with `x OR (NOT y)` and `x AND (NOT y)` becomes monotone after the alternating transform. Thus transformed extremal scalar closure holds.

In particular the necessary scalar condition from `(K)` is satisfied:

\[
\frac14\le\frac12+\frac12.
\]

So the test does not falsely reject representative attractive or repulsive cases.

### G3. Why arbitrary-source closure was not imposed

If `(C)` were imposed for arbitrary source quadruples rather than just the extremal half-line states, only unary Boolean maps would survive. That would be an unjustified strengthening and is not used here.

The final obstruction is therefore strictly at the source-supported Gray interface requested by Assignment 013.

## H. Relation to the initial source-order checkpoint

Checkpoint 013a reconstructs why the familiar Gray proof obtains scalar closure from ordinary or checkerboard order. It proves the stronger order-preserving conditions:

- ordinary: `a<=b` and `c<=0`;
- checkerboard: `b<=a` and `c>=0`.

Those conditions fail at `P_h` as expected.

However the final result does **not** rely on claiming that every conceivable scalar splice must preserve a source order. Checkpoints 013b--013c replace that potentially overstrong step by the exact extremal scalar-closure inequalities `(I1)`--`(I2)`. The final stop status is therefore robust to order-free scalar coupling attempts.

## I. Why later Gray stages are moot

The hybrid itself cannot survive one boundary event with the required marginal rates. Hence there is no faithful scalar object on which to test:

- no crossing;
- permanent coalescence;
- protection between an edge pair;
- the positive-rate local collision episode;
- spatial edge-density/ergodic arguments.

An LP over joint edge rates would only rediscover the same infeasibility after introducing more variables. The analytic rate inequalities are stronger and exact.

## J. Scope of the negative result

Killed:

> The direct Gray extension in which the information carried by a half-line hybrid is only its two source identities, one scalar splice boundary (with the ordinary/checkerboard two-type relabeling), and the common local graphical event.

Not killed:

- an interface carrying additional finite or infinite source-history/orientation state;
- a nonlocal coupling whose hybrid is not an exact scalar splice after every local event;
- state-adaptive information histories;
- the signed connected-renewal route;
- the positive-rates conjecture.

But Assignment 013 pre-registers that if scalar/two-type closure fails, the programme does not escalate to 4/8/16 edge phases, matrix-product edges, ancestry counters, or generic nonlocal coupling. Thus those possibilities are not new work generated by this failure.

## K. Assignment status

The correct pre-registered outcome is

\[
\boxed{\texttt{STOP-SCALAR-EDGE-OBSTRUCTION}.}
\]

The toolbox-derived positive-rates PASS candidates have now all failed in their bounded direct implementations:

1. uniform additive-Hamming nonbasic coupling: impossible for every Markovian coupling (Meeting 032);
2. mark-only optimized information-percolation support: decomposition-independent pair obstruction (Meeting 033 / G012);
3. direct scalar/two-type Gray splice edge: decomposition-independent local hybrid-closure obstruction (this assignment).

No positive structural signal remains from the bounded toolbox experiments.
