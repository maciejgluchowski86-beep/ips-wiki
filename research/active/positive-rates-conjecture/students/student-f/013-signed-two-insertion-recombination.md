# Student F 013: signed two-insertion recombination

## Verdict

Assignment 013 asks whether keeping the first centered insertion fully signed through one further zero-boundary segment removes the zero-frequency obstruction created by the earlier mass/disagreement split.

It does **not** remove that obstruction algebraically.

Let

\[
m_0:=Br_0-c,
\qquad r_0=\frac1{1+b},
\]

and define the zero-mass first-insertion defect

\[
\rho_N:=\mathcal J_N\pi_N-m_0\pi_{N-1}.
\tag{0.1}
\]

For

\[
\kappa_{N,u}
=\mathcal J_{N-1}\bigl((\mathcal J_N\pi_N)P_u^{N-1,0}\bigr),
\qquad
a(u)=\kappa_{N,u}(1),
\]

I prove the exact **recombined spectral decomposition**

\[
\boxed{
\begin{aligned}
&\kappa_{N,u}(f)-a(u)\pi_{N-2}(f)\\
&\quad=
m_0\rho_{N-1}(f)
+
\rho_N\!\left(
(P_u^{N-1,0}-\Pi_{N-1})
\left[Y_{N-1}\bigl(f-\pi_{N-2}(f)\bigr)\right]
\right),
\end{aligned}
}
\tag{R}
\]

where

\[
Y_j=B\eta_j-c
\]

and

\[
\Pi_{N-1}h:=\pi_{N-1}(h)\,1
\]

is the zero-frequency invariant projection of the `(N-1)`-site semigroup.

Thus the first term in `(R)` is literally the **zero temporal-frequency component of the full unsplit two-insertion transfer**. It is not introduced by a positive disagreement estimate or by the mass/disagreement decomposition. The second term is the nonzero-frequency/transient complement and tends to zero as `u->infinity` for each fixed finite volume.

The zero-frequency spatial profile is itself explicit:

\[
\boxed{
\rho_n(f)
=m_0\bigl(\bar\pi_n-\pi_{n-1}\bigr)(f)
+B\,\pi_n\bigl[(\eta_n-r_0)f\bigr].
}
\tag{Z}
\]

The second term in `(Z)` is exactly the positive-frequency signed covariance already localized exponentially in F010. Hence, if

\[
\mathcal R_M
:=
\sup_{n\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,n-M\}}}
|\rho_n(f)|,
\]

then

\[
\boxed{
\left|
\mathcal R_M-|m_0|\Delta_M
\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}.
}
\tag{0.2}
\]

In particular, away from the exceptional surface `m_0=0`, the first-insertion zero mode localizes if and only if the old tail-shift defect `Delta_M` localizes.

For the zero-frequency part of the **two-insertion** defect in Assignment 013, the relevant separation is `M+1`, so

\[
\boxed{
\left|
\sup_{N\ge M+2}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
|m_0\rho_{N-1}(f)|
-
|m_0|^2\Delta_{M+1}
\right|
\le
\frac{2|m_0|Bbc}{(1+b)^3(2+b)^M}.
}
\tag{0.3}
\]

So, generically, the full recombined transfer contains `m_0^2` times the old zero-frequency tail-shift response, up to an exponentially localized covariance.

This **does not by itself refute**

\[
\Gamma_M\to0.
\]

The modulus in `Gamma_M` is taken at each duration before `u` is integrated. The transient term in `(R)` may cancel the stationary projection for all durations carrying appreciable `w(u)` mass and relax to zero only on a depth-dependent time scale at which the factor `w(u)` is already small. Turning the spectral projection `(0.3)` into a lower bound on `Gamma_M` would require a new uniform observability/relaxation statement preventing that screening. No such theorem is currently available, and assuming a depth-uniform spectral gap would be circular relative to the programme.

Therefore the exact result of this block is negative at the algebraic level but not a counterexample to `(S5)`:

