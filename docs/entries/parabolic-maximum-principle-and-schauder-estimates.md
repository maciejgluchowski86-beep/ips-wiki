---
title: Parabolic maximum principle and Schauder estimates
status: standard fact
audit: current
tags:
  - PDE
  - parabolic equation
  - maximum principle
  - Schauder estimate
  - Holder regularity
---

# Parabolic maximum principle and Schauder estimates

Uniformly parabolic equations have two complementary regularity mechanisms used repeatedly in the PDE branch of this wiki. The maximum principle controls the size of a solution without differentiating it. Schauder estimates convert Hölder regularity of the coefficients and forcing into quantitative control of spatial and temporal derivatives.

**References.** Lawrence C. Evans, *Partial Differential Equations*, second edition, American Mathematical Society, 2010. For classical parabolic Schauder theory, see also Avner Friedman, *Partial Differential Equations of Parabolic Type*, Prentice-Hall, 1964. See [References](../meta/references.md).

**Prerequisite.** See [Elliptic, parabolic, and hyperbolic equations](elliptic-parabolic-and-hyperbolic-equations.md) for the principal-part classification and the uniform-parabolicity convention used below.

Throughout this page, \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) is the one-dimensional torus.

## Uniform parabolicity

For

$$
\partial_tv=a(t,x)\partial_x^2v+f(t,x),
\tag{1}
$$

the coefficient is *uniformly elliptic* or, in the time-dependent equation, *uniformly parabolic* on a time interval if there are constants

$$
0<\kappa\leq K<\infty
$$

such that

$$
\kappa\leq a(t,x)\leq K
\tag{2}
$$

for every relevant \((t,x)\).

## Maximum principle

Assume \(v\in C^{1,2}([0,T]\times\mathbb T)\), \(f=0\), and \(a\geq0\). Then

$$
\max_{x\in\mathbb T}v(t,x)
\leq
\max_{x\in\mathbb T}v(0,x),
\qquad
\min_{x\in\mathbb T}v(t,x)
\geq
\min_{x\in\mathbb T}v(0,x).
\tag{3}
$$

Indeed, at an interior spatial maximum one has \(v_x=0\) and \(v_{xx}\leq0\), hence \(v_t=a v_{xx}\leq0\). The corresponding statement for a minimum follows by applying the same argument to \(-v\). Standard perturbation by \(-\varepsilon t\) removes the possibility of a first flat maximum when proving the global statement rigorously.

The maximum principle is an \(L^\infty\) estimate for the *direct* nondivergence equation (1). It should not be confused with an \(L^\infty\) estimate for its adjoint density equation \(\rho_t=\partial_x^2(a\rho)\); the latter has different structure.

## Parabolic Hölder spaces

The precise norm is defined in [Parabolic Holder spaces](parabolic-holder-spaces.md). For \(0<\alpha<1\), it uses the scaling \(t\sim x^2\):

$$
[f]_{C^{\alpha/2,\alpha}}
=
\sup_{(t,x)\neq(s,y)}
\frac{|f(t,x)-f(s,y)|}
{|t-s|^{\alpha/2}+|x-y|^\alpha}.
\tag{4}
$$

The space \(C^{1+\alpha/2,2+\alpha}\) consists of functions whose time derivative and second spatial derivative exist and are parabolically Hölder continuous of exponent \(\alpha\), together with the corresponding lower derivatives.

## Schauder estimate

Let \(a,f\in C^{\alpha/2,\alpha}([0,T]\times\mathbb T)\), assume (2), and let \(v_0\in C^{2+\alpha}(\mathbb T)\). The classical periodic solution of

$$
\partial_tv-a(t,x)v_{xx}=f,
\qquad
v(0,\cdot)=v_0,
\tag{5}
$$

satisfies an estimate of the form

$$
\lVert v\rVert_{C^{1+\alpha/2,2+\alpha}([0,T]\times\mathbb T)}
\leq
C
\left(
\lVert v_0\rVert_{C^{2+\alpha}}
+
\lVert f\rVert_{C^{\alpha/2,\alpha}}
+
\lVert v\rVert_{C^0}
\right),
\tag{6}
$$

where \(C\) depends on \(\alpha,T,\kappa,K\) and the Hölder norm of \(a\). On the compact torus, standard existence theory and the maximum principle allow the \(C^0\) term to be controlled by the data in the usual linear problems.

The dependence of \(C\) matters. Schauder theory does **not** give a constant depending only on the ellipticity window if the Hölder norm of the coefficient is allowed to diverge.

## Interior Hölder regularity

Below Schauder regularity there is a rough-coefficient theory. [Interior Holder estimates](interior-holder-estimates-for-parabolic-equations.md) hold for uniformly parabolic equations with bounded measurable coefficients under the appropriate operator form: De Giorgi--Nash--Moser theory treats divergence-form weak solutions, while Krylov--Safonov theory treats scalar nondivergence equations.

These estimates give compactness of bounded solution families on cylinders away from the parabolic boundary, but they do not supply second-derivative bounds. To identify \(v_{xx}\) or control a nonlinear coefficient through a classical equation, the stronger Schauder hypotheses are needed.

## Related tools

Gaussian kernel bounds are a different tool and require their own structural hypotheses, recorded in [Aronson and Nash Gaussian bounds](aronson-nash-gaussian-bounds.md).
