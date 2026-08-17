# Group meeting 023: stationary boundary-control hierarchy reopens one proof-architecture test

Date: 2026-08-17

Professor review of:

- Meeting 022 and consultation 002's `no-credible-route` ruling;
- the principal's new proof-strategy exchange, now normalized in `notes/principal-stationary-boundary-control-strategy.md`;
- the current `state.md`, `proof-spine.md`, and Student G Assignment 009;
- the attached KCM book, specifically East-model Theorems 7.6 and 7.8 cited by the principal.

`state_narrowed: yes`.

Evidence pointer: the exact stationary occupation-polytope representation and LP duality checked below. The principal's reported LP widths remain numerical evidence only.

## Ruling in one sentence

The principal's new stationary boundary-control hierarchy is a **genuinely different architecture not ruled out by consultation 002**. It is concrete enough for exactly one bounded internal feasibility block on multiscale corrector concatenation. Student G continues the already-started `(J-SPEC)` route-decision task unchanged mathematically; Student F is activated on the new static screening test. The previous fallback "if G is unresolved, return immediately to no-credible-route" is superseded while F015 is active.

This does not revive the exhausted predecessor-trail/profile implementation, common-uniform occupation, trajectory-kernel contraction, or generic finite-box enlargement.

## 1. Professor check: invariant projections lie in the occupation polytope

Use the complemented spin convention from the principal note, so `1` is the East facilitator. For a block `x in {0,1}^N` and fixed right-boundary value `u in {0,1}`, let `L_N^u` be the finite generator.

Define

$$
\mathcal K_N
=
\left\{
 m(x,u)\ge0:
 \sum_{x,u}m(x,u)=1,
 \quad
 \sum_{x,u}m(x,u)L_N^uF(x)=0
 \ \forall F
\right\}.
$$

Let `mu` be any invariant law of the infinite IPS and put

$$
m_\mu(x,u)
=
\mu\bigl((\xi_0,\ldots,\xi_{N-1})=x,\xi_N=u\bigr).
$$

For every test `F` depending only on the first `N` sites, the infinite generator acts on `F` exactly as `L_N^{\xi_N}`. Stationarity therefore gives

$$
\sum_{x,u}m_\mu(x,u)L_N^uF(x)=0.
$$

Hence

$$
\boxed{m_\mu\in\mathcal K_N.}
$$

This part of the proposed hierarchy is exact and requires neither translation invariance nor a Markov assumption on the outside configuration.

## 2. Professor check: `K_N` is exactly a randomized stationary boundary-control relaxation

Conversely, let `m in K_N` and set

$$
\bar m(x)=\sum_u m(x,u).
$$

On states with `bar m(x)>0`, define

$$
\pi(u\mid x)=\frac{m(x,u)}{\bar m(x)}.
$$

Then for the averaged controlled generator

$$
L_N^\pi F(x)
=
\sum_u\pi(u\mid x)L_N^uF(x)
$$

one has

$$
\sum_x\bar m(x)L_N^\pi F(x)
=
\sum_{x,u}m(x,u)L_N^uF(x)=0.
$$

Thus every feasible occupation measure is realized by a finite state-dependent randomized boundary controller. `K_N` is not merely a formal LP relaxation; it is exactly the stationary occupation-measure set of that controlled finite chain.

This makes a uniform Bellman/corrector theorem over `K_N` mathematically meaningful.

## 3. Professor check: the hierarchy is nested

Take `m in K_{N+1}`. Project to the first `N` spins and use the old `N`th spin as the new boundary control:

$$
\widetilde m(x,u)
=
\sum_{v\in\{0,1\}}
 m((x,u),v).
$$

For every `F` on the first `N` spins,

$$
L_{N+1}^vF(x,u)=L_N^uF(x),
$$

because site `N` is outside the support of `F` and enters only as the right boundary of site `N-1`. Hence `tilde m in K_N`.

Therefore, for every fixed local observable `h` supported in the left part,

$$
\boxed{D_{N+1}(h)\le D_N(h).}
$$

The numerical widths reported by the principal are therefore sampling a genuine monotone hierarchy rather than unrelated finite boxes.

## 4. Professor check: exact LP dual and uniqueness implication

For

$$
D_N(h)
=
\sup_{m\in\mathcal K_N}m(h)
-
\inf_{m\in\mathcal K_N}m(h),
$$

finite-dimensional strong LP duality gives

$$
U_N(h)
=
\inf_F\max_{x,u}\bigl(h(x)-L_N^uF(x)\bigr),
$$

$$
\ell_N(h)
=
\sup_F\min_{x,u}\bigl(h(x)-L_N^uF(x)\bigr),
$$

and

