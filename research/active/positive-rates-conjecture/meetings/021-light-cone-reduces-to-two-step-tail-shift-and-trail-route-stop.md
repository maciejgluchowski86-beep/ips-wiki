# Group meeting 021: light-cone screening reduces to two-step tail shift; current predecessor-trail implementation is exhausted

Date: 2026-08-17

Professor review of:

- Meeting 020 and its pre-registered stopping rule;
- Student F commit `f0d5277`, `students/student-f/014-light-cone-screening.md`;
- `students/student-f/014-light-cone-screening-verifier.py`, commit `15b5436`;
- F013 for the exact recombined two-insertion spectral decomposition;
- F010 for suffix projectivity and one-site positive-frequency localization;
- current `state.md` and `proof-spine.md`.

`state_narrowed: yes`.

Evidence pointer: F014 Sections 2--8, especially Proposition 3.1, the exact static decomposition `(0.1)`, the two-step tail-shift identity `(0.4)`, the positive-time normal form `(0.8)`, and the conditional integrated estimate `(0.9)`; exact finite algebra is checked by the committed verifier.

## Ruling in one sentence

F014 proves that the fixed-suffix and causal light-cone pieces really do localize exponentially, but the recombined two-insertion defect retains a pre-existing two-step spatial boundary law which is exactly a tail-shift defect. Therefore Meeting 020's stopping condition is met: the **present predecessor-trail/profile implementation is recorded as exhausted**. No F015/G009 continuation of this implementation is issued.

This does **not** refute `Gamma_M->0`, `Delta_M^(2)->0`, `J_{x,r}->0`, or the positive rates conjecture.

## Professor check: the fixed two-site suffix is not the blocker

Put

$$
\omega=1-c+a>0.
$$

In the graphical decomposition, every site has neighbour-independent reset-to-one marks of rate `1-c` and reset-to-zero marks of rate `a`. For the autonomous rightmost two-site suffix, after the first independent reset of the rightmost site and then the first independent reset of the next site, two copies driven by the same graphical construction are permanently coupled.

Hence the two-site coupling time is dominated by a sum of two independent `Exp(omega)` variables, and for every centered suffix observable `h`,

$$
\boxed{
\|S_t^{(2)}h\|_\infty
\le 2\|h\|_\infty e^{-\omega t}(1+\omega t).
}
$$

I accept F's use of this bound. It is a fixed two-site statement and does not assume any depth-uniform mixing theorem.

Now let `f` be supported at least `M` sites to the left of the rightmost two-site suffix. Evolve the stationary system for time `T`, but freeze the boundary input from the suffix into the left block. Conditional on the time-zero configuration, the future suffix marks and the modified left evolution use disjoint Poisson families. The true and modified left observables can differ only if an ordered chain of at least `M+1` site rings carries boundary influence across the buffer. Therefore

$$
|\pi_N(hf)|
\le
2\|h\|_\infty\|f\|_\infty
\left[
 e^{-\omega T}(1+\omega T)
+P(\operatorname{Pois}(T)\ge M+1)
\right].
$$

Taking `T=M/4` gives

$$
\boxed{
|\pi_N(hf)|
\le
6\|h\|_\infty\|f\|_\infty e^{-\gamma_*M},
}
$$

with

$$
\gamma_*=
\min\left\{\frac\omega8,\log4-\frac34\right\}>0.
$$

I accept this as a genuine depth-uniform separated-gap theorem for every centered observable of the **fixed** two-site suffix.

## Professor check: the static two-insertion defect contains a different term

Write

$$
Y_j=B\eta_j-c,
\qquad
H_N=Y_NY_{N-1},
\qquad
h_*:=\pi_2(H_2).
$$

At `u=0`, the recombined two-insertion defect is

$$
E_{N,0}(f)
=\pi_N(H_Nf)-h_*\pi_{N-2}(f).
$$

By suffix projectivity, `pi_N(H_N)=h_*`. Adding and subtracting `h_* pi_N(f)` gives the exact identity

$$
\boxed{
E_{N,0}(f)
=\pi_N[(H_N-h_*)f]
+h_*\,\delta_N^{(2)}(f),
}
$$

where

