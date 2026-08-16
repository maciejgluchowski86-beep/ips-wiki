# Group meeting 018: outside consultation gives an actual-front certificate; authorize one occupation-weighted front block

Date: 2026-08-16

Professor review of:

- Meeting 017 and its stop/reassessment decision;
- outside consultation 001, returned verbatim to the principal with recommendation `continue-front`;
- consultant brief `consultants/assignment-001-disagreement-front-survival-review.md`;
- Student G `006-common-coupling-survival.md` and `007-random-map-hamming-contraction.md`;
- Student F `012-tail-shift-agreement.md` for the Green/occupation interface;
- current `state.md` and `proof-spine.md`.

The consultant was instructed not to edit the repository. The mathematical statements below are therefore reconstructed and ruled on here rather than treated as authoritative because they appeared in the consultation.

state_narrowed: yes

Evidence pointer: the consultant's controlled two-spin first-exposure certificate reproduced below, together with the already accepted G006/G007 coupling construction and F012 Green-response inequality.

## Decision

I choose the first of the three Meeting-017 outcomes:

> **continue with one sharply stated actual-front theorem.**

This does not reopen the stopped raw finite-window/HJB implementation. It also does not authorize generic matrix-product/nonlocal-norm engineering. The outside consultation found a new finite exploration state which directly resolves the specific pre-exposure-history defect identified in Meetings 015--017, and it produced an explicit strict superharmonic certificate. That is enough new structural information to justify one internal block aimed at the quantity F012 actually needs: time-integrated far-left disagreement occupation.

Student G receives one new assignment on this occupation problem. Student F remains idle. If that block cannot convert the retained pre-exposure history into an occupation estimate, or gives a precise obstruction for this two-spin exploration, the common-uniform global-coalescence interface stops; no exposure-state enlargement or return to raw finite enumeration is authorized automatically.

## Hard point and exploration state

Work at

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

and put

$$
g=b-a=\frac{99}{10000},
\qquad
k=1-c=\frac1{10000}.
$$

Start from one disagreement at site zero and let

$$
\sigma_m=\inf\{t:D_{-m}(t)=1\}
$$

be the first discovery time of the `m`-th site to the left.

Before a previously unexposed site `x` first becomes disagreeing, write

$$
Z=(s,t)\in\{00,01,10,11\},
$$

where `s` is the common spin at `x` and `t` is the common spin at `x-1`. The right neighbour `x+1` enters only through one of three modes:

- `D`: `x+1` is a disagreement;
- `C0`: `x+1` is coupled with common spin zero;
- `C1`: `x+1` is coupled with common spin one.

The actual mode is adapted to the full graphical history on the right. For the first-exposure upper bound it is enough that the certificate below is valid under arbitrary predictable switching between these three modes.

Before absorption at the first disagreement at `x`, the transient rates are as follows.

For the second coordinate `t`:

- if `s=0`, `0->1` at rate `a` and `1->0` at rate `k`;
- if `s=1`, `0->1` at rate `b` and `1->0` at rate `1`.

For the first coordinate `s`:

- in mode `D`, if `s=0`, `0->1` at rate `a` and absorption occurs at rate `g`; if `s=1`, `1->0` at rate `k` and absorption occurs at rate `c`;
- in mode `C0`, if `s=0`, `0->1` at rate `a`; if `s=1`, `1->0` at rate `k`;
- in mode `C1`, if `s=0`, `0->1` at rate `b`; if `s=1`, `1->0` at rate `1`.

At absorption, `t` is exactly the common spin of the next site to be explored. There is no fresh-spin or independence step.

I checked these rates directly from the common-uniform pair update rule. In particular, when the right neighbour is a disagreement, a common zero at the target becomes a disagreement at rate `b-a=g`, whereas a common one becomes a disagreement at rate `c`, exactly preserving the exposure asymmetry which invalidated favorable/adversarial freshening.

## Professor check: strict discounted stage certificate

The consultant gives

$$
\lambda=\frac1{20},
\qquad
\rho=\frac58,
$$

$$
v(0)=1,
\qquad
v(1)=\frac{15}{4},
$$

and

$$
U(00)=\frac{17}{100},\quad
U(01)=\frac{623}{1000},\quad
U(10)=\frac{97}{100},\quad
U(11)=\frac{231}{100}.
$$

For a mode `M`, let `q_M(z,z')` be the transient rates just listed and `k_M(z)` the absorption rate. Define

