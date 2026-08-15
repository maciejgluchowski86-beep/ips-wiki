# Proof spine

## Main target

Resolve the sharp sublinear-time concentration problem for the fraction of discordant edges in the voter model on random `d`-regular graphs, as proposed in Avena--Baldasso--Hazra--den Hollander--Quattropani (2024).

The intended scale is

$$
\sqrt{t/n}
$$

for `t=o(n)`, subject to the exact source formulation that Graduate Student D must verify before using it as the theorem statement.

## E0. Source theorem and open formulation

The 2024 paper proves concentration by a weak-dependence method on moderate time scales and explicitly proposes a stronger concentration statement beyond the proved window.

**Status:** source-level open target credible; exact Eq. (1.9) quantifiers/probability mode to be transcribed and checked in assignment 001.

## E1. Martingale scale

For a fixed `d`-regular graph, let `D(eta)` be the number of discordant edges and let `k_x` be the number of neighbours disagreeing with vertex `x`.

A candidate first-principles calculation from reconnaissance is

$$
LD
=\sum_x\frac{k_x}{d}(d-2k_x).
$$

Defining

$$
W(\eta)=\sum_x k_x(d-k_x),
$$

this becomes

$$
LD=\frac2dW-2D.
$$

Since one vertex update changes the discordant-edge density by `O(1/n)` at total update rate `n`, the martingale quadratic variation is naturally `O(t/n)`.

**Status:** promising reconnaissance calculation only. Graduate Student D must rederive constants and normalization exactly from the paper's voter-model convention.

## E2. Integrated centered drift

If E1 is correct, the martingale part already has the conjectured `sqrt(t/n)` scale. The load-bearing term is then the time integral of the centered local drift, equivalently a centered wedge/two-edge observable.

The likely missing estimate is a covariance or second-moment bound for this integrated drift that is uniform for all `t=o(n)`.

**Status:** current candidate bottleneck, not yet a proved reduction.

## E3. Dual coalescing-walk representation

The source paper represents discordance through coalescing random walks and obtains moderate-time concentration from weak dependence of those walks.

Assignment 001 must determine whether the centered drift covariance can be reduced to a finite system of two-, three-, or four-walk meeting events and whether the resulting estimate plausibly reaches the full sublinear window.

A useful output is an exact necessary estimate of the form

$$
\operatorname{Var}\left(\int_0^t \widetilde W_s\,ds\right)
\lesssim \frac{t}{n}
$$

or the correctly normalized analogue, together with a source/duality expression for its left-hand side.

**Status:** open.

## E4. Very-small-time formulation check

The literal `sqrt(t/n)` threshold may require care when `t` tends to zero or stays much smaller than one. Before proving anything, assignment 001 must test Eq. (1.9) in every time regime allowed by its quantifiers.

If the published expected strengthening is literally false without an additional lower-time condition or additive `n^{-1/2}` term, identifying the correct statement is a structural result and should replace the target rather than be hidden.

**Status:** mandatory falsification check.

## Novelty guardrail

Do not optimize the exponent in the already-proved moderate-time window as an end in itself. A larger but still partial polynomial window is diagnostic unless it reveals a structural threshold.

A qualifying result should resolve the proposed sharp regime, refute/correct its literal formulation, or establish a genuinely new structural concentration mechanism.

## Current first unresolved edge

Source-grounded derivation of E1--E4 and identification of the single correlation estimate carrying the sharp theorem.

**Owner:** Graduate Student D, assignment `students/student-d/assignment-001.md`.
