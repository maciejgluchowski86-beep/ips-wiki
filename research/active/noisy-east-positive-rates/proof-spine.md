# Proof spine

## Main target

Prove ergodicity for the remaining noisy-East region of simple one-sided one-dimensional positive-rate IPS, ultimately completing the positive-rates conjecture for simple IPS.

## E0. Residual noisy-East reduction

The 2025/2026 Głuchowski--Menz papers reduce the unresolved simple-IPS positive-rates problem to a region adjacent to the East boundary after time scaling and state symmetries. On the normalized face used in Student C's first calculation,

$$
r_{xy}=P_0(1\mid xy),\qquad r_{11}=0,
$$

and the difficult region approaches the East corner with `r10` near one and `r00,r01` small.

**Status:** source-checked for assignment 001 at the level needed to validate its strict residual path. Assignment 002 must state the full normalized residual set and East boundary exactly before making a regime-wide claim.

## E1. One-site wall mechanism

The long-lived-state theorem supplies ergodicity under

$$
\delta(a)<\sqrt2\,\beta(a).
$$

Near the residual East region neither state supplies a sufficient one-site wall. Student C independently reproduced the one-site obstruction from the source convention.

**Status:** established prior-work mechanism and calibrated obstruction.

## E2. Two-site agreed-block test

Student C constructed the exact killed two-site excursion under the canonical coupling. The Professor independently reconstructed it.

On

$$
r_{11}=0,\qquad
r_{10}=1-\varepsilon^2,\qquad
r_{01}=\frac\varepsilon2,\qquad
r_{00}=\varepsilon,
$$

which lies strictly in the unresolved region for small positive `epsilon`,

$$
\rho_2(\varepsilon)\to1,
\qquad
F_2(\varepsilon)\to1.
$$

At the limiting East rule, the failure is a deterministic local cycle: an exterior disagreement creates boundary orientation `10`, which survives boundary updates and crosses on the next protected-site update.

**Status:** two-site wall rejected as an East-stable contraction mechanism.

## E3. Length-three persistence diagnostic

The proposed inference from E2 to all fixed finite block lengths is false on the same path.

The exact 24-state length-three killed chain, maximized over all eight fully agreed words and both exterior disagreement orientations, satisfies

$$
\lim_{\varepsilon\downarrow0}R_3^{\rm adv}(\varepsilon)=\frac9{10}.
$$

The Professor independently rebuilt both exterior orientations and obtained the conditional limits

$$
\frac{43}{75},\quad\frac45,\quad\frac{19}{30},\quad\frac9{10}
$$

for the four agreed words ending in one, while the four words ending in zero have vanishing attack probability.

**Status:** verified diagnostic for proof-spine use. Not a project result under the standing novelty standard.

## E4. Current structural diagnostic: uniform three-site characterization

Let `R` be the exact normalized residual set and `partial_E R` its East boundary. For each parameter point define

$$
R_3^{\rm adv}(r)
$$

as the unconditional one-attack crossing probability maximized over all fully agreed three-site words and both exterior disagreement orientations.

The current question is

$$
\sup_{\bar r\in\partial_E R}
\limsup_{\substack{r\to\bar r\\r\in R}}
R_3^{\rm adv}(r)<1\ ?
$$

This requires a full piecewise-algebraic analysis of the canonical coupling across the actual residual region, not another sampled path.

**Owner:** Graduate Student C, assignment `students/student-c/assignment-002.md`.

## E5. Structural theorem required if E4 is positive

A uniform local gap at length three would still not prove ergodicity.

The missing theorem must convert a local adversarial block-crossing bound into extinction of disagreements in the infinite canonical coupling. A valid theorem must handle at least:

- exterior states changing during a block excursion;
- repeated attacks on a regenerated block;
- overlap between neighboring blocks;
- dependence between successive regeneration/crossing events;
- the relation between the local reproduction quantity and the global disagreement fronts used in the one-site proof.

A favorable fixed-block constant without this concatenation theorem is not a project result.

## Pre-committed finite-wall stop rule

Meeting 001 fixed the following opportunity-cost rule before E4 is solved.

If there exists a genuine residual sequence approaching the East boundary with

$$
R_3^{\rm adv}(r_n)\to1,
$$

the finite-wall route is closed for this programme. **Do not respond by computing length four.** This does not prove all longer blocks fail; it says the group will not pursue a block-by-block rescue without a separate structural theorem predicting it.

Even if E4 gives a uniform gap, close the finite-wall route if the frozen-exterior factor cannot be upgraded to a rigorous dynamic block-renewal domination without introducing an uncontrolled stronger quantity.

## Novelty guardrail

Block lengths two and three are diagnostics. The standing novelty standard rules out a sequence of larger block calculations as a contribution. A qualifying result must be structural: a regime-wide theorem about the wall mechanism, a valid renewal theorem yielding new ergodicity, a structural impossibility theorem, or another genuinely new mechanism.

## Current first unresolved edge

**E4: exact uniform characterization of the length-three adversarial factor over the full residual East-boundary regime.**