> full signed recombination does **not** cancel the zero-frequency component; it moves the remaining issue to whether the transient complement can screen that component over the `w`-relevant time window uniformly with spatial depth.

There is one exact exceptional surface. If

\[
m_0=0
\quad\Longleftrightarrow\quad
 a=b(1-c),
\tag{0.4}
\]

then the finite zero-boundary invariant law is exactly the Bernoulli product law with density `r_0`, the first signed insertion vanishes identically,

\[
\mathcal J_N\pi_N=0,
\]

and consequently

\[
\boxed{\Gamma_M=0\qquad\text{for every }M.}
\tag{0.5}
\]

Thus the obstruction is genuinely tied to the nonzero equilibrium mass coefficient `m_0`; along the hard near-East path it is small but nonzero.

The exact finite algebra is checked in

`students/student-f/013-signed-two-insertion-recombination-verifier.py`.

## 1. Setup

Work in the strict residual chamber and write

\[
B=b+c-a,
\qquad g=b-a,
\qquad\omega=1-c+a,
\qquad r_0=\frac1{1+b},
\]

\[
m_0=Br_0-c
=\frac{b(1-c)-a}{1+b}.
\tag{1.1}
\]

On the `N`-site zero-boundary interval let `pi_N` be the unique invariant law and

\[
(\mathcal J_N\mu)(f)=\mu(Y_Nf),
\qquad
Y_N=B\eta_N-c.
\tag{1.2}
\]

Put

\[
\nu_N:=\mathcal J_N\pi_N,
\qquad
\rho_N:=\nu_N-m_0\pi_{N-1}.
\tag{1.3}
\]

Suffix projectivity gives

\[
\nu_N(1)=\pi_N(Y_N)=m_0
\tag{1.4}
\]

for every `N>=1`, so

\[
\rho_N(1)=0.
\tag{1.5}
\]

For `N>=2`, Assignment 013 evolves `nu_N` on the remaining sites and inserts again:

\[
\kappa_{N,u}
:=
\mathcal J_{N-1}(\nu_NP_u^{N-1,0}).
\tag{1.6}
\]

## 2. The scalar mass is independent of volume

The rightmost site of the `(N-1)`-site zero-boundary chain is autonomous, with

\[
0\to1\text{ at rate }1,
\qquad
1\to0\text{ at rate }b.
\]

Hence, writing

\[
\lambda:=1+b,
\]

\[
P_u^{N-1,0}Y_{N-1}
=m_0+B e^{-\lambda u}(\eta_{N-1}-r_0).
\tag{2.1}
\]

Therefore

\[
\begin{aligned}
a_N(u)
&=\nu_N(P_uY_{N-1})\\
&=m_0^2+B C_*e^{-\lambda u},
\end{aligned}
\tag{2.2}
\]

where

\[
C_*
:=\nu_N(\eta_{N-1})-r_0m_0.
\tag{2.3}
\]

By the exact suffix intertwining of F010, the rightmost one-site marginal of `nu_N` is the same as that of `J_2 pi_2`, so `C_*` is independent of `N`. Thus

\[
\boxed{a_N(u)=a(u)}
\tag{2.4}
\]

for all `N>=2`.

For reference, with

\[
S=ab+2a+b^2-bc+2b-2c+2,
\]

direct evaluation of `pi_2` gives

\[
C_*
=
\frac{(a+bc-b)(ab+2a-b^2+bc-2b)}
{(1+b)^2S}.
\tag{2.5}
\]

At

\[
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right),
\]

\[
m_0=-\frac2{65},
\qquad
C_*=-\frac{22}{4563},
\]

and

\[
a(u)
=\frac4{4225}-\frac{22}{4563}e^{-13u/10}.
\tag{2.6}
\]

## 3. Exact recombination identity

Fix `N>=2` and abbreviate

\[
P_u=P_u^{N-1,0},
\qquad
\pi=\pi_{N-1},
\qquad
\pi^-=\pi_{N-2}.
\]

