---
title: Parabolic maximum principle and Schauder estimates
status: standard fact
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

For \(0<\alpha<1\), the parabolic Hölder seminorm uses the scaling \(t\sim x^2\):

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

There is a rougher theory below Schauder regularity. Uniformly parabolic equations with merely bounded measurable coefficients have interior Hölder estimates under the appropriate divergence or nondivergence hypotheses: De Giorgi--Nash--Moser theory applies to divergence-form equations, while Krylov--Safonov theory applies to scalar uniformly parabolic nondivergence equations. These estimates control oscillation on compact subcylinders away from the initial time, but do not supply the second-derivative bounds of Schauder theory.

For example, if a sequence of uniformly parabolic equations has coefficients uniformly bounded between \(\kappa\) and \(K\), interior Hölder estimates can provide compactness of the solutions on \([\tau,T]\times\mathbb T\) for every \(\tau>0\). To identify second derivatives or pass a nonlinear coefficient through a classical equation, additional regularity is generally needed.

## Why these estimates matter here

The maximum principle and Schauder estimates are the deterministic tools behind the self-consistent second-order diffusion route studied later in this project. The relevant smallness condition controls the coefficient inside a fixed ellipticity window; Hölder/Schauder control then supplies the regularity of \(z=v_{xx}\). Gaussian kernel bounds are a different tool and require their own structural hypotheses, recorded in [Aronson and Nash Gaussian bounds](aronson-nash-gaussian-bounds.md).