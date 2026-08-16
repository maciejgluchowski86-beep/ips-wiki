# Student G 007: two-sided random-map truncation and a macroscopic lower obstruction

## Verdict

I do **not** prove either

\[
\alpha(T)<1
\]

at the hard near-East point or convective survival. The finite-time Hamming question therefore remains unresolved.

I do obtain two results which materially sharpen Assignment 006 and prevent the next step from being "just run a larger controlled CTMC."

First, the adversarial right boundary in the Assignment-006 certificate can be removed with an explicit causal-cone error. For a finite window `[-L,R]` with a **fixed** common boundary spin `e` at `R+1`, let

\[
B_{L,R}^{e}(T)
\]

be the maximum expected number of disagreements in `[-L,0]` at time `T`, maximized only over finite common initial backgrounds with a single discrepancy at zero. Then, writing

\[
r_{L,R}(T)
=(L+1)\,\mathbb P(\operatorname{Pois}(T)\ge R+1)
\]

and

\[
\ell_L(T)
=\mathbb E[(\operatorname{Pois}(T)-L)_+],
\]

I prove the two-sided sandwich

\[
\boxed{
B_{L,R}^{e}(T)-r_{L,R}(T)
\le \alpha(T)
\le B_{L,R}^{e}(T)+r_{L,R}(T)+\ell_L(T).
}
\tag{0.1}
\]

Moreover the Assignment-006 controlled value satisfies

\[
\boxed{
0\le A_{L,R}(T)-B_{L,R}^{e}(T)
\le r_{L,R}(T).
}
\tag{0.2}
\]

Thus the controller pessimism is quantitatively harmless as `R->infinity` at every fixed time. The full-line coefficient `alpha(T)` is the limit of ordinary finite fixed-boundary CTMC computations with explicit two-sided errors. This is a genuine convergent finite approximation theorem, not another local Foster ansatz.

Second, the short-time expansion from Assignment 006 persists for a nontrivial macroscopic interval. At

\[
(a,b,c)
=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right)
\]

I construct one explicit protected-source event and prove

\[
\boxed{
\alpha(t)>1
\qquad\text{for every }0<t\le47.
}
\tag{0.3}
\]

The exact lower bound at `T=47` is larger than

\[
1.008204288867933.
\]

So a contracting block, if it exists, must emerge only after a long period of genuine damage amplification; this is much stronger than the infinitesimal derivative `9997/10000>0` from Assignment 006.

The two facts together expose the current finite-certificate bottleneck. At `T=47`, already asking the causal errors in (0.1) to be below `1%` each forces

\[
L\ge67,
\qquad
R\ge74,
\]

because

\[
\ell_{66}(47)>0.01>\ell_{67}(47)
\]

and, once `L>=67`,

\[
68\,\mathbb P(\operatorname{Pois}(47)\ge74)>0.01
>
68\,\mathbb P(\operatorname{Pois}(47)\ge75).
\]

The naive fixed-window state count is then at least

\[
4^{68}2^{74}=2^{210}.
\]

This is only a scale diagnostic, not a theorem that every certificate needs `1%` errors. But it shows that the newly convergent hierarchy cannot be decided by a modest increase of `L,R`: before any actual contraction margin is considered, the times not ruled out by (0.3) already place a direct full-state enumeration far beyond the bounded block authorized here.

The exact remaining theorem is therefore sharper than in Assignment 006:

> decide the finite-time damage map with a truncation error governed by the **actual disagreement/front tail**, rather than the causal Poisson cone, while retaining the pre-exposure common-spin history; or prove convective survival. The adversarial right boundary is no longer the issue.

An exact rational/interval verifier is committed beside this report as

`students/student-g/007-random-map-hamming-contraction-verifier.py`.

## 1. Setup

At the strict rational point write

\[
a=\frac1{10000},
\qquad
b=\frac1{100},
\qquad
c=\frac{9999}{10000},
\qquad
q=1-c+a=\frac1{5000}.
\tag{1.1}
\]

Use the common graphical construction from Assignment 006. A rate-one ring at site `i` with common uniform mark `U` updates

\[
\eta_i\mapsto
1_{\{U<r_{\eta_i,\eta_{i+1}}\}}.
\]

