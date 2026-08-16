# Group meeting 012: balanced circulation refutes the 16-phase scalar product class; test viability of the common-uniform coupling itself

Date: 2026-08-16

Professor review of:

- Student G, commit `d6f3a9d`, `students/student-g/005-16-phase-foster-feasibility.md`;
- exact verifier commit `3963d86`, `students/student-g/005-16-phase-foster-feasibility-verifier.py`;
- Meetings 010--011 and the current proof spine.

Operational correction: Student G completed Assignment 005 seconds before Meeting 011 was committed. Meeting 011 therefore incorrectly records G as still in flight. Its mathematical ruling on Student F is unaffected. A correction is appended to Meeting 011 rather than silently rewriting the historical sequence.

state_narrowed: yes

Evidence pointer: `students/student-g/005-16-phase-foster-feasibility.md`, especially Sections 2--9, and `students/student-g/005-16-phase-foster-feasibility-verifier.py`.

## Previous coupling bottleneck

Meeting 010 refuted the exposed-only independent-level Foster product but left a stronger nearest-neighbour scalar edge-product/coboundary class open. With coupled pair alphabet

$$
\mathcal A=\{00,11,01,10\},
$$

positive edge weights `q_{alpha beta}`, and

$$
C_Q(\sigma)=\prod_i q_{\sigma_{i-1},\sigma_i},
$$

the all-height bulk question reduced to the 64 local tilted drifts `G_Q(alpha,beta,gamma)` and the no-positive-cycle/coboundary condition

$$
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma).
$$

Assignment 005 asked G to solve or refute this entire class, including the possibility that boundary/height terms might complete the Foster estimate.

G refutes the class in the bulk at one strict residual point.

## Exact strict residual point

Take

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right).
$$

This is strictly residual:

$$
0<a<b,
\qquad
\frac12<c<1,
\qquad
c>a+b,
$$

and

$$
b^2=10^{-4}>2\cdot10^{-8}=2(1-c)^2.
$$

Thus the point lies in the unresolved chamber and a failure there is enough to rule out this corrector class as a proof throughout the chamber.

## Professor verification: balanced-circulation obstruction

For a triple

$$
e=(\alpha,\beta,\gamma)\in\mathcal A^3,
$$
let `p_e(z)` be the exact common-uniform probability that the middle coupled pair `beta` updates to `z`. Let

$$
\rho_e(z)\in\{0,1\}
$$

count newly created exposure edges, and write

$$
x_{\alpha\beta}=\log q_{\alpha\beta}.
$$

The exponent change of the scalar edge product under `beta -> z` is

$$
\Delta_e(z)
=
\mathbf e_{\alpha z}+\mathbf e_{z\gamma}
-\mathbf e_{\alpha\beta}-\mathbf e_{\beta\gamma}.
$$

Hence

$$
G_Q(e)
=
\sum_{z\ne\beta}p_e(z)
\left[
 s^{\rho_e(z)}e^{\langle\Delta_e(z),x\rangle}-1
\right].
$$

G gives an explicit normalized nonnegative rational circulation `mu` supported on 28 of the 64 triples. The verifier checks exactly:

1. spatial flow conservation on all 16 edge phases,
   $$
   \sum_\gamma\mu_{\alpha\beta\gamma}
   =\sum_\delta\mu_{\delta\alpha\beta};
   $$
2. zero expected exponent change in every one of the 16 `Q` coordinates,
   $$
   \sum_e\mu_e\sum_{z\ne\beta}p_e(z)\Delta_e(z)=0;
   $$
3. positive changing-update mass `C_mu` and positive exposure-entry flux `R_mu`.

The exact values are

$$
R_\mu
=
\frac{40097221742150361438903}
{4060682358517754276494700}>0,
$$

$$
C_\mu
=
\frac{10111075801610946800285497}
{812136471703550855298940000}>0.
$$

Define

$$
\theta_{e,z}
=\frac{\mu_ep_e(z)}{C_\mu}
$$

on changing outcomes. Then `theta` is a probability distribution. Weighted AM--GM gives, for every positive edge matrix `Q` and every `s>1`,

