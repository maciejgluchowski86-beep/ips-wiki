# Group meeting 003: G wave one source-audited; joint first-wave taxonomy locked

Date: 2026-08-17

Professor review of Student G's six first-wave staged entries, the principal's 12-entry mechanical-validator report, Student G's handoff/source qualifications, Student F's six entries already accepted in Meeting 002, and the cited primary-source material.

## Ruling

All six G-wave-one entries are **accepted for later live-wiki integration**:

1. `attractive-monotone-coupling-extremal-laws.md`;
2. `dobrushin-influence-contraction.md`;
3. `path-coupling-glauber-dynamics.md`;
4. `disagreement-percolation-gibbs-uniqueness.md`;
5. `duality-extinction-finite-ancestor-process.md`;
6. `information-percolation-backward-histories.md`.

Together with the six F-wave-one entries accepted in Meeting 002, the first wave now contains twelve source-audited methods. The principal reports that `validate_entries.py` passes all twelve; that remains a structural check only.

## 1. Source audit

### Attractive monotone coupling and extremal laws

Accepted at the scope stated. Warfheimer Definition 2.1 gives the standard attractiveness inequalities for binary spin systems. The paper explicitly constructs lower and upper stationary limits by monotonicity, and Theorem 2.2 proves that, for the one-dimensional spin system in a uniquely ergodic evolving background under its positivity condition, these are the only extremal stationary laws. Section 3 gives the explicit maximal-type ordered coupling. The entry correctly treats attractiveness as a reduction: equality of lower and upper laws is additional mathematics.

The attribution qualification in G's handoff is correct. The checked source is Warfheimer's primary formulation; its attribution of the no-background theorem to Liggett is not silently promoted into an independently checked priority claim.

### Dobrushin influence contraction

Accepted. Dyer--Goldberg--Jerrum define dependency matrices by single-site conditional influences. Their Corollary 18 gives, under the Dobrushin column-sum condition `||R||_1 <= mu < 1`, the random-update Glauber bound

$$
\tau_r(\varepsilon)\le \frac{n}{1-\mu}\log\frac{n}{\varepsilon}.
$$

Section 3.2, especially Lemmas 28--30, gives exactly the coordinate-oscillation propagation mechanism used in the entry. Example 2 supplies the stated graph-colouring calibration.

### Path coupling

Accepted as a separate method. Dyer--Goldberg--Jerrum Section 3.1 proves its random-update spin-system estimate by path coupling; Lemma 17 extends contraction from one-coordinate differences along a path to arbitrary configurations. The entry's generic local-contraction formulation is the standard path-coupling architecture, while the checked theorem-level spin implementation is the Dyer--Goldberg--Jerrum source. Bubley--Dyer is identified as the origin source but is not represented as having been independently source-checked in this batch.

The shared Dyer--Goldberg--Jerrum primary source with the Dobrushin entry is intentional. The proof interfaces differ: path coupling propagates a metric coupling from adjacent state pairs, whereas Dobrushin propagates a vector seminorm of observable sensitivities. The source itself presents the two derivations separately in Sections 3.1 and 3.2.

### Disagreement percolation

Accepted. Van den Berg--Maes Theorem 1 constructs a coupling whose disagreement indicators are dominated by independent Bernoulli variables and in which every interior disagreement is connected to the boundary disagreement set. Corollary 1 turns this into a boundary-effect estimate, and Corollary 2 proves uniqueness whenever the dominating site-percolation field does not percolate; in particular `sup_i p_i < p_c` suffices. Example 1 gives the hard-core threshold `a < p_c/(1-p_c)` exactly as stated.

The entry correctly labels this as a **static Gibbs-uniqueness method**, not a dynamical coupling theorem. A space-time disagreement/contact-process domination will therefore remain a separate future entry.

### Duality plus extinction of a finite ancestor process

Accepted. Remenik Proposition 2.2 gives the graphical self-duality when the environment starts at equilibrium. Taking a finite occupied set yields condition (S1), which is explicitly equivalent to nontriviality of the upper invariant law. Hence extinction from every finite nonempty dual set collapses the upper invariant law to the lower one. Theorem 2 is the stated complete-convergence theorem. The entry correctly records the dependence on a useful law-determining duality and does not reverse the implication in arbitrary models.

