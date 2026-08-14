---
title: Joint centered-mark dichotomy for raw PDE patches
status: proved here
tags:
  - PDE
  - patch
  - integrability
  - Gaussian analysis
  - Hermite polynomial
  - fluctuation
---

# Joint centered-mark dichotomy for raw PDE patches

A centered Hessian edge is too singular to propagate a pathwise Hölder norm at fixed regularity, and a stepwise decreasing Hölder scale pays the sharp cost recorded in the [Banach-scale obstruction](banach-scale-obstruction-for-raw-pde-patches.md). One can avoid that *stepwise* architecture by composing several centered marks first and taking the first absolute moment only after the whole block has been formed.

That modification gives a real gain already for two marks, but at arbitrary block length it leads to a new dichotomy.

- If all Gaussian marks in the block are retained as separate random variables until the final absolute value, the derivative-loss ladder disappears but the optimal uniform block norm grows factorially, of order \(C^m m!\).
- If the internal Gaussian bridge marks are signedly averaged before the absolute value, a bare \(m\)-edge derivative chain collapses to one \(He_{2m}\) endpoint weight. The time-simplex factor then reduces the coefficient to geometric growth. For spatially varying patches, the corresponding geometric bound is supplied by the commutator/cluster estimate in [Hölder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md).

These estimates are proved here. They are uniform block-norm statements and exact Gaussian conditioning identities. By themselves they do **not** prove nonintegrability for one fixed smooth datum: the lower-bound frequency depends on the block length. The later [raw-barycenter obstruction](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) closes that fixed-datum gap for the raw-faithful class, and the [residual signed variation characterization](residual-signed-variation-characterization-for-coarsened-patches.md) explains the two branches below as different retained sigma-fields.

## Setup

Fix

$$
0<\alpha<1,
\qquad
T>0,
\qquad
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Let \(Z_1,Z_2,\ldots\) be independent standard Gaussian variables and write

$$
He_2(z)=z^2-1.
$$

For a spatial shift \(h\), define

$$
(\Delta_hf)(x)=f(x+h)-f(x).
\tag{1}
$$

For \(m\geq1\), positive edge lengths

$$
\mathbf r=(r_1,\ldots,r_m),
\qquad
R=r_1+\cdots+r_m,
$$

and shifts

$$
h_j=\sqrt{r_j}\,Z_j,
$$

define the *retained centered \(m\)-mark block*

$$
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f(x)
=
\left(
\prod_{j=1}^m\frac{He_2(Z_j)}{r_j}
\right)
\Delta_{h_m}\cdots\Delta_{h_1}f(x).
\tag{2}
$$

All \(Z_1,\ldots,Z_m\) remain random in (2). The chronological branch times may be replaced by the positive duration variables \(r_j\); the ordered-time region becomes

$$
\Sigma_m(T)
=
\left\{
\mathbf r\in(0,\infty)^m:
 r_1+\cdots+r_m<T
\right\}
\tag{3}
$$

with unit Jacobian.

## Signed exactness of the centered block

For every smooth periodic \(f\),

$$
\mathbb E
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f(x)
=
\partial_x^{2m}P_Rf(x).
\tag{4}
$$

Indeed, expanding the mixed difference in (2) produces \(2^m\) terms. Every term except the one containing all shifts \(h_1,\ldots,h_m\) is independent of at least one \(Z_j\), and its expectation vanishes because \(\mathbb E He_2(Z_j)=0\). The surviving term is

$$
\mathbb E\left[
\left(
\prod_{j=1}^m\frac{He_2(Z_j)}{r_j}
\right)
 f\left(x+\sum_{j=1}^m\sqrt{r_j}Z_j\right)
\right],
$$

which is the composition of \(m\) second heat derivatives and hence equals \(\partial_x^{2m}P_Rf(x)\).

Thus composing centered marks before taking absolute values is an exact finite-level operation, not a change in the signed derivative operator.

## Two-mark gain

The mixed difference satisfies

$$
\left\|
\Delta_{h_2}\Delta_{h_1}f
\right\|_\infty
\leq
2[f]_{C^\alpha}
\min\{|h_1|^\alpha,|h_2|^\alpha\}.
\tag{5}
$$

Using \(\min\{a,b\}\leq\sqrt{ab}\), one obtains

$$
\begin{aligned}
&\mathbb E
\left\|
\widehat{\mathcal K}_{(r_1,r_2)}^{\mathrm{raw}}f
\right\|_\infty\\
&\qquad\leq
C_\alpha
[f]_{C^\alpha}
 r_1^{-1+\alpha/4}
 r_2^{-1+\alpha/4}.
\end{aligned}
\tag{6}
$$

Therefore

$$
\int_{\Sigma_2(T)}
\mathbb E
\left\|
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f
\right\|_\infty
\,d\mathbf r
\leq
C_{\alpha,T}[f]_{C^\alpha},
\tag{7}
$$

