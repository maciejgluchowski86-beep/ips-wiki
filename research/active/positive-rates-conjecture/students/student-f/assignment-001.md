# Student F assignment 001: recover the last-interaction reduction and make it irreversible

Work on branch `research/positive-rates-conjecture`.

The scientific target is fixed by the principal:

> Prove the positive rates conjecture for simple IPS.

You are not being assigned a narrow specialist role. Use whatever combination of source reading, generator calculations, graphical constructions, duality, finite-volume analysis, computation, or alternative ideas is useful. The principal's old route below is a starting lead, not a prescribed method.

## Read first

- root `project-state.md`;
- `CHATGPT.md`;
- `research/active/positive-rates-conjecture/state.md`;
- `research/active/positive-rates-conjecture/proof-spine.md`;
- `research/active/positive-rates-conjecture/literature.md`;
- `research/active/positive-rates-conjecture/principal-starting-note.md`;
- `research/active/positive-rates-conjecture/meetings/000-principal-reset.md`;
- the primary Głuchowski--Menz 2025 and 2026 papers defining/reducing simple PRC;
- on branch `research/noisy-east-positive-rates`, at least the final `state.md`, `proof-spine.md`, and Meeting 002 closure so you do not recreate the closed fixed-wall route;
- the canonical patch paper under `paper/` when its successful-interaction/conditional-averaging identities are relevant.

## Main objective

Reconstruct, from first principles if necessary, the earlier route remembered in the principal note:

- finite interval `R`;
- last successful monomial-dual interaction whose influence leaves `R`;
- reveal that interaction and the active spacetime ancestry trail leading to it;
- undo duality for everything else;
- identify exactly the early and late spin-system semigroups and the boundary modifications;
- identify the trail weight;
- derive the Duhamel expansion or replacement identity that was supposed to lead to a high-density criterion.

Do **not** assume the principal's recollection is exact. Correct it explicitly if the actual construction differs.

## What would count as progress

The preferred outcome is a rigorous theorem of the form

$$
Q\Longrightarrow\text{ergodicity},
$$

where `Q` is a precise qualitative density/finite-box statement that is genuinely weaker and independently attackable. If you get this, make the separation explicit: explain why proving `Q` does not already amount to proving convergence in another notation, and identify one plausible mechanism for `Q` that does not assume ergodicity.

If the old route fails, identify the first genuinely uncontrolled term or false step. A precise failure that eliminates this route counts as progress.

If, while reconstructing it, you find a materially stronger route to the fixed target, pursue that instead. You are not required to preserve the old proof architecture.

## Anti-circularity requirement

The principal expects the project to fail by cycling through equivalent reformulations. Guard against that actively.

For every candidate reduction you propose, include a short section answering:

1. What exact previous statement does this replace?
2. What implication is one-way rather than definitional?
3. Why is the new premise technically easier or more local?
4. What estimate would prove it without already proving ergodicity?
5. What example, counterexample, or parameter regime distinguishes it from a disguised convergence statement?

A new dual, patch, profile, invariant-measure, or finite-box notation with no new estimate is not progress.

## Residual chamber and route boundary

Use the source-corrected residual chamber from the active proof spine. Do not silently return to the assignment-001 path from the old wall programme, which was already covered by the 2025 theorem.

Do not continue the fixed finite-wall route by increasing block length or refining frozen-exterior one-attack constants.

## Durable output

Commit a substantial report under

`research/active/positive-rates-conjecture/students/student-f/001-last-interaction-reduction.md`

with any supporting code/TeX beside it.

The report should end with a concise handoff stating exactly one of:

- `genuine reduction obtained: ...`;
- `old route fails at: ...`;
- `stronger route found: ...`;
- `unresolved after substantive work; exact blocker: ...`.

Do not claim `state_narrowed` yourself; the Professor decides that after reading the mathematics.
