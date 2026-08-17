# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/028-boundary-resolvent-elimination-sharpens-residual-object-but-does-not-reopen.md`, `state_narrowed: yes`.

Active work:

- Student G: idle; no G011.
- Student F: idle; no F016.
- No proof architecture is currently active.

Operative proof-architecture status: **`no-credible-route`**, in the precise consultation-002 / Meeting-025 sense. This does not say the conjecture is false or that every conceivable proof architecture is impossible.

Operational overlap: G's `75d0e8a` landed after Meeting 027 because the idle ruling had not yet been relayed. Meeting 028 treats it as an orchestration overlap, not disregard of the stop. It is accepted as exact algebraic sharpening but does not reopen the branch.

## Stopped / inactive interfaces

Stopped or inactive mechanisms include:

- common-uniform global coalescence / zero-frequency disagreement occupation (Meeting 019);
- the repeated-equilibrium centered predecessor-trail/profile implementation (Meeting 021);
- global path-space TV/KL contraction of the exact trajectory kernel `Q`;
- the stationary boundary-control Bellman-corrector concatenation implementation (Meeting 024);
- G009's singular fixed-depth short/long renewal continuation (Meeting 025);
- the fixed-filter connected dual-renewal continuation after the bounded Assignment 010 block (Meetings 027--028).

The last stop is an implementation/continuation decision, not a refutation of the fixed dual-renewal witness.

## Canonical `J` quantity and `(J-SPEC)`

For singleton depth `n`,

$$
\boxed{
J_n=\frac BgR_n=\frac gBN_n,
}
\qquad B=b+c-a,\quad g=b-a,
$$

so `R_n`, `J_n`, and `N_n` have the same exponential growth rate

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

`(J-SPEC)` remains open: neither `rho_J>1` at a fixed strict residual point nor a useful opposite theorem has been proved.

## G009 singular fixed-depth theorem retained

Along

$$
a=\varepsilon,\qquad b=\frac1{10},\qquad 1-c=\frac\varepsilon{10},
$$

G009 proves for every fixed `n`

$$
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1},
$$

with

$$
\frac{499}{341}=\frac{10}{11}+\frac{189}{341}>1.
$$

The `10/11` short channel is an all-depth East Green identity. The `189/341` long channel is only a fixed-volume reset; making it uniform in depth recreates the stopped spatial-memory problem. Therefore this does not imply fixed-rate `rho_J>1`.

## Exact fixed-filter dual renewal

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

fix

$$
\sigma(u)=1-2e^{-(4/125)u}.
$$

Define

$$
H_N^\sigma=\int_0^\infty w(u)\sigma(u)P_u^N\,du,
\qquad
z_\sigma=\int_0^\infty w(u)\sigma(u)\,du,
$$

$$
Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N.
$$

Then

$$
Q_N^\sigma\mathbf1=0,
\qquad
\pi_NQ_N^\sigma=0.
$$

For connected coefficients

$$
c_1=m_0,
$$

$$
c_k^\sigma
=\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1,
\qquad k\ge2,
$$

expanding each `H=zPi+Q` extracts invariant projections exactly as renewal separators. With

$$
a_k=z_\sigma c_k^\sigma,
\qquad
\lambda_k=(-1)^ka_k,
$$

the fixed-filter witness obeys

$$
\boxed{
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
}
$$

The signed witness is dominated by the canonical absolute-duration norm, so supercritical growth of `V_n` would prove `rho_J(P_*)>1`.

Commit `e4452de` exactly verifies the first seven rational renewal coefficients. In particular

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
$$

and

$$
\sum_{k=1}^7\lambda_k>1.
$$

Numerically this partial sum is about `1.04715575732980380`. Thus

$$
\delta_7:=\sum_{k=1}^7\lambda_k-1>0
$$

is exactly certified. The sufficient tail target

$$
\sum_{k\ge8}|\lambda_k|<\delta_7
\tag{CT}
$$

remains open.

## G010 exact terminal high-pass theorem

Student G's Assignment 010 derives the stationary boundary functional identity

$$
\boxed{
C_N=A_NR_N,
\qquad
R_N=(dI-gL_N)((1+b)I-L_N)^{-1}.
}
$$

For the actual fixed filter, modulo constants,

$$
R_NQ_N=\int_0^\infty\kappa(t)P_t^N\,dt
$$

with a depth-independent signed kernel. The repaired exact verifier `010e-terminal-kernel-verifier.py` at `ce77c9c` proves

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
$$

Hence for every centered input whose range contains zero,

$$
\boxed{
\operatorname{osc}
\left(
R_{N+1}Q_{N+1}(Y_{N+1}f)
\right)
\le q_\sharp\operatorname{osc}(f),
\qquad q_\sharp=B\Theta_\sharp<1.
}
\tag{HP}
$$

This is a genuine depth-uniform, sign-sensitive positive-frequency contraction for the actual `P_*` generators and actual duration weight.

The earlier 010d reversible comparison is retained only with its correction `d4632e0`: preserving `B` and `omega` does **not** preserve the canonical duration weight because the one-particle survival factor depends separately on `a`. The reversible point is therefore only a frozen-weight generator/insertion reference.

