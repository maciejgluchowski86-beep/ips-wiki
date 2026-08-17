# 005d: binary suppression introduces no stronger condition

Date: 2026-08-17

This note executes Part E of Assignment 005. It checks the criterion after suppressing type `2`, both abstractly and on the exact three-state obstruction from `005c`.

## 1. Two-state interior transfer

With local states `{0,1}`, write

\[
u=c^{0\to1}(\mathbf0),
\qquad
w=c^{1\to0}(\mathbf0),
\qquad
r=u+w.
\]

The typed empty-target transfer is exactly

\[
K=
\begin{pmatrix}
0&0\\
u&-r
\end{pmatrix}.
\tag{1.1}
\]

There is no distinct active retyping entry. Thus the Part-A boundary-complete Metzler argument contributes **no additional binary inequality**: the sole off-diagonal entry is the physical deletion/activation coefficient `u>=0`, already automatic from physical-rate nonnegativity.

## 2. Binary outgoing row

For one nonempty target `S`, the Assignment-001/004 outgoing signed row is

\[
p=(p_0,p_1)
=\left(c^0(S),-c^0(S)-c^1(S)\right).
\tag{2.1}
\]

The `OO` zero-length condition is

\[
p_1\ge0
\iff
\boxed{c^0(S)+c^1(S)\le0.}
\tag{2.2}
\]

The physical value vector associated with `p` is

\[
g=(p_0,p_0+p_1)
=\left(c^0(S),-c^1(S)\right).
\tag{2.3}
\]

## 3. One decaying mode makes endpoint data sufficient

For `r>0`, the physical two-state chain has stationary probabilities

\[
\pi_0=\frac{w}{r},
\qquad
\pi_1=\frac{u}{r}.
\]

Starting from active physical state `1`, the binary `OI` numerator is

\[
N(t)=E_1[g(Z_t)].
\]

There is only one nonzero eigenvalue `-r`, so

\[
\boxed{
N(t)=L+\bigl(N(0)-L\bigr)e^{-rt},}
\tag{3.1}
\]

where

\[
N(0)=-c^1(S),
\]

and

\[
L=\pi(g)
=\frac{w c^0(S)-u c^1(S)}{r}.
\tag{3.2}
\]

Thus `N(t)` is affine in the single variable `e^{-rt} in [0,1]`; it is nonnegative for every `t>=0` exactly when both endpoint values are nonnegative.

Under (2.2), long-time nonnegativity is

\[
\boxed{w c^0(S)\ge u c^1(S).}
\tag{3.3}
\]

Equations (2.2) and (3.3) are precisely the canonical binary patch-positivity inequalities from the paper and Assignment 004.

As proved in `004e-binary-equivalence.md`, these two inequalities also imply the zero-length `OI` inequality `c^1(S)<=0`, so no extra endpoint condition remains.

When `r=0`, Assignment 004 already proved that the exact transfer conditions are equivalent to the canonical exceptional clause `c\equiv0`.

Therefore suppressing type `2` gives **exactly** the binary criterion and no stronger condition.

## 4. Suppression of the exact three-state obstruction

For the physical data of `005c`, suppress state `2` and discard target mode `2`. The surviving reference-neighbour rates are

\[
u=q_{01}=0,
\qquad
w=q_{10}=\frac74.
\]

For target mode `1`, the surviving binary rate coefficients are

\[
c^0(S)=\widehat c^{01}(1)=0,
\qquad
c^1(S)=\widehat c^{10}(1)=-\frac98.
\]

Hence

\[
c^0(S)+c^1(S)=-\frac98\le0,
\]

and

\[
w c^0(S)=0=u c^1(S).
\]

So the suppressed system satisfies the exact binary coefficient criterion.

The interior-time negative numerator from `005c` therefore genuinely uses the additional active state and its second decaying mode; it is not a disguised failure already present in the binary subsystem.

## 5. Acceptance test

Part E passes exactly:

- no new active-retyping inequality survives in `d=2`;
- the all-length transfer condition is equivalent to the canonical two coefficient inequalities (plus the canonical `r=0` clause);
- the concrete obstruction becomes binary patch-positive after suppressing type `2`.

Thus the Assignment-005 stop is **not** `STOP-BINARY-POSITIVITY-MISMATCH`. The correct frozen outcome remains the three-state interior-time obstruction `STOP-NO-FINITE-ENDPOINT-CRITERION`.
