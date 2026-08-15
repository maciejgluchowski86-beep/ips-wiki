# Proof spine

This file is maintained by the Professor.

## Main target

For one-dimensional hard FA-1f with vacancy density `q in (0,1)`, started from the configuration `eta^{0}` with exactly one vacancy at the origin, prove

$$
P_t f(\eta^{0})\longrightarrow \mu_p(f),\qquad p=1-q,
$$

for every local function `f`.

Equivalently, it is enough to prove convergence of all centered monomials

$$
P_t\chi_A^*(\eta^{0})\longrightarrow 0,
\qquad
\chi_A^*(\eta)=\prod_{i\in A}(\eta(i)-p),
$$

for every nonempty finite `A`.

## Obstruction map

### E0. Centered-moment reduction

**Statement.** Since centered monomials form a basis for local functions and `mu_p(chi_A^*)=0` for nonempty `A`, the main target follows from decay of every nonempty centered monomial.

**Status:** verified/standard.

**Owner:** Professor.

**Decisive pointer:** canonical patch paper, Section 5.4.

### E1. Exact positive finite-set dual after the harmonic transform

Define

$$
H(A,\eta)=q^{-|A|}\chi_A^*(\eta).
$$

There is a Markov process `(\mathcal A_t)` on finite nonempty subsets of `Z` with generator

$$
\mathcal G g(A)
=
\sum_{i\in A}
\left[
\sum_{R\subseteq\{i-1,i+1\}}
q^{|R|}p^{2-|R|}
\,g\bigl((A\setminus\{i-1,i+1\})\cup R\bigr)
-g(A)
\right].
$$

The infinite-volume semigroup duality is exact:

$$
P_t\chi_A^*(\eta)
=
q^{|A|}\mathbf E_A\left[
q^{-|\mathcal A_t|}\chi_{\mathcal A_t}^*(\eta)
\right].
$$

For the one-vacancy configuration `eta^{0}`,

$$
P_t\chi_A^*(\eta^{0})
=
q^{|A|}
\left(
1-q^{-1}\mathbf P_A(0\in\mathcal A_t)
\right).
$$

**Status:** verified for current research use by an independent Student A derivation, including nonexplosion and the infinite-volume semigroup passage.

**Owner:** retained as a Professor tool; not the active proof route.

**Decisive pointer:** `students/student-a/001-centered-h-transform.md`, Sections 1--4.

**Structural qualification.** On every finite cycle the duality matrix is invertible and

$$
G^{(V)}=\mathbf H(L^{(V)})^{\mathsf T}\mathbf H^{-1}.
$$

The transformed process is Bernoulli(`q`) reversible but is not attractive or additive, is cancellative only at `q=1/2`, has the same basic vacancy-front generator identities as hard FA-1f, and has equilibrium Dirichlet form comparable to BABP without gaining a known all-parameter finite-seed theorem. The local simultaneous-neighbour algebra is exactly the algebra of the closed Bernoulli-quench sibling route. Thus E1 is an exact positive reformulation, not presently a simplification of the theorem.

**Decisive pointer for the qualification:** `students/student-a/001-centered-h-transform.md`, Sections 7--15.

### E2. Unnormalized successful-skeleton / patch expansion for hard FA-1f

The canonical patch paper proves that, after fixing the successful-interaction skeleton, the local marked histories factor over patches. In the canonical proof the skeleton marginal contains the consistency probabilities while the displayed patch contributions are normalized conditional expectations.

The active route is to put those factors back together and work with the unnormalized amplitudes

$$
\widehat C(P)
:=
\mathbf E_P\left[F(P)\mathbf 1_{\operatorname{Con}(P)}\right]
=
\mathbf P_P(\operatorname{Con}(P))C(P),
$$

and analogously for end patches. The point is not to obtain another local cancellation constant. It is to expose the actual probability cost of maintaining a hard-model successful skeleton, which normalization can hide.

