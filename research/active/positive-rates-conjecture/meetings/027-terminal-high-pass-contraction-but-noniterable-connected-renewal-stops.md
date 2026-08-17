# Group meeting 027: terminal high-pass contracts, but the connected renewal does not iterate; bounded branch stops

Date: 2026-08-17

Professor review of:

- Meeting 026 and Assignment 010's bounded-block stopping rule;
- Student G final report `7d35358`, `students/student-g/010-connected-dual-renewal-tail-decision.md`;
- `010e-terminal-connected-kernel-checkpoint.md`, repaired verifier `010e-terminal-kernel-verifier.py` at `ce77c9c`, `010f-sandwiched-oscillation-contraction-checkpoint.md`, `010g-filtered-tail-shift-interface-checkpoint.md`, and `010h-recentered-boundary-block-checkpoint.md`;
- corrected `010d-nearby-reversible-point-checkpoint.md` at `d4632e0`;
- current `state.md`, `proof-spine.md`, and Meeting 025's `no-credible-route` fallback.

`state_narrowed: yes`.

Evidence pointer: G010 equations `(3.1)`, `(4.1)`--`(4.3)`, `(5.2)`, `(6.1)`--`(6.3)`, and the recentered block `(7.1)`--`(7.2)`. The repaired verifier now runs through the exact algebraic terminal-kernel certificate and proves `B Theta_sharp < 1`.

## Ruling

Assignment 010 materially narrows the connected positive-frequency problem but does **not** prove the connected-tail bound `(CT)`, does not prove `rho_J(P_*)>1`, and does not refute the fixed dual-renewal witness. Under the pre-registered bounded-block rule, the connected-renewal continuation now stops. No G011 is issued. Student G becomes idle; Student F remains idle.

The exact dual-renewal reduction and the new terminal high-pass theorem are retained as reusable mathematics. The operative proof-architecture status returns to consultation 002 / Meeting 025: **no presently identified proof architecture clears the continuation bar**.

This is a stop of the current implementation, not a claim that `(J-SPEC)` is false or that no complementary positive-frequency construction can exist.

## 1. Repaired exact terminal-kernel certificate

The earlier committed verifier failure was a SymPy structural-equality defect. Commit `ce77c9c` replaces the two radical identities by `simplify(lhs-rhs)==0` checks without changing the mathematics. The repaired script runs through the later assertions.

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

for the fixed filter

$$
\sigma(t)=1-2e^{-(4/125)t},
$$

G's stationary boundary elimination gives

$$
\boxed{
C_N=A_NR_N,
\qquad
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
}
\tag{27.1}
$$

Writing `r=1+b`, `epsilon=9/10000`, and `g_0=g+epsilon`,

$$
R_N=gI-g_0r(rI-L_N)^{-1}.
$$

Since `R_N` commutes with the fixed connected resolvent, modulo constants

$$
R_NQ_N=\int_0^\infty \kappa(t)P_t^N\,dt
$$

with a depth-independent signed kernel

$$
\kappa=gh-g_0(k_r*h),
\qquad k_r(t)=re^{-rt}.
\tag{27.2}
$$

The exact algebraic verifier proves a cancellation-improved bound

$$
\boxed{
\|\kappa\|_1\le\Theta_\sharp,
\qquad
\Theta_\sharp\approx0.8924718201406568,
}
\tag{27.3}
$$

and exactly

$$
\boxed{B\Theta_\sharp<1.}
\tag{27.4}
$$

The numerical value is about `0.9807372831525678`.

I accept this certificate. The derivation uses the actual `P_*` duration weight. The corrected 010d comparison is only a frozen-weight reversible **generator/insertion** reference; preserving `B` and `omega` does not preserve the canonical duration weight because the one-particle survival factor depends on `a` separately.

## 2. Genuine depth-uniform sandwiched contraction

Every output of `Q_N` is `pi_N`-centered, hence its range contains zero. Multiplication by the new insertion satisfies

$$
\operatorname{osc}(Y_{N+1}f)
\le B\operatorname{osc}(f).
$$

Combining this with `(27.3)` gives the exact all-depth theorem

$$
\boxed{
\operatorname{osc}
\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad
q_\sharp=B\Theta_\sharp<1.
}
\tag{27.5}
$$

This is real target-relevant progress. It is a positive-frequency, sign-sensitive contraction for the actual fixed filter and actual finite-volume generators; it does not use a finite-dimensional mode closure or a tail-shift estimate.

