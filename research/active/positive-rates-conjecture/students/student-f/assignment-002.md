# Student F assignment 002: regional insertion positivity or explicit failure

Work on branch `research/positive-rates-conjecture`.

The scientific target remains fixed: prove the positive rates conjecture for simple IPS.

Read the updated `state.md`, `proof-spine.md`, and `meetings/001-density-estimates-and-regional-kernel.md`, then re-read your own Assignment 001 report where needed. You retain broad methodological freedom; the point of this assignment is not to preserve the old scaffold proof if the finite test kills it.

## Decisive question

Your first report proved the conditional insertion estimate

$$
\mathbb E^-[(B\eta_i(t)-c)F]\ge0
$$

for nonnegative right-history-measurable `F` after `T_rho`, but also showed that the raw Duhamel gradient has left dependence.

Now resolve the smallest genuinely nontrivial regional case.

Construct the minimal barrier/scaffold cell containing:

- one revealed successful interaction `i -> i+1`;
- a predecessor relation that leaves a genuine left branch at the source;
- the corrected dynamic boundary rules from your Section 4;
- successful birth-versus-jump type kept hidden;
- all other marks integrated out.

Derive the resulting finite spin kernel exactly. Then determine whether its companion factor satisfies either

$$
F\ge0\text{ and right-history measurable},
$$

or, more generally, the only inequality actually needed,

$$
\mathbb E^-[\eta_iF]\ge\rho\,\mathbb E^-[F].
$$

Do not impose right-measurability if a coarser signed cancellation proves the insertion inequality directly.

## Falsification discipline

This must end in a real mathematical verdict on the cell, not another proposed representation.

If the inequality fails, produce the smallest explicit configuration/time/parameter counterexample you can and identify which part of the old route is thereby closed.

If the one-cell inequality holds, immediately test two consecutive scaffold cells. A one-cell identity that fails to compose is not enough to change the proof spine.

You may use symbolic algebra, exact finite-state semigroups, patch factorization, Duhamel expansions, or another route. If a stronger argument bypasses the scaffold entirely and proves an actual target-relevant estimate, pursue it.

Do not spend the assignment optimizing unweighted density estimates; Meeting 001 established that the existing density bounds do not directly meet the insertion threshold.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/002-regional-insertion.md`.

End with one of:

- `one-cell and two-cell insertion positivity proved: ...`;
- `old last-exit route fails on minimal cell: ...`;
- `one-cell works but composition fails at: ...`;
- `stronger route found with proved estimate: ...`;
- `unresolved after substantive work; exact blocker: ...`.
