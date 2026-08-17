# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

## E0. Current route status

There is presently **no active proof architecture**.

Student G is idle after Meeting 027; no G011. Student F is idle; no F016.

Stopped/inactive mechanisms include:

- common-uniform zero-frequency disagreement occupation;
- the repeated-equilibrium predecessor-trail/profile implementation;
- global path-space TV/KL contraction of the trajectory kernel;
- the stationary Bellman-corrector concatenation implementation;
- G009's singular fixed-depth short/long renewal continuation;
- the fixed-filter connected dual-renewal continuation after bounded Assignment 010.

The operative architecture assessment is consultation 002 / Meeting 025: **no presently identified route clears the continuation bar**. Meeting 027 adds reusable positive-frequency mathematics but does not provide a complete route.

## E1. Canonical predecessor-trail `J` quantity

Put

$$
B=b+c-a,
\qquad g=b-a,
\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

For singleton depth `n`,

$$
\boxed{
J_n=\frac BgR_n=\frac gBN_n.
}
$$

Hence

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}
$$

is also the root growth rate of `R_n` and `N_n`.

`(J-SPEC)` remains open.

## E2. G009 singular fixed-depth theorem

Along

$$
a=\varepsilon,
\qquad b=1/10,
\qquad 1-c=\varepsilon/10,
$$

G009 proves for every fixed depth `n`

$$
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1}.
$$

The base splits as

$$
\frac{499}{341}=\frac{10}{11}+\frac{189}{341}>1.
$$

The `10/11` short channel is an all-depth East Green identity. The long channel is only fixed-volume and cannot be repeated uniformly without the stopped spatial-memory theorem. This does not imply fixed-rate `rho_J>1`.

## E3. Fixed-filter `L^1` dual witness and exact renewal

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

fix

$$
\sigma(u)=1-2e^{-(4/125)u}.
$$

For

$$
H_N^\sigma=\int w(u)\sigma(u)P_u^Ndu,
\qquad
Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N,
$$

one has

$$
Q_N^\sigma\mathbf1=0,
\qquad
\pi_NQ_N^\sigma=0.
$$

Define

$$
c_1=m_0,
$$

$$
\boxed{
c_k^\sigma
=\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1,
\qquad k\ge2.
}
$$

Expanding every `H=zPi+Q` gives an exact renewal decomposition. With

$$
a_k=z_\sigma c_k^\sigma,
\qquad
\lambda_k=(-1)^ka_k,
$$

$$
\boxed{
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
}
\tag{REN}
$$

The fixed signed witness satisfies `R_n>=|W_n^sigma|`, so supercritical root growth of `V_n` proves `rho_J(P_*)>1`.

## E4. Verified finite renewal prefix

Commit `e4452de` reconstructs the finite generators and rational resolvents exactly. It verifies exact rational `lambda_1,...,lambda_7`, with

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
$$

and

$$
\sum_{k=1}^7\lambda_k>1.
$$

Numerically,

$$
\sum_{k=1}^7\lambda_k\approx1.04715575732980380.
$$

Thus

$$
\delta_7:=\sum_{k=1}^7\lambda_k-1>0
$$

is exactly certified.

The sufficient connected-tail theorem

$$
\boxed{
\sum_{k\ge8}|\lambda_k|<\delta_7
}
\tag{CT}
$$

would imply `rho_J(P_*)>1`, but remains open.

## E5. Exact stationary high-pass identity

Let

$$
A_N(f)=\pi_{N+1}(f),
\qquad
C_N(f)=\pi_{N+1}(Y_{N+1}f).
$$

G010's last-coordinate stationarity elimination gives

$$
\boxed{
C_N=A_NR_N,
\qquad
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
}
\tag{HP1}
$$

At `P_*`, with `r=1+b`, `epsilon=9/10000`, and `g_0=g+epsilon`,

$$
R_N=gI-g_0r(rI-L_N)^{-1}.
$$

This is an exact stationary boundary high-pass identity.

## E6. Depth-independent connected terminal kernel

For the actual fixed duration weight and filter, modulo constants,

$$
R_NQ_N=\int_0^\infty\kappa(t)P_t^Ndt,
$$

where

$$
\kappa=gh-g_0(k_r*h),
\qquad
k_r(t)=re^{-rt}.
$$

The repaired exact algebraic verifier `010e-terminal-kernel-verifier.py` at `ce77c9c` proves

