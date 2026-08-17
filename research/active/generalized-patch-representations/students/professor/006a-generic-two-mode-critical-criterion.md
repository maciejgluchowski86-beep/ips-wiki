# 006a: generic two-mode spectral critical criterion

Date: 2026-08-17

This note executes Parts A--B of Assignment 006 in the generic case. The endpoint-only route stopped in Assignment 005 is not revived: the interior critical value is retained explicitly.

## 1. Boundary-complete reduction from Assignment 005

Under the boundary-complete `d=3` hypothesis, typed bulk patch positivity forces the interior transfer matrix `K` to be Metzler. Hence `exp(tK)` is entrywise nonnegative. The incoming-initial `II/IO` numerator families and, after the zero-length outgoing conditions, all `OO` families are therefore automatic.

The only remaining family is `OI`:

\[
N(t)=u e^{tK}f,
\]

where `u=p=(p_0,p_1,p_2)` is one signed outgoing coefficient row and

\[
f=f_b^I=e_0^T+e_b^T,
\qquad b\in\{1,2\}.
\]

The zero-length conditions already require

\[
N(0)=p_0+p_b\ge0.
\tag{1.1}
\]

## 2. Generic spectral data

Write the active `2 x 2` block of `K` as `M`. Because `K` is Metzler, `M` has real eigenvalues. In the generic case assume they are distinct and strictly negative:

\[
-\mu,\qquad-\nu,
\qquad 0<\mu<\nu.
\tag{2.1}
\]

Equivalently, if

\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad b,c\ge0,
\]

then

\[
\Delta=\sqrt{(a-d)^2+4bc}>0,
\]

\[
\mu=\frac{-\operatorname{tr}M-\Delta}{2},
\qquad
\nu=\frac{-\operatorname{tr}M+\Delta}{2}.
\tag{2.2}
\]

No eigenvectors are needed.

The three eigenvalues of `K` are `0,-mu,-nu`. The projector onto the zero eigenspace is the polynomial

\[
P_0=\frac{(K+\mu I)(K+\nu I)}{\mu\nu}.
\tag{2.3}
\]

Therefore the long-time limit of the numerator is

\[
\boxed{L=uP_0f.}
\tag{2.4}
\]

Put

\[
n_0=uf=N(0),
\qquad
n_1=uKf=N'(0).
\tag{2.5}
\]

Since

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t},
\tag{2.6}
\]

we have

\[
A+B=n_0-L,
\qquad
-\mu A-\nu B=n_1.
\]

Solving gives the exact coefficient formulas

\[
\boxed{
A=\frac{\nu(n_0-L)+n_1}{\nu-\mu},
\qquad
B=\frac{-\mu(n_0-L)-n_1}{\nu-\mu}.}
\tag{2.7}
\]

Thus `L,A,B` are obtained from `K,u,f` by a bounded amount of algebra and one quadratic radical. This is equivalent to the spectral-projector formulas but avoids constructing the two nonzero projectors.

## 3. At most one interior critical point

Differentiate (2.6):

\[
N'(t)=-\mu A e^{-\mu t}-\nu B e^{-\nu t}.
\tag{3.1}
\]

Multiplying by `exp(mu t)` shows that the sign of `N'` is the sign of

\[
-\mu A-\nu B e^{-(\nu-\mu)t},
\]

which is affine in the strictly decreasing variable `exp(-(nu-mu)t)`. Hence `N'` has at most one zero on `(0,infty)`.

A critical point satisfies

\[
e^{-(\nu-\mu)t_*}
=R:=-\frac{\mu A}{\nu B}.
\tag{3.2}
\]

Thus a positive critical time exists exactly when `A,B` have opposite signs and

\[
0<R<1.
\tag{3.3}
\]

At a critical point, use

\[
\nu B e^{-\nu t_*}=-\mu A e^{-\mu t_*}
\]

to obtain

\[
N''(t_*)
=\mu(\mu-\nu)A e^{-\mu t_*}.
\tag{3.4}
\]

Since `nu>mu`, the critical point is a minimum exactly when `A<0`; consequently `B>0`.

Therefore the **only interior-minimum regime** is

\[
\boxed{
A<0<B,
\qquad
0<R=-\frac{\mu A}{\nu B}<1.}
\tag{3.5}
\]

Equivalently, because `A<0<B`, the second inequality is

\[
-\mu A<\nu B,
\]

which is precisely `N'(0)<0`.

## 4. Exact critical value

When (3.5) holds,

\[
t_*=\frac{-\log R}{\nu-\mu}>0.
\tag{4.1}
\]

Moreover

\[
e^{-\mu t_*}=R^{\mu/(\nu-\mu)}.
\tag{4.2}
\]

Using the critical relation again,

\[
B e^{-\nu t_*}
=-\frac{\mu}{\nu}A e^{-\mu t_*}.
\]

Hence

\[
\boxed{
N(t_*)
=L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}.}
\tag{4.3}
\]

This is the exact interior value; no time scan remains.

## 5. Necessary-and-sufficient generic criterion

### Theorem 5.1

Assume (2.1). For one remaining `OI` descriptor, the condition

\[
N(t)\ge0\qquad\text{for every }t\ge0
\tag{5.1}
\]

is equivalent to:

1. zero-length nonnegativity
   \[
   n_0=L+A+B\ge0;
   \tag{5.2}
   \]
2. long-time nonnegativity
   \[
   L\ge0;
   \tag{5.3}
   \]
3. if and only if the interior-minimum regime (3.5) holds, the single additional inequality
   \[
   \boxed{
   L+\frac{\nu-\mu}{\nu}
   A\left(-\frac{\mu A}{\nu B}\right)^{\mu/(\nu-\mu)}
   \ge0.}
   \tag{5.4}
   \]

### Proof

By Section 3 there is at most one interior critical point. If there is no interior minimum, every minimum over `[0,infty]` occurs at one of the two endpoints, so (5.2)--(5.3) are necessary and sufficient. If (3.5) holds, the unique positive critical point is the unique interior minimum, so its exact value (4.3) must additionally be nonnegative. These possibilities exhaust all signs of `A,B` and all locations of the unique possible critical point. `square`

## 6. Assignment-005 witness

For

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t},
\]

we have

\[
L=\frac1{128},
\quad A=-\frac{13}{64},
\quad B=\frac{153}{128},
\quad \mu=1,
\quad \nu=2.
\]

Then

\[
R=-\frac{\mu A}{\nu B}=\frac{13}{153},
\]

and (4.3) gives

\[
N(t_*)
=\frac1{128}
+\frac12\left(-\frac{13}{64}\right)\frac{13}{153}
=-\frac1{1224}.
\]

Thus the exact criterion detects the obstruction without scanning `t`.
