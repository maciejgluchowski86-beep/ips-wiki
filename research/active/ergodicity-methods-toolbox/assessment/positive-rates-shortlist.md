# Positive-rates A/B shortlist and bridge tests

This file is the durable shortlist component of Student G Assignment 007. It is to be merged into `positive-rates-method-audit.md`; it is not a new toolbox entry and does not reopen the stopped positive-rates proof programme.

## Ranking

1. **A — Gray one-dimensional edge coalescence** — PR2.
2. **B — refined non-diagonal discrepancy coupling** — PR2.
3. **B — information percolation** — PR5.
4. **B — block coupling / joint-block stationary control** — PR3.
5. **B — physical-front regeneration adapted to the disagreement front** — PR2.

No frozen method currently earns `A/B` for PR1, the signed two-time boundary-transmission operator. Methods that naturally use positive norms, reversible coercivity, or positive contour weights erase the cancellation Meeting 030 says is load-bearing.

The first two candidates are related and should not be funded as two independent research blocks. The first experiment below tests the nonbasic coupling mechanism that would be the most concrete way to implement a Gray-type nonmonotone edge architecture.

## 1. Gray edge coalescence — A

**Live source:** `docs/entries/one-dimensional-edge-coalescence-positive-rates.md`.

**Target interface:** PR2, common-coupling convective escape.

### Bridge lemma G: nonmonotone splice-edge coupling

For every strict residual rate triple, construct a translation-covariant finite-range grand coupling of the target dynamics and its finite-cone random maps with the following properties.

1. A one-site change in the initial data has a scalar right boundary of influence (an edge), and finite collections of such edges are ordered: edges do not cross.
2. Edges that meet coalesce permanently.
3. Between a suitable left/right edge pair, the value of the coupled random map on a fixed observation interval is protected from initial data outside the pair, the nonmonotone analogue of Gray's hybrid-region identities.
4. Neighboring surviving edges have a uniform positive chance, depending only on the positive rate lower bound and not on their spatial position or history, to coalesce during a bounded local episode.
5. The edge process is spatially stationary/ergodic under homogeneous initial random-map perturbations, so a positive density of eternal distinct edges contradicts item 4 exactly as in Gray's density argument.

The bridge is intentionally structural. It does not assume an order on spin configurations and does not ask for one-step Hamming contraction.

### Implication chain

`G` gives coalescence of the influence edges of the finite-cone random map. Therefore, with probability tending to one, the value of that random map on any fixed interval is independent of every initial assignment in the base of its backward cone. Finite propagation removes the cone truncation. Hence transition probabilities of every local observable forget the initial configuration; invariant laws agree on all local functions, yielding uniqueness and convergence.

### Exact obstruction avoided

Gray's published proof needs attractiveness/repulsiveness to obtain protected hybrid regions and ordered edges. The residual chamber contains systems with neither property. `G` replaces that order by a purpose-built coupled edge geometry. It does not use the common-uniform Hamming contraction whose `alpha(t)>1` obstruction was certified, and it does not use a positive coefficient norm or scalar Foster corrector.

### Cheapest falsification test

At the hard residual points `P_h=(1/10000,1/100,9999/10000)` and `P_*=(1/1000,1/10,9999/10000)`, enumerate the finite local states of two adjacent splice interfaces on a three- or four-site window. Introduce variables for joint event rates pairing a flip in one marginal with a flip or null move in the other. Impose exact marginal-rate constraints plus no-crossing, permanent-coalescence and protected-region constraints. This is a finite rational linear-feasibility problem. If it is infeasible already for one local interface pattern, the most direct nonmonotone Gray extension is killed before any infinite-volume argument.

## 2. Refined non-diagonal discrepancy coupling — B

**Live source:** `docs/entries/refined-discrepancy-coupling-general-exclusion.md`.

**Target interface:** PR2.

### Bridge lemma R: discrepancy-nonincreasing coupled rates

For every rate triple in the residual chamber, there exists a translation-covariant finite-range Markovian coupling of two copies of the spin system, allowed to pair a flip at site `i` in one marginal with a flip at site `j` in the other, such that for every pair with finite disagreement set `D`,

`bar L |D| <= -kappa |D|`

for a `kappa>0` depending on the rate triple but not on the configuration or `|D|`.

A pathwise version, in which `|D|` never increases and each existing discrepancy has a uniformly positive removal hazard, would be stronger and also sufficient.

