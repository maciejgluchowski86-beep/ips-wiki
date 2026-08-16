# Student G assignment 005: solve the 16-phase all-height Foster feasibility problem

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/010-exposed-product-refuted-and-16-phase-foster-reduction.md`;
- your `004-global-restart-corrector.md` and verifier;
- `meetings/009-regenerated-mass-loss-and-duration-mode-obstruction.md`;
- Student F `008-bounded-signed-kernel.md` and current `assignment-009.md`;
- your Assignment 003 only with the explicit correction that its global exposed-only product lift is false.

The scientific target remains the positive rates conjecture for simple IPS.

## What is now settled

Your refutation is accepted. The exposed-only product corrector from Assignment 003 fails on the reachable all-`01` stack. For

$$
V=\lambda^H C_{\rm old},
$$

its exact tilted drift is

$$
\frac{\mathscr L_sV}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1),
$$

with `s>1`, `lambda>1`, `e_0>=1`, so it is positive for sufficiently large `H`. Near East, with the old choices, it tends to `(H-2)/7`.

The same-parent restart tail remains valid, but `M(s)phi(lambda)` is not a global Foster multiplier.

You also gave the correct stronger local ansatz. Put

$$
\mathcal A=\{00,11,01,10\},
$$

choose positive edge weights

$$
q_{\alpha\beta}>0,
\qquad (\alpha,\beta)\in\mathcal A^2,
$$

and define

$$
C_Q(\sigma)=\prod_i q_{\sigma_{i-1},\sigma_i}.
$$

For each triple `(alpha,beta,gamma)`, the exact local tilted bulk drift is

$$
G_Q(\alpha,\beta,\gamma)
=
\sum_{\beta'\ne\beta}
\Pi_{\beta,\gamma}(\beta')
\left[
 s^{\rho(\alpha,\beta,\gamma;\beta')}
 \frac{q_{\alpha\beta'}q_{\beta'\gamma}}
 {q_{\alpha\beta}q_{\beta\gamma}}
 -1
\right].
\tag{G}
$$

Uniform all-height bulk control for this nearest-neighbour product class is equivalent to a finite no-positive-cycle / coboundary condition: find a potential `psi` on `A^2` such that

$$
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma)
\tag{C}
$$

for all 64 triples.

## Objective

Determine whether the 16-phase nearest-neighbour product/coboundary class yields a **genuine global Foster theorem**.

Do not stop at the bulk condition. A successful theorem must include the finite boundary/height transitions:

1. rightmost coalescence and trimming of a coupled suffix;
2. creation of one new unresolved level by the next trail insertion;
3. left bookkeeping boundary transitions;
4. changes in the terminal edge phase when height changes.

The preferred result is:

> For every strict residual parameter point there exist `s>1`, `lambda>1`, positive `Q=(q_{alpha beta})`, a phase potential `psi`, finite `H_0`, and `delta>0` such that the full tilted generator of an explicit corrected functional has negative drift outside `H<=H_0`, uniformly over the allowed environment. Consequently arbitrary-height coupling/restart excursions return to a finite phase set with an exponential exposure-entry moment.

If this is false, prove an exact obstruction for this whole nearest-neighbour product/coboundary class. A single unavoidable positive cycle at one strict residual point or along the near-East path is enough to kill the class there, provided you prove it for **every** choice of positive phase weights, not merely the old weights.

## Finite feasibility formulation

Exploit the finiteness aggressively.

Write `q_{alpha beta}=exp(x_{alpha beta})` if useful. For fixed `(a,b,c,s)`, investigate the 16 variables `x`, the 16 coboundary variables `psi`, and the 64 inequalities `(C)`. The local expressions are nonlinear because each `G_Q` averages exponentials, but the graph structure is finite.

Useful routes include:

- analytic construction of phase weights from local coalescence/child probabilities;
- convexity/log-coordinate arguments;
- cycle inequalities eliminating `psi`;
- exact symbolic analysis of the few symmetry-distinct cycles;
- computer-assisted discovery followed by a hand-verifiable certificate;
- a Perron--Frobenius or multiplicative Poisson-equation formulation;
- proving that a matrix-product corrector is required because no scalar edge product can satisfy all cycles.

Any computational certificate used in the final claim must be accompanied by a mathematically explicit verification argument. A finite numerical optimizer output alone is not enough.

## Near-East stress test

Along

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

the old exposed-only product has positive drift `(H-2)/7` in the limit. Determine whether a nontrivial child-alive/susceptible phase weighting removes that positive bulk cycle.

A useful first question is whether there are asymptotic weights

$$
q_{\alpha\beta}(\varepsilon)
$$

for which every cycle mean is nonpositive to leading order. If not, extract an exact near-East cycle obstruction. If yes, push through finite positive `epsilon` and the boundary inequalities.

Do not treat the old `16/21` scalar as evidence of feasibility beyond a rough scale check.

## Interface with Student F

Student F is working on the signed mass/reset side. Its new theorem

$$
\left|\frac{B}{1+b}-c\right|Z<\frac23
$$

is independent of this assignment, and its mode-resolved `L^1(w)` work shows that duration/reset modes cannot be integrated before the norm.

Your coupling corrector does **not** need to solve F's mass-relaxation problem. But if you prove a Foster theorem, report the exact finite return state and transition kernel/phase data so F can tensor or augment it with the signed temporal modes. Do not claim that the 16 coupling phases alone close the full signed trail kernel.

## What not to do

Do not:

- repair only the all-`01` stack and ignore the other 63 triples;
- return another proposed local weight assignment without checking directed cycles and boundaries;
- use the scalar same-parent pgf times height factor as a global proof;
- count a fixed maximum ancestry depth;
- replace the signed mass branch by total variation;
- integrate F's duration modes before the `L^1(w)` norm.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-g/005-16-phase-foster-feasibility.md`

with exact verifier/certificate code beside it if useful.

End with one of:

- `16-phase global Foster theorem proved: ...`;
- `nearest-neighbour product/coboundary corrector refuted because: ...`;
- `matrix-product/nonlocal corrector required because: ...`;
- `unresolved after substantive work; exact finite feasibility blocker: ...`.
