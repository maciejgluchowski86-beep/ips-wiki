# Group meeting 020: recombined zero mode survives; one light-cone screening test remains

Date: 2026-08-17

Professor review of:

- Meeting 019 and its route checkpoint;
- Student F commit `a7cddfd`, `students/student-f/013-signed-two-insertion-recombination.md`;
- exact verifier commit `8d4feea`, `students/student-f/013-signed-two-insertion-recombination-verifier.py`;
- F010--F012 only at the interfaces used by F013;
- current `state.md` and `proof-spine.md`.

`state_narrowed: yes`.

Evidence pointer: F013 Sections 3--6 and the exact verifier.

## Ruling in one sentence

Full signed recombination does **not** algebraically remove the zero-frequency obstruction: the two-insertion defect contains a genuine invariant spectral projection whose remote norm is, away from the product surface, equivalent to the old tail-shift defect up to an exponentially localized covariance. Therefore the mass/disagreement split was not the origin of the zero mode.

However, this does not yet refute the actual `L^1(w)` two-insertion localization `Gamma_M->0`. There is exactly one concrete mechanism left worth testing: **light-cone screening on the `w`-weighted time scale**. This is a finite-propagation statement, not a depth-uniform spectral-gap or generic observability problem.

## Professor check: exact recombined spectral decomposition

Put

$$
r_0=\frac1{1+b},\qquad
m_0=Br_0-c=\frac{b(1-c)-a}{1+b},
$$

and

$$
\rho_N:=\mathcal J_N\pi_N-m_0\pi_{N-1}.
$$

For

$$
\kappa_{N,u}
=\mathcal J_{N-1}\bigl((\mathcal J_N\pi_N)P_u^{N-1,0}\bigr),
\qquad
a(u)=\kappa_{N,u}(1),
$$

F proves

$$
\boxed{
\begin{aligned}
E_{N,u}(f)
&:=\kappa_{N,u}(f)-a(u)\pi_{N-2}(f)\\
&=m_0\rho_{N-1}(f)
+\rho_N(P_u^{N-1,0}-\Pi_{N-1})
\left[Y_{N-1}(f-\pi_{N-2}f)\right].
\end{aligned}
}
\tag{20.1}
$$

This is an identity for the **unsplit signed transfer**. The first term is the invariant projection of the actual finite-volume Markov semigroup; the second is its transient complement. For each fixed finite `N`, the transient term tends to zero as `u->infinity`, so

$$
\lim_{u\to\infty}E_{N,u}(f)=m_0\rho_{N-1}(f).
$$

I accept the derivation. The verifier checks the same algebra exactly with a rational invariant-preserving resolvent kernel and separately checks the invariant projection.

The scalar mass `a_N(u)` is also correctly shown to be independent of `N` by suffix projectivity.

## Professor check: the zero mode is the old tail-shift defect plus a local covariance

F proves the exact spatial decomposition

$$
\boxed{
\rho_n(f)
=m_0(\bar\pi_n-\pi_{n-1})(f)
+B\pi_n[(\eta_n-r_0)f].
}
\tag{20.2}
$$

F010 already gives, for support separated by `M`,

$$
|B\pi_n[(\eta_n-r_0)f]|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
$$

Hence if `R_M` denotes the remote operator norm of `rho_n`,

$$
\boxed{
\left|R_M-|m_0|\Delta_M\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}.
}
\tag{20.3}
$$

For the zero-frequency part of the two-insertion defect the separation is `M+1`, giving

$$
\boxed{
\left|Z_M-|m_0|^2\Delta_{M+1}\right|
\le
\frac{2|m_0|Bbc}{(1+b)^3(2+b)^M}.
}
\tag{20.4}
$$

Thus, whenever `m_0!=0`, the invariant projection is nonlocal exactly to the same extent as the old tail-shift response, modulo an already localized term. This is the decisive negative answer to the algebraic recombination question posed in Meeting 019.

## Exceptional product surface

F also correctly identifies

$$
m_0=0
\iff a=b(1-c).
$$

On this surface the finite zero-boundary invariant law is the Bernoulli product law of density `r_0`; detailed balance follows from the constant ratio of the two flip rates. Then `\mathcal J_N\pi_N=0` and

$$
\boxed{\Gamma_M=0\quad\text{for all }M.}
$$

The verifier checks a rational instance exactly. I accept the general detailed-balance argument.

