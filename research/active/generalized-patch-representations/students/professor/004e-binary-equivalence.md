# 004e: exact binary specialization and positivity equivalence

Date: 2026-08-17

This note executes Part E of Assignment 004. It is the required honesty check against the canonical paper.

## 1. Binary transfer matrices

Set

\[
E=\{0,1\}.
\]

Write

\[
u=c_i^0(\emptyset),
\qquad
w=c_i^1(\emptyset),
\qquad
r=u+w.
\]

Physical flip rates give `u,w>=0`.

The two empty-target signed dual coefficients are

\[
a_{i,1}^{0}(\emptyset)=u,
\qquad
a_{i,1}^{1}(\emptyset)=-u-w=-r.
\]

Hence 004a gives

\[
\boxed{
K_i=
\begin{pmatrix}
0&0\\
u&-r
\end{pmatrix}.}
\tag{1.1}
\]

Let

\[
\kappa_i
=\sum_{S\ne\emptyset}
\left(|c_i^0(S)|+|c_i^0(S)+c_i^1(S)|\right)
\]

and

\[
\alpha_i=u+\kappa_i.
\]

Then 004b gives

\[
\boxed{
B_i=
\begin{pmatrix}
0&0\\
u&-\alpha_i
\end{pmatrix}.}
\tag{1.2}
\]

This `alpha_i` is exactly the total outgoing marked-interaction rate in `paper/appendices/patch-contributions.tex`.

## 2. Explicit semigroups

Assume first `r>0`. Then

\[
e_1e^{tK_i}e_1^T=e^{-rt}
\tag{2.1}
\]

and

\[
\begin{aligned}
e_1e^{tK_i}(e_0^T+e_1^T)
&=\frac{u}{r}+\frac{w}{r}e^{-rt}\\
&=u\int_0^t e^{-rs}\,ds+e^{-rt}\\
&=: \psi_i(t,1).
\end{aligned}
\tag{2.2}
\]

Likewise

\[
e_1e^{tB_i}e_1^T=e^{-\alpha_i t}
\tag{2.3}
\]

and

\[
\begin{aligned}
e_1e^{tB_i}(e_0^T+e_1^T)
&=e^{-\alpha_i t}
+u\int_0^t e^{-\alpha_i s}\,ds\\
&=: \varphi_i(t).
\end{aligned}
\tag{2.4}
\]

These are exactly the paper's functions `psi_i(t,1)` and `varphi_i(t)`.

When `r=0`, `u=w=0`, formula (2.2) is read as `psi_i(t,1)=1`, again exactly as in the paper.

## 3. Outgoing selected boundary vector

For a nonempty binary target `S`, 001b gives

\[
\mathbf a_{i,1,S}
=\bigl(c_i^0(S),-c_i^0(S)-c_i^1(S)\bigr).
\tag{3.1}
\]

Its unsigned reference vector is

\[
|\mathbf a_{i,1,S}|
=\bigl(|c_i^0(S)|,|c_i^0(S)+c_i^1(S)|\bigr)
=\bigl(\delta_i(S),\beta_i(S)\bigr).
\tag{3.2}
\]

Thus the four formulas of 004c become the canonical full-patch formulas.

### II

\[
C_{II}(t)
=\frac{\psi_i(t,1)}{\varphi_i(t)}.
\tag{3.3}
\]

### IO

Using `V_i=alpha_i-r`,

\[
C_{IO}(t)
=\frac{e^{-rt}}{e^{-\alpha_i t}}
=e^{V_i t}.
\tag{3.4}
\]

### OI

The numerator is

\[
\boxed{
c_i^0(S)
-\bigl(c_i^0(S)+c_i^1(S)\bigr)\psi_i(t,1),}
\tag{3.5}
\]

and the denominator is

\[
\delta_i(S)+\beta_i(S)\varphi_i(t),
\tag{3.6}
\]

up to the common selected-record normalizer, which cancels. This is the paper's `OI/OE` row.

### OO

The numerator is

\[
-\bigl(c_i^0(S)+c_i^1(S)\bigr)e^{-rt},
\tag{3.7}
\]

while the denominator is

\[
|c_i^0(S)+c_i^1(S)|e^{-\alpha_i t}.
\tag{3.8}
\]

