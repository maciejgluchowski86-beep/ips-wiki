# Proof spine

## Main target

For one-dimensional BABP with branching parameter `lambda>0`, started from any finite nonempty particle set `B`, prove local convergence to Bernoulli equilibrium `pi` with particle density

$$
q=\frac{\lambda}{1+\lambda}.
$$

Begin with `B={0}`. Existing results cover `lambda>0.0347`; the active novelty is the remaining small-parameter range.

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

## E3. Test DFP/quasi-duality against the finite-test observable

Let

$$
F_{B'}(C)=\left(-\frac1\lambda\right)^{|C\cap B'|}.
$$

Find an exact representation, finite linear combination, or controlled approximation of

$$
\mathbf E_B F_{B'}(B(t))
$$

in terms of DFP observables to which Theorem 5.2 applies, or prove that the quasi-duality/thinning family does not span/control this observable with coefficients stable enough for small `lambda`.

Start with `B'={0}` and `B'={0,1}` before attempting general finite sets.

**Status:** open.

**Dependencies:** E0/E1; informed by E2.

**If successful:** this is the preferred theorem route.

**If it fails sharply:** the failure should identify the new one-dimensional lemma needed rather than prompt another algebraic transform.

## E4. New spatial lemma if E3 is insufficient

Only enter this edge after E2/E3 narrow the obstruction. Candidate forms include a local-density/regeneration estimate behind the BABP fronts or a coupling statement strong enough to force the finite-test self-duality observable to equilibrium.

**Status:** not yet formulated. Do not populate with speculative variants before E2/E3 are understood.

## Current first unresolved edge

**E2 and E3 form one reconnaissance bottleneck.** Student B should not merely survey them separately: the point is to decide whether the modern DFP theorem removes the exact historical threshold obstruction.

## Routes not to pursue at initialization

- Do not repeat the closed FA-1f sibling-cancellation mechanism.
- Do not start with local patch consistency weights alone. BABP already has classical self/quasi-duality, and a local positive transfer without a target-level gain would merely repackage known algebra.
- Do not infer finite-seed convergence from linear growth of `|B(t)|` alone; the self-duality test depends on the finite local intersection `B(t) cap B'`.

## Revision note

Initial spine after closure of the FA-1f finite-seed programme. The BABP direction is chosen because the open gap is narrower and stronger all-parameter auxiliary results already exist.
