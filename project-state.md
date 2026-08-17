# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact, the witness is larger, or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/030-signed-boundary-transmission-is-final-g010-blocker-no-restart.md`, `state_narrowed: yes`.
- Student G: idle; no G011.
- Student F: idle; no F016.
- No proof architecture is active.

Consultation 002 / Meeting 025's **`no-credible-route`** assessment is again operative. Assignment 010 is complete unresolved after substantive work.

### Exact dual-renewal status

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

with fixed filter

$$
\sigma(u)=1-2e^{-(4/125)u},
$$

the invariant projections are extracted exactly as renewal separators and the fixed signed witness obeys

$$
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
$$

Commit `e4452de` exactly verifies the first seven rational coefficients with

$$
\sum_{k=1}^7\lambda_k>1,
$$

but the sufficient all-depth tail theorem

$$
\sum_{k\ge8}|\lambda_k|<\delta_7,
\qquad
\delta_7:=\sum_{k=1}^7\lambda_k-1,
$$

remains open. Therefore `(J-SPEC)` and `rho_J(P_*)>1` remain open.

### Accepted G010 structure

The fixed-filter connected route now has the following exact structure.

1. The stationary marginal-discrepancy / bare tail-shift functional can be eliminated exactly from the connected coefficient, so this route is not presently equivalent to F013/F014's unrestricted tail-shift problem.
2. The terminal high-pass factor admits the complementary split
   $$
   R_N=m_0I+g_0(I-K_N),
   $$
   with strict depth-uniform one-step bounds on both channels, but no frame estimate making them iterable.
3. Recentring the fresh insertion with `X_N=Y_N+9/10000` gives
   $$
   A_NM_{X_N}
   =M_{X_N}(A_{N-1}+11/10)-g_0B M_{\eta_N}P_{N-1}.
   $$
   Thus the only failure of exact fresh frequency shift is the old right-boundary transmission term.
4. After exact regrouping `Y=X-9/10000`, the fresh shifted and scalar branches are individually subcritical:
   $$
   BZ_{\omega+11/10}=\frac{1065933}{1068400}<1,
   \qquad
   \frac9{10000}Z=\frac{1719}{3100}<1.
   $$
   Verifier `adf50d9` checks these and the other late scalar inequalities exactly.

The sole uncontrolled branch in this decomposition is the signed boundary-transmission Volterra operator

$$
\boxed{
\begin{aligned}
\mathcal V_N f
:={}&B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}\\
&\hspace{26mm}\times
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt,
\end{aligned}
}
$$

with `h(t)=w_*(t)\sigma(t)`, `r=11/10`, and `epsilon=9/10000`. Both the inner coefficient and the outer filter kernel change sign. No depth-uniform estimate retaining this two-time cancellation on the actual connected orbit was proved.

### Reversible reference results retained

At the corrected reversible reference point, with the actual `P_*` duration weight and filter frozen externally, G proves a dimension-free fresh-insertion Sobolev gain and reduces the full frozen-reference transfer norm exactly to a single killed self-adjoint channel family by a left-slice direct sum. These are genuine structural results but do not transport automatically through the actual nonreversible boundary defect.

### Raw coefficient route remains closed

Commit `d9c477e` proves that adding a multiplicative connected-component weight to the 010a degree-weighted `ell^1` norm still cannot make the actual nonconstant raw coefficient semigroup uniformly nonexpansive. Thus filter/resolvent-level cancellation remains load-bearing.

### Restart bar

A future restart of this branch requires **new input specifically controlling the signed boundary-transmission operator above on the actual connected orbit**, strongly enough to imply summable/geometric renewal coefficients, or a materially different proof architecture.

Another norm search, reversible comparison, filter optimization, finite coefficient table, bare tail-shift route, common-coupling occupation route, or generic Bellman/joint-corrector search does not clear the bar.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