Let `f` be any function on sites `1,...,N-2` and put

\[
\widetilde f=f-\pi^-(f).
\tag{3.1}
\]

Using

\[
\nu_N=m_0\pi+\rho_N
\]

and invariance of `pi` under `P_u`,

\[
\begin{aligned}
\kappa_{N,u}(f)
&=\nu_NP_u(Y_{N-1}f)\\
&=m_0\pi(Y_{N-1}f)
+\rho_NP_u(Y_{N-1}f)\\
&=m_0\left[m_0\pi^-(f)+\rho_{N-1}(f)\right]
+\rho_NP_u(Y_{N-1}f).
\end{aligned}
\tag{3.2}
\]

Likewise

\[
a(u)=m_0^2+\rho_NP_u(Y_{N-1}).
\tag{3.3}
\]

Subtracting `a(u)pi^-(f)` gives

\[
\boxed{
\kappa_{N,u}(f)-a(u)\pi^-(f)
=m_0\rho_{N-1}(f)
+\rho_NP_u(Y_{N-1}\widetilde f).
}
\tag{3.4}
\]

This derivation never splits `nu_N` into a positive mass law and a positive disagreement law. It is an identity for the original signed measure.

Now let

\[
\Pi_{N-1}h:=\pi_{N-1}(h)1.
\]

Since `rho_N(1)=0`,

\[
\rho_N\Pi_{N-1}h=0
\]

for every `h`. Therefore `(3.4)` is exactly

\[
\boxed{
\begin{aligned}
\kappa_{N,u}(f)-a(u)\pi_{N-2}(f)
&=m_0\rho_{N-1}(f)\\
&\quad+
\rho_N(P_u-\Pi_{N-1})
\left[Y_{N-1}\bigl(f-\pi_{N-2}(f)\bigr)\right].
\end{aligned}
}
\tag{3.5}
\]

This is `(R)`.

### Interpretation

The two summands in `(3.5)` are the exact temporal spectral splitting of the recombined object:

- `m_0 rho_{N-1}` is the projection onto the zero eigenvalue of the `(N-1)`-site Markov semigroup;
- the second term lies in the transient complement `P_u-Pi_{N-1}`.

Since every finite zero-boundary chain is irreducible,

\[
P_u-\Pi_{N-1}\longrightarrow0
\qquad(u\to\infty),
\]

and hence, for every fixed `N,f`,

\[
\boxed{
\lim_{u\to\infty}
\left[
\kappa_{N,u}(f)-a(u)\pi_{N-2}(f)
\right]
=m_0\rho_{N-1}(f).
}
\tag{3.6}
\]

Thus recombination does not cancel the zero temporal mode.

## 4. The zero mode contains the old tail-shift response

Let

\[
\bar\pi_n
\]

be the left marginal of `pi_n`, and put

\[
\delta_n:=\bar\pi_n-\pi_{n-1},
\qquad
\phi_n:=\eta_n-r_0.
\]

For any left function `f`,

\[
\begin{aligned}
\rho_n(f)
&=\pi_n(Y_nf)-m_0\pi_{n-1}(f)\\
&=m_0\bar\pi_n(f)
+B\pi_n(\phi_nf)
-m_0\pi_{n-1}(f).
\end{aligned}
\]

Therefore

\[
\boxed{
\rho_n(f)=m_0\delta_n(f)+B\pi_n(\phi_nf).
}
\tag{4.1}
\]

The second term is not an unresolved zero-frequency object. F010 already proves that if

\[
\operatorname{supp}f\subseteq\{1,\ldots,n-M\},
\]

then

\[
\left|
B\pi_n(\phi_nf)
\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
\tag{4.2}
\]

Define

\[
\mathcal R_M
:=
\sup_{n\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,n-M\}}}
|\rho_n(f)|.
\tag{4.3}
\]

