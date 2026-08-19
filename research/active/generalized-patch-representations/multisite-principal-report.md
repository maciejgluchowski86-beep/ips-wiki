# Principal report: extending the binary patch construction to multi-site updates

This report concerns binary IPS with simultaneous local updates

\[
L f(\eta)=\sum_{A\Subset\Lambda}c_A(\eta)\bigl(f(\eta^A)-f(\eta)\bigr),
\]

under the usual bounded finite-range/local-incidence assumptions. It is exploratory research material only. Nothing in `paper/` is modified. The confidence levels below are deliberately strict: the multi-site monomial duality is algebraically established; the proposed block/hyperpatch factorization and representation have not been written as complete proofs; the paper's positivity characterization fails as stated; the centered block-end condition proposed during this exploration is now explicitly refuted by a two-site Ising block model; and the pure-death comparison/convergence layer does not transfer under component positivity alone.

## 1. What the patch extension is

The algebraic starting point survives cleanly. Expand each local rate as

\[
c_A(\eta)=\sum_{S\subseteq N(A)}c_A(S)\chi_S(\eta).
\]

For a dual monomial \(\chi_B\), put \(D=A\cap B\). Then

\[
\chi_B(\eta^A)-\chi_B(\eta)
=
\sum_{J\subseteq D}\theta_D(J)
\chi_{(B\setminus D)\cup J}(\eta),
\]

where

\[
\theta_D(J)=(-1)^{|J|}\quad(J\neq D),
\qquad
\theta_D(D)=(-1)^{|D|}-1.
\]

After multiplication by the rate monomial \(\chi_S\), the corresponding branch has support

\[
(B\setminus D)\cup J\cup S
\]

and signed coefficient \(c_A(S)\theta_D(J)\), before canonically combining equal monomials. There is one useful simplification: if \(S\cap D\neq\varnothing\), then

\[
\chi_S\bigl(\chi_B(\eta^A)-\chi_B(\eta)\bigr)
=-\chi_{B\cup S},
\]

so that rate mode has a single canonical branch. The genuinely multi-outcome hidden variable \(J\) occurs when \(S\cap D=\varnothing\).

Representing the absolute values of the canonical off-diagonal coefficients as jump rates, retaining their signs as marks, and putting the diagonal discrepancy into a Feynman--Kac potential gives the same generator identity as in the binary paper,

\[
L_\eta H(Y,\eta)=\mathcal D H(Y,\eta)+V(Y)H(Y,\eta),
\]

and hence the same monomial FK formula. This part is algebraically established. What changes is the dual geometry: the set-valued dual is generally nonadditive, and the applicable transition at a physical block \(A\) depends on the whole current pattern \(B\cap A\), not on independent active sources.

There are then two geometrically distinct patch regimes.

### Disjoint bounded blocks

Suppose the dynamics can be organized into a fixed partition of the lattice into uniformly bounded super-blocks \(Q\), with every simultaneous update and its local dependence assigned to one super-block. The natural local dual state is

\[
D=B\cap Q\in\mathcal P(Q).
\]

After aggregating the canonical coefficients, the block acts as a finite-state signed source with post-source state \(R\subseteq Q\) and external target \(T\). A successful record should reveal the source pre-state \(D\), the external target, and, for every target block, the pre-incoming block state. It should hide the signed post-source state \(R\). The extra incoming boundary labels are needed because adding a target subset to a block does not determine that block's full state.

Cut each block time-line at successful outgoing and incoming incidences. A block patch is one such block-time strip, carrying a local process

\[
X_u^P\in\mathcal P(Q).
\]

With the enriched boundary record, every omitted-clock consistency test is local to that one block-time strip, and distinct block patches use disjoint restrictions of the underlying block Poisson families. The FK potential is block-additive,

\[
V(B)=\sum_Q v_Q(B\cap Q),
\]

so the pathwise FK variable also decomposes over block patches. A completed block patch has a scalar contribution \(C(P)\); a terminal block patch has a multi-affine contribution in the terminal spins of \(Q\).

This is the cheap extension. The existing Mecke/Radon--Nikodym proof appears to lift with finite-state notation once the boundary labels are added. However, that proof has not been written line by line. Accordingly, block factorization and the resulting block-patch representation are plausible direct extensions, not established theorems at present.

### Overlapping update blocks: envelope hyperpatches

For Kawasaki-type and other translation-invariant local moves, physical update blocks overlap. Here one-site or one-block patches cannot be conditionally independent: an omitted clock on an edge or plaquette tests the joint dual state on several strips, and a selected multi-site branch can jointly initialize several strips through the same hidden post-source variable.

The first apparent obstruction is not fatal if the skeleton reveals the right information. Revealing the actual post-event support is wrong: for a canonical branch

\[
B'_J=(B\setminus D)\cup J\cup S,
\]

