# Student G assignment 006: decide survival/extinction of the common-uniform disagreement process near East

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/012-balanced-circulation-refutes-16-phase-product-class.md`;
- your `005-16-phase-foster-feasibility.md` and verifier;
- your `004-global-restart-corrector.md`;
- Student F `009-mode-resolved-l1-block.md` and current `assignment-010.md`;
- Meetings 003--004 for the earlier live-source and finite-clearing coupling estimates.

The scientific target remains the positive rates conjecture for simple IPS.

## What is now closed on your line

Two scalar local global-corrector mechanisms are closed.

1. The exposed-only independent-level product from Assignment 003 fails on reachable long all-`01` stacks.
2. The complete nearest-neighbour scalar edge-product/coboundary class from Assignments 004--005 fails at the strict residual point
   $$
   (a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right)
   $$
   by your balanced-circulation AM--GM certificate.

Do not enlarge the scalar local context or search another finite commutative product ansatz.

The same-parent geometric restart theorem remains correct, as does the separate stack-height clearing minorant.

## Objective

Decide whether the **common-uniform coupling itself** is a viable global coalescence/regeneration mechanism in the hard near-East regime.

The preferred question is:

> Starting from a finite nonempty disagreement seed under the common-uniform coupling, can the disagreement process survive forever with positive probability at a strict near-East residual point?

Use the same rational point above if convenient. A theorem on all sufficiently small

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2
$$

is stronger but not required. A single strict residual point is enough to show that successful global coalescence of this coupling cannot serve as a proof throughout the chamber.

You have broad freedom in the choice of finite initial pair of configurations. State it explicitly. A useful target would be a single `01` disagreement in an otherwise agreed configuration, or another finite seed for which the graphical argument closes.

## Successful outcomes

### A. Survival theorem

Prove that for some finite disagreement seed,

$$
\mathbb P(D_t\ne\varnothing\text{ for all }t\ge0)>0,
$$

or an equivalent event of unbounded leftward disagreement ancestry.

A rigorous block construction or domination of a known supercritical one-dimensional oriented growth process is acceptable. You must specify the spacetime blocks, dependence structure, and inequalities; do not cite a vague contact-process analogy.

If you prove survival, explain precisely what it kills:

- any argument requiring this common-uniform coupling to globally coalesce from every finite disagreement seed;
- any Foster/regeneration theorem whose conclusion would imply such extinction.

Do **not** claim that survival refutes ergodicity or the centered signed-trail route. Synchronous couplings can fail even for ergodic processes.

### B. Extinction / nonlocal regeneration theorem

If the finite disagreement process dies out almost surely, prove a quantitative statement strong enough to replace the failed local products. Examples:

- an exponential or stretched-exponential tail for the lifetime/maximum leftward range at each fixed strict parameter point;
- a nonlocal renewal construction at complete-clearing times with an exponential moment sufficient to control repeated disagreement branching;
- a block contraction that bundles all interior exposure creation before charging a norm.

The theorem must be genuinely nonlocal; do not repackage the refuted scalar local edge products.

### C. Exact viability obstruction

If neither survival nor extinction can be proved in this block, identify the exact comparison or dependence issue preventing the decision, and reduce it to one concrete theorem rather than another corrector ansatz.

## Existing inputs you may use

From the accepted coupling work:

- every disagreement site has coalescence probability at its own update at least
  $$
  q=1-c+a;
  $$
- near East, local leftward transmission before simple competing changes is close to one;
- one fixed parent's exposure re-entry count before its first coalescence has a geometric tail;
- the principal clearing variable gives negative drift for the unresolved stack height in the certified clearing episode;
- the all-`01` stack and balanced circulation show that exposure production in the bulk cannot be prepaid by a scalar local potential.

These statements concern different observables. Do not multiply their constants unless the conditioning and stopping times actually justify it.

## Suggested survival route

Near East the heuristic rates strongly favor transmission over coalescence. Test a spacetime block event in which a disagreement at the right side of a block creates a left child (or a short left run) before the parent dies, while enough of the local orientation is preserved to iterate on disjoint or finitely dependent blocks.

If you can obtain a one-dependent oriented percolation comparison, give an explicit success probability and a rigorous criterion proving it exceeds a supercritical threshold. If using another comparison theorem, state exactly the external theorem/hypotheses and verify them.

Do not rely on simulation as proof. Computation may search for block parameters, but the final certificate must be mathematically checkable.

## Interface with Student F

F is independently studying the common-mass profile hierarchy and does not require this assignment to succeed.

If common-uniform disagreement survival is proved, tell F only the narrow consequence: its mass/disagreement representation cannot rely on eventual global coalescence of that synchronous coupling; local coupling identities may remain usable.

If extinction with a nonlocal quantitative regeneration theorem is proved, formulate the return kernel/stopping-time data in a way F could condition its profile-valued `L^1(w)` transfer on.

## What not to do

Do not:

- try another scalar finite-range product/coboundary corrector;
- enlarge the 16-phase alphabet mechanically;
- claim matrix-product correctors fail without proof;
- infer nonergodicity from failure or survival of the synchronous coupling;
- replace the signed mass branch by total variation;
- return only a finite-time simulation or a few-generation calculation.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-g/006-common-coupling-survival.md`

with exact code/certificates beside it if useful.

End with one of:

- `common-uniform coupling survives from a finite seed at: ...`;
- `common-uniform coupling extinction/regeneration proved: ...`;
- `common-uniform global coalescence route remains unresolved; exact blocker: ...`.
