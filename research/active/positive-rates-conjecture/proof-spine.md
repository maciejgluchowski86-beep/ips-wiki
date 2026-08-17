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

One bounded proof-architecture test is active after Meeting 026:

- Student G Assignment 010: connected dual-renewal tail bound for a fixed signed duration filter at `P_*`.

Student F is idle.

The following remain stopped: common-uniform zero-frequency occupation, the repeated-equilibrium predecessor-profile implementation, global path-space contraction of the trajectory kernel, the stationary Bellman concatenation implementation, and the singular fixed-depth short/long renewal continuation.

Meeting 026 reopens only the exact connected/separator renewal because it removes invariant projections algebraically rather than approximating them.

Operational overlap correction: exact verifier commit `e4452de` landed while Meeting 026 was being composed and before the meeting committed. It already satisfies Assignment 010's finite-prefix verification checkpoint. G proceeds directly to the all-depth connected-tail theorem.

## E1. Canonical predecessor-trail `J` quantity

Put

$$
B=b+c-a,
\qquad g=b-a,
\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The accepted sufficient singleton quantity has exact normalizations

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

## E2. Previous singular renewal theorem

Along

$$
a=\varepsilon,
\qquad b=1/10,
\qquad 1-c=\varepsilon/10,
$$

G009 proves for fixed depth `n`

$$
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1}.
$$

The short multiplier `10/11` is an all-depth East Green identity. The long multiplier `189/341` uses finite-volume relaxation and is not uniform in depth. That route stops because making the long reset repeat at fixed `epsilon` recreates the F014 spatial reset/tail-shift problem.

## E3. Fixed-filter `L^1` dual witness

For any fixed measurable

$$
\sigma:[0,\infty)\to[-1,1],
$$

define the signed duration witness `W_n^sigma` by inserting `sigma(u_j)` in every nontrivial duration integral. Pointwise `|sigma|<=1` gives

$$
\boxed{R_n\ge |W_n^\sigma|.}
\tag{DW}
$$

Therefore

$$
\limsup_n|W_n^\sigma|^{1/n}>1
$$

implies `rho_J>1` at the same fixed rates.

This is the route-level reason the new reduction can decide `(J-SPEC)`.

## E4. Exact separator/connected decomposition

Define

$$
H_N^\sigma
=\int_0^\infty w(u)\sigma(u)P_u^N\,du,
\qquad
z_\sigma
=\int_0^\infty w(u)\sigma(u)\,du,
$$

and

$$
\boxed{
Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N.
}
\tag{CQ}
$$

Then

$$
Q_N^\sigma\mathbf1=0,
\qquad
\pi_NQ_N^\sigma=0.
$$

Let `J_N` be the centered insertion/drop map and set

$$
c_1=m_0,
$$

$$
\boxed{
 c_k^\sigma
=\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1,
\qquad k\ge2.
}
\tag{CC}
$$

Expanding each

$$
H_j^\sigma=z_\sigma\Pi_j+Q_j^\sigma
$$

and using suffix projectivity, every `Pi_j` becomes an exact renewal separator. Thus the fixed-filter witness has an exact ordered-composition expansion.

## E5. Exact scalar renewal recurrence

Put

$$
a_k=z_\sigma c_k^\sigma,
\qquad
v_0=1,
$$

and let `v_n` be the separator-expanded witness coefficient. Then

$$
\boxed{
v_n=\sum_{k=1}^na_kv_{n-k}.
}
$$

With

$$
V_n=(-1)^nv_n,
\qquad
\lambda_k=(-1)^ka_k,
$$

one obtains

$$
\boxed{
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
}
\tag{REN}
$$

This is exact at every depth and uses one fixed filter.

## E6. Fixed rational filter and verified finite prefix

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

Meeting 026 fixes

$$
\boxed{
\sigma(u)=1-2e^{-(4/125)u}.
}
\tag{SIG}
$$

The phase-type resolvent formula makes all finite coefficients rational, with

$$
\boxed{
z_\sigma=\frac{114559900}{205809}.}
$$

Commit `e4452de`, `009b-dual-renewal-verifier.py`, reconstructs the finite generators and resolvents in exact rational arithmetic and verifies exact rational `lambda_1,...,lambda_7` with

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
$$

and exact

