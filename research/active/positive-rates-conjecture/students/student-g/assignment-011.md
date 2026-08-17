# Student G Assignment 011: distinguished-zero transfer through zero-boundary invariant marginals

Date: 2026-08-17

This is a **bounded architecture test** prompted directly by the principal after the toolbox applicability synthesis. It reopens the positive-rates programme only for the question below. It does not reopen Assignment 010, the common-coupling occupation route, generic coupling engineering, or a broad literature search.

## Principal direction

Investigate whether an East-style distinguished-zero argument can be adapted to the remaining positive-rates residual chamber even though the infinite-volume invariant law is not known explicitly, by using the finite zero-boundary invariant laws `pi_N` as named surrogate equilibrium marginals.

## Goal

Decide whether the projective zero-boundary family actually supplies a new screening architecture, or whether an East-style argument necessarily reduces to the already-isolated boundary-shift/tail-shift defect.

A successful return does **not** need to prove the conjecture. It must do one of:

1. produce a concrete new distinguished-zero/screening bridge whose missing estimate is materially weaker or different from the stopped tail-shift/common-coupling/PR1 blockers; or
2. prove a precise obstruction/equivalence showing that the proposed use of `pi_N` merely renames an already-stopped object.

## Required reading

On branch `research/positive-rates-conjecture` read:

- `CHATGPT.md`;
- `research/active/positive-rates-conjecture/state.md`;
- `research/active/positive-rates-conjecture/proof-spine.md`;
- `research/active/positive-rates-conjecture/programme-established-results.md`;
- `research/active/positive-rates-conjecture/meetings/013-equilibrium-profile-truncates-zero-frequency-response-remains.md`;
- `research/active/positive-rates-conjecture/meetings/014-zero-frequency-response-equals-tail-shift-defect.md`;
- `research/active/positive-rates-conjecture/meetings/030-signed-boundary-transmission-is-final-g010-blocker-no-restart.md`;
- `research/active/positive-rates-conjecture/students/student-f/010-profile-regeneration-truncation.md`;
- `research/active/positive-rates-conjecture/students/student-f/011-zero-frequency-boundary-response.md`.

Also read, from branch `research/ergodicity-methods-toolbox`:

- `docs/entries/east-distinguished-zero-screening.md`;
- `research/active/ergodicity-methods-toolbox/assessment/final-method-priorities.md`, only for the screening standard and anti-loop rules.

Repository conclusions are evidence, not authority. Recheck every load-bearing inference used below.

## Fixed notation

On `Lambda_N={1,...,N}` with fixed zero boundary at `N+1`, let `P_t^N` be the zero-boundary semigroup and `pi_N` its unique invariant law. The accepted one-sided suffix projectivity is

`R_{N,M} pi_N = pi_M`.

Let `bar pi_{N+1}` denote the marginal of `pi_{N+1}` on its leftmost `N` sites. The previous programme isolated

`delta_{N+1}=bar pi_{N+1}-pi_N`

and, far from the boundary, its uniform size is the tail-shift quantity `Delta_M`.

## Part A. Reconstruct the East proof at the exact structural level

Do not begin with estimates. State the minimum properties of the East distinguished-zero proof that make the conditional-equilibrium induction work.

Separate explicitly:

1. marker/path measurability from the unscreened side;
2. fixed-zero-boundary invariance between marker moves;
3. what happens to the site released when the marker moves;
4. consistency of the equilibrium family when the screened interval grows by one site.

Then substitute the generic positive-rates zero-boundary family `pi_N` for Bernoulli equilibrium and identify exactly which properties survive from one-sidedness/invariance alone.

## Part B. Exact one-move compatibility gate

Prove or refute the following elementary obstruction carefully.

Suppose an East-style marker moves one site to the right at a time determined only by the marker/right-side graphical history, and suppose the move does not inspect or modify the old screened block of `N` sites. Immediately before the move that block has law `pi_N`. If immediately after the move the enlarged `N+1` screened block is to have law `pi_{N+1}`, then necessarily

`bar pi_{N+1} = pi_N`.

The distribution assigned to the released marker site cannot repair failure of this prefix-marginal condition.

Tasks:

- give the clean measure-theoretic proof of the implication;
- compute `pi_1` and `pi_2` exactly at the hard point
  `P_h=(1/10000,1/100,9999/10000)` and test `bar pi_2=pi_1`;
