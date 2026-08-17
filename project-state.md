# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because the computation is exact, the witness is larger, or the constant is better. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed until changed or stopped by the principal: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/029-fresh-insertion-sobolev-gain-narrows-route-but-current-generation-may-finish.md`, `state_narrowed: yes`.
- Student G: formally idle; no G011. One response was already generating before the idle ruling reached the session. Do not forcibly interrupt it; do not prompt again after it returns.
- Student F: idle; no F016.
- No proof architecture is formally active.

Consultation 002 / Meeting 025's **`no-credible-route`** assessment remains operative unless the already-running G artifact supplies the explicit actual-orbit theorem required by Meetings 028--029.

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

remains open.

### Accepted G010 positive-frequency mathematics

The terminal high-pass factor

$$
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}
$$

satisfies the exact depth-uniform sandwiched contraction from repaired verifier `ce77c9c`:

$$
\operatorname{osc}\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp<1.
$$

Late checkpoint `75d0e8a` eliminates the old marginal-discrepancy/tail-shift functional from the connected coefficient and writes it as an explicit boundary-resolvent expectation on the actual connected orbit.

The later corrected complementary-channel checkpoint gives

$$
R_N=m_0I+g_0(I-K_N),
\qquad K_N=(1+b)((1+b)I-L_N)^{-1},
$$

so the old positive-frequency zero is cancellation between two explicit channels, not a zero of the genuine high-pass channel. Each channel has a depth-uniform one-step bound, and after one insertion their channelwise triangle estimate is strictly below one. This is not yet iterable because no frame/reverse estimate controls the next raw connected input.

Recentring the fresh coordinate gives the exact intertwining

$$
A_NM_{X_N}
=
M_{X_N}(A_{N-1}+1+b)
-g_0B M_{\eta_N}P_{N-1},
$$

isolating the sole failure of exact fresh frequency shift as the old-boundary transmission term. The old boundary projection is a small non-orthogonal tilt in product-centered coordinates, with magnitude below `1/300`.

### New reversible fresh-insertion Sobolev theorem

At the corrected reversible reference point

$$
P_0=(1/10000,1/10,999/1000),
$$

using the **actual `P_*` duration weight and filter frozen externally**, define `A_{0,N}=-L_{0,N}` and

$$
q(x)=Z_{\omega+x}-2Z_{\omega+\tau+x}.
$$

Verifier `56d47cb` exactly proves

$$
|xq(x)|<1\qquad(x>0).
$$

For the fresh product-centered insertion,

$$
M_X^*A_{0,N}^{-1}M_X
\le
\frac{998001}{11000000}I,
$$

and hence

$$
\|A_{0,N}^{1/2}\widetilde Q_{0,N}^\sigma(Y_Nf)\|_2
\le
\left(
\sqrt{\frac{998001}{11000000}}
+
\frac9{400}
\right)\|f\|_2
<\|f\|_2.
$$

This is a genuine dimension-free positive-frequency theorem for the frozen-weight reversible reference transfer. It is **not yet** a theorem on the actual `P_*` connected orbit.

### Restart bar and current overlap handling

A qualifying continuation now requires either:

- a depth-uniform two-seminorm/energy inequality propagating the fresh-coordinate Sobolev gain through the actual nonreversible defect and explicit boundary transmission/tilt; or
- an orbit-specific theorem giving summable/geometric decay of the connected coefficients.

The present checkpoints identify concrete local ingredients but do not prove that actual-orbit iteration. Therefore no G011 is issued.

Because a G response was already in flight before the idle ruling could be relayed, Meeting 029 instructs the principal **not to click stop and destroy it**. Let that response finish, preserve any commits, route them immediately, and send G no further prompt until a new Professor ruling.

## Most recently completed programme

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
