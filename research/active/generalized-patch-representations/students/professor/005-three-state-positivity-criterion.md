# Assignment 005 report: three-state typed positivity has an interior-time obstruction

Date: 2026-08-17

Outcome:

**`STOP-NO-FINITE-ENDPOINT-CRITERION`.**

The exact typed semigroup positivity definition from Assignment 004 remains valid. What fails is the hoped-for binary-style reduction to zero-length and long-time coefficient inequalities already in boundary-complete `d=3`.

## 1. Interior transfer becomes Metzler under boundary completeness

Let

\[
q_{xy}=c^{x\to y}(\mathbf0)
\]

be the physical local replacement rates at reference-neighbour configuration. The empty-target transfer is

\[
K=
\begin{pmatrix}
0&0&0\\
q_{01}&-(q_{01}+q_{10}+q_{12})&q_{21}-q_{01}\\
q_{02}&q_{12}-q_{02}&-(q_{02}+q_{20}+q_{21})
\end{pmatrix}.
\]

Boundary completeness makes every incoming-active to outgoing-active short patch realizable. Therefore, for distinct active types `a,r`,

\[
e_a e^{tK}e_r^T=tK(a,r)+O(t^2)\ge0
\]

forces

\[
K(a,r)\ge0.
\]

The deletion entries `K(r,0)` are physical nonnegative rates, so every off-diagonal entry of `K` is nonnegative. Hence `K` is Metzler and

\[
e^{tK}\ge0
\]

entrywise for every `t>=0`.

Consequently all incoming-initial `II/IO` numerator families are automatically nonnegative.

Decisive note: `005a-metzler-incoming-reduction.md`, commit `f8a73319`.

## 2. Outgoing zero-length constraints

For an outgoing row

\[
p=(p_0,p_1,p_2)=\mathbf a_{r,\tau},
\]

boundary completeness gives the zero-length requirements

\[
p_1\ge0,
\qquad p_2\ge0,
\]

from `OO`, and

\[
p_0+p_1\ge0,
\qquad p_0+p_2\ge0
\]

from `OI`.

Because `e^{tK}` is nonnegative and its inactive row cannot reach active columns, the `OO` families are then nonnegative for all time. Thus only outgoing-initial/incoming-terminal (`OI`) numerators remain nontrivial.

## 3. Exact Markov-semigroup reduction

Let `Q` be the physical local generator at reference-neighbour configuration. For coefficient row `p`, define

\[
g=(p_0,p_0+p_1,p_0+p_2).
\]

With

\[
R=
\begin{pmatrix}
1&0&0\\
1&1&0\\
1&0&1
\end{pmatrix},
\]

a direct calculation gives

\[
R K^T=Q R.
\]

Therefore the remaining `OI` numerator is exactly

\[
\boxed{
p e^{tK}f_b^I=(e^{tQ}g)_b=E_b[g(Z_t)].}
\]

Under the Metzler conditions the two nonzero eigenvalues are real. Generically each numerator has two decaying modes:

\[
L+A e^{\lambda_+t}+B e^{\lambda_-t}.
\]

This is the structural difference from the binary case, which has only one decaying mode.

Decisive note: `005b-outgoing-row-markov-reduction.md`, commit `a4f36bd`.

## 4. Exact physically realizable counterexample

Use one neighbour and reference-neighbour physical rates

\[
q_{01}=0,
\quad q_{02}=1/4,
\quad q_{10}=7/4,
\quad q_{12}=1/4,
\quad q_{20}=1/4,
\quad q_{21}=1/2.
\]

Thus

\[
Q=
\begin{pmatrix}
-1/4&0&1/4\\
7/4&-2&1/4\\
1/4&1/2&-3/4
\end{pmatrix},
\qquad
K=
\begin{pmatrix}
0&0&0\\
0&-2&1/2\\
1/4&0&-1
\end{pmatrix}.
\]

