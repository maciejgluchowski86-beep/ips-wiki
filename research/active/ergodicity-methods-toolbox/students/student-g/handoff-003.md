# Student G Assignment 003 handoff

## Status

Assignment 003 is complete. Seven graphical/coupling entries were staged under `research/active/ergodicity-methods-toolbox/entries/`, with one substantive entry per commit. No file under `docs/` and no `mkdocs.yml` file was edited.

## Entries and commits

1. `block-coupling-joint-resampling.md` — `a05807ce37cde96a83497cf8d54b65b00b99b620`.
2. `supercritical-block-construction-complete-convergence.md` — `b6be0525a7f7bed753aa230bbe16b9e8475c7d32`.
3. `front-regeneration-renewal-times.md` — `a5a0c86cf0f9f2fd39a7123cabddf1c8a7d5b92c`.
4. `weighted-wasserstein-contraction-infinite-ips.md` — `050a22f44d4dbeecb377487d6056d9482f344ba7`.
5. `finite-speed-finite-volume-transfer.md` — `8f397e3272be149beb1d703f748ec2ce6cfe465e`.
6. `refined-discrepancy-coupling-general-exclusion.md` — `ff73b5867abeb1cd0a89a8dc68ed9ae5937aa394`.
7. `parity-duality-branching-annihilating.md` — `537a9c129fadc239450309a1f6daf0ac2c154b2a`.

## Taxonomy and substitution decisions

### Literal block coupling retained as distinct

Felsner--Heldt--Roch--Winkler explicitly introduce an auxiliary chain that resamples an entire block because direct coupling of the original one-site up/down chain does not give the needed contraction. Conditional block fillings are coupled monotonically and their expected discrepancy is measured by a block-divergence quantity; only after proving contraction of the block chain do they compare it back to local updates. This is genuinely different from the live one-site path-coupling page and from Hayes--Vigoda equilibrium-typicality coupling.

### Supercritical block construction stays separate from subcritical disagreement domination

Sturm--Swart Theorem 5 constructs a coarse good-block process for the ADBARW that contains oriented percolation. Section 4.2 chooses the percolation parameter above its survival threshold and uses this persistent coarse structure in the complete-convergence theorem. The direction of comparison and conclusion are therefore the opposite of the live dynamical-disagreement page, where a dominating space-time process must be subcritical and die.

### Front regeneration is a renewal interface, not CFTP or East screening

Jara--Moreno--Ramírez construct regeneration times for a propagating reactive exclusion front. The post-regeneration process has a translated conditional restart law and successive regeneration increments are independent, giving renewal-theoretic convergence of the environment seen from the front. There is no backward random-map coalescence, and the front mechanism is not the distinguished-zero equilibrium-screening argument used for East.

### Weighted Wasserstein contraction is beyond finite Hamming path coupling

Bezborodov--Di Persio--Friesen--Kuchling work on a countable-site continuous-spin state space with weighted `l1` norm. Their effective-drift inequality produces exponential `W1` contraction for arbitrary finite-first-moment laws and therefore a unique invariant law. The state space may have infinitely many active coordinates, so the proof interface is genuinely different from finite-state Hamming path coupling.

### Finite-to-infinite graphical transfer is an actual relaxation step

Cancrini--Martinelli--Roberto--Toninelli Section 8 does more than construct the infinite process as a finite-volume limit. For a local observable and a box of size proportional to time, equation (8.1) splits infinite-volume variance into a common-clock finite-speed restriction error and a finite-volume relaxation term; (8.2) makes the first exponentially small and Lemma 8.1 controls the second. This directly proves their infinite-volume Theorem 4.2.

### Basic/common graphical coupling slot substituted

I did **not** create a generic basic/common graphical-coupling entry. The primary sources found for the usual common-clock/basic discrepancy estimate did not expose a proof interface distinct from the already live attractiveness, Dobrushin/path-coupling, and dynamical-disagreement pages.

The replacement is `refined-discrepancy-coupling-general-exclusion.md`. Gobron--Saada prove that for configuration-dependent exclusion the ordinary basic coupling is generally not attractive; Theorem 2.13 and Proposition 3.30 instead engineer non-diagonal coupled transition rates, allowing different microscopic jumps in the two marginals while making the discrepancy count nonincreasing. Proposition 3.36 and Theorem 2.15 add discrepancy elimination/irreducibility and classify extremal translation-invariant invariant laws. This is a concrete coupling-construction technique beginning precisely where basic coupling fails.

### Branching-annihilating parity duality stays separate from finite-dual extinction and voter coalescence

The Sturm--Swart parity dual is a branching-annihilating system that can survive and grow. Theorem 3 identifies the unique homogeneous coexisting invariant law and convergence by combining parity duality with extinction-versus-unbounded-growth, not by killing all ancestors. It is therefore distinct from both the live contact-type finite-dual-extinction entry and voter coalescing-walk duality. It shares a primary paper with the supercritical block-construction entry because that paper uses two genuinely different proof interfaces: oriented-percolation renormalization establishes a survival regime, while parity duality converts branching-annihilating growth into invariant-law identification.

