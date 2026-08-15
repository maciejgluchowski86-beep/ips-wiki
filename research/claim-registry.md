# Project claim registry

This file is the mechanical status index for project-specific mathematical claims that appear on `main` outside the scratch research workspace.

A manuscript or note being present on `main` does not by itself make its claims established. Before relying on a project-specific theorem, check this registry and the cited audit record.

Allowed registry statuses are:

- `claimed`: there is a project proof or serious argument, but required independent verification is incomplete;
- `verified`: the claim has completed the verification required by `CHATGPT.md` for its present use;
- `canonical`: the human principal has explicitly designated the cited project source as authoritative for this result.

A `verified` entry must cite the relevant `audit-log.md` record or other durable audit record. A `canonical` entry records the principal's explicit source-precedence decision and does not imply that Claude independently checked the proof.

## Canonical patch results

### PATCH-FACTOR-001

Status: `canonical`

Claim: conditional on the successful-interaction skeleton up to a finite horizon, the patch interaction data are independent with their consistent patch laws; equivalently, the patch factorization theorem holds.

Source: `paper/sections/representation.tex`, theorem `Patch factorization`.

Basis: the principal explicitly designated `paper/` as the correct and authoritative source for the patch construction and its proofs, superseding deprecated wiki pages that still call this result conditional.

### PATCH-REP-001

Status: `canonical`

Claim: the signed monomial Feynman--Kac representation factors over patches and yields the exact patch representation of the spin-system semigroup stated as Theorem A in the paper.

Source: `paper/sections/main-results.tex` and the proof in `paper/sections/representation.tex`.

Basis: the same principal designation of `paper/` as the canonical patch source.

## Active or later project claims

### BABP-EDGE-001

Status: `verified`

Claim: for one-dimensional BABP in the time-scaled convention with birth rate `lambda` per occupied neighbour and death rate `1` per occupied neighbour, at

$$
\lambda=\frac1{40}
$$

there exists a bounded corrector depending on the first ten sites behind the rightmost particle such that, for

$$
H(B)=R(B)+\phi(u(B)),
$$

the generator drift is uniformly bounded below by

$$
\mathcal L H(B)\ge \frac{1033}{40000000}>0.
$$

For every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge \frac{1033}{40000000}
\qquad\text{a.s.}
$$

and, by reflection,

$$
\limsup_{t\to\infty}\frac{L(B_t)}t
\le -\frac{1033}{40000000}
\qquad\text{a.s.}
$$

This is a lower-asymptotic-velocity statement. It does not assert that either ratio has a limit.

Source proof/certificate:

- `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md`;
- `research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`.

Professor check:

- `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`;
- `research/active/babp-finite-seed/meetings/003-edge-corrector-breakthrough.md`.

Independent hostile audit:

- commit `d1ef2ca`;
- `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

The audit independently rederived the generator, checked that one unresolved exterior bit suffices and no event class is missing, established the martingale bounds needed for the displayed liminf/limsup conclusion, independently decoded and checked all `2048` exact certificate inequalities, analytically reproduced the `k=1` threshold `lambda>1/3`, and independently numerically reproduced the `k=8` zero crossing `0.0346195434755...`.

Significance and historical boundary: within the audited finite-window corrector hierarchy, the `k=10` certificate gives a positive ballistic-edge bound at `lambda=0.025`, below the numerical `0.0347` boundary appearing in Sudbury's published finite-seed theorem. The accessible Sudbury record confirms the `0.0347` convergence threshold, hunted-submartingale method, and edge-speed bounds, but the full body was not accessible. Therefore the literal identification of Sudbury's computation with this exact `k=8` LP, normalization, or eight-site encoding is **not verified**. The `k=1` and `k=8` calibrations are strong mechanism-level evidence, not source-verified historical identity.

Claim boundary: this entry does **not** claim finite-seed convergence at `lambda=1/40`, does **not** claim an improvement of Sudbury's published convergence theorem, and does **not** claim existence of limiting edge speeds.

### BABP-CONV-001

Status: `claimed`

Claim: fix `lambda>0` and consider one-dimensional nearest-neighbour BABP in the same convention as `BABP-EDGE-001`. Assume there exist an integer `k>=1`, a bounded corrector

$$
\phi:\{0,1\}^k\to\mathbb R,
$$

and `v>0` such that the exact finite-window right-edge drift satisfies

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every `u in {0,1}^k` and `z in {0,1}`. Then, for every finite nonempty deterministic initial particle set `B`,

$$
\operatorname{Law}_B(B_t)\Longrightarrow\pi_q
\qquad(t\to\infty),
$$

locally on `{0,1}^Z`, where

$$
q=\frac{\lambda}{1+\lambda}
$$

and `pi_q` is Bernoulli product equilibrium.

The statewise drift hypothesis is essential to the proof as presently written. Bare liminf/limsup ballistic-edge bounds are not asserted to imply convergence.

Proof mechanism: the same corrector is placed on the two populations bordering a tagged internal vacant gap. The corrected gap width has uniformly negative drift. Exponential tilting gives uniform exponential tails for gap lifetime and maximal width; a Poisson domination of boundary displacement and a compensator sum over gap nucleations yield

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Together with stationarity of all one-dimensional weak limit points and the stationary-law classification, this excludes the empty component from every subsequential limit.

External inputs used by the Professor check:

- Jahnel--Köppl (2026), Theorem 2.5: for one-dimensional IPS satisfying their bounded-rate/bounded-update/exponentially decaying influence assumptions, every weak limit point is stationary. BABP has single-site finite-range updates and uniformly bounded site rates, so these assumptions apply for every fixed `lambda>0`.
- Martinelli--Shapira--Toninelli (2025), Corollary 2.9: every stationary law of one-dimensional BABP is a convex combination of the completely healthy/empty configuration and Bernoulli equilibrium.

Source proof:

- `research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md`, commit `f79d0fb`.

Professor check:

- `research/active/babp-finite-seed/notes/professor-corrector-to-convergence-verification.md`;
- `research/active/babp-finite-seed/meetings/004-corrector-to-convergence.md`.

Concrete corollary: combining the general bridge with verified claim `BABP-EDGE-001` gives, at

$$
\lambda=\frac1{40},
$$

local convergence from every finite nonempty deterministic initial particle set to Bernoulli equilibrium. This parameter lies below the `0.0347` finite-seed convergence range recorded in Martinelli--Shapira--Toninelli (2025), Remark 5.4.

Claim boundary: this entry does not claim convergence for every `lambda>0`; it does not claim a quantitative convergence rate; it does not extend the initial condition beyond finite nonempty deterministic sets; and it does not assert that bare asymptotic edge-velocity bounds suffice without the statewise corrector.

Audit status: this theorem is substantially stronger than `BABP-EDGE-001`, so audit `d1ef2ca` does not verify it. Two fresh independent correctness reviews are requested in:

- `research/active/babp-finite-seed/audits/002-corrector-to-convergence-request.md`;
- `research/active/babp-finite-seed/audits/003-corrector-to-convergence-request.md`.

Do not promote `BABP-CONV-001` to `verified` until both reviews have returned and the Professor has resolved any objections.