**Status:** open as a research reduction. The underlying factorization is canonical; the exact hard-FA specialization, all unnormalized patch formulas, and the correct full-skeleton measure bookkeeping have not yet been independently derived in the active workspace.

**Owner:** Graduate Student A.

**First required output:** a complete exact table of unnormalized FA-1f patch amplitudes and the corresponding skeleton-intensity factors, followed by a check on the smallest full skeleton in which one successful record creates all of its source/target descendant patches. A single ancestry-chain calculation is not enough because every successful record transmits dependence to both neighbours.

### E3. Model-specific replacement for the two hard-model failures of Theorem C

The canonical convergence theorem uses uniform pure deaths twice. Hard FA-1f has no such component. A successful patch route must replace both uses at the level of the actual unnormalized skeleton expansion.

#### E3a. Late-interaction control

Find a target-relevant estimate showing that the total contribution of skeletons with a successful interaction after a cut time `T` becomes negligible as `T -> infinity`, for the one-vacancy centered observable or an equivalent quantity. The estimate may be polynomial; exponential decay is not required.

The canonical pure-death proof obtains this from an exponential factor along one backward chain. In hard FA-1f the naive chain-only unnormalized calculation appears critical, so any gain must use more than one-dimensional chain weight: full branching geometry, coalescence/overlap, recurrence, terminal structure, or another model-specific mechanism.

**Status:** open.

#### E3b. Terminal-dependence relaxation on no-late-interaction skeletons

On skeletons with no successful interaction after `T`, prove that the remaining dependence on the terminal one-vacancy configuration converges to the equilibrium terminal value in a summable/controlled way after the unnormalized skeleton weights are included.

The one-site empty-target relaxation in the canonical formulas is explicit, but in the hard model it is not by itself enough: one must control the total skeleton weight multiplying the relaxing end factors without the pure-death comparison majorant.

**Status:** open.

### E4. Recombination

Combine E3a and E3b with finite propagation and the canonical patch representation to prove decay of every centered monomial from `eta^{0}`.

**Status:** open; downstream of E2/E3.

## Current first unresolved edge

**E2 is now the current bottleneck.**

The exact `h`-transform E1 has been settled and is not being pursued as the main mechanism. Before investing in a global patch argument we need to know what the unnormalized hard-FA skeleton actually weighs after *all* patches created by the first few successful records are included.

The most informative immediate question is whether the apparent criticality of a single backward outgoing chain survives the first full branching composition. If the full unnormalized expansion merely reproduces the closed sibling algebra or has no target-relevant loss after that composition, this patch subroute should be downgraded or closed quickly.

## Mathematically distinct alternative route

E1 remains available as an exact identity and may become useful if a genuinely new probabilistic theorem for the transformed process appears. It is not an active alternative merely because it exists.

A genuinely different later route would have to use external finite-seed FA structure not encoded by either the transformed process or the local patch weights, for example a regeneration theorem behind the physical vacancy fronts. No such route is currently developed enough to enter the spine.

## Routes eliminated or demoted

- 1D Bernoulli-quench sibling cancellation: closed project route; do not retry. Student A found that its local algebra reappears exactly in the simultaneous-neighbour term of E1. Any future absolute-value contraction based on those two sibling weights is the closed route.
- Centered `h`-transform as a standalone proof strategy: **demoted after Meeting 001**. E1 is correct but finite-volume similarity, identical front identities, lack of attractiveness/additivity, and the BABP comparison give no present simplification.
- 2D FA-1f local signed-move cancellation for the relaxation logarithm: different target and closed route.
- 2D nearest-vacancy/electrical-capacity observable: different target and closed route.

## Revision note

Meeting 001 materially changed the spine. Student A verified E1 but also showed that it is an invertible finite-volume coordinate transform and that the obvious probabilistic handles do not improve the finite-seed problem. The programme therefore pivots within the same target from E1 to the unnormalized patch/skeleton route E2. The exact student evidence is `students/student-a/001-centered-h-transform.md`.