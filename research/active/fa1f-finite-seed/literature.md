# Literature note

## Active target

One-dimensional hard FA-1f, arbitrary `q in (0,1)`, started from a single vacancy (later finite nonempty vacancy set): convergence on local observables to the Bernoulli equilibrium law.

## Primary open-problem source

Fabio Martinelli, Assaf Shapira, Cristina Toninelli, *Long time behaviour of one facilitated kinetically constrained models: results and open problems*, arXiv:2510.20461 (2025).

- Introduction, Conjecture 1: for every `q in (0,1)` and every initial law which almost surely contains at least one infected vertex, local observables should converge to equilibrium.
- The introduction explicitly names the Dirac mass on a configuration with a single infection at the origin as a natural initial law.
- The paper states that robust tools for the conjecture are not available and identifies non-attractiveness and failure of the usual logarithmic-Sobolev/hypercontractive strategy as principal difficulties.
- Section 6 contains preliminary results for FA-1f started from finitely many vacancies rather than the full convergence theorem.

This source is a recent preprint rather than a published journal paper, but it is by central authors in the subject and directly formulates the exact broader conjecture containing the active target.

## Canonical project source

Maciej Głuchowski and Georg Menz, *Patch representations and convergence for facilitated spin systems*, canonical manuscript in `paper/`.

Relevant locations:

- Theorem A / Section 4: exact patch factorization and patch representation over the successful-interaction skeleton.
- Theorem B / Section 5: patch positivity and positivity of the semigroup in the centered-monomial basis.
- Section 7.1: for hard FA-1f, patch positivity holds and the patch threshold is `p^*=p`; the centered-order comparison by itself does not enlarge the known qualitative class treated by earlier high-density work.
- Section 8.2: the hard-model convergence proof would require model-specific replacements for the two uniform-death estimates; convergence from finitely many vacancies in FA-1f is listed as an unresolved problem.

For patch construction and its proofs this manuscript is authoritative for the project and supersedes the IPS wiki layer.

## Older partial results to keep in view

- Oriane Blondel, Nicoletta Cancrini, Fabio Martinelli, Cyril Roberto, Cristina Toninelli, *Fredrickson--Andersen one spin facilitated model out of equilibrium*, Markov Processes and Related Fields 19 (2013), 383--406. High-vacancy-density convergence under an exponential-tail condition on distances to vacancies.
- Thomas Mountford and Glauco Valle, *Exponential convergence for the Fredrickson--Andersen one-spin facilitated model*, Journal of Theoretical Probability 32 (2019), 282--302. Further high-density exponential convergence.
- Ivailo Hartarsky and Cristina Toninelli, *Kinetically constrained models*, SpringerBriefs in Mathematical Physics 53 (2025), especially Chapter 7 for out-of-equilibrium context.

## Successor check

A targeted search performed when the programme was initialized found no later paper claiming the full single-vacancy/all-`q` convergence theorem. This is not yet a publication-level novelty audit. Before a theorem claim, search 2025--2026 successors, citation chains, duality terminology, finite-seed/front results, and related branching/coalescing processes in detail.

## Representation novelty warning

The centered `h`-transform process in `notes/professor-initial-reduction.md` may already exist under another duality or quasi-duality name. The programme does not depend on novelty of that representation; what matters is whether it gives a new proof of the open convergence theorem. Student A should nevertheless identify prior occurrences because known structure may be useful.