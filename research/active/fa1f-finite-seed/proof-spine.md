# Proof spine

This file records the final mathematical state of the **closed** FA-1f finite-seed programme.

## Main target

For one-dimensional hard FA-1f with vacancy density `q in (0,1)`, started from the configuration `eta^{0}` with exactly one vacancy at the origin, prove

$$
P_t f(\eta^{0})\longrightarrow \mu_p(f),\qquad p=1-q,
$$

for every local function `f`.

Equivalently, it is enough to prove

$$
P_t\chi_A^*(\eta^{0})\longrightarrow0
$$

for every finite nonempty `A`.

The mathematical problem remains open. This workspace is closed because the two concrete mechanisms developed here were shown not to reduce the hard obstruction.

## Settled edges

### E0. Centered-moment reduction

**Status:** verified/standard.

Centered monomials form a basis for local functions and have zero `mu_p` mean for nonempty index sets.

### E1. Exact positive finite-set dual after the harmonic transform

For

$$
H(A,\eta)=q^{-|A|}\chi_A^*(\eta),
$$

the transformed finite-set chain has generator

$$
\mathcal G g(A)
=
\sum_{i\in A}
\left[
\sum_{R\subseteq\{i-1,i+1\}}
q^{|R|}p^{2-|R|}
 g\bigl((A\setminus\{i-1,i+1\})\cup R\bigr)
-g(A)
\right].
$$

The exact semigroup duality is

$$
P_t\chi_A^*(\eta)
=
q^{|A|}\mathbf E_A\left[
q^{-|\mathcal A_t|}\chi_{\mathcal A_t}^*(\eta)
\right].
$$

For the single-vacancy configuration,

$$
P_t\chi_A^*(\eta^{0})
=
q^{|A|}\left(1-q^{-1}\mathbf P_A(0\in\mathcal A_t)\right).
$$

**Status:** verified for current research use.

**Decisive pointer:** `students/student-a/001-centered-h-transform.md`, Sections 1--4.

**Strategic result:** demoted as a proof mechanism. On finite cycles it is an invertible similarity transform of FA-1f; the transformed process is not attractive or additive, has the same basic front identities, and the available BABP comparison does not import an all-parameter finite-seed theorem.

### E2. Unnormalized successful-skeleton / patch transfer

Student A derived the exact Mecke representation before normalization, the hard-FA consistency probabilities and unnormalized patch amplitudes, and the zero/one/two-record contributions to the singleton deviation.

The restricted same-source transfer has a genuine mass deficit, but the complete first branching transfer is critical: the missing mass is routed exactly into child-source sectors.

More strongly, let `K_t(A,B)` be the coefficient matrix of the centered semigroup,

$$
P_t\chi_A^*=\sum_BK_t(A,B)\chi_B^*.
$$

Let `Q_t=e^{t\mathcal G}` be the E1 Markov semigroup. Then

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B).
$$

Hence

$$
\sum_Bq^{|B|-|A|}K_t(A,B)=1.
$$

**Status:** verified for the strategic decision.

**Decisive pointers:**

- `students/student-a/002-unnormalized-patches.md`, especially Sections 9--14;
- `students/student-a/002-transfer-normalization-clarification.md`;
- `notes/professor-transfer-verification.md`.

**Strategic result:** the unnormalization-only route is closed. Restoring consistency probabilities changes the decomposition but not the conservative `h`-weighted coefficient dynamics.

## Unresolved theorem-level obstruction

A proof of the target would still need genuinely new one-dimensional spatial information, for example a regeneration/coupling theorem behind the vacancy fronts or another mechanism controlling local equilibration from a finite seed. Neither E1 nor the local patch weights provide such a theorem.

The former E3a/E3b goals remain mathematically correct descriptions of what a patch-based extension of the canonical convergence theorem would need:

- control of late successful interactions without uniform pure deaths;
- terminal-dependence relaxation with the full skeleton weight included.

But after E2 these are no longer active proof-spine edges, because no concrete mechanism for either remains.

## Routes eliminated or demoted

- 1D Bernoulli-quench sibling cancellation: permanently closed prior route.
- Centered `h`-transform as a standalone proof strategy: demoted in Meeting 001.
- Unnormalized-consistency-probability contraction: closed in Meeting 002. The full transfer is exactly E1 in different coordinates.
- Any future attempt to turn the simultaneous two-neighbour refresh into an absolute-value sibling contraction: the already closed Bernoulli-quench route.

## Programme decision

**Closed in Meeting 002 on expected-value grounds.**

This is not an impossibility claim about finite-seed FA-1f. The target remains worthwhile and open. The decision is that the group's two concrete leverage points from the principal's patch/centered-moment machinery have both been reduced to the same conservative positive dynamics, and no third target-relevant spatial mechanism is presently identified. Continuing would amount to searching for an unspecified new idea rather than pursuing a live proof edge.
