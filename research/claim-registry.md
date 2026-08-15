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

Claim boundary: this entry does **not** claim finite-seed convergence at `lambda=1/40`, does **not** claim an improvement of Sudbury's published convergence theorem, and does **not** claim existence of limiting edge speeds. The edge-bound-to-local-convergence bridge remains an open proof-spine edge.