### Implication chain

The bridge gives `E|D_t| <= exp(-kappa t)|D_0|`. To compare two arbitrary initial configurations on a fixed observation interval at time `t`, use finite propagation to restrict the relevant initial data to a base interval of size `O(t)` with exponentially small error, couple the two truncated configurations by `R`, and obtain an `O(t) exp(-kappa t)` disagreement bound on the observation interval. Local transition laws therefore agree asymptotically, implying uniqueness and convergence.

### Exact obstruction avoided

The hard `alpha(t)>1` certificate concerns the **common-uniform coupling**. Gobron--Saada's lesson is precisely that basic coupling may be too rigid and that different microscopic moves can be paired while preserving both marginals. `R` changes the coupling itself. It is not a new norm on the old coupling.

The route must also avoid collapsing into the refuted scalar local Foster classes. If the proposed construction only gives a phase-dependent additive drift estimate for the common coupling, rather than a genuinely new non-diagonal coupled generator, it is already stopped work.

### Cheapest falsification test — recommended first overall

Solve the finite rational LP of joint local rates at `P_h` first. For every local pair pattern in which a flip of one copy can create a disagreement, require the excess rate to be matched by a simultaneous move that removes at least as many discrepancies elsewhere. Maximize `kappa` subject to exact marginal constraints. A certified optimum `kappa<=0` for a required local pattern kills Bridge R. Add Gray's no-crossing/coalescence constraints to the same LP to test Bridge G at almost no extra conceptual cost.

This is the single cheapest experiment recommended by the audit.

## 3. Information percolation — B

**Live source:** `docs/entries/information-percolation-backward-histories.md`.

**Target interface:** PR5, a bypass of PR1--PR4.

### Bridge lemma IP: sparse red histories for the positive-rates random map

Use positivity of all flip rates to decompose the generator into state-independent reset-to-zero/reset-to-one marks plus residual local maps. For a finite observation set `A` at time `t`, let `H_A(s,t)` be the minimal backward support under this random-map representation and classify connected history clusters as red/blue/green as in the live information-percolation page.

Prove, uniformly over finite-volume truncations and exterior initial states, the red-intersection estimate

`E[ 2^{|R_t intersect R'_t|} | green histories ] - 1 <= C_A exp(-gamma t)`

for two conditionally independent red sets `R_t,R'_t`, or another source-supported Miller--Peres-type bound strong enough to force the local total-variation distance to zero.

### Implication chain

The information-percolation `L^2` estimate then makes the law on `A` at time `t` asymptotically independent of the initial state even if some backward histories reach time zero. Taking `t -> infinity` gives local mixing and uniqueness of the invariant law.

### Exact obstruction avoided

This route does **not** require extinction of the common-coupling disagreement set, so convective escape is irrelevant. It does not require all ancestor histories to die, so it is strictly weaker than CFTP/clan finiteness. It also never estimates the signed boundary-transmission operator `V_N` or a positive raw coefficient norm.

The distinction is essential: replacing the red-intersection estimate by a crude Dobrushin coefficient or by `expected offspring < 1` would turn the proposal back into methods already known to be too strong or too crude.

### Cheapest falsification test

At `P_h` and `P_*`, enumerate all deterministic two-input local maps that can appear in a Poisson random-map decomposition of the generator and optimize the decomposition for backward-support sparsity. Build the exact finite-depth transfer operator for **pairs** of minimal supports and the intersection weight `2^{|R intersect R'|}`. A certified volume-uniform lower bound preventing decay for every admissible local decomposition would kill this simple IP bridge. A merely supercritical first-moment branching number does **not** kill the method, because the Lubetzky--Sly mechanism can work beyond naive subcritical branching.

## 4. Block coupling / joint-block stationary control — B

**Live source:** `docs/entries/block-coupling-joint-resampling.md`.

**Target interface:** PR3, the stationary boundary-control diameter.

### Bridge lemma BC: uniform cross-block Bellman mismatch

For a fixed block length `ell` and `delta>0`, uniformly in `N` and every nonconstant local test `h`, let `s_N^+` and `s_N^-` be the exact Bellman endpoint slacks from the stationary control hierarchy. Prove

`inf_{m in K_{N+ell}} m(s_N^+) + inf_{m in K_{N+ell}} m(s_N^-) >= delta D_N(h)`.

The point is that the estimate is obtained from a **joint `ell`-site coupling/control of the boundary block**, not from an additive corrector applied independently at each scale.

