# Meeting 001: finite-state typed duality passes; typed patch factorization opens

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- `students/professor/001a-typed-generator-action.md`, commit `0e438eef`;
- `students/professor/001b-signed-typed-dual.md`, commit `2b060e2e`;
- `students/professor/001c-coarse-typed-skeleton.md`, commit `3bea5d67`;
- exact verifier, final commit `c8e47458`;
- final report `students/professor/001-finite-state-duality.md`, commit `2f37d6bf`;
- handoff `students/professor/001-handoff.md`, commit `6bdd26ef`.

## Direction and repository ruling

The principal's new direction supersedes all previously queued work. It is a new programme generalizing the canonical patch-positivity paper, not a reopening of positive-rates, FA-1f, or any earlier stopped route.

Branch:

`research/generalized-patch-representations`.

Workspace:

`research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be published to `main` without a later principal instruction.

The first block was deliberately definitions/notation plus algebraic duality, not an abstract duality search. For more than two local states the dual state cannot be specified until a local tensor basis is chosen.

## Ruling

Assignment 001 ends

**`CONTINUE-TYPED-PATCH`.**

The reference-state indicator tensor basis provides a canonical enough first generalization and, importantly, the resulting dual is not merely a finite-matrix transpose: it has fixed local Poisson clocks and a finite hidden branch mark.

## 1. Typed tensor basis

For finite

\[
E=\{0,1,\ldots,d-1\},
\qquad E_*=E\setminus\{0\},
\]

use

\[
h_0\equiv1,
\qquad h_a(x)=1_{\{x=a\}},\quad a\in E_*.
\]

Typed active configurations are finite partial maps `xi:Lambda -> E_*`, with

\[
H_\xi(\eta)=\prod_{i\in\operatorname{supp}\xi}1_{\{\eta_i=\xi(i)\}}.
\]

These tensor indicators form a basis of every finite cylinder algebra by explicit Möbius inversion.

Products use typed compatible union. Unequal labels at one overlap give zero, represented by a cemetery state `dagger` with `H_dagger=0`.

## 2. Exact general single-site generator action

For

\[
L f(\eta)
=\sum_i\sum_{x\ne y}1_{\{\eta_i=x\}}c_i^{x\to y}(\eta_{N(i)})
\bigl[f(\eta^{i,y})-f(\eta)\bigr],
\]

expand every neighbour rate in the typed tensor basis. If the active dual source type is `r`, then for target `tau` and source outcome `s in E` the signed coefficients are

\[
a_{i,r}^{0}(\tau)=\widehat c_i^{0\to r}(\tau),
\]

\[
a_{i,r}^{s}(\tau)=\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau),
\quad s\in E_*\setminus\{r\},
\]

\[
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
\]

Here `s=0` deletes the source, `s=r` preserves its type, and the other values retype the source.

The corresponding local typed map removes/retypes the source and compatibly merges the target. Coefficients are independent of the rest of the current dual configuration; pre-existing target colors affect only the deterministic merge/cemetery result.

## 3. Local signed Feynman--Kac dual

Use rate

\[
|a_{i,r}^{s}(\tau)|
\]

and coefficient sign for every non-diagonal local branch. Put the empty-target source-survival coefficient directly into the additive potential.

This gives the exact generator identity

\[
L_\eta H(Y,\eta)
=D H(Y,\eta)+V(\xi)H(Y,\eta).
\]

Under bounded finite-range physical rates the typed dual is nonexplosive. As in the canonical paper, an explicit Feynman--Kac exponential-integrability hypothesis is retained for the infinite-volume semigroup formula rather than being silently inferred from nonexplosion.

## 4. Binary specialization is exact

For `E={0,1}`, typed configurations become ordinary finite subsets and

\[
a_{i,1}^{0}(S)=c_i^0(S),
\qquad
 a_{i,1}^{1}(S)=-c_i^0(S)-c_i^1(S).
\]

Thus source deletion gives death/split, source survival gives birth, and the empty-target survival coefficient is exactly the paper's diagonal birth term in the potential. No regrouping is required.

## 5. Successful record

For a nonempty typed target, superpose the source-outcome clocks at fixed `(i,r,tau)`:

\[
\Lambda_{i,r}(\tau)=\sum_s|a_{i,r}^{s}(\tau)|.
\]

The natural record is

\[
(i,t,r,\tau),
\]

which hides the post-interaction source outcome `s`.

Every hidden branch has one outgoing endpoint at `i` and incoming endpoints at `supp tau`, so deletion/survival/retyping does not change patch geometry.

The pre-interaction source type `r` should normally be revealed because both the aggregate record intensity and the outgoing consistency condition depend on it. Binary systems hide this issue because the active source type is unique.

## 6. Exact finite test

The final verifier exhausts the `d=3`, one-neighbour elementary basis family. It includes both source types, all six physical transitions, all three neighbour basis modes, compatible and conflicting pre-existing target labels, and all nine physical configurations. It checks direct generator action against both the typed linear expansion and the signed graphical generator plus potential.

The main `d=3` comparison contains 972 exact checks. The script separately verifies the binary reduction and source-type-dependent superposed intensities.

## 7. Next proof-spine edge

Do **not** define generalized patch positivity yet.

The next theorem is conditional factorization for the typed successful skeleton. The new boundary data are:

- outgoing boundary: required pre-source type `r`;
- incoming boundary at target site `j`: target type `tau(j)`;
- hidden outgoing mark: post-source outcome `s`;
- possible typed conflict when an incoming target meets a different active type.

The key question is whether target compatibility/conflict can be represented by local patch consistency/zero factors while preserving product independence of hidden marks on disjoint source--time strips.

## Novelty status

No literature novelty claim is made yet for the abstract finite-state typed duality. The result is established internally as the correct structural bridge for this programme. Literature comparison should occur after the factorization mechanism is clear enough to know what theorem is actually being claimed.

## Operational note on `main`

During branch setup, one placeholder file was accidentally created on `main` and immediately deleted. A subsequent GitHub compare from reset commit `7c6b060` to `main` returned `files: []`. Thus the `main` tree is unchanged; the two no-op commits remain only in history. All programme content is on the research branch.
