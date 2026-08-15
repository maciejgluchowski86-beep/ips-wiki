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

Status: `claimed`

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

Consequently the right edge has strictly positive asymptotic outward speed and, by reflection, the left edge has strictly negative asymptotic outward speed.

Source proof/certificate:

- `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md`;
- `research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`.

Professor check:

- `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`;
- `research/active/babp-finite-seed/meetings/003-edge-corrector-breakthrough.md`.

Significance: the same finite-window edge-corrector hierarchy has threshold `1/3` at window size one and numerical zero-drift threshold `0.0346195435...` at window size eight, calibrating to the historical `0.0347` edge-speed/submartingale cutoff in Sudbury's published finite-seed theorem. Since `1/40=0.025<0.0347`, the ten-site certificate strictly penetrates that historical finite-window edge-speed cutoff.

Claim boundary: this entry does **not** claim finite-seed convergence at `lambda=1/40`. The edge-speed-to-local-convergence bridge remains an open proof-spine edge.

Pending independent audit: `research/active/babp-finite-seed/audits/001-edge-corrector-request.md`. Do not promote to `verified` until the resulting durable audit supports it.
