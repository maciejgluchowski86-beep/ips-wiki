# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact, the witness is larger, or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/026-dual-renewal-connected-tail-reopens-one-bounded-j-spec-block.md`, `state_narrowed: yes`.
- Student G: active on `students/student-g/assignment-010.md`, one bounded connected dual-renewal tail certificate at `P_*`.
- Student F: idle; no F016.
- No second route is authorized.

On `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the residual chamber is

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

### Route status

Meetings 019, 021, and 024 stop respectively the common-uniform zero-frequency occupation interface, the repeated-equilibrium predecessor-profile implementation, and the stationary Bellman concatenation implementation. Consultation 002 rules out global path-space TV/KL contraction of the exact trajectory kernel. Meeting 025 stops G009's singular fixed-depth short/long renewal continuation because its long reset is nonuniform in depth.

A late G checkpoint, `394b7e3`, landed after Meeting 025 because the idle ruling had not yet been relayed. Meeting 026 evaluates it as new post-stop input and reopens **one bounded exception**. This is an orchestration overlap, not disregard of the stop.

### Exact dual-renewal mechanism

For a fixed admissible duration filter `sigma`, define

$$
H_N^\sigma=\int w(u)\sigma(u)P_u^Ndu,
\qquad
Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N,
$$

where

$$
z_\sigma=\int w(u)\sigma(u)du.
$$

Then

$$
Q_N^\sigma\mathbf1=0,
\qquad
\pi_NQ_N^\sigma=0.
$$

Writing `J_N` for the centered insertion/drop map, define connected coefficients

$$
c_1=m_0,
$$

$$
c_k^\sigma
=\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1.
$$

Expanding every `H=zPi+Q`, the invariant projections are extracted **exactly** as renewal separators. The fixed-filter signed witness therefore obeys an exact scalar recurrence

$$
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1,
$$

with

$$
\lambda_k=(-1)^kz_\sigma c_k^\sigma.
$$

The witness is dominated by the canonical absolute-duration norm, so supercritical growth of `V_n` proves `rho_J>1`.

### Fixed filter and active target

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

fix

$$
\sigma(u)=1-2e^{-(4/125)u}.
$$

Then

$$
z_\sigma=\frac{114559900}{205809}.
$$

G009b reports, and the Professor independently reconstructed numerically,

$$
\sum_{k=1}^7\lambda_k\approx1.047155757329804.
$$

The first five coefficients are positive and the sixth and seventh negative, so naive positive truncation is invalid. No verifier accompanied the late checkpoint; Assignment 010 must first commit exact rational verification of the finite prefix.

Put

$$
\delta_7=\sum_{k=1}^7\lambda_k-1.
$$

The active theorem is

$$
\boxed{
\sum_{k\ge8}|\lambda_k|<\delta_7.
}
$$

This would imply `sum_k lambda_k>1`, hence a renewal singularity inside the unit disk and

$$
\boxed{\rho_J(P_*)>1.}
$$

### Why Meeting 026 treats this as genuinely new

F013/F014 failed because replacing a long segment by its invariant projection left a shifted invariant-law zero-frequency error. In the new recurrence every invariant projection is separated exactly before the connected coefficients are defined. The active operator

$$
Q_N^\sigma J_N
$$

contains no exact invariant spectral projection internally.

This does **not** make it automatically contractive: slow nonzero modes may still survive. That depth-uniform connected-tail question is precisely Assignment 010.

### Stopping rule

Do not count a larger coefficient table, optimize the filter, posit finite-dimensional mode closure, or restart tail-shift/common-coupling/Bellman searches. Assignment 010 must produce an all-depth connected-tail theorem or a structural obstruction sharper than the already known growing-mode fact. Otherwise the programme returns to Meeting 025's `no-credible-route` state.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
