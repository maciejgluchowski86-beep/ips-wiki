# 010a: literature-driven selection of a structurally distinct application

Date: 2026-08-17

This note executes Assignment 010 Part A. The selection below is frozen **before the typed patch-positivity calculation**. Positivity is not a selection criterion.

## 1. Candidate 1: three-state ferromagnetic Potts Metropolis dynamics

Take the ordinary three-state ferromagnetic Potts model with colors `0,1,2` and nearest-neighbour Hamiltonian

\[
H(\eta)=-J\sum_{\{x,y\}}\mathbf 1\{\eta_x=\eta_y\},\qquad J>0.
\]

The standard single-spin Metropolis Glauber rule is: propose a new color at one site and accept it with probability

\[
\exp\{-\beta[H(\eta^{x\to y})-H(\eta)]_+\}.
\]

Nardi--Zocca (2019) and Bet--Gallo--Nardi (2021) study the zero-field Potts model under this single-spin Metropolis Glauber dynamics; Bet--Gallo--Kim (2023) likewise study a three-state general-interaction Potts model and explicitly specify the one-spin Metropolis rule. The continuous-time IPS version is the standard Poissonization of the same local rule: each site receives proposal clocks and an accepted proposal performs one single-site replacement. Multiplying all rates by a common proposal-clock factor only rescales time and will be kept explicit below.

Why this is a strong Assignment-010 candidate:

- all three colors are dynamically and observably equivalent in the zero-field model;
- every physical event changes exactly one site;
- already-active colors replace one another directly;
- the acceptance probability depends on the **source color** and on the local neighborhood through an energy difference, rather than being a deterministic voter-copy arrow or a source-independent heat-bath reset;
- there is no vacancy/birth architecture, so Assignment 009's contact/SIRS catalytic-birth interpretation does not decide the model before calculation;
- the model is classical and extensively studied for tunneling, coarsening, mixing and metastability, so it is not being introduced to fit the patch criterion.

The published model is irreducible at finite inverse temperature on a finite connected graph, but irreducibility plays no role in this selection.

## 2. Candidate 2: three-color cyclic particle system

Bramson--Griffeath's cyclic particle system has colors `0,1,2` (more generally `0,...,N-1`) and continuous-time nearest-neighbour invasion. In the three-color case, a color `i+1 mod 3` individual paints a neighboring color `i` site with its color. Equivalently, a site in state `i` changes to `i+1 mod 3` at a rate proportional to the number of neighboring sites in state `i+1 mod 3`.

This is also:

- genuinely three-state;
- continuous-time;
- single-site replacement;
- purely active-to-active neighbor-driven retyping;
- nonirreducible, with nontrivial clustering/fixation theory depending on the number of colors.

It is nevertheless a weaker test of the surviving novelty anchor. Its basic graphical event is an exposed deterministic invasion arrow: once source and target colors are known, the physical post-update color is known. The standard graphical construction is therefore much closer to the deterministic voter/cyclic-arrow picture explicitly flagged in Assignment 010 Part D. This does not prove that its indicator-basis signed dual is trivial, but it makes it substantially less informative as a first test of whether **hidden** post-source randomness and cemetery-aware averaging matter.

## 3. Selection ruling

The selected model is

\[
\boxed{\text{three-state ferromagnetic Potts model with Metropolis single-spin Glauber dynamics}.}
\]

The selection is based on:

1. mathematical naturality and a substantial published literature;
2. genuine three-state local physics;
3. exact single-site replacement structure;
4. active-to-active neighbor-sensitive retyping;
5. source-dependent local transition probabilities, giving a materially better chance to exercise nontrivial hidden signed outcomes than deterministic invasion/copy rules.

No typed coefficient row, transfer matrix or patch-positivity inequality was used to choose between the candidates.

## 4. Frozen specialization for Part B

For the exact local calculation, use the standard zero-field three-state Potts interaction on the square lattice, with four nearest neighbors, matching the grid-graph setting of the cited Potts metastability literature. Let

\[
z=e^{-\beta J}\in(0,1]
\]

and let `q>0` denote the common proposal-rate prefactor for each alternative target color. If the source color is `x`, the proposed target is `y!=x`, and `n_a` is the number of nearest neighbors of color `a`, then the continuous-time replacement rate is

\[
\boxed{c^{x\to y}(n_0,n_1,n_2)=q\,z^{(n_x-n_y)_+}.}
\]

The exact value of `q` only rescales all local clocks. The published discrete-time rule corresponds, after Poissonization, to a fixed common `q`; no relative transition rate is changed.

Reference state `0` is fixed now. Because of color symmetry this choice has no positivity advantage over references `1` or `2`.

## Sources

- F. R. Nardi and A. Zocca, *Tunneling behavior of Ising and Potts models in the low-temperature regime*, Stochastic Processes and their Applications 129 (2019), 4556--4575.
- G. Bet, A. Gallo and F. R. Nardi, *Critical Configurations and Tube of Typical Trajectories for the Potts and Ising Models with Zero External Field*, Journal of Statistical Physics 184 (2021), Article 30.
- G. Bet, A. Gallo and S. Kim, *Metastability of the three-state Potts model with general interactions*, Electronic Journal of Probability 28 (2023), paper 117.
- M. Bramson and D. Griffeath, *Flux and fixation in cyclic particle systems*, Annals of Probability 17 (1989), 26--45.
