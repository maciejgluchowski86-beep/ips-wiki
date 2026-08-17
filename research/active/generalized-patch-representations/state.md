# Programme state

Date: 2026-08-17

## Active direction

Generalize the canonical binary patch-representation / patch-positivity framework beyond binary flip spin systems.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without a later principal instruction.

Latest meeting: `meetings/008-novelty-audit-keeps-killed-typed-factorization.md`.

## Mathematical theorem stack

### Assignments 001--003: arbitrary finite-state typed representation

Outcomes:

- 001 `CONTINUE-TYPED-PATCH`;
- 002 `CONTINUE-TYPED-REPRESENTATION`;
- 003 `CONTINUE-TYPED-POSITIVITY`.

For arbitrary finite local state space with reference state `0`, bounded finite-range **single-site replacement** IPS admit the project's reference-indicator signed Feynman--Kac dual. A nonempty successful record

\[
(i,t,r,\tau)
\]

reveals source/time/pre-source type/typed target while hiding the post-source outcome.

One-site typed patches factor the signed FK weight only after a necessary multi-state modification. Incoming typed target conflicts can enter cemetery and thereby remove future no-record constraints, so bare conditioning on the coarse record list is false. Since the duality function vanishes at cemetery, the exact replacement is a killed/noncemetery weighted factorization. This yields the bulk/end patch representation

\[
P_TH_{\xi_0}(\eta)
=
\int
\prod_{P\in\mathcal B_T}C(P)
\prod_{P\in\mathcal E_T}C_T(\eta_{i(P)},P)
\,\nu_T(dg).
\]

### Assignment 004: exact local transfer

Outcome: `CONTINUE-TYPED-POSITIVITY-CRITERION`.

For active type `r`, the signed weighted interior transfer is exactly

\[
K_i(0,\cdot)=0,
\qquad K_i(r,s)=a_{i,r}^s(\emptyset).
\]

Typed bulk patch positivity is exact nonnegativity of four local matrix-semigroup numerator families over realizable boundary descriptors. The `d=2` specialization is exactly the canonical binary patch-positivity property.

### Assignments 005--007: controlled `d=3` analysis

Assignment 005 proved that zero-length and long-time endpoint inequalities do **not** characterize three-state positivity: the exact physically realizable witness

\[
N(t)=\frac1{128}-\frac{13}{64}e^{-t}+\frac{153}{128}e^{-2t}
\]

has positive endpoints but minimum `-1/1224`.

Assignment 006 gave an exact finite critical-point test for every boundary-complete `d=3` `OI` numerator. Assignment 007 identified a genuinely nonbinary exchange-symmetric subclass with exact algebraic criterion

\[
c\ge a,
\]

and, for every outgoing row `p=(p_0,p_1,p_2)`,

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

These results remain correct. Assignment 008 changes their **research-contribution status**, not their mathematics.

## Assignment 008: novelty and closest-prior-work audit

Outcome: **`CONTINUE-TO-APPLICATIONS`**.

The audit is deliberately mixed.

### Fixed component statuses

1. finite-state typed signed duality: **`known ingredients, assembly plausibly new`**;
2. killed typed patch factorization / representation: **`plausibly new theorem/mechanism`**;
3. transfer-matrix bulk positivity formulation: **`known ingredients, assembly plausibly new`**;
4. exact boundary-complete `d=3` finite spectral criterion: **`known / directly subsumed`**;
5. exchange-symmetric exact algebraic criterion: **`known ingredients, assembly plausibly new`**;
6. combined generalized patch framework: **`plausibly new theorem/mechanism`**.

### Important negative novelty findings

The audit found that:

- finite-state graphical/product duality is established in Lloyd--Sudbury/Sudbury, Sturm--Swart and Latz--Swart type theories;
- Dawson--Greven already have explicit finite-type **signed Feynman--Kac duality**;
- Fernández--Ferrari--Garcia ancestor clans and Lubetzky--Sly information percolation are predecessors for revealing relevant spacetime/Poisson dependency geometry before all local randomness is processed;
- Metzler/internal positivity and `C e^{tA}B` external positivity are standard positive-systems theory;
- the Assignment-006 scalar `d=3` theorem is **directly subsumed** by third-order SISO external-positivity literature. Multiplying `p e^{tK}f` by `e^{-dt}` preserves its sign and gives a stable third-order impulse response. Lin--Fang (1997) and Weller--Martin (2020) already provide exact third-order nonnegative-impulse / monotone-response characterizations.

Thus none of these ingredients or the `d=3` spectral calculation should be framed as new.

### Strongest surviving novelty candidate

No equivalent source was found for the full interface

\[
\text{arbitrary finite-state replacement IPS}
\to
\text{signed typed FK dual}
\to
\text{coarse successful record hiding source outcome}
\]

followed by one-site signed patch averaging in the presence of typed target conflicts, where cemetery makes bare skeleton conditioning fail and the exact representation is restored through the killed/noncemetery weighted product identity.

This is the primary plausible novelty anchor. The claim is **plausibly new**, not established historical priority.

Decisive files:

- `students/professor/008a-classical-duality-and-graphical-predecessors.md`, commit `e2966ae0`;
- `008b-feynman-kac-and-multistate-duality-comparison.md`, commit `02350f42`;
- `008c-signed-fk-and-hidden-skeleton-factorization.md`, commit `f139fde3`;
- `008d-external-positivity-overlap.md`, commit `41994e79`;
- `008e-component-status-and-chronology.md`, commit `0c91fe66`;
- final report `008-novelty-and-prior-work-audit.md`, commit `6db1efa8`;
- handoff `008-handoff.md`, commit `4524207b`;
- Meeting 008, commit `42719a83`.

## Current proof-spine edge

**Applications of the surviving generalized patch mechanism.**

Per the sequencing ruling fixed in Meeting 007 and enforced by Assignment 008, applications are now the next active mathematical block.

The next block must start from a **natural genuinely nonbinary finite-state single-site replacement IPS from the literature**, not a coefficient table designed to satisfy the criterion. It should test:

1. whether the typed dual/successful-skeleton representation specializes naturally;
2. whether bulk patch positivity actually holds, using the exchange-symmetric/refresh criterion or the general finite-dimensional external-positivity formulation as appropriate;
3. whether the representation proves or clarifies something useful that is not already standard for that model;
4. application-specific prior work before claiming a contribution.

A failed positivity test is an acceptable and informative result.

## `d>3` ordering

Do **not** insert a generic `d>3` positivity-algebra block before applications.

The arbitrary finite-state representation is already proved, while the positivity problem at higher dimension overlaps the established external-positivity problem for higher-order linear systems. Reopen generic `d>3` tractable criteria only if:

- a concrete application naturally requires more than three local states; or
- later literature evidence identifies a particular higher-dimensional structured class with independent value.

## Scope and publication boundary

Current proved mathematical scope: arbitrary finite-state bounded finite-range **single-site replacement** dynamics in the reference-state indicator tensor basis. Simultaneous multi-site physical updates remain outside scope.

No content is to be promoted to `main` without later principal instruction. Existing `docs/entries/`, `docs/meta/`, and `mkdocs.yml` are outside the active write surface.

All previously stopped programmes remain closed.