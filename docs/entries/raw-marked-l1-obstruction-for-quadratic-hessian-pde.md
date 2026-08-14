---
title: Raw-barycenter L1 obstruction for the quadratic Hessian PDE
status: proved here
tags:
  - PDE
  - patch
  - integrability
  - total variation
  - importance sampling
  - lacunary series
  - Hessian
---

# Raw-barycenter L1 obstruction for the quadratic Hessian PDE

For the quadratic Hessian equation, the previous obstruction theorems were barriers to particular estimates: fixed pathwise Hölder/Besov norms fail, a decreasing Hölder scale pays at least \((cn/\Delta)^n\), and an all-order retained Gaussian block has a sharp uniform \(C^m m!\) norm. Those lower bounds used frequencies depending on the generation or block length, so they did not show that one fixed smooth datum has a nonintegrable raw estimator.

This page removes that caveat for a precise class of estimators. A single smooth terminal datum can contain all of the required exponentially separated frequencies. On a disjoint family of long comb genealogies, the intrinsic total variation of the **raw centered marked contribution** is not summable. The conclusion is proposal invariant: changing the lifetime law, the genealogy proposal, the Gaussian proposal, or dependencies among those proposal variables only changes the Radon--Nikodym density used by the estimator, not the total variation of the underlying signed comb measure.

The theorem deliberately does **not** quantify over every unbiased estimator that happens to use Gaussian marks. Its class is the **raw-barycenter-retaining class**: after the canonical raw genealogy and interior marks are exposed, any additional randomization must still have the raw signed marked integrand as its conditional mean. This includes arbitrary importance sampling and auxiliary conditionally unbiased randomization, but excludes antithetic, bridge-averaged, control-variate, or multi-sample schemes that move signed mass between different raw marked realizations.

That distinction is essential for the relation to [Conjecture C](l1-random-patch-conjecture-for-quadratic-hessian-pde.md).

**References.** The centered Hessian mark and finite conditional construction are recorded in [Conditional factorization for finite PDE patches](conditional-factorization-for-finite-pde-patches.md). The all-order retained-block estimate and the lower-bound function \(G\) are in [Joint centered-mark dichotomy for raw PDE patches](joint-centered-mark-dichotomy-for-raw-pde-patches.md). The smooth fixed-datum construction uses [Lacunary and Hadamard-gap trigonometric series](lacunary-and-hadamard-gap-trigonometric-series.md). Proposal cancellation and disjoint-event lower bounds are isolated in [Disjoint-event lower bounds for compensated branching estimators](disjoint-event-lower-bounds-for-compensated-branching-estimators.md). Heat-kernel positivity is recorded in [Brownian confinement and heat-kernel positivity](brownian-confinement-and-heat-kernel-positivity.md). The theorem below is proved here.

## Quadratic Hessian equation

Fix

$$
T>0,
\qquad
\lambda\in\mathbb R\setminus\{0\},
\qquad
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Consider

$$
\partial_tv
=
\frac12v_{xx}
+\lambda(v_{xx})^2,
\qquad
v(0)=\phi.
\tag{1}
$$

Writing

$$
z=v_{xx},
\qquad
g=\phi'',
$$

gives

$$
z(t)
=
P_tg
+\lambda\int_0^t
\partial_x^2P_{t-s}[z(s)^2]\,ds.
\tag{2}
$$

A centered raw realization of one Hessian transfer of duration \(r>0\) is

$$
\widehat K_rF(x,Z)
=
\frac{He_2(Z)}{r}
\left[
F(x+\sqrt r Z)-F(x)
\right],
\qquad
He_2(Z)=Z^2-1,
\tag{3}
$$

with \(Z\sim N(0,1)\). Its signed expectation is exactly \(\partial_x^2P_rF\).

## Long combs and their intrinsic signed measures