For target type `1`, use physical-rate indicator coefficients

\[
(\widehat c^{01},\widehat c^{02},\widehat c^{10},
\widehat c^{12},\widehat c^{20},\widehat c^{21})
=(0,-1/8,-9/8,1,-1/8,0).
\]

For target type `2`, use

\[
(0,0,-1/8,0,-1/8,0).
\]

All 18 physical rates at neighbour states `0,1,2` are nonnegative.

The four outgoing signed rows are

\[
\mathbf a_{1,1}=(0,1/8,0),
\]

\[
\mathbf a_{2,1}=(-1/8,9/8,1/4),
\]

\[
\mathbf a_{1,2}=(0,1/8,0),
\qquad
\mathbf a_{2,2}=(0,0,1/8).
\]

Both target labels and both active source types have positive coarse nonempty-target rate. All zero-length `OO/OI` inequalities hold for every row.

## 5. Interior-time negative contribution with positive endpoints

For the distinguished row

\[
p=(-1/8,9/8,1/4),
\]

the value vector is

\[
g=(-1/8,1,1/8).
\]

The physical generator has spectrum `{0,-1,-2}`. For incoming terminal type `1`, exact spectral projection gives

\[
\boxed{
N(t)
=\frac1{128}-\frac{13}{64}e^{-t}
+\frac{153}{128}e^{-2t}.}
\]

The endpoint data are strictly positive:

\[
N(0)=1,
\qquad
N(\infty)=1/128.
\]

But at

\[
e^{-t_*}=13/153,
\qquad t_*=\log(153/13),
\]

one has

\[
\boxed{N(t_*)=-1/1224<0.}
\]

Thus the exact typed patch contribution is negative at an interior patch length despite the binary-style endpoint inequalities being satisfied.

The verifier checks all other `OI` and `OO` families in the constructed gate exactly; none has another hidden negative minimum.

Decisive note: `005c-exact-interior-time-obstruction.md`, commit `3d8778ac`.

Exact verifier: `005-three-state-endpoint-obstruction-verifier.py`, commit `fc8c999e`.

## 6. Binary suppression passes exactly

Suppress type `2`. The Part-A active-retyping condition disappears because only one active type remains.

Abstractly, with

\[
u=c^{0\to1}(\mathbf0),
\qquad w=c^{1\to0}(\mathbf0),
\]

the binary `OI` numerator has only one decaying mode:

\[
N(t)=L+\bigl(-c^1(S)-L\bigr)e^{-(u+w)t},
\]

where

\[
L=\frac{w c^0(S)-u c^1(S)}{u+w}.
\]

Therefore endpoint nonnegativity is exactly the canonical criterion

\[
c^0(S)+c^1(S)\le0,
\]

\[
w c^0(S)\ge u c^1(S),
\]

with the canonical `u+w=0` exceptional clause from Assignment 004.

For the concrete witness, suppression gives

\[
u=0,
\qquad w=7/4,
\qquad c^0(S)=0,
\qquad c^1(S)=-9/8,
\]

which satisfies both binary inequalities. Thus the three-state obstruction is not produced by strengthening or corrupting the binary criterion.

Decisive note: `005d-binary-suppression.md`, commit `ffdb1929`.

## 7. Interpretation of the stop

The stop is specific:

- the exact typed bulk positivity property from Assignment 004 is not refuted;
- the finite-state patch representation is not refuted;
- boundary completeness gives a useful Metzler reduction;
- the binary criterion remains exactly embedded;
- what fails is a criterion controlled only by zero-length and long-time coefficient data.

The obstruction is the second transient mode of the three-state physical local chain. Two decaying exponentials can cancel at an interior time even when both endpoint values are positive.

A later block could, if judged worthwhile, derive a finite **spectral critical-point** test which explicitly checks the possible interior minimum. That would be a different criterion from the binary-style endpoint collapse stopped here.

Applications and convergence were not started in this assignment.
