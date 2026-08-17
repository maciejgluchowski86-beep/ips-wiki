# 005a: boundary completeness forces a Metzler interior transfer

Date: 2026-08-17

This note executes Parts A--B of Assignment 005. The setting is one fixed site, local type space

\[
E=\{0,1,2\},
\]

with the boundary-completeness hypothesis from the assignment.

## 1. Physical form of the empty-target transfer

Write the physical single-site replacement rates when every neighbour is in the reference state as

\[
q_{xy}=c^{x\to y}(\mathbf 0),\qquad x\ne y.
\]

These are nonnegative. By the indicator-basis formulas from Assignment 001, the signed empty-target transfer is

\[
K=
\begin{pmatrix}
0&0&0\\
q_{01}&-(q_{01}+q_{10}+q_{12})&q_{21}-q_{01}\\
q_{02}&q_{12}-q_{02}&-(q_{02}+q_{20}+q_{21})
\end{pmatrix}.
\tag{1.1}
\]

In particular

\[
K(1,0)=q_{01}\ge0,
\qquad
K(2,0)=q_{02}\ge0.
\tag{1.2}
\]

The only off-diagonal signs not fixed by physical nonnegativity are the active retyping entries

\[
K(1,2)=q_{21}-q_{01},
\qquad
K(2,1)=q_{12}-q_{02}.
\tag{1.3}
\]

## 2. Boundary completeness forces active retyping nonnegative

Fix distinct active types `a,r in {1,2}`. Boundary completeness says that an incoming-initial patch of type `a` and an outgoing terminal of source type `r` is a realizable descriptor. Its signed numerator is

\[
N_{a\to r}^{IO}(t)=e_a e^{tK}e_r^T.
\]

At zero length,

\[
N_{a\to r}^{IO}(0)=0,
\]

and differentiation gives

\[
\frac{d}{dt}N_{a\to r}^{IO}(0)=K(a,r).
\]

Typed patch positivity requires `N(t)>=0` for every sufficiently small positive `t`, hence

\[
\boxed{K(a,r)\ge0\qquad(a\ne r).}
\tag{2.1}
\]

Thus in `d=3`

\[
q_{21}\ge q_{01},
\qquad
q_{12}\ge q_{02}.
\tag{2.2}
\]

Combining (1.2) and (2.1), every off-diagonal entry of `K` is nonnegative. Therefore `K` is a Metzler matrix.

This proves the Part-A claim; it is necessary, not an imposed surrogate definition.

## 3. Direct semigroup positivity

Choose

\[
c\ge\max\{-K(0,0),-K(1,1),-K(2,2)\}.
\]

Then `K+cI` is entrywise nonnegative. Hence every matrix power `(K+cI)^n` is entrywise nonnegative and

\[
e^{t(K+cI)}
=\sum_{n\ge0}\frac{t^n}{n!}(K+cI)^n
\]

is entrywise nonnegative for every `t>=0`. Therefore

\[
\boxed{e^{tK}=e^{-ct}e^{t(K+cI)}\ge0\text{ entrywise}.}
\tag{3.1}
\]

No Perron--Frobenius theorem is needed for this implication.

## 4. Incoming-initial patch families are automatic

The incoming terminal and outgoing terminal columns are

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T,
\]

both entrywise nonnegative. For an incoming initial type `a`, (3.1) gives

\[
\boxed{e_a e^{tK}f_b^I\ge0,}
\qquad
\boxed{e_a e^{tK}f_r^O\ge0}
\tag{4.1}
\]

for every `a,b,r in {1,2}` and `t>=0`.

Thus under boundary completeness, once the necessary short-time retyping inequalities have made `K` Metzler, **all incoming-initial `II` and `IO` numerator families drop out of the remaining positivity problem**.

The entire unresolved sign problem is in outgoing initial rows `p=a_{r,tau}`.

## 5. Active block

It is useful to record the constrained form

\[
K=
\begin{pmatrix}
0&0&0\\
d_1&-\alpha&\beta\\
d_2&\gamma&-\delta
\end{pmatrix},
\tag{5.1}
\]

where

\[
d_1=q_{01},\quad d_2=q_{02},\quad
\beta=q_{21}-q_{01}\ge0,\quad
\gamma=q_{12}-q_{02}\ge0,
\]

\[
\alpha=q_{01}+q_{10}+q_{12},
\qquad
\delta=q_{02}+q_{20}+q_{21}.
\]

The active block is

\[
A=\begin{pmatrix}-\alpha&\beta\\\gamma&-\delta\end{pmatrix}.
\]

Its determinant is

\[
\begin{aligned}
\det A
={}&(q_{01}+q_{10}+q_{12})(q_{02}+q_{20}+q_{21})
-(q_{21}-q_{01})(q_{12}-q_{02})\\
={}&q_{01}q_{12}+q_{01}q_{20}+q_{01}q_{21}
+q_{02}q_{10}+q_{02}q_{12}+q_{02}q_{21}\\
&+q_{10}q_{20}+q_{10}q_{21}+q_{12}q_{20}\ge0.
\end{aligned}
\tag{5.2}
\]

Its discriminant is

\[
(\alpha-\delta)^2+4\beta\gamma\ge0,
\tag{5.3}
\]

so the two active eigenvalues are real and nonpositive. This will be used in the outgoing-row analysis.
