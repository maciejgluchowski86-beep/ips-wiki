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

Latest meeting: `meetings/020-recombined-zero-mode-survives-light-cone-screening-test.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-014.md`, one bounded light-cone screening test for the recombined two-insertion signed defect.
- Student G successor: idle. No G009 common-coupling continuation is authorized.

## Closed / stopped mechanisms

Closed: fixed finite walls; cellwise nonnegative scaffold insertion; one-step centered `L^1`; crude scalar `max{c,b-a}Z<1`; exposed-only global Foster product; full nearest-neighbour scalar edge-product/coboundary Foster class; depth-uniform finite linear common-mass mode closure.

Stopped: raw finite-window/HJB certification by enlarging `L,R,T` or changing the right-boundary controller.

Abandoned as a load-bearing interface after Meeting 019: common-uniform global coalescence / zero-frequency disagreement occupation. Previously proved common-coupling facts remain valid auxiliary lemmas.

## Global predecessor-trail target

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
\qquad w(u)=e^{-\omega u}s_1(u).
$$

The working reduction leaves

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

Showing `J_{x,r}->0` with depth is sufficient for the nonempty-exit term. Every duration remains visible until the final modulus.

## F013: zero mode survives full signed recombination

Define

$$
(\mathcal J_N\mu)(f)=\mu((B\eta_N-c)f),
\qquad
\rho_N=\mathcal J_N\pi_N-m_0\pi_{N-1},
$$

with

$$
r_0=\frac1{1+b},
\qquad
m_0=Br_0-c=\frac{b(1-c)-a}{1+b}.
$$

For the full two-insertion signed defect

$$
E_{N,u}(f)
:=\kappa_{N,u}(f)-a(u)\pi_{N-2}(f),
$$

F013 proves the exact spectral decomposition

$$
\boxed{
E_{N,u}(f)
=m_0\rho_{N-1}(f)
+\rho_N(P_u^{N-1,0}-\Pi_{N-1})
\left[Y_{N-1}(f-\pi_{N-2}f)\right].
}
$$

Thus the zero temporal-frequency component is intrinsic to the unsplit signed transfer.

Also

$$
\boxed{
\rho_n(f)
=m_0(\bar\pi_n-\pi_{n-1})(f)
+B\pi_n[(\eta_n-r_0)f].
}
$$

The second term is exponentially localized by F010, so away from `m_0=0` the remote norm of `rho_n` is equivalent to `|m_0|Delta_M` up to an exponential error. For the two-insertion zero mode the leading nonlocal term is `|m_0|^2 Delta_{M+1}`.

Therefore the old zero-frequency obstruction was **not** created by splitting signed mass and disagreement pieces.

On the exceptional surface

$$
a=b(1-c),
$$

one has `m_0=0`; the finite zero-boundary invariant law is Bernoulli product of density `1/(1+b)`, `J_N pi_N=0`, and the two-insertion defect vanishes identically.

## Why `Gamma_M` is still not decided

The target is

$$
\Gamma_M
=
\sup_N\int_0^\infty w(u)
\|E_{N,u}\|_{\mathrm{remote},M}du.
$$

The transient complement may cancel the invariant projection at the **same duration** `u`; this is allowed by the norm order. F013 does not prove or refute `Gamma_M->0`.

A generic depth-uniform observability or mixing theorem is not accepted as a concrete continuation.

## Meeting 020: one final light-cone screening mechanism

Because

$$
0\le w(u)\le e^{-\omega u}
$$

and `|Y_j|<=c`,

$$
\|E_{N,u}\|_{TV}\le2c^2.
$$

Hence for every `alpha>0`,

$$
\int_{\alpha M}^\infty
w(u)\|E_{N,u}\|_{\mathrm{remote},M}du
\le
\frac{2c^2}{\omega}e^{-\omega\alpha M}.
$$

Therefore `Gamma_M->0` only requires **short-time spatial screening** for `u<=alpha M`. Assignment 014 asks for a bound such as

$$
\|E_{N,u}\|_{\mathrm{remote},M}
\le
C e^{-\gamma M}
+C P(\operatorname{Pois}(\Lambda u)\ge\delta M),
\qquad 0\le u\le\alpha M,
$$

or an equivalent light-cone estimate.

The required first subproblem is the static centered two-site suffix covariance at `u=0`, followed by a finite-propagation comparison for positive time. No depth-uniform spectral gap is to be assumed.

If this succeeds, `Gamma_M` decays exponentially and the next question is composability of the localized two-insertion block. If it fails structurally or remains unresolved without a sharper mechanism, the current predecessor-trail/profile implementation is recorded as exhausted; do not default to generic observability, a third insertion, matrix products, or reopening common-uniform occupation.

## Anti-circularity

Do not integrate duration before the actual absolute-value norm; revive scalar local coupling products; return to common-uniform global occupation; assume an unproved uniform spectral gap; replace the light-cone test by generic long-time mixing; or infer arbitrary-depth `J` control from two-insertion localization.

## Wiki

Keep the live wiki frozen during research.