$$
\delta_N^{(2)}
:=\bar{\bar\pi}_N-\pi_{N-2}.
$$

The first term is exactly the centered fixed-suffix covariance just proved exponentially local. Since `|H_N-h_*|<=2c^2`,

$$
\left|
E_{N,0}(f)-h_*\delta_N^{(2)}(f)
\right|
\le12c^2e^{-\gamma_*M}\|f\|_\infty.
$$

At the standard strict residual point

$$
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right),
$$

the exact two-site calculation gives

$$
\boxed{h_*=-\frac{34}{8775}\ne0.}
$$

The verifier checks this fraction and the exact finite-volume decomposition. I independently checked the algebraic decomposition; the verifier is evidence for the finite rational calibration, not for the analytic light-cone inequalities.

## Professor check: this is exactly a two-step tail-shift defect

Let `mu=pi_infty^0` be the projective half-line zero-boundary law in boundary-outward coordinates and let `theta` be the left shift on these coordinates. Define

$$
\mathcal F_M=\sigma(X_j:j\ge M).
$$

The double-left marginal of `pi_N` and `pi_{N-2}` correspond to two windows in the same projective law separated by two spatial shifts. Taking the supremum over all finite remote windows gives

$$
\boxed{
\Delta_M^{(2)}
:=\sup_N\|\delta_N^{(2)}\|_{\mathrm{remote},M}
=\|\theta^2\mu-\mu\|_{\mathcal F_M}.
}
$$

The same reverse-martingale argument as F011 therefore gives

$$
\lim_{M\to\infty}\Delta_M^{(2)}
=\|\theta^2\mu-\mu\|_{\mathcal T},
\qquad
\mathcal T=\bigcap_M\mathcal F_M.
$$

Thus the static remote norm `S_M` of `E_{N,0}` satisfies

$$
\boxed{
\left|S_M-|h_*|\Delta_M^{(2)}\right|
\le12c^2e^{-\gamma_*M}.
}
$$

At any parameter point with `h_*!=0`, exponential static screening is therefore equivalent, up to the explicit fixed-suffix error, to exponential two-step tail-shift localization. This is not a consequence of finite propagation.

One-step tail-shift agreement would imply the two-step statement, but the converse is not purely measure-theoretic because a period-two tail phase is not excluded a priori.

## Professor check: positive time does not remove the same law

Cut the influence of site `N-1` into the left `(N-2)`-site block. The cut semigroup factors as the zero-boundary semigroup `Q_u=P_u^{N-2,0}` on the left and the autonomous one-site semigroup on site `N-1`.

Since

$$
S_uY_{N-1}
=m_0+B e^{-(1+b)u}(\eta_{N-1}-r_0),
$$

define

$$
G_u
:=Y_N\left[m_0+B e^{-(1+b)u}(\eta_{N-1}-r_0)\right].
$$

Then `pi_N(G_u)=a(u)`, and the cut defect is exactly

$$
\widehat E_{N,u}(f)
=\pi_N[(G_u-a(u))Q_uf]
+a(u)\delta_N^{(2)}(Q_uf).
$$

The first term is again a centered fixed two-site suffix covariance. The second is the same double-left boundary law, merely tested against the left evolution.

F then compares the true and cut semigroups by an ordered graphical crossing event and truncates `Q_uf` before the light cone reaches the remote test. For every `1<=d<=M`, there is a bounded `q` still separated by `M-d` from the suffix such that

$$
\boxed{
\begin{aligned}
\left|E_{N,u}(f)-a(u)\delta_N^{(2)}(q)\right|
\le{}&12c^2e^{-\gamma_*(M-d)}\\
&+8c^2P(\operatorname{Pois}(u)\ge d)\\
&+2c^2P(\operatorname{Pois}(u)\ge M+1).
\end{aligned}
}
$$

I accept this normal form. Choosing `d=floor(M/2)` and `0<=u<=M/8` makes every displayed remainder exponentially small in `M`. The only term not controlled by the fixed suffix or the causal cone is

$$
a(u)\delta_N^{(2)}(q).
$$

This is spatial memory already present at time zero, not influence propagated during the trail duration.

## Integrated consequence

Meeting 020 already observed that

