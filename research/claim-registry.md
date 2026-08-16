# Project claim registry

This file is the mechanical status index for project-specific mathematical claims that appear on `main` outside scratch research workspaces.

Allowed mathematical statuses are `claimed`, `verified`, and principal-designated `canonical`. A `verified` claim must point to a durable independent audit record. **Mathematical verification is separate from research-contribution status.** Under the standing novelty standard in `CHATGPT.md`, correct mathematics can be verified while still not counting as a new project result.

## Canonical patch results

### PATCH-FACTOR-001

Status: `canonical`

Claim: conditional on the successful-interaction skeleton up to a finite horizon, the patch interaction data are independent with their consistent patch laws; equivalently, the patch factorization theorem holds.

Source: `paper/sections/representation.tex`, theorem `Patch factorization`.

Basis: principal designation of `paper/` as the canonical patch source.

### PATCH-REP-001

Status: `canonical`

Claim: the signed monomial Feynman--Kac representation factors over patches and yields the exact patch representation of the spin-system semigroup stated as Theorem A.

Source: `paper/sections/main-results.tex` and `paper/sections/representation.tex`.

Basis: principal designation of `paper/` as the canonical patch source.

## Verified BABP mathematics retained for reuse

### BABP-EDGE-001

Status: `verified`

Research-contribution status: **not a project result under the standing novelty standard**.

Claim: for one-dimensional BABP with rates

$$
0\to1\text{ at rate }\lambda N_x,
\qquad
1\to0\text{ at rate }N_x,
$$

at `lambda=1/40` there is a bounded ten-site edge corrector with

$$
D_{10,1/40}(u,z;\phi)\ge \frac{1033}{40000000}>0
$$

for every edge state `(u,z)`. Consequently, for every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t
\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

No existence of limiting edge speeds is asserted.

Source/certificate:

- `research/active/babp-finite-seed/students/student-b/001-threshold-and-dfp.md`;
- `research/active/babp-finite-seed/students/student-b/edge-corrector-certificate.py`.

Professor check:

- `research/active/babp-finite-seed/notes/professor-edge-corrector-verification.md`.

Independent hostile audit:

- commit `d1ef2ca`;
- `research/active/babp-finite-seed/audits/001-edge-corrector-audit.md`.

Novelty status: Sudbury (1999), Section 3, already gives the same arbitrary-window robust submartingale mechanism and Lemma 7 extends successful constructions to larger windows. The ten-site witness is a correct larger-window instance, not a new project result.

### BABP-CONV-001

Status: `verified`

Research-contribution status: **not a new project theorem; verified self-contained formulation/proof of a classical implication**.

Claim: if for fixed `lambda>0` there exist `k`, bounded `phi`, and `v>0` such that

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every edge state `(u,z)`, then every finite nonempty deterministic initial set converges locally to Bernoulli equilibrium `pi_{lambda/(1+lambda)}`.

Stable proof:

- `research/results/babp-finite-seed-convergence.md`.

Independent correctness reviews:

- commit `abb05f6`, `research/active/babp-finite-seed/audits/002-convergence-review-a.md`;
- commit `1aeb5a5`, `research/active/babp-finite-seed/audits/002-convergence-review-b.md`.

Historical status: Sudbury (1999) states that the Neuhauser--Sudbury finite-seed stationary-state argument proceeds unchanged once the suitable finite-window submartingale is available. No novelty claim is made for this implication.

## Verified voter-discordance mathematics retained for reuse

### VOTER-CONC-001

Status: `verified`

Research-contribution status: **not a new project result under the standing novelty standard**.

Claim: let `G` be a finite simple `d`-regular graph with `d>=1`, not necessarily connected, with `n` vertices. Start the rate-one continuous-time voter model from i.i.d. Bernoulli(`u`) opinions, `u in (0,1)`, and let `Dcal_t` be the fraction of discordant edges. If `pi` is uniform on vertices and `tau_meet` is the meeting time of two independent rate-one continuous-time simple random walks started from `pi tensor pi`, then for every `t>=0`,

$$
\boxed{
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
}
$$

For uniformly random simple `d`-regular graphs with fixed `d>=3`, Avena--Baldasso--Hazra--den Hollander--Quattropani (2024), equation (5.8), together with the high-probability `Theta(n)` stationary mean meeting time and spectral-gap input used there, gives for every deterministic `t_n=o(n)`

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}\left(\frac{1+t_n}{n}\right),
$$

hence concentration at scale `C_n sqrt((1+t_n)/n)` for every `C_n->infinity`. For deterministic `1<=t_n=o(n)`,

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)=O_{\mathbb P}(t_n/n),
$$

and the source scale `C_n sqrt(t_n/n)` follows.

The literal displayed source Eq. (1.9) is false when its quantifiers permit unrestricted very-small times: the Bernoulli initial condition has `n^{-1/2}` fluctuations and `t_n=n^{-3}`, `C_n=log n` is an explicit counterexample. Priority of this narrow source correction is unresolved; no complete classification of subunit-time sequences is claimed.

Source proof:

- commit `e73fd25`;
- `research/active/voter-discordant-concentration/students/student-d/002-four-walk-cancellation.md`.

Professor reconstruction:

- `research/active/voter-discordant-concentration/notes/professor-assignment-002-verification.md`.

Independent correctness reviews:

- Review A: commit `add0681`, `research/active/voter-discordant-concentration/audits/001-genealogy-review-a.md`, `PASS`;
- Review B: commit `45f960b`, `research/active/voter-discordant-concentration/audits/002-genealogy-review-b.md`, `PASS`, explicitly independent of Review A.

Closest-prior-work / novelty audit:

- commit `5ab5dce`;
- `research/active/voter-discordant-concentration/audits/003-novelty-prior-work.md`.

Fatal comparison: Avena et al. (2024), Proposition 4.1 proof (4.2), already gives the relevant two-edge no-cross-interaction decoupling, while (5.5)--(5.6) gives

$$
\mathbf P_{\nu\otimes\nu}(\tau^{e,f}\le t)
\le4\mathbf P_{\pi\otimes\pi}(\tau_{\rm meet}\le t).
$$

For Bernoulli initial data these ingredients immediately imply

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t),
$$

which, combined with source (5.8), already yields the same random-regular asymptotic concentration conclusions. The project improves the constant `4` to `2` and supplies a cleaner genealogy-conditioned quotient-cut proof, but this does not constitute a new theorem-level contribution under the standing novelty standard.

Claim boundary: no uniform-in-time process-supremum concentration theorem is claimed.
