---
title: Representation-level dichotomy
status: proved here
tags:
  - PDE
  - branching process
  - coding tree
  - Feynman-Kac formula
  - integrability
---

# Representation-level dichotomy

For the [dichotomy benchmark](dichotomy-benchmark.md), the raw [Nguwi--Penent--Privault coding-tree](npp-coding-tree.md) functional is not absolutely integrable at any positive horizon, while a [Henry-Labordère--Oudjane--Tan--Touzi--Warin marked branching](marked-branching-diffusion-for-gradient-nonlinearities.md) estimator has finite second moment on an explicit positive time interval. The comparison is between two tree constructions attached to the same terminal-value PDE and the same terminal datum. The HLOTW construction gives a viscosity solution on the stated interval; no solution representation is attributed to the NPP tree in this example because the integrability premise of the [NPP Feynman--Kac theorem](npp-coding-tree-feynman-kac-theorem.md) fails.

**References.** Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882. Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* **55** (2019), no. 1, 184--210, arXiv:1603.01727. See [References](../meta/references.md).

Fix

$$
\eta\neq0,
\qquad
0<a\leq
\frac{\operatorname{erfc}(1/\sqrt2)}{\sqrt3},
$$

and consider

$$
\partial_tu+\frac12\partial_x^2u
+\eta\left(e^{(\partial_xu)^4}-1\right)=0,
\qquad
u(T,x)=a\cos x.
\tag{1}
$$

Write

$$
T_*(\eta)
=
\frac{1}{2\pi e(e-1)^2\eta^2}.
\tag{2}
$$

## Theorem

For equation (1), the following statements hold.

1. **NPP coding tree.** For every \(T>0\), every \(0\leq t<T\), and every \(x\in\mathbb R\),

$$
\mathbb E\left[
\left|H(\mathcal T_{t,x,f^*})\right|
\right]
=
\infty,
\qquad
f(z_0,z_1)=\eta(e^{z_1^4}-1).
\tag{3}
$$

Moreover,

$$
\mathbb E\left[
\left|H(\mathcal T_{t,x,\operatorname{Id}})\right|
\right]
=
\infty.
\tag{4}
$$

These conclusions hold for every strictly positive NPP lifetime density and for the positive mechanism-selection probabilities in the coding-tree construction.

2. **HLOTW marked branching.** Let \(0<T<T_*(\eta)\). Take the monomial data and branching probabilities from the [benchmark entry](dichotomy-benchmark.md), and choose

$$
\rho_T(s)
=
\frac{s^{-1/2}e^{-s/(2T)}}{\sqrt{2\pi T}},
\qquad s>0.
\tag{5}
$$

Then the HLOTW estimator \(\psi_{t,x}\) satisfies

$$
\mathbb E|\psi_{t,x}|^2
\leq1
\qquad
(0\leq t\leq T,\ x\in\mathbb R),
\tag{6}
$$

and

$$
u(t,x)=\mathbb E[\psi_{t,x}]
\tag{7}
$$

is a continuous viscosity solution of (1).

The second statement uses the singular-lifetime extension established below. The density (5) is continuous and strictly positive on \((0,T]\) but diverges at zero, so it does not literally satisfy the endpoint wording of HLOTW Assumption 3.1.

## Proof of the NPP statement

The terminal datum is \(\phi(x)=a\cos x\), so

$$
\phi''(x)=-a\cos x\not\equiv0.
$$

Thus the direction \(j=1\) is active for the [repeated-Hessian obstruction](repeated-hessian-obstruction-for-coding-trees.md). For \(r\geq1\), the globally convergent series

$$
e^{z^4}
=
\sum_{q=0}^\infty\frac{z^{4q}}{q!}
$$

gives, for real \(z\),

$$
\partial_z^{4r}e^{z^4}
=
\sum_{q=r}^\infty
\frac{(4q)!}{q!(4q-4r)!}z^{4(q-r)}
\geq
\frac{(4r)!}{r!}.
\tag{8}
$$

Consequently,

$$
\left|
\partial_{z_1}^{4r}f(z_0,z_1)
\right|
\geq
|\eta|\frac{(4r)!}{r!}
\tag{9}
$$

uniformly on \(\mathbb R^2\). For any bounded set \(B\) of positive Lebesgue measure, the quantity from the repeated-Hessian theorem therefore satisfies

$$
D_{2r}(B;f,1)
\geq
|B|\,|\eta|\frac{(4r)!}{r!}.
$$

Hence

$$
\limsup_{m\to\infty}
\left(
\frac{D_m(B;f,1)}{m!}
\right)^{1/m}
=
\infty,
$$

