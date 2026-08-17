# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every one-dimensional homogeneous binary one-sided nearest-neighbour simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/033-mark-only-information-percolation-killed-gray-scalar-edge-last-bounded-test.md`, `state_narrowed: yes`.
- Student G: active on Assignment 013, scalar Gray splice-edge feasibility.
- Student F: idle; no F016.
- No full proof architecture is reopened. G013 is one final bounded structural test of the last untested toolbox PASS mechanism.

## Most recent result: mark-only information percolation is pair-obstructed

Student G Assignment 012 is accepted as **`STOP-PAIR-OBSTRUCTION`**.

At

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

every exact deterministic-Boolean random-map decomposition has aggregate mark-only ancestry rates satisfying

$$
d+j\le\frac1{5000},
\qquad
r\ge\frac{4999}{5000},
$$

where `d,j,r` are death, right-only and genuine two-parent rates.

For two independent backward supports, a width-one `T=8` good-cell event maps one common ancestor to two adjacent common ancestors. Uniformly over the whole decomposition polytope, the bad-cell probability is less than `1/128`. The good-cell field is independent between time layers and one-dependent in space; a simple minimal bad-cut contour argument yields positive survival probability of an oriented common-ancestor lower cluster. Hence

$$
\inf_{n\ge0}
E\left[2^{|A_{8n}\cap A'_{8n}|}-1\right]>0.
$$

This kills the **mark-only deterministic-Boolean minimal-support** information-percolation bridge at the hard point for every exact local decomposition. It is a pair-history obstruction, not a first-moment argument.

A state-adaptive value-reveal history is not ruled out, but no such bridge is presently specified noncircularly and it is not automatically promoted after the failure of the mark-only route.

The final G012 constants were audited: an initial contour count missing an anchoring factor was replaced by the safe `2m 3^m` bound; the cell estimate was tightened from `q<1/100` to `q<1/128`; the displayed survival lower bound therefore became weaker (`1/121` rather than `1/7`). This is intentional.

## Earlier principal-directed result: distinguished-zero transfer

Student G Assignment 011 remains accepted as **`STOP-EQUIVALENT`**.

The proposed transfer of East distinguished-zero screening by substituting the finite zero-boundary invariant family `pi_N` for Bernoulli equilibrium fails off the product surface. Exact one-step prefix compatibility holds precisely on

$$
a=b(1-c),
$$

where

$$
\pi_N=\operatorname{Ber}\!\left(\frac b{1+b}\right)^{\otimes N}.
$$

Off that surface, buffered screening is exactly the old tail-shift defect and finite release kernels cannot repair the untouched protected prefix. Marker-existence analysis is moot for that architecture.

## Universal additive-Hamming coupling obstruction

Meeting 032 proves that cross-site pairing cannot improve instantaneous drift of additive Hamming distance under any Markovian coupling. At `P_h`, a one-disagreement local pattern has best possible drift

$$
\frac{9997}{10000}>0.
$$

Thus the refined-coupling bridge requiring uniform negative additive-Hamming drift is false for every Markovian coupling. This does not refute Gray's nonadditive edge geometry.

## Active bounded experiment: Gray scalar splice edges

Assignment 013, commit `190ec3d158353eae45a7639b19c651cca6752641`, reconstructs Gray's load-bearing hybrid identities and tests whether a direct scalar/two-type nonmonotone replacement can close locally at `P_h`.

The local definition must first accept representative attractive/repulsive cases. It must then impose exact grand-coupling marginals, scalar hybrid closure, protected regions, no crossing and permanent coalescence. G must return an analytic rate obstruction, exact local infeasibility certificate, or an explicit feasible scalar-edge mechanism.

If scalar/two-type closure fails, the assignment forbids escalation to larger edge-state hierarchies. A negative G013 return exhausts the toolbox-derived A/B positive-rates opportunity set; there is no automatic restart on adaptive histories or generic coupling/norm searches.

## Connected-renewal route remains stopped

The sharp blocker remains the signed boundary-transmission Volterra operator on the actual connected orbit,

$$
\mathcal V_N f
=B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
$$

Both temporal factors change sign. No depth-uniform estimate preserving the two-time cancellation has been proved.

Bare tail shift, another `pi_N` distinguished-zero buffer, common-coupling all-depth occupation, uniform additive-Hamming coupling, mark-only Boolean support information percolation, Bellman/scalar Foster variants, reversible perturbation, generic norm searches, and longer coefficient tables remain stopped.

## Retained mathematics

Retained background includes the predecessor-trail reduction and canonical `J` quantity, projective zero-boundary invariant family and exact tail-shift identity, common-coupling fixed-site/local-erasure and actual-front results, stationary boundary-control hierarchy, exact trajectory-valued spatial kernel obstruction, G009/G010 positive-frequency/renewal structure, G011's product-surface distinguished-zero obstruction, the universal additive-Hamming coupling theorem, and G012's exact random-map ancestry/pair-history obstruction.

## Wiki freeze

The live wiki remains frozen during active research. No `docs/` or `mkdocs.yml` edits are authorized by the current work.
