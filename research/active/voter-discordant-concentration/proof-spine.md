# Proof spine

## Main theorem package

`VOTER-CONC-001` has passed the Professor reconstruction and two independent hostile correctness reviews, but remains **claimed** pending the pre-committed novelty / closest-prior-work audit.

For a finite simple `d`-regular graph with `d>=1`, not necessarily connected, i.i.d. Bernoulli(`u`) voter initial data, and every `t>=0`,

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
}
$$

For a uniformly random simple `d`-regular graph with fixed `d>=3`, this yields for every deterministic `t_n=o(n)`

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}((1+t_n)/n),
$$

and hence concentration at scale `C_n sqrt((1+t_n)/n)` for every `C_n->infinity`. For deterministic `1<=t_n=o(n)`, the stronger variance scale `O_P(t_n/n)` gives the source's proposed `C_n sqrt(t_n/n)` scale.

## E0. Small-time correction of source Eq. (1.9)

Literal Eq. (1.9) allows arbitrary `t_n->0`, while Bernoulli initial conditions have nondegenerate `n^{-1/2}` fluctuations. The choice

$$
t_n=n^{-3},\qquad C_n=\log n
$$

is a counterexample to the displayed statement.

Both hostile reviews independently confirm this calculation.

**Status:** correctness passed. Stable scope: the project proves the original source scale for deterministic `1<=t_n=o(n)` and the corrected `sqrt((1+t_n)/n)` scale for all deterministic sublinear sequences. No claim of a complete classification of every subunit sequence under the original scale.

## E1. Deterministic genealogical variance inequality

Condition on the Harris genealogy `H_t`. The ancestral clusters `C_v(t)` receive independent Bernoulli initial labels. The discordant-edge count is a weighted cut statistic on the quotient multigraph.

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

where `J_t` counts original edges whose endpoints have coalesced genealogically. Coupling two ancestral edge families to independent pair systems up to cross-family interaction and applying source (5.6) gives

$$
\operatorname{Var}(\mathbf E[\mathcal D_t\mid H_t])\le q_t^G.
$$

Therefore

$$
\operatorname{Var}_u^G(\mathcal D_t)\le2q_t^G.
$$

Review A and Review B both reconstructed the within-family-coalescence issue and found no missing term. The source four-independent-walk event can only overcount active cross-family interaction, which is harmless for the upper bound.

**Status:** correctness passed by two independent hostile reviews; registry status still `claimed` pending novelty audit.

## E2. Random-regular meeting estimate

For uniformly random simple regular graphs, keep fixed `d>=3`.

Use Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), source **(5.8)**, together with the high-probability `Theta(n)` stationary mean meeting time and spectral-gap bound used there. For deterministic `t_n=o(n)`,

$$
q_{t_n}^G=O_{\mathbb P}((1+t_n)/n).
$$

For deterministic `1<=t_n=o(n)`,

$$
q_{t_n}^G=O_{\mathbb P}(t_n/n).
$$

For `0<=t_n<1`, monotonicity from time one gives `O_P(1/n)`.

The bare printed source (5.7) wording `O(t/n)` is not used uniformly down to `t=0`, since `q_0=1/n`.

**Status:** correctness passed by both reviews.

## E3. Concentration consequence

E1 and E2 give the variance bounds above. Quenched Chebyshev then yields the corrected concentration theorem and the source scale from time one onward.

**Status:** correctness passed by both reviews.

## Superseded proof routes

The following remain mathematically useful but are not load-bearing:

- Dynkin martingale / integrated-centered-drift decomposition;
- staggered four-lineage covariance formula;
- integrated-drift target;
- variance-differential route;
- same-time signed four-walk cancellation;
- Section 5 sample-and-discard shrinking-scale analysis.

Assignment 002 also established

$$
\mathcal D(\sigma)=\frac1{2n}\sigma^TQ\sigma,
\qquad
L\mathcal D(\sigma)=\frac1n\sigma^T(P-P^2)\sigma,
$$

without asserting a sign for `Cov(Dcal,L Dcal)`.

## Current unresolved edge: priority / novelty

The remaining gate is not mathematical correctness. It is whether the theorem package is genuinely new.

A fresh external auditor is assigned in

`audits/assignment-003-novelty-prior-work.md`.

The audit must search predecessor and successor literature and alternate terminology for:

1. the deterministic regular-graph variance inequality or a stronger theorem implying it;
2. the genealogy-conditioned quotient-cut / total-variance argument;
3. the corrected all-sublinear random-regular concentration theorem;
4. the source-scale `sqrt(t_n/n)` theorem for deterministic `1<=t_n=o(n)`;
5. the literal small-time correction of source Eq. (1.9).

The fact that the 2024 source posed Eq. (1.9) as open is evidence but not sufficient priority checking.

## Promotion rule

Meeting 002 pre-committed to a dedicated novelty audit after two correctness reviews and **before `verified` promotion or manuscript contribution language**. Preserve that rule.

If the novelty audit finds decisive prior art, mathematical correctness remains intact but research-contribution status must be downgraded. If it survives, `VOTER-CONC-001` may be promoted to `verified` with the two correctness audits and novelty audit attached.

## Direction

Continue through novelty audit; Graduate Student D remains idle.
