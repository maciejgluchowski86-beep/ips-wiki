# Group meeting 006: one-step centered transfer is refuted; target becomes block mass/disagreement contraction

Date: 2026-08-16

Professor review of:

- principal's third centered-trail exploration answer, supplied as rendered-text capture and recorded in `notes/principal-centered-trail-update2.md`;
- Meeting 005 and the then-active one-generation transfer target `(T)`;
- Meeting 004 and Student F's live-disagreement coupling results, especially the all-site coalescence lower hazard;
- the current trail decomposition and right/left factorization.

Student G is still working on Assignment 002 and is not interrupted.

state_narrowed: yes

Evidence pointer: `notes/principal-centered-trail-update2.md`, especially Sections 1--6.

## Urgent correction to Meeting 005

Meeting 005 adopted as a sufficient target a one-generation centered signed-measure contraction

$$
(b-a)\int_0^\infty e^{-\omega u}
\|\mathcal C_{y,u}\nu\|_{*,y-1}\,du
\le\theta\|\nu\|_{*,y},\qquad \theta<1.
\tag{T}
$$

The principal's continued calculation has now produced an **exact depth-two obstruction** to that target near the East boundary. Assignment 006 is therefore superseded immediately. Student F must not spend the current block trying to prove `(T)`.

The trail decomposition itself is not refuted.

## Professor checks of the new load-bearing claims

Use

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

### Segmentwise right killing

The killed two-state comparison gives a right-region survival factor `s_1(u)` on each segment and hence

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_{k=1}^n s_1(u_k).
$$

With

$$
w(u)=e^{-\omega u}s_1(u),
$$

its integral is

$$
Z=\int_0^\infty w(u)\,du
=\frac{\omega+1+B+a}{(\omega+a)(\omega+1+B)-a}.
$$

The direct sup-norm estimate indeed yields exponential depth decay whenever

$$
\boxed{\max\{c,g\}Z<1.}
$$

Thus the trail method already proves a genuine parameter subregion. This condition excludes the difficult near-East regime.

### Exact depth-two obstruction

On

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

let

$$
m_\varepsilon=-\frac{\varepsilon}{1+\varepsilon}
$$

and

$$
M_{2,\varepsilon}
=\frac{(1+\varepsilon)(2\varepsilon-1)}{2\varepsilon^2+5\varepsilon+1}.
$$

The two-level invariant scalar is

$$
A_{2,\varepsilon}(u)
=m_\varepsilon^2
+e^{-(1+\varepsilon)u}(M_{2,\varepsilon}-m_\varepsilon^2).
$$

It starts negative and tends to the positive limit `m_epsilon^2`, hence changes sign.

I independently checked the asymptotics of the absolute-value integrals. They agree with the capture:

$$
\boxed{
\frac{g}{|m_\varepsilon|}
\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|\,du
\longrightarrow\frac32,
}
$$

and with the segmentwise right survival factor,

$$
\boxed{
\frac{g}{|m_\varepsilon|}
\int_0^\infty w(u)|A_{2,\varepsilon}(u)|\,du
\longrightarrow\frac75.
}
$$

Also

$$
Z\sim\frac{2}{5\varepsilon^2},
$$

and the equilibrium mass coefficient satisfies

$$
|Br_0-c|Z\longrightarrow\frac25.
$$

Therefore this is not a weak-bound artifact. Near East, one-step pointwise positivity and one-step `L^1` contraction are false even after the improved right-region factor is inserted.

## What survives from Meeting 005

The following remain live:

1. the exact canonical predecessor-trail decomposition and positive factor `e^{-omega tau}`;
2. left/right Poisson factorization, subject to the independent audit already requested;
3. finite zero-boundary relaxation after the final trail time;
4. the exact East equilibrium cancellation;
5. the stronger segmentwise right-region product bound;
6. the use of the full all-depth centered invariant expectation rather than cellwise positivity.

The sufficient quantity is sharpened to

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_{k=1}^n w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|\,du.
}
$$

Showing `J_{x,r}->0` with trail depth is now the correct analytic target for the nonempty-exit term.

## New structural decomposition

For a law `mu` whose rightmost spin has density `r`, write `bar mu` for its left marginal and `mu^1,mu^0` for the conditional left laws. The exact identity

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f)
}
$$

splits each centered insertion into a signed **mass channel** and a positive **disagreement channel**.

Near East, the equilibrium mass channel is only order `epsilon^2`, while the disagreement channel is order `epsilon`. The right-weighted mass multiplier tends to `2/5`, so every genuine regeneration of the disagreement component creates a strict scalar loss.

This identity explains why taking total variation immediately is wrong: it discards the disagreement structure and reproduces the depth-two expansion.

## Connection to Student F's coupling work

The principal's reset-coupling argument for the unresolved trail-generated disagreement stack gives

$$
\mathbb P(K\ge j)
\ge
\frac{B+\omega}{B+2\omega}2^{-(j-1)},
$$

and hence

$$
\mathbb EK\ge\frac{2(B+\omega)}{B+2\omega}>1.
$$

If `H` is unresolved stack height and one trail step adds at most one new level,

$$
H'\le(H-K)_+ +1,
$$

so for large height

$$
\mathbb E(H'-H)
\le-\frac{B}{B+2\omega}<0.
$$

The race calculation is consistent with Student F's independent coupling discovery that every disagreement has a positive environment-uniform coalescence intensity. Thus the live-disagreement work is no longer merely a paused alternative route: its coupling technology is now a natural component of the centered-trail proof attempt.

The stack-height drift alone does **not** prove decay of signed transfer mass. The unresolved issue is branching of the decomposition into `bar mu` and `mu^1-mu^0` through repeated insertions.

## Revised remaining lemma

The one-step norm theorem is false. The plausible remaining theorem is parameter-dependent **block contraction**.

Find a norm on decompositions into signed mass components and coupled disagreement pairs, weighted by unresolved stack height, and constants

$$
m_0<\infty,\qquad \theta<1,
$$

such that the complete right-weighted transfer satisfies

$$
\boxed{
\|T^{m_0}\nu\|_*\le\theta\|\nu\|_*
}
$$

for every trail-generated signed measure.

The norm must retain cancellation in the disagreement channel. Bounding `mu^1-mu^0` by unrestricted total variation is forbidden unless a new compensating estimate is proved, because that recreates the exact `3/2` / `7/5` depth-two expansion.

A proof of block contraction must be tied back to `J_{x,r}->0` and then to the complete trail decomposition, including the no-exit complementary term.

## Ruling

The principal's continued trail route **survives**, but Meeting 005's one-generation target `(T)` is closed by an exact two-level counterexample.

The active spine is now:

> predecessor trail -> segmentwise right killing -> mass/disagreement decomposition -> negative-drift unresolved disagreement stack -> block contraction of the signed mass/disagreement transfer.

This is a genuine narrowing. We have eliminated a false all-depth norm target, proved a nontrivial easy parameter region, and isolated the remaining obstruction as signed branching through regeneration cycles rather than generic finite-volume mixing or disagreement survival.

Student F is redirected immediately. Student G continues Assignment 002 unchanged.
