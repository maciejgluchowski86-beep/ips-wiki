# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Latest meeting: `meetings/006-one-step-transfer-refuted-block-stack-target.md`, `state_narrowed: yes`.

Active work:

- Student F: **Assignment 006 is superseded immediately** by `students/student-f/assignment-007.md`, block contraction of the trail-generated mass/disagreement stack;
- Student G: still finishing `students/student-g/assignment-002.md`; do not interrupt it.

## Closed proof mechanisms

1. Fixed finite agreed-block / frozen-exterior wall crossing.
2. Cellwise last-exit/scaffold insertion positivity: one-cell regional integration works, but two-cell hidden transfer changes sign on short cells.
3. **Meeting 005 one-generation centered-transfer contraction `(T)`.** The principal's continued calculation gives an exact near-East depth-two obstruction with absolute-value ratio tending to `3/2` without the improved right factor and `7/5` with it. Therefore no one-step `L^1` norm of that form can be the all-depth theorem.

The canonical predecessor-trail decomposition itself remains active.

## Reusable direct coupling mathematics

Student F proved for the common-uniform coupling that every disagreement site has predictable coalescence intensity at least

$$
q=1-c+a>0,
$$

regardless of orientation and of the right-neighbour pair state. This gives genuine one- and two-generation regeneration and positive finite-depth clearing events. The crude finite-depth clearing gaps are summable and do not themselves yield all-depth extinction.

Student F also proved

$$
\mathcal L^{\rm coup}D_i
\le
-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i.
$$

Student G proved direct transient zero-density / finite-box concentration and adjacent-`11` suppression. These remain available inputs.

## Canonical centered predecessor trail

Durable notes:

- `notes/principal-centered-trail-reduction.md`;
- `notes/principal-centered-trail-update2.md`.

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The principal's exact working reduction decomposes a nonempty-exit centered-dual history into left region, canonical predecessor trail, and right region. The selected residual trail interactions are births and the complete trail factor is

$$
\boxed{e^{-\omega\tau}}.
$$

The full Poisson-Mecke factorization remains a working lemma pending independent audit before any closing proof.

## Stronger segmentwise right-region control

The right contribution admits a product survival bound

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_{k=1}^n s_1(u_k),
$$

where `s_1` is survival of an explicit killed two-state chain. Define

$$
w(u)=e^{-\omega u}s_1(u),
$$

and

$$
Z=\int_0^\infty w(u)\,du
=\frac{\omega+1+B+a}{(\omega+a)(\omega+1+B)-a}.
$$

A direct sup-norm argument proves trail decay on the genuine parameter subregion

$$
\boxed{\max\{c,g\}Z<1.}
$$

This subregion does not reach the difficult near-East regime.

## Exact depth-two obstruction to Meeting 005 target

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

let

$$
m_\varepsilon=-\frac{\varepsilon}{1+\varepsilon},
$$

and

$$
M_{2,\varepsilon}
=\frac{(1+\varepsilon)(2\varepsilon-1)}{2\varepsilon^2+5\varepsilon+1}.
$$

The exact depth-two invariant scalar

$$
A_{2,\varepsilon}(u)
=m_\varepsilon^2
+e^{-(1+\varepsilon)u}(M_{2,\varepsilon}-m_\varepsilon^2)
$$

changes sign. The principal capture gives, and the Professor independently checked,

$$
\frac{g}{|m_\varepsilon|}\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|\,du\to\frac32,
$$

and

$$
\frac{g}{|m_\varepsilon|}\int_0^\infty w(u)|A_{2,\varepsilon}(u)|\,du\to\frac75.
$$

Thus one-step pointwise positivity, left-only one-step `L^1` contraction, and one-step contraction using only segmentwise right killing are all false near East.

## Correct all-depth sufficient quantity

The right-weighted invariant quantity is

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_{k=1}^n w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|\,du.
}
$$

The trail reduction gives

$$
\limsup_{t\to\infty}\sup_\eta |D_R(t,\eta)|
\le C_A\sum_{x\in A}J_{x,r}.
$$

Hence `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. The complementary no-exit term must still be audited in the full convergence reconstruction.

## Mass/disagreement decomposition

For a law `mu` whose rightmost spin has density `r`, left marginal `bar mu`, and conditional left laws `mu^1,mu^0`, the centered insertion obeys

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f).
}
$$

This is now the key structural identity. It separates a signed mass channel from a positive disagreement channel. Near East, the equilibrium mass coefficient is order `epsilon^2`, the disagreement coefficient is order `epsilon`, and the right-weighted equilibrium mass multiplier tends to

$$
\frac25.
$$

Taking unrestricted total variation of the disagreement channel loses the required cancellation and reproduces the depth-two expansion.

## Disagreement-stack drift inside the trail route

The principal's reset coupling for the conditional-law difference gives a number `K` of consecutive unresolved levels removed during one zero-boundary segment with

$$
\mathbb P(K\ge j)
\ge
\frac{B+\omega}{B+2\omega}2^{-(j-1)}.
$$

Hence

$$
\mathbb EK\ge\frac{2(B+\omega)}{B+2\omega}>1.
$$

If one transfer adds at most one unresolved level,

$$
H'\le(H-K)_+ +1,
$$

so stack height has strict negative drift for large `H`.

This makes Student F's live-coupling work directly relevant to the trail proof. However, stack-height recurrence alone does not control signed mass branching.

## Current bottleneck: block mass/disagreement contraction

The active target is a **parameter-dependent block contraction**, not a one-step transfer norm.

Seek a norm on trail-generated decompositions into signed mass components and coupled disagreement pairs, weighted by unresolved stack height, and constants

$$
m_0<\infty,\qquad \theta<1
$$

such that the complete right-weighted transfer satisfies

$$
\boxed{\|T^{m_0}\nu\|_*\le\theta\|\nu\|_*.}
$$

The unresolved point is controlling repeated branching into `bar mu` and `mu^1-mu^0` without falling back on total variation.

## Anti-circularity rule

Do not attempt to rescue one-step `(T)`, return to cellwise positivity, or enumerate finite trail depths as a substitute for an all-depth theorem. The next accepted progress must prove the block mass/disagreement contraction, prove `J->0` by another structural mechanism, expose a false step in the trail reduction/update, or give a rigorous all-depth obstruction.

## Wiki

Keep the live wiki frozen during research.