For two copies `X,Y` driven by the same rings and marks, put

\[
D_i(t)=1_{\{X_i(t)\ne Y_i(t)\}}.
\]

Let `Phi_t` be the resulting random map and

\[
\alpha(t)
=\sup_{\eta,i}
\mathbb E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
\tag{1.2}
\]

Assignment 006 and Meeting 015 give

\[
\alpha(t+s)\le\alpha(t)\alpha(s),
\]

and one strict inequality `alpha(T)<1` would imply exponential extinction of every finite disagreement seed.

No predecessor-trail reset chain is used below.

## 2. Replace the adversarial right boundary by a fixed boundary

Fix integers `L,R>=0` and a boundary spin `e in {0,1}`. Consider the finite common-uniform system on `[-L,R]` in which

- sites `[-L,0]` retain the full coupled pair state;
- sites `[1,R]` are common in both copies and retain one common spin;
- site `R+1` is frozen to `e` in both copies.

The dynamics at the left endpoint `-L` is already closed because the spin update is one-sided and depends only on the site and its **right** neighbour. No left boundary is needed.

Start from any finite state compatible with a single discrepancy at zero: every site in `[-L,-1]` is diagonal, site zero is `01` or `10`, and sites `[1,R]` are common. Define

\[
H_L(D)=\sum_{i=-L}^0D_i
\]

and

\[
\boxed{
B_{L,R}^{e}(T)
=
\max_{\text{finite single-flip initial states}}
\mathbb E H_L(D(T)).
}
\tag{2.1}
\]

This is an ordinary finite CTMC. At the rational point all jump probabilities at a ring are rational. There is no optimization over a time-dependent boundary path.

### Proposition 2.1: control-removal bound

For the controlled value `A_{L,R}(T)` from Assignment 006,

\[
\boxed{
0\le A_{L,R}(T)-B_{L,R}^{e}(T)
\le
(L+1)\mathbb P(\operatorname{Pois}(T)\ge R+1).
}
\tag{2.2}
\]

#### Proof

The lower bound is immediate: the constant control `z(t)=e` is admissible in the controlled problem.

For the upper bound, fix an initial finite state and any predictable boundary control. Couple the controlled chain and the fixed-`e` chain with the same clocks and marks on `[-L,R]`. The only possible initial discrepancy between the two evolutions is in what an update of site `R` sees at `R+1`.

Before this boundary discrepancy can affect the payoff sites `[-L,0]`, influence must propagate successively through sites

\[
R,R-1,\ldots,1,0.
\]

The earliest possible propagation time is therefore stochastically bounded below by the sum of `R+1` independent rate-one exponential waiting times. Hence

\[
\mathbb P(\text{boundary control affects site }0\text{ by }T)
\le
\mathbb P(\operatorname{Pois}(T)\ge R+1).
\tag{2.3}
\]

On the complementary event the two payoffs are identical. On the exceptional event their difference is at most `L+1`. Therefore the value under this arbitrary control is at most the corresponding fixed-boundary value plus the right side of (2.2). Maximize first over controls and then over initial finite states. `square`

This directly answers the concern in Assignment 007 that the right controller might be too pessimistic: its excess value vanishes with an explicit Poisson causal tail.

## 3. Two-sided convergent finite approximation of `alpha(T)`

Put

\[
r_{L,R}(T)
=(L+1)\mathbb P(\operatorname{Pois}(T)\ge R+1)
\tag{3.1}
\]

and retain Assignment 006's left discovery bound

\[
\ell_L(T)
=\mathbb E[(\operatorname{Pois}(T)-L)_+].
\tag{3.2}
\]

### Theorem 3.1: fixed-boundary sandwich

For either fixed boundary `e in {0,1}`,

\[
\boxed{
B_{L,R}^{e}(T)-r_{L,R}(T)
\le \alpha(T)
\le
B_{L,R}^{e}(T)+r_{L,R}(T)+\ell_L(T).
}
\tag{3.3}
\]

Consequently, for every fixed `T`, the finite fixed-boundary quantities converge to `alpha(T)` as `L,R->infinity` in the sense of the explicit sandwich.

