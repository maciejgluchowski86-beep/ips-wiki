# Group meeting 004: F wave two source-audited; analytic wave three opens

Date: 2026-08-17

Professor review of Student F Assignment 002 entries at commits `7dd08be`, `dce51c3`, `155ec69`, `2357240`, `6944151`, and `ba59e4d`, together with the principal's report that `validate_entries.py` passes all eighteen staged entries and that `docs/` and `mkdocs.yml` remain unchanged from `origin/main`.

## Ruling

All six F-wave-two entries are **accepted for later live-wiki integration**. They remain staged until a quiet integration window; Student G is still committing Assignment 002 entries, so no public-wiki promotion is performed in this meeting.

Accepted entries:

1. `lu-yau-martingale-conditional-variance.md`;
2. `spectral-independence-local-to-global.md`;
3. `block-factorization-entropy.md`;
4. `holley-stroock-bounded-perturbation.md`;
5. `moving-particle-long-jump-exclusion.md`;
6. `finite-size-strong-mixing-criterion.md`.

The branch therefore has eighteen mechanically valid staged entries, of which all eighteen have now passed Professor source audit. The first twelve remain the first integration batch; the six here are queued immediately behind them.

## 1. Source audit

### Lu--Yau martingale / conditional-variance recursion

Accepted. Landim--Panizo--Yau explicitly state that they follow the martingale method introduced by Lu--Yau and prove diffusive-order spectral-gap and logarithmic-Sobolev estimates for conservative Ginzburg--Landau dynamics. Section 3 is an induction on volume using conditional variance and Section 4 is the entropy analogue. The entry correctly distinguishes this filtration recursion from geometric block bisection and states the need for local-CLT/equivalence-of-ensembles control.

The checked source also confirms the scope: bounded perturbations of a Gaussian single-site potential and constants of order `L^{-2}` for the gap and logarithmic-Sobolev constant. The entry does not overstate this as a generic conservative theorem.

### Spectral independence / local-to-global influence

Accepted. Anari--Liu--Oveis Gharan Definitions 1.1--1.2 define the signed pairwise influence matrix and the requirement that spectral bounds persist under conditioning. Theorem 1.3 transfers the conditional spectral-independence parameters to a Glauber spectral-gap bound; Theorems 1.5--1.6 provide the high-dimensional local-to-global mechanism. Theorem 1.8 and Remark 1.10 give the hard-core application up to the tree uniqueness threshold. The entry correctly separates this from Dobrushin row-sum contraction.

### Block / approximate factorization of entropy

Accepted. Chen--Liu--Vigoda's block-factorization architecture is accurately stated. In particular Lemma 2.3 gives, for a `b`-marginally bounded Gibbs distribution of maximum degree `Delta`, the implication from `ceil(theta n)`-uniform block factorization with `theta <= b^2/(12 Delta)` to approximate tensorization with

$$
C_1=\frac{18\log(1/b)}{b^4}C.
$$

The paper's main applications give optimal-order Glauber mixing in the listed bounded-degree regimes. This remains a separate toolbox entry from spectral independence and from the generic mLSI page because the load-bearing interface is an entropy decomposition theorem.

### Holley--Stroock bounded perturbation

Accepted with F's attribution discipline retained. Menz--Schlichting Theorem 3.2 is an explicit modern statement of the Holley--Stroock perturbation principle: PI/LSI constants lose at most the exponential of the perturbation oscillation (temperature-scaled in their convention). Definition 3.3 and Lemma 3.4 isolate the useful small-oscillation regime. The original Holley--Stroock stochastic-Ising paper is cited as origin, not silently treated as the inspected theorem statement.

The limitation in the entry is essential and correct: a sum of bounded local perturbations generally has volume-order total oscillation, so naive global application can lose `exp(O(|Lambda|))` and is not a volume-uniform mixing theorem.

### Moving-particle / long-jump exclusion comparison

Accepted. Joe Chen's moving-particle lemma is specifically a finite weighted-graph exclusion theorem derived from the octopus inequality, replacing a long exchange by the full local exclusion energy with effective-resistance cost. The follow-up local-ergodicity paper explicitly uses one-block/two-block estimates, the moving-particle lemma, and resistance geometry for symmetric and boundary-driven exclusion on exhausting weighted graphs.

The entry correctly states that this is not a positive infinite-volume gap theorem: its reusable role is long-jump replacement/coercive comparison inside local-ergodicity and hydrodynamic arguments.

### Finite-size strong-mixing criterion

Accepted. Martinelli--Olivieri Part II explicitly advertises the decisive quantifier structure used in the entry: strong mixing in one finite cube `Lambda_0` is bootstrapped by block decimation to an LSI, hypercontractivity, and exponential convergence in large volumes that are `multiples` of `Lambda_0`. The entry correctly keeps that geometric restriction and distinguishes this finite-size certification architecture from assuming Dobrushin--Shlosman mixing uniformly over all large regions.

## 2. Taxonomy consequences

Wave two fills six previously distinct gaps rather than adding variants of the first-wave pages:

- filtration/martingale recursion for conservative coercivity;
- conditional influence spectra and high-dimensional local-to-global expansion;
- entropy block factorization as an intermediate proof interface;
- bounded-density perturbative transfer;
- exclusion-specific long-jump/effective-resistance comparison;
- finite-size-to-large-volume strong-mixing bootstrap.

Cross-links will be added during live integration. No merges are ordered.

## 3. Student F continuation

Student F is assigned one further analytic breadth wave. Assignment 003 should prioritize mechanisms not yet represented:

- Bakry--Emery / Bochner curvature or Gamma-calculus methods with an IPS/spin application;
- two-scale/coarse-graining coercivity for conservative spin systems;
- the Aldous/interchange-process spectral-gap reduction and its exclusion consequence;
- Nash inequalities or closely related heat-kernel/spectral-profile smoothing with a concrete IPS application;
- nonreversible symmetrization/sector/hypocoercive coercivity with a genuine IPS or spin-system application;
- conductance/Cheeger/isoperimetric lower bounds for relaxation or mixing in a spin-system chain.

If one target lacks a clean primary-source IPS application, F may substitute a genuinely distinct analytic method from the coverage spine, but must state the substitution in the handoff rather than forcing a weak entry.

## 4. Current work status

- Student F: Assignment 002 complete; Assignment 003 opened.
- Student G: remains active on Assignment 002; do not interrupt or retask before its handoff.
- Eighteen entries have passed mechanical validation and Professor source audit.
- `docs/` and `mkdocs.yml` remain untouched in this meeting.
- Live integration remains queued for the next window in which no student is actively committing a staging batch.