$$
\begin{aligned}
\sum_e\mu_eG_Q(e)
&=C_\mu\left[
\sum_{e,z}\theta_{e,z}
 s^{\rho_e(z)}e^{\langle\Delta_e(z),x\rangle}-1
\right]\\
&\ge
C_\mu\left[
 s^{\sum\theta_{e,z}\rho_e(z)}
 \exp\left\langle\sum\theta_{e,z}\Delta_e(z),x\right\rangle
-1\right]\\
&=
\boxed{
C_\mu\left(s^{R_\mu/C_\mu}-1\right)>0.
}
\end{aligned}
$$

This implication is exact and independent of any optimizer or floating-point search once the rational circulation is supplied.

## Why this contradicts every coboundary certificate in the class

If a potential `psi` satisfied

$$
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma)
$$

for all triples, averaging against the spatial circulation would give

$$
\sum_e\mu_eG_Q(e)\le0
$$

because the right side telescopes by flow conservation. This contradicts the strict AM--GM lower bound above.

Equivalently, every finite circulation decomposes into directed cycles, so for every positive `Q` and every `s>1` at least one directed spatial cycle has strictly positive mean bulk drift.

The obstruction is extensive in stack height. Repeating a positive cycle produces positive bulk drift linear in the number of repetitions. Any right-boundary height gain, insertion correction, left-boundary correction, terminal phase weight, or suffix-trimming term contributes only at the ends and cannot repair the class.

Therefore

$$
\boxed{
\text{the 16-phase nearest-neighbour scalar product/coboundary Foster class is refuted.}
}
$$

## Scope of the negative result

The following remain valid:

- G's same-parent geometric restart tail;
- the one-exposure resolvent and compensator;
- the separate stack-height clearing minorant;
- F's equilibrium and transient mass-mode contractions;
- the centered predecessor-trail reduction as a working reduction.

The result does **not** prove failure of matrix-product or genuinely nonlocal correctors, failure of every finite temporal coupling state, nondecay of `J_{x,r}`, or failure of the positive rates conjecture.

It does show that two successive scalar local Foster architectures have now failed for structural rather than numerical reasons: first the exposed-only product, then the complete nearest-neighbour scalar edge-product/coboundary class.

## Relation to Meeting 011 / Student F

Meeting 011 proves independently that the common-mass signed semigroup has no depth-uniform finite linear mode closure. F is now attacking profile regeneration/truncation in the `J`-compatible `L^1(w)` norm.

G's refutation strengthens the separation recorded there: there is no 16-phase scalar coupling cocycle for F to tensor with. If the common-uniform coupling remains useful, its global control must be genuinely nonlocal or noncommutative.

F's Assignment 010 does not need interruption; the principal has already relayed G's handoff to F.

## Direction decision: do not escalate local corrector dimension mechanically

The next G block should not be `32 phases`, a longer scalar context, or another finite local product ansatz. The balanced-circulation obstruction and the earlier all-`01` obstruction are enough evidence that merely enriching a commutative local credit system risks repeating the same mechanism.

Before investing in matrix-product/nonlocal correctors, decide whether the **common-uniform coupling itself is a viable global extinction mechanism near East**.

The natural diagnostic is survival versus extinction of a finite disagreement seed at the same strict near-East point (or on a small near-East interval). Local transmission is already known to be very strong and rightmost coalescence very weak there. If a finite disagreement seed survives with positive probability, then any proof route requiring eventual global coalescence/regeneration of this synchronous coupling is structurally unavailable, and the group should stop building Foster correctors for it. If the disagreement dies out almost surely, the proof must exploit a genuinely nonlocal regeneration theorem rather than the refuted local products.

## Ruling

The state narrows again.

- The entire 16-phase nearest-neighbour scalar product/coboundary Foster class is refuted at a strict residual point by an exact rational circulation certificate.
- Boundary and height corrections cannot rescue it because the obstruction is in repeatable bulk cycles.
- The same-parent renewal theorem survives.
- G is redirected away from local scalar corrector enlargement and toward a structural survival/extinction test for the common-uniform disagreement process near East.
- F continues Assignment 010 on the independent common-mass profile truncation problem.

The full trail factorization and no-exit term remain downstream audits only after `J_{x,r}->0` is actually proved.
