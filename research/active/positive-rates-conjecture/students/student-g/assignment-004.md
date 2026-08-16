# Student G assignment 004: rigorize the global restart-corrector Foster lift

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/008-restart-tail-and-empty-supnorm-region.md`;
- your `003-restart-count-block-bridge.md` and verifier;
- Student F `007-block-mass-disagreement-contraction.md`;
- Student F `assignment-008.md` so your work remains complementary;
- Meetings 006--007 and the principal mass/disagreement-stack note.

The scientific target remains the positive rates conjecture for simple IPS.

## What is accepted from Assignment 003

The following are Professor-checked:

1. for one fixed parent episode, the number of exposure entries before that parent first coalesces satisfies
   $$
   P(N\ge n\mid\mathcal F)\le h_1^{n-1};
   $$
2. hence for `1<=s<h_1^{-1}`,
   $$
   E[s^N\mid\mathcal F]\le M(s)=\frac{(1-h_1)s}{1-h_1s};
   $$
3. the stack-clearing minorant gives
   $$
   \phi(\lambda)=\lambda\left(1-\alpha+\frac{\alpha}{2\lambda-1}\right)<1
   $$
   on the stated interval;
4. algebraically, near East the proposed choice `lambda=2`, `s=1+epsilon^2/4` gives
   $$
   M(s)\phi(2)\to16/21<1.
   $$

What is **not yet accepted** is the step from these scalar bounds to the global product corrector `C_s` and Foster inequality `(5.4)` for all unresolved levels simultaneously.

## Exact issue to resolve

Your report assigns local factors to unresolved levels and states that already-existing same-parent restarts have nonpositive corrected drift while only one genuinely new level costs at most `M(s)`. For a closing theorem this must be made pathwise/Markovian, not asserted informally.

Define an explicit global phase state that distinguishes, at minimum, the statuses needed for a parent level whose child is:

- currently agreed and exposed;
- currently disagreeing after child creation;
- returned to agreement and re-exposed;
- parent coalesced but susceptible to later reinfection from deeper ancestry;
- or permanently removed by the certified clearing mechanism.

Then prove transition by transition that the chosen corrector is superharmonic, or modify the corrector until it is.

The main concern is that an unresolved level that is not currently exposed can later become exposed again; a factor `1` for an inactive phase is not automatically enough unless the future restart cost has already been prepaid somewhere else in the state variable. Make that bookkeeping explicit.

## Objective

Prove one of the following.

### Preferred theorem

There exists a rigorously defined global state `Sigma`, a corrector `C_s(Sigma)`, and

$$
V_s(\Sigma)=\lambda^{H(\Sigma)}C_s(\Sigma)
$$

such that for every strict residual point there are `lambda>1`, `s>1`, finite `H_0`, and `theta<1` with

$$
E[s^{\Delta R}V_s(\Sigma')\mid\mathcal F]
\le\theta V_s(\Sigma)
$$

for `H>=H_0`, uniformly over the allowed exterior environment.

Derive from this a fully explicit small-set/renewal theorem giving an exponential moment for the total restart count until inherited-stack regeneration.

### Acceptable alternative

If the product-corrector construction fails, identify an exact transition or residual state for which no assignment of the proposed finite local phase weights can be superharmonic. Then state what stronger state variable is required.

## Interface with Student F

Student F is now attacking the **bounded-height signed mass/disagreement kernel conditional on your Foster lift**. If you prove the lift, give the exact finite phase set and constants that F can insert. If you refute it, give the smallest explicit obstruction immediately so F does not build on a false premise.

## F correction you must incorporate

The crude condition

$$
\max\{c,b-a\}Z<1
$$

has **no solutions in the residual chamber**; F proved `cZ>1` everywhere there. Do not cite a pre-existing easy residual subregion.

This does not affect the same-parent geometric tail or the proposed restart/height corrector, which are different objects.

## What not to do

Do not:

- repeat the same-parent tail proof and stop;
- treat `M(s)phi(lambda)<1` algebra alone as a proof of the global Foster inequality;
- hide inactive/reinfected phases in an undefined product factor;
- replace the remaining signed mass branch by total variation;
- claim `16/21` controls `J_{x,r}` directly.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-g/004-global-restart-corrector.md`

with an exact finite-state verifier if useful.

End with one of:

- `global restart-corrector Foster theorem proved: ...`;
- `finite restart phase reduction proved: ...`;
- `product corrector fails at: ...`;
- `unresolved after substantive work; exact global-corrector blocker: ...`.
