# 004c: four typed bulk transfer formulas

Date: 2026-08-17

This note executes Part C of Assignment 004, using the signed transfer `K_i` from 004a and the killed reference transfer `B_i` from 004b.

## 1. Boundary vectors

Fix a source site `i` and a bulk patch length

\[
t=e(P)-b(P)>0.
\]

For `x in E`, let `e_x` denote the coordinate row vector and `e_x^T` the corresponding column.

### Incoming initial boundary

If the patch starts incoming with type `a in E_*`, the initial local state is deterministic:

\[
\mu_a^{I}=e_a.
\tag{1.1}
\]

The signed and unsigned initial vectors coincide.

### Outgoing initial boundary

Suppose the patch starts at a selected outgoing record with revealed pre-source type `r in E_*` and nonempty typed target `tau`.

Write

\[
\mathbf a_{i,r,\tau}
=\bigl(a_{i,r}^{s}(\tau)\bigr)_{s\in E},
\qquad
|\mathbf a_{i,r,\tau}|
=\bigl(|a_{i,r}^{s}(\tau)|\bigr)_{s\in E}.
\tag{1.2}
\]

The coarse selected-record rate is

\[
\Lambda_{i,r}(\tau)
=\sum_s|a_{i,r}^{s}(\tau)|.
\]

Under the reference patch law the hidden outcome has row vector

\[
\mu_{r,\tau}^{O,ref}
=\frac{|\mathbf a_{i,r,\tau}|}{\Lambda_{i,r}(\tau)}.
\tag{1.3}
\]

Multiplying by the outgoing-start branch sign changes this to the signed weighted row vector

\[
\mu_{r,\tau}^{O,sgn}
=\frac{\mathbf a_{i,r,\tau}}{\Lambda_{i,r}(\tau)}.
\tag{1.4}
\]

The common factor `1/Lambda` cancels in the normalized contribution.

### Incoming terminal boundary

If the terminal record is incoming with target type `b in E_*`, consistency is

\[
X_{t-}\in\{0,b\}.
\]

Thus the terminal column is

\[
f_b^I=e_0^T+e_b^T.
\tag{1.5}
\]

### Outgoing terminal boundary

If the terminal record is outgoing with revealed pre-source type `r_e in E_*`, consistency requires

\[
X_{t-}=r_e,
\]

so

\[
f_{r_e}^O=e_{r_e}^T.
\tag{1.6}
\]

## 2. General ratio principle

For any initial signed row `u`, reference row `u_ref`, and terminal consistency column `f`, Assignment 003 and the definitions of `K_i,B_i` give

\[
\text{unnormalized signed bulk weight}
=u e^{tK_i}f,
\]

\[
P_P(Con(P))
=u_{ref}e^{tB_i}f.
\]

Hence, on every realizable descriptor for which the denominator is positive,

\[
C(P)=\frac{u e^{tK_i}f}{u_{ref}e^{tB_i}f}.
\tag{2.1}
\]

## 3. Four orientations

### II: incoming start, incoming terminal

For initial incoming type `a` and terminal incoming type `b`,

\[
\boxed{
C_{II}(a,b;t)
=
\frac{e_a e^{tK_i}f_b^I}
{e_a e^{tB_i}f_b^I}.}
\tag{3.1}
\]

### IO: incoming start, outgoing terminal

For initial incoming type `a` and terminal outgoing source type `r_e`,

\[
\boxed{
C_{IO}(a,r_e;t)
=
\frac{e_a e^{tK_i}f_{r_e}^O}
{e_a e^{tB_i}f_{r_e}^O}.}
\tag{3.2}
\]

### OI: outgoing start, incoming terminal

For outgoing initial descriptor `(r,tau)` and incoming terminal type `b`,

\[
\boxed{
C_{OI}(r,\tau;b;t)
=
\frac{\mathbf a_{i,r,\tau}e^{tK_i}f_b^I}
{|\mathbf a_{i,r,\tau}|e^{tB_i}f_b^I}.}
\tag{3.3}
\]

### OO: outgoing start, outgoing terminal

For outgoing initial descriptor `(r,tau)` and outgoing terminal source type `r_e`,

\[
\boxed{
C_{OO}(r,\tau;r_e;t)
=
\frac{\mathbf a_{i,r,\tau}e^{tK_i}f_{r_e}^O}
{|\mathbf a_{i,r,\tau}|e^{tB_i}f_{r_e}^O}.}
\tag{3.4}
\]

The selected-record normalizer `Lambda_{i,r}(tau)` is absent from (3.3)--(3.4) because it multiplies numerator and denominator equally.

## 4. Exact positivity family

By 004b, every denominator in (3.1)--(3.4) is strictly positive exactly on a realizable bulk descriptor. Therefore bulk patch nonnegativity is equivalent to the following numerator inequalities, only where the corresponding denominator is positive:

\[
\boxed{
e_a e^{tK_i}f_b^I\ge0,}
\tag{4.1}
\]

\[
\boxed{
e_a e^{tK_i}f_{r_e}^O\ge0,}
\tag{4.2}
\]

\[
\boxed{
\mathbf a_{i,r,\tau}e^{tK_i}f_b^I\ge0,}
\tag{4.3}
\]

\[
\boxed{
\mathbf a_{i,r,\tau}e^{tK_i}f_{r_e}^O\ge0.}
\tag{4.4}
\]

These inequalities, for every site, finite bulk descriptor, and length `t>0`, are the **exact transfer characterization** of bulk patch positivity in the present finite-state single-site replacement theory.

No entrywise nonnegativity of `K_i` or `e^{tK_i}` has been imposed. Such a condition would generally be stronger than (4.1)--(4.4) and is not the generalized definition unless later proved equivalent.

## 5. Boundary length zero

The formulas admit right limits as `t downarrow 0` obtained by replacing `e^{tK_i}` and `e^{tB_i}` with the identity. These limits and their first derivatives are analyzed in 004e. They are useful necessary conditions but are not substituted for the exact all-length family above.
