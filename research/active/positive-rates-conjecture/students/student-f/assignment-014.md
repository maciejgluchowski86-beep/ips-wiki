# Student F assignment 014: light-cone screening of the recombined two-insertion defect

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/020-recombined-zero-mode-survives-light-cone-screening-test.md`;
- your `013-signed-two-insertion-recombination.md`;
- your `010-profile-regeneration-truncation.md`, especially the separated-gap positive-frequency estimate and the one-segment finite-speed bound;
- current `proof-spine.md`.

The scientific target remains the positive rates conjecture for simple IPS.

This is a bounded test of one specific mechanism. Do not turn it into a general spectral-gap, observability, matrix-product, third-insertion, or common-coupling problem.

## Accepted input from Assignment 013

Write

$$
E_{N,u}(f)
:=
\kappa_{N,u}(f)-a(u)\pi_{N-2}(f),
$$

where

$$
\kappa_{N,u}
=\mathcal J_{N-1}\bigl((\mathcal J_N\pi_N)P_u^{N-1,0}\bigr).
$$

You proved

$$
E_{N,u}(f)
=m_0\rho_{N-1}(f)
+\rho_N(P_u^{N-1,0}-\Pi_{N-1})
\left[Y_{N-1}(f-\pi_{N-2}f)\right].
\tag{L1}
$$

The invariant projection is genuinely nonlocal off the product surface and differs from `m_0^2 Delta_{M+1}` only by an exponentially localized covariance. Algebraic recombination therefore does not remove the zero mode.

The quantity to decide remains

$$
\Gamma_M
=
\sup_{N\ge M+2}
\int_0^\infty w(u)
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
|E_{N,u}(f)|du.
\tag{L2}
$$

## Why one mechanism remains

The trail weight satisfies

$$
0\le w(u)\le e^{-\omega u},
\qquad \omega=1-c+a>0.
$$

Since `|Y_j|<=c`, the full defect has the crude uniform bound

$$
\|E_{N,u}\|_{TV}\le2c^2.
$$

Therefore for every `alpha>0`,

$$
\int_{\alpha M}^\infty
w(u)\|E_{N,u}\|_{\mathrm{remote},M}du
\le
\frac{2c^2}{\omega}e^{-\omega\alpha M}.
\tag{L3}
$$

So a proof of `Gamma_M->0` only needs a **short-time spatial screening theorem** for `u<=alpha M`; no depth-uniform long-time mixing theorem is required.

## Primary target

Prove constants

$$
C<\infty,
\qquad
\gamma>0,
\qquad
\alpha>0,
$$

(depending on the fixed residual rates but not on `N,M`) such that

$$
\boxed{
\sup_{N\ge M+2}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
|E_{N,u}(f)|
\le C e^{-\gamma M}
\qquad(0\le u\le\alpha M).
}
\tag{L4}
$$

A slightly weaker but sufficient form is

$$
\boxed{
\|E_{N,u}\|_{\mathrm{remote},M}
\le
C e^{-\gamma M}
+C\,P(\operatorname{Pois}(\Lambda u)\ge\delta M)
}
\tag{L5}
$$

for fixed positive `Lambda,delta`, with `alpha` chosen below the corresponding Poisson speed. Likewise a bound `C exp[-gamma(M-vu)_+]` is acceptable.

If you prove `(L4)` or `(L5)`, combine it explicitly with `(L3)` and give an exponential upper bound for `Gamma_M`.

## Required first subproblem: the static two-site suffix defect

At `u=0`,

$$
E_{N,0}(f)
=
\pi_N(Y_NY_{N-1}f)
-\pi_N(Y_NY_{N-1})\pi_{N-2}(f).
\tag{L6}
$$

Decide first whether the centered fixed two-site suffix observable in `(L6)` has a depth-uniform separated-gap estimate

$$
\boxed{
|E_{N,0}(f)|\le C_0\vartheta^M\|f\|_\infty,
\qquad \vartheta<1.
}
\tag{L7}
$$

Do not assume this from the one-site F010 bound. Derive it from stationarity and the autonomous two-site suffix generator, or prove that such a derivation fails for a precise reason.

A natural route is to solve the Poisson equation on the **fixed two-site autonomous suffix** for the centered observable `Y_NY_{N-1}-pi_2(Y_2Y_1)`, then use stationarity to push the remaining dependence to the single boundary edge and apply finite propagation. The suffix dimension is fixed; this is not the closed depth-uniform finite-mode route refuted in F009.

## Dynamic short-time step

If `(L7)` holds, compare positive `u` with the static/no-crossing situation using the graphical construction for `P_u^{N-1,0}`.

The point is to show that before an oriented causal chain crosses a fixed fraction of the `M`-site buffer, the recombined defect is still governed by a centered **fixed-size right suffix observable** plus the already localized static error. Any remainder should be charged to an explicit Poisson crossing tail.

You may choose the buffer split and the exact finite suffix size. Keep it fixed independently of `M,N`.

## Successful positive outcome

Prove a bound sufficient for `(L4)` or `(L5)` and conclude

$$
\boxed{\Gamma_M\le C'\theta^M}
$$

for some `theta<1`.

State exactly what this establishes: two-insertion signed localization after the correct `L^1(w)` norm. It still does not prove composability or `J_{x,r}->0`.

## Successful negative outcome

A useful negative result is an exact obstruction showing that even for `u` bounded by a fixed linear fraction of the spatial gap, the recombined defect retains a nonlocal zero-frequency component which cannot be reduced to a fixed-suffix centered observable plus a causal-crossing tail.

For example, if `(L7)` is false because its remote norm is again equivalent to `Delta_M`, prove that exact equivalence. Or if the graphical no-crossing decomposition necessarily retains an unlocalized signed boundary law, identify it exactly.

Do not count the mere absence of a known spectral gap as a negative result; this assignment is designed to avoid needing one.

## Stopping rule

This is the final currently authorized predecessor-trail/profile implementation block.

If the light-cone mechanism succeeds, the next meeting may test composability of the resulting localized two-insertion block.

If it fails structurally, or remains unresolved without a sharper mechanism than `(L4)`--`(L5)`, the present predecessor-trail/profile implementation is recorded as exhausted. Do not propose generic observability, a third insertion, a matrix-product norm, or reopening common-uniform occupation as the default continuation.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/014-light-cone-screening.md`

with exact verifier code beside it if finite symbolic/rational identities are used.

End with one of:

- `light-cone screening proved: Gamma_M <= ...`;
- `light-cone screening refuted because: ...`;
- `unresolved after substantive work; exact screening blocker: ...`.
