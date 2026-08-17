# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

The scientific target remains fixed:

> Prove the positive rates conjecture for one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/033-mark-only-information-percolation-killed-gray-scalar-edge-last-bounded-test.md`, `state_narrowed: yes`.

## Active work

Student G is active on

`students/student-g/assignment-013.md`

at commit `190ec3d158353eae45a7639b19c651cca6752641`.

Assignment 013 is the final bounded structural test of the remaining toolbox PASS candidate: whether a scalar/two-type Gray-style splice-edge grand coupling can close locally at the hard point. It is not a full proof-programme reopening.

Student F remains idle. No F016 is active.

## G012 information-percolation pair histories: accepted `STOP-PAIR-OBSTRUCTION`

At

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

G012 classifies every exact deterministic Boolean random-map decomposition by aggregate ancestry rates

- `d`: constant/death;
- `s`: self-only;
- `j`: right-only;
- `r`: genuine two-parent.

The exact projected polytope is verifier-backed, but the pair obstruction only needs the direct inequalities

$$
\boxed{d+j\le\frac1{5000}},
\qquad
\boxed{r\ge\frac{4999}{5000}}.
$$

These follow directly from the four flip-rate budgets and essential-parent classification, independently of vertex enumeration.

For two independent mark-only backward supports, G constructs a width-one block event of duration `T=8` such that a common ancestor at site `i` produces common ancestors at both `i` and `i+1`. Uniformly over every admissible decomposition, the bad-cell probability satisfies

$$
q<\frac{18483379}{2500000000}<\frac1{128}.
$$

The good-cell field is independent between time layers and one-dependent in space. A simple minimal bad-cut contour estimate gives positive survival probability for the lower oriented common-ancestor cluster and therefore

$$
\inf_{n\ge0}
E\left[2^{|A_{8n}\cap A'_{8n}|}-1\right]>0.
$$

The final report gives the crude explicit lower bound `>1/121`. The scalar verifier checks the rational cell bounds; the Professor separately checked the planar contour argument with simple/minimal contours.

### Constant change audit

The initial G012b checkpoint used an under-anchored contour count `2 3^m` and obtained a displayed survival lower bound `1/7`. The final proof safely counts at most `2m 3^m` contours, tightens the cell bound from `q<1/100` to `q<1/128`, and obtains the weaker but valid explicit survival lower bound `1/121`. The change is intentional rather than an arithmetic slip.

### Scope

Killed:

> the optimized **mark-only deterministic-Boolean minimal-support** information-percolation bridge tested in Assignment 012, for every exact local random-map decomposition at `P_h`.

Not killed:

- a genuinely state-adaptive reveal process using discovered spin values to prune essential parents;
- a nonadditive Gray splice-edge geometry;
- the positive-rates conjecture itself.

State-adaptive reveal is not automatically promoted after this negative result. It presently lacks a concrete bounded bridge and risks importing the unknown spin law/mixing statement it is meant to prove.

## G011 distinguished-zero transfer remains closed as `STOP-EQUIVALENT`

The `pi_N`-based East transfer fails off the product surface. Exact one-step prefix compatibility requires

$$
\bar\pi_{N+1}=\pi_N,
$$

and at `N=1 -> 2`

$$
\bar\pi_2(1)-\pi_1(1)
=-\frac{2a\,[a-b(1-c)]}
{(a+1-c)\,[2ab-ac+3a-bc+b+c^2-3c+2]}.
$$

The compatibility locus is exactly

$$
a=b(1-c),
$$

where

$$
\pi_N=\operatorname{Ber}\!\left(\frac b{1+b}\right)^{\otimes N}.
$$

A contaminated buffer gives exactly the old tail-shift defect `Delta_M`; a finite release kernel cannot change the protected prefix. Marker-existence analysis is therefore moot for that architecture.

## Uniform additive-Hamming coupling bridge remains killed

For any Markovian coupling of two spin-flip chains, off-diagonal cross-site joint jumps cannot improve the drift of additive Hamming distance. The optimal drift is

$$
\inf_{\text{couplings}}\bar L H
=
\sum_{i:x_i=y_i}|\lambda_i(x)-\lambda_i(y)|
-
\sum_{i:x_i\ne y_i}(\lambda_i(x)+\lambda_i(y)).
$$

At `P_h`, a one-disagreement local pattern has best possible drift

$$
\frac{9997}{10000}>0.
$$

Thus the toolbox refined-coupling bridge requiring uniform negative Hamming drift is impossible for every Markovian coupling. This does not decide Gray's nonadditive scalar-edge mechanism.

## Active final bounded test: Gray scalar splice edges

Assignment 013 reconstructs the load-bearing Gray hybrid identities and asks whether they admit a direct scalar/two-type replacement without attraction or repulsion.

The test must:

1. formulate a faithful finite local edge-state class and pass attractive/repulsive sanity checks;
2. impose exact grand-coupling marginals, scalar hybrid closure, protection, no crossing and permanent coalescence;
3. at `P_h`, either derive an analytic rate obstruction, produce an exact rational infeasibility certificate, or exhibit an explicit locally feasible scalar-edge mechanism.

The assignment does **not** allow escalation to larger edge-state hierarchies if scalar/two-type closure fails.

Permitted statuses:

- `STOP-SCALAR-EDGE-OBSTRUCTION`;
- `STOP-NO-FAITHFUL-LOCALIZATION`;
- `CONTINUE-GRAY-BRIDGE`.

If this bounded Gray test stops negatively, the toolbox-derived positive-rates opportunity set is exhausted. There is no automatic restart on state-adaptive histories, larger edge states, generic coupling/norm searches, or old stopped routes.

## Previous connected-renewal route remains stopped

The sharp residual object remains the signed boundary-transmission Volterra operator

$$
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
$$

No depth-uniform actual-orbit estimate retaining its two-time cancellation has been proved. Meeting 030's restart bar remains operative.

Bare tail shift, common-uniform all-depth occupation, Bellman/joint-corrector, scalar Foster, reversible-comparison continuation, generic norm searches, and longer coefficient tables remain stopped.

## Retained exact mathematics

Retained background includes the predecessor-trail reduction and canonical `J` quantity, projective zero-boundary invariant family and tail-shift identity, common-coupling fixed-site/local-erasure and actual-front results, stationary-control hierarchy, trajectory-valued spatial-kernel obstruction, G009/G010 positive-frequency/renewal structure, G011's product-surface distinguished-zero obstruction, the universal additive-Hamming coupling obstruction, and G012's random-map ancestry polytope/pair-history obstruction.

## Unresolved target-level facts

Open:

- whether a direct nonadditive scalar/two-type Gray splice-edge geometry exists at `P_h`;
- one-/two-step tail-shift agreement off the product surface;
- `(J-SPEC)` and connected-tail `(CT)`;
- the actual-orbit signed boundary-transmission estimate `(V)`;
- common-uniform extinction versus convective survival;
- stationary diameter collapse `D_N(h)->0`;
- whether a genuinely state-adaptive information-history theorem can be formulated without circularity;
- full ergodicity in the residual chamber.

## Wiki

Keep the live wiki frozen during research. No `docs/` or `mkdocs.yml` edits are authorized.
