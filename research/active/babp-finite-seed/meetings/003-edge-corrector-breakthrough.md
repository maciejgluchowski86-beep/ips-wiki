# Group meeting 003: edge-corrector breakthrough

Date: 2026-08-15

Professor review of Graduate Student B assignment 001 and Graduate Student A opportunity-cost reconnaissance.

state_narrowed: yes

Evidence pointer: `students/student-b/001-threshold-and-dfp.md`, `students/student-b/edge-corrector-certificate.py`, `notes/professor-edge-corrector-verification.md`, and later independent audit `audits/001-edge-corrector-audit.md`.

## Decision at the meeting

Student B derived the finite-window BABP edge-corrector problem, recovered the `lambda>1/3` one-site boundary, numerically found the eight-site crossing near `0.0346195435`, and supplied an exact rational ten-site certificate at `lambda=1/40` with minimum statewise drift

$$
\frac{1033}{40000000}>0.
$$

The Professor independently rederived the generator and LP calibration. The programme was continued and committed because this gave a concrete small-parameter handle.

Independent audit `d1ef2ca` subsequently verified `BABP-EDGE-001` and corrected the theorem boundary: the certificate gives

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le-v
\quad\text{a.s.},
$$

not existence of limiting speeds, and the edge certificate alone did not yet prove finite-seed convergence.

## Full-text historical correction after Meeting 006

The original Meeting 003 record also said that literal identity with Sudbury's internal `k=8` construction was unverified. That statement is now obsolete because the principal later obtained the full Sudbury (1999) paper.

The identification is source-verified. Sudbury Section 3 uses exactly the same finite-window robust submartingale framework: after reflection his `m` is the project `k`, his `m`-block is `u`, his single end-value is `z`, his correction vector is `phi`, and his local corrected gain is the project drift `D_{k,lambda}`. His Maxwell's-demon formulation and Lemma 5 require one correction vector to work for every state-dependent assignment of the one-bit exterior value, which is equivalent to requiring both `z=0,1` inequalities in every state. Table 2 gives `m=8`, `lambda_m=0.0347` and explicitly describes the listed values as trial-and-error values rather than exact critical parameters. Lemma 7 gives free extension to every larger window.

Thus the finite-window mechanism was not discovered by this project. The enduring verified Meeting 003 contribution is the exact rational `k=10`, `lambda=1/40` certificate and its audited drift/ballistic consequences. The project eight-site value `0.0346195434755...` is a numerical refinement of Sudbury's own eight-site boundary.

## Direction

`continue`.

Meeting 006 contains the current novelty/provenance assessment and supersedes the earlier incomplete-source language.