knowledge of the actual post-support determines

\[
J=B'_J\cap D,
\]

and therefore reveals the sign-bearing branch. The cancellation is then lost and one is back at the canonical absolute signed-dual bound.

Instead the successful record should reveal only a deterministic boundary envelope. For a record \((A,t,D,S)\), cut every site in

\[
A\cup S
\]

at time \(t\), regardless of the hidden post-source state \(J\). The envelope therefore fixes the spacetime boundaries while leaving \(J\) hidden. This is the exact multi-site analogue of the binary paper cutting the source line while hiding whether the source survives the interaction.

Atomic site strips are then glued whenever they are coupled by a common selected hidden mark or whenever an omitted physical update block can jointly query/update them during overlapping time intervals. The connected components are the proposed **hyperpatches**. All hidden signs, omitted clocks, consistency constraints and local FK-potential contributions involving several strips are internal to one component.

This resolves the geometry/sign conflict without collapsing to the raw absolute bound. If a selected envelope record has signed hidden outcomes \(a_u\) and downstream component factors \(F_u\), the raw absolute dual produces

\[
\sum_u|a_u|\,|F_u|,
\]

whereas the envelope construction retains

\[
\left|\sum_u a_uF_u\right|.
\]

For an interacting Kawasaki mode this is exactly the distinction between separating the `stay' and `move' branches and averaging them before taking absolute values.

The expected factorization statement is now componentwise: conditional on the envelope skeleton, distinct hyperpatches should use disjoint Poisson restrictions and hidden selected marks, and their completeness constraints should factor into component consistency events. The pathwise FK weight should then factor over the same components. No further conceptual obstruction has been found, but this is genuinely new proof work. Hyperpatch factorization and representation remain plausible, not proved.

Thus the proposed extension has a precise hierarchy:

\[
\boxed{\text{exact multi-site signed FK duality}}
\]

followed by

\[
\boxed{\text{plausible one-block representation for disjoint blocks}}
\]

and

\[
\boxed{\text{plausible envelope-hyperpatch representation for overlapping blocks}}.
\]

Only the first box is presently established.

## 2. Which results of the binary paper are retained

The robust part of the paper is the representation layer. The positivity, order, comparison and convergence package is not robust under multi-site updates.

| Result from the binary paper | Disjoint bounded blocks | Envelope hyperpatches |
|---|---|---|
| **Monomial Feynman--Kac duality** | **Retained, algebraically established.** Same generator/FK conclusion with finite block-state transitions. | **Retained, algebraically established.** Same conclusion with a nonadditive pattern-dependent dual. |
| **Patch factorization** | **Plausible direct lift; proof not written.** Enriched boundary block states make consistency local to one block strip, so the paper's Mecke proof appears to need only finite-state bookkeeping. | **Needs a genuinely new argument; plausible, not proved.** Must prove measurability/completeness of envelope hyperpatch components and componentwise independence of the relevant Poisson restrictions. |
| **Patch representation** | **Plausible conditional on factorization; proof not written.** Block-additive potential and terminal block factorization give the required pathwise decomposition. | **Plausible conditional on hyperpatch factorization; proof not written.** Requires a componentwise pathwise FK decomposition together with the new factorization theorem. |
| **Abstract patch positivity \(C(P)\ge0\)** | **Still a meaningful definition.** A completed block patch has a scalar averaged contribution. | **Still a meaningful definition.** A completed hyperpatch has a scalar averaged contribution. |
| **Paper's two coefficient inequalities characterizing patch positivity** | **Fails as stated.** Block positivity becomes a finite matrix-semigroup boundary-response problem on up to \(2^{|Q|}\) local states. No replacement coefficient theorem has been derived. | **Fails as stated.** Hyperpatch spatial size need not be uniformly bounded, so one should not expect a fixed finite local criterion in general. |
| **Explicit scalar threshold profile \(p_i^\star\)** | **Not retained.** Terminal block factors are multi-affine and impose a finite family of profile inequalities, not one scalar threshold formula per site. | **Not retained.** Terminal hyperpatch factors can involve many terminal legs. |
| **Nonnegative centered end factors** | **Not a generic retained property: explicitly false.** See the dimer counterexample below. It can only be imposed as an additional restrictive hypothesis. | **Not retained.** An analogous centered-coefficient condition could be imposed, but there is no reason to expect it generically. |
| **Centered-moment cone and preservation of \(\preceq_*\)** | The algebraic cone \(\mathcal M_*\) can of course still be defined after choosing a profile, but **semigroup preservation is not retained**. Even positive centered end coefficients would only give nonnegative skeleton end weights; the paper separately uses a centered-monomial Metzler generator calculation to prove order preservation. That calculation must be redone and no implication from block positivity is known. | **Same conclusion, with more work.** Hyperpatch positivity does not imply centered-basis semigroup positivity. |
| **Pure-death comparison** | **Does not transfer under block positivity.** Independent deaths insert a hidden-history-dependent factor \(\exp(-\varepsilon\int |X_u|du)\), so positivity of the averaged block contribution does not imply monotonicity in \(\varepsilon\). | **Does not transfer.** The same obstruction occurs inside a larger component. A new death/Laplace-monotonicity hypothesis and proof would be required. |
| **Common invariant limit and its rate** | **Not retained. Needs a new argument.** The paper's proof uses the exact outgoing-patch identity \(C(P)=e^{-\varepsilon\Delta}C^\varepsilon(P)\), then multiplies it along an ancestry chain. That identity is lost after averaging block histories with different active-time integrals. | **Not retained. Needs substantially new arguments.** Causal ancestry and finite propagation survive geometrically, but the decisive positive weight comparison and exact late-interaction factor do not. |
| **Unique invariant law / uniform exponential ergodicity** | **Not retained.** It could conceivably be recovered for a nonconservative block system after a replacement convergence theorem, but nothing in the present extension proves it. | **Not retained, and false as a global conclusion for the main conservative applications.** Kawasaki, speed-change exclusion, Kob--Andersen and facilitated exclusion preserve particle number/density, so one global attracting invariant law is not the correct target. |

