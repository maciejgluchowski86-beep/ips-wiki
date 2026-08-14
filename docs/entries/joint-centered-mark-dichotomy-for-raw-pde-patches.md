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

A centered Hessian edge is too singular to propagate a pathwise Hölder norm at fixed regularity, and a stepwise decreasing Hölder scale pays the sharp Banach-scale cost recorded in the [Banach-scale obstruction](banach-scale-obstruction-for-raw-pde-patches.md). One can avoid that *stepwise* architecture by composing several centered marks first and taking the first absolute moment only after the whole block has been formed.

That modification gives a real gain already for two marks, but at arbitrary block length it leads to a new dichotomy.

- If all Gaussian marks in the block are retained as random variables until the final absolute value, the derivative-loss ladder disappears but the optimal uniform block norm grows factorially, of order \(C^m m!\).
- If the internal Gaussian bridge marks are signedly averaged before the absolute value, a bare \(m\)-edge derivative chain collapses to one \(He_{2m}\) endpoint weight. The time-simplex factor then reduces the coefficient to geometric growth. For spatially varying patches, the corresponding geometric bound is supplied by the commutator/cluster estimate in [Hölder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md).

The second branch is a *partially averaged estimator*. It no longer retains all continuous interior marks and therefore does not prove the literal [raw random-patch conjecture](l1-random-patch-conjecture-for-quadratic-hessian-pde.md).

The estimates below are proved here. They are statements about uniform block norms and exact Gaussian conditioning identities. They do **not** prove that the raw infinite-depth estimator diverges for one fixed smooth terminal datum.

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

Define the uniform retained-mark block constant

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

There are constants \(0<c_{\alpha,T}\leq C_{\alpha,T}<\infty\) such that for every \(m\geq1\),

$$
c_{\alpha,T}^m m!
\leq
\mathfrak R_m(\alpha,T)
\leq
C_{\alpha,T}^m m!.
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

after enlarging the constant and using \(m^m\leq e^m m!\) up to a harmless universal Stirling factor.

### Lower bound

For an integer \(N\geq1\), take

$$
f_N(x)=N^{-\alpha}\cos(Nx).
\tag{15}
$$

Then \([f_N]_{C^\alpha}\asymp1\), uniformly in \(N\). Moreover,

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

The proof is the same compactness/Riemann--Lebesgue argument used for the one-edge lower bound: \(G\) is continuous and strictly positive on compact subsets of \((0,\infty)\), while for large \(q\) the oscillatory term cannot cancel the strictly positive \(L^1\) mass of \(|He_2|\) under Gaussian measure.

For fixed \(\mathbf r\), equations (2) and (16) therefore give

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

Restrict the duration integral to

$$
1\leq q_j=N\sqrt{r_j}\leq Q,
\qquad
Q=N\sqrt{\frac{T}{2m}}.
$$

This box lies inside \(\Sigma_m(T)\). Since \(dr_j/r_j=2dq_j/q_j\), equations (18)--(19) yield

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

Choose \(N\) of order

$$
N
\asymp
\sqrt{\frac{m}{T}}\,
 e^{m/\alpha}.
\tag{21}
$$

Then \(\log Q\asymp m/\alpha\) and

$$
N^{-\alpha}
\asymp
T^{\alpha/2}m^{-\alpha/2}e^{-m}.
$$

Thus the right side of (20) is bounded below by

$$
 c_{\alpha,T}^m
m^{-\alpha/2}
\left(\frac{m}{e}\right)^m.
$$

Stirling's formula and absorption of the remaining polynomial factor into the exponential constant give

$$
\mathfrak R_m(\alpha,T)
\geq
c_{\alpha,T}^m m!,
$$

proving the lower half of (10).

The optimizing frequency in (21) depends on \(m\). This point is important later.

## Signed averaging of Gaussian bridge marks

The factorial in (10) comes from retaining the \(m\) Gaussian marks separately until the absolute value is taken. There is an exact signed collapse if the internal Gaussian bridge variables are integrated first.

Let

$$
Y
=
\sum_{j=1}^m\sqrt{r_j}Z_j,
\qquad
R=\sum_{j=1}^m r_j,
\qquad
Z=\frac{Y}{\sqrt R}.
\tag{22}
$$

Then \(Z\sim N(0,1)\). The variable \(Y\) is the total Brownian displacement; the remaining \(m-1\) Gaussian degrees of freedom are bridge coordinates describing how that displacement is split among the edges.

### Proposition: bridge-score identity

One has

$$
\mathbb E\left[
\left.
\prod_{j=1}^m
\frac{He_2(Z_j)}{r_j}
\right|Y
\right]
=
\frac{He_{2m}(Z)}{R^m}.
\tag{23}
$$

To prove (23), test both sides against a bounded smooth function \(F(Y)\). Repeated Gaussian integration by parts on the left gives

$$
\mathbb E\left[
F(Y)
\prod_{j=1}^m
\frac{He_2(Z_j)}{r_j}
\right]
=
\partial_x^{2m}P_RF(x)\big|_{x=0}.
$$

The one-Gaussian Hermite formula gives the same quantity as

$$
\mathbb E\left[
F(\sqrt RZ)
\frac{He_{2m}(Z)}{R^m}
\right].
$$

