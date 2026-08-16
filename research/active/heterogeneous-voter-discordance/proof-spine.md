# Proof spine

## Main target

For the voter model on an undirected bounded-degree configuration model with unequal degrees, identify and prove the analogues of the regular-random-graph discordance profile and consensus-time diffusion constant.

The first bounded ensemble has empirical degree law converging to a fixed `p` supported on `{3,...,D}`.

## E0. Source-level openness and closest prior work

Den Hollander (2025), *Evolution of Discordance*, Section 2.4, explicitly states that extending the regular-graph discordance theorems to the configuration model with unequal degrees remains open and that the analogues of `theta_d` and `f_d(t)` are not even conjectured there.

Directed configuration-model results are not substitutes for the undirected problem.

**Status:** credible current target; Student E must perform a fresh predecessor/successor and general-voter-theorem audit before any novelty claim.

## E1. Correct conserved coordinate and bracket observable

For a fixed undirected graph, let

$$
\pi_x=\frac{d_x}{2m},
\qquad
B^\pi(\eta)=\sum_x\pi_x\eta_x.
$$

For the rate-one vertex-update voter model,

$$
L B^\pi=0.
$$

If `k_x` is the number of disagreeing neighbours of `x`, then

$$
\Gamma(B^\pi)(\eta)
=\sum_x\frac{k_x}{d_x}\left(\frac{d_x}{2m}\right)^2
=\frac1{4m^2}\sum_xd_xk_x
$$

and therefore

$$
\boxed{
\Gamma(B^\pi)(\eta)
=\frac1{4m^2}
\sum_{\{x,y\}\in E:\eta_x\ne\eta_y}(d_x+d_y).
}
$$

This weighted edge boundary collapses to a constant multiple of the raw discordant-edge count only in the regular case.

**Status:** first-principles structural calculation; Student E must independently rederive and source-check how it interfaces with general finite-voter Wright--Fisher criteria.

## E2. Short-time raw-discordance profile

For Bernoulli(`u`) initial data and a fixed edge `{x,y}`,

$$
\mathbf P_u(\eta_t(x)\ne\eta_t(y))
=2u(1-u)\mathbf P_{x,y}(\tau_{\rm meet}>t).
$$

A uniformly sampled configuration-model edge should converge locally to an edge-rooted size-biased Galton--Watson tree. This suggests a candidate profile

$$
f_p^{\rm raw}(t)
=\mathbf E_{\mathcal T_p}
\mathbf P^{\mathcal T_p}_{o_-,o_+}(\tau_{\rm meet}>t),
$$

where the exact law of the edge-rooted tree and any conditioning must be written correctly.

**Status:** candidate only. Need exact rooting law, local-limit theorem, and finite-time interchange.

## E3. Bracket-weighted profile

The diffusion bracket weights a discordant edge `{x,y}` by `d_x+d_y`. Hence the local object relevant to the Wright--Fisher coefficient is not automatically `f_p^{raw}`. Student E must derive the correct edge/root bias and candidate weighted profile

$$
f_p^{\rm br}(t)
$$

from first principles rather than guessing a moment correction.

A useful falsification question is whether `f_p^{raw}` and `f_p^{br}` reduce to one scalar profile after an explicit change of measure. If not, the regular identity between interface profile and diffusion coefficient genuinely splits in the heterogeneous setting.

**Status:** open structural edge.

## E4. Consensus-time meeting constant

Let

$$
\gamma_n=\mathbf E_{\pi\otimes\pi}^G[\tau_{\rm meet}].
$$

General voter-model diffusion theorems suggest that the consensus-scale coefficient is controlled by `gamma_n`, but the exact hypotheses and normalization must be checked. For the configuration-model ensemble the key questions are:

1. does `gamma_n/n` converge in probability to a deterministic constant for bounded heterogeneous degree law `p`?
2. is that constant already known in random-walk/coalescence literature?
3. can it be represented by a local nonmeeting/Green-function quantity on the size-biased Galton--Watson limit?
4. how does that constant relate to the bracket-weighted local profile in E3?

**Status:** source/literature and derivation task.

## E5. First theorem-scale bottleneck

The first assignment must end with one exact statement whose proof would materially advance the open problem. Plausible forms are:

- a local-profile theorem proving convergence of the expected raw and weighted discordance for every fixed time;
- a theorem identifying the stationary meeting-time constant in terms of the edge-rooted local limit;
- or a structural obstruction showing that the regular one-constant picture cannot survive heterogeneity.

A numerical evaluation for one degree law does not count.

## Current owner

Graduate Student E, `students/student-e/assignment-001.md`.
