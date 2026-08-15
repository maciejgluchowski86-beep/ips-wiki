# Proof spine

## Main target

For one-dimensional BABP with branching parameter `lambda>0`, started from any finite nonempty particle set `B`, prove local convergence to Bernoulli equilibrium `pi` with particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

Begin with `B={0}`. Existing results cover `lambda>0.0347`; the active novelty is the remaining small-parameter range.

This is the current working target. A bounded concurrent reconnaissance compares its expected value against other explicit open problems before the group commits to prolonged technical development.

## E0. Self-duality convergence criterion

BABP self-duality gives, for finite `B'`,

$$
\mathbf E\left[\left(-\frac1\lambda\right)^{|B'(t)\cap B|}\right]
=
\mathbf E\left[\left(-\frac1\lambda\right)^{|B(t)\cap B'|}\right].
$$

Martinelli--Shapira--Toninelli Remark 5.3 states that decay of the right-hand side to zero for every finite test set `B'` implies convergence of the law of `B(t)` to `pi`.

**Status:** established external input; Student B should rederive the precise implication needed for finite-dimensional distributions.

## E1. Existing all-parameter inputs

For every `lambda>0`:

- DFP is exponentially ergodic on local observables uniformly over initial configurations (Martinelli--Shapira--Toninelli Theorem 5.2);
- BABP started from a finite nonempty seed grows linearly in cardinality almost surely, via BABP--DFP quasi-duality;
- BABP started from Bernoulli product initial laws converges exponentially to equilibrium.

**Status:** established external input.

## E2. Locate the historical threshold obstruction

Reconstruct the best classical finite-seed convergence argument, in particular Sudbury's theorem giving convergence for `lambda>0.0347`.

Identify the exact statement whose proof requires the numerical lower bound on `lambda`: a submartingale drift, edge-speed estimate, coupling success probability, block event, or other inequality. Express that condition in current `lambda`, `p`, `q` notation and determine which parts of the proof are already available for every `lambda>0` from the 2025 results.

**Status:** open.

**Current owner:** Graduate Student B.

## E3. Determine whether the new all-parameter inputs remove E2

The first concrete probe is the existing DFP/quasi-duality interface, because it is the new ingredient in the 2025 progress paper. Let

$$
F_{B'}(C)=\left(-\frac1\lambda\right)^{|C\cap B'|}.
$$

Test whether

$$
\mathbf E_B F_{B'}(B(t))
$$

can be controlled using DFP ergodicity/quasi-duality, beginning with `B'={0}` and `B'={0,1}`. An exact representation, stable finite linear combination, or a proof that no stable representation exists would all narrow the spine.

**Status:** open.

**Dependencies:** E0/E1; informed by E2.

**Important qualification:** duality is not a required method. If reconstructing Sudbury's proof shows that the true missing statement is spatial, regenerative, coupling-based, spectral, or otherwise independent of DFP algebra, replace this edge with that statement rather than forcing an algebraic route.

## E4. The actual new lemma

After E2/E3, formulate the smallest target-level statement not already in the literature whose proof would close the remaining small-parameter range.

A satisfactory E4 has the form:

> all other ingredients are available, and finite-seed convergence follows from this precise lemma.

The lemma may be a local-density estimate, regeneration/coupling statement, control of the signed finite-test observable, or another mechanism revealed by the historical audit.

**Status:** not yet formulated sharply enough.

## O1. Opportunity-cost comparison

In parallel with E2/E3, inspect recent high-quality progress/survey literature that explicitly records open problems in probability/IPS/KCM and adjacent areas. Produce a small ranked set of alternative targets with:

- precise theorem statement;
- exact evidence that the problem remains open or an honest successor check;
- the present obstruction;
- why this group has a plausible leverage point;
- why the problem is preferable or inferior to BABP on tractability/significance grounds.

This is not a second scientific programme and should not become an aimless survey.

**Status:** open bounded reconnaissance.

**Owner:** Graduate Student A.

**Decision use:** if Student B finds that the 2025 BABP inputs leave the old threshold mechanism essentially unchanged, compare immediately against O1 before inventing a new BABP representation.

## Current first unresolved edge

**E2/E3 are the BABP mathematical bottleneck. O1 is the concurrent opportunity-cost check.**

The Professor should decide the next substantial investment only after both have returned or one produces a decisive answer first.

## Routes not to pursue at initialization

- Do not repeat the closed FA-1f sibling-cancellation mechanism.
- Do not start with local patch consistency weights alone. BABP already has classical self/quasi-duality, and a local positive transfer without a target-level gain would merely repackage known algebra.
- Do not infer finite-seed convergence from linear growth of `|B(t)|` alone; the self-duality test depends on the finite local intersection `B(t) cap B'`.
- Do not treat cancellation or duality as a success condition. They are optional tools only.
- Do not continue BABP merely because work has started. If O1 reveals a materially better target and E2/E3 expose no new handle, pivot.

## Revision note

The principal supplied new tractability evidence after closure of the FA-1f programme: extensive prior ChatGPT work on 1D FA-1f off-equilibrium convergence had not produced a result. The principal also released cancellation/duality as any presumed organizing mechanism and recommended recent progress/open-problem papers for target selection. The FA closure is therefore strengthened, while BABP remains active only as the best current concrete target pending the first obstruction audit and bounded opportunity-cost reconnaissance.