because

$$
\int_{\Sigma_2(T)}
 r_1^{-1+\alpha/4}r_2^{-1+\alpha/4}
\,dr_1dr_2
=
T^{\alpha/2}
\frac{\Gamma(\alpha/4)^2}
{\Gamma(1+\alpha/2)}.
\tag{8}
$$

This is a genuine non-stepwise gain: no intermediate \(C^{\alpha-\delta}\) norm and no regularity increment \(\delta\) is introduced between the two centered edges. The estimate is obtained from the mixed two-shift increment before the first absolute moment is taken.

It does not contradict the Banach-scale obstruction. That theorem assumes that after **each** centered Hessian edge one takes a first-moment Banach norm and then propagates a uniform one-edge estimate to the next generation. Equation (7) violates precisely that hypothesis: the first edge is left inside the signed random block until the second mark has acted.

## Retaining all marks: factorial block norm

Define

$$
\mathfrak R_m(\alpha,T)
=
\sup_{[f]_{C^\alpha}>0}
\frac{
\displaystyle
\int_{\Sigma_m(T)}
\mathbb E
\left\|
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f
\right\|_\infty
\,d\mathbf r
}{[f]_{C^\alpha}}.
\tag{9}
$$

### Theorem

There are constants \(0<c_{\alpha,T}\leq C_{\alpha,T}<\infty\) such that, for every \(m\geq1\),

$$
\boxed{
c_{\alpha,T}^m m!
\leq
\mathfrak R_m(\alpha,T)
\leq
C_{\alpha,T}^m m!.
}
\tag{10}
$$

Hence delaying the absolute value across the entire retained-mark block removes the descending regularity ladder but replaces it by sharp factorial growth in the block length.

### Upper bound

For arbitrary shifts \(h_1,\ldots,h_m\),

$$
\left\|
\Delta_{h_m}\cdots\Delta_{h_1}f
\right\|_\infty
\leq
2^{m-1}[f]_{C^\alpha}
\min_{1\leq j\leq m}|h_j|^\alpha.
\tag{11}
$$

Since the minimum is bounded by the geometric mean,

$$
\min_j|h_j|^\alpha
\leq
\prod_{j=1}^m|h_j|^{\alpha/m},
$$

and therefore

$$
\begin{aligned}
\mathbb E
\left\|
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f
\right\|_\infty
\leq{}&
2^{m-1}[f]_{C^\alpha}
\prod_{j=1}^m
r_j^{-1+\alpha/(2m)}\\
&\times
\left(
\mathbb E[|He_2(Z)|\,|Z|^{\alpha/m}]
\right)^m.
\end{aligned}
\tag{12}
$$

The Gaussian factor is bounded uniformly in \(m\). The Dirichlet integral gives

$$
\int_{\Sigma_m(T)}
\prod_{j=1}^m
r_j^{-1+\alpha/(2m)}
\,d\mathbf r
=
T^{\alpha/2}
\frac{
\Gamma(\alpha/(2m))^m
}{
\Gamma(1+\alpha/2)
}.
\tag{13}
$$

Since \(\Gamma(\alpha/(2m))\leq C_\alpha m\), equations (12)--(13) give

$$
\mathfrak R_m(\alpha,T)
\leq
(C_{\alpha,T}m)^m
\leq
C_{\alpha,T}^m m!,
\tag{14}
$$

after enlarging the constant and using Stirling's formula.

### Lower bound

For an integer \(N\geq1\), take

$$
f_N(x)=N^{-\alpha}\cos(Nx).
\tag{15}
$$

Then \([f_N]_{C^\alpha}\asymp1\), uniformly in \(N\), and

$$
\left\|
\Delta_{h_m}\cdots\Delta_{h_1}f_N
\right\|_\infty
=
N^{-\alpha}
\prod_{j=1}^m
\left|e^{iNh_j}-1\right|.
\tag{16}
$$

Set

$$
G(q)
=
\mathbb E\left[
|He_2(Z)|\,|e^{iqZ}-1|
\right].
\tag{17}
$$

There exists \(c_G>0\) such that

$$
G(q)\geq c_G,
\qquad q\geq1.
\tag{18}
$$

Indeed, \(G\) is continuous and strictly positive on compact subsets of \((0,\infty)\). For large \(q\), the Riemann--Lebesgue lemma applied to the oscillatory part prevents cancellation of the strictly positive \(L^1\) mass of \(|He_2|\).

For fixed \(\mathbf r\),

$$
\mathbb E
\left\|
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f_N
\right\|_\infty
=
N^{-\alpha}
\prod_{j=1}^m
\frac{G(N\sqrt{r_j})}{r_j}.
\tag{19}
$$

Restrict to

$$
1\leq q_j=N\sqrt{r_j}\leq Q,
\qquad
Q=N\sqrt{\frac{T}{2m}}.
$$

