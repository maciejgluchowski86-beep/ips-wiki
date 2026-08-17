---
title: Asymptotic reflection coupling for nonlinear infinite-dimensional SPDEs
status: literature
audit: current
tags:
  - coupling
  - reflection coupling
  - SPDE
---

# Asymptotic reflection coupling for nonlinear infinite-dimensional SPDEs

## Criterion

Let $\mathbb V\subset\mathbb H\subset\mathbb V^*$ be a Gelfand triple and consider the nonlinear stochastic evolution equation

\[
dX_t=A(t,X_t)\,dt+B(t,X_t)\,dW_t^{(1)}+Q\,dW_t^{(2)},
\]

where $Q$ is Hilbert--Schmidt. Wang assumes the standard hemicontinuity, monotonicity, coercivity and growth hypotheses $(A1)$--$(A4)$, strengthened by a quantitative dissipativity condition $(A1')$ or $(A1'')$ involving the intrinsic $Q$-norm of differences.

The formal reflection coupling would reflect the additive Brownian noise in the direction $Q^{-1}(X_t-Y_t)$. In infinite dimension this coefficient is generally too singular to define the reflected SPDE because $Q$ is Hilbert--Schmidt. Section 3 therefore replaces $Q^{-1}$ by $(Q+n^{-1}I)^{-1}$ and introduces a near-diagonal cutoff, producing a sequence of **asymptotic reflection couplings**. Proposition 3.1 supplies the coupling estimates needed to pass to semigroup bounds.

Theorems 2.1 and 2.3 derive quantitative gradient/Hölder estimates. In the time-homogeneous dissipative regime, Theorem 2.2 gives exponential loss of dependence on the starting point; for $r>1$,

\[
\sup_{x,y\in\mathbb H}|P_tf(x)-P_tf(y)|
   \le C\|f\|_\infty e^{-\lambda t}.
\]

Remark 2.2 identifies this with uniform total-variation contraction and, in the autonomous case, uniqueness of the invariant probability measure and strong exponential ergodicity.

## Mechanism

Finite-dimensional reflection coupling is effective because the difference process receives maximal noise in its radial direction. Directly transplanting that construction to a Hilbert space fails: the inverse covariance appearing in the reflection direction is unbounded and the reflected coefficient is not a well-defined continuous Hilbert--Schmidt operator.

The regularized couplings retain the geometric idea without requiring a limiting reflected process to exist. Away from the diagonal, the additive noise in the second copy is approximately reflected in the regularized intrinsic direction of $X_t-Y_t$; near the diagonal the reflection is smoothly switched off. Itô estimates for the distance produce uniform bounds on the approximate coupling times. One then uses these bounds directly on

\[
|P_tf(x)-P_tf(y)|,
\]

and lets the regularization parameter tend to infinity. The sequence of couplings is therefore a proof device even though convergence to one literal reflection coupling is not established.

This differs from synchronous weighted-$W_1$ contraction, where the same noise is used in both copies and drift dissipation alone contracts a fixed weighted distance. It also differs from feedback-based asymptotic binding: here the load-bearing object is a regularized **reflection** of the additive noise designed to create fast approach/coupling.

## Representative IPS use

Section 6 verifies the hypotheses for stochastic generalized porous-medium equations, stochastic $p$-Laplace equations, and stochastic generalized fast-diffusion equations. These are genuinely infinite-dimensional interacting fields. The reflection construction yields regularization estimates and, in the dissipative regimes covered by Theorem 2.2, exponential convergence to the invariant law.

## Limitations

The method relies on an additive noise component with injective covariance and quantitative control in its intrinsic norm. The drift must satisfy monotonicity/coercivity inequalities strong enough to dominate the uncontrolled directions. The word "monotone" here refers to monotone-operator SPDE structure, not an order-preserving attractive coupling of spin configurations. Reflection is implemented only through an approximating sequence, and the resulting hypotheses can be difficult to verify for degenerate noises with large unforced unstable subspaces. The strongest convergence conclusions also require the autonomous dissipative setting in which an invariant law exists.

## Sources

Feng-Yu Wang, *Asymptotic Couplings by Reflection and Applications for Non-Linear Monotone SPDEs*, Nonlinear Analysis **117** (2015), 55--66. Theorems 2.1--2.3 state the regularity and exponential-convergence consequences. Section 3 constructs the regularized reflection couplings, especially equation (3.2) and Proposition 3.1. Section 6 treats porous-medium, $p$-Laplace and fast-diffusion SPDEs. DOI: https://doi.org/10.1016/j.na.2015.01.012. Preprint: https://arxiv.org/abs/1407.3522
