# Group meeting 017: fixed-boundary sandwich, long initial expansion, and stop of the raw random-map certificate implementation

Date: 2026-08-16

Professor review of:

- Student G successor, commit `769a985`, `students/student-g/007-random-map-hamming-contraction.md`;
- `students/student-g/007-random-map-hamming-contraction-verifier.py` from the same return;
- Meetings 015--016;
- current `state.md`, `proof-spine.md`, and the F012 interface retained in Meeting 016.

The change from `research:` to `student-g:` in the commit message prefix is operational only. G reports that its local git CLI disappeared during the block and it used the GitHub connector write API. This has no mathematical status.

state_narrowed: yes

Evidence pointer: G007 Sections 2--8, especially Theorem 3.1 and the protected-source argument in Sections 4--5; verifier for the exact/interval finite checks.

## Previous decision and stop condition

Meeting 016 authorized exactly one more execution block on the finite-time random-map coefficient

$$
\alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i)
$$

at the hard near-East point

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right).
$$

The stop condition was: if G007 returned unresolved and continuation amounted only to larger `L,R,T` computation, a more elaborate boundary controller, or generic matrix-product engineering without a new finite-approximation theorem, do not issue G008/F013 variants; reassess the route or use a bounded outside consultation.

G007 remains unresolved on the sign of `alpha(T)-1`. It does, however, prove a genuine new finite-approximation theorem. Therefore the literal clause "without a new finite-approximation theorem" is not satisfied. Nevertheless the new theorem itself shows that the raw finite-enumeration implementation has reached its useful limit at the first time scale not already excluded. The correct consequence is:

> stop the **raw finite-window/HJB certificate implementation** now. Any continuation must be a new structural theorem about the actual disagreement front or a genuine survival theorem, not G008 with larger windows.

No G008 or F013 is issued in this meeting.

## Professor verification: the adversarial right controller can be removed

For a finite window `[-L,R]` and a fixed common boundary spin `e` at `R+1`, let

$$
B_{L,R}^e(T)
$$

be the maximal expected disagreement count in `[-L,0]` at time `T`, over finite common initial backgrounds with one disagreement at zero. Let `A_{L,R}(T)` be the earlier controlled value in which the common spin seen at `R+1` may be chosen predictably.

G defines

$$
r_{L,R}(T)
=(L+1)P(\operatorname{Pois}(T)\ge R+1).
$$

Couple a controlled-boundary chain and a fixed-`e` chain with the same internal clocks and marks. A difference at `R+1` cannot affect site zero before a causal chain of at least `R+1` site rings has occurred. Hence

$$
P(\text{right boundary affects site }0\text{ by }T)
\le P(\operatorname{Pois}(T)\ge R+1).
$$

On the exceptional event the payoff discrepancy in `[-L,0]` is at most `L+1`. Therefore, uniformly over controls and initial states,

$$
\boxed{
0\le A_{L,R}(T)-B_{L,R}^e(T)\le r_{L,R}(T).
}
$$

I accept this argument. It resolves the earlier concern that the adversarial controller itself might be causing the failure of finite certificates.

## Professor verification: two-sided convergent fixed-boundary sandwich

Retain the left-discovery error

$$
\ell_L(T)=E[(\operatorname{Pois}(T)-L)_+].
$$

For any infinite single-flip initial pair, couple the full-line process to the fixed-boundary process on `[-L,R]`. The right-boundary mismatch contributes at most `r_{L,R}(T)` to the expected retained payoff, and disagreements left of `-L` contribute at most `\ell_L(T)`. This gives

$$
\alpha(T)
\le B_{L,R}^e(T)+r_{L,R}(T)+\ell_L(T).
$$

Conversely take a finite initial state attaining the maximum in `B_{L,R}^e(T)` and extend it arbitrarily to the full line. The finite payoff can exceed the retained full-line payoff only if right-boundary influence reaches zero, again at cost at most `r_{L,R}(T)`. Since full-line Hamming distance dominates its restriction to `[-L,0]`,

