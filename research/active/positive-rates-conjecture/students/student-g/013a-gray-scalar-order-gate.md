# G013a: Gray scalar splice closure has an order gate

Date: 2026-08-17

## Result

For the direct scalar/two-type Gray architecture in Assignment 013, the source pair must remain in a sitewise binary comparison relation. For a homogeneous binary chain, allowing the usual period-two checkerboard relabeling leaves only two nontrivial gauges:

1. ordinary order, giving the attractive inequalities;
2. alternating order, giving the repulsive inequalities.

At

\[
P_h=(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\]

both gates fail locally, independently of how microscopic events at different sites are coupled.

This is a necessary local obstruction for a faithful direct Gray scalar splice construction. It does not rule out a genuinely larger interface state which stores additional source-orientation information; Assignment 013 explicitly forbids escalating to such a hierarchy after the scalar test.

## 1. The source-order ingredient in Gray's scalar edge

Gray's left/right splice edges are not edges between two arbitrary source configurations. They are defined relative to the lower and upper source copies supplied by attractiveness. The hybrid agrees exactly with one source on one side of the edge and the other source on the other side. The labels `lower` and `upper` remain meaningful for all times because the common graphical construction preserves the source order.

For repulsive rates Gray first alternates the identities of zero and one. In those transformed variables the source copies are again ordered. In the original variables this is the checkerboard order.

Thus a direct scalar/two-type transfer which keeps Gray's hybrid/protection/no-crossing semantics needs an invariant sitewise comparison of the two source copies. Without such a comparison, a local source crossing changes which source is the lower/upper one inside a protected region; recording those changing orientation domains requires extra interface state and is no longer the direct scalar/two-type Gray object being tested.

For a binary spin there are only two orientations of the one-site order. Translation covariance with at most the period-two relabeling used in the repulsive theorem therefore gives, up to globally swapping the names of the two sources,

- constant orientation: ordinary order;
- alternating orientation: checkerboard order.

## 2. Ordinary-order necessary inequalities

Write the actual flip rates at a site as

\[
\beta_0=a,\qquad \beta_1=b
\]

for `0 -> 1` when the right neighbor is respectively `0,1`, and

\[
\delta_0=1-c,\qquad \delta_1=1
\]

for `1 -> 0`.

Suppose a grand coupling preserves ordinary coordinatewise order `X <= Y` pathwise.

Take an agreed zero at site `i`, with ordered right neighbors

\[
X_i=Y_i=0,\qquad X_{i+1}=0,\quad Y_{i+1}=1.
\]

A birth in the lower copy without a simultaneous birth in the upper copy would create `(1,0)` at site `i` and violate order. Hence the lower birth rate cannot exceed the upper birth rate:

\[
\boxed{a\le b.}
\tag{A1}
\]

Now take an agreed one with the same ordered right neighbors:

\[
X_i=Y_i=1,\qquad X_{i+1}=0,\quad Y_{i+1}=1.
\]

A death in the upper copy without a simultaneous death in the lower copy creates `(1,0)` and violates order. Therefore

\[
\boxed{\delta_1\le\delta_0},
\qquad\text{i.e.}\qquad
\boxed{c\le0.}
\tag{A2}
\]

These are coupling-independent marginal-rate constraints. Pairing the offending flip with a jump at another site cannot repair the order at site `i`.

At `P_h`, `(A1)` holds but `(A2)` fails maximally: the upper death rate exceeds the lower death rate by

\[
\delta_1-\delta_0=c=\frac{9999}{10000}>0.
\]

Hence no ordinary-order-preserving grand coupling exists at `P_h`.

## 3. Checkerboard-order necessary inequalities

Let the comparison orientation alternate with parity. Choose a parity at which `X_i <= Y_i`; then at the right neighbor the comparison is reversed, `X_{i+1} >= Y_{i+1}`.

For an agreed zero take

\[
X_i=Y_i=0,\qquad X_{i+1}=1,\quad Y_{i+1}=0.
\]

The lower copy now has birth rate `b`, while the upper copy has birth rate `a`. To prevent the lower copy from becoming `1` alone requires

\[
\boxed{b\le a.}
\tag{R1}
\]

For an agreed one in the same checkerboard context, the lower death rate is `\delta_1=1` and the upper death rate is `\delta_0=1-c`. To prevent the upper copy from dying alone requires

\[
\boxed{\delta_0\le\delta_1},
\qquad\text{i.e.}\qquad
\boxed{c\ge0.}
\tag{R2}
\]

These are exactly the one-sided repulsive inequalities on this normalized face.

At `P_h`, `(R2)` holds but `(R1)` fails by

\[
b-a=\frac{99}{10000}>0.
\]

Hence no checkerboard-order-preserving grand coupling exists at `P_h`.

## 4. Deterministic-map form and scalar splice closure

The order gate is also exactly what makes the scalar splice close pathwise.

For ordinary order, suppose a common graphical event at site `i` applies a deterministic Boolean rule `F(x,y)`. If both source configurations are ordered, then for a splice whose edge lies between `i` and `i+1`,

\[
(X_i,X_{i+1})
\le
(X_i,Y_{i+1})
\le
(Y_i,Y_{i+1}).
\]

If `F` is monotone, then

\[
F(X_i,X_{i+1})
\le
F(X_i,Y_{i+1})
\le
F(Y_i,Y_{i+1}).
\]

Because the outputs are binary, the mixed hybrid output equals one of the two source outputs. Thus after the event the hybrid is again an exact scalar splice, with the edge staying put or shifting by one interaction range.

Conversely, pathwise preservation of the two source copies in ordinary order requires every deterministic common event to be monotone on the allowed ordered local states. The checkerboard case is identical after alternating the spin labels; in original variables the event rule is monotone in the self spin and antitone in the right spin.

Hence the ordinary and checkerboard order gates are not ancillary conditions added to Gray's edge: they are precisely the local mechanism which makes the binary mixed context choose one of the two source outputs rather than create a third interface value.

## 5. Attractive/repulsive sanity check

The definition admits the known Gray regimes.

### Attractive representative

Take, for example,

\[
a=\frac14,\qquad b=\frac12,\qquad c=0.
\]

Then `a<=b` and `\delta_1=\delta_0=1`. An explicit monotone-map decomposition is

- constant `1` at rate `a`;
- `x OR y` at rate `b-a`;
- constant `0` at rate `\delta_1`;
- `x AND y` at rate `\delta_0-\delta_1=0`.

All event maps are monotone, so ordinary source order and scalar splice closure hold.

More generally, whenever `a<=b` and `\delta_1<=\delta_0`, the same decomposition with rates

\[
a,\quad b-a,\quad \delta_1,\quad \delta_0-\delta_1
\]

is nonnegative.

### Repulsive representative

Take

\[
a=\frac12,\qquad b=\frac14,\qquad c=\frac12.
\]

Then `b<=a` and `\delta_0<=\delta_1`. An explicit original-variable decomposition by rules monotone in `x` and antitone in `y` is

- constant `1` at rate `b`;
- `x OR (NOT y)` at rate `a-b`;
- constant `0` at rate `\delta_0`;
- `x AND (NOT y)` at rate `\delta_1-\delta_0`.

After alternating the spin labels these become monotone common events, so the checkerboard source order and scalar splice closure hold.

Thus the local definition passes the required attractive and repulsive sanity checks.

## 6. Consequence for Assignment 013

The direct Gray scalar/two-type architecture cannot use either invariant binary source order at `P_h`:

\[
\text{ordinary order fails because }c>0,
\]

\[
\text{checkerboard order fails because }b>a.
\]

The remaining audit question is whether Gray's protected hybrid/no-crossing identities can be faithfully localized with a scalar edge **without** any invariant source comparison. If not, this checkpoint already supplies the analytic `STOP-SCALAR-EDGE-OBSTRUCTION` theorem. If an order-free scalar localization exists, it must be tested separately rather than dismissed by the order gate.
