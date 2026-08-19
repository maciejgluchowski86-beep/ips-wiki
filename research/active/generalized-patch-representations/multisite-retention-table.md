# Multi-site extension: retention table against the current paper

Date: 2026-08-19

Scope: exploratory research workspace only. This note does not modify `paper/`.

The comparison is against the actual theorem/proof architecture in the current paper on branch `research/generalized-patch-representations`. Two multi-site classes are distinguished:

1. **Disjoint bounded update blocks:** allowed physical source blocks form a partition of the site set, with uniformly bounded block size. The enriched successful record exposes the source pre-state and target-block pre-states, while hiding the signed post-source state. The expected local objects are one-block patches.
2. **Envelope hyperpatches:** bounded finite-range update blocks may overlap. A successful record exposes a deterministic boundary envelope but hides the sign-bearing post-source state/routing. Atomic site strips coupled by selected hidden marks or omitted overlapping clocks are glued into spacetime hyperpatches.

Status language below:

- **survives verbatim:** the theorem has the same mathematical content after replacing the local patch object and its definitions; no new conceptual hypothesis is needed beyond the class assumptions. A proof may still need to be written.
- **survives with extra hypothesis:** the same conclusion follows if an additional sign/monotonicity condition is imposed.
- **needs a new argument:** the present proof uses a one-site property which is absent, but the conclusion is not known to be false.
- **fails as stated:** the hypotheses of the paper no longer imply the claimed conclusion or characterization.

A separate mechanical status is also recorded. Several disjoint-block claims are presently proof architectures, not completed theorems.

## Retention table

