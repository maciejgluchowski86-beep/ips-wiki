# Professor FA-SCREEN-001 handoff

## Status

`STOP-SCALING-OBSTRUCTION`

The pre-registered leakage/measurability block is complete. No spectral-gap estimate was entered.

## Decisive files

- assignment: `students/professor/assignment-001-fa-screen.md`, commit `64535479`;
- literal marker/dimer leakage: `001a-fa-screen-local-leakage.md`, commit `12447442`, verifier `001a-fa-screen-local-leakage-verifier.py`, commit `0a8fcef9`;
- final width-three hazard theorem: `001c-fa-screen-width3-scaling-obstruction.md`, commit `8076b527`;
- decisive width-three verifier: `001b2-fa-screen-width3-hazard-verifier.py`, commit `71bef127`;
- final report: `001-fa-screen.md`, commit `f3650cd5`.

Intermediate note `001b-fa-screen-fixed-boundary-scaling.md` is superseded in one respect by 001c: its convenient treatment of exterior state `11` was broader than needed. The final proof uses only the seven active width-three states containing a certified screen-side vacancy and explicitly creates fresh hidden uncertainty at the protected endpoint before the dangerous mark.

## Decisive theorem

For every active width-at-most-three exterior-measurable vacancy/dimer boundary state, there is a four-unit event using only the first three exterior sites which has probability at least

$$
\delta_3(q)=e^{-12}q^2(1-q)^2>0
$$

and forces the adjacent boundary trajectory to depend on an unrevealed protected future refresh mark. Hence a faithful fixed endpoint has

$$
P(T>4n)\le(1-\delta_3(q))^n.
$$

At `q=1/10`, the exact verifier gives

$$
\delta_3(1/10)>81/2000000000.
$$

Because the registered `FA-SCREEN` bridge needs a final `s_t`-long interval in which all marks of the final protected interval remain unrevealed, earlier handoffs may search for a candidate but the selected endpoint must have age at least `s_t`. Even `O(s_t)` spatial candidates cannot beat the exponential age tail. Therefore the screen probability cannot tend to one while `s_t->infinity` and `|I_t|=o(s_t)`.

## Scope

Killed: the fixed-final-interval screen built from exterior-measurable single-vacancy/dimer finite boundary automata of width at most three.

Not killed: a genuinely different moving-boundary relaxation theorem, or the independent reserve architecture `FA-INFO` using state-adaptive causal reveals.

No `docs/` or `mkdocs.yml` files were changed.
