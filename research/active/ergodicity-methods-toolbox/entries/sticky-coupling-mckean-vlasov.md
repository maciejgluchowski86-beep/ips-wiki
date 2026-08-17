---
method_id: sticky-coupling-mckean-vlasov
title: Sticky coupling for McKean--Vlasov diffusions
category: coupling
targets:
  - convergence
model_scope: McKean--Vlasov diffusions and their weakly interacting mean-field particle approximations
source_status: primary-checked
primary_source: Alain Durmus, Andreas Eberle, Arnaud Guillin and Katharina Schuh, "Sticky nonlinear SDEs and convergence of McKean--Vlasov equations without confinement," Stochastics and Partial Differential Equations: Analysis and Computations 12 (2024), 1855--1906
primary_pinpoint: Theorems 1--2 in Section 2; Theorem 7 in Section 3.3; Theorem 8 and Section 5
primary_url: https://doi.org/10.1007/s40072-023-00315-8
application_source: Alain Durmus, Andreas Eberle, Arnaud Guillin and Katharina Schuh, same paper
application_pinpoint: Theorem 1 for exponential McKean--Vlasov contraction and Theorem 8 for uniform-in-time propagation of chaos
application_url: https://doi.org/10.1007/s40072-023-00315-8
wiki_candidate: yes
---

# Sticky coupling for McKean--Vlasov diffusions

## Criterion

Durmus--Eberle--Guillin--Schuh consider nonlinear diffusions

\[
d\bar X_t=(b*\bar\mu_t)(\bar X_t)\,dt+dB_t,
\qquad \bar\mu_t=\operatorname{Law}(\bar X_t),
\]

with an antisymmetric drift decomposed as $b(z)=-Lz+\gamma(z)$, a one-sided dissipativity bound, and a quantitative smallness condition on the bounded nonlinear part $\gamma$; these are assumptions B1--B2 of the paper. Their Theorem 2 constructs a coupling $(\bar X_t,\bar Y_t)$ together with a one-dimensional process $r_t$ satisfying

\[
|\bar X_t-\bar Y_t|\le r_t
\]

and

\[
dr_t=
\bigl(\bar b(r_t)+2\|\gamma\|_\infty\,\mathbb P(r_t>0)\bigr)dt
+2\mathbf 1_{\{r_t>0\}}\,dW_t.
\]

The diffusion coefficient vanishes at zero: the comparison process has a **sticky boundary** rather than simply reflecting or instantly leaving zero. Under B1--B2, Theorem 1 constructs an increasing concave cost $f$ and constants $\tilde c>0$, $M_1<\infty$ such that

\[
\mathcal W_f(\bar\mu_t,\bar\nu_t)
 \le e^{-\tilde c t}\mathcal W_f(\bar\mu_0,\bar\nu_0),
\qquad
\mathcal W_1(\bar\mu_t,\bar\nu_t)
 \le M_1e^{-\tilde c t}\mathcal W_1(\bar\mu_0,\bar\nu_0).
\]

Theorem 7 supplies the corresponding exponential decay for the sticky one-dimensional comparison equation.

## Mechanism

Away from zero, the approximating coupling is reflection-like and creates radial noise that pulls two copies together; at zero it becomes synchronous so equality can persist. Taking a weak limit produces the sticky distance dynamics above. The nonlinear term $\mathbb P(r_t>0)$ records the fraction of coupled pairs that have not stuck together, so the comparison is not an ordinary scalar reflection-coupling calculation.

The central reduction is therefore from a nonlinear $d$-dimensional McKean--Vlasov coupling to a one-dimensional nonlinear sticky SDE. A carefully chosen concave $f$ turns its generator estimate into

\[
\frac d{dt}\mathbb E f(r_t)\le-\tilde c\,\mathbb E f(r_t),
\]

and domination of $|\bar X_t-\bar Y_t|$ transfers this decay back to Wasserstein distance.

This differs from synchronous weighted-$W_1$ contraction, where one directly dissipates a deterministic weighted distance, and from ordinary reflection coupling, where the distance diffusion is nondegenerate until a coupling time. The sticky state is itself part of the effective dynamics.

## Representative IPS use

The same paper applies the construction to the $N$-particle mean-field approximation

\[
dX_t^{i,N}=\frac1N\sum_j b(X_t^{i,N}-X_t^{j,N})dt+dB_t^i.
\]

Theorem 8 couples the particles componentwise with independent nonlinear McKean--Vlasov copies and obtains a uniform-in-time error of order $N^{-1/2}$ in the paper's transportation distances, in addition to exponential decay of the initial mismatch. Thus the sticky comparison simultaneously controls long-time nonlinear relaxation and propagation of chaos for a genuinely interacting particle system.

## Limitations

The theorem requires quantitative dissipativity at large separation and a small-enough bounded nonlinear perturbation; the method does not cover arbitrary strongly interacting or phase-coexisting McKean--Vlasov systems. The centering/moment assumptions in the stated results are also substantive. Its conclusions are Wasserstein contraction and propagation of chaos, not total-variation coalescence of the full particle configurations. Finally, the one-dimensional comparison equation is nonlinear through its own law, so verifying its zero-sticky phase and obtaining an explicit rate require additional analysis rather than a generic coupling inequality.

## Sources

- Durmus, Eberle, Guillin and Schuh, *Sticky nonlinear SDEs and convergence of McKean--Vlasov equations without confinement*, Theorems 1--2, 7--8. DOI: https://doi.org/10.1007/s40072-023-00315-8.
