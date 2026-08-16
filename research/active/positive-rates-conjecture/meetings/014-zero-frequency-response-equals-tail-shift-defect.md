# Group meeting 014: zero-frequency response is exactly the spatial tail-shift defect

Date: 2026-08-16

Professor review of:

- Student F, commit `1727be2`, `students/student-f/011-zero-frequency-boundary-response.md`;
- verifier commit `a845bf2`, `students/student-f/011-zero-frequency-boundary-response-verifier.py`;
- Meeting 013, current `state.md` and `proof-spine.md`;
- Student G Assignment 006 only for interface/status awareness.

Operational note: the original Student G session failed after Meeting 012 before its Assignment-006 work reached the repository. No mathematical result from that lost response is used or rejected. A successor G session in the same student lineage has been given Assignment 006 unchanged. The principal salvaged only the warning that importing the trail reset drift into Assignment 006 would be circular because that drift presupposes the reset chain Assignment 006 is testing. The replacement G session remains in flight.

state_narrowed: yes

Evidence pointer: `students/student-f/011-zero-frequency-boundary-response.md`, especially Sections 3--8, and the finite indexing checks in `011-zero-frequency-boundary-response-verifier.py`.

## Previous blocker

Meeting 013 reduced the common-mass problem to the zero-frequency boundary response

$$
\Delta_M
:=
\sup_{N\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}(f)\subseteq\{1,\ldots,N-M\}}}
|\bar\pi_N(f)-\pi_{N-1}(f)|.
$$

The load-bearing question was whether `Delta_M -> 0` uniformly in total volume. Finite speed alone cannot settle this because the exact Green representation has no positive Laplace parameter.

F does not prove or refute `Delta_M -> 0`. It identifies exactly what the statement means on the projective half-line invariant law and proves the requested one-next-segment lift conditional on it.

## Professor verification: exact half-line identification

Let

$$
\mu=\pi_\infty^0
$$

be the projective half-line zero-boundary invariant law in coordinates

$$
X_j=\eta_{-j},\qquad j\ge0,
$$

where `X_0` is adjacent to the fixed zero boundary. Let

$$
\theta(x_0,x_1,x_2,\ldots)=(x_1,x_2,x_3,\ldots)
$$

and

$$
\mathcal F_m=\sigma(X_j:j\ge m).
$$

For a sigma-field `G`, write

$$
\|\nu-\rho\|_{\mathcal G}
=
\sup_{\substack{|F|\le1\\F\ \mathcal G\text{-measurable}}}
|\nu(F)-\rho(F)|.
$$

I checked F's finite-window indexing from suffix projectivity. For fixed `N=M+L`, the block entering `Delta_M` has law, under `\bar\pi_N`, of

$$
(X_{N-1},\ldots,X_M),
$$

and under `\pi_{N-1}` of

$$
(X_{N-2},\ldots,X_{M-1}).
$$

Reversing coordinate order does not change variation. Taking the supremum over all finite lengths `L` therefore gives

$$
\boxed{
\Delta_M
=
\|\theta\mu-\mu\|_{\mathcal F_{M-1}}.
}
$$

The verifier independently checks this finite-window identification at several exact rational windows and the associated projection monotonicity. Its role is arithmetic/indexing only; the infinite-tail conclusion below is analytic.

In particular `Delta_M` is nonincreasing because `\mathcal F_M\subset\mathcal F_{M-1}`.

## Professor verification: exact tail limit

Let

$$
\mathcal T=\bigcap_{m\ge0}\mathcal F_m
$$

be the remote-left spatial tail sigma-field. Put

$$
\lambda=\frac12(\mu+\theta\mu),
\qquad
H=\frac{d(\theta\mu-\mu)}{d\lambda}.
$$

Then `|H|<=2`. For every sub-sigma-field `G`, the restriction of the signed measure `theta mu-mu` to `G` has density

$$
E_\lambda[H\mid\mathcal G]
$$

with respect to `lambda|_G`, hence

$$
\|\theta\mu-\mu\|_{\mathcal G}
=
\int |E_\lambda[H\mid\mathcal G]|d\lambda.
$$

