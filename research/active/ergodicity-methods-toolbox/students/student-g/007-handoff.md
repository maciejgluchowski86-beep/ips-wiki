# Student G Assignment 007 handoff

## Status

Assignment 007, the positive-rates applicability audit of the frozen 74-method ergodicity toolbox, is complete. This was an assessment phase only. I did not add or revise toolbox entries, did not reopen the positive-rates proof programme, and did not edit `docs/` or `mkdocs.yml`.

The required main audit is:

- `research/active/ergodicity-methods-toolbox/assessment/positive-rates-method-audit.md` — completed at commit `cd7497650cc8778ee508444699ec38baf713ce56`.

Durability checkpoints created during the audit:

- initial target/obstruction scaffold — `de513e8bf0a73c930011ddc0540b0b998ae9a378`;
- complete 74-method disposition matrix — `05caf402f776192d68c8350965d0e0c42eb12e26`;
- extended A/B bridge details — `research/active/ergodicity-methods-toolbox/assessment/positive-rates-shortlist.md`, commit `cfc7dcc2fe11f65d9a356b415d7fd28295048d9b`.

## Disposition counts

Every one of the 74 frozen live methods was assigned exactly one rating under `assessment-protocol.md`:

- **A:** 1
- **B:** 4
- **C:** 25
- **X:** 10
- **N:** 34

Total: 74.

For every `A/B/C/X` rating, the main audit names the positive-rates interface and gives a repository/source pointer. Every `A/B` method has an explicit bridge lemma, implication chain, obstruction-avoidance check, and cheapest falsification test.

## Ranked A/B shortlist

1. **A — Gray one-dimensional edge coalescence** — target PR2, convective disagreement escape.
2. **B — refined non-diagonal discrepancy coupling** — target PR2.
3. **B — information percolation** — PR5, a genuine bypass rather than an improvement of the stopped common-coupling/renewal norms.
4. **B — block coupling / joint-block stationary control** — target PR3, stationary boundary-control diameter.
5. **B — physical-front regeneration adapted to the disagreement front** — target PR2.

No method in the frozen inventory earned `A/B` for PR1, the final signed two-time boundary-transmission operator. The methods most naturally formulated through positive norms, reversible coercivity, positive contour/error weights, or early absolute values erase the cancellation that Meeting 030 leaves as the load-bearing open feature.

### Shortlist interpretation

The first two items are not independent research programmes. Gray supplies the strongest one-dimensional target architecture, while the Gobron--Saada-style refined coupling supplies a concrete mechanism by which the unavailable attractive/basic coupling might be replaced. They should be tested together before either is escalated.

Information percolation is the most genuinely different architecture in the shortlist. It can allow backward histories to survive while proving that the subset carrying initial information is sparse enough to disappear statistically. It therefore need not settle common-coupling extinction, ancestor-clan extinction, or the signed connected-renewal operator.

The block route is the cleanest use of the stationary-control hierarchy because it attacks exactly the part left open by the additive Bellman obstruction: genuinely joint cross-block information.

The regeneration route is lower-confidence. The collection phase found no primary theorem for regeneration of an actual coupled-copy disagreement front, so the required bridge would itself be new. It remains worth a cheap finite-state diagnostic because the established positive-rates result already reduces noncoupling to leftward front escape.

## Single cheapest falsification experiment recommended first

Run one **exact rational local coupled-rate LP at the hard residual point**

`P_h = (1/10000, 1/100, 9999/10000)`.

For every required finite local pair pattern, introduce variables for a Markovian coupling that may pair a flip in one marginal with a flip at a different site in the other marginal. Impose exact marginal-rate constraints and maximize a uniform disagreement-removal constant `kappa` in

`bar L |D| <= -kappa |D|`.

A certified optimum `kappa <= 0` for any unavoidable local pattern kills the strongest version of the refined non-diagonal coupling bridge.

Using the same LP variables, add the Gray-style local constraints: scalar splice edges, no crossing, permanent coalescence after meeting, and protection of the region between a left/right edge pair. Infeasibility then also kills the direct nonmonotone Gray extension.

This is the recommended first experiment because one small exact finite-state calculation can cheaply falsify or materially strengthen the two highest-ranked methods. I have **not** run it in this assignment, because the protocol says to stop after assessment and await hostile cross-review.

## Promising methods killed or sharply downgraded by exact existing obstructions

The main audit records the full reasons. The most important are:

- **Dobrushin influence contraction — X:** the exact trajectory-valued spatial kernel has Dobrushin total-variation coefficient exactly `1`.
- **Path coupling — X:** at the hard near-East calibration point, the exact common-coupling coefficient satisfies `alpha(t)>1` for every tested `0<t<=47`; another generic metric/norm search is already stopped.
- **Maximal local coupling — X:** for binary same-site updates the common-uniform/maximal one-site coupling already realizes the optimal local mismatch, so it does not evade the preceding obstruction.
- **Attractive coupling and censoring — X:** the residual chamber contains genuinely non-attractive/non-repulsive systems.
- **Coupling independence — X as a target architecture:** when applied to right-boundary pinnings, the required conditional-law coupling is essentially the unresolved boundary/shift agreement itself, and the source is Gibbs-based.
- **Holley--Stroock/reversible perturbative comparison — X:** the stopped programme already found frozen reversible comparison unable to transport the needed conclusion; full-volume perturbation would also lose exponentially in volume.
- **Foster--Lyapunov/Harris — X in its natural local form:** the scalar local Foster architectures were refuted by exact balanced circulation and the infinite translation-invariant system has no obvious Harris small set.
- **Toom error graphs — X for the hard residual chamber:** the source needs an eroding rule with genuinely rare errors, whereas the hard near-East disagreement propagation is not a rare-error event; positive error weights would also erase the signed PR1 cancellation.

Several other methods remain `C` rather than `X` because they provide useful diagnostics or proof components without a complete target architecture: weak Poincare/single-spin influence, finite-speed transfer, finite-dual coupling/extinction, clan/CFTP, East screening, CBSEP-style auxiliary processes, second-class moving frames, and survival-conditioned regeneration.

## Repackaging warnings carried forward

- A new coupling must actually change the coupled generator; a scalar Foster/phase correction on the old common coupling is already refuted.
- Information percolation must not be replaced by ancestor extinction, a Dobrushin row sum, or early absolute values.
- The PR3 block bridge must be genuinely cross-block; additive Bellman correctors are exactly the class already ruled out.
- A disagreement-front regeneration proposal needs a fresh restart sigma-field **and** a uniform terminal extinction mechanism. Front speed, fixed-site agreement, occupation estimates, or a stationary moving-frame law can all coexist with convective survival.
- No method presently supplies a credible new PR1 mechanism; renaming a positive norm/coercive estimate does not preserve the signed two-time cancellation.

## Stop point

The audit is complete and committed. No shortlist experiment or proof attempt was started. Per Assignment 007, the next step is hostile cross-review of the dispositions and bridge lemmas before any method is promoted into a positive-rates research block.
