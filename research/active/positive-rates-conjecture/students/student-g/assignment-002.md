# Student G assignment 002: turn transient density into the weighted regional estimate, or show it cannot

Work on branch `research/positive-rates-conjecture`.

The scientific target remains fixed: prove the positive rates conjecture for simple IPS.

Read the updated `state.md`, `proof-spine.md`, and `meetings/001-density-estimates-and-regional-kernel.md`, together with Student F's first report. You are not assigned a narrow reviewer role. Use transport identities, finite boxes, exact semigroups, coupling, duality, computation, or another mechanism as useful.

## What Meeting 001 established

Your original-dynamics density estimates are correct, but they do not directly compose with F's hidden-type estimate. F needs a **weighted/conditional insertion inequality** at threshold

$$
\rho=\frac{c}{b+c-a},
$$

whereas your present unweighted asymptotic zero-density guarantee is

$$
\frac1{1+b+c}<\rho
$$

throughout the residual chamber, and the hard-core event guarantees only one-half zeros while `rho>1/2`.

Therefore do not simply strengthen the same spatial-average estimate unless you can show exactly how it enters the hidden-interaction kernel or the Duhamel error.

## Decisive objective

Find a real bridge between the original dynamics and the regional companion factor identified by F, or prove that this bridge cannot come from the present density mechanism.

Useful possibilities include, but are not limited to:

- derive an estimate for the **oriented wall occupation/integral** that appears in F's Duhamel remainder, rather than for total zero density;
- prove a conditional or weighted version of your transport--dissipation estimate strong enough to imply
  $$
  \mathbb E^-[\eta_iF]\ge\rho\,\mathbb E^-[F]
  $$
  for the actual regional `F`;
- use the mesoscopic no-`11` regime to prove a regeneration or regional cancellation estimate, with an explicit error;
- independently compute the minimal scaffold cell and test whether left dependence is genuinely fatal;
- produce a counterexample showing that no theorem based only on one-time zero density or no-`11` probability can control the required weighted insertion.

If a different route gives a stronger irreversible step toward PRC, pursue it instead.

## Anti-circularity requirement

The output must bound a new measurable quantity, prove a one-way implication, or eliminate a route. Another density identity without a demonstrated interface to ergodicity/scaffold cancellation does not count.

If you prove a local estimate, test whether it survives at least one composition step. If you obtain only a marginal statement, explain why it is strictly stronger than the estimates from Assignment 001 and exactly where it enters the proof.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-g/002-density-to-regional-control.md`.

End with one of:

- `weighted regional estimate proved: ...`;
- `density mechanism cannot control the required kernel because: ...`;
- `new regeneration/composition estimate: ...`;
- `material route eliminated: ...`;
- `unresolved after substantive work; exact blocker: ...`.