$$
\alpha(T)
\ge B_{L,R}^e(T)-r_{L,R}(T).
$$

Thus

$$
\boxed{
B_{L,R}^e(T)-r_{L,R}(T)
\le\alpha(T)
\le
B_{L,R}^e(T)+r_{L,R}(T)+\ell_L(T).
}
$$

For every fixed `T`, both causal errors vanish as `L,R\to\infty`. Hence ordinary fixed-boundary finite CTMC values form a rigorous two-sided approximation of `alpha(T)`.

I accept this as a genuine convergence theorem. It is materially stronger than Assignment 006's one-sided controlled certificate and is not another scalar Foster ansatz.

## Professor verification: protected-source lower bound through time 47

At the hard point put

$$
q=1-c+a=\frac1{5000},
\qquad
A=b+q=\frac{51}{5000},
$$

$$
\delta=1-c+b=\frac{101}{10000},
\qquad
K=\frac{c}{c-b}=\frac{9999}{9899}.
$$

Start with source pair `01` at site zero, common spin zero at site `1`, and common spin one at site `-1`.

Require no site-1 marked ring with `U<b`; this keeps site 1 equal to zero regardless of the farther-right environment, at cost `e^{-bt}`. Require no source marked ring in `[0,a)\cup[c,1]`; while the right spin is zero this keeps the source exactly `01`, at cost `e^{-qt}`. The two restrictions are independent, so the protected-source event has probability `e^{-At}`.

Conditional on that event, site `-1` sees the fixed right pair `01`. If its first ring occurs at time `s` with mark `U<c`, it becomes disagreement `10`; thereafter it remains disagreeing provided no mark in `[0,b)\cup[c,1]` occurs, whose total measure is `\delta`. Therefore the probability that site `-1` is disagreeing at time `t` under the protected source is bounded below by

$$
p_1(t)
=
\frac{c}{c-b}e^{-\delta t}(1-e^{-(c-b)t}).
$$

Thus

$$
\alpha(t)\ge L(t)
:=e^{-At}[1+p_1(t)]
=e^{-At}+K e^{-(A+\delta)t}-K e^{-(A+1)t}.
$$

G differentiates `L` and writes

$$
L'(t)=e^{-(A+\delta)t}F(t),
$$

where

$$
F'(t)<0,
\qquad
F(0)=c-A=\frac{9897}{10000}>0.
$$

Hence `L` has a unique maximum: it increases and then decreases. Since `L(0)=1` and the certified enclosure gives

$$
L(47)>1.008204288867933>1,
$$

one obtains

$$
\boxed{
\alpha(t)>1\qquad(0<t\le47).
}
$$

I independently checked the displayed formula at `t=47`; its value is approximately `1.0082042888679332`. The unimodality argument then gives the whole interval, not only the endpoint.

This is not a survival theorem. It does prove that any Hamming contraction must occur only after a long initial amplification period.

## Verifier status

The G007 verifier is not a Monte Carlo or floating optimizer. Its **displayed** endpoints are decimal floats, but the assertions are performed with `fractions.Fraction` and exact rational enclosures:

- `exp(-x)` is enclosed by alternating Taylor bounds after scaling to `x/m<=1`;
- Poisson tails and excesses are then bounded by exact rational arithmetic;
- the `B_{3,3}^0(1)` computation uses the exact denominator-10000 local kernel and uniformization of the 2048-state finite CTMC, with an explicit rational Poisson remainder;
- the time-47 lower event and causal-tail thresholds are certified by those rational intervals.

I checked the uniformization normalization: after summing over all seven site clocks, the conditional `7^{-n}` factor cancels the `7^n` in the Poisson ring-count weight, so the script's denominator `10000^n n!` before the final `e^{-7}` factor is correct.

The verifier therefore supports the finite arithmetic claims made in G007. It does not certify any of the unresolved global alternatives.

## Why the convergent finite approximation is not computationally decisive

