# 008c: signed Feynman--Kac duality and hidden-skeleton factorization

Date: 2026-08-17

This note sharpens the two novelty-sensitive interfaces of Assignment 008. It corrects any impression from `008b` that signed Feynman--Kac duality itself might be unusual, and then separates that prior art from the killed typed patch factorization.

## 1. Signed Feynman--Kac duality is directly prior art

A decisive predecessor is:

- D. A. Dawson and A. Greven, *Multiscale analysis: Fisher--Wright diffusions with rare mutations and selection, logistic branching system*, arXiv:1007.5462 (2010), later in *Probability in Complex Physical Systems*.

Their Section 3 constructs a function-valued branching/coalescing dual for a finite type-space Fisher--Wright model. Proposition 3.2 is explicitly titled **"Duality relation -- signed with Feynman--Kac dual"**. At a selection event, the function-valued component acquires a signed difference term; the duality formula compensates this with an exponential Feynman--Kac factor. The authors explicitly note the difficulty caused by the interplay of cancellation and exponential growth and then construct a different nonnegative dual in a restricted setting.

A broader companion is:

- D. A. Dawson and A. Greven, *Duality for spatially interacting Fleming--Viot processes with mutation and selection*, arXiv:1104.1099 (2011).

This develops function-valued duals driven by coalescing/branching random walks for general type space and, for finite type spaces, set-valued and tableau-valued Markov duals suitable for long-time analysis. Its finite-type theory contains a duality relation for arbitrary finite-state Markov chains as a special case.

**Novelty consequence.** "finite types + branching genealogy + signed function-valued update + Feynman--Kac factor" is directly known. This substantially lowers any standalone novelty claim for Assignment 001.

The distinction from the current IPS construction remains:

1. Dawson--Greven treat measure-valued Fisher--Wright/Fleming--Viot models with selection/mutation, not arbitrary finite-range single-site replacement IPS on a product configuration space;
2. their dual state includes a function-valued component and genealogical partitions, not the reference-indicator typed active-set process of Assignment 001;
3. no source-successful interaction skeleton that forgets the signed branch outcome and no one-site patch averaging was found there.

Accordingly item 1 remains **`known ingredients, assembly plausibly new`**, but the "signed FK" ingredient itself is now explicitly classified as known.

## 2. Marked-Poisson ancestor/skeleton constructions are also directly known

A second decisive predecessor is:

- R. Fernández, P. A. Ferrari and N. L. Garcia, *Perfect simulation for interacting point processes, loss networks and Ising models*, Stochastic Processes Appl. 102 (2002), 63--88; arXiv:math/9911162.

Their abstract describes a two-step method:

1. perfectly generate a finite random relevant portion of a **space-time marked Poisson process**, namely the ancestors of the queried object;
2. run a subsequent **cleaning** procedure according to the target interaction rules.

Thus the broad architecture "first reveal a relevant Poisson ancestor geometry, then process additional marks/interactions on that geometry" predates the patch programme.

Together with Lubetzky--Sly information percolation, this means that partial graphical revelation, backward ancestor discovery, and conditional processing of remaining update randomness are established probability techniques. They receive no standalone novelty credit.

## 3. Exact point of comparison with information percolation

Source:

- E. Lubetzky and A. Sly, *Information percolation and cutoff for the stochastic Ising model*, J. Amer. Math. Soc. 29 (2016), 729--774; arXiv:1401.6065.

Information percolation exposes the backward dependency history of target spins in a graphical update construction and decomposes the spacetime history into information-flow clusters. The geometry can be handled separately from update randomness that determines spin values. This is a very close conceptual predecessor to the phrase "reveal a coarse skeleton and average hidden local randomness later."

It does **not** directly reproduce the package being audited:

- there is no signed duality function or Feynman--Kac multiplicative weight;
- no selected update hides a signed source-outcome branch whose conditional distribution is determined by absolute dual coefficients;
- no local contribution is a conditional expectation of a signed FK factor over a one-site source-time strip;
- there is no typed target conflict sending the dual to cemetery and thereby deleting future no-record constraints;
- hence there is no analogue of the Assignment-002 killed/noncemetery repair.

## 4. Why ordinary marked-Poisson factorization does not subsume Assignment 002

Conditional independence of marks on disjoint Poisson regions is standard. If the Assignment-002 theorem merely said "disjoint one-site strips contain independent Poisson marks", it would have no novelty value.

The nontrivial interface is the event being conditioned on. In the typed dual, the bare coarse record list does **not** factor: an incoming target conflict can enter cemetery, after which later local clocks cease to constrain the record list. Thus the coarse-skeleton event is a union of a conflict branch and a surviving branch with future local no-record constraints. Assignment 002 gives an exact finite counterexample to bare factorization and repairs it only after multiplying by the noncemetery indicator; the resulting weighted Mecke identity is then a product of local consistency factors.

No source located in the classical graphical-duality, clan-of-ancestors, information-percolation, or Feynman--Kac literatures contains this same combination:

> signed FK dual + coarse successful record that forgets branch type + typed target conflicts + cemetery-induced loss of future constraints + exact killed/noncemetery patchwise factorization.

This is a negative search result, not a proof of priority, but it is the strongest novelty finding in the audit so far.

## 5. Item-2 status

### Killed typed patch factorization / representation

**Status: `plausibly new theorem/mechanism`.**

The surrounding ingredients are old:

- graphical Poisson constructions;
- ancestor clans/backward dependency histories;
- partial revelation of marked update randomness;
- signed Feynman--Kac duality;
- conditional independence of disjoint Poisson regions.

The exact theorem connecting them in the typed signed dual, especially the cemetery obstruction and killed/noncemetery repair, was not found in equivalent form.

This is currently the primary novelty anchor of the fixed package. The later transfer and positivity results should be assessed as consequences/interfaces built on it rather than used to retroactively claim the standard ingredients.