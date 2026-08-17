# Student G Assignment 006 handoff

## Status

Assignment 006 is complete. Three source-led method entries survived primary-source inspection and were staged under `research/active/ergodicity-methods-toolbox/entries/`, one substantive entry per commit. The fourth named family, Gray's 1986 general attractive-spin duality, was not turned into an entry because I could access the official article metadata and abstract but not the primary full theorem/proof text needed to satisfy `source_status: primary-checked` at the programme's exact-pinpoint standard.

This is a source-access limitation, not a negative taxonomy ruling on Gray 1986 and not a decision to merge it with Gray 1982.

No file under `docs/` and no `mkdocs.yml` file was edited.

## Entries and commits

1. `toom-error-graph-expansion-pca.md` — `79c3a08b96b53919e0b0a1bd3ffc7e373c054541`.
2. `essential-hitting-time-almost-subadditive-growth.md` — `6a169bf09b9a30bc75502e632e1302a7d6bd5419`.
3. `one-dimensional-edge-coalescence-positive-rates.md` — `2dddd6a1bfa16bf365f4907418e4093c74d06500`.

All three committed entry files were fetched back from GitHub after writing. No control-character or escaped-backslash corruption was visible; in particular, the entries avoid fragile LaTeX control sequences where plain notation suffices.

## Taxonomy decisions

### Gray 1982: edge processes are the extra mechanism beyond attractiveness

The 1982 primary paper is now fully inspectable. The entry is not a duplicate of the live attractive/extremal-law page. Gray first puts all initial states on a common Harris construction and attaches left and right **edge processes** to half-line initial conditions. Properties E1-E3 identify the half-line process as a hybrid of the upper and lower extremal copies on opposite sides of its edge; Proposition 2 propagates extremal-copy agreement inside a separated left/right edge pair.

The decisive one-dimensional mechanism is then edge ordering and coalescence. E4 prevents crossings and E5 makes a collision permanent. The Section 2 Lemma shows that neighboring edges coalesce asymptotically and that edges leave any fixed window. Its proof uses periodicity plus the spatial ergodic theorem: a hypothetical positive density of surviving distinct edges would force a positive density of bounded gaps, while strictly positive rates give each nearby pair a uniform chance to collide in unit time.

Theorem 1 then places a left/right edge pair on opposite sides of any fixed block with probability bounded below. Tracing the pair to its last close encounter reduces block agreement to agreement at at most one special site. Equations (18)-(23) use the unused graphical update coin and the positive lower rate bound to give a uniform conditional chance of the required local agreement. Proposition 3 converts that positive block-agreement probability into equality of the extremal laws and ergodicity.

This is a distinct page because the live attractiveness method stops at the reduction to upper/lower invariant laws; Gray's edge coalescence plus local positive-rate repair is what actually closes that reduction in one dimension.

### Toom error graphs are not disagreement percolation

De Maere--Ponselet expand backward influence paths. A path segment in the good plus phase pays the A2 decoupling factor. When a path meets a bad minus spin, the proof attaches a Toom graph that traces the bad spin backward until it exposes a quantitatively large set of actual update errors. A1 charges each such error by the small noise parameter; Toom erosion makes the number of graph edges proportional to the number of identified errors, while graph multiplicity grows only exponentially. Low noise therefore beats contour entropy.

The proof object is an **error-history reconstruction inside a dynamical influence expansion**, not an independent open path dominating disagreements. The conclusion is also phase-specific exponential attraction to the plus invariant law and exponential correlation decay, not global uniqueness.

### Essential hitting times are regeneration for subadditive growth, not complete-convergence renewal

Garet--Marchand introduce the essential hitting time `sigma(x)` because the ordinary infection time is badly behaved after conditioning the contact process on survival. `sigma(x)` waits until `x` is infected by a lineage that itself survives forever. The corresponding space-time shift preserves the survival-conditioned law and is ergodic.

The restart is not exactly subadditive. Theorem 2 controls the defect between `sigma(x+y)` and the regenerated sum, and Corollary 16 gives the required moments. Theorems 23-24 are almost-subadditive ergodic theorems tailored to this setting; they yield the directional limit in Theorem 22, and Section 5 transfers it to the ordinary growth process and the asymptotic shape in Theorem 3.

This is distinct from the live multitype-contact survival-conditioned renewal page. There, renewal points plus steering prove takeover and complete convergence. Here the regeneration point repairs stationarity for passage times, and almost-subadditivity is the load-bearing second step leading to deterministic growth geometry.

## Source qualifications

### Gray 1982 edge method

Primary checked source: Lawrence F. Gray, *The positive rates problem for attractive nearest neighbor spin systems on Z*, Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete 61 (1982), 389-404, DOI `10.1007/BF00539839`.

