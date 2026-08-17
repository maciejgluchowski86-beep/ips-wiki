# 002b: finite cemetery/factorization gate

Date: 2026-08-17

This note records the mandatory `d=3` gate from Assignment 002. The exact verifier is `002-typed-factorization-verifier.py`, commit `b9e75b42`.

## 1. Two-record geometry

Use two sites `0,1` and local types `E={0,1,2}`. Fix two consecutive selected coarse records.

The first is

\[
R_1=(0,t_1,r=1,\tau_1),
\qquad \tau_1(1)=1.
\]

Its hidden source outcome is

\[
s_1\in\{1,2\}.
\]

Thus immediately after `R_1`, site `1` has incoming type `1`, while site `0` has hidden type `s_1`.

Between the records, allow one empty-target clock family on site `0` indexed by source type `2` and outcome `1`. Let

\[
e=1
\]

mean that at least one such point occurs. Since after its first effective ring the local type is no longer `2`, only the presence/absence indicator matters. Therefore before `R_2` the site-0 type is

\[
X_{t_2-}(0)
=
\begin{cases}
1,&s_1=1,\\
1,&s_1=2,\ e=1,\\
2,&s_1=2,\ e=0.
\end{cases}
\]

The second selected record is

\[
R_2=(1,t_2,r=1,\tau_2),
\qquad \tau_2(0)=1,
\]

with hidden source outcome

\[
s_2\in\{0,1\}.
\]

Its incoming target at site `0` is compatible exactly unless

\[
(s_1,e)=(2,0).
\tag{1.1}
\]

The exceptional case is a genuine typed target conflict with no binary counterpart. The record `R_2` is nevertheless selected, because selection is decided by its source line immediately before applying the typed merge. The conflict then sends the global dual to cemetery.

## 2. Future no-record constraints

After `R_2`, let

- `B` be the indicator that a nonempty-target clock indexed by source type `1` occurs on site `0`;
- `C` be the indicator that a nonempty-target clock indexed by source type `1` occurs on site `1`.

On a noncemetery history, the incoming merge makes site `0` type `1`, so exactness of the two-record skeleton requires

\[
B=0.
\tag{2.1}
\]

The source line of `R_2` starts its outgoing end patch at hidden type `s_2`, so exactness also requires

\[
s_2=0\quad\text{or}\quad C=0.
\tag{2.2}
\]

On the conflict history (1.1), the global process is already in cemetery after `R_2`; both future constraints disappear because no later clock can be successful.

## 3. Exact local consistency factors

The three nontrivial patch conditions are therefore

\[
A=1_{\{(s_1,e)\ne(2,0)\}},
\]

for the site-0 patch ending at the incoming `R_2` target,

\[
B_0=1_{\{B=0\}},
\]

for the site-0 incoming end patch after `R_2`, and

\[
C_1=1_{\{s_2=0\text{ or }C=0\}},
\]

for the site-1 outgoing end patch after `R_2`.

The verifier checks configuration by configuration that

\[
1_{\{\tau_\dagger>T\}}
1_{\{G_T=(R_1,R_2)\}}
=
A B_0 C_1.
\tag{3.1}
\]

It also checks

\[
1_{\{G_T=(R_1,R_2)\}}
=
1_{\{A=0\}}+A B_0 C_1,
\tag{3.2}
\]

where the two terms on the right are disjoint. Equation (3.2) is the exact finite origin of the bare-conditioning failure.

## 4. Exact rational reference law

Take the five hidden variables

\[
s_1,\ e,\ s_2,\ B,\ C
\]

independent and fair. This is realizable by equal absolute branch rates for `s_1,s_2` and by choosing the three relevant Poisson subintervals so that

\[
P(\text{at least one point})=\frac12.
\]

For a rate `lambda>0`, an interval of length `(log 2)/lambda` has exactly this probability. The verifier uses only the resulting exact rational probabilities and never evaluates `log 2` or any floating-point quantity.

There are `32` hidden configurations. Exactly `8` contain the incoming conflict (1.1).

The bare two-record skeleton has probability

\[
\boxed{
P(G_T=(R_1,R_2))=\frac{17}{32}.}
\tag{4.1}
\]

Its noncemetery part has probability

\[
\boxed{
P(G_T=(R_1,R_2),\tau_\dagger>T)=\frac9{32}.}
\tag{4.2}
\]

The latter is exactly the product of the three local consistent masses:

\[
\frac34\cdot\frac12\cdot\frac34=\frac9{32}.
\tag{4.3}
\]

## 5. Full conditional factorization fails

Let `K` be the conflict event `(s_1,e)=(2,0)`. Under conditioning on the bare record list,

\[
P(K\mid G)=\frac8{17},
\qquad
P(B=1\mid G)=\frac4{17},
\]

whereas

\[
P(K,B=1\mid G)=\frac4{17}.
\]

Therefore

\[
\boxed{
P(K,B=1\mid G)=\frac4{17}
\ne
\frac8{17}\frac4{17}
=\frac{32}{289}.}
\tag{5.1}
\]

The conflict status of the patch before `R_2` is correlated with a future mark in the next patch. Thus the binary theorem cannot be copied literally as conditional independence given the coarse record list alone.

## 6. Cemetery weighting restores exact factorization

Multiplication by the noncemetery indicator deletes the first term in (3.2), leaving the product (3.1). Under the independent reference variables, the resulting normalized weighted law factors over

\[
(s_1,e),\qquad B,\qquad(s_2,C).
\]

The verifier checks every one of the `4 x 2 x 4 = 32` cells of this normalized joint law against the product of its three marginals.

Hence the conflict dependence is real under bare conditioning but does **not** survive the representation-sufficient zero/cemetery weighting.

## 7. Gate decision

The mandatory gate rules out neither continuation stop condition:

- it is not `STOP-NO-LOCAL-CONSISTENCY`, because noncemetery exactness is exactly the product of the local events;
- it is not `STOP-TYPED-CONFLICT-COUPLING`, because the conflict-induced dependence disappears identically after the zero/cemetery weight is inserted.

The correct general target is therefore the weighted Mecke identity allowed explicitly by Assignment 002. No claim of bare conditional-law factorization will be made.