The Assignment-011 quantity `Delta_M` is the same operator norm with `rho_n` replaced by `delta_n`. From `(4.1)`--`(4.2)`,

\[
\boxed{
|m_0|\Delta_M-\epsilon_M
\le
\mathcal R_M
\le
|m_0|\Delta_M+\epsilon_M,
}
\tag{4.4}
\]

where

\[
\epsilon_M
:=
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}.
\tag{4.5}
\]

Since `epsilon_M->0`, if `m_0!=0` then

\[
\boxed{
\mathcal R_M\to0
\iff
\Delta_M\to0.
}
\tag{4.6}
\]

For Assignment 013, a remote test satisfies

\[
\operatorname{supp}f
\subseteq\{1,\ldots,N-M-2\}.
\]

Putting `n=N-1` means the zero-mode term has separation `M+1`. Thus its remote operator norm

\[
\mathcal Z_M
:=
\sup_{N\ge M+2}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}f\subseteq\{1,\ldots,N-M-2\}}}
|m_0\rho_{N-1}(f)|
\]

satisfies

\[
\boxed{
\left|
\mathcal Z_M-|m_0|^2\Delta_{M+1}
\right|
\le
\frac{2|m_0|Bbc}{(1+b)^3(2+b)^M}.
}
\tag{4.7}
\]

This is the precise sense in which the old zero-frequency response survives full recombination.

Along the near-East path

\[
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
\]

\[
\boxed{
m_0=-\frac{\varepsilon^2(1-\varepsilon)}{1+\varepsilon}.}
\tag{4.8}
\]

Thus the surviving tail-shift coefficient is order `epsilon^4` after two insertions, but is nonzero at every strict near-East point.

## 5. Why `(4.7)` does not by itself refute `Gamma_M -> 0`

The Assignment-013 norm is

\[
\Gamma_M
=
\sup_N\int_0^\infty
w(u)\,\|E_{N,u}\|_{\rm remote,M}\,du,
\]

where `E_{N,u}` denotes the signed defect in `(3.5)` and the remote norm is the supremum over the allowed `f`.

Equation `(3.5)` has the form

\[
E_{N,u}=Z_N+T_{N,u},
\tag{5.1}
\]

with

\[
Z_N=m_0\rho_{N-1}
\]

independent of `u`, and

\[
T_{N,u}
=\rho_N(P_u-\Pi_{N-1})M_{Y_{N-1}}(I-\pi_{N-2})
\tag{5.2}
\]

the transient complement.

For each fixed finite `N`,

\[
T_{N,u}\to0.
\]

However the time at which this happens may depend arbitrarily on `N`. The current record has no depth-uniform spectral gap or sup-norm mixing theorem.

Therefore the following scenario is not excluded by `(3.5)`:

- on deep systems and for all `u` in the range where `w(u)` has substantial mass, `T_{N,u}` remains close to `-Z_N` on the remote test space;
- only at much later times does `T_{N,u}` relax to zero and reveal `Z_N`;
- the positive factor `w(u)` is then already exponentially small.

Because the modulus is taken **before** duration integration, cancellation between different values of `u` is unavailable, but cancellation between `Z_N` and `T_{N,u}` at the same duration is allowed and is exactly what must now be decided.

To turn `(4.7)` into a lower bound on `Gamma_M` one would need a new uniform observability estimate of the form

\[
\int_0^\infty w(u)
\|Z_N+T_{N,u}\|_{\rm remote,M}\,du
\ge
c_*\|Z_N\|_{\rm remote,M}-o_M(1)
\tag{5.3}
\]

with `c_*>0` independent of depth, or another theorem preventing the transient complement from screening the zero mode throughout the `w`-relevant interval.

No such estimate follows from F010--F012, and proving it by assuming a depth-uniform mixing rate would beg the main question.

Conversely, a positive proof of `Gamma_M->0` without tail-shift agreement would have to establish the opposite quantitative mechanism: **depth-dependent screening**, namely that whenever the zero mode in `(4.7)` is nonlocal, its cancellation by `T_{N,u}` persists until times large enough that `w(u)` suppresses the eventual stationary projection.

