# Assignment 004 report: typed bulk transfer matrices and positivity target

Date: 2026-08-17

Outcome: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

## 1. Exact signed interior transfer

Fix site `i`. For active local type `r in E_*`, define

\[
\rho_{i,r}=\sum_{s\ne r}|a_{i,r}^s(\emptyset)|,
\qquad
\kappa_{i,r}=\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|.
\]

The local potential from Assignment 001 is

\[
v_{i,r}=\rho_{i,r}+\kappa_{i,r}+a_{i,r}^r(\emptyset).
\]

A first-step calculation for the weighted source-line process gives

\[
\begin{aligned}
(K_iF)(r)
={}&\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
\bigl(\operatorname{sgn}a_{i,r}^s(\emptyset)F(s)-F(r)\bigr)\\
&-\kappa_{i,r}F(r)+v_{i,r}F(r).
\end{aligned}
\]

The absolute-rate subtraction, nonempty-target no-success killing, and potential cancel exactly, leaving

\[
\boxed{(K_iF)(r)=\sum_{s\in E}a_{i,r}^s(\emptyset)F(s),}
\qquad
\boxed{(K_iF)(0)=0.}
\]

Thus the unnormalized signed interior transfer is exactly `e^{tK_i}`, where every active row of `K_i` is the empty-target signed coefficient row.

Decisive note: `004a-signed-interior-transfer.md`, commit `6248cc68`.

## 2. Exact unsigned consistency transfer

Without signs or Feynman--Kac potential, the killed reference generator is

\[
\boxed{
(B_iF)(r)
=\sum_{s\ne r}|a_{i,r}^s(\emptyset)|[F(s)-F(r)]
-\kappa_{i,r}F(r),}
\]

with `(B_iF)(0)=0`.

Hence

\[
B_i(r,s)=|a_{i,r}^s(\emptyset)|\quad(s\ne r),
\]

\[
B_i(r,r)=-(\rho_{i,r}+\kappa_{i,r}).
\]

The denominator transfer is `e^{tB_i}`. Its entries are nonnegative. A denominator is strictly positive exactly when the corresponding source-line initial support can reach the terminal consistency set through positive-rate empty-target transitions; finite killing does not alter reachability.

Decisive note: `004b-unsigned-consistency-transfer.md`, commit `96197d46`.

## 3. Four exact bulk formulas

Let `e_x` be the coordinate row. Define terminal columns

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T.
\]

For an outgoing initial record `(i,.,r,tau)`, define

\[
\mathbf a_{i,r,\tau}=(a_{i,r}^s(\tau))_{s\in E},
\qquad
|\mathbf a_{i,r,\tau}|=(|a_{i,r}^s(\tau)|)_{s\in E}.
\]

The selected-record normalizer `Lambda_{i,r}(tau)` cancels between numerator and denominator. Therefore every realizable bulk patch has contribution

\[
\boxed{
C_{II}(a,b;t)=
\frac{e_a e^{tK_i}f_b^I}
{e_a e^{tB_i}f_b^I},}
\]

\[
\boxed{
C_{IO}(a,r_e;t)=
\frac{e_a e^{tK_i}f_{r_e}^O}
{e_a e^{tB_i}f_{r_e}^O},}
\]

\[
\boxed{
C_{OI}(r,\tau;b;t)=
\frac{\mathbf a_{i,r,\tau}e^{tK_i}f_b^I}
{|\mathbf a_{i,r,\tau}|e^{tB_i}f_b^I},}
\]

\[
\boxed{
C_{OO}(r,\tau;r_e;t)=
\frac{\mathbf a_{i,r,\tau}e^{tK_i}f_{r_e}^O}
{|\mathbf a_{i,r,\tau}|e^{tB_i}f_{r_e}^O}.}
\]

Since the denominators are positive on realized descriptors, bulk patch positivity is exactly the family of four numerator inequalities

\[
e_a e^{tK_i}f_b^I\ge0,
\qquad
e_a e^{tK_i}f_r^O\ge0,
\]

\[
\mathbf a_{i,r,\tau}e^{tK_i}f_b^I\ge0,
\qquad
\mathbf a_{i,r,\tau}e^{tK_i}f_{r_e}^O\ge0,
\]

for every realizable descriptor and every `t>0`.

This is an exact characterization of `C(P)>=0`, not a sufficient entrywise-positive-matrix replacement.

Decisive note: `004c-four-orientation-transfer-formulas.md`, commit `6f996224`.

## 4. Small-time necessary conditions

The zero-length and first-derivative expansions give immediate diagnostics.

For `II`,

\[
N_{II}(a,b;0)=1_{\{a=b\}},
\]

\[
N'_{II}(a,b;0)
=a_{i,a}^0(\emptyset)+a_{i,a}^b(\emptyset).
\]

For `IO`,

\[
N_{IO}(a,r;0)=1_{\{a=r\}},
\qquad
N'_{IO}(a,r;0)=a_{i,a}^{r}(\emptyset).
\]

Thus a realizable direct retyping `a -> r`, `a!=r`, forces

\[
a_{i,a}^{r}(\emptyset)\ge0.
\]

