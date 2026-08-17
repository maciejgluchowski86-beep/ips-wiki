---
title: Harris--Lyapunov ergodicity for infinite-dimensional Levy-driven systems
status: literature
audit: current
tags:
  - Harris theorem
  - Levy noise
  - SPDE
---

# Harris--Lyapunov ergodicity for infinite-dimensional Levy-driven systems

## Criterion

Priola--Shirikyan--Xu--Zabczyk use a classical Harris criterion in a genuinely infinite-dimensional phase space. Their Theorem 2.10 says that for a Markov semigroup \(P_t\) on a Polish space it is enough to find a time \(T_0>0\) and \(V\ge0\) such that

\[
P_{T_0}V(x)\le \gamma V(x)+K,
\qquad \gamma<1,
\]

and, for every \(R\), a uniform small-set overlap on the Lyapunov sublevel set,

\[
\|P_{T_0}^*\delta_x-P_{T_0}^*\delta_y\|_{\mathrm{TV}}
\le 2-\delta_R
\quad\text{whenever }V(x)+V(y)\le R.
\]

The theorem yields a strict contraction in a weighted total-variation norm after a fixed time. For their semilinear Hilbert-space equation

\[
dX_t=(AX_t+F(X_t))dt+dZ_t,
\]

Assumption 2.2 requires a dissipative diagonal operator \(A\) with eigenvalues tending to infinity, bounded Lipschitz \(F\), and sufficiently nondegenerate cylindrical symmetric \(\alpha\)-stable noise with a summability condition giving extra spatial regularity. Theorem 2.8 then gives a unique invariant law \(\mu\) and, for every \(p\in(0,\alpha)\),

\[
\|P_t^*\nu-\mu\|_{\mathrm{TV}}
\le C e^{-ct}
\left(1+\int_H |x|^p\,\nu(dx)\right)
\]

for initial laws with finite \(p\)-moment.

## Mechanism

The infinite-dimensional issue is that a bounded ball in the ambient Hilbert space is not compact, so finite-dimensional Harris verification cannot simply be copied. Section 5 resolves this by combining dissipation with **regularisation into a more compact topology**.

For the drift condition, Step 3 chooses \(V(x)=|x|^p\). Lemma 4.2 supplies a moment estimate whose dissipative term is strictly contractive at a sufficiently large skeleton time \(T_0\).

For the small-set condition, Lemma 4.3 gives moment control in a stronger space \(H_\varepsilon\) compactly embedded in \(H\). Thus a Lyapunov-bounded set reaches a compact \(H_\varepsilon\)-ball with uniformly positive probability. Lemma 5.1 supplies irreducibility, while the strong-Feller estimate from Theorem 2.5 controls total variation between nearby transition laws. Compactness upgrades pointwise positive hitting probabilities to a uniform minorisation on the relevant sublevel set. The two Harris hypotheses then give weighted-TV contraction and hence uniqueness and exponential mixing.

This is different from asymptotic coupling: the proof obtains a genuine total-variation small set and invokes a classical Harris contraction, rather than changing the noise so two trajectories merely approach asymptotically.

## Representative IPS use

Example 2.9 applies Theorem 2.8 to a semilinear stochastic heat equation on \([0,\pi]^d\) with Dirichlet boundary conditions and cylindrical \(\alpha\)-stable noise. Under the stated relation between dimension, the noise amplitudes and \(\alpha\), and for bounded Lipschitz nonlinearity, the result upgrades earlier weak-topology mixing to **exponential total-variation mixing**.

The model is not a lattice spin-flip IPS, but it is an infinite-dimensional interacting Markov field with infinitely many noisy modes. Its proof shows how Harris recurrence can survive the loss of local compactness that makes infinite systems harder than finite interacting diffusions.

## Limitations

The theorem relies on strong nondegeneracy and smoothing of the noise. In particular, Assumption 2.2(A4) is used for the strong-Feller estimate, and the positive regularity exponent in the summability condition gives compact embedding into the ambient Hilbert space. Degenerate noise, conservative dynamics, or lattice systems without a smoothing topology may not provide any comparable small set.

The nonlinearity is bounded and Lipschitz in the infinite-dimensional theorem. The argument proves exponential total-variation convergence for laws with a finite \(p\)-moment; it is not a spectral-gap or log-Sobolev theorem. Finally, the small-set verification is model-dependent: Harris' abstract theorem does not by itself provide irreducibility, compact regularisation, or a Lyapunov function.

## Sources

- Priola, Shirikyan, Xu, Zabczyk, *Exponential ergodicity and regularity for equations with Levy noise*, Assumption 2.2, Theorems 2.8 and 2.10, and Section 5, especially Step 3 and Lemma 5.1, https://doi.org/10.1016/j.spa.2011.10.003.
- The same paper, Example 2.9 for the infinite-dimensional stochastic heat equation application, https://arxiv.org/abs/1102.5553.
