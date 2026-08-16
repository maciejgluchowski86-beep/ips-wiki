# Proof spine

## Final theorem package

`VOTER-CONC-001` is mathematically **verified** and scientifically **non-contributory under the standing novelty standard**.

For a finite simple `d`-regular graph with `d>=1`, not necessarily connected, i.i.d. Bernoulli(`u`) voter initial data, and every `t>=0`,

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

Correctness survived the Professor reconstruction and two independent hostile reviews (`add0681`, `45f960b`).

For uniformly random simple regular graphs with fixed `d>=3`, Avena et al. (2024), equation (5.8), gives the sequence-wise consequences

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}((1+t_n)/n)
$$

for deterministic `t_n=o(n)`, and

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)=O_{\mathbb P}(t_n/n)
$$

for deterministic `1<=t_n=o(n)`.

## Fatal prior-work comparison

The novelty audit `audits/003-novelty-prior-work.md` identifies the target source itself as fatal prior work.

Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), Proposition 4.1 proof (4.2), gives the two-edge decoupling on the event of no cross-family interaction. Their equations (5.5)--(5.6) give

$$
\mathbf P_{\nu\otimes\nu}(\tau^{e,f}\le t)
\le4\mathbf P_{\pi\otimes\pi}(\tau_{\rm meet}\le t).
$$

For Bernoulli initial data, summing the corresponding covariance bound over ordered edge pairs immediately yields

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

This already implies the project's random-regular concentration conclusions using source (5.8). The project's constant `2` and genealogy-conditioned quotient-cut proof are sharper and cleaner but do not constitute a new theorem-level mechanism under the standing novelty standard.

## Small-time correction

Literal source Eq. (1.9) is false for unrestricted `t_n->0`; the explicit `t_n=n^{-3}`, `C_n=log n` counterexample is correctness-reviewed.

Priority is unresolved because Capannoli's 2025 thesis was inaccessible to the novelty auditor. This issue is not load-bearing for programme continuation and is not being pursued as an active task.

## Superseded development routes

The following remain reusable technical calculations only:

- Dynkin martingale / integrated-centered-drift decomposition;
- staggered and simultaneous four-lineage covariance formulas;
- variance-differential route;
- exact identities
  $$
  \mathcal D(\sigma)=\frac1{2n}\sigma^TQ\sigma,
  \qquad
  L\mathcal D(\sigma)=\frac1n\sigma^T(P-P^2)\sigma;
  $$
- genealogy-conditioned quotient-cut proof with constant `2`;
- sample-and-discard shrinking-scale diagnosis.

## Direction

`closed`.

There is no unresolved proof edge inside this programme worth another substantial block. Future voter-discordance work must target a genuinely different theorem, not a constant improvement or repackaging of the regular-graph concentration corollary.
