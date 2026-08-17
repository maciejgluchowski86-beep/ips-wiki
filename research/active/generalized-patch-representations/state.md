# Programme state

Date: 2026-08-17

## Active direction

Generalize the patch-representation / patch-positivity framework of the canonical paper `paper/` beyond binary flip spin systems.

Branch: `research/generalized-patch-representations`.

Workspace: `research/active/generalized-patch-representations/`.

Branch-only wiki section:

- `docs/generalized-patch-representations.md`;
- `docs/generalized-patch-representations/`.

Nothing from this programme is to be written or merged to `main` without a later principal instruction.

Latest meeting: `meetings/001-finite-state-typed-duality-opens-patch-factorization.md`.

## Assignment 001 result

Status: **`CONTINUE-TYPED-PATCH`**.

Final report: `students/professor/001-finite-state-duality.md`, commit `2f37d6bf`.

Handoff: `students/professor/001-handoff.md`, commit `6bdd26ef`.

Verifier: `students/professor/001-finite-state-duality-verifier.py`, final commit `c8e47458`.

For finite `E={0,...,d-1}` with reference state `0`, the indicator tensor basis gives typed active configurations. Compatible typed overlaps merge; conflicts go to a cemetery/zero state.

For active source type `r`, source outcome `s`, and typed target `tau`, the exact local branch coefficients are

\[
a_{i,r}^{0}(\tau)=\widehat c_i^{0\to r}(\tau),
\]

\[
a_{i,r}^{s}(\tau)=\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau),
\quad s\ne0,r,
\]

\[
a_{i,r}^{r}(\tau)
=-\widehat c_i^{0\to r}(\tau)-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
\]

Absolute coefficients are fixed local Poisson rates, signs are sign marks, and the empty-target source-survival coefficient goes into the Feynman--Kac potential. The binary specialization is exactly the paper's death/split/birth dual.

For nonempty target `tau`, the successful record

\[
(i,t,r,\tau)
\]

retains the pre-interaction source type and typed target while hiding the post-interaction source outcome `s` (delete/survive/retype). Hidden outcomes have identical interaction endpoints, so the first geometry gate passes.

## Current proof-spine edge

**Typed successful-skeleton conditional factorization.**

The next theorem must decide whether conditioning on typed successful records still decomposes the hidden marks into independent source--time-strip laws.

New issues relative to binary:

1. outgoing records require a specific pre-source type `r`;
2. an incoming target label `a` is compatible only when the preceding local type is inactive/reference `0` or already `a`;
3. a different active type causes the merge to hit the cemetery state;
4. the hidden outgoing source outcome `s` initializes the next source patch with one of `d` local states.

Patch positivity is downstream and is not yet defined.

## Canonical source and publication boundary

The binary paper under `paper/` remains authoritative. Existing patch pages under `docs/entries/` are source material and are not generalized in place.

No programme content is to be published to `main` unless the principal later gives a separate instruction.

## Previous programmes

All previously stopped programmes remain closed at their existing rulings. This new direction does not reopen them.