The reverse martingale theorem for the decreasing sigma-fields `F_m` gives `L^1(lambda)` convergence to `E[H|T]`. Therefore

$$
\boxed{
\lim_{M\to\infty}\Delta_M
=
\|\theta\mu-\mu\|_{\mathcal T}.
}
$$

Consequently

$$
\boxed{
\Delta_M\to0
\iff
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
$$

I accept this equivalence. It is strictly sharper than the Green-kernel formulation: failure is equivalent to a remote-left tail event whose probability changes after dropping one boundary-nearest spin.

A logical distinction is important. Triviality of the tail under each of `mu` and `theta mu` separately is not sufficient by itself: two measures can each have a trivial tail and still assign opposite probabilities to a tail event. The needed theorem is **tail-shift agreement**, or an equivalent asymptotic-stationarity statement, not merely a 0--1 law.

## Professor verification: conditional one-next-segment lift

Let

$$
\delta_N=\bar\pi_N-\pi_{N-1},
\qquad
m_0=Br_0-c,
\qquad
\kappa_E=|m_0|Z<\frac23.
$$

For a function supported at least `M` sites from the right boundary, choose a truncation buffer `1<=d<M`. Replacing the full semigroup by one cut `d` sites beyond the support gives

$$
|\delta_N(\widehat P_u f)|
\le\Delta_{M-d}\|f\|_\infty.
$$

Finite propagation gives

$$
\|P_u f-\widehat P_u f\|_\infty
\le2\|f\|_\infty P(\operatorname{Pois}(u)\ge d).
$$

Since `delta_N` is a difference of probability measures and `s_1(u)<=1`, keeping the absolute value at each duration gives

$$
\boxed{
\int_0^\infty w(u)|\delta_N(P_u f)|du
\le
\left[
Z\Delta_{M-d}
+
\frac{4}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
}
$$

Multiplying by the equilibrium mass coefficient yields

$$
\boxed{
\int_0^\infty w(u)
|m_0\delta_N(P_u f)|du
\le
\left[
\kappa_E\Delta_{M-d}
+
\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
}
$$

Thus, conditional on `Delta_M -> 0`, choosing `d=floor(M/2)` gives a genuine `J`-compatible one-next-segment truncation of the common-mass branch. The duration variable is never integrated before its absolute value, so this respects the Meeting-009 norm-order constraint.

## What this does and does not resolve

The first-insertion martingale truncation from Assignment 010 does not imply tail-shift agreement. F's alternating-product example correctly shows the logical gap: local conditional expectations can be trivial while successive spatial shifts are singular on a tail event.

The exact remaining stationary theorem is now

$$
\boxed{
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
$$

Even if this is proved, arbitrary trail iteration still requires control of later signed profiles and the disagreement branch. G's common-uniform survival/extinction test remains independent.

## Homeostasis / direction judgment

This is another unresolved F block, but it does narrow the mathematical state: the zero-frequency Poisson problem has been replaced by an exact static tail-shift theorem, and a positive answer is already shown to imply the first post-insertion duration-resolved truncation estimate.

I do not authorize a general matrix-product/nonlocal norm construction at this point. While G's replacement Assignment 006 is in flight, F gets one bounded decision block on the tail-shift theorem itself. The aim is not to restate it again, but to prove it, refute it, or derive a new structural criterion with real leverage, preferably through finite-window likelihood ratios / relative entropy / boundary-influence identities.

After F012 and G006 return, the next Professor meeting is a route-level expected-value review before any broader nonlocal construction.

## Ruling

- `state_narrowed: yes`.
- The exact identity `Delta_M=||theta mu-mu||_{F_{M-1}}` is accepted.
- `Delta_M` is nonincreasing and its limit is exactly the tail-shift variation `||theta mu-mu||_T`.
- Zero-frequency boundary locality is therefore equivalent to tail-shift agreement of the projective half-line invariant law.
- Conditional on that theorem, the common-mass branch after one centered insertion has a valid `J`-compatible one-next-segment truncation bound.
- Neither `Delta_M->0` nor its failure is proved.
- F is assigned one final bounded tail-shift decision block before the route-level review.
- G's replacement session continues Assignment 006 unchanged; no lost uncommitted G mathematics is treated as evidence.
