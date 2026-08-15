# Proof spine

## Main target

Prove ergodicity for the remaining noisy-East region of simple one-sided one-dimensional positive-rate IPS, ultimately completing the positive-rates conjecture for simple IPS.

## E0. Current reduction from prior work

Student A's reconnaissance records the current residual as the noisy-East region left after the principal's recent time-scaling and long-lived-state results.

In simple-IPS transition notation

$$
r_{xy}=P_0(1\mid xy),
$$

positive rates mean

$$
r_{11}<1,\qquad r_{10}<1,\qquad r_{01}>0,\qquad r_{00}>0.
$$

The difficult residual approaches the East boundary

$$
(r_{11},r_{10},r_{01},r_{00})=(0,1,\text{positive},0)
$$

after the available state symmetries/time rescalings.

**Status:** literature/prior-work reduction to be checked directly by Graduate Student C before using exact parameter claims.

## E1. One-site wall obstruction

The existing long-lived-state criterion uses a common state as a spacetime wall. Student A's reconnaissance records the direct obstruction near East.

For wall state `0`,

$$
\beta(0)=1-\max r_{xy}\le1-r_{10},
\qquad
\delta(0)=\max\{r_{00},r_{01}\}\ge r_{01},
$$

so the criterion necessarily fails when

$$
r_{01}\ge\sqrt2(1-r_{10}).
$$

For wall state `1`,

$$
\beta(1)=\min r_{xy}\le r_{00},
\qquad
\delta(1)=\max\{1-r_{10},1-r_{11}\}\ge1-r_{11},
$$

so it necessarily fails when

$$
1-r_{11}\ge\sqrt2 r_{00}.
$$

**Status:** cheap algebraic obstruction from reconnaissance; Student C should rederive from the exact theorem convention.

## E2. Two-site agreed-block falsification test

Replace the one-site common-state wall by a block of two sites on which the two canonical-coupling copies agree.

Condition on the influencing exterior state adversarially. Build the finite disagreement/agreement Markov chain while the block is intact. Kill when disagreement crosses the block from the influencing side before the block regenerates to full agreement.

The first object to compute is the exact crossing-versus-regeneration operator or next-generation factor `R_2(r)`.

Questions:

1. Is `R_2(r)<1` anywhere outside the known one-site region?
2. Does `R_2(r)<1` uniformly throughout the full residual noisy-East region?
3. What is the asymptotic behavior of `R_2(r)` approaching the East boundary with positive noise?
4. If `R_2(r)>=1` there, is the failure caused by a specific local cycle that persists for all fixed block lengths?

**Status:** first active edge.

## E3. Structural theorem if the two-site test is positive

A favorable finite calculation is not itself a project result under the standing novelty standard. If E2 is positive, the next theorem must explain why block regeneration controls the infinite process.

Candidate structural statement:

> There exists a block length or block-renewal construction, selected from the model parameters by an explicit rule, whose disagreement-crossing reproduction factor is uniformly below one throughout the residual positive-rate region; consequently disagreements die out and the IPS is ergodic.

The proof would need a legitimate concatenation/renewal argument, not only a better finite constant.

**Status:** conditional on E2.

## E4. Structural obstruction if finite walls fail

If E2 exposes a cycle or asymptotic mechanism forcing the crossing factor to one or above near East, test whether it persists for every fixed block length.

A theorem of the form

> no finite agreed-block wall can give a uniform subcritical disagreement reproduction bound arbitrarily close to the East boundary

would be a genuine structural negative result about this proof mechanism and would force a different route.

**Status:** alternate branch after E2.

## Current first unresolved edge

Exact two-site agreed-block killed-chain calculation under the canonical coupling, with all conventions checked against the principal's current papers.

## Novelty guardrail

Do not turn this into a sequence `block length 2,3,4,...` whose only output is a gradually improved numerical region. Larger blocks are permitted as diagnostics, but a qualifying project result must be structural under the standing novelty standard in `CHATGPT.md`.