Hence, whenever this descriptor is realizable,

\[
C_{OO}(t)
=\operatorname{sgn}_{\pm}\bigl(-c_i^0(S)-c_i^1(S)\bigr)e^{V_i t},
\tag{3.9}
\]

again exactly the canonical formula.

## 4. All-length positivity when `r>0`

The incoming contributions (3.3)--(3.4) are nonnegative automatically.

From (3.7), all `OO` patches are nonnegative if and only if

\[
\boxed{
c_i^0(S)+c_i^1(S)\le0}
\tag{4.1}
\]

for every nonempty `S`. If both coefficients in (3.1) vanish, the corresponding outgoing descriptor does not occur and (4.1) still holds with equality.

Assume (4.1). Put

\[
b_S=-c_i^0(S)-c_i^1(S)\ge0.
\]

Then the `OI` numerator is

\[
N_S(t)=c_i^0(S)+b_S\psi_i(t,1).
\tag{4.2}
\]

Since

\[
\psi_i(t,1)=\frac{u}{r}+\frac{w}{r}e^{-rt}
\]

is nonincreasing in `t` and `b_S>=0`, `N_S(t)` is minimized as `t -> infinity`. Its limiting value is

\[
\begin{aligned}
N_S(\infty)
&=c_i^0(S)-\frac{u}{r}\bigl(c_i^0(S)+c_i^1(S)\bigr)\\
&=\frac{w c_i^0(S)-u c_i^1(S)}{r}.
\end{aligned}
\tag{4.3}
\]

Therefore all `OI` patches are nonnegative for every length exactly when

\[
\boxed{
w c_i^0(S)\ge u c_i^1(S).}
\tag{4.4}
\]

Substituting back `u=c_i^0(emptyset)` and `w=c_i^1(emptyset)`, (4.1) and (4.4) are exactly

\[
c_i^0(S)+c_i^1(S)\le0,
\qquad
c_i^1(\emptyset)c_i^0(S)
\ge
c_i^0(\emptyset)c_i^1(S),
\tag{4.5}
\]

the coefficient criterion in Theorem `patch-positivity-order` of the canonical paper.

Thus, for `r>0`, the typed all-length transfer inequalities are **equivalent** to the paper's patch-positivity inequalities, not a stronger substitute.

## 5. Degenerate case `r=0`

Now `u=w=0`, so `psi_i(t,1)=1`. The `OO` condition remains

\[
c_i^0(S)+c_i^1(S)\le0.
\tag{5.1}
\]

The `OI` numerator becomes

\[
c_i^0(S)-c_i^0(S)-c_i^1(S)
=-c_i^1(S),
\]

so all `OI` patches require

\[
c_i^1(S)\le0
\tag{5.2}
\]

for every nonempty `S`.

Because `c_i^1(emptyset)=0` and the physical rate function `c_i^1(eta)` is nonnegative for every neighbour configuration, (5.2) forces `c_i^1` to vanish identically. Indeed, for a neighbour configuration with support `A`,

\[
c_i^1(A)=\sum_{S\subseteq A}c_i^1(S)\ge0.
\]

All nonconstant coefficients are nonpositive. Induction on `|A|` gives every coefficient zero: singleton values force singleton coefficients to zero, and after all proper subsets vanish the value on `A` forces `c_i^1(A)=c_i^1(A\text{ as coefficient})=0`.

With `c_i^1\equiv0`, condition (5.1) says every nonconstant coefficient of `c_i^0` is nonpositive. Since `c_i^0(emptyset)=0` and the physical rate function `c_i^0` is nonnegative, the same induction gives

\[
c_i^0\equiv0.
\]

Conversely, if `c_i\equiv0`, there are no outgoing records from `i` and every existing incoming patch contribution is nonnegative.

Hence the transfer condition at `r=0` is equivalent to the paper's exceptional clause

\[
\boxed{c_i\equiv0.}
\tag{5.3}
\]

## 6. Binary benchmark decision

Combining Sections 4--5:

> The all-length nonnegativity family (4.1)--(4.4) from the typed transfer representation specializes **exactly** to the canonical binary patch-positivity property, including the `r_i=0` degeneracy.

Therefore the Assignment-004 stop outcome `STOP-BINARY-POSITIVITY-MISMATCH` does not occur.
