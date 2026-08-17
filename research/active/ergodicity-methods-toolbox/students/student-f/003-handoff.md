# Student F Assignment 003 handoff

Date: 2026-08-17

Assignment 003 is complete. Six entries were committed individually. Five are the requested targets; the nonreversible sector/hypocoercive slot was replaced under the assignment's explicit substitution rule because I did not locate a clean primary IPS/spin application in which a sector/symmetric-part/hypocoercive estimate itself proves quantitative relaxation or a spectral gap. The sector-condition IPS sources found during reconnaissance were primarily fluctuation/CLT or hydrodynamic tools, so I did not force a weak entry.

## Entries and commits

1. `entries/bochner-bakry-emery-discrete-entropy.md`
   - commit `dc88f1452ba27596ab733c02e290c0b56b28e7c3`
   - discrete Bochner/Bakry--Emery second-entropy-derivative criterion; zero-range and Bernoulli--Laplace mLSI applications.

2. `entries/two-scale-coarse-graining-conservative-lsi.md`
   - commit `762ef88d0d8e97075d83c192952da770672fecc7`
   - conditional/marginal entropy decomposition, coarse-grained convexification, and optimal Kawasaki LSI scaling.

3. `entries/aldous-interchange-exclusion-gap.md`
   - commit `5cd7c984468fdbde33f935067f657b0e207457cd`
   - exact interchange/random-walk spectral-gap equality and exact symmetric-exclusion consequence.

4. `entries/liggett-nash-polynomial-relaxation.md`
   - commit `7a2f51e4c0a384fddb6f38ef52cd1f905701b6c7`
   - Nash/Liggett--Nash interpolation as a polynomial-relaxation mechanism when a positive gap is false.

5. `entries/kclg-renormalized-glauber-comparison.md`
   - commit `850bffb0f6f62be286b650efcb7b2225c28d3536`
   - **substitution for the nonreversible slot**: KCLG renormalization plus long-range constrained Glauber comparison; auxiliary AGL gap -> AKG/KA relaxation and polynomial equilibrium decay.

6. `entries/large-set-conductance-warm-start.md`
   - commit `3aa52a99cc844d006d8f0784022be285faf9b942`
   - weak conductance/large-set expansion plus Lovasz--Simonovits profile gives polynomial warm-start mixing for RFIM Glauber dynamics.

## Source qualifications

- Bochner entry: primary theorem chain is Caputo--Dai Pra--Posta, Lemma 2.1, Proposition 2.5, Theorems 4.2 and 5.1. The entry deliberately treats this as a *method for proving mLSI*, distinct from the existing generic LSI/mLSI page.
- Two-scale entry: Menz--Otto Proposition 2.1 and Theorem 2.6 are the recursive interfaces; Theorem 1.6 and Remark 1.7 give the canonical/Kawasaki conclusion. This is distinct from Lu--Yau filtration recursion.
- Aldous entry: Theorem 1.1 is exact equality for every finite connected weighted graph; Section 4.1.1 equation (4.1) is the exact exclusion equality for every nontrivial particle number.
- Nash entry: Inglis--Neklyudov--Zegarlinski prove polynomial semigroup decay first (Corollary 7.2) and derive their Liggett--Nash inequalities in Theorem 8.1. The entry explicitly says this, rather than reversing the historical proof order; it presents the general Nash-to-polynomial-decay architecture as the reusable method.
- KCLG substitution: inspected primary full text of Cancrini--Martinelli--Roberto--Toninelli, especially Theorems 4.1, 4.2, 5.5 and 5.6 and Sections 5--8. The method is the renormalized auxiliary-process bridge, not merely generic canonical paths.
- Conductance entry: this is deliberately **large-set conductance**, not a claim of a uniform Cheeger constant. El Alaoui--Eldan--Gheissari--Piana equations (3.17)--(3.18) and Lemma 3.5 yield warm-start polynomial mixing; tiny-set bottlenecks and cold starts remain outside the conclusion.

## Still-uncovered analytic families worth later consideration

- a genuinely relaxation-oriented nonreversible IPS sector/hypocoercive theorem, if a clean source is located;
- Foster--Lyapunov/Harris recurrence with an infinite-dimensional or IPS-like application;
- Wasserstein/weighted-gradient contraction methods distinct from path coupling;
- finite-volume-to-infinite-volume coercivity/exhaustion as a dedicated synthesis;
- comparison with unconstrained refresh dynamics for additional KCSM beyond the KA renormalized-Glauber mechanism;
- weak Poincare/super-Poincare inequalities beyond the Nash and RFIM large-set examples;
- spectral-profile/evolving-set bounds where the profile itself, rather than a single conductance inequality, is the main proof interface.

No `docs/` or `mkdocs.yml` files were edited. Mechanical validation is left to the principal/orchestrator's normal post-commit run.
