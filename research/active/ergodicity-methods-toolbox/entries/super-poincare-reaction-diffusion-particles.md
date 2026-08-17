---
method_id: super-poincare-reaction-diffusion-particles
title: Super-Poincare decomposition for reaction-diffusion particle systems
category: functional-inequality
targets:
  - super-poincare
  - log-sobolev
model_scope: Finite-but-unbounded particle systems on a Polish space with reversible birth/death of particle number and interacting diffusion within fixed-particle sectors
source_status: primary-checked
primary_source: Michael Rockner and Feng-Yu Wang, Functional Inequalities for Particle Systems on Polish Spaces, Potential Analysis 24 (2006), 223-243.
primary_pinpoint: Corollary 4.4 for the super-Poincare iff decomposition; Theorem 4.2 and Example 5.2 for the logarithmic-Sobolev interacting-diffusion specialization
primary_url: https://doi.org/10.1007/s11118-005-0913-6
application_source: Michael Rockner and Feng-Yu Wang, Functional Inequalities for Particle Systems on Polish Spaces, Potential Analysis 24 (2006), 223-243.
application_pinpoint: Example 5.2, pages 241-242 of the journal pagination / pages 19-20 of the arXiv version
application_url: https://arxiv.org/abs/math/0512100
wiki_candidate: yes
---

# Super-Poincare decomposition for reaction-diffusion particle systems

## Criterion

Röckner--Wang consider a particle system whose state is a finite configuration on a Polish space \(E\), with an unbounded number of particles. The number of particles evolves according to a reversible \(Q\)-process on \(\mathbb Z_+\), while conditional on having \(n\) particles their positions evolve through a symmetric diffusion Dirichlet form \(\mathcal E^{(n)}_0\). The full reaction-diffusion form is
\[
\mathcal E_{\Gamma_0}=\mathcal E^R_{\Gamma_0}+\mathcal E^0_{\Gamma_0},
\]
combining birth/death and within-sector motion.

A super-Poincare inequality has the form
\[
\pi(F^2)\le r\,\mathcal E_{\Gamma_0}(F,F)
      +\beta(r)\,\pi(|F|)^2,\qquad r>0.
\tag{SP}
\]
Corollary 4.4 gives an exact decomposition criterion. Under the hypotheses of Theorem 4.2 and the additional assumption that the diffusion sector has positive spectral gap, `(SP)` holds for the full particle system **if and only if** there are super-Poincare functions \(\beta_0,\beta_Q\) such that the one-particle diffusion form and the particle-number form satisfy
\[
\mu^{(1)}(f^2)\le r\mathcal E^{(1)}_0(f,f)
 +\beta_0(r)\mu^{(1)}(|f|)^2,
\]
\[
\varrho(a^2)\le r\mathcal E_Q(a,a)
 +\beta_Q(r)\varrho(|a|)^2.
\]
Thus strong smoothing of the full interacting particle dynamics can be proved by separately controlling **where the particles are** and **how many particles there are**.

## Mechanism

The invariant law is a mixture over particle number,
\[
\pi=\sum_{n\ge0}\varrho_n\mu^{(n)}.
\]
The proof decomposes the functional inequality along this mixture. The reaction form controls fluctuations between different particle-number sectors through the one-dimensional \(Q\)-process; the diffusion form controls fluctuations inside a fixed sector. Tensorisation/comparison estimates propagate one-particle diffusion coercivity to \(n\)-particle sectors, while the tail of \(\varrho_n\) controls the cost of summing those sector estimates.

The useful point is that super-Poincare is stronger than ordinary Poincare and is sensitive to both pieces. In fact, Theorem 3.1 shows that the pure reaction form can have a spectral gap while failing every super-Poincare inequality when the one-particle space has infinite support. Adding genuine diffusion restores the missing small-scale smoothing, and Corollary 4.4 identifies exactly the two component inequalities that must be supplied.

This is a different interface from weak Poincare or Nash interpolation. Those methods tolerate weak coercivity and derive slow decay. Here the aim is a **strong smoothing inequality**, assembled from reaction and spatial diffusion components.

## Representative IPS use

Example 5.2 takes the spatial motion to be an interacting diffusion associated with a finite-range Gibbs potential on a compact manifold. The fixed-sector measures are the finite-coordinate projections of the Gibbs state. Assuming the Gibbs diffusion form satisfies a logarithmic-Sobolev inequality and that the particle-number \(Q\)-process satisfies its corresponding logarithmic-Sobolev criterion, Theorem 4.2 yields a logarithmic-Sobolev inequality for the full reaction-diffusion particle system.

This example is a stronger member of the same decomposition family as Corollary 4.4: reaction and diffusion are verified separately and then recombined into a global functional inequality. It gives a concrete interacting-particle use rather than attaching generic super-Poincare theory to an unrelated chain.

## Limitations

The source treats reversible Dirichlet forms and a finite, although unbounded, number of particles; it is not an infinite-density lattice IPS theorem. The component criteria can be difficult: the particle-number chain needs its own tail/coercivity estimate and the spatial diffusion needs a uniform inequality compatible with the sector decomposition.

Super-Poincare should not be silently identified with ordinary Poincare, weak Poincare, Nash, or log-Sobolev. Corollary 4.4 concerns `(SP)` itself; Example 5.2 uses the stronger log-Sobolev specialization through Theorem 4.2. The entry therefore records a decomposition architecture, not a universal implication from one named inequality to all the others.

This entry is a substitution for the Assignment-005 artificial-Nummelin target. A targeted search again found generic Nummelin splitting theory but no clean interacting-process application in which the manufactured atom and renewal decomposition themselves drive the ergodic conclusion; creating such a page would have violated the anti-padding rule.

## Sources

- Röckner, Wang, *Functional Inequalities for Particle Systems on Polish Spaces*, Corollary 4.4; Theorem 4.2 and Example 5.2 for the interacting-diffusion/log-Sobolev specialization, https://doi.org/10.1007/s11118-005-0913-6.
- Author preprint: https://arxiv.org/abs/math/0512100.
