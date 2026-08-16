# Student F assignment 013: recombine the signed insertion through one nonstationary segment

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/019-two-spin-occupation-obstruction-and-common-coupling-stop.md`;
- your `010-profile-regeneration-truncation.md`, especially the exact signed transfer, suffix projectivity, and the positive-frequency covariance resolvent in Section 5;
- your `011-zero-frequency-boundary-response.md` and `012-tail-shift-agreement.md` only to understand what is now being avoided;
- `proof-spine.md`;
- G008 only for the reason the positive common-coupling occupation interface has been stopped.

The scientific target remains the positive rates conjecture for simple IPS.

## Route change

Meeting 019 abandons the common-uniform **global-coalescence / zero-frequency occupation** mechanism as a load-bearing proof interface. Do not try to prove `G_m`, `alpha_0(T)<1`, an all-depth source-episode theorem, or a larger coupling state in this assignment.

The active predecessor-trail quantity remains

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|\,du,
$$

with every trail duration kept visible until the final modulus.

The new question is whether the mass/disagreement split itself exposed a zero-frequency obstruction that disappears when the **full signed insertion is kept recombined** for one further segment.

## Exact starting object

On the `N`-site zero-boundary interval let `pi_N` be the invariant law and

$$
Y_N=B\eta_N-c.
$$

For a signed measure `nu` on `N` sites define the centered insertion/drop

$$
(\mathcal J_N\nu)(f)=\nu(Y_N f),
$$

where `f` is a function of sites `1,...,N-1`.

Start from the **full signed first insertion**

$$
\nu_N:=\mathcal J_N\pi_N.
\tag{S1}
$$

Do not decompose `nu_N` into

$$
(Br_0-c)\bar\pi_N
+
B r_0(1-r_0)(\pi_N^1-\pi_N^0)
$$

unless you later recombine the terms before taking the relevant modulus.

Let `P_u^{N-1,0}` be the zero-boundary semigroup on the remaining sites and define the exact two-insertion profile

$$
\boxed{
\kappa_{N,u}
:=
\mathcal J_{N-1}(\nu_N P_u^{N-1,0}).
}
\tag{S2}
$$

This is a signed measure on sites `1,...,N-2`. Its total mass is

$$
a_N(u):=\kappa_{N,u}(1).
\tag{S3}
$$

First check whether suffix projectivity makes `a_N(u)` independent of `N` once `N>=2`; if so write it simply as `a(u)`.

## Primary diagnostic

For `M>=1` define the remote recombination defect

$$
\Gamma_M
:=
\sup_{N\ge M+2}
\int_0^\infty w(u)
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
\left|
\kappa_{N,u}(f)-a_N(u)\pi_{N-2}(f)
\right|\,du.
\tag{S4}
$$

The modulus is **inside** the `u` integral, as required by the Meeting-009 norm-order obstruction.

Decide whether

$$
\boxed{\Gamma_M\longrightarrow0.}
\tag{S5}
$$

Prefer an explicit summable or exponential bound.

This is a one-next-segment test only. It is not permission to assume the analogous statement at arbitrary depth.

## Why this is mathematically distinct from the stopped coupling route

For any law `mu` with rightmost density `r`,

$$
r(1-r)(\mu^1-\mu^0)(f)
=\mu[(\eta_y-r)f].
$$

Thus the old `disagreement branch` is a signed covariance. At equilibrium your Assignment 010 already proves, with

$$
\phi_N=\eta_N-r_0,
$$

the positive-frequency resolvent identity

$$
\pi_N\left[
\phi_N((1+b)-\bar L)g
\right]
=q_0r_0\pi_N[Dg],
$$

and the explicit separated-gap estimate

$$
|\pi_N(\phi_N f)|
\le
\frac{2bc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
$$

The mass/disagreement decomposition then produced a zero-frequency boundary response in the mass branch, which led eventually to the common-coupling occupation problem. Assignment 013 asks whether that zero-frequency piece is intrinsic to the **recombined** two-insertion signed object `(S2)` or an artifact of estimating the two branches separately.

## Preferred route: exact stationarity / resolvent algebra

Exploit that `nu_N=J_N pi_N` is a very special nonstationary signed measure. Do not treat it as an arbitrary signed profile.

A useful calculation would derive an exact integration-by-parts or Poisson/resolvent identity for

$$
\kappa_{N,u}(f)-a_N(u)\pi_{N-2}(f)
$$

from stationarity of `pi_N`, ideally showing that every spatially propagating defect carries a strictly positive Laplace frequency before finite-speed bounds are applied.

If a zero-frequency term remains, identify it exactly and show whether it cancels with another term in the **full** signed expression before modulus. Do not declare failure from the old split formula alone.

You may use the exact operator-valued transfer from Assignment 009, but do not truncate it to a fixed finite generator-mode alphabet; that route is closed.

## Successful positive outcome

A strong positive result is an explicit theorem of the form

$$
\Gamma_M\le C\theta^M,
\qquad C<\infty,\quad\theta<1,
$$

or another summable depth-uniform modulus.

Then state exactly what this buys for a predecessor-trail block and what remains before arbitrary repeated signed-profile composition. Do **not** infer `J_{x,r}->0` automatically.

## Successful negative outcome

A useful negative result is an exact identity proving that, even after recombination in `(S2)`, an unavoidable zero-frequency response survives with no depth-uniform spatial localization available from the already proved inputs.

If possible, identify the surviving signed measure/operator and prove that the old tail-shift or an equivalent unresolved theorem is genuinely necessary even for `(S5)`.

That would show the common-coupling detour did not merely arise from a bad positive decomposition; it would be a real obstruction in the signed transfer itself.

## What not to do

Do not:

- return to common-uniform global occupation, `G_m`, or `alpha_0`;
- enlarge the two-spin exposure state or add ancestry counters;
- revive finite generator-mode closure;
- integrate trail duration before the modulus;
- split into mass/disagreement and bound the two pieces separately unless the final estimate explicitly recombines them before absolute value;
- launch a general matrix-product or nonlocal norm;
- infer an all-depth theorem from a two-insertion calculation.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/013-signed-two-insertion-recombination.md`

with exact verifier code beside it when finite symbolic/rational identities are used.

End with one of:

- `signed recombination localizes: Gamma_M <= ...`;
- `signed recombination refuted because an unavoidable zero-frequency term ...`;
- `unresolved after substantive work; exact recombination blocker: ...`.
