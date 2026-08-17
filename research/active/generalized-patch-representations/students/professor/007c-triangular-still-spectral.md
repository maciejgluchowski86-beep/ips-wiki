# 007c: one-way active retyping remains genuinely spectral

Date: 2026-08-17

This note executes Part C of Assignment 007.

## 1. Triangular active block

The proposed class has exactly one vanishing active retyping entry. After ordering active types appropriately, the active block is

\[
A=\begin{pmatrix}-\alpha&\beta\\0&-\delta\end{pmatrix},
\qquad \beta>0.
\]

Unless `alpha=delta`, its semigroup contains two distinct decay modes. There is no structural reason for an outgoing `OI` row to kill either mode.

## 2. The Assignment-005 obstruction already lies in this class

The exact physically realizable reference-neighbour transfer from Assignment 005 is

\[
K=
\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\tag{2.1}
\]

Hence

\[
K(1,2)=1/2>0,
\qquad
K(2,1)=0.
\]

This is exactly one-way active retyping.

For the outgoing row

\[
p=(-1/8,9/8,1/4)
\]

and incoming terminal type `1`, the exact `OI` numerator is

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}.
\tag{2.2}
\]

The zero-length and long-time values are positive,

\[
N(0)=1,
\qquad
N(\infty)=1/128,
\]

but at

\[
e^{-t_*}=13/153
\]

one has

\[
N(t_*)=-1/1224<0.
\tag{2.3}
\]

All physical one-neighbour rates are nonnegative, and the full boundary-complete gate was independently verified in Assignment 005.

## 3. Classification

Therefore triangularity by itself does not turn the exact Assignment-006 criterion into endpoint algebra. The generic two-mode critical comparison survives inside a physically natural irreversible-retyping class.

The only way a triangular active block becomes one-mode for every outgoing row is spectral degeneracy (`alpha=delta`) or elimination of one mode by the tested observable. The former belongs to the repeated-spectrum mechanism isolated in `007b`; the latter is an observable reduction and can be binary-reducible.

Thus one-way retyping is classified as **still spectral**, not as a surviving simplification.
