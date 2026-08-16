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

Closed/stopped mechanisms include fixed walls, cellwise nonnegative insertion, one-step centered `L^1`, crude scalar sup bounds, exposed-only and full nearest-neighbour scalar coupling products, depth-uniform finite common-mass mode closure, raw finite-window Hamming enumeration, and common-uniform global-coalescence / zero-frequency occupation as the load-bearing disagreement interface.

## E1. Predecessor-trail criterion

Put

$$
B=b+c-a,\qquad g=b-a,\qquad\omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The working reduction leaves

$$
\boxed{
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
}
$$

`J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. Exact Poisson--Mecke factorization and the no-exit complement remain downstream audits. Every duration must remain visible until the final modulus.

## E2. Signed insertion structure

For a law `mu`,

$$
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f),
$$

and

$$
r(1-r)(\mu^1-\mu^0)(f)=\mu[(\eta_y-r)f].
$$

Thus the old positive disagreement branch is intrinsically a signed covariance.

## E3. Norm-order obstruction

Near East, integrating a trail duration before absolute value produces an apparent factor `3/5`, while the correct `L^1(w)` factor tends to `7/5`. Therefore cancellation between different duration values is unavailable.

## E4. Surviving one-segment damping

Let `r_0=1/(1+b)`. Accepted strict losses remain

$$
|Br_0-c|Z<\frac23,
\qquad
BZ_{\omega+1+b}<1.
$$

The exact signed transfer is operator-valued, and fixed depth-uniform finite linear mode closure is impossible.

## E5. Suffix projectivity and equilibrium covariance localization

Rightmost suffixes are autonomous and

$$
R_{N,M}\pi_N=\pi_M.
$$

F010 gives, with `phi_N=eta_N-r_0`,

$$
\pi_N[\phi_N((1+b)-\bar L)g]
=q_0r_0\pi_N[Dg]
$$

and the separated-gap estimate

$$
\boxed{
|\pi_N(\phi_N f)|
\le
\frac{2bc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
}
$$

This is the accepted fixed-suffix positive-frequency localization input.

## E6. Split zero-frequency response

F011 identifies the split mass defect with tail-shift variation `Delta_M`; F012 gives the sufficient common-coupling bound

$$
\Delta_M\le2c\int_0^\infty\beta_{M-1}(t)dt.
$$

These remain valid, but global common-uniform occupation is no longer pursued as the proof interface.

## E7. F013 exact recombined spectral decomposition

Define

$$
(\mathcal J_N\mu)(f)=\mu((B\eta_N-c)f),
\qquad
m_0=\frac{b(1-c)-a}{1+b},
$$

$$
\rho_N=\mathcal J_N\pi_N-m_0\pi_{N-1}.
$$

For

$$
\kappa_{N,u}
=\mathcal J_{N-1}((\mathcal J_N\pi_N)P_u^{N-1,0}),
\qquad
a(u)=\kappa_{N,u}(1),
$$

F013 proves

$$
\boxed{
\begin{aligned}
E_{N,u}(f)
&:=\kappa_{N,u}(f)-a(u)\pi_{N-2}(f)\\
&=m_0\rho_{N-1}(f)
+\rho_N(P_u^{N-1,0}-\Pi_{N-1})
[Y_{N-1}(f-\pi_{N-2}f)].
\end{aligned}}
$$

The first term is the genuine zero temporal-frequency projection of the **unsplit** signed transfer.

## E8. The recombined zero mode is the tail-shift defect plus local covariance

F013 also proves

$$
\boxed{
\rho_n(f)
=m_0(\bar\pi_n-\pi_{n-1})(f)
+B\pi_n[(\eta_n-r_0)f].
}
$$

Therefore, if `R_M` is the remote norm of `rho_n`,

$$
\left|R_M-|m_0|\Delta_M\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}.
$$

For the two-insertion zero mode,

$$
\left|Z_M-|m_0|^2\Delta_{M+1}\right|
\le
\frac{2|m_0|Bbc}{(1+b)^3(2+b)^M}.
$$

Hence algebraic recombination does not remove the zero-frequency obstruction.

On the exact surface

$$
a=b(1-c),
$$

`m_0=0`, `pi_N` is Bernoulli product of density `1/(1+b)`, `J_N pi_N=0`, and the two-insertion defect vanishes identically.

## E9. Why `Gamma_M` may still localize

Define

$$
\Gamma_M
=\sup_N\int_0^\infty w(u)\|E_{N,u}\|_{\mathrm{remote},M}du.
$$

The transient complement can cancel the zero mode at the **same duration**. F013 therefore does not prove or refute `Gamma_M->0`.

A generic depth-uniform observability/mixing theorem is not a concrete continuation.

## E10. Meeting 020 light-cone reduction

Since

$$
0\le w(u)\le e^{-\omega u}
$$

and `|Y_j|<=c`,

$$
\|E_{N,u}\|_{TV}\le2c^2.
$$

Thus for every `alpha>0`,

$$
\boxed{
\int_{\alpha M}^\infty
w(u)\|E_{N,u}\|_{\mathrm{remote},M}du
\le\frac{2c^2}{\omega}e^{-\omega\alpha M}.
}
$$

Consequently it suffices to control **short times** `u<=alpha M`. A sufficient estimate is

$$
\boxed{
\|E_{N,u}\|_{\mathrm{remote},M}
\le
C e^{-\gamma M}
+C P(\operatorname{Pois}(\Lambda u)\ge\delta M),
\qquad 0\le u\le\alpha M,
}
$$

or `C exp[-gamma(M-vu)_+]`. This is a finite-propagation screening theorem, not a spectral-gap statement.

The first required subproblem is the static two-site suffix covariance

$$
E_{N,0}(f)
=
\pi_N(Y_NY_{N-1}f)
-\pi_N(Y_NY_{N-1})\pi_{N-2}(f),
$$

with a depth-uniform separated-gap estimate. A natural route is the Poisson equation on the **fixed two-site autonomous suffix**, followed by a graphical finite-speed comparison for positive `u`.

## E11. Active block and stop rule

Student F Assignment 014 is the only active block. It tests the light-cone estimate above.

If successful, `Gamma_M` decays exponentially and the next question is whether the localized two-insertion block is composable.

If the static two-site defect is itself equivalent to the unresolved tail-shift response, or the short-time no-crossing decomposition retains an unlocalized boundary law, or F014 returns unresolved without a sharper mechanism, record the present predecessor-trail/profile implementation as exhausted. Do not default to generic observability, a third insertion, matrix products, or reopening common-uniform occupation.

## E12. Final reconstruction after `J->0`

Only after `J_{x,r}->0` is proved should the group audit Poisson--Mecke factorization, the no-exit complement, and the final convergence-to-ergodicity implication.
