# Graduate Student D assignment 002: signed four-walk cancellation test

Work on branch `research/voter-discordant-concentration`.

Read first:

- `project-state.md`;
- `CHATGPT.md`, especially the standing novelty standard;
- `research/active/voter-discordant-concentration/state.md`;
- `research/active/voter-discordant-concentration/proof-spine.md`;
- `research/active/voter-discordant-concentration/meetings/001-sharp-concentration-reduction.md`;
- `research/active/voter-discordant-concentration/notes/professor-assignment-001-verification.md`;
- your assignment-001 report;
- the relevant duality/random-walk estimates in Avena--Baldasso--Hazra--den Hollander--Quattropani (2024).

Do not work on extending the Section 5 polynomial time window by tuning `K_n` or slack exponents.

## Goal

Test whether the corrected sharp concentration scale

$$
\operatorname{Var}_u^G(\mathcal D_t)
\lesssim_{\mathbb P}\frac{1+t}{n}
$$

for `t=o(n)` can be obtained from a **signed four-walk cancellation identity**, rather than by discarding interacting dual families.

Begin with `u=1/2`, where the four-lineage partition weights simplify maximally.

## Task A: variance-differential identity in explicit signed form

Let

$$
V(t)=\operatorname{Var}_{1/2}^G(\mathcal D_t).
$$

Starting from

$$
V'(t)=2\operatorname{Cov}_{1/2}^G(\mathcal D_t,L\mathcal D_t)
+\mathbf E_{1/2}^G\Gamma(\mathcal D)(\eta_t),
$$

write `Cov(Dcal,L Dcal)` as an exact signed sum over one edge pair and one edge/wedge pair. Keep all coefficients and multiplicities explicit.

Express every covariance term by the simultaneous four-coalescing-walk partition law at time `t`. At `u=1/2`, reduce the expression to probabilities of the three even pairings and the four-block coalescence event.

The output must expose the full signed global sum; do not stop at a bound by the absolute probability of any cross meeting.

## Task B: search for exact cancellation before estimates

Use the edge/wedge incidence structure and the coefficients

$$
\mathcal D=\frac12-\frac1{dn}\sum_{e}\sigma_{e^-}\sigma_{e^+},
$$

$$
L\mathcal D
=-\frac1d
+\frac{2}{dn}\sum_e\sigma_{e^-}\sigma_{e^+}
-\frac{2}{d^2n}\sum_x\sum_{\{y,z\}\subset N(x)}\sigma_y\sigma_z
$$

to test whether the leading cross-meeting contribution cancels algebraically after summing over the edge/wedge coefficients.

Look for any of the following, without assuming one must hold:

1. an exact incidence identity making the leading `t/n` cross-meeting term cancel;
2. a discrete divergence/gradient form of `L Dcal` that converts the signed sum to a boundary or collision term;
3. a Poisson/corrector observable `Phi` for which `L Phi` removes the problematic quadratic drift to leading order;
4. a direct sign estimate `Cov(Dcal,L Dcal)<=C/n`.

If a cancellation appears only after averaging over the random regular graph, state exactly which environment expectation/concentration input is needed and preserve the quenched-in-probability target.

## Task C: hostile asymptotic test

If no exact cancellation is visible, compute the leading contribution of widely separated edge/wedge pairs after mixing. Determine whether the signed sum is genuinely of order `1/n`, or instead of order `t/n` (or larger) at the covariance level.

A rigorous lower bound showing

$$
\operatorname{Cov}(\mathcal D_t,L\mathcal D_t)
$$

has an unavoidable positive contribution too large for the desired variance scale would refute the variance-differential route and may challenge the corrected conjecture itself. Distinguish those two possibilities carefully: failure of one decomposition is not failure of the theorem.

## Task D: fall back to the integrated-drift object only if justified

If the same-time variance route is structurally blocked but the obstruction cancels after time integration, return to the exact staggered covariance formula from assignment 001 and test

$$
\mathbf E\left[
\left(\int_0^t\widetilde h_s\,ds\right)^2
\right]
=O_{\mathbb P}(t/n).
$$

Do not merely sum the absolute cross-meeting bound. Identify the precise signed collision classes whose cancellation would be required.

## Task E: theorem-level interpretation

End by deciding which of the following is actually supported:

- a concrete signed four-walk identity/estimate that plausibly closes the corrected theorem;
- a concrete corrector/Poisson-equation reformulation that removes the obstruction;
- a rigorous obstruction to the variance-differential route but not the theorem;
- or no structural progress beyond absolute meeting estimates.

Under the standing novelty standard, an improved exponent or a longer sublinear time window is not a sufficient output.

## Pre-committed opportunity-cost rule

Meeting 001 fixed the following condition. If this block yields only absolute cross-meeting bounds whose time growth is too large for `O((1+t)/n)`, and produces no cancellation, corrector, or alternative structural mechanism, the Professor will reassess the programme rather than send you to tune Section 5 quantitatively.

## Durable output

Commit the report to

`research/active/voter-discordant-concentration/students/student-d/002-four-walk-cancellation.md`

and any symbolic/combinatorial verifier under the same directory.

End with exactly one recommendation:

- `develop signed four-walk theorem`;
- `develop corrector/Poisson equation`;
- `variance route obstructed — theorem still open: ...`;
- `route not tractable — precise obstruction: ...`.

Do not edit `main`.
