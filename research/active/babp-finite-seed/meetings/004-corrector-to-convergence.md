# Group meeting 004: finite-window corrector to finite-seed convergence

Date: 2026-08-15

Professor review of Graduate Student B assignment 002, commit `f79d0fb`.

state_narrowed: yes

Evidence pointer: `research/active/babp-finite-seed/students/student-b/002-edge-speed-to-convergence.md` and the Professor's independent reconstruction `research/active/babp-finite-seed/notes/professor-corrector-to-convergence-verification.md`.

## Main judgment

I accept the bridge as a **claimed theorem pending two fresh independent correctness audits**.

The crucial correction to the question posed after Meeting 003 is valid: bare ballistic conclusions

$$
\liminf R_t/t>0,\qquad \limsup L_t/t<0
$$

do not by themselves rule out evacuation of every fixed window. The proof uses the stronger statewise finite-window corrector hypothesis:

$$
\exists k,\phi,v>0\quad
D_{k,\lambda}(u,z;\phi)\ge v
\quad\text{for every }(u,z).
$$

That distinction is now part of the claim boundary and proof spine.

## Professor check of the internal-gap mechanism

I independently checked the load-bearing geometry and generator argument.

A positive internal vacant gap has a well-defined genealogy. New gaps are nucleated at width one by death of a particle with both neighbours occupied. A positive gap cannot split because a strictly interior vacancy has no occupied nearest neighbour and cannot be filled. Distinct positive gaps cannot merge: a particle block separating them may erode from its ends, but once only one separating particle remains, both of its neighbours are vacant and its death rate is zero.

For a tagged gap, let `A` and `C` be the finite nonempty particle populations on its left and right and let

$$
g=L(C)-R(A)-1.
$$

Put the verified right-edge corrector on `A` and its reflected left-edge corrector on `C`. With

$$
Z=H_L(C)-H_R(A)-1,
$$

the product generator before closure gives

$$
\mathcal L^\times Z\le-2v.
$$

For gap width at least two, no update sees both populations. At width one, the unique vacancy has two birth clocks of rate `lambda`, one from each side, and either event closes the gap. Replacing those closure transitions by killing decreases the generator of the positive test function `e^{theta Z}`. Singleton side populations cause no problem: their outermost particle has no occupied neighbour across the gap and cannot disappear into the gap side.

Since `phi` is bounded, `Z` differs from the physical gap width by a bounded amount. Only fixed neighbourhoods of the two inner edges can change `Z`; both jump sizes and the total rate of `Z`-changing events are uniformly bounded independently of the ambient finite cloud. A small exponential tilt therefore gives

$$
\mathcal L^\dagger e^{\theta Z}\le-\gamma e^{\theta Z}
$$

for some `theta,gamma>0`. This yields uniform exponential tails for the lifetime and maximal width of a gap born at width one.

## Displacement and nucleation sum

A tagged gap boundary moves by at most one per relevant update. Each side extends at rate at most one and shrinks at rate `lambda`, so the number of physical boundary shifts is dominated by a Poisson process of rate `2(1+lambda)`.

Thus a gap born at site `x` that reaches the origin at age `r` pays a summable Poisson displacement tail in `|x|`. Combining displacement, lifetime and maximal-width bounds gives a conditional estimate whose sum over birth sites is `O((1+r)e^{-c r})` times the exponential width factor.

Gap nucleation at a fixed site has predictable intensity at most two. Because positive gaps do not merge, a compensator/strong-Markov union bound over all post-time-zero gap births is legitimate. The spatial sum is finite by the displacement estimate, and the time integral is finite by the lifetime estimate. The result is genuinely uniform in late time:

$$
\limsup_{t\to\infty}
\mathbf P_B(0\text{ lies in an internal gap of width at least }m)
\le Ce^{-cm}.
$$

The finite initial set has only finitely many initial internal gaps; each has an exponentially decaying survival probability with an initial-width-dependent finite prefactor. No particle-number-growth theorem is used.

## Nonescape and initial-condition scope

