# Group meeting 010: exposed-only Foster product is false; all-height coupling bulk reduces to a 16-phase cycle problem

Date: 2026-08-16

Professor review of:

- Student G, commit `4128cee`, `students/student-g/004-global-restart-corrector.md`;
- exact verifier commits `bec4dda` and `4586833`, `students/student-g/004-global-restart-corrector-verifier.py`;
- Meetings 008--009;
- Student F's current mode-resolved `L^1(w)` assignment.

Operational correction: Meeting 009 recorded Student G as still in flight on Assignment 004. G returned after that meeting. This note records the mathematical ruling without rewriting Meeting 009 retrospectively.

state_narrowed: yes

Evidence pointer: `students/student-g/004-global-restart-corrector.md`, especially Sections 4--10, and `students/student-g/004-global-restart-corrector-verifier.py`.

## Previous bottleneck

Meeting 008 accepted G's same-parent restart tail but declined to promote the proposed product Foster lift because simultaneous unresolved levels were not represented by an explicit global phase state. Meeting 009 still treated that lift as unverified while F worked conditionally on a scalar Foster premise.

G has now supplied the missing transition-by-transition test. The proposed exposed-only product corrector is not merely unproved; it is false.

## Professor verification: reachable all-`01` stack kills the old product

Write

$$
\omega=1-c+a,
$$

and consider a coupled stack with bookkeeping boundary `sigma_{-1}=00`, coupled zero right boundary, and

$$
\sigma_i=(X_i,Y_i)=01,
\qquad 0\le i\le H-1.
$$

This state is reachable: if an exposed parent has orientation `01` and its agreed left child is zero, a child-creation update produces a new `01` disagreement with probability `b-a>0`; repetition produces arbitrarily long runs with positive probability.

Assignment 003's product assigned an exposed `00|01` edge a factor `e_0>=1`, while every nonexposed unresolved level carried factor one. Let

$$
V=\lambda^H C_{\rm old},
\qquad s>1,
\qquad \lambda>1.
$$

I independently checked the local common-uniform transitions.

For the leftmost `01`, whose right neighbour is also `01`, the update `01->00` occurs with probability `1-a`. It moves the unique exposure one step right, so `C_old` is unchanged but one exposure entry is charged. Its tilted contribution is

$$
(1-a)(s-1).
$$

For each interior site `1<=i<=H-2`, the same `01->00` event creates an additional exposed edge while the original leftmost exposure remains. Thus `C_old` gains a factor `e_0` and one entry factor `s`, giving contribution

$$
(1-a)(s e_0-1).
$$

At the rightmost disagreement, with coupled-zero right boundary, coalescence occurs with probability

$$
\omega=1-c+a.
$$

That permanently removes one unresolved level, contributing

$$
\omega(\lambda^{-1}-1).
$$

Therefore

$$
\boxed{
\frac{\mathscr L_sV}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1).
}
$$

Because `s>1` and `e_0>=1`, the coefficient of `H-2` is strictly positive. The negative height-boundary term is independent of `H`. Hence for every strict residual point, every fixed `s>1`, every finite `lambda>1`, and every corrector of this exposed-only form, the tilted drift is positive for all sufficiently large `H`.

This exactly refutes Assignment 003's global product rule.

## Near-East check and status of `16/21`

On

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

with the Assignment-003 choices

$$
s=1+\frac{\varepsilon^2}{4},
\qquad \lambda=2,
$$

the exposed factor satisfies

$$
e_0\to\frac87.
$$

The exact tilted drift therefore obeys

$$
\boxed{
\frac{\mathscr L_sV}{V}\to\frac{H-2}{7}.
}
$$

Thus the previously checked scalar diagnostic

$$
M(s)\phi(2)\to\frac{16}{21}<1
$$

is not a global Foster multiplier. It remains only a compatibility diagnostic for separately bundled same-parent restart and height scalars.

The same-parent geometric tail itself remains valid and Professor-checked; the error occurs only when simultaneously unresolved levels are multiplied using factor one on child-alive/nonexposed phases.

## Exact stronger coupling state

G replaces the exposed-only product by a nearest-neighbour coupled-pair phase ansatz. Let

$$
\mathcal A=\{00,11,01,10\},
$$

and assign positive edge weights

$$
q_{\alpha\beta}>0,
\qquad (\alpha,\beta)\in\mathcal A^2.
$$

The product corrector is

$$
C_Q(\sigma)=\prod_i q_{\sigma_{i-1},\sigma_i}.
$$

For every triple `(alpha,beta,gamma)`, the common-uniform update of the middle pair and the exposure-entry tilt give an exact local bulk drift

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
$$

There are 16 edge phases and 64 triples. The verifier checks the same-orientation and opposite-orientation formulas directly from the common-uniform transition law.

For the old exposed-only assignment the same-orientation triple `(01,01,01)` reduces to the positive bulk term

$$
(1-a)(s e_0-1)>0,
$$

which is the finite-phase self-loop behind the all-`01` counterexample.

## Finite no-positive-cycle criterion

Construct the directed de Bruijn graph with vertices `(alpha,beta) in A^2` and edges

$$
(\alpha,\beta)\to(\beta,\gamma)
$$

weighted by `G_Q(alpha,beta,gamma)`.

For a nearest-neighbour product corrector, uniform all-height control of the **interior** bulk is equivalent to absence of a positive spatial cycle. Equivalently, there must exist a potential `psi` on the 16 edge phases such that

$$
\boxed{
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma)
}
$$

for all 64 triples. Summation then telescopes, leaving only finite endpoint terms. Conversely a positive directed cycle can be repeated to create positive drift linear in stack height, which no fixed boundary gain can absorb.

I accept this as an exact reduction for the nearest-neighbour product/coboundary class. It does **not** prove that feasible `Q,psi` exist. Right-boundary height removal, left boundary, trail insertion, and suffix trimming also give finitely many boundary inequalities that must be checked for a complete Foster theorem.

## Relation to F's mode-resolved signed work

This correction does not invalidate F's independent regenerated-mass theorem

$$
|Br_0-c|Z<\frac23
$$

or the mode-resolved `L^1(w)` programme. It does remove the scalar `(FL)` premise as a theorem.

F is already instructed not to silently assume more than G proves. Its Assignment 009 should continue: identify the signed mass/reset modes and the correct `L^1(w)` operator. Any eventual combination now needs a **valid phase-resolved coupling Foster corrector**, not Assignment 003's exposed-only product.

G's 16-phase coupling state and F's mass-relaxation/reset state solve different closure problems. If G's finite phase inequalities are feasible, F may still need additional temporal mode coordinates on the signed side.

## Ruling

The programme narrows again.

- Assignment 003's global product Foster lift is **refuted**.
- The same-parent geometric tail and height minorant survive separately.
- The `16/21` number is downgraded permanently to a scalar stress diagnostic.
- The coupling-side all-height problem is now an explicit finite feasibility problem for 16 edge phases / 64 bulk inequalities plus finite boundary inequalities.
- Student F remains in flight on Assignment 009.
- Student G is routed to solve or refute this finite phase Foster feasibility problem throughout the residual chamber, with near-East as the primary stress regime.