## 3. Why `(27.5)` does not iterate

On an `L_N` mode with `L_N=-x`, the high-pass multiplier is

$$
R(x)=\frac{d+gx}{1+b+x}.
$$

At `P_*`,

$$
\boxed{x_0=\frac{|d|}{g}=\frac1{100},}
\tag{27.6}
$$

and `R(x_0)=0`. Therefore there is no depth-uniform reverse comparison on the full positive-frequency space obtained by simply inverting this one high-pass factor.

This does not prove that the actual finite-volume spectra contain `x_0`, nor that the connected orbit concentrates there. Its exact consequence is narrower: the one-seminorm functional-calculus iteration suggested by `(27.5)` is structurally unavailable without further information about the actual orbit or another observable covering the blind frequency.

## 4. Exact remaining pairing

Let

$$
A_N(f)=\pi_{N+1}(f),
\qquad
\delta_N=A_N-\pi_N,
$$

and define the connected orbit

$$
f_1=Y_1,
\qquad
f_N=Y_NQ_{N-1}f_{N-1}.
$$

Because `pi_N R_NQ_N=0`, the connected coefficient satisfies exactly

$$
\boxed{
 c_{N+1}=\delta_N(R_NQ_Nf_N).
}
\tag{27.7}
$$

The same stationarity identity gives

$$
\boxed{
\delta_NL_N
=-B A_N(I-L_N)((1+b)I-L_N)^{-1}P_N.
}
\tag{27.8}
$$

So the remaining object is a zero-frequency spatial boundary response only after testing against the **special filtered connected orbit** `R_NQ_Nf_N`.

This is strictly narrower than F013/F014's unrestricted one-/two-step tail-shift norms. G does not prove either direction of equivalence, and I agree that none follows from the present algebra. Thus the connected route has not merely renamed the old tail-shift problem.

## 5. Recentered boundary block

With

$$
X_i=Y_i+\varepsilon,
\qquad
c_0=999/1000,
\qquad
g_0=999/10000,
$$

the newest-coordinate block becomes

$$
\boxed{
L_{N+1}
=
\begin{pmatrix}
L_N+c_0P_N & g_0c_0P_N\\
P_N & L_N-(1+b)I+g_0P_N
\end{pmatrix}.
}
\tag{27.9}
$$

After normalizing the new coordinate by `sqrt(c_0g_0)`, the two off-diagonal interface blocks agree. The affine scalar branch `Y=X-epsilon` is already uniformly contractive, with exact bound below `0.609`. The unresolved transmission is therefore through the boundary-containing `X` branch and the inherited older-volume dynamics, not the scalar recentering defect.

## 6. Stop-rule application

Assignment 010 was explicitly one bounded block. It has now produced both a genuine theorem and a precise residual blocker:

- the terminal/sandwiched high-pass contraction `(27.5)` is strict and depth-uniform;
- one-high-pass iteration is blocked by the exact positive-frequency zero `(27.6)`;
- the actual coefficient reduces to the special orbit pairing `(27.7)`.

The plausible repairs are a complementary high-pass observable or an orbit-specific estimate for `(27.7)`. Neither is currently supplied with a concrete second operator, a two-seminorm contraction matrix, or another theorem whose constants can be checked. Assigning “find the complementary norm” would therefore be a new generic search, not continuation of a proved mechanism. Given the bounded-block precommitment and the limited target-level payoff of further `(J-SPEC)` diagnostics, I do not authorize it now.

A future restart may occur if genuinely new input supplies, for example:

1. an explicit second observable/seminorm with a proved two-component depth-uniform contraction closing the blind frequency; or
2. a theorem specific to the actual connected orbit that bounds the pairings `(27.7)` summably or geometrically.

Merely proposing another filter, another norm, or larger connected-coefficient computations does not clear the restart bar.

## Current programme state

- `state_narrowed: yes`.
- `(J-SPEC)` remains open.
- `(CT)` remains open.
- The exact dual-renewal recurrence and fixed-filter finite prefix remain valid.
- The repaired terminal-kernel certificate and sandwiched contraction `(27.5)` are accepted as reusable exact mathematics.
- The filtered boundary-response identity `(27.7)`--`(27.8)` is the sharpest residual formulation of this route.
- No G011; Student G idle.
- No F016; Student F idle.
- No proof architecture currently active.
- Consultation 002 / Meeting 025 `no-credible-route` is again the operative proof-architecture assessment pending genuinely new principal, external, or literature input.
