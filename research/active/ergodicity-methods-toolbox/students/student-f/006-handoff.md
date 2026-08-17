# Student F Assignment 006 handoff

Date: 2026-08-17

Assignment 006 is complete. Five entries were committed individually. Three assigned targets survived primary-source inspection directly. Two further entries are declared substitutions after the bounded spectral-profile and fully-unconstrained-refresh searches failed. The full-Cheeger/conductance target also failed its renewed bounded source search; I did not manufacture a sixth page merely to hit the assignment count.

## Entries and commits

1. `entries/hierarchical-renormalisation-spectral-gap-recursion.md`
   - commit `a9dcd61a384ed60b7c3ec72c9f609e896d0bf61a`
   - renormalised Brascamp--Lieb inequalities propagate a Glauber spectral-gap estimate through a hierarchy of effective measures; this tracks critical finite-volume relaxation scaling.

2. `entries/infinite-dimensional-harris-levy-spde.md`
   - commit `bcefd9cf062470058b3d1a93d6faf5466384e1c0`
   - genuine Hilbert-space Harris theorem: dissipative moment drift plus regularisation into a compactly embedded topology, irreducibility and strong Feller give a small set and exponential total-variation convergence.

3. `entries/projective-consistency-splitting-gibbs-equilibrium.md`
   - commit `8bb2012373892522313cdfdbdb73e83cd9872a66`
   - exact marginal consistency of finite-depth hard-core Gibbs distributions on a Cayley tree is equivalent to boundary-message recursions; projective extension gives the infinite splitting Gibbs law, which is a reversible equilibrium law for the loss-network process.

4. `entries/relative-entropy-loss-gibbs-attractor.md`
   - commit `54619273988a411f2e9babbfe22230d8d3a40edf`
   - **substitution for spectral profile/evolving sets**: entropy density is a Lyapunov functional; zero entropy loss implies Gibbs; therefore every omega-limit point of an irreversible translation-invariant IPS trajectory is Gibbs.

5. `entries/stochastic-localization-ising-glauber-gap.md`
   - commit `5a1b057eeafdd0649bb6f9b8f825a02c2524d598`
   - **substitution for direct constrained-to-unconstrained refresh comparison**: stochastic localization reduces a general high-temperature Ising interaction to random rank-one needles while the true Glauber Dirichlet form is controlled, yielding a Poincare/spectral-gap bound.

## Source qualifications and exact pinpoints

### Hierarchical renormalisation recursion

Primary: Roland Bauerschmidt and Thierry Bodineau, *Spectral Gap Critical Exponent for Glauber Dynamics of Hierarchical Spin Models*, Communications in Mathematical Physics 373 (2020), 1167--1206, DOI `10.1007/s00220-019-03553-x`.

- Section 2, Theorem 2.1: one-step Brascamp--Lieb recursion from a renormalised/coarse measure to the preceding scale under assumptions (A1)--(A3).
- Corollary 2.2: iteration of the matrix-valued inequality through all renormalisation scales.
- Corollary 2.3: spectral-gap bound from the accumulated Brascamp--Lieb matrix.
- Theorems 1.1--1.2 and Sections 3--4: hierarchical four-dimensional `|phi|^4`, Sine--Gordon and Discrete Gaussian applications.

The interface is the **sequence of renormalised measures/effective potentials**. It is distinct from geometric block bisection, Lu--Yau conditioning, and the KCM nested-droplet recursion because the probability measure itself changes at every scale.

### Infinite-dimensional Harris/Lyapunov

Primary: Enrico Priola, Armen Shirikyan, Lihu Xu and Jerzy Zabczyk, *Exponential ergodicity and regularity for equations with Levy noise*, Stochastic Processes and their Applications 122 (2012), 106--133, DOI `10.1016/j.spa.2011.10.003`.

- Assumption 2.2: dissipative diagonal linear part, bounded Lipschitz drift, nondegenerate cylindrical symmetric alpha-stable noise and the required summability/regularity.
- Theorem 2.10: abstract skeleton-chain Harris criterion from Lyapunov contraction plus a TV small-set condition.
- Theorem 2.8: unique invariant law and exponential total-variation convergence with a polynomial moment weight.
- Section 5, Step 3 and Lemma 4.2: Lyapunov function `V(x)=|x|^p` and drift.
- Lemma 4.3: regularisation into `H_epsilon`, compactly embedded into the ambient Hilbert space.
- Lemma 5.1 plus Theorem 2.5: irreducibility and strong Feller used to obtain uniform minorisation on the compactified Lyapunov sublevel.
- Example 2.9: semilinear stochastic heat equation application.

