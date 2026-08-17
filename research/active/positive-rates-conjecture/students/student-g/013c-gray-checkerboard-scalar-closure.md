# G013c: checkerboard Gray scalar splice also fails at the hybrid-closure gate

Date: 2026-08-17

## Result

The alternating-spin transform does not rescue a scalar Gray splice at the hard point. The obstruction can be proved using **only exact hybrid identity and scalar closure for the two extremal half-line orientations**. No global source order, no-crossing theorem, edge-density argument, or enlarged interface state is used.

For a deterministic Boolean local event `F`, ordinary extremal scalar-splice closure is

\[
F(0,1),F(1,0)\in\{F(0,0),F(1,1)\}.
\tag{C}
\]

Let

\[
v_{xy}=1_{\{F(x,y)\ne x\}}
\]

be its four flip indicators. Every rule satisfying `(C)` obeys the two eventwise inequalities

\[
\boxed{v_{11}\le v_{00}+v_{10}},
\tag{I1}
\]

\[
\boxed{v_{00}\le v_{01}+v_{11}}.
\tag{I2}
\]

Consequently every Poisson grand-coupling decomposition whose events preserve scalar extremal splices satisfies the corresponding inequalities for the four marginal flip rates.

At the hard point, the ordinary gauge violates `(I1)`. After the checkerboard transform, both parities reduce to the same necessary inequality

\[
\boxed{b\le a+(1-c)},
\tag{CHK}
\]

which is also violated strongly:

\[
\frac1{100}>\frac1{10000}+\frac1{10000}=\frac1{5000}.
\]

Therefore neither the ordinary nor the repulsive/checkerboard scalar Gray architecture is locally feasible at `P_h`.

## 1. Proof of the eventwise inequalities

Assume `(C)`.

### Proof of `(I1)`

Suppose `v_11=1`, so `F(1,1)=0`. If `v_00=1`, the right side of `(I1)` is already at least one. Otherwise `v_00=0`, so `F(0,0)=0` as well. The two diagonal outputs are then equal. Condition `(C)` forces

\[
F(1,0)=0.
\]

Since the input self spin in context `10` is one, this means `v_10=1`. Hence `v_11<=v_00+v_10` in all cases.

### Proof of `(I2)`

Suppose `v_00=1`, so `F(0,0)=1`. If `v_11=1`, the right side is already at least one. Otherwise `v_11=0`, so `F(1,1)=1` as well. Again the diagonal outputs agree, and `(C)` forces

\[
F(0,1)=1.
\]

The input self spin in context `01` is zero, so `v_01=1`. Hence `v_00<=v_01+v_11`.

Summing either eventwise inequality against nonnegative Poisson event rates gives the same inequality for the generator's flip rates.

## 2. Ordinary gauge at `P_h`

The actual flip-rate vector in context order `(00,01,10,11)` is

\[
\lambda
=\left(a,b,1-c,1\right).
\]

By `(I1)`, ordinary scalar splice closure requires

\[
1\le a+(1-c).
\]

Equivalently `c<=a`. At `P_h`,

\[
a+(1-c)=\frac1{5000},
\]

so the inequality fails by a factor of `5000`.

This sharpens the weaker ordinary bound recorded in `013b-gray-order-free-scalar-closure.md`.

## 3. Checkerboard transform

Let

\[
\zeta_i=\eta_i\oplus p_i,
\qquad p_i=i\pmod2.
\]

A spin flip remains a spin flip under this relabeling, but the local contexts are permuted.

At an even site (`p_i=0,p_{i+1}=1`), transformed context `(z,w)` corresponds to original context `(z,1-w)`. Hence the transformed flip-rate vector is

\[
\lambda^{\rm even}
=\left(b,a,1,1-c\right).
\]

Applying `(I2)` to the transformed scalar splice gives

\[
b\le a+(1-c).
\]

At an odd site (`p_i=1,p_{i+1}=0`), transformed context `(z,w)` corresponds to original context `(1-z,w)`. The transformed flip-rate vector is

\[
\lambda^{\rm odd}
=\left(1-c,1,a,b\right).
\]

Applying `(I1)` gives again

\[
b\le (1-c)+a.
\]

Thus both site types impose exactly `(CHK)`.

At `P_h`,

\[
b=\frac1{100},
\qquad
a+(1-c)=\frac1{5000},
\]

so no checkerboard scalar-splice grand coupling exists.

## 4. Sanity against Gray's known regimes

This is not an overstrong arbitrary-pair condition. It uses only the same two extremal half-line mixed contexts as `013b`.

For ordinary attractive rates, the standard monotone event decomposition (constant `1`, OR, constant `0`, AND) satisfies `(C)` event by event, so `(I1)`--`(I2)` hold automatically.

For repulsive rates, after alternating the spin labels the standard repulsive decomposition becomes a monotone decomposition in the transformed variables, so the same transformed scalar-closure condition `(C)` holds. In particular the representative repulsive point from `013a`,

\[
(a,b,c)=\left(\frac12,\frac14,\frac12\right),
\]

satisfies

\[
b\le a+(1-c)=1.
\]

Thus the test admits representative attractive and repulsive Gray architectures as required.

## 5. Assignment-013 consequence

The direct scalar/two-type Gray route fails at a strictly earlier interface than anticipated:

- ordinary scalar hybrid closure fails at `P_h`;
- checkerboard/repulsive scalar hybrid closure fails at `P_h`;
- therefore no local scalar edge can reach the later no-crossing, permanent-coalescence, protected-pair, or edge-density stages.

The obstruction is exact and decomposition-independent over all deterministic Boolean common-event representations. A grand coupling which evades it must carry additional interface/source information beyond the single scalar splice boundary (or abandon exact Gray hybrid identity). That is outside Assignment 013's pre-registered scope.

This establishes the final status `STOP-SCALAR-EDGE-OBSTRUCTION`.
