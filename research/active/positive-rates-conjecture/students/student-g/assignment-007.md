# Student G assignment 007: decide the finite-time random-map Hamming contraction

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/015-local-coalescence-convective-escape-and-random-map-test.md`;
- your `006-common-coupling-survival.md` and verifier;
- Meetings 012 and 014 only as needed for the coupling/profile interface;
- current `proof-spine.md`;
- Student F `assignment-012.md` only for awareness. Do not depend on its outcome.

The scientific target remains the positive rates conjecture for simple IPS.

## What is accepted from Assignment 006

For every strict residual point and every finite common-uniform disagreement seed:

1. every fixed site becomes permanently coupled almost surely;
2. survival is equivalent to convective escape to `-infinity`;
3. with `q=1-c+a`,
   $$
   \mathcal L^{\rm coup}D_i\le-qD_i+cD_{i+1};
   $$
4. for every `z>c/q`,
   $$
   E\sum_i z^iD_i(t)
   \le e^{-(q-c/z)t}\sum_i z^iD_i(0);
   $$
5. the finite-time single-flip Hamming amplification
   $$
   \alpha(t)=\sup_{\eta,i}E\,d_H(\Phi_t\eta,\Phi_t\eta^i)
   $$
   is finite and submultiplicative;
6. if `alpha(T)<1` for one finite `T`, every finite seed dies out with an exponential block-time tail;
7. for finite `L,R`, the controlled-window quantity `A_{L,R}(T)` satisfies
   $$
   \alpha(T)
   \le A_{L,R}(T)+E[(\operatorname{Pois}(T)-L)_+].
   \tag{C}
   $$

At

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

short time is genuinely expansive:

$$
\left.\frac d{dt}E|D_t|\right|_{t=0}
=\frac{9997}{10000}>0.
$$

Do not use the predecessor-trail reset-height drift as an embedded chain for this actual coupling; that would be circular.

## Objective

Decide whether the exact finite-time block criterion

$$
\boxed{\alpha(T)<1}
$$

holds at the strict rational near-East point above.

This is a bounded execution of the finite random-map diagnostic from Assignment 006. It is **not** permission to begin general matrix-product or nonlocal Foster engineering.

A successful positive result gives a quantitative extinction theorem for the actual common-uniform disagreement process. A successful negative result should prove genuine convective survival or another theorem that rules out finite-time Hamming contraction, not merely fail to find a certificate.

## Preferred route A: rigorous finite controlled-CTMC certificate

Exploit `(C)` aggressively.

Construct an exact or rigorously interval-certified computation of

$$
A_{L,R}(T)
$$

for selected finite `L,R,T`. The state contains:

- the full coupled-pair state on `[-L,0]`;
- the agreed common spins on `[1,R]`;
- an adversarial predictable common boundary spin at `R+1` used only when site `R` rings.

The terminal payoff is the disagreement count in `[-L,0]`.

You may use continuous-time dynamic programming, uniformization, or another exact finite-state formulation. A useful rigorous upper construction is allowed to be more adversarial than the actual controller, provided the domination is proved.

If uniformization is used, exploit that all site clocks have state-independent total ring rate. Rational transition probabilities at the hard rational parameter point should be retained. Transcendental Poisson weights or matrix exponentials may be enclosed by explicit rational intervals with certified tails; a floating optimizer value alone is not a proof.

The target certificate is one explicit triple `(L,R,T)` and a rigorously verified inequality

$$
A_{L,R}(T)+E[(\operatorname{Pois}(T)-L)_+]<1.
$$

If found, derive the resulting numerical/exact `rho<1` and state the extinction tail

$$
P(\tau>nT)\le \rho^n|D_0|.
$$

## Preferred route B: tighten the finite hierarchy before brute force

If the controlled right boundary is too pessimistic, derive a **rigorous convergent two-sided truncation** for `alpha(T)` rather than simply increasing state size.

For example, compare the true process with a finite window having a fixed or explicitly enumerated right boundary and bound the effect of the omitted right environment by a causal-cone term. Any such theorem must state the exact error and why it is uniform over the infinite initial common background.

A result of the form

$$
\alpha(T)
\le B_{L,R}(T)+\ell_L(T)+r_R(T),
\qquad
\ell_L(T),r_R(T)\to0
$$

for an exactly computable finite quantity `B_{L,R}(T)` would be valuable even before a crossing below one, provided it is genuinely convergent and not another local credit ansatz.

## Preferred route C: rigorous survival / lower obstruction

If evidence strongly points against `alpha(T)<1`, do not report failure of the upper certificate as survival evidence.

A negative conclusion must establish something structural, preferably:

- positive-probability convective survival from an explicit finite seed; or
- a theorem implying `alpha(T)>=1` for every `T>0`.

A single time with `alpha(T)>1`, or a finite controlled upper bound above one, proves neither.

A block-survival comparison is allowed, but spacetime blocks, dependence, orientation/common-spin history, and the supercritical criterion must be explicit. Do not treat the common spin at first exposure as adversarially fresh or favorably fresh without a valid coupling comparison.

## Structural compression before large computation

The naive state count `4^(L+1) 2^R` grows quickly. Before pushing large windows, look for exact reductions that preserve the value function:

- translation/reflection is limited by orientation, so prove any symmetry before using it;
- collapse states only when their future controlled transition laws and terminal disagreement payoffs are identical;
- exploit one-sided causal ordering;
- exploit the fact that sites to the right remain diagonal;
- use monotonicity of the controller only if proved from the Bellman operator.

Do not spend the block only increasing `L,R` numerically.

## Interface with Student F

F is in flight on Assignment 012, deciding tail-shift agreement of the projective half-line invariant law.

If you prove `alpha(T)<1`, report the exact graphical block statement, not merely the scalar `rho`. The later interface would condition the disagreement branch on a complete common-coupling slab of length `T`; F's signed mass profile would still have to retain its duration variables and tail-shift/profile errors.

If you prove convective survival, state only the narrow consequence: F cannot rely on eventual global coalescence of this synchronous coupling. Do not infer failure of the signed trail route or of ergodicity.

The Professor will hold the promised route-level expected-value review when F012 returns. This assignment is deliberately bounded to the exact `alpha` diagnostic already exposed by Assignment 006.

## What not to do

Do not:

- revive the exposed-only or 16-phase scalar product correctors;
- import the predecessor-trail reset-height drift into the actual disagreement process;
- treat an optimizer/simulation output as a theorem;
- infer survival because a finite upper certificate stays above one;
- infer extinction from local fixed-site coalescence or from the moving-frame `V_z` contraction;
- launch an unrestricted matrix-product/nonlocal norm construction;
- replace `alpha(T)` by a different quantity without proving the implication needed for extinction or survival.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-g/007-random-map-hamming-contraction.md`

with rigorous certificate code beside it when computation is used.

End with one of:

- `finite-time common-coupling contraction proved: alpha(T)<=...<1 at T=... via ...`;
- `convective survival proved from finite seed: ...`;
- `finite-time Hamming contraction refuted because: ...`;
- `unresolved after substantive work; exact alpha-certificate blocker: ...`.
