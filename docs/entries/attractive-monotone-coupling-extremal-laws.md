---
title: Attractive monotone coupling and extremal invariant laws
status: literature
audit: current
tags:
  - ergodicity methods
  - coupling
  - attractiveness
---

# Attractive monotone coupling and extremal invariant laws

## Criterion

For a binary spin system with flip rate $c(x,\eta)$ and coordinatewise order, a standard attractiveness criterion is the following. Whenever $\eta\leq\eta'$, require

\[
c(x,\eta)\leq c(x,\eta')
\quad\text{if }\eta(x)=\eta'(x)=0,
\]

and

\[
c(x,\eta)\geq c(x,\eta')
\quad\text{if }\eta(x)=\eta'(x)=1.
\]

Then one can couple copies started from ordered configurations so that the order is preserved for all times. In particular, when the all-zero and all-one configurations are available, monotonicity gives lower and upper limiting stationary laws

\[
\nu^- = \lim_{t\to\infty}\delta_{\mathbf 0}S(t),
\qquad
\nu^+ = \lim_{t\to\infty}\delta_{\mathbf 1}S(t).
\]

Every invariant law is stochastically sandwiched between these extremal limits. Consequently, proving $\nu^-=\nu^+$ proves uniqueness; the same sandwich then yields convergence of every initial law to that common invariant law for bounded increasing cylinder functions, hence weak convergence on the product space.

## Mechanism

The coupling uses the same update opportunities for the two configurations. At a site where both copies are $0$, the smaller process uses the common part of the two birth rates and the larger process receives any excess birth rate. At a site where both are $1$, the common part of the death rates is again used jointly and the smaller configuration receives the excess death rate. The two attractiveness inequalities are exactly what prevents an ordered pair from crossing.

This converts a global invariant-measure problem into an extremal one. Starting from $\mathbf 0$ gives an increasing family in stochastic order, while starting from $\mathbf 1$ gives a decreasing family. Any process started between them remains between them under the common coupling. Thus many uniqueness proofs for attractive systems need only show that the upper and lower processes lose their disagreement.

Warfheimer uses a stronger, explicit maximal-type coupling of three ordered spin marginals. The rates in Tables 3.1-3.2 make the marginals flip together as much as possible while preserving their individual rates and the order. This illustrates that monotonicity is not merely an order comparison: the coupled process can be designed so that the remaining disagreement has a tractable geometry.

## Representative IPS use

Warfheimer studies a one-dimensional spin system whose rates are modulated by another evolving spin system. Conditions (2.1)-(2.2) make the joint process attractive. Theorem 2.2 shows that if the background process has a unique stationary distribution and the stated positivity constant $C$ is positive, then the lower and upper invariant laws are the only extremal stationary distributions. The contact process in a randomly evolving environment is listed in Remark (ii) as satisfying the relevant positivity condition under the stated symmetry assumptions.

This example also shows the distinction between the method's two stages. The monotone coupling identifies the possible extremal laws; equality of the lower and upper laws is an additional problem and is not supplied by attractiveness alone.

## Limitations

The method needs an order compatible with the dynamics. Non-attractive spin systems may admit no order-preserving basic coupling. Even for attractive systems, the extremal-law construction is a reduction rather than a uniqueness theorem: supercritical contact-type systems can have distinct lower and upper invariant laws. Quantitative mixing rates also do not follow from stochastic ordering alone; one needs a separate estimate on the decay of the coupled disagreement.

For systems with an evolving environment, assumptions on the background matter. Warfheimer gives examples showing that the conclusion about the number of extremal stationary laws can fail when the background has multiple stationary distributions or when the required positivity degenerates.

## Sources

Primary source: Marcus Warfheimer, *Attractive nearest-neighbor spin systems on the integers in a randomly evolving environment*, arXiv:0712.2929v2 (2010), Definition 2.1 and (2.1)-(2.2), Theorem 2.2, and Section 3. https://arxiv.org/abs/0712.2929

The paper explicitly attributes the corresponding no-background one-dimensional extremal-law theorem to T. M. Liggett, *Attractive nearest neighbor spin systems on the integers*, Annals of Probability 6 (1978), 629-636; the checked criterion and application above use Warfheimer's later primary formulation rather than relying on that attribution for a stronger claim.
