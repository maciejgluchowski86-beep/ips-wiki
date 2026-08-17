# Group meeting 034: Gray scalar splice is locally obstructed; bounded toolbox positive-rates set is exhausted

Date: 2026-08-17

`state_narrowed: yes`.

Professor execution/review of Assignment 013 after the Student G session failed operationally. The assignment itself remained durable at commit `190ec3d`; all mathematics below was checkpointed during execution rather than held until the end.

Evidence:

- `students/student-g/013a-gray-scalar-order-gate.md`, commit `89174ccf`;
- `students/student-g/013b-gray-order-free-scalar-closure.md`, commit `e144fc82`;
- `students/student-g/013c-gray-checkerboard-scalar-closure.md`, commit `4bb63d54`;
- exact Boolean/rational verifier, final commit `f5a104d1`;
- final report `students/student-g/013-gray-scalar-edge-feasibility.md`, commit `0744788e`;
- handoff `students/student-g/013-handoff.md`.

## Ruling

**Assignment 013 ends `STOP-SCALAR-EDGE-OBSTRUCTION`.**

The direct scalar/two-type extension of Gray's edge geometry is locally impossible at the hard point. The obstruction is earlier than no-crossing: exact extremal half-line hybrid identity plus scalar closure for a common local graphical event already contradicts the marginal flip rates, in both the ordinary and checkerboard gauges.

This kills the direct Gray scalar bridge tested by Assignment 013. It does not prove that all conceivable larger interface couplings are impossible, but the assignment's pre-registered stopping rule explicitly forbids escalating to them after scalar failure.

## 1. Faithful local scalar condition

Condition on one local event type in a genuine Gray/Harris grand random-map construction. Its action at a site is a deterministic Boolean rule

\[
F:\{0,1\}^2\to\{0,1\}
\]

used consistently for every source and hybrid marginal.

Take only the two extremal ordinary source copies, all zero and all one, and the two orientations of one half-line splice. At the splice boundary the mixed local contexts are `(0,1)` and `(1,0)`, while the source contexts are `(0,0)` and `(1,1)`. Exact scalar closure after the event therefore requires only

\[
\boxed{
F(0,1),F(1,0)\in\{F(0,0),F(1,1)\}.
}
\tag{SC}
\]

This is deliberately weaker than arbitrary-source splice closure and uses no assumed source order.

The verifier enumerates all 16 Boolean maps and confirms exactly ten satisfy `(SC)`.

## 2. Eventwise rate obstruction

Write

\[
v_{xy}=1_{\{F(x,y)\ne x\}}.
\]

Every event satisfying `(SC)` obeys

\[
\boxed{v_{11}\le v_{00}+v_{10}},
\qquad
\boxed{v_{00}\le v_{01}+v_{11}}.
\tag{1}
\]

The proof is elementary. If `F(1,1)=0` and `F(0,0)=0`, then the equal diagonal outputs force `F(1,0)=0`; the other case already has `v00=1`. The second inequality is the spin-reversed argument.

Summing `(1)` against arbitrary nonnegative rates of common graphical event types gives the same inequalities for the generator flip-rate vector.

## 3. Ordinary scalar splice fails

On the normalized face, the actual ordinary rate vector in context order `(00,01,10,11)` is

\[
(a,b,1-c,1).
\]

The first inequality in `(1)` requires

\[
1\le a+(1-c).
\]

At

\[
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\]

\[
a+(1-c)=\frac1{5000},
\]

so ordinary scalar hybrid closure is impossible.

This conclusion does not use the common-uniform coupling and is independent of how Poisson mass is redistributed among admissible deterministic local rules.

## 4. Checkerboard/repulsive scalar splice fails

Apply the alternating spin relabeling

\[
\zeta_i=\eta_i\oplus(i\bmod2).
\]

At even sites the transformed flip-rate vector is

\[
(b,a,1,1-c),
\]

while at odd sites it is

\[
(1-c,1,a,b).
\]

The second inequality in `(1)` at even parity and the first at odd parity both require

\[
\boxed{b\le a+(1-c).}
\]

At `P_h`,

\[
\frac1{100}>\frac1{5000}.
\]

Hence the checkerboard scalar splice is also impossible before any no-crossing or coalescence constraint is imposed.

## 5. Anti-overstrengthening check

The scalar condition accepts representative cases from both Gray regimes.

- At an attractive representative, the usual common event maps constant `1`, OR, constant `0`, AND are monotone and satisfy `(SC)` eventwise.
- At a repulsive representative, after the alternating relabeling the corresponding event maps are monotone in transformed variables and therefore satisfy the same scalar closure condition.

Thus the hard-point obstruction is not an artifact of demanding arbitrary-source closure or of building attraction into the definition.

The preliminary source-order checkpoint is conceptually useful but is not load-bearing for the final stop theorem.

## 6. Why the later Gray stages are moot

The hybrid cannot remain a scalar splice after one boundary event while reproducing the marginal generator. There is therefore no scalar object on which to impose or prove:

- no crossing;
- permanent coalescence;
- protected-region propagation;
- local positive-rate edge collision;
- Gray's stationary edge-density contradiction.

A larger interface carrying orientation/history information might evade the local theorem, but that is precisely the edge-state escalation excluded by Assignment 013's stopping rule.

## 7. Positive-rates direction judgment

The bounded toolbox-derived PASS candidates have now all been tested at their load-bearing objects and failed in their direct forms:

1. **refined/nonbasic Hamming coupling:** Meeting 032 proves uniform negative additive-Hamming drift impossible for every Markovian coupling at `P_h`;
2. **information percolation:** Assignment 012 / Meeting 033 proves a decomposition-independent positive lower bound for the two-copy mark-only support intersection;
3. **Gray scalar edge geometry:** Assignment 013 proves the local scalar hybrid-closure obstruction above.

The principal-directed `pi_N` distinguished-zero transfer likewise stopped exactly at tail shift in Assignment 011.

Therefore the toolbox-derived positive-rates opportunity set is exhausted under its pre-registered bounded tests. There is **no active positive-rates proof architecture** and the operative status returns to `no-credible-route` for the present group. The conjecture remains open and all retained exact mathematics remains valid.

Do not automatically reopen:

- state-adaptive information histories;
- larger/multiphase Gray edge states;
- generic nonlocal couplings or norms;
- common-uniform occupation/extinction;
- tail shift;
- Bellman/Foster variants;
- reversible/filter/long coefficient searches.

The connected-renewal route still has exactly Meeting 030's restart bar: new input controlling the signed boundary-transmission operator on the actual connected orbit while retaining its two-time cancellation, or a materially different architecture.

## 8. Next direction

The previously completed toolbox synthesis separately recommended a narrow reopening of the FA-1f Bernoulli-quench problem on the **FA-SCREEN two-sided causal-screen theorem**, beginning with its finite graphical leakage/measurability gate. That direction was deferred only because the principal's positive-rates distinguished-zero question consumed the sole worker.

With the bounded positive-rates tests now exhausted, **FA-SCREEN becomes the queued next active research direction**. It is not withdrawn.

No public wiki edits are authorized by this meeting.
