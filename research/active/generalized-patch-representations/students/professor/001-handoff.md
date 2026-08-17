# Assignment 001 handoff

Date: 2026-08-17

Outcome: **`CONTINUE-TYPED-PATCH`**.

## Decisive mathematics

The canonical finite-state basis is the reference-state indicator tensor basis. Typed active configurations are finite partial maps into `E\{0}`; conflicting labels merge to a cemetery/zero state.

For active source type `r` and typed target `tau`, the exact source-outcome coefficients are

\[
a_{i,r}^{0}(\tau)=\widehat c_i^{0\to r}(\tau),
\]

\[
a_{i,r}^{s}(\tau)=\widehat c_i^{s\to r}(\tau)-\widehat c_i^{0\to r}(\tau)
\quad(s\ne0,r),
\]

\[
a_{i,r}^{r}(\tau)=-\widehat c_i^{0\to r}(\tau)-\sum_{y\ne r}\widehat c_i^{r\to y}(\tau).
\]

Absolute values are fixed local Poisson rates, coefficient signs are sign marks, and the empty-target source-survival coefficient is placed in the Feynman--Kac potential. This gives an exact local graphical generator duality and reduces identically to the binary death/split/birth process.

For nonempty target `tau`, the natural successful record is

\[
(i,t,r,\tau),
\]

which hides the post-interaction source outcome `s`. All hidden outcomes touch the same source and target site-lines, so the first geometry gate passes.

## Files

- algebra/generator action: `001a-typed-generator-action.md`, commit `0e438eef`;
- signed typed dual + binary reduction: `001b-signed-typed-dual.md`, commit `2b060e2e`;
- coarse typed skeleton: `001c-coarse-typed-skeleton.md`, commit `3bea5d67`;
- exact verifier: `001-finite-state-duality-verifier.py`, final commit `c8e47458`;
- final report: `001-finite-state-duality.md`, commit `2f37d6bf`;
- branch-only wiki page: `docs/generalized-patch-representations/finite-state-typed-duality.md`, commit `e28d48c1`.

## Verifier

Run

```bash
python research/active/generalized-patch-representations/students/professor/001-finite-state-duality-verifier.py
```

Expected final line:

```text
all finite-state typed-duality checks passed
```

The script reports 972 exact `d=3` elementary generator/FK checks and separately checks the binary specialization.

## Next bridge

Do **not** move directly to positivity.

The next bounded theorem is conditional factorization for the typed successful skeleton. The key new local boundary conditions are:

1. outgoing terminal record `(i,t,r,tau)`: preceding local type must equal `r`;
2. incoming target label `a`: preceding local type must be either inactive/reference `0` or already type `a`; a different active type is a conflict/cemetery event;
3. after a compatible incoming record, the next local patch starts with type `a`;
4. the hidden outgoing source outcome `s` initializes the next source patch after an outgoing boundary.

The main question is whether cemetery-producing target conflicts can be represented by local zero factors without destroying the product source--time-strip factorization.

## Operational note

The programme branch was created from reset commit `7c6b060`. During setup a connector mistake briefly created a one-word placeholder file on `main`; it was immediately deleted. A compare of `7c6b060..main` afterwards returned `files: []`, so the main tree is unchanged even though those two no-op commits exist in history. All actual programme files are on `research/generalized-patch-representations`.