At `T=47`, requiring only `1%` error from each causal side already forces

$$
L\ge67,
\qquad
R\ge74,
$$

with naive finite state count

$$
4^{68}2^{74}=2^{210}.
$$

The `1%` choice is only a scale diagnostic, not a lower bound for every proof. But the diagnostic is enough for the route decision: all times `T<=47` are rigorously noncontractive, while the explicit causal approximation at the first admissible time already needs a state space far outside the bounded computation envisaged in Assignment 007. Larger `T` worsens the raw causal errors at fixed windows.

Thus the two-sided convergence theorem validates the finite approximation mathematically but does not make direct enumeration a plausible proof strategy.

## Exact remaining structural alternatives

G correctly identifies what would be genuinely new rather than a larger computation:

1. **Actual-front theorem.** Replace the causal Poisson error by a uniform tail estimate for the true disagreement/front process, on its actual near-East scale, while preserving the common-spin history before first exposure.
2. **Convective-survival theorem.** Construct a genuine finite-seed survival mechanism, e.g. a valid block/percolative comparison preserving the exposure-time common state.

The second would close every route requiring eventual global coalescence of this synchronous coupling. The first could make the finite-time contraction diagnostic tractable, but it is a new probabilistic theorem, not a finite-certificate refinement.

Importing the predecessor-trail reset-height drift remains circular: that reset chain already assumes the one-step composition structure which the actual-front theorem would need to justify.

## Expected-value reassessment

The group has now spent several blocks eliminating local scalar architectures and several more reducing the remaining profile/coupling questions to finite-time common-map damage. The random-map line has produced real mathematics:

- fixed-site permanent coupling;
- convective-survival equivalence;
- moving-frame contraction;
- submultiplicative Hamming amplification;
- Green-response control by damage susceptibility;
- a convergent two-sided finite approximation;
- a rigorous noncontraction interval through time 47.

But even **success** on `alpha(T)<1` would still leave the signed all-depth profile composition and final `J_{x,r}` estimate to be built. The expected payoff of another internal block devoted solely to engineering the common-uniform Hamming contraction has therefore fallen substantially.

The natural next question, actual-front behavior with pre-exposure common history, is mathematically distinct and potentially decisive, but it is also close to a new research programme inside the proof. Before investing another student block, use a bounded outside consultation to assess whether this front theorem or convective survival has a credible short structural route, and whether either is plausibly easier than attacking the signed predecessor-trail quantity directly.

## Direction decision

1. **Stop the raw finite-window/HJB random-map certificate implementation.** Do not enlarge `L,R,T` and do not introduce another right-boundary controller.
2. **Do not issue G008 or F013.** Both students are idle after their current responses.
3. **Do not authorize generic matrix-product/nonlocal-norm engineering.**
4. **Use one bounded outside consultation** on the actual disagreement front / convective-survival alternative. The consultant is not a new graduate student and does not change the fixed scientific target.
5. After that consultation, the Professor must choose one of:
   - continue with a sharply stated actual-front/survival theorem if the consultant supplies a credible structural mechanism;
   - abandon global coalescence of the common-uniform coupling as a proof interface and return to the signed predecessor-trail spine with a different disagreement representation;
   - if neither has adequate expected value, record that this proof route is presently exhausted and reassess the remaining non-coupling proof-spine mechanisms under the principal-fixed target.

## Ruling

- `state_narrowed: yes`.
- The adversarial right controller is quantitatively removable.
- `alpha(T)` has a rigorous two-sided fixed-boundary finite approximation with explicit causal errors.
- At the hard near-East point, `alpha(t)>1` for every `0<t<=47`.
- The G007 verifier's decimal output is backed by exact rational interval assertions; it is not a floating-point proof.
- Neither finite-time Hamming contraction, global extinction, nor convective survival is proved.
- The raw finite random-map certificate implementation stops here.
- No G008/F013 variant is issued.
- One bounded outside consultation on the true disagreement-front/survival mechanism is authorized before any further internal block.