The corrected arXiv version is an appropriate source; the correction concerns a different theorem and does not alter the duality/complete-convergence statements used here.

### Information percolation

Accepted. Lubetzky--Sly define the minimal backward update support, then Definition 2.3 classifies the resulting space-time clusters as red, blue and green. Conditional on the green histories, the blue spins form the initial-state-independent background while the red set carries the surviving initial information. Their equation (2.7), based on the Miller--Peres $L^2$ estimate, uses the conditional exponential intersection moment of two independent red sets as the mixing criterion. Theorem 1 applies the framework to continuous-time Ising Glauber dynamics on the torus throughout `beta < beta_c` and obtains cutoff with an `O(1)` window.

G's taxonomy warning is accepted: information percolation is not coupling from the past and not a clan-of-ancestors perfect-simulation criterion. It can prove mixing while some histories still reach time zero.

## 2. Joint first-wave taxonomy

The twelve accepted entries are organized by **proof interface**, not by source, historical school, or conclusion alone.

### A. Coupling and local influence

- attractive monotone coupling and extremal laws;
- Dobrushin influence contraction;
- path coupling.

### B. Spatial mixing and boundary influence

- disagreement percolation for Gibbs uniqueness;
- Dobrushin--Shlosman spatial mixing to dynamical relaxation.

### C. Functional inequalities and comparison

- Poincare / spectral gap;
- logarithmic Sobolev and modified logarithmic Sobolev inequalities;
- Dirichlet-form / canonical-path comparison;
- block dynamics and bisection variance decomposition.

### D. Graphical ancestry, duality and regeneration

- duality plus extinction of a finite ancestor process;
- information percolation and backward histories;
- East distinguished-zero screening.

This is the ordering to use for the first live `Ergodicity methods` hub. The hub should state explicitly that the categories overlap and that an entry is filed by its load-bearing proof object. Shared sources are not grounds for merging distinct proof interfaces.

## 3. Cross-linking and deduplication rules for promotion

When the staged entries are promoted:

- Poincare should link to LSI/mLSI, Dirichlet comparison and block/bisection as ways of proving coercivity rather than re-explaining each;
- LSI/mLSI should link to Dobrushin--Shlosman as one spatial route to a uniform functional inequality;
- Dobrushin influence and path coupling should cross-link and state their different state-space objects;
- disagreement percolation should link to Dobrushin influence only as a contrasting geometric uniqueness criterion and should not be presented as dynamical;
- information percolation should remain separate from future CFTP and clan-of-ancestors pages;
- East distinguished-zero screening should link to Poincare because the cited nonequilibrium convergence theorem imports the East spectral gap.

Self-containedness still permits short restatements of standard definitions; the goal is to remove duplicated derivations, not all repetition.

## 4. Live-wiki integration timing

The first twelve entries are now **mathematically and taxonomically cleared for live-wiki promotion**. They are not promoted in this meeting because F is actively committing Assignment 002 and G is about to begin Assignment 002 on the same branch. Avoid a large batch of `docs/` commits while student writes are in flight. At the next quiet integration window, promote the accepted set under:

- `docs/ergodicity-methods.md`;
- one `status: literature`, `audit: current` page per method in `docs/entries/`;
- a top-level `Ergodicity methods` section in `mkdocs.yml` using the taxonomy above.

This is an operational delay only; no further mathematical audit of these twelve is required unless a later source conflict appears.

## 5. Student G continuation

G has cleared Assignment 001. Assignment 002 opens immediately on six distinct graphical/coupling gaps:

1. dynamical disagreement domination by a contact or oriented-percolation process;
2. coupling from the past;
3. clan-of-ancestors / perfect simulation via finite backward dependency clans;
4. censoring inequalities for monotone spin-system dynamics;
5. block, local or maximal coupling methods that are genuinely stronger than one-site path coupling;
6. coalescing-random-walk duality and clustering/convergence in voter-type systems.

CFTP, clan-of-ancestors and information percolation must remain separate unless the primary sources themselves force a merger.

## 6. Current work status

- Student F: active on Assignment 002.
- Student G: active on Assignment 002.
- Twelve first-wave entries accepted and queued for the next quiet live-wiki integration window.
