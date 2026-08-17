# Student F assignment 015: stationary boundary-control corrector concatenation

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/023-stationary-boundary-control-hierarchy-reopens-one-proof-test.md`;
- `notes/principal-stationary-boundary-control-strategy.md`;
- current `state.md` and `proof-spine.md`;
- F014 only to remember that the predecessor-trail/profile implementation is exhausted and must not be revived;
- consultation 002 only for the path-space `Q` isometry obstruction.

The scientific target remains the positive rates conjecture. This is one bounded feasibility test of a **new static stationary-law architecture**.

Do not work on `J-SPEC`; Student G owns that in parallel.

## 1. Exact object

Use the complemented spin convention

$$
\xi_i=1-\eta_i,
$$

so that `1` is the East facilitator. Put

$$
g=b-a,\qquad k=1-c.
$$

Then

$$
0\to1\text{ at rate }a+g\xi_{i+1},
\qquad
1\to0\text{ at rate }k+c\xi_{i+1}.
$$

For a block `x in {0,1}^N` and fixed right-boundary control `u in {0,1}`, let `L_N^u` be the finite generator.

Define

$$
\mathcal K_N
=
\left\{
 m(x,u)\ge0:
 \sum_{x,u}m(x,u)=1,
 \quad
 \sum_{x,u}m(x,u)L_N^uF(x)=0
 \ \forall F
\right\}.
$$

For local `h`,

$$
D_N(h)
=
\sup_{m\in\mathcal K_N}m(h)
-
\inf_{m\in\mathcal K_N}m(h).
$$

Meeting 023 already checks that every infinite-volume invariant law projects into `K_N`, that the hierarchy is nested, and that finite-dimensional LP duality gives

$$
U_N(h)
=
\inf_F\max_{x,u}\bigl(h(x)-L_N^uF(x)\bigr),
$$

$$
\ell_N(h)
=
\sup_F\min_{x,u}\bigl(h(x)-L_N^uF(x)\bigr),
$$

with `D_N=U_N-ell_N`.

Independently rederive these facts before using them, but do not spend the block merely rewriting them.

## 2. Primary target: derive a repeatable corrector concatenation

The principal proposes a multiscale inequality of the form

$$
\boxed{
D_{2N}(h)
\le
(1-\rho)D_N(h)+Ce^{-\gamma N}
}
\tag{R}
$$

for `N>=N_*(a,b,c)` with `rho,gamma>0` depending on the fixed rates.

Your task is to decide whether the LP dual has a **structural composition rule** capable of proving `(R)` or a comparably strong scale recursion.

A useful positive result must do more than solve two finite LPs. It should identify how an upper/lower corrector on an `N`-block can be embedded, translated, averaged, or supplemented by a bounded interface corrector to produce a valid inequality on a `2N`-block **uniformly over both values of the adversarial boundary control at every state**.

You may enlarge the finite corrector by a fixed interface state independent of `N`, but do not replace the problem by an arbitrary depth-growing matrix ansatz.

## 3. Computational reconnaissance

Use computation to discover the corrector structure if useful.

The principal reports for `h(x)=x_0`:

| `(a,b,c)` | `D_5` | `D_9` |
|---|---:|---:|
| `(10^-4,10^-2,0.9999)` | `0.16055` | `0.01185` |
| `(0.002,0.1,0.9999)` | `0.28486` | `0.02100` |
| `(0.001,0.1,0.9999)` | `0.40101` | `0.04863` |

Treat these only as motivation. Independently reproduce whatever finite values you use.

If floating-point LPs suggest a sparse/rational dual corrector, rationalize it and verify the Bellman inequalities exactly. A larger exact finite certificate with no theorem that it repeats is not a successful outcome.

## 4. Hard-East ingredient: identify the exact robustness lemma

The principal points to hard-East relaxation behind a facilitator. The attached KCM book gives:

- Theorem 7.6: exponential convergence of hard-East local observables once a facilitator is present in the oriented future;
- Theorem 7.8: linear finite-volume East mixing time with empty or ergodic boundary.

These theorems do **not** directly imply `(R)` for the noisy chain under arbitrary state-dependent control.

Formulate precisely the additional statement that would be needed to turn a neighbour-independent facilitator reset into a fixed-probability screening event for the controlled noisy block.

Then do one of the following:

1. prove a usable robustness/censoring lemma, even on a genuine residual subregion;
2. reduce it to an explicit finite set of Bellman inequalities which your corrector concatenation verifies;
3. prove a precise obstruction showing that the arbitrary controller or the soft reset noise defeats the proposed block screening mechanism.

Do **not** condition on the absence of all soft/noisy marks over an `O(N)` spacetime block and call the resulting exponentially small event the screening probability. The desired `rho` must stay positive at fixed rates as `N` grows.

## 5. Static target only

If you obtain a scale recursion forcing

$$
D_N(h)\to0
$$

for all local `h`, state exactly the parameter region and constants. This proves uniqueness of the invariant measure.

Do not spend this assignment on the later dynamic upgrade `(ZF)` unless the static theorem is already complete. Static uniqueness is not yet full ergodicity.

## 6. What does not count

Do not return as a positive result:

- smaller numerical `D_N` at larger `N`;
- a single finite LP certificate with no concatenation theorem;
- a generic spectral-gap or full-chain mixing assumption;
- path-space `Q` contraction, which consultation 002 refutes globally;
- a renamed tail-shift theorem;
- a third predecessor-trail insertion or common-uniform occupation argument;
- a hard-East theorem quoted without a proof that its hypotheses survive the noisy controlled block.

## 7. Successful outcomes

A strong positive outcome is an explicit theorem of the form

$$
D_{2N}(h)\le(1-\rho)D_N(h)+\varepsilon_N,
\qquad
\sum_j\varepsilon_{2^jN}<\infty,
$$

or another repeatable recursion implying `D_N(h)->0`, proved on a nontrivial residual region.

A useful negative outcome is an exact obstruction to concatenating the finite LP correctors uniformly over the controller, or a counterexample to the required robust seed-screening lemma.

If you get only finite-box shrinkage and no repeatability mechanism, report unresolved and stop.

## 8. Stopping rule

This is one bounded architecture-feasibility block.

If it returns unresolved without a repeatable corrector/screening mechanism, do not propose a larger `N` LP sweep as the successor. The Professor will reassess the route.

End with exactly one of:

- `stationary screening mechanism proved: ...`;
- `stationary screening mechanism refuted because: ...`;
- `unresolved after substantive work; boundary-control blocker: ...`.

## 9. Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/015-stationary-boundary-control-screening.md`

with exact verifier/certificate code beside it when computation is used.