## Source qualifications

### Block coupling

Primary checked source: Stefan Felsner, Daniel Heldt, Sandro Roch and Peter Winkler, *Block coupling and rapidly mixing k-heights*, arXiv:2410.08992 (2024), DOI `10.48550/arXiv.2410.08992`. Checked pinpoints: Theorem 1, Sections 2.3--2.4 and 3.2, Theorems 6--8. This is currently a preprint; the entry labels it as such.

### Supercritical block construction / complete convergence

Primary checked source: Anja Sturm and Jan M. Swart, *Voter models with heterozygosity selection*, Ann. Appl. Probab. 18 (2008), 59--99, DOI `10.1214/07-AAP444`. Checked pinpoints: Theorem 5 and Section 2.3 for oriented-percolation domination; Theorem 4 and Section 4.2 for complete convergence.

### Front regeneration

Primary checked source: Milton Jara, Gregorio Moreno and Alejandro F. Ramírez, *Front Propagation in an Exclusion One-dimensional Reactive Dynamics*, Markov Process. Related Fields 14 (2008), 185--206; stable arXiv identifier `math/0703173`. Checked pinpoints: Theorems 1--2, Section 2.4, Propositions 1, 3 and 4, Section 3. The journal page independently confirms volume/issue/pages.

### Weighted Wasserstein contraction

Primary checked source: Viktor Bezborodov, Luca Di Persio, Martin Friesen and Peter Kuchling, *Interacting particle systems with continuous spins*, arXiv:2308.07838 (2023), DOI `10.48550/arXiv.2308.07838`; the authors list it as forthcoming in Annales de l'Institut Henri Poincare, Probabilites et Statistiques. Checked pinpoints: Theorems 1.1--1.2, equation (1.5), Section 7, Example 2.3. The entry relies on the arXiv version actually inspected rather than on an uninspected final pagination.

### Finite-speed finite-volume transfer

Primary checked source: Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto and Cristina Toninelli, *Kinetically Constrained Lattice Gases*, Comm. Math. Phys. 297 (2010), 299--344, DOI `10.1007/s00220-010-1038-3`. Checked pinpoints: Theorem 4.2 and Section 8, especially equations (8.1)--(8.2) and Lemma 8.1.

### Refined discrepancy coupling

Primary checked source: Thierry Gobron and Ellen Saada, *Couplings and attractiveness for general exclusion processes*, Ensaios Matemáticos 38 (2023), 263--313, DOI `10.21711/217504322023/em3810`, with arXiv version `2302.00971`. Checked pinpoints: Theorems 2.9, 2.13 and 2.15; Propositions 3.30 and 3.36; Section 4. The entry does not claim global uniqueness across conserved densities: Theorem 2.15 gives the ordered one-parameter classification of extremal translation-invariant invariant laws, hence uniqueness only after the density parameter is fixed within that class.

### Parity branching-annihilating duality

Primary checked source: Sturm--Swart as above. Checked pinpoints: Section 2.1, equations (1.8) and (2.4)--(2.8), Theorem 3, Theorem 12 and Section 3.5. The entry carefully states uniqueness of the homogeneous **coexisting** invariant law, not uniqueness of all invariant laws; absorbing constant laws remain.

## Further uncovered graphical/coupling families

The search still suggests several potentially distinct later entries:

- **successful coupling of finite dual particle systems**, where two copies of an interacting dual are coupled until they agree and this is used to classify invariant measures, rather than relying on extinction or parity growth;
- **second-class-particle / shock coupling** as a reusable interface for conservative IPS when a distinguished discrepancy has its own stochastic dynamics;
- **literal maximal local coupling for nonmonotone spin systems** beyond the block-resampling method recorded here;
- **regeneration of disagreement interfaces or competition fronts** in systems where the renewal object is a coupling discrepancy rather than a physical reaction front;
- **block construction for complete convergence in contact/multitype systems** where the percolation comparison is combined with restart arguments but not with the parity-duality mechanism of Sturm--Swart;
- **nonmonotone Wasserstein couplings** using reflection, synchronous-plus-jump coupling, or concave/weighted transport costs in infinite interacting systems;
- **projective graphical transfer uniform in boundary conditions** that yields uniqueness from finite-volume coupling estimates, distinct from the equilibrium semigroup-transfer example recorded here.

A dedicated generic `basic graphical coupling` page remains unearned by the sources checked in this wave: at present it would synthesize already-live interfaces rather than add a new one.

## Mechanical validation

All seven entries were written against the current `entry-template.md` and committed separately. `validate_entries.py` remains the principal/orchestrator's structural check; this handoff does not treat validator success as mathematical or attribution verification.