---
title: Finite-volume coercivity plus semigroup exhaustion to infinite-volume uniqueness
status: literature
audit: current
tags:
  - finite volume
  - Gibbs uniqueness
  - functional inequalities
---

# Finite-volume coercivity plus semigroup exhaustion to infinite-volume uniqueness

## Criterion

Uniform finite-volume functional inequalities do not by themselves constitute an infinite-volume theorem; one needs an interface controlling how finite semigroups approximate the infinite dynamics while the box grows. Zitt gives such an exhaustion argument for continuous-spin finite-range Gibbs fields.

Let \(\Lambda_n=[-n,n]^d\), fix a tempered boundary condition, let \(\mu_n\) be the corresponding finite-volume Gibbs law, and let \(P_t^{\Lambda_n}\) and \(P_t\) denote the finite- and infinite-volume diffusion semigroups. Theorem 2.2 proves uniqueness of the tempered infinite-volume Gibbs measure under either of two finite-volume coercivity hypotheses:

1. \(\mu_n\) satisfies a logarithmic Sobolev inequality with constants \(C_n\) obeying
\[
C_n\le C\frac{n}{\log n},
\]
with \(C\) below an explicit model-dependent threshold; or
2. \(\mu_n\) satisfies a generalized Beckner inequality \(GBI(a)\) with constants uniform in \(n\), for an exponent \(a>a_{\min}\) specified by the interaction and dimension.

The conclusion is uniqueness of the tempered Gibbs measure in infinite volume. The finite-volume constants need not even be uniformly bounded in the logarithmic-Sobolev branch.

## Mechanism

The proof exposes the limiting interface through the decomposition
\[
P_tf=(P_tf-P_t^{\Lambda_n}f)+(P_t^{\Lambda_n}f-\mu_nf)+\mu_nf.
\]
The box is not sent to infinity independently of time. Instead Zitt chooses \(n=n(t)\) proportional to \(t\).

The first term is a finite-speed/locality error. The second is the finite-volume relaxation error. LSI gives enough entropy decay even when its constant grows like \(n/\log n\); in the second branch a generalized Beckner inequality gives slower, subexponential entropy decay, and Lemma 3.6 shows it is still sufficient when \(n(t)\asymp t\).

For the third term, compactness gives subsequential Gibbs limits. The first two errors force \(P_{t_k}f\) to converge to one such limit on tempered configurations. Any other tempered Gibbs measure is invariant for \(P_t\), so integrating the same convergence against it identifies the two Gibbs laws.

## Representative IPS use

The source treats an infinite-dimensional system of interacting real-valued spins with finite-range smooth interaction and the associated reversible stochastic dynamics. Functional inequalities are assumed only in growing boxes with one fixed tempered boundary condition, while uniqueness is concluded for the full infinite-volume Gibbs specification.

This is useful when coercivity is accessible in finite dimensions but its constants deteriorate mildly with volume. The exhaustion can tolerate that deterioration provided relaxation on \(\Lambda_{n(t)}\) still beats the finite-volume approximation error.

## Limitations

The argument needs quantitative locality of the dynamics and compactness/tightness of the finite-volume Gibbs laws. A finite-volume gap or LSI with uncontrolled volume growth is insufficient; the relaxation time must be compatible with the speed at which the box must grow to screen its boundary. The theorem concerns tempered Gibbs measures and a particular class of finite-range continuous-spin interactions.

This differs from the [finite-size strong-mixing criterion](finite-size-strong-mixing-criterion.md), which bootstraps one mesoscopic spatial-mixing estimate to large-volume coercivity. It also differs from the [graphical finite-speed transfer](finite-speed-finite-volume-transfer.md), where a common graphical construction directly transfers a quantitative local-observable relaxation estimate.

## Sources

- Zitt, *Functional inequalities and uniqueness of the Gibbs measure - from log-Sobolev to Poincare*, Assumptions 1-2, Theorem 2.2, decomposition (12), and Lemma 3.6, https://doi.org/10.1051/ps:2007054.
- Open preprint: https://arxiv.org/abs/math/0702403.
