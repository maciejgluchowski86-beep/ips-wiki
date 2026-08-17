---
status: proved here
audit: current
---

# Three-state endpoint obstruction for typed patch positivity

This page records the boundary-complete `d=3` reduction and the exact obstruction found after the typed patch representation and transfer formulas were established.

It is a research-branch result on `research/generalized-patch-representations`; it is not published on `main`.

## Setting

Let the local state space be

\[
E=\{0,1,2\},
\]

with `0` the reference/inactive dual type. For one site, the exact signed interior transfer from the typed patch representation has generator

\[
K(0,\cdot)=0,
\qquad
K(r,s)=a_r^s(\emptyset),
\quad r\in\{1,2\}.
\]

For incoming terminal type `b` and outgoing terminal active type `r`, write

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T.
\]

For an outgoing initial record with signed hidden-outcome row

\[
p=(p_0,p_1,p_2),
\]

the remaining bulk numerators are

\[
p e^{tK}f_b^I,
\qquad
p e^{tK}f_r^O.
\]

## Boundary completeness forces a Metzler transfer

Let

\[
q_{xy}=c^{x\to y}(\mathbf0)
\]

be the physical replacement rates when every neighbour is in the reference state. Then

\[
K=
\begin{pmatrix}
0&0&0\\
q_{01}&-(q_{01}+q_{10}+q_{12})&q_{21}-q_{01}\\
q_{02}&q_{12}-q_{02}&-(q_{02}+q_{20}+q_{21})
\end{pmatrix}.
\]

If both active types occur as outgoing terminal types, a short incoming-initial/outgoing-terminal patch from active type `a` to distinct active type `r` has numerator

\[
e_a e^{tK}e_r^T=tK(a,r)+O(t^2).
\]

All-patch nonnegativity therefore forces

\[
q_{21}\ge q_{01},
\qquad
q_{12}\ge q_{02}.
\]

Together with the physical deletion entries `q_{01},q_{02}>=0`, every off-diagonal entry of `K` is nonnegative. Hence `K` is Metzler and

\[
e^{tK}\ge0
\]

entrywise for every `t>=0`.

Consequences:

- every incoming-initial `II/IO` numerator is automatically nonnegative;
- for an outgoing row, zero-length `OO/OI` constraints are
  \[
  p_1,p_2,p_0+p_1,p_0+p_2\ge0;
  \]
- the `OO` families are then automatically nonnegative for all time.

Only outgoing-initial/incoming-terminal (`OI`) numerators remain nontrivial.

## Physical Markov interpretation

Define the physical value vector

\[
g=(p_0,p_0+p_1,p_0+p_2).
\]

Let `Q` be the physical one-site generator at reference-neighbour configuration. The indicator-basis evaluation map intertwines the coefficient transfer and the physical generator, so

\[
\boxed{
p e^{tK}f_b^I=(e^{tQ}g)_b=E_b[g(Z_t)],
}
\]

where `Z` is the physical three-state chain with generator `Q`.

Thus the unresolved sign question is exactly whether a local Markov semigroup started from an active state can drive the expectation of a function that is nonnegative on active states but possibly negative on state `0` below zero at an intermediate time.

## Exact interior-time obstruction

Take

\[
Q=
\begin{pmatrix}
-1/4&0&1/4\\
7/4&-2&1/4\\
1/4&1/2&-3/4
\end{pmatrix}.
\]

The corresponding typed transfer is

\[
K=
\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\]

A one-neighbour physical rate table can be chosen so that all physical rates are nonnegative, both target labels occur with positive coarse rate from both active source types, and one outgoing row is

\[
p=(-1/8,9/8,1/4).
\]

Its value vector is

\[
g=(-1/8,1,1/8).
\]

The physical generator has spectrum `{0,-1,-2}`. For incoming terminal type `1`, the exact numerator is

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}.
\]

Both endpoint values are strictly positive:

\[
N(0)=1,
\qquad
\lim_{t\to\infty}N(t)=\frac1{128}.
\]

However, at

\[
e^{-t_*}=\frac{13}{153},
\]

one has

\[
\boxed{N(t_*)=-\frac1{1224}<0.}
\]

Thus zero-length and long-time coefficient inequalities do not characterize boundary-complete three-state typed patch positivity.

## Why this does not alter the binary criterion

After suppressing type `2`, there is only one nonzero decay mode. The remaining `OI` numerator is affine in `e^{-rt}`, so endpoint signs are sufficient. The resulting conditions are exactly the canonical binary patch-positivity inequalities

\[
c^0(S)+c^1(S)\le0,
\]

\[
c^1(\emptyset)c^0(S)
\ge c^0(\emptyset)c^1(S),
\]

with the same degenerate clause when the empty-neighbour total rate vanishes.

The three-state obstruction therefore reflects a genuinely new transient mode, not a strengthening of the binary property.

## Status of the criterion problem

The exact semigroup definition of typed bulk patch positivity remains valid. What fails is the direct binary-style collapse to endpoint inequalities.

In generic boundary-complete `d=3`, the remaining `OI` numerator has two real decaying modes,

\[
L+A e^{-\mu t}+B e^{-\nu t}.
\]

A later exact criterion must therefore retain the possible interior critical point rather than discard it.
