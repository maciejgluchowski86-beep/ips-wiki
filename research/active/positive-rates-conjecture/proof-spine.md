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

**Meeting 021 additionally records the current centered predecessor-trail/profile implementation as exhausted.** The reduction itself remains valid mathematics, but no further local composition variant is active.

## E1. Predecessor-trail criterion retained

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

**Status after Meeting 021:** target retained, present implementation exhausted.

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

Near East, integrating a trail duration before absolute value produces an apparent factor `3/5`, while the correct `L^1(w)` factor tends to `7/5`. Cancellation between different duration values is unavailable.

## E4. Surviving one-segment damping

Let `r_0=1/(1+b)`. Accepted strict losses remain

$$
|Br_0-c|Z<\frac23,
\qquad
BZ_{\omega+1+b}<1.
$$

The exact signed transfer is operator-valued, and fixed depth-uniform finite linear mode closure is impossible.

## E5. Suffix projectivity and fixed-suffix localization

Rightmost suffixes are autonomous and

$$
R_{N,M}\pi_N=\pi_M.
$$

F010 gives the one-site positive-frequency covariance estimate. F014 strengthens the reusable part: for every centered observable `h` of the **fixed rightmost two-site suffix** and every remote `f`,

$$
\boxed{
|\pi_N(hf)|
\le
6\|h\|_\infty\|f\|_\infty e^{-\gamma_*M},
}
$$

where

$$
\gamma_*
=\min\left\{\frac\omega8,\log4-\frac34\right\}>0.
$$

This uses only neighbour-independent resets of the fixed suffix plus finite propagation; it is not a depth-uniform full-chain mixing theorem.

## E6. One-step zero-frequency tail shift

F011 identifies the split mass defect with

$$
\Delta_M
=\|\theta\mu-\mu\|_{\mathcal F_{M-1}}
$$

for the projective half-line zero-boundary law `mu`. F012 gives the sufficient common-coupling bound

$$
\Delta_M\le2c\int_0^\infty\beta_{M-1}(t)dt.
$$

These remain valid. The global common-uniform occupation route to the right side was stopped in Meeting 019.

## E7. F013: exact recombined spectral decomposition

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

Also

$$
\rho_n(f)
=m_0(\bar\pi_n-\pi_{n-1})(f)
+B\pi_n[(\eta_n-r_0)f].
$$

The covariance term is exponentially local, so the zero mode contains the old tail-shift defect off `m_0=0`.

On `a=b(1-c)`, `m_0=0`, the zero-boundary invariant law is Bernoulli product and the signed insertion vanishes.

## E8. Meeting 020 late-time reduction

Define

$$
\Gamma_M
=\sup_N\int_0^\infty w(u)\|E_{N,u}\|_{\mathrm{remote},M}du.
$$

Since

$$
0\le w(u)\le e^{-\omega u},
\qquad
\|E_{N,u}\|_{TV}\le2c^2,
$$

for every `alpha>0`,

$$
\int_{\alpha M}^\infty
w(u)\|E_{N,u}\|_{\mathrm{remote},M}du
\le
\frac{2c^2}{\omega}e^{-\omega\alpha M}.
$$

Thus only short-time screening needed testing; generic long-time mixing was unnecessary.

## E9. F014 static obstruction: two-step tail shift

Put

$$
H_N=Y_NY_{N-1},
\qquad
h_*=\pi_2(H_2),
\qquad
\delta_N^{(2)}=\bar{\bar\pi}_N-\pi_{N-2}.
$$

F014 proves the exact identity

$$
\boxed{
E_{N,0}(f)
=\pi_N[(H_N-h_*)f]
+h_*\delta_N^{(2)}(f).
}
$$

The first term is exponentially localized by E5. At

$$
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right),
$$

$$
\boxed{h_*=-\frac{34}{8775}\ne0.}
$$

Define the remote norm

$$
\Delta_M^{(2)}
:=\sup_N\|\delta_N^{(2)}\|_{\mathrm{remote},M}.
$$

Then

$$
\boxed{
\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal F_M}.
}
$$

Consequently the static remote norm `S_M` of `E_{N,0}` obeys

$$
\boxed{
\left|S_M-|h_*|\Delta_M^{(2)}\right|
\le12c^2e^{-\gamma_*M}.
}
$$

Thus fixed-suffix localization alone cannot prove the requested static screening off the product surface.

## E10. F014 positive-time light-cone normal form

Cut the influence of site `N-1` into the left `(N-2)`-site block. For every `1<=d<=M`, F014 constructs a bounded test `q` still separated by `M-d` from the right suffix such that

$$
\boxed{
\begin{aligned}
\left|E_{N,u}(f)-a(u)\delta_N^{(2)}(q)\right|
\le{}&12c^2e^{-\gamma_*(M-d)}\\
&+8c^2P(\operatorname{Pois}(u)\ge d)\\
&+2c^2P(\operatorname{Pois}(u)\ge M+1).
\end{aligned}}
$$

Choosing `d=floor(M/2)` and `u<=M/8` makes the whole remainder exponentially small. Therefore the no-crossing/light-cone calculation succeeds except for the pre-existing spatial law `delta_N^(2)`.

Combining with E8 gives constants `C,gamma>0` such that

$$
\boxed{
\Gamma_M
\le
c^2 Z\,\Delta_{\lceil M/2\rceil}^{(2)}
+Ce^{-\gamma M}.
}
$$

Two-step tail-shift agreement would therefore imply two-insertion localization, but it is an additional zero-frequency spatial theorem rather than a finite-propagation consequence.

## E11. Stop decision for the current implementation

Meeting 020 pre-registered the following stopping case: if fixed-suffix localization and finite propagation leave a nonlocal zero-frequency boundary law, or F014 returns unresolved without a sharper mechanism, record the current predecessor-trail/profile implementation as exhausted.

F014 lands exactly in that case.

**Decision:**

- no F015 third-insertion or generic observability continuation;
- no matrix-product/nonlocal-norm search as a default continuation;
- no reopened common-uniform occupation / larger exposure state;
- students F and G idle;
- current predecessor-trail/profile implementation exhausted.

This is an expected-value route stop, not a refutation of `J` decay or of every possible predecessor-trail representation.

## E12. Current structural fork: genuinely different architecture required

Before another internal block, outside consultation 002 must assess whether a **genuinely different** architecture exists. Candidate categories are:

1. a direct spatial stationary-law mechanism exploiting one-sided suffix projectivity without assuming dynamical mixing;
2. a disagreement/information-percolation representation not equivalent to common-uniform global occupation;
3. a different dual/transform/density-profile representation not reducible to the present `J`, scalar Foster classes, or finite mode closure.

A proposal to prove `Delta_M` or `Delta_M^(2)` counts as new only if it supplies an independent structural mechanism specific to the stationary law.

Consultant brief: `consultants/assignment-002-post-trail-architecture-review.md`.

## E13. Final reconstruction after any future `J->0`

If some future architecture returns to the predecessor-trail reduction and proves `J_{x,r}->0`, only then audit Poisson--Mecke factorization, the no-exit complement, and the final convergence-to-ergodicity implication.

## Anti-circularity checkpoint

Do not integrate duration before absolute value; revive closed scalar Foster classes; enlarge finite common-mass modes; infer extinction from fixed-site coupling/front speed; infer survival from finite-time Hamming expansion; treat fixed-suffix mixing as tail-shift mixing; or continue the exhausted implementation by merely moving the same zero-frequency law into a larger state space.
