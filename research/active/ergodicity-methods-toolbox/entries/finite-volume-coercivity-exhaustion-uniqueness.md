---
method_id: finite-volume-coercivity-exhaustion-uniqueness
title: Finite-volume coercivity plus semigroup exhaustion to infinite-volume uniqueness
category: finite-to-infinite
targets:
  - uniqueness
model_scope: Continuous-spin finite-range Gibbs fields and their infinite-dimensional Glauber-type diffusion semigroups
source_status: primary-checked
primary_source: Pierre-André Zitt, Functional inequalities and uniqueness of the Gibbs measure - from log-Sobolev to Poincare, ESAIM Probability and Statistics 12 (2008), 258-272.
primary_pinpoint: Assumptions 1-2 and Theorem 2.2; decomposition (12) and the proof on pp. 5-7 for log-Sobolev; Lemma 3.6 and the completion of the Beckner case on pp. 10-11
primary_url: https://doi.org/10.1051/ps:2007054
application_source: Pierre-André Zitt, Functional inequalities and uniqueness of the Gibbs measure - from log-Sobolev to Poincare, ESAIM Probability and Statistics 12 (2008), 258-272.
application_pinpoint: Theorem 2.2
application_url: https://arxiv.org/abs/math/0702403
wiki_candidate: yes
---

# Finite-volume coercivity plus semigroup exhaustion to infinite-volume uniqueness

## Criterion

Uniform finite-volume functional inequalities do not by themselves constitute an infinite-volume theorem; one needs an interface controlling how finite semigroups approximate the infinite dynamics while the box grows. Zitt gives such an exhaustion argument for continuous-spin finite-range Gibbs fields.

Let \(\Lambda_n=[-n,n]^d\), fix a tempered boundary condition (the paper uses zero), let \(\mu_n\) be the corresponding finite-volume Gibbs law, and let \(P_t^{\Lambda_n}\) and \(P_t\) denote the finite- and infinite-volume diffusion semigroups. Theorem 2.2 proves uniqueness of the tempered infinite-volume Gibbs measure under either of two finite-volume coercivity hypotheses:

1. \(\mu_n\) satisfies a logarithmic Sobolev inequality with constants \(C_n\) obeying
\[
C_n\le C\frac{n}{\log n},
\]
with \(C\) below an explicit model-dependent threshold; or
2. \(\mu_n\) satisfies a generalized Beckner inequality \(GBI(a)\) with constants uniform in \(n\), for an exponent \(a>a_{\min}\) specified by the interaction and dimension.

The conclusion is **uniqueness of the tempered Gibbs measure in infinite volume**. The finite-volume constants need not even be uniformly bounded in the logarithmic-Sobolev branch.

## Mechanism

The proof exposes the limiting interface through the exact decomposition
\[
P_tf
=
(P_tf-P_t^{\Lambda_n}f)
+(P_t^{\Lambda_n}f-\mu_nf)
+\mu_nf.
\tag{*}
\]
The box is not sent to infinity independently of time. Instead Zitt chooses \(n=n(t)\) proportional to \(t\).

The first term in (*) is a finite-speed/locality error: if the boundary is at distance of order \(t\) from the support of \(f\), the finite- and infinite-volume evolutions are close despite the time growth of derivative estimates. The second term is the finite-volume relaxation error. LSI gives enough entropy decay even when its constant grows like \(n/\log n\); in the second branch a generalized Beckner inequality gives slower, subexponential entropy decay, and Lemma 3.6 shows it is still sufficient when \(n(t)\asymp t\).

For the third term, compactness produces a subsequence \(\mu_{n(t_k)}\) converging to a tempered Gibbs measure \(\mu\). The first two errors imply \(P_{t_k}f(x)\to\mu(f)\) for tempered configurations. If \(\nu\) is any other tempered Gibbs measure, it is invariant for \(P_t\); bounded convergence then gives
\[
\nu(f)=\nu(P_{t_k}f)\longrightarrow\mu(f),
\]
so \(\nu=\mu\).

## Representative IPS use

The source treats an infinite-dimensional system of interacting real-valued spins with finite-range smooth interaction and the associated reversible stochastic dynamics. Its theorem is precisely a finite-volume-to-infinite-volume transfer: functional inequalities are proved or assumed only in growing boxes with one fixed tempered boundary condition, while uniqueness is concluded for the full infinite-volume Gibbs specification.

This is useful when a coercive inequality is naturally accessible through finite-dimensional diffusion calculus but its constants deteriorate mildly with volume. The exhaustion can tolerate that deterioration provided relaxation on \(\Lambda_{n(t)}\) still beats the finite-volume approximation error.

## Limitations

The argument needs quantitative locality of the dynamics and tightness/compactness of the finite-volume Gibbs laws. A finite-volume gap or LSI with uncontrolled volume growth is insufficient; the relaxation time must be compatible with the speed at which the box must grow to screen its boundary. The theorem concerns tempered Gibbs measures and a particular class of finite-range continuous-spin interactions, not arbitrary IPS.

This proof interface is distinct from the live finite-size strong-mixing criterion. Martinelli--Olivieri bootstrap one mesoscopic spatial-mixing estimate to uniform coercivity in larger finite volumes. Zitt instead starts from a **sequence of finite-volume coercive estimates** and couples the volume to time in order to pass to an infinite-volume uniqueness statement. It is also stronger as a limiting architecture than merely saying that a uniform finite-volume gap has an infinite-volume limit: the semigroup approximation and invariant-measure identification are explicit load-bearing steps.

## Sources

- Zitt, *Functional inequalities and uniqueness of the Gibbs measure - from log-Sobolev to Poincare*, Assumptions 1-2, Theorem 2.2, decomposition (12), and Lemma 3.6, https://doi.org/10.1051/ps:2007054.
- Open preprint: https://arxiv.org/abs/math/0702403.