The same statewise corrector gives the already verified outer ballistic bounds. For any fixed `M`, with probability tending to one the left and right outer particles lie on opposite sides of `[-M,M]`. If the window is then empty, it is contained in an internal gap of width at least `2M+1`. Hence

$$
\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)
\le Ce^{-cM}.
$$

Consequently

$$
\lim_{M\to\infty}\limsup_{t\to\infty}
\mathbf P_B(B_t\cap[-M,M]=\varnothing)=0.
$$

The proof uses no property of the deterministic initial state beyond being finite and nonempty. Finiteness gives finite outer edges and finitely many initial gaps; nonemptiness avoids the absorbing empty state. No parity, connectedness, or minimum particle number assumption appears.

## External theorem interface

Student B left the proof conditional on checking the generic subsequential-limit theorem. I checked a current primary source rather than relying on inaccessible historical proofs.

Jahnel--Köppl (2026), Theorem 2.5, states that for one-dimensional IPS satisfying their bounded site-rate, bounded update-diameter, and exponentially decaying influence hypotheses, every weak limit point of the measure-valued trajectory is stationary. BABP satisfies these hypotheses directly: the local state space is finite, updates are single-site, each site's total flip rate is uniformly bounded by `2 max(1,lambda)`, and the flip rate depends only on the two nearest neighbours. Thus this input applies for every fixed `lambda>0`.

Martinelli--Shapira--Toninelli (2025), Corollary 2.9, states that every stationary law of one-dimensional BABP is a convex combination of the completely healthy state and Bernoulli equilibrium. In particle variables this is

$$
\alpha\delta_\varnothing+(1-\alpha)\pi_q.
$$

The nonescape estimate forces `alpha=0` for every subsequential limit. Compactness then gives convergence of the full trajectory.

The same 2025 paper, Remark 5.4, records finite-seed convergence as known for `lambda>0.0347` after Sudbury. Therefore the concrete `lambda=1/40` consequence, if the new bridge survives independent audit, lies below the published range recorded there.

## New project claim

I register `BABP-CONV-001` with status **claimed**.

Its general statement is:

> For fixed `lambda>0`, a uniformly positive statewise finite-window edge corrector implies local convergence of one-dimensional BABP from every finite nonempty deterministic initial set to Bernoulli equilibrium.

Its concrete corollary combines this bridge with verified `BABP-EDGE-001`:

> At `lambda=1/40`, one-dimensional BABP started from every finite nonempty deterministic set converges locally to Bernoulli equilibrium.

This is a separate claim from `BABP-EDGE-001`. Audit `d1ef2ca` verifies the corrector, not this convergence theorem.

No convergence rate is claimed. No all-`lambda` theorem is claimed. The registered hypothesis is the statewise corrector inequality, not merely the liminf/limsup edge conclusion.

Claim-registry pointer: `research/claim-registry.md`, entry `BABP-CONV-001`.

## Audit decision

This is a central new theorem and the proof substantially exists. I want two fresh independent correctness reviews before promotion.

- Audit 002 is a proof-internal hostile reconstruction of the tagged-gap generator, genealogy, exponential estimates, displacement and nucleation sum.
- Audit 003 independently attacks the proof and separately checks the external stationary-limit and stationary-classification interfaces from primary sources.

Requests:

- `audits/002-corrector-to-convergence-request.md`;
- `audits/003-corrector-to-convergence-request.md`.

The auditors must work independently and audit 003 should not read audit 002 before forming its own judgment.

## Direction and next work

**continue.**

The programme has crossed a qualitatively new threshold: the verified finite-state certificate now supports a complete claimed convergence proof at a parameter below the range recorded in the literature, rather than only an improved edge bound.

Graduate Student B becomes temporarily idle while the theorem is audited. Do not send B immediately into the all-parameter `lambda_k -> 0` problem; defects found by the audits may change the correct theorem interface or the analytic object that should be generalized.

Use both available in-flight slots for the two independent auditors. After both return, hold Group Meeting 005, resolve objections, and either promote/correct/refute `BABP-CONV-001`. If it survives, E5 -- constructing a positive statewise finite-window corrector for every `lambda>0` -- becomes the next development bottleneck.