A *length-\(m\) comb* is the planar binary Duhamel tree in which one distinguished child continues through exactly \(m\) consecutive quadratic branchings, while the other child at every branching is a terminal side leaf; after the \(m\)-th branching the distinguished child is terminal as well.

Fix a remaining horizon

$$
h=T-t>0.
$$

We restrict to combs whose distinguished edge durations \(r_1,\ldots,r_m\) satisfy

$$
r_j>0,
\qquad
r_1+\cdots+r_m<\frac h2.
\tag{4}
$$

Every side leaf and the final distinguished leaf then has remaining heat time in \([h/2,h]\).

At finite depth, the exact patch randomization from the finite conditional-factorization theorem produces a finite signed measure on the following raw data:

- the comb genealogy and its durations;
- the fresh Gaussian/Hermite marks at the \(m\) centered Hessian edges;
- the independent terminal Brownian marks of the \(m\) side leaves and the final distinguished leaf.

After the usual lifetime, genealogy-selection, and survival compensators are cancelled against the corresponding positive sampling factors, denote this intrinsic signed marked measure by

$$
\nu_m.
$$

For each fixed \(m\), smooth terminal data make \(\nu_m\) a finite signed measure. Its total variation is denoted by \(\|\nu_m\|_{\mathrm{TV}}\).

Different values of \(m\) correspond to disjoint raw genealogies: the distinguished lineage has exactly \(m\) internal vertices and then terminates. Thus the comb cylinders are pairwise disjoint.

## Raw-barycenter-retaining estimators

The class is most cleanly defined by contradiction, for an assumed integrable candidate. This avoids writing an ordinary conditional expectation of an object whose integrability is precisely what is at issue.

Let \((\Omega,\mathcal F,Q)\) be any simulation probability space and let \(R\) denote its exposed *raw coordinate*: the sampled canonical genealogy together with the branch-time, Gaussian/Hermite, and descendant marks that are being retained. The law \(Q\) may use arbitrary dependencies among these proposal variables and may include any additional auxiliary randomness outside \(R\).

For the raw length-\(m\) comb cylinder \(\Gamma_m\), let \(Q_m\) be the restriction of the raw-coordinate proposal law to that cylinder. Assume

$$
\nu_m\ll Q_m.
\tag{5}
$$

If (5) fails, that proposal cannot retain this raw comb contribution as a conditional barycenter.

An integrable candidate estimator \(Y\in L^1(Q)\) is called *raw-barycenter-retaining on the combs* if, for every \(m\),

$$
\mathbb E_Q[Y\mid\sigma(R)]
=
\frac{d\nu_m}{dQ_m}(R)
\qquad
Q\text{-a.s. on }\Gamma_m.
\tag{6}
$$

Equation (6) is the precise retention property used in the theorem. It says that proposal changes and auxiliary randomness may alter how the raw state is sampled or how its contribution is randomized, but they may not transfer signed mass between different raw marked states once \(R\) is fixed.

Conditional Jensen gives, on every comb cylinder,

$$
\begin{aligned}
\mathbb E_Q[|Y|\mathbf1_{\Gamma_m}]
&\ge
\mathbb E_Q\left[
\left|
\mathbb E_Q[Y\mid\sigma(R)]
\right|
\mathbf1_{\Gamma_m}
\right]\\
&=
\int_{\Gamma_m}
\left|
\frac{d\nu_m}{dQ_m}
\right|dQ_m
=
\|\nu_m\|_{\mathrm{TV}}.
\end{aligned}
\tag{7}
$$

This already shows why the class is proposal invariant: the right side of (7) depends only on the intrinsic signed comb measure, not on \(Q_m\).

## A Fourier lower bound for one comb

Let

$$
\widehat g(k)
=
\frac1{2\pi}
\int_0^{2\pi}g(x)e^{-ikx}\,dx.
$$

Suppose

$$
\widehat g(1)=a,
\qquad
\widehat g(N)=b,
\tag{8}
$$

for some integer \(N>m\). The other Fourier coefficients of \(g\) are arbitrary.

