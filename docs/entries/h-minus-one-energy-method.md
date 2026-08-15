---
title: The H^{-1} energy method on the torus
status: standard fact
audit: current
tags:
  - PDE
  - Sobolev space
  - energy estimate
  - parabolic equation
---

# The H^{-1} energy method on the torus

The $H^{-1}$ energy method is useful for equations in which two spatial derivatives fall on a flux. Testing against the inverse Laplacian removes those two derivatives and produces an $L^2$ dissipation term. On the torus this requires zero spatial mean, because constants lie in the kernel of the Laplacian.

**References.** The method is a standard Sobolev-space energy argument; see Lawrence C. Evans, *Partial Differential Equations*, second edition, American Mathematical Society, 2010, for weak derivatives, Sobolev spaces, and energy methods. See [References](../meta/references.md).

Throughout, $\mathbb T=\mathbb R/(2\pi\mathbb Z)$, and integrals are over one period.

## Definition of the energy

Let $w\in H^{-1}(\mathbb T)$ satisfy $\langle w,1\rangle=0$. There is a unique zero-mean $\psi\in H^1(\mathbb T)$ such that

$$
-\partial_x^2\psi=w
\tag{1}
$$

in the weak sense. Define

$$
\lVert w\rVert_{H^{-1}}^2
:=
\int_{\mathbb T}|\partial_x\psi|^2\,dx.
\tag{2}
$$

The weak formulation of (1) gives

$$
\lVert w\rVert_{H^{-1}}^2
=
\langle w,\psi\rangle_{H^{-1},H^1}.
\tag{3}
$$

Equivalently, for a zero-mean $w\in H^{-1}(\mathbb T)$ with Fourier coefficients $\widehat w_k$,

$$
\lVert w\rVert_{H^{-1}}^2
=
2\pi\sum_{k\neq0}\frac{|\widehat w_k|^2}{k^2}.
\tag{4}
$$

The restriction $w\in H^{-1}$ is exactly what makes the energy in (2)--(4) finite; an arbitrary zero-mean distribution need not have finite inverse-Laplacian energy.

## Basic energy identity

Suppose $w$ has zero mean for every time and satisfies

$$
\partial_tw
=
\partial_x^2(a w+F).
\tag{5}
$$

One explicit sufficient regularity regime for the calculation below is

$$
w\in C^1([0,T];L^2(\mathbb T)),
\qquad
G:=aw+F\in C([0,T];H^2(\mathbb T)),
\tag{6}
$$

with (5) holding in $L^2(\mathbb T)$. These assumptions are stronger than necessary, but they make every differentiation and integration by parts classical in the relevant Sobolev spaces.

Let $\psi=(-\partial_x^2)^{-1}w$ with zero mean. Since

$$
-\partial_x^2\psi_t
=
\partial_x^2G,
$$

the zero-mean normalization gives

$$
\psi_t
=-G+\frac1{2\pi}\int_{\mathbb T}G\,dx.
$$

The constant disappears when paired with the zero-mean function $w$. Differentiating (3) therefore gives

$$
\frac12\frac{d}{dt}\lVert w\rVert_{H^{-1}}^2
=
-\int a w^2\,dx
-\int Fw\,dx.
\tag{7}
$$

If $a\geq\kappa>0$, then

$$
\frac12\frac{d}{dt}\lVert w\rVert_{H^{-1}}^2
+
\kappa\lVert w\rVert_2^2
\leq
\left|\int Fw\,dx\right|.
\tag{8}
$$

## Contraction estimate

Suppose

$$
F=\beta v,
\qquad
\lVert\beta\rVert_\infty\leq\delta.
$$

Then

$$
\left|\int Fw\,dx\right|
\leq
\delta\lVert v\rVert_2\lVert w\rVert_2.
$$

Young's inequality in the form

$$
2\delta XY
\leq
\kappa X^2+
\frac{\delta^2}{\kappa}Y^2
$$

gives from (7)

$$
\frac{d}{dt}\lVert w\rVert_{H^{-1}}^2
+
\kappa\lVert w\rVert_2^2
\leq
\frac{\delta^2}{\kappa}\lVert v\rVert_2^2.
\tag{9}
$$

If $w(0)=0$, integration yields

$$
\sup_{0\leq s\leq t}\lVert w(s)\rVert_{H^{-1}}^2
+
\kappa\int_0^t\lVert w(s)\rVert_2^2\,ds
\leq
\frac{\delta^2}{\kappa}
\int_0^t\lVert v(s)\rVert_2^2\,ds.
\tag{10}
$$

Consequently, at the level of the space-time $L^2$ norm,

$$
\lVert w\rVert_{L^2_tL^2_x}
\leq
\frac{\delta}{\kappa}
\lVert v\rVert_{L^2_tL^2_x}.
\tag{11}
$$

Thus $\delta<\kappa$ gives a contraction.

## Mean-zero condition

Integrating (5) over the torus gives

$$
\frac{d}{dt}\int_{\mathbb T}w(t,x)\,dx=0.
$$

Hence equal initial means remain equal and their difference has mean zero for all time. The $H^{-1}$ estimate controls such mean-zero differences. Recovering an underlying function from its second derivative still leaves a time-dependent spatial constant; that constant must be fixed separately by the mean evolution of the original PDE.