This adds a genuine infinite-dimensional classical-Harris proof rather than Hairer's asymptotic binding mechanism.

### Exact projective consistency

Primary: James Martin, Utkir Rozikov and Yuri Suhov, *A Three State Hard-Core Model on a Cayley Tree*, Journal of Nonlinear Mathematical Physics 12 (2005), 432--448, DOI `10.2991/jnmp.2005.12.3.7`.

- Section 2, equation (2.1): finite-depth Gibbs distributions with boundary activities.
- equation (2.2): exact compatibility under summing out the newest boundary sphere; the paper states that compatibility determines a unique infinite cylinder measure.
- Proposition 1: compatibility iff the boundary-activity ratios satisfy the explicit recursion (2.3a)--(2.3b).
- Proposition 2: the resulting infinite measure is Gibbs for the hard-core specification.
- Theorem 1: unique translation-invariant splitting solution for every activity within that restricted class.
- Abstract/Section 1: splitting Gibbs measures are reversible equilibrium distributions for the continuous-time nearest-neighbour loss-network process.

**Scope caveat for Professor audit:** the source explicitly treats the `mu^(n)` as finite-volume Gibbs distributions and proves exact projective consistency; it does not separately formulate a theorem saying that each `mu^(n)` is invariant for a named finite-volume Markov chain. The infinite projective law is explicitly an equilibrium/reversible law of the interacting process. I therefore titled and wrote the page around *projective consistency of Gibbs marginals*, not around a false claim that finite-volume chain invariance was proved. If Assignment 006 is read as requiring finite-volume dynamical invariance literally at every level, this entry should be rejected or reclassified rather than silently strengthened. The projective-extension mechanism itself is exact and load-bearing.

### Relative-entropy loss / Gibbs attractor substitution

Primary: Benedikt Jahnel and Jonas Koppl, *Dynamical Gibbs Variational Principles for Irreversible Interacting Particle Systems with Applications to Attractor Properties*, Annals of Applied Probability 33 (2023), 4570--4607, DOI `10.1214/22-AAP1926`.

- Proposition 2.5: nonpositivity/monotonicity of relative-entropy density along the IPS evolution.
- Theorem 2.6: dynamical Gibbs variational principle; the approximating entropy loss exists, is upper semicontinuous and nonpositive, and zero entropy loss implies membership in the Gibbs set under (R1)--(R6), (S1)--(S4).
- Theorem 2.10: every weak omega-limit point of a trajectory of translation-invariant initial laws is Gibbs for the stationary specification.
- Proposition 3.18 and Section 3.5: a non-Gibbs law has a weak neighborhood on which every short trajectory loses a fixed positive amount of entropy density; recurrence to such a neighborhood infinitely often contradicts the lower bound on relative entropy density.

This is not an LSI page: there is no uniform entropy-production constant and no rate. It is a qualitative attractor mechanism, valid for fairly general irreversible IPS and compatible with phase coexistence.

### Stochastic-localization substitution

Primary: Ronen Eldan, Frederic Koehler and Ofer Zeitouni, *A Spectral Condition for Spectral Gap: Fast Mixing in High-Temperature Ising Models*, Probability Theory and Related Fields 182 (2022), 1035--1051, DOI `10.1007/s00440-021-01085-x`.

- Theorem 1: for a finite Ising measure with `0 <= J < I`, the natural heat-bath Glauber Poincare inequality has continuous-time gap at least `1-||J||_op` in the paper's all-sites-rate-one normalization (equivalently `(1-||J||_op)/n` for one uniformly chosen update per discrete step).
- Lemma 8: sharp terminal Poincare inequality for the rank-one Ising model.
- Lemma 9: the true Glauber Dirichlet form is a supermartingale under the localization flow.
- Section 2: the stochastic measure-valued flow removes interaction directions until rank at most one.
- Section 3 and Theorem 11: mixing-time consequence.
- Section 4: structural rank-one/needle decomposition.
- Section 5: dense high-temperature examples including Sherrington--Kirkpatrick.