Checked pinpoints:

- Section 1, Proposition 1 and Corollary 1.1 for interval comparison under the basic coupling;
- Section 1, edge properties E1-E5 and Proposition 2 for the hybrid identities, edge ordering/coalescence, and preservation of agreement between edges;
- Section 2, Proposition 3 for the positive block-agreement ergodicity criterion;
- Section 2, Theorem 1 and the Lemma immediately preceding equation (13) for edge coalescence/escape;
- equations (9)-(14) for positioning opposite edges around the target block;
- equations (18)-(23) for the uniform positive-rate local agreement estimate;
- Section 3, Theorem 2 for the repulsive-rate transformation.

The source itself states that periodicity is used essentially only in the Section 2 Lemma; the rest uses uniform upper and strictly positive lower rate bounds.

### Toom error graphs

Primary checked source: Augustin de Maere and Lise Ponselet, *Exponential Decay of Correlations for Strongly Coupled Toom Probabilistic Cellular Automata*, Journal of Statistical Physics 147 (2012), 634-652, DOI `10.1007/s10955-012-0487-9`, arXiv `1110.1540`.

Checked pinpoints:

- assumptions A1-A2 in Section 2;
- Theorem 1 for exponential convergence from the plus-phase basin;
- the spatial-correlation corollary after Theorem 1;
- Theorem 2 for exponential temporal correlations;
- Sections 3-4 for the influence-path expansion;
- Section 5 for Toom graphs/trusses and equation (16), relating graph size to identified errors;
- Sections 5-6, especially equations (23)-(26), for the graph-count/error-weight summation.

The entry deliberately states phase-specific convergence rather than uniqueness of the PCA.

### Essential hitting times

Primary checked source: Olivier Garet and Régine Marchand, *Asymptotic shape for the contact process in random environment*, Annals of Applied Probability 22 (2012), 1362-1410, DOI `10.1214/11-AAP796`, arXiv `0910.1230`.

Checked pinpoints:

- Section 2.6 for the essential hitting-time definition and regeneration interpretation;
- Theorem 1 for invariance/ergodicity of the regenerated space-time shift;
- Theorem 2 and Corollary 16 for quantitative control and moments of the subadditivity defect;
- Theorems 23-24 for the almost-subadditive ergodic machinery;
- Theorem 22 for directional convergence of essential hitting times;
- Theorem 3 and Section 5 for the asymptotic shape and transfer back to ordinary infection/coupling times.

The page is explicitly adjacent long-time-growth material; it does not re-label the shape theorem as invariant-law ergodicity.

## Gray 1986: source-access hold, not taxonomy rejection

Target 2 was not staged. I verified the official bibliographic record and abstract for Lawrence Gray, *Duality for General Attractive Spin Systems with Applications in One Dimension*, Annals of Probability 14 (1986), 371-396, DOI `10.1214/aop/1176992522`. The abstract confirms that the paper develops a duality for general attractive Markovian spin-flip systems and applies it in one dimension, including Theorem 2 on exponential convergence from all ones in noncritical nonergodic systems, Theorem 4 on the law near edges, and Theorem 5 on equivalence of critical-value definitions.

However, the Project Euclid/JSTOR full article body was not retrievable in this session. I therefore could not inspect Gray's own dual state space, duality identity, or the theorem-proof chain connecting that dual to the edge result. Modern primary work by Sturm--Swart gives a detailed pathwise reformulation of Gray's monotonicity-based duality, but using that reformulation as if Gray 1986 itself had been checked would violate this programme's source convention.

Accordingly:

- do not record Gray 1986 as refuted, merged, or redundant;
- do not treat the abstract theorem numbers as sufficient for `primary-checked`;
- reopen this source family if a readable scan/full text of Gray 1986 becomes available.

## Further source-led gaps

- **Gray 1986 monotone duality and edge relaxation** remains the most immediate unfinished source-led candidate once primary full text is available.
- **Gray's continuous-time Toom stability theorem** (1999) may expose a continuous-time contour/error-history interface distinct from the PCA page, but it should be inspected from source before any split is claimed.
- Contact-process **essential hitting times with sharper deviation or random-environment homogenisation machinery** may support later pages only when the extra theorem object is distinct from the almost-subadditive regeneration already staged here.
- Toom/Peierls graph expansions for genuinely continuous-time IPS remain a possible graphical family if an application proves relaxation rather than only stability/survival.

Closed generic searches from earlier meetings remain closed.

## Mechanical and encoding checks

The three entries were written against the current `entry-template.md` and committed separately. Each was fetched back after creation to check that the stored UTF-8 text matched the intended Markdown and did not contain visible control-character corruption. `validate_entries.py` remains the principal/orchestrator's structural check and is not treated here as mathematical or source verification.