as is immediate along \(m=2r\) from Stirling's formula. The repeated-Hessian obstruction gives (3). Its proof also shows why the conclusion is independent of the auxiliary lifetime and mechanism probabilities: on each restricted genealogy these sampling probabilities cancel the reciprocal weights in \(H\).

For the identity code, the NPP mechanism has

$$
\mathcal M(\operatorname{Id})=\{(f^*)\}.
$$

Condition on the first identity branching occurring before \(T\). Its unique child is an \(f^*\)-rooted coding tree with a strictly positive remaining horizon. By (3), its conditional absolute expectation is infinite for every possible branching time and location. Tonelli's theorem then gives (4).

## Published HLOTW hypotheses and the endpoint issue

HLOTW equation (2.1) permits a subset \(L\subseteq\mathbb N^{m+1}\) and puts a probability mass function on \(L\); no finiteness requirement on \(L\) is stated. Their Assumption 3.1 requires positive offspring probabilities with finite mean offspring number, a lifetime density continuous and strictly positive on \([0,T]\) with positive survival probability past \(T\), bounded continuous diffusion coefficients that are Lipschitz in space, and bounded continuous monomial coefficients and gradient directions. Assumption 3.6 adds bounded continuous first spatial derivatives of the diffusion coefficients and uniform ellipticity.

For constant \(\mu=0\) and \(\sigma=1\), their automatic-differentiation weight becomes

$$
\mathcal W_{t,s}
=
\frac{W_s-W_t}{s-t}.
\tag{10}
$$

Their Assumption 3.10(i), for some \(q>1\), asks that both

$$
C_{1,q}\left(\frac1{\overline F(T)}\right)^q
\leq1
\tag{11}
$$

and

$$
\sup_{\ell\in L,\,s\in(0,T]}
C_{2,q}
\left(
\frac{\lVert c_\ell\rVert_\infty}
{p_\ell\sqrt{s}\rho(s)}
\right)^q
\leq1
\tag{12}
$$

hold. HLOTW Remark 3.11 observes that (12) in the gradient case requires a density with \(\rho(s)\gtrsim s^{-1/2}\) near zero when the coefficient-to-offspring ratios are uniformly bounded. Section 5 then recommends Gamma laws with shape parameter at most \(1/2\). Such laws are singular at zero. Thus the finite endpoint continuity required literally by Assumption 3.1 is incompatible with the paper's own explicit gradient criterion and Gamma implementation at the borderline shape \(1/2\).

The next proposition isolates the extension actually used here rather than treating (5) as a literal instance of Assumption 3.1.

## Proposition

For the benchmark data and the Gamma density (5), suppose the positive-time conditions (11)--(12) hold with \(q=2\). Then the proof of HLOTW Theorems 3.5 and 3.12 applies with Assumption 3.1's endpoint-continuity clause replaced by continuity and strict positivity of \(\rho\) on \((0,T]\). In particular, (6)--(7) follow.

## Proof

The density (5) is a probability density on \((0,\infty)\); every sampled lifetime is strictly positive almost surely. The branching law has finite mean offspring number, so the age-dependent branching process has finitely many particles on every finite horizon by the same nonexplosion argument used by HLOTW.

All factors in the HLOTW estimator are evaluated either at a strictly positive internal lifetime increment or through the survival function \(\overline F\). Thus \(\rho(0)\) is never evaluated. The Gamma density is finite, continuous, and strictly positive at every positive argument, while its survival function is continuous at zero with \(\overline F(0)=1\).

The automatic-differentiation statement is independent of the lifetime law. In the proof of HLOTW Theorem 3.12, every internal lifetime increment \(\Delta T_k\) is positive and the \(q\)-moment estimate is obtained from the multiplicative majorant

$$
\prod_{k\in\mathcal K_T^\partial}
C_{1,q}
\left(\frac1{\overline F(\Delta T_k)}\right)^q
\prod_{k\in\mathcal K_T^\circ}
C_{2,q}
\left(
\frac{\lVert c_{I_k}\rVert_\infty}
{p_{I_k}\sqrt{\Delta T_k}\rho(\Delta T_k)}
\right)^q.
\tag{13}
$$

Conditions (11)--(12) bound every factor in (13) by one, giving the same uniform \(L^q\) estimate as in the published proof. In particular, the estimator families required by HLOTW Theorem 3.5 are locally uniformly integrable.

