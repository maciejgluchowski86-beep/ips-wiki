# 008e: component novelty statuses and literature chronology

Date: 2026-08-17

This note fixes the item-by-item novelty classification required by Assignment 008 after the closest-source reconstructions in `008a`--`008d`. The mathematical package is unchanged from the assignment.

## 1. Item-by-item status table

### Item 1. Finite-state typed signed duality

**Status: `known ingredients, assembly plausibly new`.**

Direct prior ingredients include:

- Lloyd--Sudbury/Sudbury product-form local IPS dualities;
- Sturm--Swart and Latz--Swart finite-state graphical/pathwise dualities, including genuinely `3+`-state examples;
- general algebraic/intertwining duality frameworks;
- Dawson--Greven signed Feynman--Kac branching/function-valued duality for finite type spaces;
- general Feynman--Kac genealogical particle representations and finite-matrix multiplicative-functional representations.

No source was found with the exact Assignment-001 statement for arbitrary bounded finite-range single-site replacement IPS in the reference-indicator tensor basis, with its specific typed branch coefficients and diagonal FK potential. But the individual mechanisms are sufficiently standard that Assignment 001 should be presented as an enabling synthesis, not a standalone novelty theorem.

### Item 2. Killed typed patch factorization / representation

**Status: `plausibly new theorem/mechanism`.**

Strong conceptual predecessors exist:

- marked-Poisson graphical constructions;
- clans of ancestors / backward sketches;
- information-percolation partial revelation of dependency geometry and later update randomness;
- signed FK duality;
- conditional independence of disjoint marked-Poisson regions.

No source found combines them in the project-specific way:

\[
\text{signed FK typed dual}
\to
\text{coarse successful record hiding source outcome}
\to
\text{one-site signed patch averaging},
\]

with incoming typed-target conflicts producing cemetery and thereby making bare skeleton conditioning nonfactorizable, followed by the exact killed/noncemetery weighted factorization that restores a product of local consistency factors.

This is the strongest novelty anchor of the package.

### Item 3. Transfer-matrix bulk positivity formulation

**Status: `known ingredients, assembly plausibly new`.**

Once a matrix realization is given, positivity questions for

\[
C e^{tA}B
\]

are standard internal/external positive-systems theory. Metzler generators, invariant cones and external positivity are mature subjects.

What was not found in prior IPS work is the exact derivation from the typed patch law that the signed killed interior generator collapses to

\[
K_i(r,s)=a_{i,r}^s(\emptyset)
\]

because the escape and no-success killing terms cancel against the FK potential, together with the four patch-boundary input/output vectors. Thus the IPS-to-linear-system dictionary is plausibly new, while the positivity theory after that dictionary is known.

### Item 4. Exact boundary-complete `d=3` finite spectral criterion

**Status: `known / directly subsumed`.**

For every remaining `OI` pair,

\[
N(t)=p e^{tK}f.
\]

For arbitrary `d_0>0`, multiplying by `e^{-d_0t}` preserves its sign and gives

\[
e^{-d_0t}N(t)=p e^{t(K-d_0I)}f,
\]

the impulse response of a stable third-order SISO linear realization. The boundary-complete `d=3` spectrum is real.

Lin--Fang (IEEE TAC 1997) gave necessary-and-sufficient criteria for monotone nondecreasing step responses of third-order SISO systems with real poles; equivalently, their impulse response is nonnegative. Weller--Martin (IFAC 2020) explicitly gave an exact geometric characterization of external positivity/nonnegative impulse response for third-order SISO systems.

Therefore Assignment 006 is a correct project-specific derivation in convenient Markov coordinates, but not an independent theorem-level novelty claim.

### Item 5. Exchange-symmetric exact algebraic criterion

**Status: `known ingredients, assembly plausibly new`.**

No source found states the typed-IPS criterion

\[
c\ge a,
\quad
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\quad
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

However, after the patch-to-linear-system reduction, its analytic content is a structured third-order external-positivity calculation using exchange symmetry, mode ordering, and standard Markov-chain symmetry/lumpability tools. The exact IPS coefficient translation appears bespoke, but the scalar positivity theorem is not an independent new positive-systems mechanism.

This result remains useful as an exact application gate and as evidence that the generalized patch property has genuinely nonbinary examples. It should not be the primary novelty claim.

### Item 6. Combined generalized patch framework

**Status: `plausibly new theorem/mechanism`.**

The closest literature covers nearly every ingredient separately, sometimes very closely. The audit nevertheless found no source that directly subsumes the full chain

\[
\begin{aligned}
&\text{arbitrary finite-state single-site replacement IPS}\\
&\to\text{ signed typed FK dual}\\
&\to\text{ partially revealed successful skeleton}\\
&\to\text{ killed typed one-site patch factorization}\\
&\to\text{ exact bulk/end patch representation}\\
&\to\text{ local transfer realization and patch positivity}.
\end{aligned}
\]

The novelty case rests specifically on the *interfaces* between standard ingredients, especially item 2. It does not rest on finite-state tensor algebra, signed FK duality, graphical ancestors, Metzler positivity, or third-order spectral calculus individually.

## 2. Chronology

### Before the principal's binary patch construction

The literature already contained:

- classical graphical IPS constructions and additive/cancellative duals (Harris, Griffeath, Liggett);
- product-form algebraic IPS dualities (Lloyd--Sudbury, Sudbury);
- signed Feynman--Kac branching/function-valued duals in population models (Dawson--Greven by 2010);
- clans-of-ancestors two-stage marked-Poisson constructions (Fernández--Ferrari--Garcia 1999/2002);
- exact third-order monotone-step / nonnegative-impulse criteria in control (Lin--Fang 1997).

Thus broad claims based on any one of these ideas would be false.

### Closely related developments around/after the binary construction

- Lubetzky--Sly information percolation (2014--2016) provides a strong predecessor for partial revelation of spacetime dependency geometry and subsequent handling of update randomness.
- Sturm--Swart (2018) systematizes finite-state monotone/additive pathwise duality.
- Latz--Swart (2021/2023) develops commutative-monoid/semiring pathwise dualities and explicitly obtains new `3+`-state IPS dualities.
- Weller--Martin (2020) gives exact third-order external positivity; later positive-systems work continues the general external-positivity problem.
- Franceschini--Saada--Schütz--Velasco (arXiv:2408.15613, later publication) gives analytical dualities for several epidemic IPS, including multistate SIR, but no hidden-successful-skeleton signed patch representation was found.

No successor located in this audit directly extends the principal's patch mechanism to arbitrary finite-state single-site replacement IPS or reproduces the killed typed factorization.

## 3. Negative findings that must survive project framing

The following statements must **not** be used as novelty claims:

1. "finite-state IPS have graphical duals";
2. "signed Feynman--Kac duals exist";
3. "one can reveal a backward Poisson dependency skeleton before all update randomness";
4. "Metzler matrices generate nonnegative semigroups";
5. "nonnegativity of `C e^{tA}B` is external positivity";
6. "third-order real-pole external positivity has a finite exact criterion";
7. "symmetry/lumpability can reduce Markov spectral modes".

The project-specific contribution, if retained after final ruling, must be stated at the level of the killed typed patch representation and its exact derivation from arbitrary finite-state replacement dynamics, with the transfer formulation as a consequence.

## 4. Remaining uncertainty

No precise source comparison remains unresolved enough to justify `UNRESOLVED-NOVELTY-AUDIT`. The strongest candidate sources were reconstructed at the level needed to distinguish their hypotheses and mathematical objects from the fixed package.

As always, "no source found" is not a proof of historical priority. The appropriate label is **plausibly new**, not established first-in-literature priority.