$$
\boxed{
\|\kappa\|_1\le\Theta_\sharp,
\qquad
\Theta_\sharp\approx0.8924718201406568,
}
$$

and exactly

$$
\boxed{B\Theta_\sharp<1.}
\tag{HP2}
$$

The previous verifier failure was only a SymPy structural-equality issue; `ce77c9c` repairs it with exact `simplify(lhs-rhs)==0` checks.

The corrected 010d reversible comparison preserves only the generator/insertion reference after freezing the actual `P_*` weight externally; preserving `B` and `omega` does not preserve the canonical duration law.

## E7. Sandwiched positive-frequency contraction

For every `pi_N`-centered input `f`, multiplication by the next insertion costs at most `B` in oscillation. Therefore

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
\tag{HP3}
$$

This is a genuine depth-uniform sign-sensitive contraction on the actual connected dynamics. It is not a finite-dimensional mode closure and does not use tail-shift agreement.

## E8. Exact blind frequency

On a mode with `L_N=-x`,

$$
R(x)=\frac{d+gx}{1+b+x}.
$$

At `P_*`,

$$
\boxed{x_0=\frac{|d|}{g}=\frac1{100},}
\tag{BZ}
$$

and `R(x_0)=0`.

Therefore the one-high-pass norm in `(HP3)` cannot be uniformly inverted over the entire positive-frequency space. This does **not** prove that `x_0` belongs to the finite-volume spectrum or that the actual orbit concentrates there; it rules out only the naive one-seminorm functional-calculus iteration without extra orbit information.

## E9. Exact filtered boundary-response pairing

Let

$$
\delta_N=A_N-\pi_N,
$$

and define

$$
f_1=Y_1,
\qquad
f_N=Y_NQ_{N-1}f_{N-1}.
$$

G010 proves

$$
\boxed{
 c_{N+1}=\delta_N(R_NQ_Nf_N).
}
\tag{FB}
$$

The discrepancy itself satisfies

$$
\boxed{
\delta_NL_N
=-B A_N(I-L_N)((1+b)I-L_N)^{-1}P_N.
}
\tag{SRC}
$$

Thus the remaining connected coefficient is a zero-frequency boundary response tested only against the **special positive-frequency high-pass orbit** `R_NQ_Nf_N`.

This is narrower than F013/F014's unrestricted tail-shift norms. Neither direction of equivalence is proved.

## E10. Recentered newest-boundary block

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
\tag{XB}
$$

After normalizing the new coordinate by `sqrt(c_0g_0)`, the two off-diagonal interface blocks are equal. The scalar recentering branch `Y=X-epsilon` has uniform oscillation cost below `0.609`; the unresolved transmission is through the boundary-containing `X` branch and inherited older-volume dynamics.

## E11. Current blocker and stop rule

The connected route is now blocked at a precise point:

- `(HP3)` contracts a full insertion only after measuring the output through `R_N`;
- `(BZ)` prevents generic recovery of the unfiltered connected norm from that one high-pass quantity;
- the coefficient needed for `(CT)` is exactly the special pairing `(FB)`.

A plausible future repair would require either:

1. an **explicit complementary observable/seminorm** with a proved two-component depth-uniform contraction that covers the blind frequency; or
2. an **orbit-specific theorem** that bounds `(FB)` summably/geometrically.

No such object or theorem is currently supplied. “Find another norm” is therefore not an active assignment.

Meeting 027 applies Assignment 010's bounded-block stop: no G011, no F016, both students idle, and the programme returns to the consultation-002 / Meeting-025 `no-credible-route` architecture state.

## E12. Other retained exact mathematics

The stationary occupation-control hierarchy `K_N`, monotone diameters `D_N`, Bellman scale-extension identity, and controller-uniform unweighted mismatch theorem remain correct but inactive after Meeting 024.

Common-uniform fixed-site coalescence/front facts and the exact trajectory-valued spatial kernel remain correct but inactive.

## Anti-circularity checkpoint

Do not infer `(CT)` from the finite prefix; treat `R_NQ_N` contraction as an iterable norm without covering `(BZ)`; assert that `(FB)` is equivalent to bare tail shift without a theorem; import the nearby reversible model's canonical duration law; optimize the filter or compute longer prefixes as a substitute for an all-depth theorem; or treat `rho_J>1`, if later proved, as nonergodicity. It would refute only the sufficient absolute-duration route.
