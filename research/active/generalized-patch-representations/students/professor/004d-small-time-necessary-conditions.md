# 004d: small-time necessary conditions

Date: 2026-08-17

This note executes Part D of Assignment 004. It expands the exact numerator families from 004c at `t=0`. These are necessary conditions only; no sufficient cone is asserted.

Fix a site `i` and abbreviate

\[
K=K_i,
\qquad
p_{r,\tau}(s)=a_{i,r}^s(\tau).
\]

For active types `a,b,r in E_*`, recall

\[
f_b^I=e_0^T+e_b^T,
\qquad
f_r^O=e_r^T.
\]

Since

\[
e^{tK}=I+tK+O(t^2),
\]

every numerator has an explicit zero-length value and first derivative.

## 1. II: incoming -> incoming

\[
N_{II}(a,b;t)=e_a e^{tK}f_b^I.
\]

Therefore

\[
N_{II}(a,b;0)=1_{\{a=b\}},
\tag{1.1}
\]

and

\[
\boxed{
N'_{II}(a,b;0)
=K(a,0)+K(a,b)
=a_{i,a}^0(\emptyset)+a_{i,a}^b(\emptyset).}
\tag{1.2}
\]

If `a != b`, the numerator starts from zero. Whenever the corresponding descriptor is realizable to first order, i.e. the unsigned denominator has positive first derivative,

\[
|a_{i,a}^0(\emptyset)|+|a_{i,a}^b(\emptyset)|>0,
\]

all-patch nonnegativity forces

\[
\boxed{
a_{i,a}^0(\emptyset)+a_{i,a}^b(\emptyset)\ge0.}
\tag{1.3}
\]

If `a=b`, the numerator starts from `1`, so its first derivative gives no sign constraint by itself.

## 2. IO: incoming -> outgoing

\[
N_{IO}(a,r;t)=e_a e^{tK}f_r^O.
\]

Thus

\[
N_{IO}(a,r;0)=1_{\{a=r\}},
\tag{2.1}
\]

and

\[
\boxed{
N'_{IO}(a,r;0)
=K(a,r)=a_{i,a}^{r}(\emptyset).}
\tag{2.2}
\]

For distinct active types `a != r`, if the empty-target retyping edge is present and the terminal outgoing record type is globally realizable, then the unsigned denominator is positive to first order and all-patch nonnegativity forces

\[
\boxed{
a_{i,a}^{r}(\emptyset)\ge0.}
\tag{2.3}
\]

This is a genuinely multi-state constraint. In the binary theory there is no pair of distinct active types.

## 3. OI: outgoing -> incoming

Let the initial selected record be `(i,.,r,tau)` with signed outcome row

\[
p=p_{r,\tau}.
\]

Then

\[
N_{OI}(r,\tau;b;t)=p e^{tK}f_b^I.
\]

At zero length,

\[
\boxed{
N_{OI}(r,\tau;b;0)
=p(0)+p(b)
=a_{i,r}^0(\tau)+a_{i,r}^{b}(\tau).}
\tag{3.1}
\]

The corresponding unsigned zero-length normalizer is

\[
|p(0)|+|p(b)|.
\]

Hence whenever at least one of these two hidden outcomes has positive reference probability, all-patch nonnegativity forces

\[
\boxed{
a_{i,r}^0(\tau)+a_{i,r}^{b}(\tau)\ge0.}
\tag{3.2}
\]

The first derivative is

\[
\boxed{
N'_{OI}(r,\tau;b;0)
=pKf_b^I
=\sum_{s\in E_*}a_{i,r}^{s}(\tau)
\bigl(a_{i,s}^{0}(\emptyset)+a_{i,s}^{b}(\emptyset)\bigr).}
\tag{3.3}
\]

(The `s=0` term vanishes because the inactive row of `K` is zero.)

If the zero-length numerator vanishes while the descriptor is realizable to first order, then (3.3) must be nonnegative.

## 4. OO: outgoing -> outgoing

\[
N_{OO}(r,\tau;r_e;t)=p e^{tK}f_{r_e}^O.
\]

At zero length,

\[
\boxed{
N_{OO}(r,\tau;r_e;0)
=p(r_e)=a_{i,r}^{r_e}(\tau).}
\tag{4.1}
\]

The unsigned zero-length normalizer is `|p(r_e)|`. Therefore every realizable hidden active outcome appearing in an outgoing--outgoing zero-length limit must satisfy

\[
\boxed{
a_{i,r}^{r_e}(\tau)\ge0.}
\tag{4.2}
\]

In particular, negative nonempty-target coefficients leading directly to an active hidden outcome are incompatible with all-patch positivity whenever the corresponding `OO` descriptor occurs.

The first derivative is

\[
\boxed{
N'_{OO}(r,\tau;r_e;0)
=pKf_{r_e}^O
=\sum_{s\in E_*}a_{i,r}^{s}(\tau)
a_{i,s}^{r_e}(\emptyset).}
\tag{4.3}
\]

If `a_{i,r}^{r_e}(tau)=0` but the denominator becomes positive to first order, then (4.3) must be nonnegative.

## 5. What is new relative to binary spins

With a single active type, `IO` never connects distinct active labels, so (2.3) has no binary counterpart. Likewise (4.2) reduces to the single binary source-survival coefficient inequality.

For `d>=3`, empty-target retyping coefficients and nonempty-target active-outcome coefficients therefore create immediate sign constraints before any long-time analysis. These conditions are falsifiable diagnostics for typed patch positivity, but they are not claimed sufficient.

## 6. Realizability qualification

The exact positivity definition from 004c applies only when the denominator is positive. A terminal outgoing type also requires that the outer selected record of that type have positive coarse intensity; an incoming terminal type must be deliverable by some outer target record. These outer geometric/intensity conditions are part of skeleton realizability and are separate from the source-line transfer denominator.

Accordingly, (1.3), (2.3), (3.2), and (4.2) are asserted only for bulk descriptors actually present in the killed-skeleton support.
