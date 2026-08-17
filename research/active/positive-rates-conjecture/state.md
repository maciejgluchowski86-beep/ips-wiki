# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Target:

> Prove the positive rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS.

On `r11=0`, write

\[
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
\]

with residual chamber

\[
\mathcal R=\{0<a<b,\ 1/2\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\}.
\]

Latest meeting: `meetings/034-gray-scalar-edge-obstructed-toolbox-positive-rates-set-exhausted.md`, `state_narrowed: yes`.

## Current status

There is **no active positive-rates proof architecture**.

Assignment 013 is complete with status

`STOP-SCALAR-EDGE-OBSTRUCTION`.

The Student G session failed operationally after the assignment was dispatched, so the Professor executed the bounded test directly and checkpointed all durable mathematics. Student G and Student F are not executing work.

The bounded toolbox-derived positive-rates PASS mechanisms are now exhausted in their direct stipulated forms:

1. uniform additive-Hamming nonbasic coupling: impossible for every Markovian coupling at `P_h`;
2. optimized mark-only information percolation: decomposition-independent pair obstruction at `P_h`;
3. direct scalar/two-type Gray splice edge: decomposition-independent local hybrid-closure obstruction at `P_h`.

The principal-directed `pi_N` distinguished-zero transfer is also closed as `STOP-EQUIVALENT` to the old tail-shift defect off the product surface.

The programme therefore returns to **`no-credible-route` for the present group**. This is an expected-value/architecture ruling, not a proof that the conjecture is false or that every imaginable method fails.

## G013 exact Gray scalar-edge obstruction

At the hard point

\[
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\]

condition on one local event type in a genuine Gray/Harris grand random-map construction. Its common action is a deterministic Boolean rule

\[
F:\{0,1\}^2\to\{0,1\}.
\]

Using only the all-zero/all-one source copies and the two extremal half-line splice orientations, exact scalar hybrid closure at the first boundary event requires

\[
\boxed{F(0,1),F(1,0)\in\{F(0,0),F(1,1)\}.}
\tag{SC}
\]

This assumes neither arbitrary-source closure nor a global source order.

For event flip indicators

\[
v_{xy}=1_{\{F(x,y)\ne x\}},
\]

`(SC)` implies

\[
\boxed{v_{11}\le v_{00}+v_{10}},
\qquad
\boxed{v_{00}\le v_{01}+v_{11}}.
\tag{1}
\]

Summing against arbitrary nonnegative event rates gives the same inequalities for the generator's flip rates.

### Ordinary gauge

The rate vector is

\[
(a,b,1-c,1).
\]

The first inequality in `(1)` forces

\[
1\le a+(1-c).
\]

At `P_h`, the right side is `1/5000`, so ordinary scalar closure is impossible.

### Checkerboard/repulsive gauge

After alternating spin labels, the even and odd transformed rate vectors are

\[
(b,a,1,1-c),
\qquad
(1-c,1,a,b).
\]

The two inequalities in `(1)` force at either parity

\[
 b\le a+(1-c).
\]

At `P_h`, `1/100>1/5000`, so checkerboard scalar closure is also impossible.

The obstruction occurs before no-crossing, permanent coalescence, protected-region propagation or Gray's edge-density argument.

The exact verifier at commit `f5a104d1` enumerates the Boolean scalar-closure class, checks the eventwise inequalities, the hard-point violations, and representative attractive/repulsive sanity points.

Full report: `students/student-g/013-gray-scalar-edge-feasibility.md`, commit `0744788e`.

## Scope of G013

Killed:

> the direct Gray extension whose interface state consists only of the two source identities, one scalar splice boundary (ordinary/checkerboard gauge), and the common local graphical event.

Not ruled out abstractly:

- larger interface/source-history states;
- nonlocal couplings without exact scalar closure after each event;
- state-adaptive information histories;
- the connected-renewal route;
- the conjecture itself.

Assignment 013's pre-registered stop rule forbids automatic escalation to those larger Gray/coupling states after scalar failure.

## Other stopped exact interfaces

### Distinguished-zero / zero-boundary invariant family

G011 proves exact prefix compatibility only on

\[
a=b(1-c),
\]

the product surface. A growing buffer is exactly the old tail-shift defect `Delta_M`; finite release kernels cannot change the protected prefix.

### Mark-only information percolation

At `P_h`, every exact Boolean-map decomposition satisfies

\[
d+j\le\frac1{5000},\qquad r\ge\frac{4999}{5000}.
\]

The width-one two-copy lower cluster survives with positive probability, so

\[
\inf_n E[2^{|A_{8n}\cap A'_{8n}|}-1]>0.
\]

### Additive Hamming coupling

For every Markovian coupling, a one-disagreement hard-point configuration has best possible instantaneous Hamming drift

\[
\frac{9997}{10000}>0.
\]

### Connected renewal

The sharp retained blocker remains the signed boundary-transmission operator

\[
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
(g_0e^{-rs}-\varepsilon)e^{sL_{N-1}}f\,ds\,dt.
\]

No depth-uniform actual-orbit estimate preserving its two-time cancellation is known. Meeting 030's restart bar remains unchanged.

## Restart discipline

Do not automatically restart on:

- state-adaptive histories merely because mark-only histories failed;
- larger/multiphase Gray edges;
- generic nonlocal coupling/norm engineering;
- common-uniform occupation/extinction;
- bare tail shift;
- Bellman/Foster variants;
- reversible/filter/long-coefficient searches.

A positive-rates restart needs genuinely new input controlling the existing sharp blocker or a materially different architecture with an explicit upstream mechanism and bounded falsification test.

## Next research direction

The toolbox synthesis independently recommended reopening the FA-1f Bernoulli-quench problem on the **FA-SCREEN two-sided causal-screen theorem**, beginning with its finite graphical leakage/measurability gate.

That direction was deferred while the positive-rates distinguished-zero and bounded PASS tests used the available execution capacity. With G013 negative, **FA-SCREEN is the queued next active research direction; it is not withdrawn.**

## Wiki

The live wiki remains frozen during research. No `docs/` or `mkdocs.yml` edits are authorized.