There are constants \(A_h>0\) and \(B_h>0\), depending only on \(h\), such that whenever

$$
N^2\frac{h}{4m}>1,
\tag{9}
$$

the length-\(m\) comb satisfies

$$
\boxed{
\|\nu_m\|_{\mathrm{TV}}
\ge
A_h
\bigl(B_h|\lambda|\,|a|\bigr)^m
|b|
\left[
\log\left(\frac{hN^2}{4m}\right)
\right]^m.
}
\tag{10}
$$

The estimate is a total-variation statement. It is therefore insensitive to cancellation with any other frequencies in the same fixed datum.

### Terminal Fourier projections

Let \(p_s^{\mathbb T}(x,y)\) be the periodic heat kernel. Since every terminal leaf has remaining time in \([h/2,h]\),

$$
\kappa_h
=
\min_{\substack{h/2\le s\le h\\x,y\in\mathbb T}}
p_s^{\mathbb T}(x,y)
>0.
\tag{11}
$$

For any integer \(k\), any such \(s\), and a leaf started at \(x\), the complex test function

$$
\Psi_{k,s,x}(y)
=
\frac{\kappa_h}{p_s^{\mathbb T}(x,y)}
e^{-ik(y-x)}
\tag{12}
$$

has modulus at most one. Hence total-variation duality permits its use. Integrating a terminal leaf against (12) gives

$$
\begin{aligned}
&\int_{\mathbb T}
p_s^{\mathbb T}(x,y)g(y)
\Psi_{k,s,x}(y)\,dy\\
&\qquad=
2\pi\kappa_h\widehat g(k)e^{ikx}.
\end{aligned}
\tag{13}
$$

Thus the final distinguished leaf can be projected exactly onto frequency \(N\), while every side leaf can be projected exactly onto frequency \(1\). No assumption on the remaining Fourier coefficients is needed.

A complex test may be replaced by one of its real or imaginary parts at the cost of a universal factor, so (13) is legitimate for the total variation of a real signed measure.

### The \(m\) logarithmic Hessian factors

After the final leaf is projected onto \(e^{iNx}\), multiplication by the innermost side mode \(e^{ix}\) produces frequency \(N+1\). After the next side multiplication the frequency is \(N+2\), and so on. Thus the centered Hessian edges act successively on pure modes with frequencies

$$
K_j\in\{N+1,\ldots,N+m\}.
\tag{14}
$$

For a pure mode \(e^{iKx}\), equation (3) contributes the raw multiplier

$$
\frac{He_2(Z)}r
\left(e^{iK\sqrt r Z}-1\right).
\tag{15}
$$

Define

$$
G(q)
=
\mathbb E\left[
|He_2(Z)|\,|e^{iqZ}-1|
\right].
\tag{16}
$$

As proved in the joint centered-mark entry, there is a constant \(c_G>0\) such that

$$
G(q)\ge c_G,
\qquad q\ge1.
\tag{17}
$$

Restrict every duration to the box

$$
N^{-2}
\le r_j\le
\frac{h}{4m},
\qquad
1\le j\le m.
\tag{18}
$$

This box lies inside (4), and \(K_j\sqrt{r_j}\ge1\). Taking the phase of each factor (15) into the total-variation test gives

$$
\int_{N^{-2}}^{h/(4m)}
\frac{G(K_j\sqrt r)}r\,dr
\ge
c_G
\log\left(\frac{hN^2}{4m}\right).
\tag{19}
$$

The fresh Gaussian marks are independent in the intrinsic finite-patch measure, so the \(m\) factors multiply. Combining (13), the \(m\) quadratic coefficients \(|\lambda|\), and (19) proves (10), after absorbing fixed factors into \(A_h,B_h\).

The point is the shape of (19): after absolute values, every retained centered Hessian mark contributes one logarithm. Restricting to the rectangular duration region (18) is why no compensating \(1/m!\) appears.