$$
0\le w(u)\le e^{-\omega u},
\qquad
\|E_{N,u}\|_{TV}\le2c^2,
$$

so the late-time part `u>=M/8` is exponentially small. Combining this with the short-time normal form yields constants `C,gamma>0` such that

$$
\boxed{
\Gamma_M
\le
c^2Z\,\Delta_{\lceil M/2\rceil}^{(2)}
+Ce^{-\gamma M}.
}
$$

Therefore two-step tail-shift agreement would imply `Gamma_M->0`, and exponential two-step tail-shift localization would imply exponential two-insertion localization.

This is a useful conditional theorem. It is not a proof of the missing tail theorem.

## Why the stopping rule is met

Meeting 020 pre-registered the following outcome: if the short-time recombined defect contains a nonlocal zero-frequency response not controlled by fixed-suffix localization plus finite propagation, or if F014 returns unresolved without a sharper mechanism, record the current predecessor-trail/profile implementation as exhausted.

That is exactly what occurred:

1. the fixed two-site suffix mixes and localizes exponentially;
2. the graphical light-cone remainder is exponentially controlled;
3. after both are removed, the surviving term is the two-step tail-shift defect `Delta_M^(2)`;
4. no independent mechanism for that zero-frequency spatial theorem was produced.

Continuing by simply assigning `prove Delta_M^(2)->0`, by generic full-chain observability/mixing, by a third insertion, or by a matrix-product norm would move the unresolved global spatial theorem rather than exploit a new mechanism. Those are not authorized continuations of this implementation.

Accordingly:

> **the present predecessor-trail/profile implementation is exhausted.**

This is an expected-value route decision, not a theorem that every predecessor-trail representation is impossible.

## What remains mathematically valid

The programme retains substantial reusable mathematics:

- the centered predecessor-trail reduction and exact all-depth target `J_{x,r}`;
- the norm-order obstruction;
- strict regenerated-mass and first-transient damping;
- operator-valued signed transfer and the finite-mode obstruction;
- suffix projectivity and fixed-suffix positive-frequency localization;
- exact one- and two-step tail-shift reformulations of zero-frequency spatial defects;
- the common-uniform coupling's fixed-site coalescence, convective-survival equivalence, moving-frame contraction, finite-time approximation, long initial expansion, and retained-spin first-discovery front theorem;
- F013's exact unsplit two-insertion spectral decomposition;
- F014's centered two-site suffix localization and short-time light-cone normal form.

None currently closes `J`.

## Route-level decision

No F015 is issued. No G009 is issued. Students F and G are idle.

The principal-fixed scientific target remains the positive rates conjecture. The exhausted object is the **current implementation**, whose two attempted interfaces have now both terminated at an uncontrolled zero-frequency spatial law:

- the positive common-coupling interface terminated at all-depth disagreement occupation / source-return capacity;
- the recombined signed-profile interface terminated at one- or two-step tail-shift memory of the half-line invariant law.

The next substantial internal block should not start until a genuinely different proof architecture has been identified. I authorize one bounded outside route-selection consultation, `consultants/assignment-002-post-trail-architecture-review.md`, before assigning further student work.

The consultation is asked to distinguish a genuinely new mechanism from another reformulation of tail-shift mixing or global common-coupling extinction. In particular, a proposal to attack `Delta_M` or `Delta_M^(2)` counts as new only if it supplies an independent structural theorem specific to the one-sided stationary law rather than assuming or renaming the missing mixing statement.

## Ruling

- `state_narrowed: yes`.
- The fixed two-site suffix covariance localizes exponentially.
- The true positive-time recombined defect has an exponentially accurate no-crossing normal form whose only nonlocal term is `a(u) delta_N^(2)`.
- `Delta_M^(2)=||theta^2 mu-mu||_{F_M}` is the exact remaining spatial law.
- `Gamma_M <= c^2 Z Delta_{ceil(M/2)}^(2)+C e^{-gamma M}`.
- `Gamma_M`, two-step tail-shift agreement, `J` decay, and the conjecture remain unresolved.
- Meeting 020's stopping condition is met.
- The current predecessor-trail/profile implementation is recorded as exhausted.
- No F015/G009 variant is issued.
- One bounded outside consultation on a genuinely different architecture is authorized before further internal work.
