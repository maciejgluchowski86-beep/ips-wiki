# Audit log

## 2026-08-15 — programme initialization

The Professor closed the preceding FA-1f finite-seed programme after Group Meeting 002 and selected BABP finite-seed convergence as a genuinely new scientific direction.

Target: prove convergence of one-dimensional BABP from every finite nonempty particle set for all `lambda>0`, removing the remaining classical small-parameter gap.

Selection evidence inspected directly:

- canonical patch paper `paper/sections/applications.tex` and `paper/sections/discussion.tex`;
- Martinelli--Shapira--Toninelli (2025), Section 5, including Theorem 5.2, self-duality, quasi-duality, all-parameter finite-seed linear growth, and Remark 5.4 recording the `lambda>0.0347` convergence range;
- Sudbury (1999) bibliographic/theorem-level record of the `0.0347` improvement.

Graduate Student B was assigned the BABP obstruction audit. Graduate Student A concurrently performed a bounded opportunity-cost scan.

## 2026-08-15 — Group Meeting 003: edge-corrector breakthrough

Student B's decisive output:

- `students/student-b/001-threshold-and-dfp.md`;
- `students/student-b/edge-corrector-certificate.py`.

Student B derived the finite-window right-edge corrector problem, recovered `lambda>1/3` at `k=1`, numerically obtained the `k=8` crossing near `0.0346195435`, and supplied an exact rational certificate at `k=10`, `lambda=1/40` with minimum drift `1033/40000000>0`.

The Professor independently checked the generator, the liminf/limsup ballistic consequence, the `k=1` algebra, and a separate `k=8`/`k=10` LP implementation.

Meeting 003 recorded `state_narrowed: yes`, committed to BABP, and requested a fresh hostile audit.

## 2026-08-15 — Independent audit 001 completed

Audit:

- commit `d1ef2ca`;
- `audits/001-edge-corrector-audit.md`.

The auditor independently rederived the edge generator, checked all `2048` exact certificate inequalities, reconstructed `k=8`, and verified the martingale bounds. `BABP-EDGE-001` was promoted to `verified` with the precise conclusion

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

for every finite nonempty initial configuration.

The audit corrected three overstatements: no speed-limit existence is proved; literal historical identity with Sudbury's exact `k=8` computation is unverified; and the edge certificate alone does not improve Sudbury's convergence theorem.

## 2026-08-15 — Group Meeting 004: corrector-to-convergence bridge

Student B committed:

- commit `f79d0fb`;
- `students/student-b/002-edge-speed-to-convergence.md`.

The key new distinction is that the theorem does not follow from the outer liminf/limsup bounds alone. It follows from the stronger statewise corrector hypothesis

$$
D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for every finite-window edge state.

Student B applies the same corrector to the two particle populations bordering each internal vacant gap. The Professor independently reconstructed the load-bearing argument in `notes/professor-corrector-to-convergence-verification.md` and accepted the following steps for claimed status:

- internal gaps are nucleated at width one;
- positive gaps do not split, and distinct positive gaps cannot merge because the last separating particle has two vacant neighbours and zero death rate;
- the corrected tagged-gap width has drift at most `-2v` until closure;
- exponential tilting gives uniform exponential tails for gap lifetime and maximal width;
- gap-boundary displacement is dominated by a Poisson process of rate `2(1+lambda)`;
- a compensator/strong-Markov sum over all space-time gap nucleations is finite and gives a genuine late-time uniform bound;
- combining the internal-gap bound with the audited outer ballistic bounds yields

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM};
$$

- no particle-number growth theorem is used;
- the deterministic initial set is only required to be finite and nonempty.

The Professor also checked the external theorem interface using current primary sources:

- Jahnel--Köppl (2026), Theorem 2.5, gives stationarity of all weak limit points for one-dimensional IPS with bounded update diameter, bounded site rates, and exponentially decaying influence; BABP satisfies these conditions by single-site nearest-neighbour updates and uniformly bounded site rates;
- Martinelli--Shapira--Toninelli (2025), Corollary 2.9, classifies every stationary one-dimensional BABP law as a convex combination of the empty configuration and Bernoulli equilibrium.

The empty-window estimate forces the empty-mixture coefficient to vanish, giving local convergence.

New claim `BABP-CONV-001` was entered in `research/claim-registry.md` with status `claimed`:

> a uniformly positive statewise finite-window BABP edge corrector implies finite-seed local convergence.

Concrete claimed corollary from verified `BABP-EDGE-001`:

> at `lambda=1/40`, BABP from every finite nonempty deterministic initial set converges locally to Bernoulli equilibrium.

Martinelli--Shapira--Toninelli (2025), Remark 5.4, records the published finite-seed range only above `0.0347`, so the corollary would extend the recorded range if independently verified.

Meeting 004:

- path: `meetings/004-corrector-to-convergence.md`;
- `state_narrowed: yes`;
- direction: `continue`.

Because this theorem is substantially stronger than the audited edge claim, audit `d1ef2ca` does not cover it. The Professor requested two fresh independent correctness reviews:

- `audits/002-corrector-to-convergence-request.md`: proof-internal hostile reconstruction;
- `audits/003-corrector-to-convergence-request.md`: independent proof attack plus primary-source theorem-interface audit.

Graduate Student B is temporarily idle while both auditors work. If the theorem survives, the next development edge is to construct a positive statewise finite-window corrector for every `lambda>0`, for example by proving the finite-window thresholds tend to zero.