# Meeting 008: novelty audit keeps killed typed factorization, removes d3 spectral novelty

Date: 2026-08-17

`state_narrowed: yes`.

Evidence:

- classical duality / graphical predecessor audit `students/professor/008a-classical-duality-and-graphical-predecessors.md`, commit `e2966ae0`;
- FK / multistate duality audit `008b-feynman-kac-and-multistate-duality-comparison.md`, commit `02350f42`;
- signed-FK / hidden-skeleton factorization audit `008c-signed-fk-and-hidden-skeleton-factorization.md`, commit `f139fde3`;
- external-positivity overlap `008d-external-positivity-overlap.md`, commit `41994e79`;
- component status / chronology `008e-component-status-and-chronology.md`, commit `0c91fe66`;
- final report `008-novelty-and-prior-work-audit.md`, commit `6db1efa8`;
- handoff `008-handoff.md`, commit `4524207b`.

## Ruling

Assignment 008 ends

**`CONTINUE-TO-APPLICATIONS`.**

The ruling is deliberately mixed rather than globally positive.

## Component novelty statuses

1. finite-state typed signed duality: **`known ingredients, assembly plausibly new`**;
2. killed typed patch factorization / representation: **`plausibly new theorem/mechanism`**;
3. transfer-matrix bulk positivity formulation: **`known ingredients, assembly plausibly new`**;
4. exact boundary-complete `d=3` finite spectral criterion: **`known / directly subsumed`**;
5. exchange-symmetric exact algebraic criterion: **`known ingredients, assembly plausibly new`**;
6. combined generalized patch framework: **`plausibly new theorem/mechanism`**.

## Negative findings

The audit found several stronger predecessors than the programme had previously recorded.

### Signed FK is known

Dawson--Greven's finite-type Fisher--Wright work has an explicit signed Feynman--Kac branching/function-valued dual. Signed cancellation plus an exponential FK factor is therefore not a new ingredient.

### Partial graphical revelation is known

Fernández--Ferrari--Garcia clans of ancestors and Lubetzky--Sly information percolation already separate a relevant spacetime/ancestor geometry from later mark/update processing. The broad slogan "reveal a coarse graphical skeleton and integrate hidden randomness later" is not new.

### `d=3` spectral positivity is directly subsumed

For a remaining `OI` numerator

\[
N(t)=p e^{tK}f,
\]

multiplication by `e^{-dt}`, `d>0`, preserves its sign and turns it into the impulse response of a stable third-order SISO realization `(K-dI,f,p)`. The active spectrum is real under the boundary-complete reduction.

Lin--Fang (1997) already gives necessary-and-sufficient real-pole third-order monotone-step/nonnegative-impulse criteria, and Weller--Martin (2020) explicitly gives exact third-order external positivity. Therefore Assignment 006 is not an independent novelty theorem.

This also makes an automatic generic `d>3` positivity-algebra programme less attractive: higher-order external positivity is itself an established and difficult control-theory problem.

## Positive finding

No source located in the classical IPS duality, multistate duality, signed-FK, clan-of-ancestors, information-percolation, or positive-systems literature directly contains the following interface:

\[
\text{arbitrary finite-state replacement IPS}
\to
\text{signed typed FK dual}
\to
\text{successful record hiding signed source outcome}
\]

followed by one-site patch averaging in the presence of typed target conflicts, where cemetery makes **bare** skeleton conditioning nonfactorizable and the exact representation is recovered only through a killed/noncemetery weighted product identity.

That killed typed factorization is not a cosmetic corollary. It is what makes the generalized patch representation possible after the genuinely new multi-state cemetery obstruction appears.

The appropriate research status is therefore **plausibly new**, not proven historical priority.

## Why the programme continues rather than narrows further

The surviving novelty is concentrated around the factorization mechanism, but that mechanism is the structural center of the arbitrary-finite-state representation rather than an isolated side theorem. The transfer formulation demonstrates what it buys, even though the subsequent third-order positivity calculus overlaps known control theory.

A separate narrowing phase would not resolve the main remaining question: whether the generalized representation is useful for a natural nonbinary IPS.

## Next direction

Per Meeting 007's precommitted ordering, **applications are the next active mathematical block**.

The application block must:

- start from a natural genuinely nonbinary finite-state single-site replacement IPS from the literature;
- test the typed representation and patch positivity honestly rather than tune an artificial coefficient table;
- distinguish a useful consequence from a mere re-expression of known duality;
- check application-specific prior work before claiming value.

Generic `d>3` criterion algebra remains deferred unless an application requires more states or a later literature finding changes its expected value.

No application work is executed in this meeting.