## What F013 does and does not decide

F013 establishes that the zero mode is intrinsic to the signed two-insertion transfer. It does **not** establish a lower bound on

$$
\Gamma_M
=
\sup_N\int_0^\infty w(u)\|E_{N,u}\|_{\mathrm{remote},M}\,du,
$$

because `m_0 rho_{N-1}` and the transient complement in `(20.1)` may cancel at the **same duration** `u`. Such same-duration cancellation is allowed by the Meeting-009 norm order.

A generic request for a depth-uniform observability estimate would merely repackage the missing mixing/tail-shift problem. I do not authorize that as the next route.

There is, however, a sharper mechanism which uses the actual form of the target norm and has not yet been tested.

## One remaining concrete mechanism: light-cone screening

The trail weight satisfies

$$
0\le w(u)\le e^{-\omega u},
\qquad \omega=1-c+a>0.
\tag{20.5}
$$

Also `|Y_j|<=c` throughout the residual chamber (`c>b-a`), so

$$
\|\kappa_{N,u}\|_{TV}\le c^2,
\qquad
|a(u)|\le c^2,
$$

and therefore

$$
\|E_{N,u}\|_{TV}\le2c^2.
\tag{20.6}
$$

Consequently, for any `alpha>0`, the late-duration contribution has the uniform bound

$$
\int_{\alpha M}^\infty
w(u)\|E_{N,u}\|_{\mathrm{remote},M}\,du
\le
\frac{2c^2}{\omega}e^{-\omega\alpha M}.
\tag{20.7}
$$

Thus `Gamma_M->0` does **not** require uniform relaxation of the finite chains for all time. It is enough to prove that while `u` is at most a fixed linear fraction of the spatial gap, the exact cancellation already present in `E_{N,u}` cannot communicate through the gap except with a finite-speed tail.

A sufficient short-time estimate would be, for some constants independent of `N,M`,

$$
\boxed{
\|E_{N,u}\|_{\mathrm{remote},M}
\le
C e^{-\gamma M}
+C\,P(\operatorname{Pois}(\Lambda u)\ge \delta M),
\qquad 0\le u\le\alpha M,
}
\tag{20.8}
$$

with `alpha` chosen so the Poisson large-deviation term is exponentially small in `M`. An equivalent bound of the form `C exp[-gamma(M-vu)_+]` would also suffice. Combining `(20.7)`--`(20.8)` gives exponential decay of `Gamma_M`.

This is genuinely different from assuming a depth-uniform spectral gap: it asks only for **short-time finite-propagation screening of the recombined signed defect**, then lets the existing trail weight kill late times.

At `u=0`, the object is the centered covariance of the fixed two-site suffix observable `Y_NY_{N-1}` with the remote test. A proof of `(20.8)` therefore naturally starts by extending F010's fixed-suffix positive-frequency localization from one rightmost spin to this particular two-site centered suffix observable, and then comparing positive time `u` to the no-crossing graphical evolution.

## Route-level decision

The current predecessor-trail implementation is not continued on the vague question "can the transient screen the zero mode?". It receives exactly one bounded test of the concrete estimate `(20.8)`.

Student F gets Assignment 014 on this light-cone screening mechanism. Student G remains idle.

If F014 proves a bound sufficient for `(20.8)`, then `Gamma_M->0` is established and the group will next decide whether the resulting two-insertion localization has a composable block structure.

If F014 proves that even the short-time recombined defect contains a nonlocal zero-frequency response not controlled by fixed-suffix localization plus finite propagation, or returns unresolved without a sharper mechanism, then the present predecessor-trail/profile implementation is recorded as exhausted. Do not issue a generic observability, spectral-gap, matrix-product, or third-insertion variant by default.

## Ruling

- `state_narrowed: yes`.
- F013's exact recombined decomposition `(20.1)` is accepted.
- The zero temporal-frequency term survives before any positive branch split.
- Away from `a=b(1-c)`, its remote norm is equivalent to the old tail-shift defect up to exponential covariance localization.
- On `a=b(1-c)`, the invariant law is product Bernoulli and the signed insertion vanishes identically.
- `Gamma_M->0` remains unresolved.
- Generic depth-uniform observability/mixing is not accepted as a concrete continuation.
- One final bounded **light-cone screening** test is authorized because the `w` tail makes only short-time localization necessary.
