# Proof spine

## Main target

The corrected sharp concentration theorem for the discordant-edge density in the voter model on random `d`-regular graphs is now **claimed**:

$$
\mathbf P_u^G\left(
|\mathcal D_{t_n}^n-\mathbf E_u^G\mathcal D_{t_n}^n|
>C_n\sqrt{\frac{1+t_n}{n}}
\right)\xrightarrow{\mathbb P}0
$$

for fixed `d>=3`, `u in (0,1)`, every deterministic `t_n=o(n)`, and every `C_n->infinity`.

For deterministic `t_n>=1`, the claimed proof gives the sharper source scale `C_n sqrt(t_n/n)`.

## E0. Small-time correction of source Eq. (1.9)

Literal Eq. (1.9) allows arbitrary `t_n->0`, but Bernoulli initial conditions have nondegenerate `n^{-1/2}` fluctuations. The explicit choice

$$
t_n=n^{-3},\qquad C_n=\log n
$$

contradicts the displayed source statement.

**Status:** Professor-checked; included in `VOTER-CONC-001`; independent audit pending with the theorem package.

## E1. Deterministic genealogical variance inequality

Condition on the Harris genealogy `H_t`. The ancestral clusters `C_v(t)` receive independent Bernoulli initial labels. The discordant-edge count is a weighted cut statistic on the quotient multigraph of clusters.

Let

$$
q_t^G=\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

The conditional cut variance satisfies

$$
\mathbf E[\operatorname{Var}(\mathcal D_t\mid H_t)]\le q_t^G.
$$

The conditional mean is

$$
\mathbf E[\mathcal D_t\mid H_t]
=p\left(1-\frac{J_t}{m}\right),
\qquad p=2u(1-u),
$$

where `J_t` counts original edges whose endpoints have coalesced genealogically. Coupling two ancestral edge families to independent pair systems up to their first cross-family interaction and then applying source Eq. (5.6) gives

$$
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t])\le q_t^G.
$$

Therefore

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)\le2q_t^G.
}
$$

**Status:** central claimed theorem; Professor independently reconstructed; two hostile reviews pending.

## E2. Random-regular meeting estimate

For a uniform random simple `d`-regular graph with fixed `d>=3`, Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), equations (5.7)--(5.8), together with the standard high-probability spectral-gap and mean-meeting-time inputs used there, give for deterministic `1<=t_n=o(n)`

$$
q_{t_n}^G=O_{\mathbb P}(t_n/n).
$$

For `0<=t_n<1`, monotonicity and the time-one estimate give

$$
q_{t_n}^G=O_{\mathbb P}(1/n).
$$

Hence for every deterministic `t_n=o(n)`,

$$
q_{t_n}^G=O_{\mathbb P}((1+t_n)/n).
$$

**Status:** source interface checked by Professor; independent audit pending.

## E3. Concentration consequence

E1 and E2 give

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}((1+t_n)/n).
$$

Chebyshev yields the corrected target for arbitrary `C_n->infinity`. If `t_n>=1`, use the sharper `O_P(t_n/n)` estimate to obtain the source scale.

**Status:** claimed consequence pending independent review.

## Superseded proof routes

The following are no longer load-bearing, though their exact calculations remain useful:

- the Dynkin martingale / integrated-centered-drift decomposition;
- the staggered four-lineage covariance formula;
- the sufficient integrated-drift estimate;
- the variance differential
  $$
  V'(t)=2\operatorname{Cov}(\mathcal D_t,L\mathcal D_t)+\mathbf E\Gamma(\mathcal D)(\eta_t);
  $$
- the same-time signed four-walk cancellation problem;
- the Section 5 sample-and-discard shrinking-scale analysis.

Assignment 002 nevertheless produced the exact incidence identities

$$
\mathcal D(\sigma)=\frac1{2n}\sigma^TQ\sigma,
\qquad
L\mathcal D(\sigma)=\frac1n\sigma^T(P-P^2)\sigma.
$$

No sign estimate for `Cov(Dcal,L Dcal)` is asserted.

## Current unresolved edge: verification and novelty

There is no further development lemma before correctness audit.

Two independent reviewers must stress-test E1--E3, especially:

1. conditional cut-variance combinatorics;
2. ancestral cluster-square equals stationary meeting probability;
3. the four-family covariance coupling and within-family coalescence;
4. oriented versus unoriented edge averaging;
5. source (5.7)--(5.8) and the sequence-wise quenched probability mode;
6. small-time claim boundaries.

If both correctness reviews pass, run a separate closest-prior-work / novelty audit. Only then consider `verified` promotion and a stable theorem note/manuscript.

## Novelty guardrail

`VOTER-CONC-001` is structurally eligible under the standing novelty standard because it is a deterministic graph inequality and a full-regime theorem, not a larger-window or better-constant instance. Publication-level novelty is **not yet established**.

## Direction

Continue through independent audit; Graduate Student D is idle meanwhile.