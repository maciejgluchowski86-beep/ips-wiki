# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

On `r11=0`, write

\[
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
\]

with residual chamber

\[
\mathcal R=\{0<a<b,\ 1/2\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\}.
\]

## E0. Current route status

There is **no active proof architecture**.

Meeting 034 completes the last bounded toolbox-derived PASS test. Its outcome is `STOP-SCALAR-EDGE-OBSTRUCTION`. Together with Meetings 032--033 and G011, the current group has no positive structural signal warranting another positive-rates proof block.

The conjecture remains open. The present status is `no-credible-route`, not a mathematical impossibility theorem.

Do not enlarge a stopped mechanism merely by increasing its state space or renaming its missing theorem.

## E1. Sharp connected-renewal blocker retained

For singleton depth `n`, the canonical predecessor-trail quantity satisfies

\[
J_n=\frac BgR_n=\frac gBN_n,
\qquad B=b+c-a,\quad g=b-a.
\]

At

\[
P_*=(1/1000,1/10,9999/10000),
\]

the fixed signed-filter witness has an exact renewal recurrence with a verified supercritical seven-coefficient prefix. The sufficient all-depth connected-tail bound remains open.

After the G010 recentering, all straightforward fresh/scalar branches are subcritical. The sole uncontrolled branch is

\[
\boxed{
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
(g_0e^{-rs}-\varepsilon)e^{sL_{N-1}}f\,ds\,dt.
}
\]

Both temporal factors change sign. No depth-uniform estimate on the actual connected orbit preserving that two-time cancellation is known.

A future restart of this architecture requires new input controlling this operator strongly enough to imply summable/geometric connected coefficients. Bare tail shift, another norm, reversible comparison, filter optimization or longer finite coefficient tables do not clear the bar.

## E2. Zero-boundary invariant family / distinguished-zero transfer

Let `pi_N` be the unique invariant law in the `N`-site chain with fixed zero boundary. One-sidedness gives right-suffix projectivity, while the incompatible left-prefix defect is measured far from the boundary by `Delta_M`.

G011 proves that an East-style marker which enlarges the protected interval while leaving the old block untouched requires

\[
\bar\pi_{N+1}=\pi_N.
\]

Already at `N=1 -> 2`, compatibility holds exactly on

\[
a=b(1-c),
\]

the product surface where

\[
\pi_N=\operatorname{Ber}\!\left(\frac b{1+b}\right)^{\otimes N}.
\]

A width-`m` buffered repair has exact error `Delta_{m+1}` and a finite release kernel cannot change the untouched prefix. Therefore the `pi_N` distinguished-zero transfer is `STOP-EQUIVALENT` off the product surface.

## E3. Common-uniform and additive-Hamming coupling routes

For the common-uniform coupling, every fixed site eventually couples permanently; finite-seed survival is equivalent to convective escape to `-infinity`. At the hard point

\[
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\]

one nevertheless has

\[
\alpha(t)>1\qquad(0<t\le47).
\]

The later occupation/front closure fails because the visible front state forgets hidden right-ancestry capacity. The global-coalescence/occupation route remains stopped.

More generally, cross-site pairings cannot improve additive Hamming drift for any Markovian coupling. A one-disagreement hard-point configuration has best possible instantaneous drift

\[
\frac{9997}{10000}>0.
\]

Thus a uniform `\bar L H\le-\kappa H` bridge is impossible for every Markovian coupling.

## E4. Mark-only information-percolation obstruction

For any exact deterministic Boolean random-map decomposition at `P_h`, aggregate ancestry death/right-jump/two-parent rates satisfy

\[
d+j\le\frac1{5000},
\qquad
r\ge\frac{4999}{5000}.
\]

G012 constructs a width-one two-copy oriented lower cluster in the support intersection. Its bad-cell probability is uniformly below `1/128`, yielding positive survival probability and hence