## Why the high-pass theorem does not iterate

On a mode with `L_N=-x`,

$$
R(x)=\frac{d+gx}{1+b+x}.
$$

At `P_*`,

$$
\boxed{x_0=\frac{|d|}{g}=\frac1{100},}
$$

so `R(x_0)=0`. Therefore no uniform reverse comparison on the full positive-frequency space follows by inverting this one high-pass factor.

This does **not** prove that the finite-volume spectrum contains `x_0`, nor that the actual connected orbit lives near it. It proves only that the one-high-pass functional-calculus iteration is unavailable without additional orbit information or a complementary observable.

## Boundary response: filtered pairing and exact elimination

Let

$$
A_N(f)=\pi_{N+1}(f),
\qquad
\delta_N=A_N-\pi_N,
$$

and define

$$
f_1=Y_1,
\qquad
f_N=Y_NQ_{N-1}f_{N-1},
\qquad
q_N:=Q_Nf_N.
$$

G010 first proved

$$
 c_{N+1}=\delta_N(R_Nq_N)
$$

with source equation

$$
\delta_NL_N
=-B A_N(I-L_N)((1+b)I-L_N)^{-1}P_N.
$$

The late checkpoint `75d0e8a`, accepted at Meeting 028, eliminates `delta_N` exactly. Put

$$
r=1+b,
\qquad
S_N=(rI-L_N)^{-1},
\qquad
D_N=(I-L_N)S_N.
$$

Then

$$
\boxed{
 c_{N+1}
 =A_N\!\left[
 \frac dr q_N
 +\left(g-\frac dr\right)B
 D_NP_NS_Nq_N
 \right].
}
\tag{BRE}
$$

At `P_*`, `d/r=-\varepsilon`, `\varepsilon=9/10000`, and `g_0=g+\varepsilon`, so

$$
\boxed{
 c_{N+1}=A_N(\mathfrak B_Nq_N),
}
$$

with

$$
\boxed{
\mathfrak B_N
=-\varepsilon I
+g_0B(I-L_N)(rI-L_N)^{-1}
P_N(rI-L_N)^{-1}.
}
\tag{BR}
$$

Thus no estimate of the unrestricted norm of `delta_N` or bare tail-shift TV is logically required for the connected coefficient. Any future claim that this route is equivalent to F013/F014's bare tail-shift problem must survive `(BRE)`--`(BR)` and requires additional mathematics.

The elementary bound

$$
|c_{N+1}|
\le
\frac{342081}{1718750}\operatorname{osc}(q_N)
$$

is far too crude and gives no depth decay. The sharp residual problem is now summable/geometric control of

$$
A_N(\mathfrak B_Nq_N)
$$

along the actual recursion

$$
q_N=Q_N(Y_Nq_{N-1}).
$$

This is a target, not a currently available mechanism.

## Recentered newest-boundary block

With

$$
X_i=Y_i+\varepsilon,
\qquad
c_0=999/1000,
\qquad
g_0=999/10000,
$$

the newest-coordinate block is

$$
L_{N+1}
=
\begin{pmatrix}
L_N+c_0P_N & g_0c_0P_N\\
P_N & L_N-(1+b)I+g_0P_N
\end{pmatrix}.
$$

After normalizing `X` by `sqrt(c_0g_0)`, the two off-diagonal interface blocks agree. The scalar recentering branch `Y=X-\varepsilon` is already uniformly contractive, with exact oscillation cost below `0.609`. The unresolved transmission is through the boundary-containing `X` branch and inherited older-volume dynamics.

## Meetings 027--028 stop decision

Assignment 010 was a pre-registered bounded block. It produced a real all-depth theorem `(HP)` and then the exact boundary-resolvent elimination `(BRE)`, but no proof of `(CT)` and no fixed-rate `rho_J>1` theorem.

The late elimination does not clear Meeting 027's restart bar. A future restart requires either:

- an **explicit complementary high-pass observable/seminorm** with a proved two-component depth-uniform contraction covering the blind frequency; or
- an **orbit-specific theorem** giving summable/geometric control of `A_N(\mathfrak B_Nq_N)` along the actual connected recursion.

Neither currently exists. A generic instruction to prove decay of the new boundary-resolvent expression or to search for another norm is not authorized. No G011.

## Other retained exact mathematics

The stationary occupation-control hierarchy `K_N`, monotone diameters `D_N`, Bellman scale-extension identity, and controller-uniform unweighted mismatch theorem remain correct but inactive after Meeting 024.

The common-uniform fixed-site coupling facts and the exact trajectory-valued spatial kernel remain correct but inactive.

## Unresolved target-level facts

Open:

- `(J-SPEC)` and `(CT)`;
- the boundary-resolvent orbit coefficients `(BRE)`--`(BR)`;
- one-/two-step tail-shift agreement off the product surface;
- `Gamma_M->0` and general `J_{x,r}->0`;
- common-uniform extinction versus convective survival;
- stationary diameter collapse `D_N(h)->0`;
- full ergodicity in the residual chamber.

## Wiki

Keep the live wiki frozen during research.
