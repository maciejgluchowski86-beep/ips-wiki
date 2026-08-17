# 010d: Potts prior work and application-value ruling

Date: 2026-08-17

This note executes Assignment 010 Part E after the exact negative positivity verdict in `010c`.

## 1. The selected dynamics is standard, not project-designed

The selected model is the ordinary zero-field ferromagnetic Potts model with single-spin Metropolis Glauber dynamics.

Bet--Gallo--Nardi (2021) explicitly formulate the q-state zero-field ferromagnetic Potts model on periodic grid graphs with Hamiltonian

\[
H(\sigma)=-J\sum_{\{v,w\}}\mathbf 1\{\sigma(v)=\sigma(w)\},
\]

and single-spin Metropolis transition probability proportional to

\[
\exp\{-\beta[H(\sigma')-H(\sigma)]_+\}
\]

when the two configurations differ at one site. They study critical configurations and tubes of typical tunneling trajectories. Nardi--Zocca (2019) study tunneling and mixing-time asymptotics for the same zero-field Potts Metropolis dynamics. Bet--Gallo--Kim (2023) treat a three-state Potts model with general interactions under a Glauber-type single-spin dynamics.

Thus neither the three-state model nor the Metropolis local rule is introduced by this programme.

## 2. Existing Potts dynamics literature is already substantial

The Potts Glauber literature contains strong results by methods unrelated to the present patch representation, including:

- metastable/tunneling transition times, critical gates and typical paths in low-temperature Metropolis dynamics;
- rapid- and slow-mixing regimes using path coupling, block dynamics, conductance and comparison arguments;
- critical two-dimensional mixing results and cluster/random-cluster representations for Potts equilibrium and dynamics.

For example, Bordewich--Greenhill--Patel (2016) prove rapid/slow mixing results for ferromagnetic Potts Glauber dynamics using coupling and block-dynamics techniques. Gheissari--Lubetzky (2017) analyze mixing of critical two-dimensional Potts models. These are established model-specific frameworks and are not consequences of the typed patch construction.

## 3. What the typed killed representation does differently

The exact specialization in `010b` is not a deterministic recoloring-arrow representation. For the singleton source-type-1/target-type-1 successful record,

\[
\mathbf a_{1;1,0}
=
\left(
qz^2(1-z^2),
q(z-1)(z^3+z^2-1),
-qz^2(1-z^2)
\right),
\]

so at every finite positive inverse temperature the coarse successful record hides at least two possible post-source outcomes with positive absolute branch rates.

Moreover, typed target patterns can conflict with active labels and hit cemetery. Hence the Assignment-002 killed/noncemetery factorization is genuinely operative and is not merely a rewriting of a deterministic voter/cyclic invasion graph.

A targeted search did not identify a published Potts duality/graphical construction that already contains this particular signed hidden-outcome plus cemetery-aware patch factorization. This is consistent with, but does not strengthen beyond, Assignment 008's programme-level `plausibly new` status for the general killed typed interface. Absence from this bounded search is not a historical-priority proof.

## 4. Why there is nevertheless no positive Potts application theorem

The same nontrivial hidden geometry produces a realized negative short `OO` patch:

\[
a_1^2(\tau)=-qz^2(1-z^2)<0
\qquad(0<z<1).
\]

Therefore typed bulk patch positivity fails throughout the interacting finite-temperature regime. The patch-positive comparison/convergence machinery cannot be invoked.

Consequently this block does **not** claim:

- a new Potts duality theorem;
- a new mixing or metastability theorem;
- a new invariant-measure or convergence result;
- a model-specific monotonicity theorem.

The useful output is instead the exact classification of why the positivity layer fails in a genuinely active-to-active, non-deterministic-hidden-mark model.

## 5. Distinction from Assignment 009

Assignment 009's two-stage/SIRS obstruction arose in vacancy/birth architectures: a target mode increased `0->r` while contributing nothing to any active-source transition into `r`.

The Potts failure has the same algebraic short-`OO` template but a different physical source. Here **every** color is active and every directed color replacement has positive physical rate. For the decisive target mode,

\[
\widehat c^{0\to1}(\tau)>0,
\qquad
\widehat c^{2\to1}(\tau)=0,
\]

because the active-source `2->1` Metropolis transition is already at the acceptance ceiling and therefore has zero first target-mode increment.

Thus the broader lesson is not merely “catalytic births fail.” It is:

> typed patch positivity is locally obstructed whenever one source state's response to a target mode is strictly smaller than the reference source response, producing a negative hidden active-outcome coefficient that can feed a subsequent outgoing record.

This is the general short-`OO` contrast lemma proved in `010c`.

## 6. Application ruling

The selected model genuinely exercises the surviving killed typed representation but fails typed bulk patch positivity exactly and throughout its interacting finite-temperature regime.

The correct Assignment-010 outcome is therefore

\[
\boxed{\texttt{STOP-SECOND-APPLICATION-POSITIVITY-FAILS}.}
\]

This is not `STOP-SECOND-APPLICATION-ONLY-KNOWN-DUALITY`: the failure occurs after the hidden-mark honesty gate has passed, not because the model collapses to a standard deterministic dual.

No third application family should be opened automatically, and generic `d>3` positivity algebra remains outside this block.

## Sources

- G. Bet, A. Gallo and F. R. Nardi, *Critical Configurations and Tube of Typical Trajectories for the Potts and Ising Models with Zero External Field*, Journal of Statistical Physics 184 (2021), Article 30, DOI 10.1007/s10955-021-02814-1.
- F. R. Nardi and A. Zocca, *Tunneling behavior of Ising and Potts models in the low-temperature regime*, Stochastic Processes and their Applications 129 (2019), 4556--4575, DOI 10.1016/j.spa.2018.12.001.
- G. Bet, A. Gallo and S. Kim, *Metastability of the three-state Potts model with general interactions*, Electronic Journal of Probability 28 (2023), article 112/117 depending database formatting, DOI 10.1214/23-EJP1003.
- M. Bordewich, C. Greenhill and V. Patel, *Mixing of the Glauber dynamics for the ferromagnetic Potts model*, Random Structures & Algorithms 48 (2016), 21--52.
- R. Gheissari and E. Lubetzky, *Mixing times of critical 2D Potts models*, Communications on Pure and Applied Mathematics 71 (2018), 994--1046.