#### Proof: upper bound

Take an arbitrary infinite initial pair differing only at zero. Restrict it to `[-L,R]` and run the fixed-boundary finite chain with the same internal graphical marks. By the same causal argument as (2.3), the two coupled pair processes agree on `[-L,0]` at time `T` except on an event of probability at most

\[
\mathbb P(\operatorname{Pois}(T)\ge R+1).
\]

Therefore

\[
\mathbb E\sum_{i=-L}^0D_i(T)
\le
B_{L,R}^{e}(T)+r_{L,R}(T).
\tag{3.4}
\]

Every disagreement strictly left of `-L` requires more than `L` successive leftward discoveries. The Assignment-006 finite-speed argument gives

\[
\mathbb E\sum_{i<-L}D_i(T)
\le
\ell_L(T).
\tag{3.5}
\]

Add (3.4) and (3.5), then take the supremum over the infinite initial background.

#### Proof: lower bound

Choose a finite initial state attaining the maximum in (2.1) and extend its common spins arbitrarily to the full line, retaining only the one discrepancy at zero. Couple the infinite process to the fixed-boundary process as above. On the event that boundary influence has not reached site zero, their payoffs in `[-L,0]` are identical; otherwise the finite payoff can exceed the infinite payoff by at most `L+1`. Hence

\[
\mathbb E d_H(D(T))
\ge
B_{L,R}^{e}(T)-r_{L,R}(T).
\]

Taking the supremum defining `alpha(T)` proves the lower inequality. `square`

### Remark 3.2

The theorem is deliberately about the complete finite-time random map. It does not assign local scalar credits, introduce a matrix product, or truncate disagreement ancestry by the predecessor-trail reset rule. It is therefore outside the mechanisms refuted in Meetings 010--012 and respects the Meeting-016 stop condition by supplying a genuine convergence theorem for the finite approximation.

## 4. A protected-source lower event

The hard point is not merely expansive at `t=0`. Consider the deterministic initial background

\[
(X_0,Y_0)=(0,1),
\qquad
X_{-1}=Y_{-1}=1,
\qquad
X_1=Y_1=0.
\tag{4.1}
\]

The spins farther right and farther left may be chosen arbitrarily; the event below does not use them.

Put

\[
A=b+q=\frac{51}{5000},
\qquad
\delta=1-c+b=\frac{101}{10000},
\qquad
x=c-b=\frac{9899}{10000}.
\tag{4.2}
\]

### 4.1 Protect the common right spin and the source

At site `1`, while the spin is zero, both possible update probabilities are at most `b`. Require that no site-`1` clock ring up to time `t` has mark `U<b`. These forbidden marked rings form a rate-`b` Poisson process. On this event site `1` remains zero, regardless of the entire process to its right.

While site `1` is zero and the source pair at zero is `01`, a source update coalesces precisely for marks

\[
U<a
\quad\text{or}\quad
U\ge c,
\]

a set of total measure

\[
a+(1-c)=q.
\]

Require no such source mark up to time `t`. These forbidden marks form an independent rate-`q` process. The source then remains exactly `01` for the entire interval.

Call the intersection `E_t`. Then

\[
\boxed{
\mathbb P(E_t)=e^{-At}.
}
\tag{4.3}
\]

### 4.2 Force one left disagreement to be alive at time `t`

On `E_t`, site `-1` sees a fixed right pair `01` and begins in `11`.

Require its first clock ring to occur at time `s<=t` with mark `U<c`. The first-ring density together with the mark condition is

\[
c e^{-s}\,ds,
\]

and this update creates pair `10` at site `-1`.

While the pair is `10` with fixed right pair `01`, a ring coalesces it for

\[
U<b
\quad\text{or}\quad
U\ge c,
\]

of total measure

\[
\delta=b+1-c.
\]

Require no such coalescing mark after the birth time. The probability of this site-`-1` event is therefore at least

\[
\begin{aligned}
p_1(t)
&=
\int_0^t c e^{-s}e^{-\delta(t-s)}ds\\
&=
\boxed{
\frac{c}{c-b}
e^{-\delta t}
\left(1-e^{-(c-b)t}\right).
}
\end{aligned}
\tag{4.4}
\]

