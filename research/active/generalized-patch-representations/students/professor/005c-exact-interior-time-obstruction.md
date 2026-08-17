# 005c: exact three-state interior-time obstruction

Date: 2026-08-17

This note executes the mandatory gate and gives the decisive counterexample for Assignment 005. It is an exact one-neighbour `d=3` physical IPS, not an arbitrary signed matrix.

## 1. Reference-neighbour physical rates

At a fixed source site, let the one neighbour have state `z in {0,1,2}`. When `z=0`, take physical replacement rates

\[
q_{01}=0,
\qquad q_{02}=\frac14,
\qquad q_{10}=\frac74,
\qquad q_{12}=\frac14,
\qquad q_{20}=\frac14,
\qquad q_{21}=\frac12.
\tag{1.1}
\]

Thus the physical one-site generator at reference neighbour state is

\[
Q=
\begin{pmatrix}
-\frac14&0&\frac14\\
\frac74&-2&\frac14\\
\frac14&\frac12&-\frac34
\end{pmatrix}.
\tag{1.2}
\]

The empty-target typed transfer from Assignment 004 is

\[
\boxed{
K=
\begin{pmatrix}
0&0&0\\
0&-2&\frac12\\
\frac14&0&-1
\end{pmatrix}.}
\tag{1.3}
\]

It is Metzler, exactly as Part A requires.

## 2. Two nonempty typed target modes

For neighbour target type `1`, choose indicator-basis rate coefficients

\[
\begin{array}{c|rrrrrr}
xy&01&02&10&12&20&21\\ \hline
\widehat c^{xy}(1)&0&-1/8&-9/8&1&-1/8&0.
\end{array}
\tag{2.1}
\]

For neighbour target type `2`, choose

\[
\begin{array}{c|rrrrrr}
xy&01&02&10&12&20&21\\ \hline
\widehat c^{xy}(2)&0&0&-1/8&0&-1/8&0.
\end{array}
\tag{2.2}
\]

Since there is only one neighbour, the physical rate at neighbour state `a` is the reference value (1.1) plus the coefficient in row `a`.

At neighbour state `1`, the six physical rates are

\[
0,\ \frac18,\ \frac58,\ \frac54,\ \frac18,\ \frac12,
\tag{2.3}
\]

and at neighbour state `2` they are

\[
0,\ \frac14,\ \frac{13}{8},\ \frac14,\ \frac18,\ \frac12.
\tag{2.4}
\]

Together with (1.1), all 18 one-neighbour physical rates are nonnegative.

The exact verifier `005-three-state-endpoint-obstruction-verifier.py` checks all 18 values directly.

## 3. Outgoing signed rows and boundary support

Using the Assignment-001 coefficient formulas, the nonempty target rows are

\[
\mathbf a_{1,1}=(0,1/8,0),
\tag{3.1}
\]

\[
\boxed{\mathbf a_{2,1}=(-1/8,9/8,1/4),}
\tag{3.2}
\]

\[
\mathbf a_{1,2}=(0,1/8,0),
\qquad
\mathbf a_{2,2}=(0,0,1/8).
\tag{3.3}
\]

Every pair `(source type r, target type a)` has positive coarse rate, so both active source types generate outgoing records and both incoming target labels occur. Every nonzero hidden source outcome in these rows has positive absolute branch rate. Under the boundary-complete test hypothesis, the corresponding `OO/OI` descriptors are therefore represented.

The zero-length constraints are satisfied for every row:

\[
p_1,p_2\ge0,
\qquad
p_0+p_1,p_0+p_2\ge0.
\tag{3.4}
\]

For the distinguished row (3.2),

\[
p=(-1/8,9/8,1/4),
\tag{3.5}
\]

so

\[
p_1=9/8>0,
\qquad p_2=1/4>0,
\]

\[
p_0+p_1=1>0,
\qquad p_0+p_2=1/8>0.
\tag{3.6}
\]

Thus the witness does not exploit a zero-length equality or derivative edge.

