# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact, the witness is larger, or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/027-terminal-high-pass-contraction-but-noniterable-connected-renewal-stops.md`, `state_narrowed: yes`.
- Student G: idle; no G011.
- Student F: idle; no F016.
- No proof architecture is currently active.

On `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the residual chamber is

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

### Operative route status

Consultation 002 / Meeting 025's **`no-credible-route`** proof-architecture assessment is again operative after Meeting 027. This is not a claim that the conjecture is false or that all conceivable approaches are impossible.

Stopped/inactive interfaces include:

- common-uniform zero-frequency disagreement occupation;
- the repeated-equilibrium predecessor-trail/profile implementation;
- global path-space TV/KL contraction of the exact trajectory kernel;
- the stationary Bellman-corrector concatenation implementation;
- G009's singular fixed-depth short/long renewal continuation;
- the fixed-filter connected dual-renewal continuation after the bounded G010 block.

### Canonical `J` status

For singleton depth `n`,

$$
J_n=\frac BgR_n=\frac gBN_n,
$$

so

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}
$$

is also the root growth rate of `R_n` and `N_n`.

`(J-SPEC)` remains open.

G009 proves a singular fixed-depth renewal theorem with base

$$
\frac{499}{341}=\frac{10}{11}+\frac{189}{341}>1,
$$

but the long channel is not uniform in depth, so this does not imply fixed-rate `rho_J>1`.

### Exact fixed-filter dual renewal retained

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

with fixed filter

$$
\sigma(u)=1-2e^{-(4/125)u},
$$

the invariant projections can be extracted exactly as renewal separators. The resulting fixed-filter witness obeys

$$
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
$$

Commit `e4452de` exactly verifies the first seven rational coefficients, with

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
$$

and

$$
\sum_{k=1}^7\lambda_k>1.
$$

The sufficient all-depth tail target

$$
\sum_{k\ge8}|\lambda_k|
<
\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1>0,
$$

remains open.

### G010 positive-frequency theorem

Assignment 010 derives the exact stationary high-pass factor

$$
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
$$

For the actual fixed `P_*` duration weight and filter, the repaired exact verifier at `ce77c9c` proves a depth-independent signed kernel bound

$$
\|\kappa\|_1\le\Theta_\sharp,
\qquad
\Theta_\sharp\approx0.8924718201406568,
$$

with exact

$$
\boxed{B\Theta_\sharp<1.}
$$

Hence a full centered insertion followed by the high-pass connected resolvent satisfies the depth-uniform oscillation contraction

$$
\boxed{
\operatorname{osc}
\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp=B\Theta_\sharp<1.
}
$$

This is genuine target-relevant mathematics, but it is not iterable through one seminorm: on a mode `L=-x`,

$$
R(x)=\frac{d+gx}{1+b+x}
$$

vanishes at the exact positive frequency

$$
x=|d|/g=1/100.
$$

The actual connected coefficient reduces exactly to the narrower filtered boundary-response pairing

$$
\boxed{
 c_{N+1}=\delta_N(R_NQ_Nf_N),
}
$$

with `f_N` the special connected orbit. This is not proved equivalent to F013/F014's unrestricted tail-shift norm.

The recentered newest-boundary block is symmetric after normalization, and the scalar recentering branch has uniform oscillation cost below `0.609`; the unresolved transmission lies in the boundary-containing component and inherited older-volume dynamics.

### Meeting 027 stop decision

G010 did not prove the connected-tail theorem or `rho_J(P_*)>1`, and did not refute the fixed witness. It did identify a sharper blocker than the old mode-growth or bare tail-shift statements.

A plausible future repair would need either:

- an **explicit complementary high-pass observable** with a proved two-component depth-uniform contraction covering the blind frequency; or
- an **orbit-specific theorem** giving summable/geometric control of the filtered boundary-response pairing.

Neither currently exists. A generic instruction to search for another norm does not clear the bounded-block continuation bar. No G011 is authorized.

Work resumes only after genuinely new principal, external, or literature input supplies a concrete mechanism of that strength or another materially different proof architecture.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
