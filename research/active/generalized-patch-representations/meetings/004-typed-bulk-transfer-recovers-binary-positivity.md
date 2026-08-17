# Meeting 004: typed bulk transfer recovers binary patch positivity

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- signed interior transfer `students/professor/004a-signed-interior-transfer.md`, commit `6248cc68`;
- unsigned consistency transfer `004b-unsigned-consistency-transfer.md`, commit `96197d46`;
- four orientation formulas `004c-four-orientation-transfer-formulas.md`, commit `6f996224`;
- small-time conditions `004d-small-time-necessary-conditions.md`, commit `c24554c2`;
- binary equivalence `004e-binary-equivalence.md`, commit `f6485b2c`;
- final exact verifier `004-typed-transfer-verifier.py`, commit `0bbfccd0`;
- final report `004-typed-bulk-positivity-transfer.md`, commit `be4429bc`;
- handoff `004-handoff.md`, commit `62b9a9fa`.

## Ruling

Assignment 004 ends

**`CONTINUE-TYPED-POSITIVITY-CRITERION`.**

The programme now has an exact finite-dimensional definition of bulk typed patch positivity for finite-state bounded finite-range single-site replacement dynamics, and it specializes exactly to the canonical binary patch-positivity property.

Neither registered stop condition occurs:

- `STOP-NO-LOCAL-TRANSFER` does not occur;
- `STOP-BINARY-POSITIVITY-MISMATCH` does not occur.

## 1. Signed interior transfer is exactly the empty-target coefficient matrix

For active local type `r`, let

\[
\rho_{i,r}=\sum_{s\ne r}|a_{i,r}^s(\emptyset)|,
\qquad
\kappa_{i,r}=\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|.
\]

The local potential is

\[
v_{i,r}=\rho_{i,r}+\kappa_{i,r}+a_{i,r}^r(\emptyset).
\]

The first-step weighted killed generator is

\[
\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
\bigl(\operatorname{sgn}a_{i,r}^s(\emptyset)F(s)-F(r)\bigr)
-\kappa_{i,r}F(r)+v_{i,r}F(r).
\]

The reference escape subtraction and nonempty-target killing cancel against the corresponding terms in the potential, leaving

\[
\boxed{(K_iF)(r)=\sum_s a_{i,r}^s(\emptyset)F(s),}
\qquad
(K_iF)(0)=0.
\]

This is the central structural simplification of the block.

## 2. Denominator transfer

The consistency normalizer uses instead the killed Markov generator

\[
(B_iF)(r)
=
\sum_{s\ne r}|a_{i,r}^s(\emptyset)|[F(s)-F(r)]
-\kappa_{i,r}F(r),
\]

with zero inactive row.

The denominator is positive precisely on source-line descriptors reachable through positive-rate empty-target transitions, subject also to the outer skeleton boundary intensities.

## 3. Four exact numerator families

Put

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T,
\]

and

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E}.
\]

Then the four bulk contributions are ratios with signed transfer `e^{tK_i}` in the numerator and killed reference transfer `e^{tB_i}` in the denominator. Therefore, on realizable descriptors, bulk positivity is exactly

\[
e_a e^{tK_i}f_b^I\ge0,
\qquad
e_a e^{tK_i}f_r^O\ge0,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I\ge0,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O\ge0
\]

for every `t>0`.

This exact semigroup-positive family is now the definition of **typed bulk patch positivity** in the current theory. No entrywise-positive matrix condition is substituted for it.

## 4. Multi-state short-time constraints

The transfer family exposes constraints with no binary counterpart. In particular, whenever the corresponding descriptors are realizable,

\[
a_{i,a}^{r}(\emptyset)\ge0
\quad(a\ne r)
\]

is forced by short incoming--outgoing patches, while zero-length outgoing--outgoing limits force

\[
a_{i,r}^{r_e}(\tau)\ge0.
\]

The final verifier deliberately includes a genuine IPS coefficient set with

\[
a_{1}^{2}(\emptyset)=-1,
\]

and obtains

\[
N_{IO}(0)=D_{IO}(0)=0,
\qquad
N'_{IO}(0)=-1,
\qquad
D'_{IO}(0)=1.
\]

Thus the new criterion detects a real multi-state obstruction.

## 5. Finite gate correction and verification target

An initial draft of the finite gate used signed dual rows which were algebraically consistent but not jointly realizable as empty-neighbour coefficients of one physical three-state generator. This was caught before closing the assignment.

The final verifier at commit `0bbfccd0` reconstructs all typed rows from an actual one-neighbour physical generator with nonnegative rates. It checks the physical rates themselves before testing transfer identities.

## 6. Binary benchmark passes exactly

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
K_i=\begin{pmatrix}0&0\\u&-r\end{pmatrix},
\]

which gives exactly the paper's `psi_i(t,1)`. The denominator matrix gives exactly `varphi_i(t)`.

For nonempty target `S`, the outgoing signed vector is

\[
(c_i^0(S),-c_i^0(S)-c_i^1(S)).
\]

Thus the typed `OI` and `OO` numerators are exactly the canonical ones.

When `r>0`, all-length positivity is equivalent to

\[
c_i^0(S)+c_i^1(S)\le0,
\]

\[
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S).
\]

When `r=0`, the transfer conditions are equivalent to `c_i\equiv0`.

This is precisely the coefficient criterion in the canonical patch paper. The generalized notion therefore passes the required honesty check.

## 7. Direction after this meeting

The principal asked for generalized patch positivity, but applications were explicitly listed downstream and Assignment 004 prohibited starting them here.

The next mathematical edge is therefore **coefficient characterization of the exact typed semigroup-positive family**, not applications or convergence.

A useful next block should determine whether the all-length inequalities can be reduced to finite/local coefficient conditions for a nontrivial multi-state class, or prove that no comparably simple coefficient criterion exists without additional structure.

Entrywise nonnegativity of `K_i` is not an acceptable definition unless proved equivalent to the exact four numerator families.

No literature novelty claim is made yet. A targeted literature audit remains necessary once the generalized positivity theorem is stable enough to compare precisely.