The strengthened block-end condition considered during this exploration is now decisively ruled out as a generic rescue of the centered-order layer. Take the one-dimensional zero-field ferromagnetic Ising model and partition the lattice into dimers. At each dimer \(Q=\{1,2\}\), propose the simultaneous flip of both spins and accept with the Metropolis rate. Write

\[
\rho=e^{-4\beta J}.
\]

For the dual source pre-state \(D=\{1\}\) and external successful target \(T=\{0\}\), exact canonical aggregation gives

\[
a_{Q,\{1\}}^{\varnothing}(\{0\})=1-\rho,
\qquad
 a_{Q,\{1\}}^{\{2\}}(\{0\})=-(1-\rho),
\]

with every other post-source coefficient cancelling. For every interacting temperature \(\beta J>0\), this record has positive rate, and a terminal horizon immediately after the record gives the normalized block-end factor

\[
\boxed{C_Q(u_1,u_2)=\frac{1-u_2}{2}.}
\]

Around any proposed profile \(p^\star\),

\[
C_Q(u_1,u_2)
=
\frac{1-p_2^\star}{2}
-\frac12(u_2-p_2^\star),
\]

so

\[
\boxed{\kappa_{\{2\}}=-\frac12<0}
\]

for every \(p^\star\). At \(\beta=0\) the offending successful record itself disappears; there is no nontrivial positive-temperature region in this family where the proposed centered block-end condition survives. This was checked by an exact symbolic verifier with no floating-point arithmetic.

Accordingly, the cheap disjoint-block tier should be described as a **cheap representation tier only**. It is not a cheap extension of the paper's centered-moment theorem.

The sharp retention summary is therefore

\[
\boxed{\text{duality is retained exactly; representation is credible but unproved;}}
\]

\[
\boxed{\text{the positivity characterization, centered-order package, pure-death comparison and convergence package are not retained.}}
\]

## 3. New applications opened by multi-site updates

The single-site-flip restriction excludes several standard IPS whose elementary physical move changes more than one occupation variable. The multi-site extension brings these models into the algebraic scope of the signed monomial dual immediately. Whether they obtain a patch **representation theorem** depends on completing the block/hyperpatch factorization proofs above. None of the applications below currently inherits the paper's positivity, comparison or convergence conclusions.

### Cheap/non-overlapping block tier

This tier is mathematically real but is populated mainly by block samplers and deliberately partitioned block dynamics rather than by the most natural translation-invariant lattice gases.

**Fixed-partition Ising block dynamics.** Continuous-time heat-bath or Metropolis dynamics on a fixed partition into bounded blocks can be organized as a finite-state process on each super-block, with simultaneous within-block changes decomposed into the corresponding flip subsets. Once the disjoint-block factorization is written, the patch statement would give an exact one-block representation for spin monomials and a finite transfer-matrix description of each completed block contribution. What it does not give generically is centered-moment positivity: the explicit dimer Metropolis calculation above already disproves that hope for a standard interacting two-site block-flip family.

**Hard-core/disjoint-clique block dynamics.** Binary occupation variables on a fixed partition of cliques or bounded blocks fit the same super-block formalism, with inadmissible hard-core transitions assigned zero rate. The prospective theorem gives an exact block-patch representation and finite-dimensional component sign problem. Again, this is primarily a demonstration of representation scope; existing block-dynamics technology is already strong, and no new mixing theorem follows from the patch construction alone.

