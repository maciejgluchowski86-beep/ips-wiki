# 009c: exact patch-positivity obstruction for the two-stage contact process

Date: 2026-08-17

This note executes Part C for the model selected independently in `009a` and specialized in `009b`.

## 1. Realized outgoing row and interior transfer

For every neighbour target

\[
\tau_j=\{j\mapsto2\},
\]

the selected successful-record row is

\[
\boxed{p=\mathbf a_{1,\tau_j}=\lambda(1,-1,-1).}
\tag{1.1}
\]

The exact signed interior transfer is

\[
K=
\begin{pmatrix}
0&0&0\\
0&-a&0\\
0&\gamma&-1
\end{pmatrix},
\qquad
\boxed{a=1+\delta+\gamma.}
\tag{1.2}
\]

All physical parameters satisfy

\[
\lambda,\gamma,\delta\ge0.
\]

## 2. A realized `OO` descriptor

Every successful record has pre-source type `1`. Therefore an outgoing-start source patch may end at a later outgoing record only when its local state immediately before the terminal record is again type `1`.

The selected initial record has hidden outcome `S=1` with positive reference probability `1/3` whenever `lambda>0`, because the corresponding coefficient is

\[
p_1=-\lambda.
\]

After that hidden outcome, there is positive probability that no successful nonempty-target record occurs before an arbitrary prescribed terminal time interval. The terminal source-type-1 record itself has positive coarse rate. Thus the outgoing-to-outgoing descriptor with terminal source type `1` is genuinely realized; it is not an artifact of boundary completion.

Equivalently, its killed-reference denominator is strictly positive for every positive patch length.

## 3. Exact signed numerator

The required `OO` numerator is

\[
N_{OO}(t)=p e^{tK}e_1^T.
\tag{3.1}
\]

The active block of `K` is lower triangular. Its relevant entries are

\[
(e^{tK})_{11}=e^{-at}>0,
\tag{3.2}
\]

and, if `a>1`,

\[
(e^{tK})_{21}
=\gamma\frac{e^{-t}-e^{-at}}{a-1}\ge0.
\tag{3.3}
\]

If `a=1`, then necessarily `gamma=delta=0`, so `(e^{tK})_{21}=0`.

Since the zeroth row does not contribute to an active terminal,

\[
\boxed{
N_{OO}(t)
=-\lambda\left[
e^{-at}
+\gamma\frac{e^{-t}-e^{-at}}{a-1}
\right]}
\tag{3.4}
\]

for `a>1`, and

\[
N_{OO}(t)=-\lambda e^{-t}
\tag{3.5}
\]

when `a=1`.

Therefore

\[
\boxed{N_{OO}(t)<0\quad\text{for every }t\ge0\text{ whenever }\lambda>0.}
\tag{3.6}
\]

This includes the zero-length limit

\[
N_{OO}(0)=p_1=-\lambda<0.
\]

## 4. Denominator positivity

Let `d=|N(i)|` be the finite neighbour number. The total nonempty successful hazard at local type `1` is

\[
\kappa_1=3\lambda d.
\]

The unsigned killed transfer has active rows

\[
B|_{\{1,2\}}
=
\begin{pmatrix}
-3\lambda d&0\\
\gamma&-\gamma
\end{pmatrix}.
\tag{4.1}
\]

The outgoing absolute row is

\[
|p|=\lambda(1,1,1).
\]

Hence the realized `OO` denominator

\[
D_{OO}(t)=|p|e^{tB}e_1^T
\]

contains the strictly positive term

\[
\lambda e^{-3\lambda d t}>0.
\tag{4.2}
\]

Thus

\[
D_{OO}(t)>0
\]

for every finite `t` whenever `lambda>0`.

Consequently the corresponding bulk contribution has the sign of (3.4), and is strictly negative.

## 5. Patch-positivity verdict

The interacting parameter range of the published two-stage contact process is `lambda>0`. On all of this range, independently of `gamma,delta`, the realized `OO` patch above has negative contribution.

Therefore

\[
\boxed{\text{the two-stage contact process is not typed patch positive for any }\lambda>0.}
\tag{5.1}
\]

At `lambda=0` there are no nonempty successful records, so this is the trivial noninteracting boundary rather than a positive application regime.

## 6. Structural mechanism

The obstruction is **outgoing hidden-row sign**, not an interior external-positivity transient.

The physical catalytic birth term

\[
0\to1
\quad\text{at rate}\quad
\lambda 1_{\{\text{target}=2\}}
\]

becomes, in the indicator tensor basis,

\[
\lambda\bigl(
1-1_{\{\text{source}=1\}}-1_{\{\text{source}=2\}}
\bigr)
1_{\{\text{target}=2\}}.
\]

Thus the selected successful record necessarily assigns negative sign to the hidden source-preserving outcome `S=1`. Because another successful record requires pre-source type `1`, two consecutive records on the same source line expose that negative sign in an arbitrarily short `OO` patch.

This is a direct model-level obstruction supplied by the generalized patch formalism.

## 7. General catalytic-birth no-go lemma

The same argument gives a reusable local observation.

Suppose a finite-state single-site replacement IPS has a nonempty target mode `tau` and active type `r` such that

\[
\widehat c^{0\to r}(\tau)=b>0,
\]

while all target-mode coefficients `\widehat c^{s\to r}(tau)` for active `s!=0` vanish and the `r`-source outgoing record can occur again after hidden outcome `r`.

Then the typed outgoing row satisfies

\[
a_r^r(\tau)=-b<0.
\]

The zero-length realized `OO` numerator ending at source type `r` is therefore `-b`, so typed patch positivity fails.

The two-stage contact process is an exact instance with `r=1`, `b=lambda`, and target type `2`.
