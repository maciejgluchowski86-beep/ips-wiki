---
method_id: refined-discrepancy-coupling-general-exclusion
title: Refined discrepancy coupling beyond basic exclusion coupling
category: coupling
targets:
  - uniqueness
model_scope: Conservative exclusion processes with configuration-dependent jump rates for which ordinary basic coupling is not attractive
source_status: primary-checked
primary_source: Thierry Gobron and Ellen Saada, "Couplings and attractiveness for general exclusion processes," Ensaios Matemáticos 38 (2023), 263--313
primary_pinpoint: Theorems 2.9, 2.13 and 2.15; Propositions 3.30 and 3.36; Section 4
primary_url: https://doi.org/10.21711/217504322023/em3810
application_source: same as primary source
application_pinpoint: Sections 4.2--4.4 and Theorem 2.15
application_url: https://arxiv.org/abs/2302.00971
wiki_candidate: yes
---

# Refined discrepancy coupling beyond basic exclusion coupling

## Criterion

For simple exclusion, the basic coupling attempts the same particle jump in both copies whenever possible. For general exclusion processes whose jump rates \(\Gamma_\eta(x,y)\) depend on the configuration, Gobron--Saada show that this coupling is generally too rigid: except for simple exclusion, basic coupling need not preserve order.

Their Theorem 2.9 gives necessary and sufficient rate inequalities for monotonicity. Theorem 2.13 then proves a stronger constructive statement: whenever the general exclusion process is monotone, there exists an increasing Markovian coupling on \(\Omega\times\Omega\) under which the number of discrepancies between the two configurations is nonincreasing. Proposition 3.30 gives the coupled generator explicitly. Crucially, a jump \(x_1\to y_1\) in one marginal may be paired with a **different** jump \(x_2\to y_2\) in the other; matching only identical transitions would fail.

For invariant-law classification, add the no-blocking and full-connectivity hypotheses of Definition 2.14. Proposition 3.36 constructs a further coupling for which opposite-sign discrepancies have a positive route to disappear. Theorem 2.15 then shows, for translation-invariant rates, that the extremal translation-invariant invariant measures form a stochastically ordered one-parameter family \(\{\mu_\rho:\rho\in R\}\). If a one-parameter family of product invariant measures is already known, these are exactly all extremal translation-invariant invariant measures. Thus there is a unique such extremal stationary law at each admissible density parameter.

## Mechanism

The method treats the **coupled transition rates themselves as variables to design**. Configuration dependence may create an excess jump rate in one copy at a departure or arrival site. Instead of leaving that excess jump uncoupled, the construction redistributes it among compatible jumps of the other marginal. The monotonicity inequalities are precisely the mass-balance conditions that make this transportation of rates possible.

For ordered configurations, the engineered coupling preserves the order. For unordered configurations, Proposition 3.30 composes increasing couplings through the coordinatewise maximum and obtains a process whose total number of discrepancies never increases. The invariant-measure argument needs a stronger form: under connectivity assumptions, discrepancies of opposite sign can be transported until they meet and disappear. Applying this coupling to two extremal stationary laws forces their joint stationary coupling to be ordered, which yields the one-parameter stochastic ordering in Theorem 2.15.

This is not a generic restatement of basic coupling. The source proves that ordinary basic coupling is unavailable for the class except in the simple-exclusion case; the reusable object is an explicitly **non-diagonal coupling of different microscopic moves**.

## Representative IPS use

Section 4 treats exclusion with speed change and several traffic-type processes. For these systems the jump rate depends on nearby occupation variables, so the same-arrow basic construction need not be attractive. The authors compute the non-basic coupling rates, obtain exact attractiveness conditions, and then use Theorem 2.15 to determine extremal translation-invariant invariant measures in the regimes satisfying the required irreducibility assumptions.

## Limitations

The method is specialized to conservative exclusion-type systems and requires solving nontrivial inequalities for the jump rates. Nonincrease of discrepancies alone does not imply coalescence or uniqueness of the invariant law across different conserved densities. The stronger invariant-law conclusion needs translation invariance, no blocking configurations, connectivity, and enough positivity to eliminate opposite discrepancies. The theorem therefore classifies extremal translation-invariant stationary measures rather than proving convergence from every initial configuration. In models without an order or a conserved discrepancy interpretation, the coupled-rate construction may have no analogue.

## Sources

Primary checked source: Gobron and Saada, *Couplings and attractiveness for general exclusion processes*, Ensaios Matemáticos 38 (2023), 263--313. Theorems 2.9 and 2.13 give monotonicity and the discrepancy-nonincreasing coupling; Proposition 3.30 constructs its generator. Proposition 3.36 and Theorem 2.15 supply the discrepancy-elimination step and extremal invariant-law classification. Section 4 shows explicitly that the construction reduces to basic coupling for simple exclusion and must be different for the more general models.