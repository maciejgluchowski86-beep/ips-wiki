---
title: Strict Hölder loss for a centered heat-Hessian edge
status: observation
audit: current
tags:
  - PDE
  - heat semigroup
  - Hessian
  - Holder regularity
  - integrability
---

# Strict Hölder loss for a centered heat-Hessian edge

This entry records the sharp one-edge first-moment estimate that survives from the terminated quadratic-Hessian programme. It makes no claim about an iterated Banach-scale obstruction or an infinite branching representation.

## Setup

Let
\[
\mathbb T=\mathbb R/(2\pi\mathbb Z),
\qquad
Z\sim N(0,1),
\qquad
He_2(z)=z^2-1.
\]
For $r>0$ define the centered heat-Hessian edge
\[
\widehat K_r f(x,Z)
=
\frac{He_2(Z)}{r}
\left[f(x+\sqrt r\,Z)-f(x)\right].
\tag{1}
\]
For $0<\gamma<1$, write
\[
[f]_{C^\gamma}
=
\sup_{x\neq y}
\frac{|f(x)-f(y)|}{d_{\mathbb T}(x,y)^\gamma}.
\tag{2}
\]
Fix
\[
0<\underline\alpha<\overline\alpha<1,
\qquad
T>0.
\tag{3}
\]
All constants below may depend on $\underline\alpha,\overline\alpha,T$, but not on the regularity gap. For
\[
\underline\alpha\leq\beta<\alpha\leq\overline\alpha,
\qquad
\delta=\alpha-\beta,
\]
define
\[
\mathfrak C_{\alpha,\beta}(T)
=
\sup_{[f]_{C^\alpha}>0}
\frac{
\displaystyle
\int_0^T
\mathbb E\left[
[\widehat K_r f(\cdot,Z)]_{C^\beta}
\right]dr
}{[f]_{C^\alpha}}.
\tag{4}
\]

## Sharp one-edge estimate

There are constants $0<c\leq C<\infty$ such that, for every pair $\beta<\alpha$ in the range (3),
\[
\frac{c}{\delta}
\leq
\mathfrak C_{\alpha,\beta}(T)
\leq
\frac{C}{\delta},
\qquad
\delta=\alpha-\beta.
\tag{5}
\]

### Upper bound

For $h\in\mathbb R$, the standard translation estimate gives
\[
[\tau_hf-f]_{C^\beta}
\leq
C_0|h|^\delta[f]_{C^\alpha},
\tag{6}
\]
uniformly for exponents in the compact range (3). One elementary proof splits the increment defining the $C^\beta$ seminorm according to whether its spatial separation is at most $|h|$ or larger than $|h|$.

Applying (6) to (1) yields
\[
\mathbb E
[\widehat K_r f]_{C^\beta}
\leq
C_0r^{-1+\delta/2}
\mathbb E\left[|He_2(Z)|\,|Z|^\delta\right]
[f]_{C^\alpha}.
\tag{7}
\]
The Gaussian moment is uniformly bounded for $0<\delta\leq\overline\alpha-\underline\alpha$. Therefore
\[
\int_0^T
\mathbb E
[\widehat K_r f]_{C^\beta}
\,dr
\leq
C_1[f]_{C^\alpha}
\int_0^T r^{-1+\delta/2}\,dr
=
\frac{2C_1T^{\delta/2}}{\delta}
[f]_{C^\alpha}.
\tag{8}
\]
Since $T^{\delta/2}$ is uniformly bounded on the fixed exponent range, this proves the upper bound in (5).

### Lower bound

For an integer $N\geq1$, let
\[
f_N(x)=N^{-\alpha}\cos(Nx).
\tag{9}
\]
Uniformly for $\alpha$ in (3),
\[
[f_N]_{C^\alpha}\asymp1.
\tag{10}
\]
For a spatial shift $h$,
\[
\tau_hf_N-f_N
=
-2N^{-\alpha}
\sin\left(\frac{Nh}{2}\right)
\sin\left(Nx+\frac{Nh}{2}\right),
\]
and hence, uniformly for $\beta$ in (3),
\[
[\tau_hf_N-f_N]_{C^\beta}
\geq
c_0N^{-\delta}
\left|
\sin\left(\frac{Nh}{2}\right)
\right|.
\tag{11}
\]
Substituting $h=\sqrt r\,Z$ into (1), equations (10)--(11) give
\[
\int_0^T
\mathbb E
[\widehat K_r f_N]_{C^\beta}
\,dr
\geq
c_1N^{-\delta}
\int_0^T
\frac{1}{r}
F(N\sqrt r)\,dr,
\tag{12}
\]
where
\[
F(q)
=
\mathbb E\left[
|He_2(Z)|
\left|\sin\left(\frac{qZ}{2}\right)\right|
\right].
\tag{13}
\]
There is a constant $c_F>0$ such that
\[
F(q)\geq c_F,
\qquad q\geq1.
\tag{14}
\]
Indeed, $F$ is continuous and strictly positive on every compact subset of $(0,\infty)$. For large $q$, use $|\sin\theta|\geq\sin^2\theta$ to obtain
\[
F(q)
\geq
\frac12\mathbb E|He_2(Z)|
-
\frac12
\mathbb E\left[|He_2(Z)|\cos(qZ)\right].
\]
The last term tends to zero by the Riemann--Lebesgue lemma because $|He_2(z)|$ times the Gaussian density is integrable. This proves (14).

With $q=N\sqrt r$, equation (12) therefore yields, whenever $N\sqrt T\geq1$,
\[
\int_0^T
\mathbb E
[\widehat K_r f_N]_{C^\beta}
\,dr
\geq
2c_1c_FN^{-\delta}
\log(N\sqrt T).
\tag{15}
\]
Choose an integer $N$ with
\[
N\asymp T^{-1/2}e^{1/\delta}.
\tag{16}
\]
Then $N^{-\delta}$ is bounded below by a positive constant depending only on the fixed exponent range and $T$, while
\[
\log(N\sqrt T)\asymp\frac1\delta.
\]
Together with (10), this proves the lower bound in (5).
