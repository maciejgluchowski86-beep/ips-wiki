# Student G assignment 001: independent attack on the fixed positive-rates target

Work on branch `research/positive-rates-conjecture`.

The scientific target is fixed by the principal:

> Prove the positive rates conjecture for simple IPS.

You are deliberately given broad freedom. Do not treat yourself as a narrowly defined reviewer or specialist. Your job is to make real mathematical progress toward the fixed target and to reject circular reformulations aggressively.

## Read first

- root `project-state.md`;
- `CHATGPT.md`;
- `research/active/positive-rates-conjecture/state.md`;
- `research/active/positive-rates-conjecture/proof-spine.md`;
- `research/active/positive-rates-conjecture/literature.md`;
- `research/active/positive-rates-conjecture/principal-starting-note.md`;
- the primary Głuchowski--Menz 2025 and 2026 sources;
- the final state/proof-spine/Meeting 002 on branch `research/noisy-east-positive-rates`;
- the canonical patch paper under `paper/` if it becomes useful.

Student F is separately trying to recover the principal's remembered last-successful-interaction/Duhamel route. You may also use that idea, but do not wait for F and do not assume it is the right proof.

## Objective

Find one irreversible step toward ergodicity in the true residual noisy-East chamber.

A particularly promising possibility, suggested by the principal's prior work, is a **qualitative high-density or finite-box statement** that is strong enough to feed an ergodicity argument but weak enough to prove without already knowing convergence. Explore this seriously, including large-box approximations, boundary-condition uniformity, one-sided propagation, regeneration, or East-style front information.

But you are free to abandon the density route if another mechanism produces a stronger genuine estimate.

## Questions worth attacking

These are prompts, not a checklist.

- Can positive rates plus one-sidedness force a nontrivial uniform lower density of the state that destroys the East obstruction after a burn-in time, uniformly over initial configurations or over extremal invariant laws?
- Is there a finite-interval statement, uniform over boundary conditions, whose thermodynamic limit yields such a density bound?
- Can one prove that every invariant law in the residual chamber gives positive density to a facilitating/noise-created pattern, then upgrade that qualitative fact to uniqueness by a one-sided regeneration argument?
- Can an East-model front/regeneration theorem survive a small nonreversible perturbation in a form sufficient for PRC?
- Does the canonical patch/confined-interaction machinery give a quantitative finite-box error that turns a density estimate into ergodicity without assuming the invariant law explicitly?
- Is there a monotone auxiliary process, censoring construction, or oriented percolation comparison that controls only the needed density event even though the full IPS is non-attractive?

The right answer may be a counterexample to one of these intermediate hopes. Record it if so.

## Anti-circularity requirement

Do not report a new formulation as progress unless it produces a new inequality, implication, or obstruction.

In particular, the following are insufficient by themselves:

- saying ergodicity is equivalent to disagreement extinction;
- replacing spins by density profiles;
- replacing the IPS by a dual without estimating the dual;
- replacing infinite volume by boxes without a quantitative boundary error;
- asserting that every invariant law should have high density without deriving an identity or bound;
- invoking East mixing while leaving the nonreversible perturbation as an unquantified error;
- another fixed-block wall statistic.

For every proposed route, state what measurable quantity you can bound that was not bounded before and what exact theorem would follow from that bound.

## Use of previous work

The old fixed finite-wall route is closed. Do not increase the wall length or optimize its one-attack constants.

The project already knows the exact residual chamber and that the earlier `a=epsilon, b=epsilon/2` path was not residual. Re-check source boundaries when needed, but do not spend the assignment rediscovering these facts.

## Durable output

Commit a substantial report under

`research/active/positive-rates-conjecture/students/student-g/001-independent-structural-attack.md`

with any supporting calculations/code.

End with one of:

- `new target-relevant estimate: ...`;
- `material route eliminated: ...`;
- `new structural route with first proved lemma: ...`;
- `unresolved after substantive work; exact blocker: ...`.

The Professor will compare your result with Student F's and decide the next spine change.