| Paper result | Disjoint bounded blocks | Envelope hyperpatches | Precise reason / replacement |
|---|---|---|---|
| **Monomial Feynman--Kac duality** (`thm:monomial-duality`) | **Survives verbatim in conclusion.** Exact algebra already derived. | **Survives verbatim in conclusion.** Exact algebra already derived. | For a physical block `A`, current dual support `B`, and `D=A cap B`, expand `chi_B(eta^A)-chi_B(eta)` over post-source subsets `J subseteq D`, combine equal resulting monomials, represent off-diagonal signed coefficients by rates/signs and put the diagonal discrepancy in `V(B)`. The dual is no longer additive and its applicable clocks depend on `B cap A`, but the generator identity `L_eta H=D H+V H` and FK formula have the same form. Infinite-volume passage still needs the usual bounded-incidence/local-finiteness and FK-integrability assumptions. **This part is algebraically established, not merely conjectural.** |
| **Patch factorization** (`thm:patch-factorization`) | **Survives verbatim at block level, but proof not yet written.** | **Needs a new argument.** | In the disjoint-block class, after enriching the record with all boundary block states, every omitted-clock consistency test is local to one block-time strip and distinct strips use disjoint Poisson restrictions; the paper's Mecke/Radon--Nikodym proof should be a notational lift. This is presently a proof architecture, not a checked theorem. With overlaps, one-site/block-strip consistency does not factor. The proposed replacement is conditional independence of **hyperpatch components** under consistent hyperpatch laws. One must prove measurability of the envelope-defined components, completeness iff all component consistency events hold, and disjointness of the underlying Poisson restrictions/hidden selected marks. No contradiction is known, but this is genuinely new proof work. |
| **Patch representation** (`thm:patch-representation`) | **Survives verbatim once block factorization is proved.** | **Needs a new argument, conditional on hyperpatch factorization.** | In disjoint blocks, `V(B)=sum_Q v_Q(B cap Q)` is block-additive, selected signs belong to unique outgoing block patches, and `chi_{B_t}` factors over terminal blocks. Thus the pathwise FK variable factors exactly and conditional averaging gives the same representation with scalar bulk block factors and multi-affine block end factors. In the overlap case the same idea should work only after every physical clock/potential contribution is assigned to one envelope hyperpatch. The pathwise factorization appears component-local, but it has not been proved together with the factorization theorem. |
| **Patch positivity as an abstract property** (`C(P)>=0`) | **Survives verbatim as a definition.** | **Survives verbatim as a definition.** | Replace one-site patches by block patches or hyperpatches. A completed component has a scalar averaged signed FK contribution, so asking it to be nonnegative is meaningful in both classes. |
| **Patch-positivity coefficient characterization and scalar threshold formula** (part (i) of `thm:patch-positivity-order`) | **Fails as stated; replacement needs new finite-dimensional analysis.** | **Fails as stated, with no uniformly local replacement expected in general.** | The two inequalities in the paper exploit a two-state one-site interior and four boundary types. For a block `Q`, the local state is `P(Q)`, so even with bounded `|Q|` positivity becomes a finite matrix-semigroup boundary-response problem of dimension at most `2^{|Q|}`. This is still tractable block by block but no general coefficient formula has been derived. End factors are multi-affine, so there is no automatic scalar threshold `p_i^star`; instead one gets a finite set of profile inequalities per block. For overlapping hyperpatches, spatial component size is not uniformly bounded, so positivity is an unbounded family of component sign conditions. |
| **Nonnegative end weights for measures in `M_*`** (the centered end expansion used before order preservation) | **Survives with an extra hypothesis, not yet proved for any nontrivial block model.** | **Survives with an analogous extra hypothesis, conditional on hyperpatch factorization.** | Fix a profile `p^star`. For every terminal block patch require the centered multi-affine expansion `C_Q(z,P)=sum_{R subseteq Q} kappa_R(P) prod_{i in R}(z_i-p_i^star)` to have **all** `kappa_R(P)>=0`, including the constant term. Because terminal block supports are disjoint, multiplying these expansions gives nonnegative coefficients of global centered monomials, so `mu in M_*` makes each skeleton end average nonnegative. For hyperpatches the same algebra should work using their disjoint terminal-leg sets once the representation is proved. **This strengthened block-end condition is only proposed; it has not been derived from bulk patch positivity or verified in a model.** |
| **Centered-moment cone `M_*` as an algebraic cone** | **Survives verbatim once a profile `p^star` is chosen.** | **Survives verbatim once a profile `p^star` is chosen.** | The definitions `chi_A^*=prod_{i in A}(eta_i-p_i^star)`, `M_*={mu:mu(chi_A^*)>=0}`, convexity/closedness, and `mu_p in M_* iff p>=p^star` are independent of the generator. What is lost is the paper's canonical explicit choice of `p^star` coming from the scalar patch-threshold formula. |
| **Centered-moment order preservation** (part (ii) of `thm:patch-positivity-order`) | **Needs a new argument under block patch positivity; survives with a separate centered-basis Metzler hypothesis.** | **Needs a new argument under hyperpatch positivity; survives with the same type of separate Metzler hypothesis.** | Important correction to the earlier exploratory note: nonnegative bulk factors plus nonnegative centered coefficients of every end block factor give nonnegative **ordinary-monomial skeleton weights**, but do **not** by themselves prove `mu preceq_* nu => mu P_t preceq_* nu P_t`. The current paper explicitly says the end expansion is insufficient and then proves order preservation by showing the generator matrix in the centered-monomial basis has nonnegative off-diagonal entries. For multi-site flips one must redo that generator calculation. A sufficient extra hypothesis is exactly that every finite-volume generator is Metzler in the centered-monomial basis (with compatible zero-boundary restrictions); then the paper's matrix-exponential argument carries over essentially verbatim. It is not currently proved that block/hyperpatch positivity plus the strengthened end condition implies this Metzler property. |
| **Preservation of `M_*` and ordinary monomial comparison under `preceq_*`** | **Same status as centered-order preservation.** | **Same status as centered-order preservation.** | These are downstream consequences of positivity of the semigroup on centered monomials in the paper. Under the separate centered-basis Metzler hypothesis they survive. The weaker block-end condition alone gives some skeleton-level ordinary-monomial inequalities for `mu in M_*`, but not the full semigroup cone/order theorem. |
| **Pure-death comparison** (`cor:pure-death-comparison`) | **Fails as stated under block patch positivity; could survive with a stronger death-monotonicity hypothesis.** | **Fails as stated under hyperpatch positivity; would need a stronger componentwise death-monotonicity hypothesis and new proof.** | The paper uses the one-site fact that removing independent `1->0` noise leaves the dual jumps/skeleton/reference patch law unchanged and changes each relevant patch contribution monotonically; on an outgoing-terminal patch it even gives the exact scalar factor `exp(-epsilon Delta)`. For a block/hyperpatch hidden history, independent deaths produce the path factor `exp(-epsilon int |X_u|du)`, which varies between hidden histories. Positivity of the averaged component does not imply monotonicity in `epsilon`. A sufficient replacement would be a Laplace/death-monotonicity condition asserting the required component averages and centered end coefficients are monotone under this tilt. No such theorem is currently proved. |
| **Invariant-measure comparison** (`cor:pure-death-invariant-comparison`) | **Fails with the parent comparison; conditional if a replacement death-comparison theorem is proved.** | **Same.** | The Cesaro argument itself is unchanged, but it has no input without the semigroup pure-death comparison. |
| **Common invariant limit with rate `O((1+t)^D e^{-epsilon t/2})`** (`thm:common-invariant-limit`) | **Needs a new argument; not retained from block positivity/end positivity alone.** | **Needs a substantially new argument; not retained.** | The current proof uses four one-site ingredients: nonnegative weights dominated by the death-removed system, the exact outgoing-patch factor `C(P)=e^{-epsilon Delta}C^epsilon(P)`, a backward chain of outgoing patches whose lengths add exactly to the late interaction time, and one-site end relaxation at rate at least `epsilon`. The first two already fail to follow from block positivity. In block patches a possible causal ancestry chain still exists, but hidden multiplicity `|X_u|` and joint state evolution prevent the exact factor from being read off patch lengths. Hyperpatches add branching/overlap of causal components. Finite propagation itself should survive, but the decisive late-interaction and no-late-relaxation estimates need replacement lemmas. |
| **Full-patch formula for the limiting moments** (part of `thm:common-invariant-limit`) | **Conditional on a new convergence theorem.** | **Conditional on a new convergence theorem.** | If convergence can be proved using nonnegative integrable component weights, the natural limit formula is again the expectation of the product of completed block/hyperpatch contributions on finite-component realizations. At present the needed domination/convergence is missing. |
| **Unique invariant law and uniform exponential ergodicity** (`cor:uniform-ergodicity`) | **Needs a new argument even for nonconservative block systems; not currently retained.** | **Needs a new argument, and it is false for the main conservative applications on the full state space.** | As a formal theorem for multi-site systems augmented with independent facilitating-state creation, uniqueness could follow from an eventual replacement for the common-invariant-limit theorem plus a condition making all initial configurations enter the admissible affine cone. But the current proof depends on the lost convergence theorem and on the explicit threshold control. For Kawasaki, speed-change exclusion, Kob--Andersen and facilitated exclusion, particle number/density is conserved; hence a single invariant law attracting all initial configurations is not the right conclusion at all. Any application theorem there must be sectorwise/fixed-density or concern correlations/relaxation rather than global unique ergodicity. |