The dimer Metropolis example itself is useful as a calibration model: it lies squarely in the cheap representation class while simultaneously showing that the paper's centered positivity structure does not survive merely because the update blocks are disjoint and finite.

### Overlapping envelope-hyperpatch tier

This is where the important new physical models lie.

**Speed-change exclusion.** Nearest-neighbour occupations are exchanged at a local rate depending on the surrounding environment. The edge supports overlap, and the multilinear expansion of the speed produces signed `stay/move' dual outcomes. Once the hyperpatch theorem is proved, it would give an exact occupation-moment representation that averages those environmental modes along one connected bond-history component before absolute values are taken. This is probably the cleanest nontrivial model on which to prove the envelope factorization itself. SSEP is the degenerate calibration point: its monomial dual is already positive exclusion, so patches add no cancellation.

**Kawasaki dynamics for the Ising lattice gas.** The elementary move exchanges two neighbouring occupations, with rates determined by a local energy change. This was the model that exposed the geometry/sign issue: revealing which endpoint actually carries the post-event dual line reveals the sign-bearing branch, while cutting the whole edge envelope retains the routing variable inside the hyperpatch. A proved hyperpatch representation would give exact formulas for occupation monomial expectations with local cancellation of the environment-dependent exchange modes. It would not give a common invariant law; Kawasaki conserves particle number, so any later relaxation result must be fixed-density/sectorwise.

**Facilitated exclusion processes.** These are conservative analogues of kinetically constrained spin models: a particle jump to a neighbouring vacancy is allowed only when a local facilitation condition is satisfied. This is probably the most natural application for the audience of the binary paper. It was excluded solely because its elementary facilitated move is a bond move rather than a single-site refresh. The envelope construction would, if proved, give an exact hyperpatch representation of occupation moments in which the signed expansion of the facilitation constraint is averaged across successive overlapping bond moves. The one-dimensional nearest-neighbour geometry makes facilitated exclusion the best candidate for an explicit first hyperpatch calculation. No hyperpatch positivity result is currently known.

**Kob--Andersen kinetically constrained lattice gases.** The Kob--Andersen class consists of exclusion/Kawasaki-type particle moves subject to local vacancy constraints before and after the move. Conceptually this is the strongest extension of the paper's KCSM story: the patch mechanism would move from single-site KCSMs to their conservative kinetically constrained lattice-gas counterparts. A proved representation would average the signed constraint expansion over connected histories of constrained exchanges. Any useful centered correlation inequality or sectorwise relaxation estimate would require additional model-specific work; nothing in the present retention analysis supplies it automatically.

**Pair-contact process with diffusion.** PCPD combines nearest-neighbour diffusion with genuinely multi-site pair reactions, including simultaneous pair annihilation. Both the diffusion and pair-reaction supports overlap. The hyperpatch architecture would place density and higher occupation moments of this reaction-diffusion model inside the same signed representation framework. Positivity is not expected automatically; the realistic first payoff would be the exact representation and a cancellation majorant sharper than raw absolute FK, if that can be quantified.

**Annihilating random walks with pairwise immigration/deposition.** Pair deposition is literally a simultaneous two-site update, and the jump/annihilation moves also have overlapping local supports. These models are useful less as a novelty target than as an exact benchmark: several related systems have independent Pfaffian structure. A hyperpatch formula could therefore be checked against known exact correlation formulas and used to validate component bookkeeping.

**Local-flip tiling dynamics.** Domino and lozenge Glauber moves simultaneously alter several binary edge-occupation variables, with overlapping face/vertex supports. They would require the envelope machinery plus an additional constrained-state-space treatment because the binary variables satisfy matching/tiling constraints. This is a real extension of scope but not a first application, since much of the extra work is unrelated to the patch mechanism itself.

The application ranking is therefore not the same as the proof-cost ranking. For proving the extension, the sensible order is fixed disjoint blocks first, then speed-change exclusion as the cleanest overlapping test. For motivating the extension to the paper's audience, the strongest examples are **facilitated exclusion and Kob--Andersen**: they are natural conservative kinetically constrained systems that the single-site-flip generator simply cannot express.

The overall assessment is consequently narrow but positive. Multi-site updates do appear to support the core idea of **conditioning on a coarse successful skeleton and averaging signed local histories before absolute values**, provided overlapping moves are handled by deterministic envelopes and hyperpatch components. The exact duality is already established and the representation proofs look technically plausible. What should not be claimed is that the main theorem package of the binary paper comes along for free. The dimer counterexample shows that even the cheap block class immediately loses the centered end-factor sign structure, and the pure-death comparison identity needed for the convergence theorem is absent once hidden component histories have different active-time integrals. The credible extension is therefore a broader **representation/cancellation framework**, with new conservative KCM, Kawasaki/exclusion and reaction-diffusion applications; any positivity, order or ergodicity theorem beyond that must be earned separately model by model.