This box lies inside \(\Sigma_m(T)\). Since \(dr_j/r_j=2dq_j/q_j\),

$$
\int_{\Sigma_m(T)}
\mathbb E
\left\|
\widehat{\mathcal K}_{\mathbf r}^{\mathrm{raw}}f_N
\right\|_\infty
\,d\mathbf r
\geq
N^{-\alpha}
\bigl(2c_G\log Q\bigr)^m.
\tag{20}
$$

Choose

$$
N
\asymp
\sqrt{\frac{m}{T}}e^{m/\alpha}.
\tag{21}
$$

Then the right side of (20) is at least a constant times

$$
c_{\alpha,T}^m
m^{-\alpha/2}
\left(\frac{m}{e}\right)^m,
$$

and Stirling's formula gives the lower half of (10) after absorbing the polynomial factor into the exponential constant.

The optimizing frequency in (21) depends on \(m\). Thus theorem (10) is a sharp uniform operator obstruction, not yet a fixed-datum nonintegrability theorem.

## Signed averaging of Gaussian bridge marks

Let

$$
Y
=
\sum_{j=1}^m\sqrt{r_j}Z_j,
\qquad
R=\sum_{j=1}^m r_j,
\qquad
Z=Y/\sqrt R.
\tag{22}
$$

Then \(Z\sim N(0,1)\). The variable \(Y\) is the total Brownian displacement; the remaining \(m-1\) Gaussian degrees of freedom are bridge coordinates.

### Proposition: bridge-score identity

One has

$$
\boxed{
\mathbb E\left[
\left.
\prod_{j=1}^m
\frac{He_2(Z_j)}{r_j}
\right|Y
\right]
=
\frac{He_{2m}(Z)}{R^m}.
}
\tag{23}
$$

To prove (23), test both sides against a bounded smooth function \(F(Y)\). Repeated Gaussian integration by parts on the left and the one-Gaussian Hermite formula on the right both give

$$
\partial_x^{2m}P_RF(x)\big|_{x=0}.
$$

Hence the conditional expectations agree.

## Geometric growth after bridge averaging

For a bare derivative chain, after bridge averaging one has

$$
\mathbb E\left[
\left|
\frac{He_{2m}(Z)}{R^m}
\bigl(f(x+\sqrt RZ)-f(x)\bigr)
\right|
\right]
\leq
c_{2m,\alpha}
R^{-m+\alpha/2}[f]_{C^\alpha},
\tag{24}
$$

where

$$
c_{2m,\alpha}
=
\mathbb E[|He_{2m}(Z)|\,|Z|^\alpha]
\leq
C_\alpha\sqrt{(2m)!}.
\tag{25}
$$

For fixed total duration \(R\), the simplex of positive edge durations with sum \(R\) has volume

$$
\frac{R^{m-1}}{(m-1)!}.
\tag{26}
$$

Thus the time-integrated coefficient is at most

$$
C_{\alpha,T}
\frac{\sqrt{(2m)!}}{(m-1)!}
\leq
C_{\alpha,T}4^m.
\tag{27}
$$

The factorial retained-mark scale therefore collapses to geometric growth after signed bridge averaging.

### Spatially varying side profiles

Identity (23) applies literally to a bare derivative chain. In a full Duhamel patch, multiplication by spatially varying side profiles occurs between Hessian transfers, so the entire patch does not collapse directly to one \(He_{2m}\) weight.

The corresponding full-patch estimate remains geometric after deterministic signed interior averaging under uniform spatial \(C^\alpha\) control of the side profiles. Commuting derivative blocks through the multipliers splits the patch into derivative clusters. A cluster of length \(\ell\) contributes

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2},
$$

with geometric coefficient, and the full commutator expansion has at most \(2^m\) terms. See [Hölder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md).

## Final interpretation

The two branches are best read through residual signed variation.

**Retain all canonical Gaussian marks.** This keeps a finer sigma-field and the sharp uniform block cost is factorial. The theorem does not by itself give a fixed-datum divergence result because the saturating frequency changes with \(m\). The later lacunary construction packs all needed frequencies into one smooth datum and proves non-\(L^1\) for the raw-faithful class.

**Average the internal bridge coordinates.** This passes to a coarser Gaussian sigma-field. On a genuine multi-edge patch, the residual score has geometric growth. Globally, however, naive patchwise bridge coarsening does not solve the quadratic-Hessian problem: the fixed-datum obstruction can be realized on right combs, whose maximal-left patches all have length one, so there is no bridge coordinate to average on those genealogies. See [Time-spine coarsening for quadratic Hessian patches](time-spine-coarsening-for-quadratic-hessian-patches.md).

The final [residual signed variation theorem](residual-signed-variation-characterization-for-coarsened-patches.md) shows that neither ``Gaussian marks survive'' nor ``Gaussian marks are averaged'' is itself the integrability criterion. The exact invariant is the total variation left after the chosen conditional averaging.
