---
method_id: weak-poincare-glauber-relaxation
title: Weak Poincare inequalities from nonuniform Glauber relaxation
category: functional-inequality
targets:
  - convergence
model_scope: Infinite-volume heat-bath Glauber dynamics for translation-invariant Markov random fields, including attractive low-temperature Ising phases
source_status: primary-checked
primary_source: Florian Völlering, A variance inequality for Glauber dynamics applicable to high and low temperature regimes, Electronic Journal of Probability 19 (2014), no. 46, 1-21.
primary_pinpoint: Theorem 3.1 (coupling-to-variance estimate), Theorem 3.3 and Corollary 3.4 (attractive/Ising application), and Proposition 4.8 (weak Poincare inequality and relaxation consequence)
primary_url: https://doi.org/10.1214/EJP.v19-2791
application_source: Florian Völlering, A variance inequality for Glauber dynamics applicable to high and low temperature regimes, Electronic Journal of Probability 19 (2014), no. 46, 1-21.
application_pinpoint: Corollary 3.4 and Proposition 4.8
application_url: https://arxiv.org/abs/1208.2578
wiki_candidate: yes
---

# Weak Poincare inequalities from nonuniform Glauber relaxation

## Criterion

A weak Poincare inequality relaxes the uniform coercivity of an ordinary Poincare inequality by allowing a remainder term. In a standard form,
\[
\operatorname{Var}_\mu(f)
\le \alpha(r)\,\mathcal E(f,f)+r\,\Phi(f),\qquad r>0,
\]
where \(\alpha(r)\) may diverge as \(r\downarrow0\). Optimizing the scale \(r\) along the semigroup yields subexponential or polynomial-type variance decay even when no useful uniform spectral gap is available.

Völlering derives such an inequality directly for infinite-volume Glauber dynamics from the decay of a single-spin disturbance. Let \(\theta_t(\eta)\) be the probability, under the basic graphical coupling of configurations differing only at the origin, that the two copies still disagree at time \(t\). Theorem 3.1 defines weighted tail integrals \(D_p(T)\) of \(\|\theta_t\|_{L^q(\mu)}\) and proves
\[
\operatorname{Var}_\mu(S_Tf)
\le C_dD_p(T)
\sum_x\| (\nabla_xf)^2\|_{L^p(\mu)}.
\]
Under a uniform positive lower bound on flip rates, Proposition 4.8 truncates the time integral at a scale \(R\) and obtains a weak Poincare inequality with a Dirichlet-form term proportional to the truncated integral and a remainder controlled by \(D_p(R)\). It then yields an explicit nonexponential decay function for \(\operatorname{Var}_\mu(S_Tf)\).

## Mechanism

The proof tracks how the effect of one spin flip spreads through the graphical construction. A martingale/telescoping decomposition of a general observable reduces its variance to the accumulated influence of single-site perturbations. If this influence is uniformly integrable in time, one recovers an ordinary Poincare inequality. When only an \(L^q(\mu)\) averaged influence is integrable, the same argument retains a scale-dependent remainder instead of forcing uniform coercivity.

This is exactly what weak Poincare inequalities are designed to encode. Short-time influence contributes to the Dirichlet energy; the long-time tail becomes the weak remainder. Choosing the splitting time as a function of the observation time converts whatever decay is known for the one-spin disturbance into relaxation for a broad class of observables.

## Representative IPS use

The source treats nearest-neighbour heat-bath spin-flip systems on \(\mathbb Z^d\). For attractive dynamics, Theorem 3.3 reduces the needed coupling quantity further to decay of the autocorrelation of the spin at the origin. Corollary 3.4 applies this mechanism to the low-temperature two-dimensional Ising plus phase, using available one-spin autocorrelation control to obtain quasi-polynomial relaxation for general quasi-local observables.

Thus the method can work in a phase-coexistence regime where uniform Dobrushin--Shlosman mixing is false and a global uniform Poincare estimate is not the right starting point.

## Limitations

The rate obtained is only as good as the single-site coupling or autocorrelation input, and Proposition 4.8 loses rate compared with the sharper direct estimate of Theorem 3.1 because the truncated uniform contribution also enters the weak-Poincare bound. The theorem assumes an invariant/ergodic reference phase; it does not prove uniqueness of the Gibbs state, and in low-temperature Ising it is deliberately applied inside one selected phase.

This is distinct from the live Liggett--Nash method. Nash inequalities interpolate Dirichlet energy with a separate size norm to produce algebraic smoothing. Here the weak coercivity profile is manufactured from **nonuniform dynamical influence tails** and may produce quasi-polynomial or other non-power-law relaxation. It is also distinct from the live RFIM large-set-conductance method, which converts a weak coercive estimate into isoperimetric control for warm-start mixing.

## Sources

- Völlering, *A variance inequality for Glauber dynamics applicable to high and low temperature regimes*, Theorem 3.1, Theorem 3.3, Corollary 3.4, and Proposition 4.8, https://doi.org/10.1214/EJP.v19-2791.
- Open preprint: https://arxiv.org/abs/1208.2578.
