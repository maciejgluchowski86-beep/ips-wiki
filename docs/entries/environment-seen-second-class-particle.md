---
title: Environment seen from a second-class particle
status: literature
audit: current
tags:
  - second-class particle
  - TASEP
  - moving frame
---

# Environment seen from a second-class particle

## Criterion

Consider TASEP on $\mathbb Z$ with one distinguished second-class particle. Initially the second-class particle is at the origin and every other site is occupied independently with density $\rho\in(0,1)$. Let $\Phi_t^\rho$ be the law of the configuration at time $t$ **viewed from the current position of the second-class particle**. Martin--Sly--Zhang construct an explicit stationary moving-frame law $\Psi^\rho$ in Section 2.3 and prove in Theorem 1.7 that

\[
\Phi_t^\rho\Longrightarrow \Psi^\rho\qquad(t\to\infty).
\]

They further construct a two-sided stationary TASEP process in this moving frame and prove in Proposition 5.3 that it is ergodic under time shifts. Thus the random marker does more than locate a microscopic discrepancy: recentering on it produces a Markov environment with its own stationary and ergodic long-time law.

## Mechanism

A second-class particle is the unique discrepancy in the basic coupling of two TASEPs that differ initially at one site. Instead of trying to annihilate that discrepancy, the method changes coordinates so that the marker is always at the origin and studies the surrounding first-class particles and holes.

Section 2.3 constructs $\Psi^\rho$ from a stationary multi-class TASEP/renewal representation. The key moving-frame comparison in Section 4 couples a nonstationary process started from the Bernoulli background with this stationary marked process. Labels attached to second-class particles are rearranged so that the configuration observed from the selected label has the stationary law. Geometric control of the labels then yields Theorem 1.7.

Proposition 5.3 shows that stationarity is not enough: the marked-frame process is actually time ergodic. Its proof uses a spatial coupling of two samples of $\Psi^\rho$ that makes prescribed central windows initially independent while arranging matching particle counts on larger intervals with high probability. TASEP dynamics can then reconcile the central observations, contradicting any nontrivial invariant event. Hence moving with the discrepancy exposes an ergodic environment even though the marker itself never disappears.

This is distinct from the live exact product-shock page. There, a specially chosen translated shock family is closed exactly under the coupled generator and the second-class marker itself performs an autonomous random walk. Here the surrounding moving-frame environment is not preserved at every time from the chosen initial law; convergence to a nontrivial stationary law is the theorem to be proved.

## Representative IPS use

Theorem 1.7 is itself a TASEP convergence-to-equilibrium result in a random moving frame. It starts from a single second-class particle inserted into an otherwise independent Bernoulli-$\rho$ configuration and identifies the limiting environment seen from that particle.

The time-ergodicity statement in Proposition 5.3 is then load-bearing in the paper's last-passage-percolation application: Birkhoff averaging in the stationary second-class frame is used to identify limiting empirical environments along geodesics. Thus the method shows why an “environment viewed from a defect” can be more tractable than the defect position or the laboratory-frame configuration separately.

## Limitations

The proof is highly model-specific and uses the integrable/queueing and multi-class structure of TASEP. The theorem concerns a homogeneous density on both sides of the isolated second-class particle, not arbitrary shock or rarefaction initial data. It proves convergence of the **moving-frame environment**, not global mixing of TASEP on $\mathbb Z$; particle-number conservation prevents such a statement without fixing an appropriate stationary sector. The stationary law $\Psi^\rho$ also has non-product correlations around the marked particle, so ordinary product-measure arguments do not replace the coupling construction.

## Sources

- Martin, Sly and Zhang, *Convergence of the Environment Seen from Geodesics in Exponential Last-Passage Percolation*, Theorem 1.7, Section 2.3, Section 4, Proposition 5.3. DOI: https://doi.org/10.4171/jems/1594; inspected preprint: https://arxiv.org/abs/2106.05242.
