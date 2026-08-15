# Graduate Student A — Assignment 001

Work on branch `research/fa1f-finite-seed`.

Before calculating, read:

- `research/active/fa1f-finite-seed/state.md`;
- `research/active/fa1f-finite-seed/proof-spine.md`;
- `research/active/fa1f-finite-seed/notes/professor-initial-reduction.md`;
- the canonical patch paper in `paper/`, especially Theorem B / Section 5.4, Section 7.1, and Section 8.2;
- Martinelli--Shapira--Toninelli, arXiv:2510.20461, at least the introduction/Conjecture 1 and Section 6 on finite-vacancy FA-1f.

The active theorem is one-dimensional hard FA-1f, every `q in (0,1)`, started from a single vacancy, converging locally to the Bernoulli equilibrium law.

This is **not** a request to revive the closed Bernoulli-quench sibling-cancellation route. That closed route expanded a homogeneous Bernoulli quench and sought a generation-by-generation signed sibling gain; its three-generation calculation restored the bad scaling. The present proposed route starts from a deterministic finite seed and claims an exact positive Markov dual after a centered `h`-transform. Nevertheless, the transformed update refreshes two neighbours simultaneously, so check explicitly whether the calculation is secretly reproducing the old sibling mechanism. If it is, say so and explain exactly where the equivalence occurs.

Your first job is to settle proof-spine edge E1 from first principles.

## 1. Verify or refute the exact transformed dual

For

$$
\chi_A^*(\eta)=\prod_{i\in A}(\eta(i)-p),
\qquad p=1-q,
\qquad H(A,\eta)=q^{-|A|}\chi_A^*(\eta),
$$

check the Professor's claim that the set process with generator

$$
\mathcal G g(A)
=
\sum_{i\in A}
\left[
\sum_{R\subseteq\{i-1,i+1\}}
q^{|R|}p^{2-|R|}
\,g\bigl((A\setminus\{i-1,i+1\})\cup R\bigr)
-g(A)
\right]
$$

satisfies

$$
\mathcal G_A H(A,\eta)=L_\eta H(A,\eta).
$$

Do not stop at the formal identity. Give a correct finite-volume or nonexplosion argument establishing the semigroup duality for finite initial `A`, or identify the exact missing hypothesis if there is one.

Then check the single-vacancy specialization

$$
P_t\chi_A^*(\eta^{0})
=
q^{|A|}
\left(1-q^{-1}\mathbf P_A(0\in\mathcal A_t)\right).
$$

If any displayed identity is false, produce the earliest countercalculation and stop downstream use of it.

## 2. Understand the transformed process beyond the one-particle picture

Assuming the duality is correct, derive the exact transition rules for at least:

- one isolated active site;
- two adjacent active sites;
- two active sites at distance two;
- a finite contiguous interval.

Compute useful generator identities that expose the geometry, including at minimum the drift of `|A|` and of the number of adjacent active pairs if tractable. Check carefully whether Bernoulli(`q`) product measure is invariant for the infinite-volume version.

Determine whether the process is attractive, additive, cancellative, or has an obvious known dual/quasi-dual. Do not infer these from resemblance; prove or disprove each property you use with a smallest example.

A useful compact form to investigate is whether the generator can be decomposed into a BABP-type neighbour-refresh part plus a genuinely simultaneous two-neighbour term, and whether that decomposition helps or merely recreates the previously failed sibling calculation.

## 3. Decide whether E1 creates leverage on E2

The theorem is reduced by E1 to

$$
\mathbf P_A(0\in\mathcal A_t)\to q
$$

for every finite nonempty `A`.

Do one serious obstruction-level probe of this statement. Choose the most informative of the following after you understand the process:

- derive an exact front/edge evolution or a usable regeneration state;
- find a comparison/coupling with a known branching-coalescing process;
- identify a harmonic or Lyapunov quantity that controls local density;
- show by a concrete calculation that the transformed process is essentially no easier than the original FA-1f problem.

The purpose is not to solve E2 in this assignment. It is to determine whether the positive dual is a real reduction or just a change of coordinates.

## 4. Prior-work check

Search specifically for this transformed finite-set process or equivalent local duality under FA-1f duality, quasi-duality, branching-coalescing, neighbour-refresh, and related terminology. Also inspect the old closed 1D sibling-cancellation material if it can be located in repository history. Distinguish:

- same process already known;
- same local process but used for a different theorem;
- genuinely different process;
- old closed mechanism reappearing.

Novelty of the representation is not required, but known theory may solve part of E2.

## Durable output

Commit the decisive mathematics to

`research/active/fa1f-finite-seed/students/student-a/001-centered-h-transform.md`

and update any auxiliary note/code files you need on the same research branch. End with a short handoff to the Professor giving the exact file pointers and the one or two conclusions that should change the proof spine.

Do not switch to another scientific direction. If the transformed dual is sterile or overlaps the closed sibling route, that is a useful result: document it precisely and return it to the Professor.