Since this holds for all such \(F\), the conditional-expectation identity (23) follows.

Equation (23) is a signed Gaussian identity. It is unavailable if one has already replaced the individual score weights by their absolute values.

## Geometric growth after bridge averaging

For a bare consecutive derivative chain, replace the \(m\) separate Gaussian score marks by the bridge-averaged endpoint score in (23). Because \(\mathbb E He_{2m}(Z)=0\), a Hölder increment gives

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

For fixed total duration \(R\), the simplex of positive \((r_1,\ldots,r_m)\) with sum \(R\) has volume

$$
\frac{R^{m-1}}{(m-1)!}.
\tag{26}
$$

Consequently the time-integrated coefficient is bounded by

$$
\frac{c_{2m,\alpha}}{(m-1)!}
\int_0^T R^{-1+\alpha/2}\,dR
\leq
C_{\alpha,T}
\frac{\sqrt{(2m)!}}{(m-1)!}.
\tag{27}
$$

Finally,

$$
\frac{\sqrt{(2m)!}}{(m-1)!}
=
m\sqrt{\binom{2m}{m}}
\leq
m2^m
\leq
4^m,
\tag{28}
$$

after enlarging the base of the geometric bound. Thus the factorial retained-mark scale collapses to geometric growth once the bridge marks are signedly averaged before the absolute value.

### Spatially varying side profiles

Identity (23) applies literally to a bare derivative chain. In a full Duhamel patch, multiplication by spatially varying side profiles occurs between Hessian transfers, so the whole patch does not collapse directly to one \(He_{2m}\) weight. This is the same caveat recorded in the [finite patch theorem](finite-depth-duhamel-patch-regrouping.md).

The conclusion nevertheless remains geometric after signed interior averaging under uniform spatial \(C^\alpha\) control of the side profiles. Commuting derivative blocks through the multipliers splits the patch into derivative clusters. A cluster of length \(\ell\) contributes

$$
\frac{c_{2\ell,\alpha}}{(\ell-1)!}
R^{-1+\alpha/2},
$$

with coefficient at most geometric in \(\ell\), and the full commutator expansion has at most \(2^m\) terms. This is exactly the deterministic cluster estimate proved in [Hölder cancellation for heat-semigroup derivatives](holder-cancellation-for-heat-semigroup-derivatives.md).

Thus the bare bridge identity explains the mechanism, while the commutator expansion supplies the corresponding full-patch geometric estimate.

## Relation to the Banach-scale obstruction

The [Banach-scale theorem](banach-scale-obstruction-for-raw-pde-patches.md) applies to a proof that takes a first-moment Banach norm after every centered edge and propagates one-edge operator bounds down a decreasing scale. The joint block construction does not satisfy that hypothesis. It forms

$$
\Delta_{h_m}\cdots\Delta_{h_1}f
$$

before taking the first absolute moment, so several centered translations can interact inside the same random variable.

The evasion is therefore mathematical rather than terminological: equation (7) is a finite two-edge same-input-regularity estimate obtained without introducing any intermediate loss parameter. The price appears only when the block length is allowed to grow: theorem (10) gives the replacement obstruction \(C^m m!\).

## Relation to conjecture C

The two branches must be kept distinct.

**Retained marks.** The random block (2) keeps all Gaussian marks. Its sharp uniform first-moment block norm is factorial. This blocks a direct proof that tries to control arbitrary raw length-\(m\) patches by one uniform Hölder-to-first-moment block estimate. It does not prove that the actual raw estimator for a fixed datum is non-\(L^1\), because the lower bound uses the generation-dependent frequency (21).

**Bridge-averaged marks.** Equation (23) integrates out the \(m-1\) internal bridge coordinates before the absolute value. The remaining endpoint Gaussian is still random, but the original continuous interior marks are no longer all retained. This is a Rao--Blackwell-type partial averaging of the raw Gaussian data. It has the favorable geometric scale (27)--(28), but it violates item 3 in the literal statement of conjecture C, which requires the continuous interior Gaussian/Hermite marks to remain random rather than be deterministically integrated out.

Thus the geometric branch is not conjecture C in disguise. It is another partially averaged representation between the fully raw estimator and the completely interior-averaged skeleton estimator of [Theorem C-prime](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md).

## What remains open

The theorem replaces the derivative-loss barrier by a different tradeoff:

- retaining the full Gaussian interior randomness permits joint centered cancellation but leaves factorial uniform block growth;
- signedly averaging the Gaussian bridge variables recovers geometric growth but gives up part of that interior randomness.

Neither statement is a disproof of conjecture C. The factorial lower bound uses a frequency depending on \(m\), just as the Banach-scale lower bound uses a frequency depending on the regularity loss. To disprove C one would need a lower bound tied to one fixed smooth datum, or another argument showing that the actual raw estimator fails to belong to \(L^1\).

Conversely, a proof of C can no longer be expected from a stepwise Banach-scale estimate or from a uniform all-order retained-mark block norm. It would have to preserve additional structure not seen by those norms: frequency together with genealogy, correlations between different patches, a martingale or square-function mechanism, or cancellation across several centered marks that survives without integrating those marks out.