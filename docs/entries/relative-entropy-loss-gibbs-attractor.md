---
title: Relative-entropy loss and the Gibbs attractor principle
status: literature
audit: current
tags:
  - entropy loss
  - Gibbs attractor
  - irreversible IPS
---

# Relative-entropy loss and the Gibbs attractor principle

## Criterion

Let \((\nu_t)_{t\ge0}\) be the law of a translation-invariant finite-state interacting particle system and suppose there is a translation-invariant stationary measure \(\mu\) that is Gibbs for a specification \(\gamma\). Jahnel--Koppl impose their rate assumptions (R1)--(R6) and specification assumptions (S1)--(S4). Under these hypotheses Theorem 2.6 proves a **dynamical Gibbs variational principle** for the approximating relative-entropy loss density \(g_L(\nu\mid\mu)\): it exists on the stated class, is upper semicontinuous and nonpositive, and

\[
g_L(\nu\mid\mu)=0
\quad\Longrightarrow\quad
\nu\in\mathcal G(\gamma).
\]

Proposition 2.5 supplies the monotonicity behind this criterion: relative entropy density with respect to the stationary Gibbs measure cannot increase along the dynamics.

Theorem 2.10 converts the zero-loss criterion into an attractor statement. Every weak limit point of a trajectory of translation-invariant initial laws is a Gibbs measure for the same specification \(\gamma\). Consequently, if \(\mathcal G(\gamma)\) consists of a single translation-invariant measure in the relevant class, compactness of the probability-law trajectory forces convergence to that measure.

## Mechanism

This is an **entropy-dissipation argument without an entropy coercivity constant**. One does not prove an LSI, mLSI, or inequality of the form entropy \(\le C\) entropy production. Instead the proof only needs two structural facts: entropy density is a bounded-below Lyapunov functional, and states with zero instantaneous entropy loss are exactly Gibbs states.

The key contradiction is made local and uniform. Proposition 3.18 shows that if a translation-invariant law \(\nu\) is not Gibbs, then there is a weak neighborhood \(G_\nu\), a short time interval and \(\delta>0\) such that every trajectory starting in \(G_\nu\) loses relative-entropy density at rate at least \(\delta\) over that interval. If a non-Gibbs law were an omega-limit point, the trajectory would return to this neighborhood infinitely often. Each visit would force another fixed entropy drop, contradicting the lower boundedness of relative entropy density.

Theorem 2.6 supplies exactly the difficult identification needed for that argument: upper semicontinuity of the loss and the implication “zero loss \(\Rightarrow\) Gibbs” for irreversible local-update dynamics. The output is therefore a description of the entire omega-limit set, even when there are several Gibbs phases and no quantitative mixing rate.

This is distinct from logarithmic-Sobolev methods. LSI turns entropy production into a uniform exponential rate; the Gibbs-attractor method allows the dissipation to become arbitrarily small along large time scales and still rules out non-Gibbs limit points.

## Representative IPS use

The source is itself formulated for translation-invariant interacting particle systems on \(\mathbb Z^d\) with finite local state space and updates on arbitrary finite regions. Reversibility is not required: the reference Gibbs measure need only be time-stationary, together with the stated nondegeneracy and continuity assumptions on rates and specification.

Thus Theorem 2.10 applies to irreversible IPS for which ordinary detailed-balance Dirichlet-form arguments are unavailable. It gives a robust long-time conclusion: every subsequential weak limit is an equilibrium Gibbs state. When the Gibbs specification has a unique translation-invariant Gibbs measure, this yields convergence of translation-invariant trajectories to that equilibrium, but the theorem deliberately permits phase coexistence and hence does not assert global uniqueness in general.

## Limitations

The argument is qualitative. It gives no spectral gap, log-Sobolev constant, or numerical convergence rate. With several Gibbs measures, it only places the omega-limit set inside the Gibbs simplex; it need not select a phase or prove that the full trajectory converges.

Translation invariance is built into the theorem quoted here, as are finite local state space and the technical rate/specification hypotheses (R1)--(R6), (S1)--(S4). The zero-loss characterization is the load-bearing theorem; relative entropy monotonicity alone is insufficient, because an irreversible dynamics can in principle have non-equilibrium states with vanishing first-order entropy loss unless this is ruled out.

Finally, this page concerns dynamical attraction to the Gibbs set, not the static Gibbs variational principle by itself. It is not a substitute for Harris recurrence when there is no useful Gibbs reference law.

## Sources

- Jahnel, Koppl, *Dynamical Gibbs Variational Principles for Irreversible Interacting Particle Systems with Applications to Attractor Properties*, Proposition 2.5 and Theorem 2.6, https://doi.org/10.1214/22-AAP1926.
- The same paper, Theorem 2.10, Proposition 3.18 and Section 3.5 for the omega-limit/attractor argument, https://arxiv.org/abs/2205.02738.
