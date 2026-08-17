---
method_id: hierarchical-renormalisation-spectral-gap-recursion
title: Renormalised Brascamp--Lieb recursion for hierarchical spin spectral gaps
category: functional-inequality
targets:
  - spectral-gap
model_scope: Finite-volume hierarchical continuous-spin models with a multiscale block-spin decomposition and controlled renormalised measures
source_status: primary-checked
primary_source: Roland Bauerschmidt and Thierry Bodineau, Spectral Gap Critical Exponent for Glauber Dynamics of Hierarchical Spin Models, Communications in Mathematical Physics 373 (2020), 1167--1206.
primary_pinpoint: Section 2, especially Theorem 2.1 and Corollaries 2.2--2.3; applications in Theorems 1.1--1.2
primary_url: https://doi.org/10.1007/s00220-019-03553-x
application_source: Roland Bauerschmidt and Thierry Bodineau, Spectral Gap Critical Exponent for Glauber Dynamics of Hierarchical Spin Models, Communications in Mathematical Physics 373 (2020), 1167--1206.
application_pinpoint: Theorems 1.1--1.2 and Sections 3--4
application_url: https://arxiv.org/abs/1809.02075
wiki_candidate: yes
---

# Renormalised Brascamp--Lieb recursion for hierarchical spin spectral gaps

## Criterion

Suppose a spin measure at scale \(j\) decomposes into a coarse block-spin field with renormalised law \(\mu_+\) and a conditional fluctuation field. Bauerschmidt--Bodineau assume their scale-\(j\) hypotheses (A1)--(A3): most importantly, the conditional fluctuation measure has a Brascamp--Lieb bound with a controlled defect \(arepsilon<1\), together with compatibility of the hierarchical covariance and coarse projection. If the next-scale law satisfies

\[
\operatorname{Var}_{\mu_+}(F)
 \le \mathbb E_{\mu_+}(\nabla F,D_+\nabla F),
\]

then Theorem 2.1 proves a Brascamp--Lieb inequality for the current law with matrix

\[
D\le \frac{C}{1-\varepsilon}
   +\frac{D_+}{(1-\varepsilon)^2}.
\]

At the last scale the second term disappears. Corollary 2.2 iterates this one-step inequality through all renormalisation scales, producing an explicit matrix \(D_0\) for the original measure. Corollary 2.3 then gives the spectral-gap bound

\[
\operatorname{Var}_{\mu_0}(F)
\le \lambda^{-1}\mathbb E_{\mu_0}|\nabla F|^2,
\qquad
\lambda^{-1}\le \|D_0\|,
\]

where \(\|D_0\|\) is the largest eigenvalue of the accumulated Brascamp--Lieb matrix.

## Mechanism

The proof interface is the **renormalised measure itself**. Condition on the coarse block spin and decompose total variance into conditional fluctuations plus variance of the conditional expectation. Uniform convexity of the fluctuation field controls the first term. The second term is differentiated with respect to the coarse variable and estimated by the Brascamp--Lieb inequality already known one scale higher. The loss at one scale is therefore explicit and multiplicative/additive in \(C_j\) and \((1-\varepsilon_j)^{-1}\).

This is useful near criticality, where no volume-uniform gap should be expected. Rather than seek contraction at the microscopic scale, one follows the deterioration of coercivity along the renormalisation flow. The critical spectral-gap exponent is obtained by summing the scale-by-scale losses attached to the sequence of effective potentials.

The architecture is distinct from ordinary block bisection. Bisection proves a recursive variance estimate by geometrically splitting a fixed measure into overlapping regions. Here each recursion step changes the measure: microscopic fluctuations are integrated out, producing a new effective interaction, and the spectral-gap estimate is propagated along that renormalisation-group trajectory.

## Representative IPS use

Bauerschmidt--Bodineau apply the recursion to Glauber-type dynamics for hierarchical versions of strongly correlated spin systems. Theorem 1.1 treats the four-dimensional \(n\)-component \(|\varphi|^4\) model at criticality and from the high-temperature side; Theorem 1.2 treats hierarchical two-dimensional Sine--Gordon and Discrete Gaussian models in the rough phase. Sections 3--4 verify the scale hypotheses for the corresponding renormalised potentials. The resulting inverse gaps have the free-field polynomial scale, with the stated logarithmic correction in the critical \(|\varphi|^4\) case.

Thus the method can extract the *scaling* of relaxation at a critical point, rather than only prove positivity of a fixed infinite-volume gap.

## Limitations

The one-step theorem requires a multiscale decomposition for which the conditional fluctuation field is quantitatively convex after conditioning and for which derivatives through the coarse-graining map can be controlled. Those properties are especially natural for hierarchical covariances; transferring the method to a nonhierarchical lattice model requires a suitable renormalisation construction and uniform control of the effective potentials.

The conclusion is a finite-volume Poincare/spectral-gap estimate. It does not by itself prove uniqueness of an infinite-volume Gibbs state, log-Sobolev inequalities, or worst-case total-variation mixing. Near criticality the gap deliberately vanishes with system size. The model-specific work lies in verifying (A1)--(A3) along the entire renormalisation trajectory; without that control, the abstract recursion is only a formal reduction.

## Sources

- Bauerschmidt, Bodineau, *Spectral Gap Critical Exponent for Glauber Dynamics of Hierarchical Spin Models*, Section 2, Theorem 2.1 and Corollaries 2.2--2.3, https://doi.org/10.1007/s00220-019-03553-x.
- The same paper, Theorems 1.1--1.2 and Sections 3--4 for the hierarchical \(|\varphi|^4\), Sine--Gordon, and Discrete Gaussian applications, https://arxiv.org/abs/1809.02075.