\[
\boxed{
\inf_{n\ge0}E[2^{|A_{8n}\cap A'_{8n}|}-1]>0.
}
\]

So no exact deterministic-Boolean **mark-only essential-parent support** decomposition can satisfy the desired Miller--Peres pair-intersection decay at `P_h`.

This does not rule out state-adaptive value-reveal trees, but no independent noncircular adaptive bridge is currently specified. Do not promote that possibility merely because the mark-only architecture failed.

## E5. G013 Gray scalar-edge obstruction

Assignment 013 tests Gray's nonadditive edge observable directly, rather than Hamming distance.

Condition on one common local event type in a grand random-map construction. Let

\[
F:\{0,1\}^2\to\{0,1\}
\]

be its deterministic local update rule. Using only the two extremal source copies and the two orientations of one half-line splice, exact scalar hybrid closure at the first splice-boundary event requires

\[
\boxed{F(0,1),F(1,0)\in\{F(0,0),F(1,1)\}.}
\tag{SC}
\]

For event flip indicators `v_xy`, `(SC)` implies

\[
\boxed{v_{11}\le v_{00}+v_{10}},
\qquad
\boxed{v_{00}\le v_{01}+v_{11}}.
\tag{G}
\]

These inequalities survive arbitrary nonnegative mixing of local event types.

### Ordinary gauge

The hard-point rate vector is

\[
(a,b,1-c,1),
\]

so `(G)` requires

\[
1\le a+(1-c)=\frac1{5000},
\]

impossible.

### Checkerboard gauge

After alternating labels the two site types have rate vectors

\[
(b,a,1,1-c),
\qquad
(1-c,1,a,b).
\]

The same scalar-closure inequalities require

\[
b\le a+(1-c),
\]

but at `P_h`

\[
\frac1{100}>\frac1{5000}.
\]

Thus both ordinary and repulsive/checkerboard scalar Gray splices fail **before** no-crossing, protection or permanent coalescence enter.

The definition passes representative attractive/repulsive sanity checks and does not impose arbitrary-source splice closure. Exact verifier: commit `f5a104d1`.

Therefore G013 is `STOP-SCALAR-EDGE-OBSTRUCTION`. Assignment 013 forbids escalation to larger interface-state hierarchies after this failure.

## E6. Other retained stopped interfaces

- Stationary boundary-control/Bellman hierarchy: valid, stopped at the weighted adaptive mismatch theorem.
- Trajectory-valued spatial kernel: full path-space TV coefficient is one.
- Reversible reference Sobolev/left-slice structure: valid, no transport through actual nonreversible defect.
- Raw coefficient Lyapunov families: known local/product/component-weight versions fail.
- Tail shift: still open as a statement, but not a restart architecture by itself.

## E7. Current restart rule

The bounded toolbox-derived positive-rates opportunity set is exhausted.

Do not restart on:

- larger/multiphase Gray edge states;
- unspecified adaptive information histories;
- generic nonlocal couplings or norms;
- common-uniform occupation/extinction;
- bare tail shift;
- Bellman/Foster variants;
- reversible/filter/long-coefficient searches.

A future positive-rates restart requires either:

1. new mathematics controlling the signed boundary-transmission operator on the actual connected orbit while retaining its cancellation; or
2. a materially different architecture with a concrete upstream object, implication to ergodicity, and bounded falsification test not equivalent to an existing blocker.

## E8. Next programme-level direction

The completed toolbox synthesis separately recommends FA-1f Bernoulli-quench **FA-SCREEN**: a two-sided causal-screen theorem whose first gate is a finite graphical leakage/measurability test.

With G013 negative, that is the queued next active research direction. The positive-rates programme remains as retained mathematical background rather than active execution.

## Anti-circularity checkpoint

Do not infer connected-tail control from finite renewal coefficients; iterate one-step positive-frequency bounds without a frame theorem; identify connected renewal with bare tail shift; infer that marker geometry repairs the G011 prefix mismatch; replace G012's pair obstruction by a first-moment statement; reinterpret G013 as a theorem against every possible interface state; or reopen a stopped method merely by enlarging its state description.
