---
title: Banach-scale obstruction for raw PDE patches
status: proved here
tags:
  - PDE
  - patch
  - integrability
  - Holder regularity
  - Banach scale
  - fluctuation
---

# Banach-scale obstruction for raw PDE patches

The raw centered Hessian edge admits a gain if one measures its input in a stronger Hölder space than its output. That gain is not free. If one spends a regularity increment \(\delta\) at one edge, the optimal first-moment time-integrated operator constant is of order \(1/\delta\). Consequently, any argument that treats successive centered Hessian edges **one at a time in first moment**, pays a decreasing sequence of Hölder exponents, and keeps the total loss below a fixed budget \(\Delta\), incurs at least

$$
\left(\frac{c n}{\Delta}\right)^n
$$

after \(n\) generations. The uniform allocation \(\delta_k=\Delta/n\) is the best possible allocation; nonuniform budgets are worse.

This is a barrier theorem for a specific proof architecture. It rules out the direct Nash--Moser-style idea of repairing the raw fluctuation problem merely by descending through a fixed Hölder Banach scale and taking a first-moment norm after every centered edge. It is **not** a disproof of the [full random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md). The one-edge lower bound is saturated by frequencies that depend on the regularity loss being spent, hence on the generation in an iterated budget. The theorem does not produce one fixed smooth terminal datum whose raw estimator has infinite absolute expectation.

It also does not exclude a genuine smoothing/telescoping scheme that retains frequency information and compensates smoothing errors, nor an argument that preserves genealogy, uses cancellation across several centered marks before taking absolute values, or works in a norm carrying both scale and genealogical information.

**References.** The raw centered Hessian edge and the fixed-exponent obstruction are introduced in the [random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md). Hölder spaces and translation estimates are reviewed in [Parabolic Hölder spaces](parabolic-holder-spaces.md) and [Hölder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md). The theorem below is proved here.

## Setup

Let

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z),
$$

let \(Z\sim N(0,1)\), and let

$$
He_2(z)=z^2-1.
$$

For \(r>0\) define the raw centered Hessian edge

$$
\widehat K_r f(x,Z)
=
\frac{He_2(Z)}{r}
\left[f(x+\sqrt r\,Z)-f(x)\right].
\tag{1}
$$

For \(0<\gamma<1\), write

$$
[f]_{C^\gamma}
=
\sup_{x\neq y}
\frac{|f(x)-f(y)|}{d_{\mathbb T}(x,y)^\gamma}.
\tag{2}
$$

Fix numbers

$$
0<\underline\alpha<\overline\alpha<1,
\qquad
T>0.
\tag{3}
$$

All constants below may depend on \(\underline\alpha,\overline\alpha,T\), but not on the regularity gap \(\delta\).

For

$$
\underline\alpha\leq\beta<\alpha\leq\overline\alpha,
\qquad
\delta=\alpha-\beta,
$$

define the time-integrated first-moment edge norm

$$
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
$$

The proposal law used to sample an edge lifetime does not appear in (4). At first moment its density cancels the reciprocal importance-sampling compensator, leaving Lebesgue integration in \(r\).

## Theorem: sharp one-edge loss

There are constants \(0<c\leq C<\infty\) such that, for every pair \(\beta<\alpha\) in the range (3),

$$
\frac{c}{\delta}
\leq
\mathfrak C_{\alpha,\beta}(T)
\leq
\frac{C}{\delta},
\qquad
\delta=\alpha-\beta.
\tag{5}
$$

Thus the cost \(1/\delta\) is intrinsic to the one-edge first-moment Hölder-scale estimate.

### Upper bound

For \(h\in\mathbb R\), the standard translation estimate gives

$$
[\tau_hf-f]_{C^\beta}
\leq
C_0|h|^\delta[f]_{C^\alpha},
\tag{6}
$$

uniformly for exponents in the compact range (3). One elementary proof splits the increment defining the \(C^\beta\) seminorm according to whether its spatial separation is at most \(|h|\) or larger than \(|h|\).

Applying (6) to (1) gives

$$
\mathbb E
[\widehat K_r f]_{C^\beta}
\leq
C_0r^{-1+\delta/2}
\mathbb E\left[|He_2(Z)|\,|Z|^\delta\right]
[f]_{C^\alpha}.
\tag{7}
$$

The Gaussian moment in (7) is uniformly bounded for \(0<\delta\leq\overline\alpha-\underline\alpha\). Therefore

$$
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
$$