## 4. Exact two-mode semigroup

The characteristic polynomial of (1.2) is

\[
\lambda(\lambda+1)(\lambda+2).
\]

Put

\[
x=e^{-t}\in(0,1].
\]

Then

\[
e^{tQ}=P_0+xP_1+x^2P_2,
\tag{4.1}
\]

where

\[
P_0=
\begin{pmatrix}
11/16&1/16&1/4\\
11/16&1/16&1/4\\
11/16&1/16&1/4
\end{pmatrix},
\]

\[
P_1=
\begin{pmatrix}
3/8&-1/8&-1/4\\
3/8&-1/8&-1/4\\
-9/8&3/8&3/4
\end{pmatrix},
\]

\[
P_2=
\begin{pmatrix}
-1/16&1/16&0\\
-17/16&17/16&0\\
7/16&-7/16&0
\end{pmatrix}.
\tag{4.2}
\]

These matrices are the exact spectral projectors at eigenvalues `0,-1,-2`.

## 5. Distinguished `OI` numerator

The physical value vector associated with (3.5) is

\[
g=(p_0,p_0+p_1,p_0+p_2)
=(-1/8,1,1/8).
\tag{5.1}
\]

Take incoming terminal type `1`. By the Markov reduction (3.4) of `005b`, the required numerator is the physical semigroup expectation started from physical state `1`:

\[
N(t)=(e^{tQ}g)_1.
\]

Substituting (4.1)--(4.2) gives

\[
\boxed{
N(t)
=\frac1{128}
-\frac{13}{64}e^{-t}
+\frac{153}{128}e^{-2t}.}
\tag{5.2}
\]

The endpoint signs are strictly positive:

\[
N(0)=1>0,
\qquad
\lim_{t\to\infty}N(t)=\frac1{128}>0.
\tag{5.3}
\]

Nevertheless, as a quadratic in `x=e^{-t}`, (5.2) has its unique interior minimum at

\[
x_*=-\frac{-13/64}{2(153/128)}=\frac{13}{153}.
\tag{5.4}
\]

Equivalently

\[
t_*=\log\frac{153}{13}>0.
\]

At this exact point,

\[
\boxed{N(t_*)=-\frac1{1224}<0.}
\tag{5.5}
\]

Thus a required bulk `OI` contribution is negative at an interior length although all its zero-length and long-time endpoint inequalities hold strictly.

## 6. All other required families in the gate

The exact verifier checks every `OI` polynomial associated with (3.1)--(3.3) and both incoming terminal types.

The other `OI` polynomial for the distinguished row is

\[
\frac1{128}+\frac{39}{64}x-\frac{63}{128}x^2,
\]

which is nonnegative on `[0,1]` because it is concave and both endpoint values are nonnegative.

Every `OO` family is nonnegative for all time. This follows abstractly from the Metzler reduction and `p_1,p_2>=0`; the verifier also checks the exact quadratic forms.

For all other outgoing rows the verifier computes the exact quadratic minimum on `[0,1]` and obtains a nonnegative value.

Hence the only failure in the tested boundary-complete family is the intended interior-time `OI` dip (5.5), not a hidden endpoint or realizability defect.

## 7. Consequence for the pre-registered outcome

This is exactly the obstruction named in Assignment 005:

- all natural zero-length sign inequalities hold;
- the long-time `OI` limits are nonnegative, with the witness limit strictly positive;
- physical one-neighbour rates are nonnegative;
- the interior transfer is Metzler;
- both target labels and both active source types have positive nonempty-target support;
- yet a required numerator becomes negative at an interior time.

Therefore a binary-style criterion based only on zero-length and long-time coefficient inequalities does **not** characterize boundary-complete three-state typed patch positivity.

Under the frozen stop rule, this triggers

\[
\boxed{\texttt{STOP-NO-FINITE-ENDPOINT-CRITERION}.}
\]

The exact semigroup definition from Assignment 004 remains valid. What is refuted is the hoped-for endpoint collapse analogous to the binary theorem.
