---
method_id: componentwise-reflection-uniform-mean-field
title: Componentwise reflection coupling with particle-number-uniform contraction
category: coupling
targets:
  - convergence
model_scope: Weakly interacting mean-field diffusions with nonconvex confinement and estimates uniform in particle number
source_status: primary-checked
primary_source: Wei Liu, Liming Wu and Chaoen Zhang, "Long-time behaviors of mean-field interacting particle systems related to McKean-Vlasov equations," Communications in Mathematical Physics 387 (2021)
primary_pinpoint: Theorem 2.5 in Section 2.3; Section 3.1 and equation (3.3); Theorem 2.9 in Section 2.4
primary_url: https://doi.org/10.1007/s00220-021-04198-5
application_source: Wei Liu, Liming Wu and Chaoen Zhang, same paper
application_pinpoint: Theorem 2.5 for uniform-in-N exponential Wasserstein contraction; Theorem 2.9 for propagation of chaos; Examples 2.13--2.14
application_url: https://arxiv.org/abs/2007.09462
wiki_candidate: yes
---

# Componentwise reflection coupling with particle-number-uniform contraction

## Criterion

Consider the $N$-particle mean-field diffusion

\[
dX_t^{i,N}=\sqrt2\,dB_t^i-\nabla V(X_t^{i,N})dt
-\frac1{N-1}\sum_{j\ne i}\nabla_xW(X_t^{i,N},X_t^{j,N})dt.
\]

Liu--Wu--Zhang introduce a one-particle dissipativity profile $b_0(r)$ and a reference function $h$ solving the one-dimensional Poisson equation

\[
4h''(r)+b_0(r)h'(r)=-r,
\qquad h(0)=0.
\]

Their weak-interaction condition (H) requires, in particular,

\[
\|\nabla^2_{xy}W\|_\infty\,\|h'\|_\infty<1.
\]

Under this condition and the additional linear upper bound $b_0(r)\le Mr$, Theorem 2.5 gives constants $A_\varepsilon<\infty$ and $K_\varepsilon>0$, independent of $N$, such that for the $N$-particle semigroup

\[
W_{1,d_{\ell^1}}
\bigl(P_t^{(N)}(x,\cdot),P_t^{(N)}(y,\cdot)\bigr)
\le A_\varepsilon e^{-K_\varepsilon t}d_{\ell^1}(x,y),
\]

where $d_{\ell^1}(x,y)=\sum_i|x_i-y_i|$. Thus the many-particle contraction rate does not deteriorate as the number of interacting coordinates grows.

## Mechanism

Section 3.1 couples two $N$-particle systems **component by component**. For each coordinate difference $Z_t^i=X_t^{i,N}-Y_t^{i,N}$, the Brownian increment in the second copy is approximately reflected in the direction $Z_t^i/|Z_t^i|$ when the copies are separated and made synchronous near zero. The reflection matrices are therefore different for different particles rather than one global reflection in $\mathbb R^{Nd}$.

Applying Itô's formula to $h(|Z_t^i|)$ yields a dissipative term coming from the single-particle reference equation and interaction-error terms bounded by $\|\nabla^2_{xy}W\|_\infty$. Summing over $i$ closes because the mean-field factor $1/(N-1)$ cancels the number of neighboring coordinates. The resulting cost is equivalent to the $\ell^1$ transportation distance, and the contraction constants remain uniform in $N$.

The particle-number uniformity is the load-bearing feature. Wang's infinite-dimensional reflection method addresses a singular Hilbert-space reflection operator by regularization; here each reflected noise is finite-dimensional, while the difficulty is preventing the accumulation of $N$ weak interaction errors. The method also differs from sticky coupling: the distance processes are controlled through a Poisson-designed cost and approximate reflection, not through a nonlinear one-dimensional process with a sticky atom at zero.

## Representative IPS use

Theorem 2.5 gives exponential Wasserstein convergence of the full weakly interacting particle system under confinement potentials that may have several wells, provided the cross-interaction Hessian is sufficiently small. The paper gives explicit double-well examples rather than assuming global convexity.

The same coupling estimates feed into Theorem 2.9, which proves propagation-of-chaos bounds uniform over long times. Hence an estimate designed for relaxation of each finite $N$ system also remains stable as $N\to\infty$, which is essential for transferring long-time information to the McKean--Vlasov limit.

## Limitations

The cross interaction must be quantitatively weak relative to the single-particle dissipativity, excluding regimes with strong collective phase transitions. The theorem uses additive nondegenerate Brownian noise and regularity/bounded-Hessian assumptions on the interaction. Uniformity in $N$ does not mean uniform total-variation coalescence; the conclusion is Wasserstein contraction in a cost equivalent to $\ell^1$. The method is tailored to mean-field interactions, where averaging makes the sum of componentwise errors close uniformly; the same calculation need not work for arbitrary strongly coupled spatial systems.

## Sources

- Liu, Wu and Zhang, *Long-time behaviors of mean-field interacting particle systems related to McKean-Vlasov equations*, Theorem 2.5, Section 3.1, Theorem 2.9. DOI: https://doi.org/10.1007/s00220-021-04198-5; inspected full version: https://arxiv.org/abs/2007.09462.