The clocks and marks used in (4.4) are independent of `E_t`.

On `E_t` the source itself contributes one disagreement at time `t`; on the additional event (4.4), site `-1` contributes a second. Thus

\[
\boxed{
\alpha(t)
\ge
L(t)
:=e^{-At}\left[1+p_1(t)\right].
}
\tag{4.5}
\]

Equivalently, with

\[
K=\frac{c}{c-b}=\frac{9999}{9899},
\]

\[
L(t)
=e^{-At}
+K e^{-(A+\delta)t}
-K e^{-(A+1)t}.
\tag{4.6}
\]

## 5. The lower bound stays above one through time 47

Differentiate (4.6):

\[
L'(t)
=e^{-(A+\delta)t}F(t),
\]

where

\[
F(t)
=-A e^{\delta t}
-K(A+\delta)
+K(A+1)e^{-(1-\delta)t}.
\tag{5.1}
\]

Since `1-delta=c-b>0`,

\[
F'(t)
=-A\delta e^{\delta t}
-K(A+1)(1-\delta)e^{-(1-\delta)t}
<0.
\tag{5.2}
\]

Moreover

\[
F(0)
=-A+K(1-\delta)
=c-A
=\frac{9897}{10000}>0.
\tag{5.3}
\]

Thus `L` is strictly increasing until one unique maximum and strictly decreasing afterwards. Since

\[
L(0)=1
\]

and exact rational exponential enclosures in the verifier give

\[
\boxed{
L(47)>1.008204288867933>1,
}
\tag{5.4}
\]

unimodality implies

\[
\boxed{
\alpha(t)>1
\qquad(0<t\le47).
}
\tag{5.5}
\]

This is not a survival theorem and it does not imply `alpha(t)>=1` for all times. It does prove that any finite-time contraction must wait beyond a substantial initial amplification regime.

## 6. Exact finite fixed-boundary computation

At rational parameters the fixed-boundary quantity `B_{L,R}^e(T)` is an ordinary rational CTMC followed by Poisson uniformization.

For the checkable instance

\[
L=R=3,
\qquad e=0,
\qquad T=1,
\]

the state space has

\[
4^4 2^3=2048
\]

states and seven state-independent rate-one clocks. Conditional on `n` clock rings, each ring location is uniform on the seven sites. The transition probabilities at each ring have denominator `10000`. The verifier therefore iterates the exact integer uniformized kernel and encloses the final Poisson series by rational alternating-series bounds on the exponential plus an explicit positive remainder estimate.

It obtains

\[
\boxed{
1.870443193102958
< B_{3,3}^{0}(1)
<1.870443193107048.
}
\tag{6.1}
\]

The two-sided causal errors give

\[
\boxed{
1.794490565598343
<\alpha(1)
<1.969732747054596.
}
\tag{6.2}
\]

The lower side of (6.2) is consistent with, but not needed for, the stronger protected-source interval theorem (5.5). The purpose of (6.1) is to verify that the fixed-boundary finite approximation is computationally exact and that no HJB/control optimization is required after Theorem 3.1.

No floating optimizer or Monte Carlo value is used in these certificates.

## 7. Why direct finite enumeration stops being informative

The lower theorem (5.5) rules out the desired inequality for all `T<=47`. Suppose one next tries to use the convergent sandwich (3.3) at a time just beyond this range.

At `T=47`, exact Poisson enclosures give

\[
\ell_{66}(47)
=0.010166471257955\ldots>0.01,
\]

whereas

\[
\ell_{67}(47)
=0.006682825976498\ldots<0.01.
\]

Thus a `1%` left causal error already needs `L>=67`. With `L>=67`, the right error has prefactor at least `68`, and

\[
68\,P(\operatorname{Pois}(47)\ge74)
=0.011230155115999\ldots>0.01,
\]

while

\[
68\,P(\operatorname{Pois}(47)\ge75)
=0.006901437158235\ldots<0.01.
\]

Hence `1%` on both sides requires at least

\[
L=67,
\qquad
R=74,
\]

already at time 47. The ordinary finite state space (before any Poisson uniformization) then has size