The continuity step in the proof of HLOTW Theorem 3.5 is also unchanged. For a fixed tree realization, every internal lifetime at which \(\rho\) is evaluated is strictly positive, so only continuity on \((0,T]\) is used; the event that a branching time falls exactly at the terminal horizon has probability zero. Uniform integrability then supplies the same passage to expectations. The first-branch conditioning identity and the viscosity argument use the density only through positive lifetime values and \(\overline F\). Therefore the singular value at the unused endpoint does not affect the proof.

This proves the stated singular-lifetime extension for (5).

## Verification of the HLOTW bound

Use the countable monomial data

$$
L=\{(0,4r):r\geq1\},
\qquad
c_r=\frac{\eta}{r!},
\qquad
p_r=\frac1{(e-1)r!}.
\tag{14}
$$

The series in the HLOTW driver is then absolutely convergent for every gradient value and equals \(\eta(e^{z^4}-1)\). Moreover,

$$
\sum_{r\geq1}4r p_r
=
\frac{4e}{e-1}<\infty,
\qquad
\frac{|c_r|}{p_r}
=|\eta|(e-1).
\tag{15}
$$

Thus the offspring and coefficient parts of Assumption 3.1 hold. The coefficients \(\mu=0\), \(\sigma=1\), and \(b_1=1\) satisfy both the remaining diffusion conditions of Assumption 3.1 and Assumption 3.6. The terminal datum \(a\cos x\) is bounded and Lipschitz with both supremum norm and Lipschitz constant equal to \(a\).

For the density (5),

$$
\overline F_T(T)
=
\operatorname{erfc}(1/\sqrt2).
\tag{16}
$$

Take \(q=2\). If \(Z\sim N(0,1)\), then on a Brownian edge of length \(s-t\),

$$
X_s-x=\sqrt{s-t}\,Z,
\qquad
\mathcal W_{t,s}
=\frac{Z}{\sqrt{s-t}}.
$$

From the HLOTW definition of \(C_{1,2}\), with the auxiliary scalar \(|b_0|\leq a\),

$$
\mathbb E|b_0(X_s-x)\mathcal W_{t,s}|^2
=
b_0^2\mathbb E Z^4
\leq3a^2.
$$

Since \(\lVert\phi\rVert_\infty^2=a^2\), this gives

$$
C_{1,2}=3a^2.
\tag{17}
$$

The first condition (11) is therefore

$$
\frac{3a^2}{\operatorname{erfc}(1/\sqrt2)^2}
\leq1,
$$

which is exactly the restriction \(a\leq a_*\).

Similarly,

$$
C_{2,2}
=
\mathbb E|Z|^2
=1.
\tag{18}
$$

Finally,

$$
\sqrt{s}\rho_T(s)
=
\frac{e^{-s/(2T)}}{\sqrt{2\pi T}},
$$

so for \(0<s\leq T\),

$$
\frac1{\sqrt{s}\rho_T(s)}
=
\sqrt{2\pi T}\,e^{s/(2T)}
\leq
\sqrt{2\pi eT}.
\tag{19}
$$

Using (15), the left side inside the square in (12) is bounded by

$$
|\eta|(e-1)\sqrt{2\pi eT}.
$$

Thus (12) with \(q=2\) holds whenever

$$
2\pi e(e-1)^2\eta^2T
\leq1.
\tag{20}
$$

Solving (20) gives exactly

$$
T
\leq
\frac1{2\pi e(e-1)^2\eta^2}
=T_*(\eta).
\tag{21}
$$

For the strict range \(T<T_*(\eta)\) in the theorem, both HLOTW majorant conditions hold. The proposition and the \(q=2\) estimate in the proof of HLOTW Theorem 3.12 give (6). First-branch conditioning recovers the countable series in (14), which is the entire driver in (1), and the HLOTW viscosity argument gives (7).

## Interpretation

The distinction is at the level of representation. The NPP mechanism repeatedly differentiates the jet nonlinearity; in this benchmark the derivatives contain the factorial scale

$$
\partial_{z_1}^{4r}f
\gtrsim
\frac{(4r)!}{r!},
$$

which is detected by the repeated-Hessian genealogy. The HLOTW construction instead branches over the monomial coefficients \(\eta/r!\) and transfers only first spatial derivatives through marked Malliavin weights. The same [mild equation](mild-formulation-and-branching-diffusion-representation.md) is therefore sampled by two structurally different tree constructions with different absolute-moment behavior.

This does not contradict the NPP Feynman--Kac theorem. That theorem assumes all-code \(L^1\) integrability; the benchmark violates that premise. Nor does the comparison assert that both tree functionals represent a common solution: only the HLOTW expectation is identified here with a viscosity solution, while the NPP statement is the failure of the raw coding-tree functional's required integrability.
