# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The scientific target is fixed by the principal. Proof routes may be abandoned; the target does not change.

## E0. Source reduction

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The source-corrected unresolved chamber is

$$
\boxed{
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
}
$$

The fixed-wall route and the cellwise scaffold-positivity route are closed.

## E1. Direct dynamics retained for reuse

Student G's transient identities and Student F's coupling work remain established technical inputs. In particular,

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11),
$$

and, for coupled disagreement indicator `D_i` and high-risk state `J_i`,

$$
\mathcal L^{\rm coup}D_i
\le
-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i.
$$

Every disagreement site has predictable coalescence intensity at least

$$
q:=1-c+a>0.
$$

This gives true one- and two-generation regeneration and positive finite-depth ordered-clearing events. The certified depth-dependent clearing gaps are summable, so these facts do not themselves prove arbitrary-depth extinction.

**Status:** live-disagreement route paused, not closed. No further finite-generation escalation.

## E2. Closed cellwise scaffold mechanism

Earlier reconstruction of the principal's old last-exit idea showed that one-cell regional integration is positive, but when the predecessor interaction is itself hidden the exact transfer is

$$
\Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c,
$$

and `Psi_Delta(0)<0` for all sufficiently short positive `Delta` at every residual parameter point.

**Status:** the mechanism "hide one interaction type, integrate one cell, iterate nonnegative transfers cell by cell" is closed.

This does **not** close the new centered predecessor-trail route below, because that route allows signs and only asks for contraction after the full left-region invariant expectation is formed.

## E3. Centered dual residual algebra

Use the normalized centered character

$$
H_p(A,\eta)=\prod_{i\in A} h_p(\eta_i),
\qquad
h_p(u)=\frac{u-p}{1-p}.
$$

For the residual normalized family define

$$
B=b+c-a,
\qquad
p_*=\rho=\frac cB,
\qquad
q_* = \frac{b-a}{B},
\qquad
\omega=1-c+a.
$$

The centered dual coefficients specialize to

$$
\boxed{
\beta=B,
\qquad
\lambda=0,
\qquad
\delta_* = \frac{b(1-c)-a}{b-a}.
}
$$

When `delta_*<0`, use the signed-death convention with jump rate `|delta_*|`. The vertical no-death factor and FK potential still combine to

$$
\boxed{e^{-\omega\tau}.}
$$

**Status:** Professor algebra check passed. The complete Poisson-Mecke factorization remains a working lemma pending Student F's independent reconstruction.

## E4. Canonical predecessor trail and exact nonempty-exit factorization

For a finite interval `R=[ell,r]` and initial dual set `A subset R`, define `tau_R(t)` using **every** active successful birth/jump crossing, including refresh coin zero. On `{tau_R(t)>0}`, recursively choose the final relevant exit and then the last relevant predecessor entering each current trail site.

The root `x in A` determines the trail depth exactly:

$$
n_x=r-x+1.
$$

Conditional on the decorated trail, spacetime splits into left region, trail, and right region using disjoint Poisson families. In the residual family every selected trail interaction is a birth. The principal exploration gives

