# Student F assignment 005: all-depth disagreement-stack contraction or obstruction

Work on branch `research/positive-rates-conjecture`.

The scientific target remains fixed: prove the positive rates conjecture for simple IPS.

Read first:

- updated `state.md` and `proof-spine.md`;
- `meetings/004-two-generation-regeneration-and-depth-obstruction.md`;
- your Assignment 003 and 004 reports;
- Student G Assignment 001 for the transport / `11` estimates;
- the closed fixed-wall and cellwise-scaffold records only as route exclusions.

Student G is still finishing Assignment 002. Do not wait for it.

## What is now established

Under the common-uniform coupling, every disagreement site has predictable coalescence intensity at least

$$
q=1-c+a>0
$$

regardless of orientation and regardless of whether its right neighbour is agreed or disagreed.

If a disagreeing site is immediately to the right of an agreed site, then it coalesces before that agreed site's next rate-one clock ring with conditional probability at least

$$
p=\frac q{1+q}.
$$

After the first child is born, this gives the genuine two-generation regeneration bound

$$
\mathbb P(\tau_2<\sigma_2\mid\mathcal F)
\ge p^2.
$$

Reinfection is included in the process; the successful event is a subevent on which the relevant reinfection clocks do not beat the coalescences.

Meeting 004 also corrected the finite-depth formulation: `p^m` is a valid ordered-clearing lower bound when `m` bounds the **active-span depth**, not merely the number of disagreement sites currently present. These depth-dependent gaps are summable and therefore do not themselves force extinction of an ancestry stack whose depth keeps increasing.

## Decisive objective

Do **not** compute a three-generation analogue and stop there.

Find an **all-depth structural contraction** for the live disagreement process, or a rigorous obstruction showing that the most natural such contractions cannot work.

The output must handle arbitrary finite ancestry depth in one theorem/inequality.

## Promising structural routes

These are suggestions, not restrictions.

### 1. Weighted disagreement-stack Lyapunov function

Search for a nonnegative local weight on pair states and a spatial weight `lambda` such that a quantity of the general form

$$
W(X,Y)
=\sum_i \lambda^{r-i} w(S_i,S_{i+1},\ldots)
$$

has negative generator drift while the disagreement episode is alive. The state weight may distinguish disagreement orientation, agreed zero/one, the high-risk state `J_i`, or a short finite context.

The useful theorem would be a genuine supermartingale / drift inequality implying that the leftward disagreement front cannot escape indefinitely.

A finite linear-program or symbolic search for candidate weights is acceptable, but a numerical witness without a proof valid throughout the residual parameter point under study is not enough.

### 2. Finite multi-type branching/influence domination

Use the uniform coalescence hazard `q` and the exact child-creation kernels to define finitely many disagreement types. Determine whether there is a finite mean offspring/transfer matrix whose spectral radius is `<1` and which rigorously dominates the true live ancestry stack.

If this succeeds only on part of the residual chamber, characterize the parameter region exactly and explain whether a complementary mechanism remains.

### 3. Close the coupling drift through `J_i`

Meeting 003 established

$$
\mathcal L^{\rm coup}D_i
\le
-qD_i+(b-a)D_{i+1}+(c-b+a)J_i.
$$

The marginal `11` estimate is insufficient because it creates an additive term. Seek a **disagreement-weighted** or conditional estimate of the form

$$
\mathbb E J_i
\le \alpha\,\mathbb E D_{i+1}+\beta\,\mathbb E D_i
$$

or an integrated version strong enough to close a Gronwall / weighted-sum inequality. Any such coefficients must be explicitly checked in the residual chamber.

### 4. Finite summary / restart kernel

Identify a finite summary of an arbitrarily deep ancestry stack whose transition law dominates the true process and has a strict contraction. This would be the cleanest way to convert the finite-depth clearing events into a genuine renewal theorem.

## Falsification discipline

The following do not count as progress:

- depth-three or depth-four hitting probabilities without an all-depth theorem;
- replacing active-span depth by another equivalent stack notation;
- another marginal zero / `11` estimate;
- a branching-process analogy without a rigorous domination;
- a Lyapunov candidate whose drift is checked only numerically on sample parameters;
- using the crude death-rate `q` alone in a contact-process comparison if the resulting comparison is supercritical and no sharper state structure is proved.

If every natural finite-context Lyapunov or multi-type domination fails, produce an explicit residual parameter/state obstruction and explain what feature defeats it. That would be useful narrowing.

## Near-East discipline

The East boundary remains a stress test, not part of the target. Along

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

the first-generation gap is order `epsilon^2`, while the structured two-generation controlled gap is order `epsilon`.

Any proposed all-depth mechanism should be tested asymptotically on this path. A contraction constant may tend to zero as `epsilon->0`; what matters is whether it stays positive at each strict parameter point and whether the all-depth argument actually composes.

## Anti-circularity requirement

Meeting 004 deliberately stops finite-depth escalation. Your report must end with one of:

- `all-depth contraction proved: ...`;
- `finite multi-type renewal proved: ...`;
- `weighted disagreement drift proved: ...`;
- `all-depth route fails because: ...`;
- `unresolved after substantive work; exact structural blocker: ...`.

Commit to

`research/active/positive-rates-conjecture/students/student-f/005-all-depth-disagreement-stack.md`

with supporting code/certificates beside it if useful.