- if feasible, derive the symbolic difference and factor it to identify the parameter locus on which exact one-step compatibility holds;
- commit an exact rational verifier for the finite calculation if nontrivial arithmetic is used.

If exact compatibility fails, record explicitly that the literal East Lemma 8.2 analogue with the family `pi_N` is false. This does **not** end the assignment; Part C asks whether an approximate or buffered screen is genuinely new.

## Part C. Does approximate distinguished-zero screening give new leverage?

Investigate only concrete repairs that preserve the one-sided screening idea. At minimum test these two possibilities.

### C1. Buffered moving boundary

After a marker move, allow a boundary layer of width `m` to be regarded as contaminated and ask only that observables farther left see the old `pi_N` and new `pi_{N+1}` laws approximately equally.

Determine whether the resulting error is exactly controlled by the existing `Delta_m` / tail-shift defect, or whether conditioning on the marker path yields a strictly better finite-time/local quantity. Write the implication both ways as sharply as possible.

A statement of the form "assume `Delta_m -> 0`, then screening works" is **not new input** unless the distinguished-zero construction also supplies a new proof of that decay.

### C2. Regenerative release of a finite boundary layer

Because the one-site zero-boundary chain has state-independent reset representations, test whether one can choose a marker-move/release event depending only on the marker/right-side marks that resamples the released site, or a fixed-width boundary layer, according to the correct conditional law needed for `pi_{N+1}`.

Do not assume such a kernel exists. Derive the exact consistency condition it would have to satisfy. Check on `N=1,2,3` whether a finite local release kernel can map the old `pi_N` block plus fresh right-side randomness to the required new marginal without inspecting the protected left block.

If any proposed finite release state closes, state it explicitly as a Markov kernel and verify all marginals. If every fixed-width exact release would still require a prefix-shift identity of `pi_N`, prove that reduction and stop enlarging the release state.

## Part D. Marker existence and direction

Only if Part C produces a genuinely new compatibility mechanism, address the actual marker process.

A valid marker/screen must be determined from the current site and the graphical history to its right, so conditioning on it does not reveal protected left marks. It may jump more than one site; exact nearest-neighbour motion is not required.

State precisely:

- how a zero marker is created/selected;
- how long it remains a valid fixed-zero boundary;
- how it advances or is replaced;
- what sigma-field determines success/failure;
- why the protected-side graphical marks remain fresh.

Do not prove long tail estimates until this sigma-field closes.

## Pre-registered stop condition

**STOP and return an obstruction report** if, after the exact one-move test, every credible approximate/buffered/release formulation requires as an upstream hypothesis one of the following already-stopped objects:

- `Delta_M -> 0` / tail-shift agreement of `pi_infty^0` with its shift;
- the common-uniform all-depth occupation/extinction theorem abandoned at Meeting 019;
- control of the signed boundary-transmission operator `(V)` from Meeting 030;
- a generic full-state coupling or norm already excluded by the programme.

In that case, do not enlarge marker state spaces or start a new numerical search. The useful result is the exact equivalence/obstruction.

**CONTINUE** only if you exhibit a concrete new object `S` such that:

1. `S` is defined from the one-sided marker/right-side graphical process and zero-boundary invariants;
2. `S` is not equivalent to the objects above;
3. `S` has an explicit implication chain to local forgetting/uniqueness;
4. there is a bounded next falsification/proof test.

If CONTINUE, formulate the sharpest bridge lemma and one next assignment-sized experiment. Do not attempt the full conjecture in this block.

## Durability and output

Commit mathematically durable intermediate results immediately, especially:

- the exact one-move compatibility theorem/counterexample;
- any symbolic parameter locus;
- any finite release-kernel feasibility result;
- any exact equivalence with `Delta_M`.

Final report:

`research/active/positive-rates-conjecture/students/student-g/011-distinguished-zero-transfer.md`

Final handoff:

`research/active/positive-rates-conjecture/students/student-g/011-handoff.md`

The handoff must state one of exactly:

- `STOP-EQUIVALENT`;
- `STOP-LOCAL-OBSTRUCTION`;
- `CONTINUE-NEW-BRIDGE`.

If `CONTINUE-NEW-BRIDGE`, name the new bridge lemma and the single next bounded experiment. Then stop for Professor review.

## Scope discipline

- No broad literature search.
- No generic new coupling/norm engineering.
- No return to longer connected-renewal coefficient tables.
- No `docs/` or `mkdocs.yml` edits.
- Preserve exact LaTeX backslashes when writing files; avoid escaped control characters.
