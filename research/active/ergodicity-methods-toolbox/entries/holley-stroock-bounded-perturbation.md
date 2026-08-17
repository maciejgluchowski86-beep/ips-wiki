---
method_id: holley-stroock-bounded-perturbation
title: Holley-Stroock bounded-perturbation transfer
category: functional-inequality
targets:
  - spectral-gap
  - log-sobolev
  - convergence
model_scope: Gibbs measures and reversible spin/diffusion dynamics obtained as bounded changes of density from a reference model with known coercivity
source_status: primary-checked
primary_source: Georg Menz and Andre Schlichting, Poincare and logarithmic Sobolev inequalities by decomposition of the energy landscape, Annals of Probability 42 (2014), 1809-1884.
primary_pinpoint: Theorem 3.2, Holley-Stroock perturbation principle; Definition 3.3 and Lemma 3.4 for an epsilon-uniform localized perturbation transfer
primary_url: https://doi.org/10.1214/14-AOP908
application_source: Claudio Landim, Gustavo Panizo, and Horng-Tzer Yau, Spectral gap and logarithmic Sobolev inequality for unbounded conservative spin systems, Annales de l'Institut Henri Poincare Probabilites et Statistiques 38 (2002), 739-777.
application_pinpoint: Section 4 around equation (4.2), where bounded perturbation of the Gaussian potential supplies the one-site LSI input; Theorems 2.1-2.2 for the resulting conservative spin estimates
application_url: https://doi.org/10.1016/S0246-0203(02)01108-1
wiki_candidate: yes
---

# Holley-Stroock bounded-perturbation transfer

## Criterion

Let a reference probability measure \(\mu\) satisfy a Poincare inequality or logarithmic Sobolev inequality with coercive constant \(\rho>0\), and let

\[
\widetilde\mu(dx)=Z^{-1}e^{-W(x)}\mu(dx)
\]

with \(W\) bounded. The Holley--Stroock perturbation principle transfers the same functional inequality to \(\widetilde\mu\), with loss controlled only by the oscillation
\(\operatorname{osc}W=\sup W-\inf W\). In the convention where larger \(\rho\) means stronger coercivity,

\[
\widetilde\rho\ge e^{-\operatorname{osc}W}\rho;
\]

at inverse temperature \(\beta\), the loss becomes \(e^{-\beta\operatorname{osc}W}\). Equivalently, inverse Poincare/LSI constants worsen by at most \(e^{\operatorname{osc}W}\). Menz--Schlichting state this as Theorem 3.2 and use a temperature-scaled version in Definition 3.3 and Lemma 3.4.

## Mechanism

A bounded change of Hamiltonian makes the two probability densities uniformly comparable:

\[
e^{-\operatorname{osc}W}
\lesssim
\frac{d\widetilde\mu}{d\mu}
\lesssim
e^{\operatorname{osc}W},
\]

up to normalization. Variance and entropy under the perturbed measure can therefore be bounded by their reference counterparts, while the same comparison transfers the Dirichlet energy. Combining the two density-ratio comparisons gives the exponential oscillation loss.

The method is valuable because the reference model can be chosen for analytic convenience: a uniformly convex Gaussian-like model, a product measure, or another system whose spectral gap/LSI is already known. One then transfers coercivity without rebuilding the semigroup analysis for the perturbed Hamiltonian.

This is a **stability** argument, not a spatial-mixing proof. It does not show that arbitrary weak local interactions have a uniform gap unless their *total* density perturbation remains bounded. It is often most effective locally, after coarse graining, or when a perturbation is supported on a fixed number of sites.

## Representative IPS use

Holley and Stroock developed the principle in their study of stochastic Ising models. A continuous-spin conservative application is visible in Landim--Panizo--Yau: their single-site potential has the form

\[
V(x)=\frac{x^2}{2}+F(x)
\]

with \(F\) bounded. In Section 4 they invoke bounded perturbation of the Gaussian measure to obtain the one-site logarithmic Sobolev input needed for their conservative Ginzburg--Landau analysis. The global diffusive-order estimates then require additional Lu--Yau martingale/equivalence-of-ensembles work; bounded perturbation supplies a robust local coercive ingredient rather than the whole conservative theorem.

Menz--Schlichting similarly exploit the principle after modifying a nonconvex Hamiltonian locally: if the modification differs from the original by only \(O(\varepsilon)\) at temperature \(\varepsilon\), the exponential perturbation loss stays order one.

## Limitations

The decisive quantity is the oscillation of the **full finite-volume Hamiltonian difference**. If
\(W_\Lambda=\sum_{x\in\Lambda}w_x\) with nonzero bounded local terms, then typically \(\operatorname{osc}W_\Lambda=O(|\Lambda|)\). The comparison then loses \(e^{O(|\Lambda|)}\), which is useless for a volume-uniform spectral gap or LSI. Thus "bounded local interaction" is not the same as a uniformly bounded perturbation of the entire Gibbs law.

The method also requires absolute continuity and bounded density ratios; hard constraints or perturbations that create/delete configurations fall outside it. Finally, Holley--Stroock transfers an existing coercive inequality but does not identify the optimal constant and can be very crude even when the perturbed system mixes rapidly.

## Sources

- Menz, Schlichting, *Poincare and logarithmic Sobolev inequalities by decomposition of the energy landscape*, Theorem 3.2 and Definition 3.3/Lemma 3.4, https://doi.org/10.1214/14-AOP908; preprint https://arxiv.org/abs/1202.1510.
- Holley, Stroock, *Logarithmic Sobolev inequalities and stochastic Ising models*, Journal of Statistical Physics 46 (1987), 1159--1194, original perturbation principle, https://doi.org/10.1007/BF01011161.
- Landim, Panizo, Yau, *Spectral gap and logarithmic Sobolev inequality for unbounded conservative spin systems*, Section 4 near (4.2), https://doi.org/10.1016/S0246-0203(02)01108-1.
