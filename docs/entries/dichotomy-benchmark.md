---
title: Dichotomy benchmark
status: definition
tags:
  - PDE
  - branching process
  - coding tree
  - Feynman-Kac formula
  - integrability
---

# Dichotomy benchmark

The *dichotomy benchmark* is the one-dimensional terminal-value problem

$$
\partial_tu(t,x)
+\frac12\partial_x^2u(t,x)
+\eta\left(e^{(\partial_xu(t,x))^4}-1\right)
=0,
\qquad
u(T,x)=a\cos x,
\tag{1}
$$

where

$$
\eta\in\mathbb R\setminus\{0\},
\qquad
0<a\leq a_*,
\qquad
 a_*=
\frac{\operatorname{erfc}(1/\sqrt2)}{\sqrt3}.
\tag{2}
$$

Here the complementary error function is

$$
\operatorname{erfc}(r)
=
\frac{2}{\sqrt\pi}
\int_r^\infty e^{-s^2}\,ds.
\tag{3}
$$

It is a special case of the [heat-reference terminal PDE](heat-reference-fully-nonlinear-pde.md) with \(n=1\), terminal datum

$$
\phi(x)=a\cos x,
$$

and jet nonlinearity

$$
f(z_0,z_1)
=\eta(e^{z_1^4}-1).
\tag{4}
$$

The nonlinearity is entire and has the globally convergent expansion

$$
f(z_0,z_1)
=
\sum_{r=1}^\infty
\frac{\eta}{r!}z_1^{4r}.
\tag{5}
$$

The relevant entire-function terminology is defined in [Directional jet radius](directional-jet-radius.md). Equation (5) allows the same driver to be encoded directly by the countable monomial family used in the [marked branching diffusion for gradient nonlinearities](marked-branching-diffusion-for-gradient-nonlinearities.md). At the same time, repeated jet differentiation of (4) is visible to the [Nguwi--Penent--Privault coding tree](npp-coding-tree.md). These two encodings are compared in [Representation-level dichotomy](representation-level-dichotomy.md).

**References.** The two branching constructions are those of Jiang Yu Nguwi, Guillaume Penent, and Nicolas Privault, *A fully nonlinear Feynman-Kac formula with derivatives of arbitrary orders*, arXiv:2201.03882, and Pierre Henry-Labordère, Nadia Oudjane, Xiaolu Tan, Nizar Touzi, and Xavier Warin, *Branching diffusion representation of semilinear PDEs and Monte Carlo approximation*, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* **55** (2019), no. 1, 184--210, arXiv:1603.01727; see [References](../meta/references.md).

## HLOTW monomial data

For the HLOTW notation, take

$$
d=m=1,
\qquad
\mu=0,
\qquad
\sigma=1,
\qquad
b_1=1,
$$

and

$$
L=\{\ell_r=(0,4r):r\geq1\},
\qquad
c_{\ell_r}=\frac{\eta}{r!}.
\tag{6}
$$

Then the HLOTW driver

$$
\sum_{\ell\in L}
c_\ell y^{\ell_0}(b_1z)^{\ell_1}
$$

is exactly (4). The branching probabilities used for the explicit comparison are

$$
p_r
=
\frac{1}{(e-1)r!},
\qquad r\geq1.
\tag{7}
$$

They satisfy

$$
\sum_{r\geq1}p_r=1,
\qquad
\sum_{r\geq1}|\ell_r|p_r
=
\frac{4e}{e-1}<\infty,
\qquad
\frac{|c_{\ell_r}|}{p_r}
=|\eta|(e-1).
\tag{8}
$$

The explicit positive horizon used in the comparison is

$$
T_*(\eta)
=
\frac{1}{2\pi e(e-1)^2\eta^2}.
\tag{9}
$$
