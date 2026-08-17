---
method_id: foster-lyapunov-harris-geometric-ergodicity
title: Foster-Lyapunov drift plus Harris small-set recurrence
category: lyapunov-regeneration
targets:
  - uniqueness
  - convergence
model_scope: General-state-space Markov processes, with an interacting stochastic bead-spring diffusion as a concrete infinite-dimensional-adjacent particle application
source_status: primary-checked
primary_source: Jonathan C. Mattingly, Scott A. McKinley, Natesh S. Pillai, Geometric ergodicity of a bead-spring pair with stochastic Stokes forcing, Stochastic Processes and their Applications 122 (2012), 3953-3979.
primary_pinpoint: Theorem 2.2 (Harris contraction criterion), Lemma 2.3 (Lyapunov drift), Proposition 2.4 (minorization), and Theorem 2.1 (geometric ergodicity of the interacting bead-spring process)
primary_url: https://doi.org/10.1016/j.spa.2012.07.003
application_source: Jonathan C. Mattingly, Scott A. McKinley, Natesh S. Pillai, Geometric ergodicity of a bead-spring pair with stochastic Stokes forcing, Stochastic Processes and their Applications 122 (2012), 3953-3979.
application_pinpoint: Theorem 2.1 together with Lemma 2.3 and Proposition 2.4
application_url: https://arxiv.org/abs/0902.4496
wiki_candidate: yes
---

# Foster-Lyapunov drift plus Harris small-set recurrence

## Criterion

A Harris-type geometric-ergodicity proof combines a drift back toward a controlled region with a local mixing condition inside that region. In Mattingly--McKinley--Pillai, Theorem 2.2 uses a function \(V\ge0\) with compact level sets and constants \(t>0\), \(c_0\in(0,1)\), \(c_1>0\) such that
\[
P_tV(x)\le c_0V(x)+c_1.
\]
For a sufficiently large sublevel set
\[
C=\{V\le K\},\qquad K\ge \frac{2c_1}{1-c_0},
\]
one also assumes a uniform minorization
\[
P_t(x,\cdot)\ge \alpha\nu(\cdot),\qquad x\in C,
\]
for some \(\alpha>0\) and probability law \(\nu\). The theorem gives a strict contraction of \(P_t^*\) in a weighted total-variation metric \(\rho_\beta\). Iteration yields uniqueness of the invariant probability measure in the corresponding weighted class and exponential convergence toward it.

## Mechanism

The Lyapunov inequality prevents probability mass from spending too much time arbitrarily far from the central region: outside a large sublevel set the expected value of \(V\) contracts. The minorization says that, once two copies are in that controlled region, both transition kernels contain a common component \(\alpha\nu\). A coupling can therefore force the copies to agree with fixed positive probability whenever they simultaneously visit the small set.

The weighted metric packages these two effects into one contraction. Far away, the Lyapunov weight supplies contraction even before coupling; near the center, the common minorizing measure supplies contraction in ordinary total variation. This is the characteristic Harris architecture: recurrence alone does not give a quantitative rate, and minorization on a set that is rarely reached is useless; together they produce geometric ergodicity.

## Representative IPS use

Mattingly--McKinley--Pillai study two particles connected by a nonlinear spring and advected by a stochastic Stokes velocity field. The state contains the bead connector and finitely many fluid modes, so it is a genuinely interacting particle/diffusion system rather than a finite-state chain. Singular spring forces such as Lennard--Jones-type repulsion are allowed.

Their Lemma 2.3 proves the geometric Lyapunov drift. Proposition 2.4 obtains the required minorization from topological irreducibility and hypoelliptic smoothing. Theorem 2.1 then concludes geometric ergodicity: the connector converges exponentially to a unique nontrivial stationary law. The source is especially instructive because the ``small set'' is not obtained for free from compactness; singular drift forces a good-set/bad-set control argument before the Harris theorem can be applied.

## Limitations

A Foster--Lyapunov function is model-dependent and can be hard to construct in an infinite interacting system. The drift must be strong enough to control excursions, while the small-set/minorization condition requires genuine smoothing or irreducibility; deterministic conservation laws, degenerate noise, or multiple closed communicating classes can defeat it. In infinite-volume lattice IPS, compact sublevel sets and uniform minorization are often unavailable in the natural topology, so Harris theory is much easier to use for interacting diffusions, finite-particle systems, interfaces, or finite-volume reductions than for translation-invariant infinite spin systems.

This entry is the drift-plus-small-set **ergodicity criterion**. Nummelin splitting is a different regeneration construction only when the artificial atom and renewal decomposition themselves carry the proof; merely invoking a small-set minorization does not create a separate method.

## Sources

- Mattingly, McKinley, Pillai, *Geometric ergodicity of a bead-spring pair with stochastic Stokes forcing*, Theorem 2.2, Lemma 2.3, Proposition 2.4, and Theorem 2.1, https://doi.org/10.1016/j.spa.2012.07.003.
- Open preprint: https://arxiv.org/abs/0902.4496.
