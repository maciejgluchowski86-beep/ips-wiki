# Student G assignment 003: restart-count bridge for the mass/disagreement block theorem

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/007-student-g-exposure-resolvent-and-restart-bottleneck.md`;
- `meetings/006-one-step-transfer-refuted-block-stack-target.md`;
- `notes/principal-centered-trail-update2.md`;
- your `002-density-to-regional-control.md`;
- Student F Assignments 003--004 for the coupling/coalescence lemmas;
- Student F `assignment-007.md` so your work is complementary rather than duplicative.

The fixed scientific target remains the positive rates conjecture for simple IPS.

## What you have now proved

For every live exposure edge with

$$
D_i=0,
\qquad D_{i+1}=1,
$$
including non-rightmost disagreements, if the exposure ends when either a left child is created or the right disagreement coalesces, then the dangerous state

$$
J_i=1_{\{X_i=Y_i=1\}}
$$
inside that exposure has an explicit killed-chain resolvent. In particular the child probability is uniformly `<1`, and

$$
E\left[\int J_i\right]
$$

is explicitly bounded. The exact child compensator is

$$
P(\text{child before right coalescence})
=
E\int\bigl[(b-a)+(c-b+a)J_i(t)\bigr]dt.
$$

Your crude all-time summation fails near East because it controls the number of exposure entries by raw disagreement occupations. The unresolved quantity is therefore the **restart/exposure-entry count**, not the single-exposure kernel.

## Current global spine

The principal trail reduction now uses

$$
B=b+c-a,
\qquad g=b-a,
\qquad \omega=1-c+a,
$$

and the exact centered insertion decomposition

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f).
\tag{MD}
$$

The first term is a signed mass component. The second is a positive coefficient times a conditional-law difference. Meeting 006 seeks a parameter-dependent block contraction on decompositions of these two kinds, weighted by unresolved disagreement-stack height.

Do not confuse your local indicator `J_i` with the global trail quantity `J_{x,r}`. The latter is the right-weighted invariant integral whose decay would close the nonempty-exit term.

## Objective

Build the **coupling-side bridge from `(MD)` to block contraction**.

Start with a conditional-law difference

$$
\mu^1-\mu^0
$$

produced by `(MD)`. Represent it by an explicit coupling of the two conditional laws. Track how a right-weighted zero-boundary transfer creates, removes, or restarts exposed disagreement edges.

The preferred theorem is a renewal/corrector estimate showing that repeated exposure entries are sufficiently controlled that, after a finite parameter-dependent block, the combined mass/disagreement weight contracts.

A useful successful statement could take one of the following forms:

1. an exponential-moment bound for the number of exposure entries before genuine stack regeneration;
2. a finite-state renewal kernel for bounded restart states plus a geometric tail controlled by the stack drift;
3. a Wasserstein/disagreement norm on `mu^1-mu^0` whose block evolution, together with the signed mass coefficient `Br-c`, has spectral radius `<1`;
4. a Foster--Lyapunov corrector involving both unresolved height and exposure-entry count;
5. an exact obstruction showing that the branching/restart mechanism defeats every natural finite-context version of the proposed block contraction.

The result must interface explicitly with `(MD)` and the right-weighted transfer from Meeting 006. A theorem only about the unweighted coupling process is not enough.

## Near-East stress test

Along

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

your crude global substitution loses all damping. The principal's block mechanism nevertheless has two favorable pieces:

- genuine stack regeneration has a strict mass multiplier, asymptotically `2/5` in the equilibrium mass channel;
- unresolved stack height has strict negative drift.

Your task is to determine whether the restart count between those regenerations has a weighted tail compatible with a net block contraction.

A contraction constant may tend to one as `epsilon->0`; only strict positive-rate parameter points need contraction.

## What not to do

Do not:

- derive another single-exposure `h_x` or `g_x` formula and stop;
- return to the closed cellwise scaffold positivity route;
- use the crude entry-count estimate from Assignment 002 as if it were sufficient;
- replace `mu^1-mu^0` by unrestricted total variation without proving a compensating gain;
- compute a few finite ancestry depths without an all-depth renewal/corrector statement;
- claim that your local `J_i` near-East obstruction refutes global `J_{x,r}->0`.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-g/003-restart-count-block-bridge.md`

with exact code/certificates beside it if useful.

End with one of:

- `restart-count block bridge proved: ...`;
- `coupling norm closes the mass/disagreement block theorem: ...`;
- `block route fails from the coupling side because: ...`;
- `unresolved after substantive work; exact restart-count blocker: ...`.
