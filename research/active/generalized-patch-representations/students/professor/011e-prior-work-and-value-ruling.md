# 011e: prior-work sanity check and value ruling

Date: 2026-08-17

## 1. What Part D does and does not establish

Assignments 011a--011d establish a mathematically nontrivial chain:

\[
|Q_t|\le R_t\le A_t,
\qquad
R_{t+s}\le R_tR_s,
\]

where `R_t` delays absolute values until after killed hidden-patch averaging, and `A_t` removes signs before that averaging.

For additive support weight, collision-free patch-tree domination yields a finite multitype renewal kernel built from

\[
|b_u e^{tK}e_r|.
\]

A subcritical exponentially tilted next-generation kernel gives volume-uniform exponential control of a site-oscillation seminorm. The exact one-neighbour Potts interpolation gate shows this criterion can be strictly weaker than the corresponding raw absolute-FK first-moment criterion.

That is genuine mathematics beyond the one-line inequality `|EX|<=E|X|`.

It is **not yet** a new natural-model ergodicity theorem.

## 2. Standard ingredients already in the literature

Several downstream ingredients are established theory and cannot carry novelty.

### Dobrushin/oscillation contraction

Dobrushin's classical work on locally interacting Markov processes already develops contraction/ergodicity mechanisms for systems with many locally interacting components. Modern Dobrushin-coefficient and Hopf-oscillation work treats contraction of Markov operators and semigroups in oscillation/variation seminorms systematically.

Thus the implication

\[
\text{positive operator/seminorm contraction}
\Longrightarrow
\text{exponential ergodicity or oscillation decay}
\]

is standard.

### The principal's existing finite-alphabet IPS criterion

More directly, Głuchowski--Menz, *Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems* (J. Stat. Phys. 192, 6, 2025), already introduces a representational seminorm for arbitrary finite alphabets and proves an update-coefficient recursion implying uniform exponential covariance decay. The paper explicitly treats product bases, coefficient absolute values, continuous-time recursion and applications including the two-stage contact process.

Therefore the **downstream theorem form** in 011d -- a finite-dimensional coefficient/seminorm criterion implying exponential decay -- is not a new contribution by itself.

### Multitype age-dependent renewal

The first-moment equation

\[
Z=h+\mathcal K*Z
\]

and the use of a multitype next-generation/spectral-radius criterion are standard Bellman--Harris / age-dependent branching-process machinery. This part of 011d is an implementation device, not a novelty claim.

### Signed-semigroup domination

The raw comparison

\[
|b e^{tK}f|\le |b|e^{tM}|f|
\]

with `M` obtained by absolute off-diagonal domination is standard signed-matrix/positive-semigroup technology.

## 3. What still appears project-specific

The literature comparisons above do **not** identify an equivalent of the particular intermediate majorant

\[
R_t,
\]

which is produced by:

1. revealing the successful typed skeleton;
2. keeping post-source outcomes hidden;
3. inserting the noncemetery/killed factor needed because bare factorization is false;
4. averaging each signed local hidden history;
5. taking absolute values only after that patch average;
6. retaining enough typed boundary data to prove
   \[
   R_{t+s}\le R_tR_s.
   \]

This remains part of the same plausible novelty anchor as the killed typed patch representation itself.

Assignment 011 also proves that the improvement can be strict and can cross the raw absolute-FK renewal threshold in an exact positive-rate coefficient family.

## 4. Why this does not justify another research block

The exact separation gate was deliberately a **structural interpolation**, not a published difficult model. It proves that the new majorant is mathematically stronger than the raw absolute dual majorant. It does not show that it proves a theorem unavailable from existing coupling, Dobrushin/representational-seminorm, attractiveness or model-specific methods.

For the natural models already selected independently of the criterion:

- two-stage contact/SIRS fail pointwise patch positivity, and their reproducing outgoing source-line kernel carries essentially no useful sign cancellation beyond the raw first-moment route;
- Potts Metropolis has strict local cancellation, but its high-temperature ergodicity/mixing regime is already accessible by established methods, while the exact gate in 011d modifies the neighbour-dependent interaction strength specifically to separate the two majorants.

Opening another model search would violate the opportunity-cost discipline fixed after Assignments 009--010. Generic `d>3` remains even less attractive because it overlaps external-positivity theory.

## 5. Contribution-status ruling

The correct status after Assignment 011 is:

- killed typed patch factorization / representation: **still plausibly new theorem/mechanism**;
- patch-variation kernel `R_t` and its submultiplicativity: **plausibly new corollary/extension of that mechanism**, but historical priority not established;
- oscillation/renewal implication once a positive contraction kernel is available: **known ingredients / standard downstream machinery**;
- exact one-neighbour interpolation threshold separation: **correct structural gate, not a natural application contribution**.

Accordingly Assignment 011 does not meet the continuation bar `CONTINUE-KILLED-CANCELLATION`: it does not produce a new natural-model consequence or a downstream theorem whose mathematical content is independent of established contraction/renewal theory.

It also does not fit `STOP-CANCELLATION-ONLY-LOCAL`, because composability was successfully proved.

The correct pre-registered ruling is

\[
\boxed{\texttt{STOP-CANCELLATION-NO-QUALITATIVE-GAIN}.}
\]

The programme should stop deliberately here. The retained research output is the finite-state killed typed representation, its cemetery-aware factorization, the local short-`OO` obstruction, and the new-looking intermediate patch-variation majorant. No generic `d>3` block and no further application search should be opened.