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

Latest meeting: `meetings/009-regenerated-mass-loss-and-duration-mode-obstruction.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-009.md`, mode-resolved `L^1(w)` block operator retaining mass relaxation/reset-history modes;
- Student G: still in flight on `students/student-g/assignment-004.md`, global restart-corrector Foster lift.

## Closed mechanisms / corrections

1. Fixed finite agreed-block / frozen-exterior wall crossing.
2. Cellwise last-exit/scaffold insertion positivity.
3. Meeting 005 one-generation centered-transfer contraction `(T)`: exact near-East depth-two ratios tend to `3/2` without right killing and `7/5` with it.
4. The crude condition `max{c,b-a}Z<1` contributes no residual subregion: throughout `\mathcal R`, `c>b-a` and `cZ>1`.

The canonical predecessor-trail decomposition remains active.

## Global trail target

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
$$

and let

$$
w(u)=e^{-\omega u}s_1(u),
\qquad
Z=\int_0^\infty w(u)du
=\frac{a+b+2}{a(2b+3)+(1-c)(b+2)}.
$$

The nonempty-exit term is controlled by

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Showing `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. The exact Poisson--Mecke trail factorization and the complementary no-exit term still require independent audit before a closing proof.

## Exact mass/disagreement decomposition

Each centered insertion splits as

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The first term is signed mass; the second is a positive conditional-law disagreement channel.

## Student G: accepted restart inputs

For one fixed parent disagreement, the number `N` of exposure re-entries before that parent first coalesces satisfies

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1},
$$

and hence has the explicit exponential pgf bound

$$
E[s^N\mid\mathcal F]\le\frac{(1-h_1)s}{1-h_1s}.
$$

The stack-height minorant gives an exponential height factor `phi(lambda)<1`; near East the scalar restart/height stress factor can be chosen to tend to `16/21<1`.

What remains unverified is G's global product/phase Foster lift over all parent levels. Assignment 004 is still in flight.

## Student F Assignment 008: uniform regenerated-mass loss

For the one-site zero-boundary equilibrium density

$$
r_0=\frac1{1+b},
$$

Student F proves, and the Professor checks,

$$
\boxed{
|Br_0-c|Z<\frac23
}
$$

at every strict residual parameter point.

Thus a mass component genuinely returned to the equilibrium mode has a uniform right-weighted scalar loss. This is independent of G's Foster premise.

## New structural obstruction: duration modes cannot be integrated before the norm

A mass branch need not be in the equilibrium mode. Its current rightmost density evolves as

$$
r(u)=r_0+(r-r_0)e^{-(1+b)u},
$$

so it carries a nontrivial mass-relaxation mode.

Near East, for the exact depth-two invariant profile `A_{2,epsilon}(u)`,

$$
\frac g{|m_\varepsilon|}
\left|\int_0^\infty w(u)A_{2,\varepsilon}(u)du\right|
\to\frac35<1,
$$

whereas the quantity actually appearing in `J_{x,r}` obeys

$$
\boxed{
\frac g{|m_\varepsilon|}
\int_0^\infty w(u)|A_{2,\varepsilon}(u)|du
\to\frac75>1.
}
$$

Therefore a proof may use signed cancellation at fixed duration profile, but may not manufacture cancellation by integrating duration before taking the block norm.

F's fully-regenerated height-one signed matrix has strong local cancellation, with spectral radius tending to `sqrt(2/5)` near East, but it is not iterable as the true block kernel because it has already averaged duration.

## Static spin words do not close the bounded state

At `(a,b,c)=(1/10,3/10,4/5)`, F gives exact nonzero conditional-independence determinants proving that the zero-boundary invariant spatial law is neither first- nor second-order Markov. Thus current spin or a short static spin word cannot supply exact bounded-state closure.

This does not rule out a finite temporal reset-history / generator-mode state.

## Current bottleneck

The block route now has two interfaces.

1. **G:** prove or refute a global finite restart/Foster phase state for arbitrary disagreement height.
2. **F:** build the corresponding **mode-resolved `L^1(w)` signed block operator**, retaining mass relaxation/reset-history modes until the norm is taken. The new equilibrium mass loss `<2/3` is the regenerative anchor.

A scalar Foster return statement alone is insufficient to determine the signed bounded kernel; the return state must preserve enough mass/reset information to reconstruct the signed profile.

If both interfaces close, combine them to prove `J_{x,r}->0`; only then reconstruct the full trail/no-exit convergence implication.

## Anti-circularity rule

Do not integrate duration before the absolute-value norm, iterate the diagnostic `K^(1)` matrix as the proof kernel, replace the invariant law by a short static Markov approximation, return to one-step `(T)`, or replace the disagreement channel by unrestricted total variation.

## Wiki

Keep the live wiki frozen during research.
