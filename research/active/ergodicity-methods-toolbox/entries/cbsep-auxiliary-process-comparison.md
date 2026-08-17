---
method_id: cbsep-auxiliary-process-comparison
title: CBSEP and generalized-CBSEP auxiliary-process comparison
category: kcsm-model-specific
targets:
  - spectral-gap
  - log-sobolev
  - mixing
model_scope: Finite-volume KCM whose mobile vacancies or droplets can be represented by coalescing-and-branching exclusion variables on a coarse graph
source_status: primary-checked
primary_source: Ivailo Hartarsky, Fabio Martinelli, Cristina Toninelli, Coalescing and branching simple symmetric exclusion process, Annals of Applied Probability 32 (2022), 2841-2859.
primary_pinpoint: Equation (3), Corollaries 3.1-3.2, Theorem 2, and Section 5
primary_url: https://doi.org/10.1214/21-AAP1750
application_source: Ivailo Hartarsky, Fabio Martinelli, Cristina Toninelli, Sharp threshold for the FA-2f kinetically constrained model, Probability Theory and Related Fields 185 (2023), 993-1037.
application_pinpoint: Proposition 5.2 and Section 5.3, especially equations (5.9)-(5.11)
application_url: https://doi.org/10.1007/s00440-022-01169-2
wiki_candidate: yes
---

# CBSEP and generalized-CBSEP auxiliary-process comparison

## Criterion

The coalescing and branching simple symmetric exclusion process (CBSEP) is an auxiliary conservative-looking particle system designed to retain the **mobility of facilitating defects** while being easier to analyze than the KCM from which those defects arise. On an edge with at least one particle, an update resamples the two endpoint occupations according to Bernoulli product equilibrium conditioned on being nonempty. Particles consequently move, coalesce, and branch.

For FA-1f on a finite graph, Hartarsky--Martinelli--Toninelli compare the two Dirichlet forms explicitly. Their equation (3) gives, for an absolute constant \(c\),
\[
c^{-1}\mathcal D_{\rm FA}(f)
\le \mathcal D_{\rm CBSEP}(f)
\le c\,d_{\max}p^{-1}\mathcal D_{\rm FA}(f),
\tag{CB}
\]
where \(p\) is the vacancy/particle density. Thus any coercive estimate proved for CBSEP can be transferred to FA-1f with an explicit loss. Corollaries 3.1--3.2 combine `(CB)` with the CBSEP logarithmic-Sobolev and relaxation bounds to obtain finite-volume FA-1f mixing estimates.

The generalized process (g-CBSEP) replaces the binary state at each coarse vertex by a finite state space \(S=S_0\sqcup S_1\); only whether a block lies in \(S_1\) records the presence of a mobile droplet. The projection onto \(1_{S_1}\) is exactly ordinary CBSEP. Theorem 2 proves
\[
T_{\rm mix}^{\rm CBSEP}
\le T_{\rm mix}^{\rm gCBSEP}
\le C\left(T_{\rm mix}^{\rm CBSEP}
+\frac{T_{\rm cov}^{\rm RW}}{d_{\min}}\right).
\tag{GCB}
\]
This makes g-CBSEP a controlled auxiliary dynamics for a coarse KCM state carrying internal block information.

## Mechanism

The key simplification is to keep only the **locations of mobile defects** as dynamically relevant. CBSEP is attractive and contains a random-walk component, so its relaxation can be estimated using meeting, hitting, cover-time, and logarithmic-Sobolev information for random walks. Coalescence removes redundant defects and branching preserves the correct equilibrium density.

For a KCM, the proof then has three interfaces. First choose a defect variable: a vacancy for FA-1f or a rare super-good mobile droplet for a cooperative model. Second prove that the induced coarse edge refresh is no faster than, or Dirichlet-comparable with, legal microscopic KCM moves. Third insert the auxiliary CBSEP/g-CBSEP Poincare or mixing estimate. The difficult KCM geometry is thereby isolated in the comparison step, while transport of the mobile object is delegated to the tractable auxiliary particle system.

This differs from generic canonical-path comparison because the comparison target is itself a **purpose-built interacting process** with branching/coalescence structure and independently proved relaxation theory.

## Representative IPS use

For FA-1f with vacancy density of order \(1/|V|\), Corollary 3.2 uses `(CB)` and the CBSEP estimates of Corollary 3.1 to bound total-variation and \(L^2\) mixing on discrete tori; the paper also obtains logarithmic-Sobolev information stronger than earlier mixing-only estimates.

The generalized process is load-bearing in the sharp FA-2f argument. In the 2023 paper, each coarse box has a state space \(S\), while \(S_1\) is the event that it contains a super-good mobile droplet. Proposition 5.2 proves
\[
\operatorname{Var}(f)
\le O\!\left(\pi(S_1)^{-1}
\max\{1,\log \pi(S_1)^{-1}\}\right)
\mathcal D_{\rm gCBSEP}(f)
\]
when the expected number of super-good boxes diverges. Section 5.3 identifies this g-CBSEP Dirichlet form with allowed two-box droplet moves and then implements those moves by FA-2f legal paths. The auxiliary process therefore supplies the mesoscopic relaxation estimate rather than merely motivating the droplet picture.

## Limitations

The construction is finite-volume and requires a useful coarse defect whose equilibrium indicator behaves approximately as a sparse Bernoulli field. The comparison back to the KCM can lose powers of the defect density, and for cooperative models the main work is proving that a g-CBSEP edge refresh can be simulated by legal microscopic moves at acceptable cost.

A CBSEP theorem alone does not prove infinite-volume uniqueness or ergodicity of the original KCM. The stated applications are finite-volume relaxation/mixing inputs. Nor is g-CBSEP simply a dual process: it is an auxiliary reversible dynamics introduced for **coercive comparison**, and its projection to ordinary CBSEP is used to exploit simpler random-walk structure.

## Sources

- Hartarsky, Martinelli, Toninelli, *Coalescing and branching simple symmetric exclusion process*, equation (3), Corollaries 3.1--3.2, Theorem 2 and Section 5, https://doi.org/10.1214/21-AAP1750.
- Hartarsky, Martinelli, Toninelli, *Sharp threshold for the FA-2f kinetically constrained model*, Proposition 5.2 and Section 5.3, https://doi.org/10.1007/s00440-022-01169-2.