This is distinct from the live spectral-independence page: spectral independence controls conditional influence matrices and invokes local-to-global expansion, whereas stochastic localization randomizes the external field and lowers the rank of the interaction while transporting the functional inequality along a measure-valued stochastic flow.

## Negative taxonomy results

### Target 1: full Cheeger/conductance positive relaxation in a spin system

The renewed search was kept bounded as assigned and again did **not** produce a distinct positive-relaxation interface. The spin-system sources located use full conductance/Cheeger primarily in the opposite direction, to exhibit bottlenecks and prove exponentially **slow** mixing. For example, Potts/Ising papers with positive rapid-mixing regimes typically prove those upper bounds by coupling, block dynamics, comparison, spectral independence or entropy factorization; their conductance arguments control the low-temperature slow-mixing side. Positive conductance estimates found in sampling literature generally reduce to multicommodity/canonical-path congestion, already represented by the live comparison page, or to the live large-set/warm-start RFIM interface.

No page was written. This target has now failed two bounded searches and should not be reopened generically without a concrete named primary source whose positive theorem actually uses a full Cheeger lower bound as the load-bearing engine.

### Target 2: spectral profile / evolving sets

The bounded re-search again found the original spectral-profile/evolving-set literature as powerful **general finite-chain/random-walk theory**, but not a primary spin/IPS theorem where the profile itself is the interacting-system proof engine. The exclusion results encountered use coupling/chameleon or other model-specific methods; merely appending a generic profile inequality to an interacting chain would violate the anti-padding rule.

No spectral-profile page was written. The replacement is the relative-entropy-loss/Gibbs-attractor entry above. This target has also now failed two targeted waves and should be considered closed absent a named interacting-process source.

### Target 6: direct constrained-to-fully-unconstrained refresh comparison

The targeted KCSM search did not locate a theorem satisfying the assignment's strict distinction. Existing KCSM comparison mechanisms represented in the toolbox compare to a **slower constrained** East process, to long-range constrained dynamics, to renormalised good-block chains, or to CBSEP/g-CBSEP. Proofs routinely use the product-measure/Efron--Stein variance as the unconstrained reference inequality in the background, but I did not find a primary theorem where an independent-refresh Markov chain itself is introduced as the load-bearing comparison dynamics and its updates are quantitatively simulated by legal KCSM moves in a way distinct from canonical paths/good paths/bootstrap closure.

The replacement is stochastic localization for Ising Glauber gaps, discovered during the analytic comparison search. The fully-unconstrained-refresh KCSM target remains uncovered; do not mark it covered by the live one-sided constraint-domination page.

## Taxonomy decisions

- Target 3 survives directly as a genuine infinite-dimensional **classical Harris** proof because compact regularisation is used to manufacture a TV-small set; this is not asymptotic coupling.
- Target 5 survives directly: renormalisation-group spectral-gap recursion is a separate interface because each step changes the effective measure and carries a Brascamp--Lieb matrix through the RG flow.
- Target 4 has an exact projective-law construction, with the finite-volume-dynamical-invariance caveat stated above. The page should survive only if the Professor accepts the assignment's intended emphasis as exact law consistency rather than separately proved invariance of each finite chain.
- Target 2 is replaced by entropy-loss/Gibbs-attractor dynamics.
- Target 6 is replaced by stochastic localization.
- Target 1 receives no replacement because five genuinely distinct entries already emerged and the assignment explicitly says not to force six.

## Further uncovered families

- direct KCSM comparison to a genuinely independent refresh chain remains uncovered under the strict Assignment-006 interpretation;
- exact projective extension of a family that is **explicitly proved invariant for finite interacting Markov chains at every level** would strengthen or replace the Cayley-tree projective page;
- full-Cheeger positive spin relaxation and load-bearing spectral-profile/evolving-set IPS remain closed after two negative bounded searches;
- infinite-volume versions of stochastic localization or related localization-scheme coercivity for interacting fields would be a genuinely new limiting interface if source-supported;
- entropy-loss attractor methods beyond translation-invariant finite-state lattice IPS, especially continuous-spin systems, remain potential breadth targets;
- the previously closed artificial-Nummelin and generic nonreversible sector/hypocoercive searches were not reopened.

No `docs/` or `mkdocs.yml` files were edited. Mechanical validation is left to the principal/orchestrator's post-commit check; this handoff does not claim a validator pass.
