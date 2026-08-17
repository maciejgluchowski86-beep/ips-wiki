# G013b: order-free ordinary scalar splice closure already fails at the hard point

Date: 2026-08-17

## Result

Even without assuming that the two source copies remain ordered, the **ordinary** Gray scalar splice cannot close at `P_h`.

Take the two extremal source configurations `X=0` and `Y=1`. A common deterministic local event at a site is a Boolean rule

\[
F:\{0,1\}^2\to\{0,1\},
\]

applied to every source and hybrid local context. Requiring exact scalar closure for both orientations of the half-line splice already forces

\[
\boxed{
F(0,1),F(1,0)\in\{F(0,0),F(1,1)\}.
}
\tag{C}
\]

For any such rule, if the event flips input `11`, then it flips at least one of `00,01,10`. Therefore every Poisson decomposition by scalar-closure events satisfies

\[
\boxed{
\lambda_{11}
\le
\lambda_{00}+\lambda_{01}+\lambda_{10},
}
\tag{R}
\]

where `lambda_xy` is the spin-flip rate in local context `(x,y)`.

At

\[
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right)
\]

one has

\[
(\lambda_{00},\lambda_{01},\lambda_{10},\lambda_{11})
=\left(\frac1{10000},\frac1{100},\frac1{10000},1\right),
\]

so `(R)` would require

\[
1\le\frac{102}{10000}=\frac{51}{5000},
\]

which is false.

Thus the ordinary scalar splice is locally infeasible at the hard point before no-crossing, coalescence or edge-density estimates enter.

## 1. Why `(C)` is the faithful scalar-closure condition

At the initial time let the lower source be all zero and the upper source all one. Consider a splice boundary between sites `i` and `i+1`.

For the increasing half-line hybrid, the update at site `i` sees the mixed local context `(0,1)`, while the two sources see `(0,0)` and `(1,1)`. After the common event, the hybrid can still be represented by the same two updated sources with a single scalar boundary only if its updated value at `i` equals one of the two source values there. Hence

\[
F(0,1)\in\{F(0,0),F(1,1)\}.
\]

For the decreasing half-line hybrid the mixed context is `(1,0)`, giving

\[
F(1,0)\in\{F(0,0),F(1,1)\}.
\]

No source order is used in this argument. It is only exact hybrid identity plus scalar closure at the first boundary event.

The condition is deliberately imposed only on the two extremal-source splice states Gray actually starts from, not on arbitrary source pairs.

## 2. Enumeration of scalar-closure Boolean events

There are ten Boolean rules satisfying `(C)`:

- the two constants;
- the four rules with `F(0,0)=0,F(1,1)=1` and arbitrary mixed outputs;
- the four rules with `F(0,0)=1,F(1,1)=0` and arbitrary mixed outputs.

Equivalently, if the two diagonal outputs agree then the rule must be constant.

Now suppose such a rule flips input `11`. Then `F(1,1)=0`.

If it did not flip `00`, then `F(0,0)=0` as well. The diagonal outputs would agree, so `(C)` would force the rule to be the constant-zero map. That map flips input `10` as well. Therefore an event flipping `11` necessarily flips at least one of the other three inputs.

This proves the eventwise indicator inequality

\[
1_{\{F_{11}\ne1\}}
\le
1_{\{F_{00}\ne0\}}
+1_{\{F_{01}\ne0\}}
+1_{\{F_{10}\ne1\}}.
\]

Multiplying by the nonnegative event rate and summing over every common graphical event proves `(R)`.

## 3. Attractive sanity check

This closure condition does not reject the ordinary attractive Gray regime.

The usual monotone Boolean rules

- constant `1`;
- `x OR y`;
- constant `0`;
- `x AND y`

all satisfy `(C)`. Hence the standard attractive decomposition from `013a-gray-scalar-order-gate.md` is contained in the ordinary scalar-closure cone.

So the obstruction at `P_h` is not caused by imposing arbitrary-source closure or by demanding more than Gray's two extremal half-line orientations at the first local event.

## 4. Why this does not by itself test the repulsive transform

Gray's repulsive theorem first alternates the identities of zero and one. The extremal source copies in transformed coordinates correspond to checkerboard source configurations in the original variables, not to the ordinary all-zero/all-one pair used above.

Therefore `(R)` is the correct ordinary-gauge scalar test but should not be applied as a repulsive sanity check. The checkerboard gauge must be tested after the alternating relabeling. Its decisive remaining condition is no-crossing/order preservation in the transformed variables, handled separately in Assignment 013.
