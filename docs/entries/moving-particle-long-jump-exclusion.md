---
title: Moving-particle and long-jump comparison for exclusion
status: literature
audit: current
tags:
  - ergodicity methods
  - conservative IPS
  - exclusion process
---

# Moving-particle and long-jump comparison for exclusion

## Criterion

For symmetric exclusion on a finite connected weighted graph \((G,c)\), write \(\nabla_{xy}f(\eta)=f(\eta^{xy})-f(\eta)\) for exchanging occupations at arbitrary vertices \(x,y\), not necessarily adjacent. Chen's moving-particle lemma, Theorem 1.1, states that for every Bernoulli density \(\alpha\),

\[
\frac12\nu_\alpha[(\nabla_{xy}f)^2]
\le
R_{\mathrm{eff}}(x,y)\,
\mathcal E_{\mathrm{EX}}(f),
\]

where \(R_{\mathrm{eff}}(x,y)\) is the electrical effective resistance of the underlying weighted graph and \(\mathcal E_{\mathrm{EX}}\) is the full nearest-neighbor exclusion Dirichlet form. Thus the energy cost of an arbitrary long particle exchange is controlled by a geometric resistance times the energy of legal local exchanges.

## Mechanism

Conservative systems often require comparing two distant boxes or replacing the occupation at one location by another. A direct long exchange is not a transition of nearest-neighbor exclusion, so it must be represented in the local Dirichlet form. The elementary approach chooses a path from \(x\) to \(y\), moves a particle along it, and applies Cauchy--Schwarz. This is a [canonical-path estimate](dirichlet-form-canonical-path-comparison.md) and can overcount edges badly.

The moving-particle lemma exploits the special algebra of exclusion/interchange. Chen's proof uses the octopus inequality of Caputo--Liggett--Richthammer and packages all possible routes through the graph into effective resistance. The resulting bound is intrinsic to the electrical network rather than to one chosen path. On irregular or fractal graphs this can be much sharper and remains meaningful without translation invariance.

Once a long exchange is controlled, one may insert it into a variational estimate: a two-block discrepancy, for example, can be bounded by transporting a particle from one block to another and paying only \(R_{\mathrm{eff}}\mathcal E\). This converts spatial replacement into a coercive estimate for the actual conservative generator.

## Representative IPS use

Chen's follow-up local-ergodicity paper studies symmetric and boundary-driven exclusion on increasing weighted graphs. Proposition 4.2 imports the moving-particle inequality, and Lemma 4.3 uses it in the two-block spectral estimate. Together with one-block estimates and resistance-volume assumptions, the argument proves local ergodic replacement results on strongly recurrent graphs, including fractal-type examples such as the Sierpinski gasket.

The lemma also reflects the spectral-gap structure of exclusion: the same octopus inequality underlies the theorem that the exclusion/interchange spectral gap is governed by the underlying random walk. For toolbox purposes the distinctive reusable move is narrower: **replace an illegal long exchange by the whole local exclusion energy with a resistance cost**.

## Limitations

This is model-specific comparison machinery, not a generic canonical-path theorem. It uses the exchange structure and symmetry of exclusion; arbitrary Kawasaki rates, nonreversible conservative dynamics, or several particle species may not satisfy the same inequality. Effective resistance can itself grow rapidly with distance, so the bound is useful only when the geometry and scaling make that growth affordable. The Bernoulli formulation must also be adapted when working on a fixed-particle canonical sector, although the exclusion exchange gradients are compatible with that decomposition.

The moving-particle estimate alone does not prove global mixing or an infinite-volume spectral gap. Conservative IPS typically have diffusive slow modes and no positive infinite-volume gap; the lemma instead feeds finite-volume spectral estimates, hydrodynamic replacement lemmas, and local ergodicity arguments.

## Sources

- Chen, *The moving particle lemma for the exclusion process on a weighted graph*, Theorem 1.1 and Section 1.1, https://doi.org/10.1214/17-ECP82; preprint https://arxiv.org/abs/1606.01577.
- Chen, *Local ergodicity in the exclusion process on an infinite weighted graph*, Proposition 4.2, Lemma 4.3, and Sections 3--5, https://arxiv.org/abs/1705.10290.
