# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow.

## Standing novelty standard

A quantitatively improved instance of an already-established arbitrary-size method does not count as a new project result merely because the computation is exact or the numerical constant is better. Larger windows, orders, degrees, truncation levels, or analogous complexity parameters are useful diagnostics/certificates but do not justify a contribution claim by themselves.

A qualifying project result must add structural mathematics: for example a theorem about a method across a genuine parameter regime, a qualitative mechanism, a structural success/failure theorem, or a proof/refutation of the target open problem.

## Active scientific direction

**Residual positive-rates conjecture / noisy East for simple one-sided one-dimensional IPS.**

- Branch: `research/noisy-east-positive-rates`.
- Workspace: `research/active/noisy-east-positive-rates/`.
- Positive target: prove ergodicity in the remaining noisy-East region, ultimately completing the simple-IPS positive-rates conjecture.
- Active student: persistent Graduate Student C.
- Latest meeting on the research branch: `research/active/noisy-east-positive-rates/meetings/001-two-site-wall-review.md`, `state_narrowed: yes`.

### First wall test

Student C's exact two-site calculation is negative near East. On the genuine strict residual path

$$
r_{11}=0,\qquad
r_{10}=1-\varepsilon^2,\qquad
r_{01}=\frac\varepsilon2,\qquad
r_{00}=\varepsilon,
$$

the two-site killed-excursion Perron factor and one-attack crossing factor satisfy

$$
\rho_2(\varepsilon)\to1,
\qquad
F_2(\varepsilon)\to1.
$$

The Professor independently rebuilt the chain and verified the deterministic East-limit crossing mechanism on the research branch in `notes/professor-wall-test-verification.md`.

A targeted length-three diagnostic on the same path prevents an immediate structural kill of all finite walls. The full 24-state chain, maximized over all eight fully agreed three-site words and both exterior disagreement orientations, has

$$
R_3^{\rm adv}(\varepsilon)\to\frac9{10}.
$$

This is diagnostic only, not a project result.

### Current structural question

Graduate Student C assignment 002 must characterize the exact length-three adversarial factor over the **entire normalized residual region and every asymptotic approach to the East boundary**. The relevant question is whether

$$
\sup_{\bar r\in\partial_E R}
\limsup_{\substack{r\to\bar r\\r\in R}}
R_3^{\rm adv}(r)<1.
$$

The exact residual set `R` and its East boundary must first be recovered from the 2025/2026 source reductions.

### Pre-committed finite-wall stop rule

If Student C finds any genuine residual sequence approaching the East boundary with

$$
R_3^{\rm adv}(r_n)\to1,
$$

the finite-wall route is abandoned for this programme. **Do not move to length four.** This is an opportunity-cost ruling, not a theorem that every longer block fails.

If a uniform length-three gap exists, continuation still requires a rigorous block-renewal/concatenation theorem that survives dynamically changing exterior states, repeated attacks, overlap, and dependence. If the frozen-exterior diagnostic cannot be upgraded to such a domination without an uncontrolled stronger quantity, the finite-wall route is also abandoned rather than enlarged.

## Most recently closed programme: BABP finite seed

BABP closed without a new project result under the standing novelty standard.

Retained verified mathematics:

- `BABP-EDGE-001`: exact ten-site `lambda=1/40` certificate, audit `d1ef2ca`;
- `BABP-CONV-001`: verified self-contained corrector-to-convergence proof, reviews `abb05f6` and `1aeb5a5`.

Neither counts as a project contribution because Sudbury's finite-window method is already defined for arbitrary window size and the convergence implication is classical. Student B's dormant invariant-front reduction remains useful only if a genuinely structural all-parameter idea appears.

Do not reopen BABP merely to enlarge finite windows or improve numerical thresholds.

## Wiki freeze

The principal controls the freeze decision. Professor recommendation remains **keep the live wiki frozen**. No BABP `proved here` update is warranted, and the noisy-East programme has no verified new theorem yet.

## Closed programmes and routes

Closed programmes not to be retried by renaming include:

- quadratic-Hessian;
- Fresnel integrability;
- Navier--Stokes stochastic cascade;
- Strong-KPP uniqueness;
- supercritical dissipative SQG;
- long-maturity marked branching;
- Gaussian bridge coarsening;
- 1D hard FA-1f finite-seed programme based on centered-transform / unnormalized patch-transfer routes;
- 1D BABP finite-seed programme based on finite-window submartingales and the unresolved invariant-front continuation.

Broader mathematical problems may remain open. What is closed is the recorded programme/mechanism at its present expected value.