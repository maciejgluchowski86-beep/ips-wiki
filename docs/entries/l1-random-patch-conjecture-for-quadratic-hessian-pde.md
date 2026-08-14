---
title: L1 random-patch conjecture for the quadratic Hessian PDE
status: conjecture
tags:
  - PDE
  - branching process
  - patch
  - integrability
  - conjecture
  - Hessian
  - coarsening
---

# L1 random-patch conjecture for the quadratic Hessian PDE

The abstract coarsening problem is now understood exactly. The remaining conjecture is about **one structured, target-uniform representation architecture**, not about the mere pointwise existence of some nonconstant coarsening.

The relevant theorem is [Residual signed variation characterizes coarsened patch representations](residual-signed-variation-characterization-for-coarsened-patches.md). If a raw skeleton measure is

$$
\mu_\tau=R_\tau\nu_\tau
$$

and \(\mathcal C_\tau\) is a skeleton-preserving coarsening, then

$$
\boxed{
\|(\mathcal C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}
=
\int
\left|
\mathbb E_{\nu_\tau}
[R_\tau\mid\sigma(\mathcal C_\tau)]
\right|d\nu_\tau.
}
\tag{1}
$$

For a fixed target \((t,x)\), summability of (1) over \(\tau\) is necessary and sufficient for \(L^1\) in the coarsened conditional-barycenter class. Thus the invariant is **residual signed variation**, not the type of retained variable.

## PDE and C-prime regime

Fix

$$
0<\alpha<1,
\qquad
T>0,
\qquad
\lambda\in\mathbb R,
\qquad
\phi\in C^{2+\alpha}(\mathbb T),
$$

and write

$$
\partial_tv
=
\frac12v_{xx}+\lambda(v_{xx})^2,
\qquad
v(0)=\phi,
\qquad
z=v_{xx}.
$$

Let

$$
X_{\alpha,T}
=
C^{\alpha/2,\alpha}([0,T]\times\mathbb T),
\qquad
M=\|P_\cdot\phi''\|_{X_{\alpha,T}},
$$

and put

$$
a
=
|\lambda|C_{\mathcal D}(\alpha,T)M.
$$

The C-prime regime is

$$
4a<1.
\tag{2}
$$

Under (2), [Theorem C-prime](skeleton-averaged-l1-representation-for-quadratic-hessian-pde.md) gives

$$
\sum_\tau|F_\tau(t,x)|<\infty
$$

uniformly through the stronger \(X_{\alpha,T}\)-norm estimate.

## What is completely settled

### Raw-faithful retention is impossible

The [raw-barycenter obstruction](raw-marked-l1-obstruction-for-quadratic-hessian-pde.md) constructs one fixed arbitrarily small smooth datum for which identity/raw-faithful retention has a divergent total-variation subseries. Pure importance sampling, proposal changes, dependence among proposal variables, and auxiliary conditionally unbiased randomness cannot repair it.

In the residual-variation formula, identity coarsening gives

$$
\mathbb E[R_\tau\mid\sigma(\operatorname{Id})]
=R_\tau,
$$

so no signed variation is removed.

### Complete averaging is L1

For constant coarsening,

$$
\|(\mathcal C_\tau)_\#\mu_\tau\|_{\mathrm{TV}}
=|F_\tau(t,x)|.
$$

This is exactly C-prime and is summable throughout (2).

### A structured intermediate exists

The [time-spine theorem](time-spine-coarsening-for-quadratic-hessian-patches.md) retains the actual ordered branch times on one root maximal-left patch while averaging all other continuous variables. If

$$
4a<1,
\qquad
bC(a)<1,
$$

where

$$
b
=
|\lambda|K_{\mathrm{time}}(\alpha,T)M,
\qquad
C(a)
=
\frac{1-\sqrt{1-4a}}{2a},
$$

then the residual variations are summable. Hence there is a genuine \(L^1\) representation with nondecorative continuous time randomness.

### Naive patchwise Gaussian bridges fail

The fixed-datum obstruction may be realized on right combs. Under the maximal-left-patch convention, every patch of such a comb has one edge. One-edge Gaussian-bridge coarsening is the identity up to an invertible coordinate change, so it preserves the divergent residual variation.

## Fixed-target existence is no longer open

The residual-variation theorem also shows that, at every **fixed** target \((t,x)\) in the C-prime regime, there are many nonconstant \(L^1\) coarsenings which retain genuine raw continuous randomness.

Indeed, let \((\varepsilon_\tau)_\tau\) be positive and summable. Since every finite non-leaf raw patch measure has a nonatomic total-variation measure on its continuous coordinates, choose a nonnull set \(A_\tau\) with

$$
|\mu_\tau^{t,x}|(A_\tau)
\leq
\varepsilon_\tau.
$$

Retain the entire raw marked state on \(A_\tau\) and collapse \(A_\tau^c\) to one point. Then

$$
\begin{aligned}
\|(\mathcal C_\tau)_\#\mu_\tau^{t,x}\|_{\mathrm{TV}}
&=
|\mu_\tau^{t,x}|(A_\tau)
+|\mu_\tau^{t,x}(A_\tau^c)|\\
&\leq
|F_\tau(t,x)|+2\varepsilon_\tau.
\end{aligned}
$$

The sum is finite. On \(A_\tau\), all Gaussian/Hermite, branch-time, and descendant coordinates remain visible and affect the estimator.

Thus the old question

> for a fixed target, does there exist *some* nonconstant coarsening with genuine continuous randomness and finite first moment?

has an affirmative answer throughout the full C-prime regime.

This also shows why Gaussian survival is not the invariant. Entire Gaussian configurations may survive on sufficiently small pieces, whereas an abstract time-only coarsening can still have nonsummable residual variation.

## Conjecture C: target-uniform structured formulation

The remaining conjecture is the following stronger and more useful statement.

> **Conjecture C.** Under the full C-prime condition (2), there exists one patch-first coarsening architecture, specified independently of the individual observation point \((t,x)\), which retains nondecorative continuous interior information and whose residual signed variations are summable with quantitative control sufficient to define an \(L^1\) representation for every \((t,x)\in[0,T]\times\mathbb T\).

The time-spine construction proves this on its stronger small-data subregime. The sparse full-state construction above is pointwise and is deliberately not counted as a solution of this target-uniform structured conjecture.

Natural stronger versions may require the coarsening to be local in the patch, to retain a nonvanishing amount of information uniformly over skeletons, or to satisfy an explicit computational constraint.

## What the characterization changes

The conceptual hierarchy is no longer

> Gaussian marks bad, time marks good, complete averaging safest.

The exact statement is

> A retained sigma-field is admissible precisely to the extent that the conditional barycenter visible through it has summable \(L^1\) norm.

Equivalently, cancellation before absolute values is the reduction of signed variation under conditional averaging. The named coordinates are secondary; residual signed variation is the invariant.