### Implication chain

The established scale-extension identity gives

`D_{N+ell}(h) <= (1-delta) D_N(h)`.

Iteration yields geometric `D_N(h) -> 0` for every local `h`. Since every infinite-volume invariant law projects into every `K_N`, the invariant laws coincide on all local functions.

### Exact obstruction avoided

F015 proved that additive Bellman correctors without cross-block dependence cannot improve the endpoints. `BC` asks for precisely the missing cross-block information. It is not a new scalar potential, not the controller-uniform unweighted mismatch bound (which decays like `1/N`), and not a bare reformulation of `D_N -> 0`.

### Cheapest falsification test

Use exact rational LP at `P_h` and `P_*` for `ell=2` and then `ell=3`. For a small basis of local `h`, compute `D_N(h)` and both infimum slack terms for the first few `N`. If for some `N,h` with `D_N(h)>0` the sum of the two exact infima is **zero**, then a uniform positive `delta` bridge of this form is immediately false. If the ratios stay positive, that is evidence only; no extrapolation in `N` is permitted without proof.

## 5. Physical-front regeneration adapted to disagreements — B

**Live source:** `docs/entries/front-regeneration-renewal-times.md`.

**Target interface:** PR2.

### Bridge lemma FR: regenerative disagreement front with terminal hazard

For the common-uniform coupling started from a finite disagreement set, let `R_t` be the rightmost disagreement. Construct translated regeneration times `kappa_n` for the rightmost disagreement cluster such that:

1. on nonextinction, the next regeneration occurs with a uniformly controlled tail;
2. after translating `R_{kappa_n}` to zero, the local interface state at regeneration belongs to a fixed finite/compact class and its post-regeneration graphical future is independent of the pre-regeneration history in the sense needed for iteration;
3. at every regeneration there is a uniform probability `p>0` that the entire remaining finite disagreement set becomes empty before the next regeneration; and
4. the resulting cycle estimates are uniform enough in the initial finite set to give an extinction tail beating the `O(t)` size of a finite-propagation backward cone.

### Implication chain

Repeated fresh trials give an exponentially small probability of surviving many regeneration cycles. Together with the cycle-time tail this yields a quantitative extinction bound for finite disagreement sets. Finite propagation then transfers the bound to local coupling of arbitrary initial configurations, proving uniqueness and convergence.

### Exact obstruction avoided

The stopped common-coupling result already proves permanent coupling of every fixed site; merely tracking the front position or its occupation therefore adds nothing. `FR` requires a **fresh restart sigma-field plus terminal extinction hazard**. It is not an essential-hitting-time shape theorem, a moving-frame stationary law, or another occupation estimate.

The collection phase found no primary theorem for an actual disagreement-front regeneration of this type. This is why the rating is `B`, not `A`, and why only a bounded falsification calculation is justified before any research block.

### Cheapest falsification test

At `P_h`, construct the exact common-coupling chain in a moving frame around the rightmost disagreement, truncated to interface widths `W=2,3,...` with worst-case left boundary. Uniformize it exactly and compute: (i) the minimum probability of extinction before shifting another `W` sites left, and (ii) return probabilities to a fixed small interface class. If the minimum extinction probability collapses to zero or the interface mass escapes every fixed class as `W` increases, the proposed finite/compact regeneration architecture is strongly disfavored and should not be escalated.

## Repackaging warnings

- **Gray / refined coupling:** do not evaluate a new coupling only through the old common-coupling Hamming drift. Conversely, if the proposed nonbasic coupling reduces to a scalar local Foster correction on the old coupling, the balanced-circulation refutation applies.
- **Information percolation:** do not replace sparse red-history intersection by total ancestor extinction, Dobrushin row sums, or early absolute values. Those are different and stronger methods.
- **Block coupling:** any proof that decomposes into additive one-block Bellman correctors is already ruled out. The whole point is a genuinely joint boundary block.
- **Front regeneration:** speed, local coupling at fixed sites, or a stationary environment seen from the front is insufficient. A restart with fresh future plus a terminal extinction mechanism is required.
- **PR1:** no method in the frozen inventory currently gives a credible new way to preserve the two-time sign cancellation of `V_N`. Reversible comparison, positive curvature/coercivity, Toom positive error weights, Nash-type positive seminorms and ordinary norm contraction all erase the mechanism Meeting 030 leaves open.