For `OI`,

\[
N_{OI}(r,\tau;b;0)
=a_{i,r}^0(\tau)+a_{i,r}^{b}(\tau),
\]

and

\[
N'_{OI}(0)
=\sum_{s\in E_*}a_{i,r}^{s}(\tau)
\bigl(a_{i,s}^{0}(\emptyset)+a_{i,s}^{b}(\emptyset)\bigr).
\]

For `OO`,

\[
N_{OO}(r,\tau;r_e;0)=a_{i,r}^{r_e}(\tau),
\]

\[
N'_{OO}(0)
=\sum_{s\in E_*}a_{i,r}^{s}(\tau)a_{i,s}^{r_e}(\emptyset).
\]

Hence every realizable zero-length active hidden outcome forces

\[
a_{i,r}^{r_e}(\tau)\ge0.
\]

These retyping constraints have no analogue in the binary theory.

Decisive note: `004d-small-time-necessary-conditions.md`, commit `c24554c2`.

## 5. Mandatory `d=3` finite gate

Final verifier:

`004-typed-transfer-verifier.py`, commit `0bbfccd0`.

The final gate uses an actual one-neighbour three-state physical generator. Empty-neighbour physical rates are

\[
c^{01}=2,\quad c^{02}=1,\quad c^{10}=1,
\quad c^{12}=3,\quad c^{20}=2,\quad c^{21}=1,
\]

and the neighbour-`1` tensor-mode coefficients are

\[
\widehat c^{01}=1,\quad \widehat c^{02}=1,\quad
\widehat c^{10}=0,\quad \widehat c^{12}=1,
\quad \widehat c^{20}=-1,\quad \widehat c^{21}=2.
\]

All physical rates at neighbour states `0` and `1` are nonnegative; the unused neighbour-`2` coefficient is zero.

The resulting signed empty-target rows are

\[
(2,-6,-1),
\qquad
(1,2,-4),
\]

and the nonempty target rows are

\[
(1,-2,1),
\qquad
(1,0,-2).
\]

Thus

\[
K=
\begin{pmatrix}
0&0&0\\
2&-6&-1\\
1&2&-4
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0&0\\
2&-7&1\\
1&2&-6
\end{pmatrix}.
\]

The gate checks physical nonnegativity, direct first-step `K`, direct first-step `B`, all four boundary value/derivative formulas, exact semigroup Taylor coefficients through order six against the independent first-step recurrence, and a separate binary specialization. All arithmetic is `Fraction`; there are no floating-point positivity decisions.

The selected `IO` descriptor deliberately fails typed patch positivity:

\[
N(0)=D(0)=0,
\qquad
N'(0)=-1,
\qquad
D'(0)=1.
\]

Thus the transfer criterion detects a genuine multi-state sign obstruction.

## 6. Binary equivalence

For `d=2`, write

\[
u=c_i^0(\emptyset),
\qquad
w=c_i^1(\emptyset),
\qquad
r=u+w.
\]

Then

\[
K_i=
\begin{pmatrix}
0&0\\
u&-r
\end{pmatrix},
\]

and the transfer functions are exactly the canonical

\[
\psi_i(t,1)=\frac{u}{r}+\frac{w}{r}e^{-rt}
\]

and `varphi_i(t)` from the paper.

For a nonempty binary target `S`,

\[
\mathbf a_{i,1,S}
=\bigl(c_i^0(S),-c_i^0(S)-c_i^1(S)\bigr).
\]

The four typed formulas reduce exactly to the paper's `II`, `IO`, `OI`, `OO` full-patch formulas.

If `r>0`, all-length `OO` positivity is exactly

\[
c_i^0(S)+c_i^1(S)\le0.
\]

Under this condition, the `OI` numerator is minimized at infinite length and its limiting nonnegativity is exactly

\[
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S).
\]

These are precisely the two inequalities in the canonical theorem.

If `r=0`, transfer positivity forces every nonconstant coefficient of `c_i^1` and then of `c_i^0` to be nonpositive. Since both physical rate functions are nonnegative and their constant coefficients vanish, induction over neighbour supports gives

\[
c_i^0\equiv c_i^1\equiv0,
\]

exactly the paper's exceptional clause.

Thus the generalized all-length transfer family specializes **equivalently**, not merely sufficiently, to canonical binary patch positivity.

Decisive note: `004e-binary-equivalence.md`, commit `f6485b2c`.

## 7. Decision

The registered stop outcomes do not occur:

- `STOP-NO-LOCAL-TRANSFER`: refuted by the exact finite `K_i,B_i` transfers;
- `STOP-BINARY-POSITIVITY-MISMATCH`: refuted by the exact equivalence in Section 6.

Assignment 004 therefore ends

\[
\boxed{\texttt{CONTINUE-TYPED-POSITIVITY-CRITERION}.}
\]

The next bounded problem is **not applications**. It is to characterize the exact semigroup-positive numerator family by tractable local coefficient inequalities, or to identify a mathematically natural structural subclass for which those inequalities can be proved. The exact transfer family itself is already the correct definition of typed bulk patch positivity.
