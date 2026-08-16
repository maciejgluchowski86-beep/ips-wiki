# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** The Professor may close or redirect proof routes but does not pivot to another scientific problem.

Target:

> Every simple one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with source-corrected residual chamber

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Latest meeting: `meetings/005-principal-trail-reduction-and-all-depth-transfer.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-006.md`, independent audit and all-depth centered predecessor-trail transfer;
- Student G: still finishing `students/student-g/assignment-002.md`; its independent return will be folded into the next meeting.

Student F Assignment 005 is superseded. Preserve any mathematics already obtained there, but the all-depth live-disagreement search is paused while the sharper centered-transfer reduction is tested.

## Closed proof routes

The following mechanisms are closed and must not be revived by finite-size escalation:

1. fixed finite agreed-block / frozen-exterior wall crossing;
2. cellwise last-exit/scaffold insertion positivity, which fails at two-cell composition.

The new predecessor-trail route is not item 2: it permits signs, integrates the full left region to its zero-boundary invariant expectation, and asks for all-depth contraction only after that integration.

## Reusable direct coupling mathematics

Student G proved on the original normalized dynamics the transport--dissipation identity

$$
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
$$

plus boundary-uniform transient zero-density, finite-box concentration, and adjacent-`11` suppression

$$
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
$$

Student F proved

$$
\mathcal L^{\rm coup}D_i
\le
-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i,
$$

and the structural fact that every disagreement site has predictable coalescence intensity at least

$$
q:=1-c+a>0.
$$

This yields true one- and two-generation regeneration events and finite-depth ordered clearing. The certified depth-`m` clearing gaps decay like powers of `q/(1+q)` and are summable, so those results do not by themselves give an all-depth disagreement contraction.

The live-disagreement route is **paused, not closed**. Its coalescence and drift lemmas remain reusable, especially if they can control zero-boundary invariant correlations.

## Meeting 005: exact centered predecessor-trail reduction

The principal supplied a separate centered-monomial exploration, now recorded in

`notes/principal-centered-trail-reduction.md`.

For the residual centered dual put

$$
B=b+c-a,
\qquad
p_*=\rho=\frac cB,
\qquad
q_* = \frac{b-a}{B},
\qquad
\omega=1-c+a.
$$

On the event that an active successful interaction exits a finite interval `R=[ell,r]`, the canonical predecessor trail has root `x in A`, depth

$$
n=r-x+1,
$$

and positive vertical factor

$$
\boxed{e^{-\omega\tau_R(t)}}.
$$

In the residual centered dual the selected trail interactions are births (`beta=B`, `lambda=0`). The nonempty-trail contribution factors into left, trail, and right regions. After the final refresh coin is averaged before absolute values, the right contribution obeys

$$
\boxed{
\sup_{\gamma,t,\eta}|R_{\gamma,t}(\eta)|\le C_A,
}
$$

with `C_A` independent of `R` and trail depth.

For fixed `R`, the left region is an original finite-volume spin system with zero right boundary after the final trail time. It relaxes uniformly to its invariant law `pi^0_{m,r}`. Because `omega>0`, trails whose final exit occurs within a fixed `R`-dependent burn-in window of time `t` have exponentially vanishing mass as `t to infinity`.

The resulting all-depth criterion for the nonempty-trail term is

$$
\boxed{
B(b-a)^{n-1}
\int_{(0,\infty)^n}
 e^{-\omega|u|}
 |\pi^0_{m,r}(F_{x,u})|\,du
\longrightarrow0
\qquad(n=r-x+1\to\infty).
}
\tag{L}
$$

The complementary no-exit term still has to be checked explicitly in the reconstructed proof; it must not be silently omitted.

## Sufficient all-depth centered-transfer theorem

For a trail-generated signed measure `nu`, define

$$
(\mathcal C_{y,u}\nu)(f)
=
\nu(h_{p_*}(\eta_y)P_u^{<y,0}f).
$$

A sufficient structural estimate is a norm on the generated class and a parameter-point constant `theta<1` such that

$$
\boxed{
(b-a)\int_0^\infty e^{-\omega u}
\|\mathcal C_{y,u}\nu\|_{*,y-1}\,du
\le
\theta\|\nu\|_{*,y}
}
\tag{T}
$$

uniformly in interval and depth. Iteration would imply exponential spatial decay in (L).

Total variation on all signed measures is not suitable because multiplication by the centered character has size `1/q_*`; the norm must retain centering cancellation.

At exact East with zero facilitating boundary, the relevant finite-volume invariant law is product Bernoulli and the final trail birth inserts a centered character independent of the preceding factor. Therefore the invariant trail contribution is **exactly zero**. Along the strict near-East path

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

the one-site constant-mode Laplace factor is

$$
\frac{1-\varepsilon}{2(1+\varepsilon)}<\frac12.
$$

The principal exploration reports that the two-level scalar invariant integrand changes sign as an inter-trail time varies. That latest sign-change claim was not accompanied by its exact formula in the capture and is **not yet independently verified**. Student F must reproduce it before using it. If correct, it rules out pointwise positivity / scalar sign iteration but not signed-measure contraction of type (T).

## Relation of the two all-depth routes

The live-coupling coalescence rate and the trail decay rate are the same parameter:

$$
\boxed{q=\omega=1-c+a.}
$$

This is structurally suggestive but not yet a theorem connecting the routes. In the coupling, `q` is a universal local coalescence floor. In the trail decomposition, `omega` is the exponential penalty for long predecessor trails. A legitimate future bridge would need an actual inequality from coupling to zero-boundary invariant correlations or transfer norms.

## Current bottleneck

The active proof target is now (L), preferably through (T), after an independent audit of the exact predecessor-trail factorization and the complementary no-exit term.

Student F must handle arbitrary depth structurally; finite-level calculations count only if they prove or falsify a specific all-depth norm / spectral-radius mechanism.

## Anti-circularity rule

Do not return to cellwise positivity, deeper live-generation enumeration, or generic finite-volume mixing. The next accepted progress must either prove the centered all-depth contraction / criterion, expose a false step in the trail reduction, or produce a rigorous obstruction to a materially specified signed-transfer mechanism.

## Wiki

Keep the live wiki frozen during research.
