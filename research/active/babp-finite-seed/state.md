# Programme state

## Direction

Title: 1D BABP from a finite seed

Branch: `research/babp-finite-seed`

Professor lineage: persistent ChatGPT Professor

Graduate Student B: temporarily idle pending theorem audits

Graduate Student A: idle after bounded opportunity-cost reconnaissance

Independent audit 001: completed, `audits/001-edge-corrector-audit.md`, commit `d1ef2ca`

Independent audits 002 and 003: requested for `BABP-CONV-001`

Workspace: `research/active/babp-finite-seed/`

Latest group meeting: `meetings/004-corrector-to-convergence.md`

## Target

For every `lambda>0`, prove local convergence of one-dimensional BABP started from every finite nonempty particle set to Bernoulli equilibrium of density

$$
q=\frac{\lambda}{1+\lambda}.
$$

The programme is committed.

## Current mathematical position

There are now two distinct project claims.

### Verified: `BABP-EDGE-001`

At

$$
\lambda=\frac1{40},\qquad k=10,
$$

there is a bounded rational right-edge corrector with exact uniform drift

$$
\frac{1033}{40000000}>0.
$$

For every finite nonempty initial set,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t
\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

This claim was independently verified in audit `d1ef2ca`. It does not assert existence of limiting speeds.

### Claimed: `BABP-CONV-001`

Student B assignment 002 and the Professor's independent reconstruction establish the following candidate theorem.

For fixed `lambda>0`, suppose there exist `k`, a bounded corrector `phi`, and `v>0` such that the exact finite-window right-edge drift satisfies

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every edge state `(u,z)`. Then one-dimensional BABP from every finite nonempty deterministic initial set converges locally to Bernoulli equilibrium.

The proof uses the statewise corrector, not merely the outer liminf/limsup conclusion. Applying the same corrector to the two populations bordering every internal vacant gap gives uniformly negative corrected-gap drift, exponential gap lifetime/width tails, and after a displacement estimate plus compensator summation,

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

This rules out the empty component in every stationary subsequential limit.

Combining this claimed bridge with verified `BABP-EDGE-001` yields the concrete claimed theorem:

> BABP at `lambda=1/40` started from every finite nonempty deterministic set converges locally to Bernoulli equilibrium.

The 2025 progress paper records finite-seed convergence only above `0.0347`, so this would extend the published range if the proof survives independent review.

Status: **claimed**, pending two fresh hostile audits. Audit `d1ef2ca` covers only `BABP-EDGE-001` and is not sufficient for this stronger theorem.

## External theorem interface

The Professor checked the two external ingredients used by the bridge.

- Jahnel--Köppl (2026), Theorem 2.5: in one dimension every weak limit point is stationary for IPS satisfying bounded site-rate, bounded update-diameter, and exponentially decaying influence assumptions. BABP has single-site finite-range updates and uniformly bounded site rates, so the theorem applies for every fixed `lambda>0`.
- Martinelli--Shapira--Toninelli (2025), Corollary 2.9: every stationary law of one-dimensional BABP is a convex combination of the empty configuration and Bernoulli equilibrium.

Audit 003 will check these source interfaces independently.

## Main proof mechanism

The active object is the **statewise finite-window edge corrector**.

For finite nonempty `B`, with right edge `R`, first `k` bits `u` behind it and exterior bit `z`, define

$$
H(B)=R(B)+\phi(u(B)).
$$

The exact generator drift is

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda[1+\phi(T_+u)-\phi(u)]\\
&+u_1[-1+\phi(T_-^zu)-\phi(u)]\\
&+\sum_{j=1}^k n_j^z(u)[\lambda(1-u_j)+u_j]
[\phi(u^{(j)})-\phi(u)].
\end{aligned}
$$

Meeting 004 found that the same local inequality controls internal-gap persistence. That is the bridge to local nonescape.

## Proof spine

Path: `proof-spine.md`.

Current first unresolved issue: **independent correctness of E4 / `BABP-CONV-001`**.

If both audits accept the theorem, the first development bottleneck becomes E5: prove that every `lambda>0` admits some finite-window statewise corrector with uniform positive drift, e.g. by proving the finite-window threshold tends to zero.

## Historical provenance

The accessible Sudbury (1999) record confirms the published `0.0347` finite-seed convergence threshold, submartingale method, and edge-speed bounds. The full body remains unavailable. Literal identity of Sudbury's calculation with the present `k=8` LP is unverified and is not needed for either project claim.

## Opportunity cost

The residual simple positive-rates/noisy-East problem remains the strongest reserve. BABP remains preferred because it has now produced one verified nontrivial edge result and one complete claimed convergence theorem below the recorded published range.

## Current work

Use both in-flight session slots for independent audits:

- `audits/002-corrector-to-convergence-request.md`: proof-internal hostile reconstruction;
- `audits/003-corrector-to-convergence-request.md`: independent proof attack plus primary-source theorem-interface audit.

Graduate Student B is paused until the audits return. This prevents building E5 on a theorem whose exact hypothesis may still need repair.

## Research delta

Latest meeting `state_narrowed`: yes

Evidence pointer: `students/student-b/002-edge-speed-to-convergence.md`, `notes/professor-corrector-to-convergence-verification.md`, and `meetings/004-corrector-to-convergence.md`.

Consecutive no-narrowing meetings: 0

Stagnation consultation: none.

## Direction

`continue`.

The project now has a claimed theorem-level improvement, but its status remains deliberately below `verified` until two independent reviews return.