$$
\operatorname{Margin}_M(z)
=
\lambda U(z)
+
\sum_{z'}q_M(z,z')[U(z)-U(z')]
+
k_M(z)[U(z)-v(t)].
$$

In state order `00,01,10,11`, direct exact rational substitution gives

`D`:

$$
\frac{1577}{10000000},\quad
\frac{693}{10000000},\quad
\frac{5183}{1000000},\quad
\frac{158127}{10000000};
$$

`C0`:

$$
\frac{83747}{10000000},\quad
\frac{155133}{5000000},\quad
\frac{1759}{50000},\quad
\frac{14556687}{10000000};
$$

`C1`:

$$
\frac{4547}{10000000},\quad
\frac{143253}{10000000},\quad
\frac{8351}{10000},\quad
\frac{1257}{400}.
$$

All are strictly positive. I independently recomputed these fractions.

The stage-cap slacks

$$
\rho v(s)-U(s,t)
$$

are

$$
\frac{91}{200},\quad
\frac1{500},\quad
\frac{1099}{800},\quad
\frac{27}{800},
$$

again all strictly positive.

For each predictable mode process, the generator inequality says that the stopped process `e^{-lambda t}U(Z_t)`, with terminal value `v(t)` at absorption, is a supermartingale. Optional stopping therefore gives, for the current first-exposure time `tau`,

$$
E\left[e^{-\lambda\tau}v(t_\tau);\tau<\infty\mid Z_0=(s,t)\right]
\le U(s,t)
\le\rho v(s).
$$

At the next discovery stage the terminal spin `t_tau` is retained as the new current spin; the still-untracked spin one site farther left may be either value, and the same inequality holds. Strong Markov induction therefore yields

$$
\boxed{
P(\sigma_m\le T)
\le
\frac{15}{4}e^{T/20}\left(\frac58\right)^m.
}
\tag{F1}
$$

I accept this as a genuine actual-front theorem. It is not the predecessor-trail reset chain and it does not freshen the common spin at exposure.

## Consequence: actual far-left finite-time damage tail

If site `-r` is disagreeing at time `T`, then it has been discovered by time `T`. Summing `(F1)` for `r>=L+1` gives

$$
\boxed{
E\sum_{j<-L}D_j(T)
\le
10e^{T/20}\left(\frac58\right)^{L+1}.
}
\tag{F2}
$$

This is strictly sharper than the causal Poisson cone on the near-East time scale. At `T=47`, the right side is below `0.01` already at `L=19`, whereas the G007 causal truncation needed `L>=67` for the same diagnostic tolerance.

The same first-exposure theorem applies to the propagation of a right-boundary mismatch toward the retained disagreement region. Thus the G007 fixed-boundary sandwich may replace its causal errors by

$$
\ell_L^*(T)
=10e^{T/20}\left(\frac58\right)^{L+1},
$$

$$
r_{L,R}^*(T)
=(L+1)\frac{15}{4}e^{T/20}\left(\frac58\right)^{R+1}.
$$

Hence

$$
\boxed{
B_{L,R}^e(T)-r_{L,R}^*(T)
\le\alpha(T)
\le
B_{L,R}^e(T)+r_{L,R}^*(T)+\ell_L^*(T).
}
\tag{F3}
$$

At `T=47`, `L=19,R=23` already make both displayed errors below `0.01`. This is a structural truncation improvement, not permission to enumerate the resulting `2^63` naive state space.

## Professor check: deterministic front-speed bound

The consultant also supplies a slower-discount certificate

$$
\lambda=\frac1{100},
\qquad
\rho=\frac{81}{100},
$$

$$
v(0)=1,
\qquad v(1)=\frac{13}{8},
$$

$$
U(00)=\frac{51}{100},\quad
U(01)=\frac{81}{100},\quad
U(10)=1,\quad
U(11)=\frac{131}{100}.
$$

The exact margins in state order `00,01,10,11` are

`D`:

$$
\frac{17}{100000},\quad
\frac{23}{2000000},\quad
\frac{6949}{1000000},\quad
\frac{16363}{2000000};
$$

`C0`:

$$
\frac{5021}{1000000},\quad
\frac{101}{12500},\quad
\frac{6949}{1000000},\quad
\frac{6463}{20000};
$$

`C1`:

$$
\frac{17}{100000},\quad
\frac{313}{100000},\quad
\frac{4969}{10000},\quad
\frac{8231}{10000}.
$$

The stage slacks are

$$
\frac3{10},\quad 0,\quad\frac{253}{800},\quad\frac1{160}.
$$

These are nonnegative, and I independently recomputed the fractions. Therefore

$$
P(\sigma_m\le T)
\le
\frac{13}{8}e^{T/100}\left(\frac{81}{100}\right)^m.
$$

A standard Borel--Cantelli argument gives the almost-sure discovery-speed bound

$$
\boxed{
\limsup_{t\to\infty}\frac{N_t}{t}
\le
\frac{1/100}{\log(100/81)}
\approx0.0474561,
}
\tag{F4}
$$

where `N_t` is the number of newly discovered sites to the left by time `t`.

This does not contradict convective survival: the guaranteed rightmost-coalescence hazard is only `q=1/5000`, and `(F4)` is far larger than that scale.

## Why this does not solve the F012 interface

F012 proves

$$
\Delta_M
\le
2c\int_0^\infty\beta_{M-1}(t)\,dt,
$$

where `beta_m(t)` is the maximal expected disagreement mass at least `m` sites to the left in a finite zero-boundary chain.

The new front estimate is of the form

$$
e^{\lambda t}\rho^m.
$$

For fixed `m` it is not integrable in `t`. Therefore `(F1)`--`(F4)` do **not** prove tail-shift agreement. They control first discovery, not the full amount of disagreement occupation behind the front.

This is the decisive distinction for route value. On a convective-survival event, disagreement remains somewhere beyond every fixed left cutoff for arbitrarily late times, so the corresponding integrated far-left occupation is infinite. Any exponential bound

$$
G_m
:=
sup_{\text{finite zero-boundary systems},\eta,i}
\int_0^\infty
E\sum_{j\le i-m}D_j(t)\,dt
\le C\theta^m
$$

with `theta<1` is therefore already an extinction-strength statement.

Even such a theorem would only settle the stationary tail-shift / first post-insertion common-mass localization. Arbitrary duration-resolved signed-profile composition and the final `J_{x,r}->0` implication would remain separate.

## Why continue-front once, rather than continue-survival

The consultant judges convective survival modestly more plausible near the hard point, citing the very small guaranteed rightmost-killing rate, the high one-exposure transmission probabilities, and G007's protected-source expansion through time 47. I do not promote that plausibility judgment to a mathematical claim.

What matters for direction is that the front side now has a concrete finite killed exploration and a strict certificate which directly attacks the previously identified pre-exposure-history blocker. The survival side still has no valid supercritical lower process preserving that history.

Therefore one more **front** block has higher expected information value than a survival block.

## One next internal task and stopping rule

Student G is assigned one occupation-weighted extension of the two-spin exploration at the hard point.

The primary target is

$$
\boxed{
G_m\le C\theta^m
\quad\text{for some }C<\infty,\ \theta<1.
}
\tag{OCC}
$$

A proof may combine the retained pre-exposure state with actual source-lifetime/re-entry information, but it must not replace the post-exposure right-side process by an immortal adversarial disagreement and then claim a theorem about the actual process. The arbitrary-mode robustness of `(F1)` is valid because it is used only until the next first discovery; zero-frequency occupation requires the actual temporal constraints on disagreement modes.

A valid negative outcome is a precise theorem that the **two-spin exploration is insufficient for zero-frequency occupation control**, after incorporating the actual source-lifetime facts already proved in this programme. Such a result must identify the missing information or recurrent mechanism. Failure of a deliberately immortal `D` controller by itself is too crude: fixed-site permanent coupling already tells us that `D` is not actually immortal.

If `(OCC)` is proved, F012 immediately gives exponential tail-shift localization

$$
\Delta_M\le 2cC\theta^{M-1}.
$$

If the two-spin exploration is rigorously shown insufficient, or if the block returns unresolved without a new occupation mechanism, the common-uniform global-coalescence interface is abandoned. Do not enlarge the exposure state, restart raw `L,R,T` enumeration, or issue a cosmetic G009/F013 continuation without a new Professor reassessment.

## Ruling

- `state_narrowed: yes`.
- Outside consultation recommendation `continue-front` is accepted.
- The four-state controlled pre-exposure process is a valid Markov exploration retaining the next-left common spin.
- The strict rational superharmonic certificate gives the actual-front tail `(F1)` and far-left finite-time damage bound `(F2)`.
- The G007 fixed-boundary sandwich improves to `(F3)` with actual-front rather than causal Poisson errors.
- A second rational certificate gives the finite almost-sure front-speed bound `(F4)`.
- None of these results proves extinction, survival, tail-shift agreement, or `J_{x,r}->0`.
- Student G receives one occupation-weighted front assignment. Student F remains idle.
- This is a new structural front theorem authorized by Meeting 017's post-consultation branch, not a revival of the stopped raw finite-window certificate implementation.