$$
\boxed{D_N(h)=U_N(h)-\ell_N(h).}
$$

The sign of `F` is conventional.

If

$$
D_N(h)\to0
$$

for every local `h`, then any two infinite-volume invariant laws have the same expectation of every local observable, because both projections lie in `K_N`. Hence the invariant measure is unique.

This establishes a clean static reduction. It does **not** establish convergence from arbitrary initial states.

## 5. Why consultation 002 does not kill this route

Consultation 002 proved that the trajectory-valued spatial kernel `Q` satisfies

$$
Q(\mathbf0,\cdot)\perp Q(\mathbf1,\cdot)
$$

and therefore has no strict global path-space TV/KL contraction.

The occupation hierarchy does not ask for contraction of whole time trajectories. It asks whether the set of **one-time stationary local marginals** compatible with arbitrary state-dependent boundary control collapses as the controlled boundary is moved away.

The path-space isometry theorem therefore does not imply `D_N(h)` stays positive. The two architectures are mathematically distinct.

## 6. Check of the cited East input

The attached KCM book supports the pure-East ingredients claimed by the principal:

- Theorem 7.6: for the hard East model, the presence of an empty/facilitating site in the oriented future of a local observable gives exponential convergence of that observable to equilibrium;
- Theorem 7.8: finite-volume East has mixing time linear in the box size, including completely empty and more generally ergodic boundary conditions.

These statements do **not** directly prove the proposed noisy controlled inequality

$$
D_{2N}(h)
\le
(1-\rho)D_N(h)+Ce^{-\gamma N}.
\tag{R}
$$

The missing point is robustness under the actual soft dynamics and an arbitrary state-dependent boundary controller. In particular, one cannot simply condition on the absence of all non-East noise over an `O(N)` spacetime block; such an event has exponentially small probability in the block volume and cannot supply a fixed `rho>0`.

Any successful seed-and-East proof must use the noisy resets structurally, or prove a censoring/robustness lemma which survives them uniformly over the controller.

## 7. Why one block is justified

The principal's reported LP widths shrink strongly from `N=5` to `N=9` even at strict near-East residual points, and the hierarchy is now known to be exact and nested. This is qualitatively different from the finite-depth `J` growth table: there is a natural LP dual, a monotone finite-volume relaxation, and a precise candidate for repeatable block composition.

But larger LPs alone would not justify continuation. The load-bearing question is whether finite dual correctors **concatenate** into a theorem such as `(R)` or another scale-recursive contraction valid for every boundary controller.

That is Student F Assignment 015.

## 8. Relation to G009

G009 remains scientifically unchanged. It asks whether the old absolute-duration predecessor-trail norm is asymptotically supercritical. A proof `rho_J>1` would permanently clarify that the old `J` domination discards essential cancellation; it is useful even if the new occupation route succeeds.

Because G has now lost two sessions during long uninterrupted reasoning runs, Assignment 009 receives only a workflow addendum: commit nontrivial intermediate asymptotic reductions/certificates as soon as they become durable. This does not alter the mathematical task or stopping rule against larger-`n` evidence.

If G009 returns unresolved, the `J-SPEC` branch stops. It no longer forces the whole programme immediately back to `no-credible-route`, because F015 is a genuinely new input which did not exist at Meeting 022.

## 9. Stop rule for the new route

F015 is a feasibility test, not permission for indefinite controlled-LP enlargement.

A positive outcome must contain a **repeatable theorem**: a concatenation rule for Bellman/Poisson correctors, an exact block screening inequality of type `(R)`, or another multiscale estimate which forces `D_N(h)->0` on a genuine residual region.

A negative outcome may show that the finite-box correctors cannot be concatenated uniformly over the state-dependent controller, or that the proposed East ingredient requires a robustness statement which is false in the controlled noisy model.

If F015 returns only smaller numerical widths or larger rational LP certificates with no repeatability mechanism, stop this route rather than increase `N`.

The dynamic upgrade `(ZF)` is not active until the static screening mechanism is established.

## Ruling

- `state_narrowed: yes`.
- The stationary occupation-control hierarchy `K_N` is exact, nested, and has an exact Bellman/Poisson LP dual.
- `D_N(h)->0` for every local `h` would prove uniqueness of the invariant measure.
- The route is distinct from the path-space trajectory kernel and from all mechanisms stopped in Meetings 019--021.
- The cited hard-East theorems support only the pure-East ingredient; robustness to noisy resets and arbitrary state-dependent control is an unresolved load-bearing step.
- G009 continues unchanged mathematically, with an intermediate-commit workflow addendum.
- F015 is issued as one bounded corrector-concatenation / screening feasibility test.
- At most these two tasks are active; no third route is authorized.
