# Student G Assignment 002 handoff

## Status

Assignment 002 is complete. Six distinct coupling/graphical method entries were staged under `research/active/ergodicity-methods-toolbox/entries/`, one substantive entry per commit. No files under `docs/` and no `mkdocs.yml` files were edited.

## Entries and commits

1. `clan-of-ancestors-perfect-simulation.md` — `ca031862c861c3324bd0d7f69069acd883c74242`.
2. `censoring-monotone-glauber-dynamics.md` — `482f16004d8150ec5846f500d4e58ffa1a2e0035`.
3. `coupling-with-stationarity-local-uniformity.md` — `38cbb3255a0eb9d9c11fbc1a301031a1ece34eec`.
4. `coupling-from-the-past.md` — `eb9b00a72b37c943ca318a2ee2446c2022db2c7a`.
5. `voter-coalescing-random-walk-duality.md` — `07d141028c8a4840ccac11e3a2c0fd60b029cf85`.
6. `dynamical-disagreement-space-time-percolation.md` — `dfcee36e5e8c705f4f2da001c19f7496c9e7e341`.

## Taxonomy decisions

No assigned labels were merged. All six expose distinct proof interfaces.

- **CFTP**, **clan-of-ancestors perfect simulation**, and the already accepted **information-percolation** method remain separate. CFTP proves coalescence of a common backward random map over all initial states. Clan methods instead prove almost-sure finiteness of a backward dependency graph and reconstruct the target forward from its oldest generation; the Fernández--Ferrari--Garcia construction explicitly does not require monotonicity or coupling of trajectories from all initial conditions. Information percolation allows some histories to survive and controls the sparse subset that still carries initial information.
- The fifth requested slot is represented by **coupling with stationarity/local uniformity** rather than by a literal block coupling. Hayes--Vigoda's theorem permits contraction to fail on a small stationary exceptional set and therefore evades worst-case adjacent-pair obstructions of ordinary path coupling. Literal block couplings and maximal local couplings remain legitimate future entries.
- **Dynamical disagreement percolation** remains separate from the accepted static van den Berg--Maes entry. Its proof object is a space-time disagreement path between coupled trajectories, dominated by an oriented percolation/contact-process-type connectivity event.
- **Voter coalescing-walk duality** remains separate from the accepted finite-dual-extinction entry. Voter ancestry need not become empty; loss of information comes from merger of ancestral lineages.

## Source qualifications

### Clan of ancestors

Primary checked source: Fernández, Ferrari and Garcia, *Stochastic Processes and their Applications* 102 (2002), Theorem 1(ii), Sections 4--5, DOI `10.1016/S0304-4149(02)00180-1`. The entry uses their finite-clan criterion and branching/percolation majorant rather than presenting the method as CFTP.

### Censoring

Primary checked source: Peres and Winkler, *Communications in Mathematical Physics* 323 (2013), Theorems 1.1--1.2, DOI `10.1007/s00220-013-1776-0`. The top-state/increasing-density hypotheses are stated explicitly; the entry does not claim censoring for arbitrary chains or arbitrary initial laws.

### Coupling with stationarity

Primary checked source: Hayes and Vigoda, *Annals of Applied Probability* 16 (2006), Theorem 1.2 and coloring application Theorem 1.4, DOI `10.1214/105051606000000330`. This is deliberately not described as ordinary path coupling.

### Coupling from the past

Primary checked source: Propp and Wilson, *Random Structures & Algorithms* 9 (1996), Sections 2, 2.2, 3.1 and 4.1, DOI `10.1002/(SICI)1098-2418(199608/09)9:1/2<223::AID-RSA14>3.0.CO;2-O`. The entry separates exact stationary sampling from an ordinary forward mixing estimate.

### Voter coalescing-walk duality

The theorem-level checked source is Jhon Astoquillca, *Journal of Theoretical Probability* 39 (2026), Article 34, Section 2.1 equations (2.4)--(2.6), Theorem 2.2 and Remark 2.3, DOI `10.1007/s10959-025-01474-1`. This source explicitly formulates the collision-property classification and recovers the classical lattice dimension split. Holley--Liggett (1975) is cited only as the classical origin/history; its full theorem text was not used as the checked primary pinpoint in this batch.

### Dynamical disagreement domination

The fully inspected primary source is Gielis, Maes and Vande Velde, *Annales de l'Institut Henri Poincare, Physique theorique* 70 (1999), 445--472, especially Section 4.1.1 Propositions 1--2, Section 4.1.2(i),(iii), and Theorems 1--2. It explicitly connects the basic coupling of two spin systems to oriented space-time percolation, including a continuous cut-and-arrow contact-process-type comparison. The earlier Gielis--Maes *Communications in Mathematical Physics* 177 (1996), 83--101 spin-flip paper is supplied as a closely related historical/application source, but the 1999 full text carries the primary-checked status here.

## Further uncovered graphical/coupling families

The source search still leaves several distinct method families worth later entries:

- literal **block coupling** or maximal local coupling, where several spins/updates are coupled jointly rather than using equilibrium-typicality as Hayes--Vigoda do;
- **block construction / complete-convergence** arguments using comparison with supercritical oriented percolation;
- **interface or disagreement-front regeneration**, including renewal times or distinguished interfaces that force eventual coupling;
- **Wasserstein/weighted-metric coupling** and Harris-type coupling for infinite-dimensional IPS-like processes;
- **finite-volume to infinite-volume graphical transfer**, where coupling or ancestor estimates uniform in the box control the infinite system;
- **basic/common graphical coupling inequalities** as a dedicated synthesis entry, distinct from attractiveness, path coupling, and disagreement domination;
- model-specific **dual coalescence/annihilation/branching** mechanisms beyond voter and contact-process examples.

## Mechanical validation

The entries were written against the current `entry-template.md` and the mandatory per-entry commit rule was followed. The principal/orchestrator has been running `validate_entries.py` after each commit and reports its output separately; this handoff does not treat that structural validator as a mathematical source audit.
