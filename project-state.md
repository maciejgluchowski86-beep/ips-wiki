# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact, the witness is larger, or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/028-boundary-resolvent-elimination-sharpens-residual-object-but-does-not-reopen.md`, `state_narrowed: yes`.
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

Consultation 002 / Meeting 025's **`no-credible-route`** proof-architecture assessment remains operative after Meetings 027--028. This is not a claim that the conjecture is false or that all conceivable approaches are impossible.

Stopped/inactive interfaces include common-uniform zero-frequency occupation, the repeated-equilibrium predecessor-trail/profile implementation, global path-space TV/KL contraction, the stationary Bellman-corrector concatenation implementation, G009's singular fixed-depth renewal continuation, and the fixed-filter connected dual-renewal continuation after bounded G010.

Operational overlap: G's `75d0e8a` landed after Meeting 027 because the idle ruling had not yet been relayed. Meeting 028 treats it as an orchestration overlap, not student disregard of the stop. The checkpoint is retained but does not reopen work.

### Canonical `J` and exact dual renewal

For singleton depth `n`,

$$
J_n=\frac BgR_n=\frac gBN_n,
$$

so

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}
$$

is also the root growth rate of `R_n` and `N_n`. `(J-SPEC)` remains open.

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

with fixed filter

$$
\sigma(u)=1-2e^{-(4/125)u},
$$

the invariant projections can be extracted exactly as renewal separators. The fixed signed witness obeys

$$
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
$$

Commit `e4452de` exactly verifies the first seven rational coefficients, with

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
\qquad
\sum_{k=1}^7\lambda_k>1.
$$

The sufficient tail target

$$
\sum_{k\ge8}|\lambda_k|
<
\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1>0,
$$

remains open.

### G010 high-pass theorem

Assignment 010 derives

$$
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
$$

For the actual fixed `P_*` duration weight and filter, repaired verifier `ce77c9c` proves

$$
\|\kappa\|_1\le\Theta_\sharp,
\qquad
\Theta_\sharp\approx0.8924718201406568,
$$

with exact

$$
B\Theta_\sharp<1.
$$

Hence

$$
\operatorname{osc}\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp=B\Theta_\sharp<1.
$$

This is a genuine depth-uniform sign-sensitive contraction, but the multiplier

$$
R(x)=\frac{d+gx}{1+b+x}
$$

vanishes at the exact positive frequency

$$
x=|d|/g=1/100,
$$

so the one-high-pass seminorm cannot be generically inverted.

### Exact boundary-resolvent elimination

G010 first reduced the connected coefficient to a filtered boundary-response pairing. Late checkpoint `75d0e8a`, accepted in Meeting 028, eliminates the marginal-discrepancy functional entirely.

Let

$$
q_N=Q_Nf_N,
\qquad
f_N=Y_NQ_{N-1}f_{N-1},
$$

$$
r=1+b,
\qquad
S_N=(rI-L_N)^{-1},
\qquad
D_N=(I-L_N)S_N.
$$

Then exactly

$$
\boxed{
 c_{N+1}
 =A_N\!\left[
 \frac dr q_N
 +\left(g-\frac dr\right)B
 D_NP_NS_Nq_N
 \right].
}
$$

At `P_*`, with `d/r=-epsilon`, `epsilon=9/10000`, and `g_0=g+epsilon`,

$$
\boxed{
 c_{N+1}=A_N(\mathfrak B_Nq_N),
}
$$

where

$$
\boxed{
\mathfrak B_N
=-\varepsilon I
+g_0B(I-L_N)(rI-L_N)^{-1}
P_N(rI-L_N)^{-1}.
}
$$

Thus bare tail-shift TV is not logically required for the connected coefficient. Any future equivalence with the stopped F013/F014 tail-shift object would need new mathematics that survives this elimination.

The elementary estimate in `75d0e8a` gives no depth decay and is far too crude for the renewal tail. The sharp residual target is summable/geometric control of

$$
A_N(\mathfrak B_Nq_N)
$$

along the actual recursion

$$
q_N=Q_N(Y_Nq_{N-1}).
$$

### Restart bar

Meeting 028 does **not** reopen the branch. A future restart requires either:

- an explicit complementary high-pass observable/seminorm with a proved two-component depth-uniform contraction covering the blind frequency; or
- an orbit-specific theorem giving summable/geometric control of `A_N(\mathfrak B_Nq_N)`.

The exact elimination alone is a reformulation/sharpening, not such a theorem. A generic instruction to prove decay of the new expression, search for another norm, optimize the filter, or compute longer coefficients does not clear the bar.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