## One fixed smooth datum contains every required scale

Choose an integer

$$
K\ge3,
\qquad
N_m=K^m,
\qquad
b_m=(m!)^{-1/2}.
\tag{20}
$$

For \(m_0\) sufficiently large and \(\varepsilon>0\), define the terminal datum for the Hessian equation by

$$
g_\varepsilon(x)
=
\varepsilon
\left[
\cos x
+
\sum_{m\ge m_0}
b_m\cos(N_mx)
\right].
\tag{21}
$$

This is one fixed function, not a sequence of test data.

For every fixed integer \(k\ge0\),

$$
\sum_{m\ge m_0}
b_mN_m^k
=
\sum_{m\ge m_0}
\frac{K^{km}}{\sqrt{m!}}
<\infty,
\tag{22}
$$

because the ratio of consecutive terms is

$$
\frac{K^k}{\sqrt{m+1}}
\longrightarrow0.
$$

Hence termwise differentiation is valid to every order and

$$
g_\varepsilon\in C^\infty(\mathbb T).
\tag{23}
$$

The function has mean zero. Therefore it is the second derivative of the smooth periodic function

$$
\phi_\varepsilon(x)
=
-\varepsilon\cos x
-
\varepsilon
\sum_{m\ge m_0}
\frac{b_m}{N_m^2}
\cos(N_mx),
\tag{24}
$$

so that \(\phi_\varepsilon''=g_\varepsilon\).

For the datum (21),

$$
|\widehat g_\varepsilon(1)|
=
\frac\varepsilon2,
\qquad
|\widehat g_\varepsilon(N_m)|
=
\frac{\varepsilon b_m}{2}.
\tag{25}
$$

Apply (10) with \(N=N_m\). Since

$$
\log\left(
\frac{hN_m^2}{4m}
\right)
=
2m\log K-\log m+O_h(1)
\ge c_Km
\tag{26}
$$

for all sufficiently large \(m\), there are positive constants \(A_h,C_h\) such that

$$
\|\nu_m\|_{\mathrm{TV}}
\ge
A_h\varepsilon
\left(C_h|\lambda|\varepsilon\right)^m
\frac{m^m}{\sqrt{m!}}.
\tag{27}
$$

Stirling's formula gives

$$
\frac{m^m}{\sqrt{m!}}
=
\exp\left(
\frac12m\log m+O(m)
\right),
\tag{28}
$$

which beats every fixed exponential factor. Consequently

$$
\|\nu_m\|_{\mathrm{TV}}
\not\longrightarrow0,
\qquad
\sum_{m\ge m_0}
\|\nu_m\|_{\mathrm{TV}}
=\infty.
\tag{29}
$$

This is the step that defeats the earlier generation-dependent-frequency caveat: all frequencies \(N_m\) occur simultaneously in the single smooth datum (21).

## Theorem: no L1 estimator in the raw-barycenter-retaining class

Fix \(T>0\) and \(\lambda\ne0\). Let \(\phi_\varepsilon\) be the single smooth terminal datum (24). For every

$$
0\le t<T,
\qquad
x\in\mathbb T,
$$

there is no estimator \(Y(t,x)\in L^1\) which is raw-barycenter-retaining on the long combs in the sense of (5)--(6).

More precisely, for every proposal law satisfying the domination conditions (5), regardless of the lifetime distribution, genealogy-selection probabilities, Gaussian importance-sampling law, dependence among proposal variables, or auxiliary conditionally unbiased randomness,

$$
\boxed{
\mathbb E_Q|Y(t,x)|=\infty.
}
\tag{30}
$$

### Proof

Assume for contradiction that \(Y(t,x)\in L^1(Q)\). The comb cylinders \(\Gamma_m\) are pairwise disjoint, so by (7) and Tonelli,