$$
\boxed{
E_A[W_t^\eta;\tau_R(t)>0]
=
\sum_{x\in A}B(b-a)^{n_x-1}
\int_{\Delta_{n_x}(t)}
 e^{-\omega t_{n_x}}
 L_\gamma(\eta)
 [\rho U_{\gamma,0}(\eta)+q_*U_{\gamma,1}(\eta)]\,dt.
}
\tag{13'}
$$

**Status:** accepted as active working reduction; Student F Assignment 006 must independently audit uniqueness, conditioning, signed-death treatment, and the complementary no-exit term before this becomes a closing lemma.

## E5. Right region is uniformly bounded

Average the final refresh coin before taking absolute values. The resulting right-region operator is a composition of sup-norm contractions: Markov semigroups, projections, sub-Markov killed semigroups, and multiplication by a spin.

Hence for fixed initial monomial `A`,

$$
\boxed{
\sup_{\gamma,t,\eta}|R_{\gamma,t}(\eta)|\le C_A,
}
\tag{R}
$$

with `C_A` independent of interval length and trail depth.

**Status:** Professor-checked operator bound. No right-region mixing theorem is needed.

## E6. Left finite-volume relaxation reduces the problem to invariant trail observables

Let `m=min A`, write trail gaps as `u=(u_1,...,u_n)`, total trail duration `|u|`, and lag after the final exit as

$$
s=t-|u|.
$$

The left contribution is

$$
L_{\gamma,t}=P_s^{<r+1,0}F_{x,u},
$$

where `F_{x,u}` is formed by alternating zero-boundary semigroups with centered multiplications at successive trail sites.

For fixed `R`, the finite zero-boundary chain on `[m,r]` is irreducible at every strict residual parameter point, so

$$
P_s^{[m,r],0}F\to \pi^0_{m,r}(F)
$$

uniformly in initial state as `s to infinity`.

The recent-exit part `s<T_R` has `|u|>t-T_R`. Since

$$
\omega=1-c+a>0,
$$

its fixed-depth simplex mass vanishes exponentially in `t`. Combining this with E5 yields the all-depth nonempty-trail criterion

$$
\boxed{
B(b-a)^{n-1}
\int_{(0,\infty)^n}
 e^{-\omega|u|}
 |\pi^0_{m,r}(F_{x,u})|\,du
\longrightarrow0,
\qquad n=r-x+1\to\infty.
}
\tag{L}
$$

**Status:** Professor checked the reduction from finite-volume relaxation to (L), conditional on E4. The complementary `tau_R(t)=0` contribution must be reconstructed explicitly before claiming that (L) alone closes ergodicity.

## E7. Exact East cancellation and near-East one-level scale

For the exact East heat-bath model with zero facilitating boundary, the finite-volume invariant law is product Bernoulli. The final trail event is a birth, so

$$
F_{x,u}=h_{p_*}(\eta_r)G_{x,u}(\eta_{<r}),
$$

and therefore

$$
\boxed{\pi^0_{m,r}(F_{x,u})=0.}
$$

The equilibrium trail contribution at East is exactly zero. The exact East point has `omega=0`, so it is only a structural limiting case for the strict positive-rate proof.

Along

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

the one-site constant-mode Laplace factor is

$$
\boxed{
\frac{b-a}{\omega}
|\pi^0_{\{r\}}(h_{p_*})|
=
\frac{1-\varepsilon}{2(1+\varepsilon)}<\frac12.
}
$$

**Status:** structural evidence that an all-depth centered contraction has the correct near-East scale at one level.

## E8. Sufficient centered-transfer theorem

For a trail-generated signed measure `nu` on sites through `y`, define

$$
(\mathcal C_{y,u}\nu)(f)
=
\nu(h_{p_*}(\eta_y)P_u^{<y,0}f),
\qquad f=f(\eta_{<y}).
$$

A sufficient all-depth theorem is the existence of norms on the generated class and `theta<1` such that

$$
\boxed{
(b-a)\int_0^\infty e^{-\omega u}
\|\mathcal C_{y,u}\nu\|_{*,y-1}\,du
\le
\theta\|\nu\|_{*,y}
}
\tag{T}
$$

uniformly in interval and depth, together with uniform starting/final functional control. Iteration gives exponential decay in (L).

Total variation on all signed measures cannot work because multiplication by `h_{p_*}` has size `1/q_*`. The norm must retain centering cancellation and only needs to control the generated signed-measure class.

The principal exploration reports that the two-level scalar invariant integrand changes sign as the inter-trail time varies. That latest sign-change claim is not yet independently verified. If true, it rules out pointwise positivity and simple scalar sign iteration, but does not rule out (T).

## E9. Relation to the live-coupling line

The same positive-rate scale appears in both routes:

$$
\boxed{q=\omega=1-c+a.}
$$

In the coupling it is a universal disagreement coalescence floor. In the predecessor-trail formula it is the exponential penalty for long trails. No automatic implication between the routes is asserted.

A productive bridge would be an actual inequality from the coupling to zero-boundary invariant sensitivity/correlation bounds strong enough to control `\mathcal C_{y,u}`. Without such an inequality, merely noting the shared parameter does not count as progress.

## E10. Current load-bearing edge: audit and prove/kill (L)/(T)

Student F Assignment 006 must:

1. independently audit E3--E6, including the `tau_R=0` complement;
2. reproduce the reported two-level sign change before using it;
3. prove (T), prove (L) by another all-depth mechanism, or produce a rigorous obstruction to a materially specified signed-transfer norm/spectral mechanism.

Finite-level calculations count only when they prove or falsify an all-depth mechanism. Do not return to cellwise positivity or deeper live-generation enumeration.

Student G remains on Assignment 002 and will be folded in on return.

## Anti-circularity checkpoint

Meeting 005 changes the all-depth object from the full disagreement ancestry stack to the narrower family of invariant centered trail observables produced by an exact predecessor decomposition. The right region and post-exit relaxation are no longer active obstacles. The remaining work is one explicit all-depth signed-transfer estimate.

## Current direction

Attack E10 while preserving the fixed positive-rates target.