\[
\boxed{
4^{68}2^{74}=2^{210}.
}
\tag{7.1}
\]

For any `T>47` the two Poisson causal errors are larger at fixed `L,R`, so this scale does not improve.

Again, `1%` is only a diagnostic tolerance. A true contraction with a very large margin could tolerate larger errors. Equation (7.1) is therefore **not** a lower bound on the state size of every conceivable proof. It is evidence about the exact finite hierarchy now available: simply increasing the raw causal window is not a scientifically meaningful continuation of Assignment 007.

## 8. Exact blocker after the bounded block

The right-controller concern from Assignment 006 is resolved by (2.2). The finite approximation itself is also no longer vague: (3.3) gives a two-sided convergent sequence of ordinary finite CTMC values.

What prevents the finite theorem from deciding `alpha(T)<1` is the mismatch between two spatial scales:

1. actual near-East damage remains localized enough that finite-window computations at short times are small-dimensional;
2. the **causal** Poisson cone ignores the pre-exposure common-spin history and allows a fictitious left front moving at rate one for the entire block, so at the first times not excluded by (5.5) it demands windows of order the elapsed time.

The missing object is therefore a uniform tail estimate on the actual finite-time disagreement/front map, strong enough to replace

\[
\ell_L(T)=E[(\operatorname{Pois}(T)-L)_+]
\]

by a quantity which decays in `L` on the true near-East front scale. Such a theorem must retain the common spin **before first exposure**. Assignment 006 already showed why replacing that spin by an adversarially fresh value destroys the useful correlation. Importing the predecessor-trail reset-height drift would be circular for the same reason.

This is a materially narrower theorem than "use a more nonlocal norm" and satisfies the Meeting-016 hard-stop instruction: I do not propose a larger raw `L,R,T` run as the next step.

## 9. Consequences and interface with F

No global coalescence theorem is proved, so none of F's common-mass arguments may assume extinction of the full-line coupling.

Theorem 3.1 is nevertheless reusable for F's zero-boundary coefficient. For boundary distances larger than `R`, the same control-removal/causal argument replaces the far-right controller by a fixed boundary with explicit Poisson error; finitely many close-boundary cases still have to be treated separately as Meeting 016 states. This does not by itself prove `alpha_0(T)<1`.

The protected-source lower event is full-line and does not automatically transfer to every zero-boundary geometry. It should not be used to refute F's `alpha_0` criterion.

## 10. Status

### Proved

1. The Assignment-006 adversarial-right CTMC and a fixed-boundary CTMC differ in value by at most the explicit right causal error (2.2).
2. `alpha(T)` obeys the two-sided convergent fixed-boundary sandwich (3.3).
3. At the hard rational point, `alpha(t)>1` for every `0<t<=47` by an explicit protected-source event.
4. The exact finite value `B_{3,3}^0(1)` and the resulting `alpha(1)` sandwich are rigorously interval-certified.
5. At the first time scale not already excluded by the lower theorem, raw 1%-causal truncation requires an astronomically large naive full state space; this rules out "just enlarge the window" as a meaningful completion of the bounded block.

### Not proved

- `alpha(T)<1` for any `T`;
- `alpha(T)>=1` for every `T`;
- convective survival;
- global extinction of the common-uniform coupling;
- a sharp actual-front tail replacing the causal Poisson cone.

## Handoff

`unresolved after substantive work; exact alpha-certificate blocker: the adversarial right controller is no longer an obstruction, because alpha(T) has the two-sided convergent fixed-boundary sandwich B_{L,R}^e(T)-r_{L,R}(T) <= alpha(T) <= B_{L,R}^e(T)+r_{L,R}(T)+ell_L(T). At the hard point an explicit protected-source event proves alpha(t)>1 for every 0<t<=47. Thus any contraction must occur only after a long initial-expansion regime, while the causal Poisson errors at that scale already force raw windows of order T (1%-per-side at T=47 gives L>=67,R>=74, naive state count 2^210). A decision now requires a theorem controlling the actual disagreement/front tail with its pre-exposure common-spin history, or a genuine convective-survival theorem; larger L,R,T enumeration or another boundary controller is not a meaningful continuation.`
