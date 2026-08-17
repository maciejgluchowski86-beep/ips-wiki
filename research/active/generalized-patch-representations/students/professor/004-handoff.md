# Assignment 004 handoff

Date: 2026-08-17

Outcome: **`CONTINUE-TYPED-POSITIVITY-CRITERION`**.

## Decisive result

For every site `i`, the weighted interior source-line transfer is the finite matrix `K_i` with

\[
K_i(0,\cdot)=0,
\qquad
K_i(r,s)=a_{i,r}^s(\emptyset),\quad r\in E_*.
\]

The cancellation is exact:

\[
\text{empty-target jump subtraction}
+	ext{ nonempty-target killing}
+	ext{ FK potential}
\longrightarrow a_{i,r}^r(\emptyset).
\]

The unsigned consistency transfer is the killed Markov matrix

\[
B_i(r,s)=|a_{i,r}^s(\emptyset)|\quad(s\ne r),
\]

\[
B_i(r,r)=
-\sum_{s\ne r}|a_{i,r}^s(\emptyset)|
-\sum_{\tau\ne\emptyset}\sum_s|a_{i,r}^s(\tau)|,
\]

with zero inactive row.

## Four exact numerators

Let

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T,
\]

and for an outgoing initial descriptor

\[
\mathbf a_{r,\tau}=(a_{i,r}^s(\tau))_{s\in E}.
\]

Bulk nonnegativity is exactly:

\[
e_a e^{tK_i}f_b^I\ge0,
\qquad
e_a e^{tK_i}f_r^O\ge0,
\]

\[
\mathbf a_{r,\tau}e^{tK_i}f_b^I\ge0,
\qquad
\mathbf a_{r,\tau}e^{tK_i}f_{r_e}^O\ge0,
\]

for every realizable descriptor and `t>0`.

The corresponding denominators use `B_i` and absolute outgoing initial vectors and are strictly positive on realized descriptors.

## Small-time information

New multi-state necessary conditions include, whenever the descriptor is realizable,

\[
a_{i,a}^{r}(\emptyset)\ge0
\quad(a\ne r)
\]

from short `IO` patches, and

\[
a_{i,r}^{r_e}(\tau)\ge0
\]

from zero-length `OO` limits.

Full derivative formulas are in `004d-small-time-necessary-conditions.md`.

## Binary acceptance test

The `d=2` specialization is exactly the canonical patch formula. For

\[
r_i=c_i^0(\emptyset)+c_i^1(\emptyset)>0,
\]

all-length transfer positivity is equivalent to

\[
c_i^0(S)+c_i^1(S)\le0,
\]

\[
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S),
\]

for every nonempty `S`. If `r_i=0`, it is equivalent to `c_i\equiv0`.

Thus there is no binary mismatch.

## Final finite verifier

`004-typed-transfer-verifier.py`, final commit `0bbfccd0`.

The final `d=3` data are derived from actual nonnegative physical rates, not arbitrary signed dual rows. The verifier checks physical nonnegativity, direct `K`, direct `B`, four orientations, exact semigroup Taylor coefficients through order six, and the binary reduction using `Fraction` arithmetic only.

## Next mathematical edge

Do **not** move to applications yet.

The next bounded task is to characterize the exact all-length semigroup-positive family above by tractable coefficient inequalities or a natural structural subclass. Entrywise nonnegativity of `K_i` is not an acceptable replacement unless proved equivalent to the exact numerator family.

## Decisive files

- `004a-signed-interior-transfer.md`, commit `6248cc68`;
- `004b-unsigned-consistency-transfer.md`, commit `96197d46`;
- `004c-four-orientation-transfer-formulas.md`, commit `6f996224`;
- `004d-small-time-necessary-conditions.md`, commit `c24554c2`;
- `004e-binary-equivalence.md`, commit `f6485b2c`;
- verifier final commit `0bbfccd0`;
- final report `004-typed-bulk-positivity-transfer.md`, commit `be4429bc`.
