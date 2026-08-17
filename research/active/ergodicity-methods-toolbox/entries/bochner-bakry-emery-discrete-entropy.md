---
method_id: bochner-bakry-emery-discrete-entropy
title: Discrete Bochner--Bakry--Emery entropy method
category: functional-inequality
targets:
  - log-sobolev
  - convergence
  - mixing
model_scope: Reversible jump processes, including zero-range and Bernoulli--Laplace particle systems, where transitions admit a tractable move calculus
source_status: primary-checked
primary_source: Pietro Caputo, Paolo Dai Pra, Gustavo Posta, Convex entropy decay via the Bochner--Bakry--Emery approach, Annales de l'Institut Henri Poincare Probabilites et Statistiques 45 (2009), 734-753.
primary_pinpoint: Lemma 2.1 and equation (2.3); Proposition 2.5 for the Bochner move identity; Theorem 4.2 for inhomogeneous zero-range; Theorem 5.1 for Bernoulli--Laplace
primary_url: https://doi.org/10.1214/08-AIHP183
application_source: Pietro Caputo, Paolo Dai Pra, Gustavo Posta, Convex entropy decay via the Bochner--Bakry--Emery approach, Annales de l'Institut Henri Poincare Probabilites et Statistiques 45 (2009), 734-753.
application_pinpoint: Theorem 4.2, pages 746-747 in the published pagination; Theorem 5.1, page 749
application_url: https://arxiv.org/abs/0712.2578
wiki_candidate: yes
---

# Discrete Bochner--Bakry--Emery entropy method

## Criterion

For a reversible irreducible Markov jump process with invariant law \(\pi\), generator \(L\), and Dirichlet form \(\mathcal E(f,g)=-\pi[fLg]\), Caputo--Dai Pra--Posta use a second-derivative entropy criterion. Their Lemma 2.1 states that if, for every positive \(f\),

\[
\kappa\,\mathcal E(f,\log f)
\le
\pi[Lf\,L\log f]+\pi\!\left[\frac{(Lf)^2}{f}\right],
\tag{B}
\]

then the entropy dissipation \(\mathcal E(P_t f,\log P_t f)\) decays at least as \(e^{-\kappa t}\), and the modified logarithmic Sobolev inequality holds with constant \(\kappa\). Proposition 2.5 supplies the discrete Bochner mechanism: represent the generator by elementary moves and construct a measure on pairs of commuting moves satisfying symmetry/invariance identities; the second entropy derivative is then reorganized into positive diagonal terms plus interaction errors. A lower bound on the resulting quadratic expression proves `(B)`.

## Mechanism

The method is the jump-process analogue of using a Bochner identity or a \(\Gamma_2\)-curvature bound for diffusions, but the useful criterion is not merely the formal slogan \(\Gamma_2\ge\rho\Gamma\). For jumps, the chain rule fails. One instead differentiates relative entropy twice along the semigroup and rewrites the resulting terms using the algebra of allowed moves. Commuting pairs supply the analogue of a Hessian-square term; noncommuting or inhomogeneous moves generate error terms that must be absorbed by the positive part.

This produces coercivity directly at the level of entropy dissipation. Once `(B)` is verified, no separate martingale recursion or spatial-mixing theorem is needed: integration gives exponential entropy convergence, hence mLSI and, on finite state spaces, quantitative total-variation control through entropy inequalities.

## Representative IPS use

For an inhomogeneous zero-range process on a complete graph with conserved particle number, let \(c_x(n)\) be the rate at which a particle leaves site \(x\) containing \(n\) particles. Theorem 4.2 assumes that for constants \(0\le\delta<c\), uniformly in sites and occupations,

\[
c\le c_x(n+1)-c_x(n)\le c+\delta.
\]

The Bochner estimate gives `(B)` with

\[
\kappa=c-\delta,
\]

uniformly in the number of sites and particles. Thus the canonical zero-range dynamics has a volume- and mass-uniform mLSI. Theorem 5.1 gives the analogous conclusion for an inhomogeneous Bernoulli--Laplace exclusion model when its site rates satisfy \(c\le\lambda_x\le c+\delta\).

These are useful examples because the move identity handles inhomogeneity that is awkward for the Lu--Yau conditional-martingale architecture.

## Limitations

The hard part is model algebra: one needs a transition representation for which the paired-move identity has a controllable positive remainder. The method can fail even when an mLSI might still be true. Section 4.2 of the primary source gives zero-range examples where entropy is not convex along the semigroup, so the second-derivative criterion itself cannot hold with positive \(\kappa\), although weaker entropy coercivity may remain possible.

The criterion is naturally reversible and does not by itself address nonreversible hypocoercivity. For local lattice dynamics, constants obtained from a complete-graph or mean-field move calculus do not automatically transfer to nearest-neighbor dynamics; an additional comparison argument may be required. This page is therefore a method for *proving* mLSI by discrete curvature/Bochner coercivity, distinct from the toolbox page that treats mLSI as an already available functional inequality.

## Sources

- Caputo, Dai Pra, Posta, *Convex entropy decay via the Bochner--Bakry--Emery approach*, Lemma 2.1, Proposition 2.5, Theorems 4.2 and 5.1, https://doi.org/10.1214/08-AIHP183.
- Open primary preprint with the same theorem numbering: https://arxiv.org/abs/0712.2578.