Since \(T^{\delta/2}\) is uniformly bounded on the exponent range, this proves the upper half of (5).

### Lower bound

For an integer \(N\geq1\), let

$$
f_N(x)=N^{-\alpha}\cos(Nx).
\tag{9}
$$

Uniformly for \(\alpha\) in (3),

$$
[f_N]_{C^\alpha}\asymp1.
\tag{10}
$$

For a spatial shift \(h\),

$$
\tau_hf_N-f_N
=
-2N^{-\alpha}
\sin\left(\frac{Nh}{2}\right)
\sin\left(Nx+\frac{Nh}{2}\right),
$$

and hence, uniformly for \(\beta\) in (3),

$$
[\tau_hf_N-f_N]_{C^\beta}
\geq
c_0N^{-\delta}
\left|
\sin\left(\frac{Nh}{2}\right)
\right|.
\tag{11}
$$

Substituting \(h=\sqrt r\,Z\) into (1), equations (10)--(11) give

$$
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
$$

where

$$
F(q)
=
\mathbb E\left[
|He_2(Z)|
\left|\sin\left(\frac{qZ}{2}\right)\right|
\right].
\tag{13}
$$

There is a constant \(c_F>0\) such that

$$
F(q)\geq c_F,
\qquad q\geq1.
\tag{14}
$$

Indeed, \(F\) is continuous and strictly positive on every compact subset of \((0,\infty)\). For large \(q\), use \(|\sin\theta|\geq\sin^2\theta\) to obtain

$$
F(q)
\geq
\frac12\mathbb E|He_2(Z)|
-
\frac12
\mathbb E\left[|He_2(Z)|\cos(qZ)\right].
$$

The last term tends to zero by the Riemann--Lebesgue lemma because \(|He_2(z)|\) times the Gaussian density is integrable. This proves (14).

With \(q=N\sqrt r\), equation (12) therefore yields, whenever \(N\sqrt T\geq1\),

$$
\int_0^T
\mathbb E
[\widehat K_r f_N]_{C^\beta}
\,dr
\geq
2c_1c_FN^{-\delta}
\int_1^{N\sqrt T}\frac{dq}{q}
=
2c_1c_FN^{-\delta}
\log(N\sqrt T).
\tag{15}
$$

Choose an integer \(N\) with

$$
N\asymp T^{-1/2}e^{1/\delta}.
\tag{16}
$$

Then \(N^{-\delta}\) is bounded below by a positive constant depending only on the fixed exponent range and \(T\), while

$$
\log(N\sqrt T)\asymp\frac1\delta.
$$

Together with (10), this proves the lower half of (5).

### Pointwise short-edge form

The same frequency test with \(N\asymp r^{-1/2}\) shows that the pointwise operator norm itself is sharp:

$$
\sup_{[f]_{C^\alpha}>0}
\frac{
\mathbb E[\widehat K_r f]_{C^\beta}
}{[f]_{C^\alpha}}
\asymp
r^{-1+\delta/2}
\tag{17}
$$

for short edges \(r\). Thus the factor \(1/\delta\) in (5) is exactly the integral of a sharp short-edge singularity, not an artefact of an inefficient estimate.

## Theorem: fixed total regularity budget

Fix

$$
0<\Delta<\alpha_0<1
$$

and consider a decreasing sequence

$$
\alpha_0>\alpha_1>\cdots>\alpha_n\geq\alpha_0-\Delta.
$$

Write

$$
\delta_k=\alpha_{k-1}-\alpha_k>0,
\qquad
\sum_{k=1}^n\delta_k\leq\Delta.
\tag{18}
$$

Consider a *stepwise first-moment Hölder-scale argument*: after each raw centered Hessian edge, the argument takes a \(C^{\alpha_k}\) norm and controls that edge by a uniform operator estimate from \(C^{\alpha_{k-1}}\) to \(L^1(\Omega;C^{\alpha_k})\), before proceeding to the next edge. Such an argument necessarily pays one constant \(A_k\) satisfying

$$
A_k
\geq
\frac{c}{\delta_k}.
\tag{19}
$$

Consequently its \(n\)-edge recursive majorant contains at least

$$
\prod_{k=1}^nA_k
\geq
c^n
\prod_{k=1}^n\frac1{\delta_k}
\geq
c^n
\left(\frac n\Delta\right)^n.
\tag{20}
$$

The last inequality is the arithmetic--geometric mean inequality:

$$
\prod_{k=1}^n\delta_k
\leq
\left(
\frac1n\sum_{k=1}^n\delta_k
\right)^n
\leq
\left(\frac\Delta n\right)^n.
$$

Thus the uniform allocation \(\delta_k=\Delta/n\) is the optimal budget. Every nonuniform budget is at least as expensive.

### A geometric budget is worse

For example, take

$$
\delta_k
=
\frac{\Delta\,2^{-k}}{1-2^{-n}},
\qquad
1\leq k\leq n.
\tag{21}
$$

Then \(\sum_k\delta_k=\Delta\), but

$$
\prod_{k=1}^n\frac1{\delta_k}
=
\left(
\frac{1-2^{-n}}{\Delta}
\right)^n
2^{n(n+1)/2}.
\tag{22}
$$

This is much larger than the already supergeometric optimum \((n/\Delta)^n\).

## Chronology does not restore a factorial gain

A possible loophole is that \(n\) branch times are chronologically ordered, so perhaps the time simplex supplies a compensating \(1/n!\). The sharp edge singularity (17) prevents this.

If the stepwise proof retains the time dependence and uses the sharp kernels

$$
r_k^{-1+\delta_k/2},
$$

then the ordered duration integral is the Dirichlet integral

$$
\begin{aligned}
I_n(t;\delta_1,\ldots,\delta_n)
&=
\int_{\substack{r_k>0\\r_1+\cdots+r_n<t}}
\prod_{k=1}^n
r_k^{-1+\delta_k/2}
\,dr_1\cdots dr_n\\
&=
t^{D/2}
\frac{
\prod_{k=1}^n\Gamma(\delta_k/2)
}{
\Gamma(1+D/2)
},
\qquad
D=\sum_{k=1}^n\delta_k.
\end{aligned}
\tag{23}
$$

For \(0<D\leq\Delta\), the denominator and the factor \(t^{D/2}\) are controlled by constants depending only on \(t\) and \(\Delta\), while

$$
\Gamma(\delta_k/2)
\asymp
\frac1{\delta_k}
$$

uniformly for \(0<\delta_k\leq\Delta\). Hence the chronological majorant still carries the product

$$
\prod_{k=1}^n\frac1{\delta_k},
$$

and therefore the lower barrier (20). The short-edge singularities consume the usual simplex gain.

## What the theorem rules out

The theorem rules out the following proof architecture for the raw fluctuation in the quadratic-Hessian patch problem:

1. choose a decreasing Hölder scale \(C^{\alpha_0}\supset C^{\alpha_1}\supset\cdots\);
2. after each centered Hessian edge, take a first-moment Banach norm;
3. control that edge uniformly over the entire unit ball of the current Hölder space;
4. pay a deterministic loss \(\delta_k=\alpha_{k-1}-\alpha_k\); and
5. keep the total loss \(\sum_k\delta_k\) bounded independently of the generation.

No choice of the loss budget turns the resulting constants into a geometric-in-generation majorant. In this precise sense, the usual **loss-of-derivatives budget by itself** does not repair the fluctuation problem.

This includes the bare Banach-scale component of a Nash--Moser strategy. It does **not** prove that every possible Nash--Moser iteration fails. A full smoothing scheme may project away the high frequencies that saturate (5) and then compensate the smoothing error by a telescoping or nonlinear correction. Such a scheme is frequency-aware and falls outside the stepwise uniform operator-norm architecture above; it would require a separate analysis.

## What the theorem does not rule out

The theorem is not a lower bound on the actual \(n\)-generation raw estimator for one fixed datum. The test frequency in (16) depends on \(\delta\). Under the optimal depth-\(n\) allocation \(\delta\simeq\Delta/n\), the saturating frequency is of order

$$
N_n
\asymp
\exp(cn/\Delta).
\tag{24}
$$

Thus the lower bound is obtained by changing the high-frequency test as the generation changes. The argument does not identify one fixed smooth \(\phi\) whose descendants simultaneously realize these operator norms at every depth. It therefore does **not** imply

$$
\mathbb E|H_{\mathrm{patch}}|=\infty
$$

for the conjectural raw estimator, and it does not disprove conjecture C.

A successful proof of C must avoid taking a uniform first-moment Banach norm after every centered edge. Plausible ways to escape the barrier include retaining frequency information, retaining genealogy together with frequency, exploiting martingale or square-function structure, or allowing cancellation across several centered Gaussian/Hermite marks before taking absolute values. The theorem does not decide which, if any, of these routes succeeds.
