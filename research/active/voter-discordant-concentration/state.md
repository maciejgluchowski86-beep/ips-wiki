# Programme state

## Direction

Title: corrected sharp concentration of voter-model discordant edges on random regular graphs

Branch: `research/voter-discordant-concentration`

Workspace: `research/active/voter-discordant-concentration/`

Persistent Graduate Student D: idle; programme closed

Latest group meeting: `meetings/004-novelty-fails-and-programme-closes.md`

## Final mathematical status

`VOTER-CONC-001` is **verified mathematics but not a new project result under the standing novelty standard**.

For every finite simple `d`-regular graph with `d>=1`, not necessarily connected, every `u in (0,1)`, and every `t>=0`,

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le2\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t).
$$

Correctness basis:

- Student D proof: commit `e73fd25`, `students/student-d/002-four-walk-cancellation.md`;
- Professor reconstruction: `notes/professor-assignment-002-verification.md`;
- hostile Review A: commit `add0681`, `audits/001-genealogy-review-a.md`, `PASS`;
- hostile Review B: commit `45f960b`, `audits/002-genealogy-review-b.md`, `PASS`, explicitly independent of Review A.

The deterministic theorem yields on fixed-`d>=3` random regular graphs

$$
\operatorname{Var}_u^G(\mathcal D_{t_n}^n)
=O_{\mathbb P}((1+t_n)/n)
$$

for deterministic `t_n=o(n)`, and `O_P(t_n/n)` for deterministic `1<=t_n=o(n)`.

## Novelty correction

The novelty audit, commit `5ab5dce`, `audits/003-novelty-prior-work.md`, is negative.

Avena--Baldasso--Hazra--den Hollander--Quattropani (2024) already provide in Proposition 4.1 proof (4.2) the relevant two-edge decoupling on no cross-family interaction and in (5.5)--(5.6) the bound

$$
\mathbf P_{\nu\otimes\nu}(\tau^{e,f}\le t)
\le4\mathbf P_{\pi\otimes\pi}(\tau_{\rm meet}\le t).
$$

For Bernoulli initial opinions these ingredients immediately give

$$
\operatorname{Var}_u^G(\mathcal D_t)
\le4\mathbf P_{\pi\otimes\pi}^G(\tau_{\rm meet}\le t),
$$

and source (5.8) then gives the same asymptotic random-regular concentration consequences. The project improves the deterministic constant from `4` to `2` and supplies a cleaner quotient-genealogy proof, but these are not a new theorem-level contribution under the standing novelty standard.

## Small-time source correction

Literal source Eq. (1.9) is mathematically false for unrestricted very-small times; the counterexample

$$
t_n=n^{-3},\qquad C_n=\log n
$$

is independently verified.

Priority of that narrow correction remains unresolved because the novelty auditor could not inspect Federico Capannoli's 2025 thesis. This does not keep the programme active: even if new, the correction is too small to carry the scientific direction on opportunity-cost grounds.

## Research delta

Latest meeting `state_narrowed: yes`.

Evidence pointer: `audits/003-novelty-prior-work.md` and `meetings/004-novelty-fails-and-programme-closes.md`.

The main contribution uncertainty is resolved negatively while correctness remains established.

## Direction

`closed`.

Do not reopen to optimize constants, repackage the factor-4 corollary, or further polish the genealogy proof. A future return requires a genuinely distinct theorem not already implied by the 2024 source ingredients.