$$
\begin{aligned}
\mathbb E_Q|Y(t,x)|
&\ge
\sum_{m\ge m_0}
\mathbb E_Q\left[
|Y(t,x)|\mathbf1_{\Gamma_m}
\right]\\
&\ge
\sum_{m\ge m_0}
\|\nu_m\|_{\mathrm{TV}}.
\end{aligned}
\tag{31}
$$

The last series diverges by (29), contradicting \(Y(t,x)\in L^1\). This proves (30).

## Why the theorem is proposal invariant

The proposal invariance is not a special cancellation requiring product-form proposals. On \(\Gamma_m\), every admissible proposal merely chooses a dominating positive measure \(Q_m\) for the same intrinsic signed measure \(\nu_m\). The conditional barycenter is its Radon--Nikodym derivative. Therefore

$$
\int
\left|
\frac{d\nu_m}{dQ_m}
\right|dQ_m
=
\|\nu_m\|_{\mathrm{TV}}.
\tag{32}
$$

A small genealogy probability appears as a large reciprocal density in (32); a small lifetime or Gaussian proposal density does the same. Jointly dependent proposals are covered by the joint Radon--Nikodym derivative. Adding auxiliary randomness cannot improve the first moment because conditional Jensen gives (7).

This is the measure-theoretic version of the proposal/lifetime cancellation used in the repeated-Hessian obstruction.

## The datum may be chosen inside the C-prime small-data regime

For every fixed \(\alpha\in(0,1)\) and \(T>0\), the function in brackets in (24) has finite \(C^{2+\alpha}\) norm. Multiplying it by \(\varepsilon\) scales that norm linearly. Hence \(\varepsilon>0\) may be chosen small enough that

$$
4|\lambda|C_{\mathcal D}(\alpha,T)
\|P_\cdot\phi_\varepsilon''\|_{X_{\alpha,T}}
<1.
\tag{33}
$$

For that same datum, [Theorem C-prime](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) gives an unbiased \(L^1\) skeleton-only estimator, while theorem (30) rules out every raw-barycenter-retaining estimator. Thus the obstruction is representation-level and persists at arbitrarily small amplitude.

## Exact scope relative to Conjecture C

The theorem falsifies the following strong reading of C:

> **Raw-barycenter C.** Keep a canonical raw marked genealogy as part of the simulation state, allow arbitrary proposal changes and auxiliary conditionally unbiased randomization, but require the canonical raw signed marked contribution to remain the conditional mean after those raw marks are exposed.

Raw-barycenter C is false even for one fixed \(C^\infty\) datum in the C-prime small-data regime.

The theorem does **not** falsify the literal wording of Conjecture C presently used in this wiki, which only says that the continuous interior marks remain random rather than being deterministically integrated out. A natural estimator can use those marks while changing their conditional barycenter.

For example, at one Hessian edge the antithetic estimator

$$
\widetilde K_rF(x,Z)
=
\frac{He_2(Z)}{2r}
\left[
F(x+\sqrt rZ)
+F(x-\sqrt rZ)
-2F(x)
\right]
\tag{34}
$$

still samples and uses the Gaussian mark \(Z\). By symmetry of the standard Gaussian and the evenness of \(He_2\),

$$
\mathbb E\widetilde K_rF
=
\partial_x^2P_rF.
\tag{35}
$$

But, given \(Z\), (34) is not the raw centered integrand (3). Thus it lies outside (6). The bridge-averaged construction in the joint centered-mark theorem, control variates whose mean vanishes only after averaging over raw states, and coupled multi-sample estimators escape for the same structural reason.

Accordingly, the surviving open problem is narrower and more precise:

> Can an \(L^1\) random-patch representation keep nontrivial continuous interior randomness while **changing the raw conditional barycenter through signed coupling or partial averaging across raw marked states**?

The theorem proves that some such departure from raw-barycenter retention is necessary. It does **not** prove that complete interior averaging is necessary, and therefore it does not prove that C-prime is minimal or optimal among all possible escape mechanisms. C-prime is the fully averaged endpoint that is currently proved.
