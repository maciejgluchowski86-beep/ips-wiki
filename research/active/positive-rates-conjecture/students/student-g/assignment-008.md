# Student G assignment 008: occupation-weighted two-spin disagreement exploration

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/018-consultation-actual-front-certificate-and-one-occupation-block.md`;
- your `006-common-coupling-survival.md` and `007-random-map-hamming-contraction.md`;
- Student F `012-tail-shift-agreement.md`, especially the bound of `Delta_M` by integrated far-left disagreement damage;
- Meetings 015--017 as needed for anti-circularity and the route stop;
- current `proof-spine.md`.

The scientific target remains the positive rates conjecture for simple IPS.

This assignment is the one structural front block authorized after outside consultation 001. It is **not** a continuation of raw finite-window/HJB enumeration, and it is not permission to enlarge local scalar Foster classes or begin generic matrix-product engineering.

## Accepted new front input

At the hard point

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

write

$$
g=b-a=\frac{99}{10000},
\qquad
k=1-c=\frac1{10000}.
$$

For one initial disagreement at zero, let

$$
\sigma_m=\inf\{t:D_{-m}(t)=1\}.
$$

Before a fresh site `x` first disagrees, retain exactly

$$
Z=(s,t),
$$

where `s` is the common spin at `x` and `t` the common spin at `x-1`. The right neighbour enters through mode `D`, `C0`, or `C1`. Meeting 018 accepts the exact controlled killed-chain rates and the strict superharmonic certificate

$$
P(\sigma_m\le T)
\le
\frac{15}{4}e^{T/20}\left(\frac58\right)^m.
\tag{F1}
$$

Consequently

$$
E\sum_{j<-L}D_j(T)
\le
10e^{T/20}\left(\frac58\right)^{L+1}.
\tag{F2}
$$

This solves the earlier first-exposure-history defect: the next-left common spin is propagated exactly at absorption and is never replaced by a fresh favorable/adversarial bit.

The same meeting also accepts a slower-discount certificate giving finite deterministic discovery speed. These are finite-time/first-discovery statements only.

## Why finite front speed is not enough

Student F proves, for the zero-boundary coupling,

$$
\boxed{
\Delta_M
\le
2c\int_0^\infty\beta_{M-1}(t)\,dt,
}
\tag{F012}
$$

where

$$
\beta_m(t)
=
\sup_{\text{finite zero-boundary systems},\eta,i}
E\sum_{j\le i-m}D_j(t).
$$

The bound `(F1)` grows like `e^{lambda t}` at fixed spatial depth and therefore cannot be integrated in time. What matters now is **occupation behind the front**, including repeated disagreement episodes, not merely the first discovery time.

Define

$$
G_m
:=
\sup_{\text{finite zero-boundary systems},\eta,i}
\int_0^\infty
E\sum_{j\le i-m}D_j(t)\,dt.
\tag{O0}
$$

## Primary objective

Prove at the hard point that there exist

$$
C<\infty,
\qquad
\theta<1,
$$

such that

$$
\boxed{
G_m\le C\theta^m
\qquad(m\ge1).
}
\tag{OCC}
$$

If successful, combine it explicitly with `(F012)` to obtain

$$
\Delta_M\le2cC\theta^{M-1}.
$$

This would settle the stationary tail-shift / first post-insertion common-mass localization theorem, though it would still not prove arbitrary signed-profile iteration or `J_{x,r}->0`.

## What the occupation exploration must retain

The first-discovery theorem could dominate the right-neighbour mode by an arbitrary predictable process because it stopped at the next absorption. That domination is **not automatically legitimate over infinite occupation time**.

In particular, do not set mode `D` to be immortal and then infer anything about the actual coupling: G006 proves that every fixed site eventually becomes permanently coupled. A permanently adversarial source can therefore be used only to prove an obstruction to a deliberately over-robust certificate class, not to refute `(OCC)` for the actual process.

The useful question is whether the two-spin pre-exposure state can be combined with the actual temporal constraints on its source. You may use, at their proved scopes:

- permanent coupling of every fixed site for finite seeds;
- the exact rightmost-coalescence hazard lower bound `q=1-c+a`;
- the same-parent exposure/re-entry geometric theorem;
- the actual-front first-discovery certificate from Meeting 018;
- strong Markov decompositions at genuine graphical stopping times.

You may not import the predecessor-trail reset-height chain as an embedded chain of the actual coupling.

## Possible positive mechanisms

You have freedom in how to attack `(OCC)`. Examples of structurally acceptable routes include:

1. an occupation-weighted Bellman/superharmonic certificate in the two-spin exploration, with source-lifetime information entering through a rigorously proved kernel rather than an immortal controller;
2. a renewal decomposition in which each first-discovery stage carries a finite expected disagreement-time reward and the retained spin gives a spatial kernel with spectral radius below one;
3. a Laplace-resolvent family whose zero-frequency limit is controlled uniformly enough to sum the occupation;
4. a comparison showing that total expected disagreement occupation spawned beyond each new front site is uniformly finite and contracts geometrically in the retained spin state.

Any finite matrix you introduce must arise from an exact stopped exploration/renewal theorem. Do not revive the refuted spatial edge-product/coboundary Foster architecture under new notation.

## Valid negative outcome

If `(OCC)` cannot be proved from the two-spin exploration, a useful negative result is a **precise structural obstruction** showing that this state is insufficient for zero-frequency occupation control even after the actual source-lifetime facts already established in the programme are incorporated.

A valid obstruction should identify exactly what information is missing. For example, it might prove that two histories with the same `(s,t)` and currently identical mode have incompatible future occupation kernels by an amount that does not vanish under any spatial-stage contraction, or that the exact renewal operator on the two-spin state has spectral radius at least one.

Do **not** count the following as sufficient negative results:

- an immortal-`D` controller has infinite occupation;
- a crude total-variation bound exceeds one;
- a finite numerical truncation fails to contract;
- the causal Poisson cone is too large;
- another scalar local product fails.

Those facts are already understood or too crude.

## Stopping rule attached to this assignment

This is the final currently authorized common-uniform front block.

End with one of:

- `occupation front theorem proved: G_m <= C theta^m with ...`;
- `two-spin occupation exploration refuted because: ...`;
- `unresolved after substantive work; exact occupation blocker: ...`.

If you return the second outcome, or the third without a genuinely new occupation mechanism, the Professor will abandon the common-uniform global-coalescence interface. Do not propose enlarging the exposure state, restarting raw `L,R,T` enumeration, or generic matrix-product engineering as the default next step.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-g/008-occupation-weighted-front.md`

with exact verifier code beside it if you use a finite rational certificate or symbolic computation.