$$
\sum_{k=1}^3\lambda_k>1,
\qquad
\sum_{k=1}^7\lambda_k>1.
$$

Numerically,

$$
\sum_{k=1}^7\lambda_k
\approx1.04715575732980380.
$$

Therefore

$$
\boxed{
\delta_7:=\sum_{k=1}^7\lambda_k-1>0
}
$$

is exactly certified. The verifier does not need to print the huge rational numerator and denominator of `delta_7`: `sum7` itself is exact rational arithmetic and `delta_7=sum7-1`.

The negative signs at lengths six and seven rule out the naive positive-renewal truncation.

## E7. Active tail target

The current load-bearing theorem is

$$
\boxed{
\sum_{k\ge8}|\lambda_k|<\delta_7.
}
\tag{CT}
$$

If `(CT)` holds, then

$$
\sum_{k\ge1}\lambda_k>1.
$$

The renewal generating function

$$
\sum_{n\ge0}V_nz^n
=
\frac1{1-\sum_{k\ge1}\lambda_kz^k}
$$

then has a singularity at some `z<1`, hence

$$
\limsup_n|V_n|^{1/n}>1.
$$

By `(DW)`, this proves

$$
\boxed{\rho_J(P_*)>1.}
$$

Thus `(CT)` would rigorously refute the absolute-duration `J` domination at a strict residual point.

## E8. Why the connected tail is new

The connected operator is

$$
\boxed{
\mathcal K_N^\sigma=Q_N^\sigma J_N.
}
\tag{KO}
$$

F013--F014 encountered an invariant projection and then needed to control the shifted invariant-law error after replacing a long segment by equilibrium. Here invariant projections are extracted exactly as renewal separators before the connected coefficients are defined. Each internal connected block contains only `Q_N^sigma` factors, with the exact invariant spectral projection removed.

Therefore `(CT)` is not algebraically the same as proving one-/two-step tail-shift agreement.

However projection removal alone is not a contraction theorem. Slow nonzero modes can still survive inside `Q_N^sigma`. Assignment 010 must control the actual growing connected orbit uniformly in depth.

## E9. Existing obstructions

F009: exact finite-dimensional mode closure fails because the cyclic mode dimension grows with depth.

G009 Proposition 6.1: invertible suffix-compatible factorized resolvents have no nonzero exact finite-cylinder reproduction cycle.

These do not refute connected coefficient decay. They prohibit two obvious implementations.

## E10. Acceptable mechanisms for Assignment 010

A positive solution may use:

- a depth-uniform seminorm contraction on the actual connected orbit;
- an exact centered resolvent/Poisson identity producing geometric decay;
- a connected cluster/finite-propagation expansion with a uniform exponential tail;
- a multi-step contraction or finite-prefix plus rigorous geometric remainder;
- another theorem directly implying `(CT)` or supercritical root growth for `(REN)`.

A longer finite coefficient table is not sufficient.

## E11. Other retained exact mathematics

The stationary occupation-control hierarchy `K_N`, its monotone diameters `D_N`, the Bellman scale-extension identity, and the unweighted mismatch theorem remain correct but inactive after Meeting 024.

Common-uniform fixed-site coalescence/front facts and the exact trajectory-valued spatial kernel also remain correct but inactive.

## E12. Current stopping rule

Student G is active only on Assignment 010. Student F is idle.

The finite-prefix verifier checkpoint is complete. G should spend the block on the all-depth connected-tail theorem, not duplicate `e4452de`.

If Assignment 010 proves an all-depth connected-tail theorem, `(J-SPEC)` is decided positively at `P_*` and the proof spine must then reassess the exact ergodicity target beyond the refuted absolute-duration bound.

If it produces a rigorous structural obstruction to the connected positive-frequency mechanism, record it and stop this branch.

If it returns only more finite coefficients or a generic request for a better norm, return to Meeting 025's `no-credible-route` state. No automatic filter optimization or another profile/coupling/Bellman variant follows.

## Anti-circularity checkpoint

Do not infer the connected tail from its first few tiny coefficients; use `Q Pi=0` as if it implied contraction; posit fixed finite mode closure; revive the old long-reset/tail-shift theorem; or treat a proof `rho_J>1` as a proof of nonergodicity. It would refute only the sufficient absolute-duration domination.