This is the exact recombination blocker left by `(R)`.

## 6. Exceptional reversible product surface

Suppose

\[
a=b(1-c).
\tag{6.1}
\]

Then `m_0=0`. Write

\[
k=1-c.
\]

For a right-neighbour spin `y`, the two flip rates satisfy

\[
c(1,y)=b\,c(0,y):
\]

for `y=0`, this is `b=b*1`, and for `y=1`, it is `a=bk` versus `k`.

Let

\[
p=r_0=\frac1{1+b}.
\]

Under Bernoulli product measure `mu_p`, flipping one zero to one multiplies the configuration probability by

\[
\frac{p}{1-p}=\frac1b.
\]

Therefore for every site and every fixed right-neighbour state,

\[
\mu_p(\eta)c_i(\eta)
=
\mu_p(\eta^i)c_i(\eta^i).
\tag{6.2}
\]

So `mu_p` is reversible for every finite zero-boundary chain. By irreducibility,

\[
\boxed{\pi_N=\mu_p^{\otimes N}.}
\tag{6.3}
\]

Moreover

\[
E_{\mu_p}[Y_N]=Bp-c=m_0=0,
\]

and `Y_N` is independent of the left block. Hence

\[
\boxed{\mathcal J_N\pi_N=0}
\tag{6.4}
\]

for every `N`, so

\[
\boxed{
\kappa_{N,u}=0,
\qquad a(u)=0,
\qquad\Gamma_M=0.
}
\tag{6.5}
\]

Thus signed recombination is completely successful on the exact reversible product surface. Off that surface, the zero-frequency mode `(4.7)` is present.

## 7. What this block decides

### Established

1. `a_N(u)` is independent of volume and has the exact two-mode form `(2.2)`.
2. The full unsplit two-insertion defect has the exact spectral decomposition `(R)`.
3. The zero temporal-frequency projection is `m_0 rho_{N-1}`.
4. Its nonlocal part is `m_0^2 delta_{N-1}` up to the already proved exponentially local signed covariance.
5. Away from `m_0=0`, localization of the zero spectral projection is equivalent to tail-shift localization.
6. On `a=b(1-c)`, the invariant law is exactly reversible product Bernoulli and the entire signed insertion vanishes.

### Not established

- `Gamma_M->0` or its failure off the product surface;
- tail-shift agreement;
- a depth-uniform observability lower bound for the zero mode;
- depth-dependent screening of the zero mode by the transient complement;
- any three-insertion or arbitrary-depth signed theorem;
- decay of `J_{x,r}`.

The central conclusion is that the zero-frequency problem was **not merely an artifact of splitting the signed insertion into positive pieces**. It is an actual spectral component of the recombined two-insertion transfer. What remains open is whether the `w`-weighted norm can hide that component through depth-dependent transient screening.

## Handoff

`unresolved after substantive work; exact recombination blocker: the full signed two-insertion defect has the exact spectral decomposition E_{N,u}=m_0 rho_{N-1}+rho_N(P_u-Pi)[Y_{N-1}(f-pi_{N-2}f)]. The first term is the genuine zero temporal-frequency projection and survives before any mass/disagreement split. Moreover rho_n=m_0(bar pi_n-pi_{n-1})+B pi_n[(eta_n-r_0)·], so its remote norm differs from |m_0| Delta_M only by F010's exponentially localized covariance; the two-insertion zero mode therefore differs from |m_0|^2 Delta_{M+1} by O((2+b)^(-M)). On the exceptional surface a=b(1-c), m_0=0, pi_N is product Bernoulli and Gamma_M=0 identically. Off that surface Gamma_M itself remains undecided because the transient complement may screen the zero mode throughout the w-relevant time window and reveal it only on a depth-dependent relaxation scale. Proving or excluding that screening is the exact remaining two-insertion question.`