## What is genuinely retained now

At the present exploratory stage, the strongest claims that can be treated as mathematically established are:

1. the exact multi-site monomial generator algebra and therefore the signed FK duality construction, under standard local-finiteness/FK assumptions;
2. the disjoint-block reduction to a finite local dual state `P(Q)` and block-additive potential;
3. the information-theoretic fact that revealing actual post-support kills the selected-event cancellation, whereas an envelope record can fix boundaries while retaining the sign-bearing hidden post-source state.

The following are well-motivated but **not yet proved theorems**:

1. conditional factorization of disjoint block patches under the enriched skeleton;
2. the resulting exact block-patch representation;
3. envelope-hyperpatch conditional factorization and representation;
4. any nontrivial block/hyperpatch positivity criterion;
5. existence of a profile `p^star` satisfying the strengthened centered end-factor condition in a named multi-site model.

## The strengthened block-end condition: exact current status

Because this point is easy to overstate, the hierarchy is:

- **bulk block positivity**: `C(P)>=0` for each completed block patch;
- **centered block-end positivity**: every coefficient `kappa_R(P)` in the expansion around `p^star` is nonnegative;
- **centered-basis semigroup positivity / Metzler generator**: needed for full preservation of `M_*` and `preceq_*` by the current proof strategy.

No implication

\[
\text{bulk block positivity}
\Longrightarrow
\text{centered block-end positivity}
\Longrightarrow
\text{centered-basis Metzler}
\]

has been proved. The first arrow is certainly not automatic from the definitions, and the second is presently only a possible structural relation to investigate. Therefore the disjoint-block extension should not yet be advertised as preserving the paper's centered-moment theorem. What is currently credible is an exact representation plus a finite-dimensional positivity problem.

## Practical retention summary for the eventual principal report

The extension has a robust **representation layer** and a non-robust **positivity/convergence layer**.

- Representation layer: monomial FK duality is exact; block factorization/representation are cheap in the disjoint class and technically heavier but plausible with envelope hyperpatches.
- Positivity layer: abstract component positivity survives, but the paper's local coefficient criterion and scalar threshold do not.
- Order layer: requires a strengthened end-factor condition for nonnegative skeleton weights and, separately, a new centered-basis generator argument for full order preservation.
- Comparison/convergence layer: pure-death comparison is the first theorem that genuinely fails under mere component positivity, so the common invariant limit and unique-ergodicity results do not currently transfer.
- Conservative applications: the representation is directly relevant, but the correct downstream questions are fixed-density/sectorwise correlation and relaxation statements, not a common invariant law on the full configuration space.
