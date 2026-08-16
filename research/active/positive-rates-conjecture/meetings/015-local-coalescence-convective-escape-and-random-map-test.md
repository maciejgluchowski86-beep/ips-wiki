# Group meeting 015: finite disagreement is locally erased; global coupling viability is a convective random-map problem

Date: 2026-08-16

Professor review of:

- Student G successor-session commit `78470a1`, `students/student-g/006-common-coupling-survival.md`;
- exact local verifier commit `43f4bb1`, `students/student-g/006-common-coupling-survival-verifier.py`;
- Meetings 012--014;
- current `state.md` and `proof-spine.md`;
- Student F Assignment 012 only for interface awareness.

Operational correction: the replacement G session committed Assignment 006 about two minutes before Meeting 014 was committed, but those commits were not seen while Meeting 014 was composed. Meeting 014 therefore incorrectly records replacement G as still in flight. Its mathematical ruling on F is unaffected. This meeting records the G ruling without rewriting that history.

state_narrowed: yes

Evidence pointer: `students/student-g/006-common-coupling-survival.md`, especially Sections 1--10, and `006-common-coupling-survival-verifier.py` for the local transition algebra.

## Previous coupling question

Meeting 012 closed the complete nearest-neighbour scalar edge-product/coboundary Foster class. Assignment 006 therefore asked a more structural question: is the actual common-uniform coupling itself a viable global coalescence mechanism near East, or can a finite disagreement seed survive forever?

G does not prove survival or extinction. It does prove that the only possible survival mechanism is convective escape to the left and reduces quantitative extinction to a genuine finite-time random-map contraction problem.

## Professor verification: no spontaneous disagreement to the right

Use the common graphical construction. If

$$
D_i=D_{i+1}=0,
$$

then both copies present the same local pair to the same uniform mark at an update of site `i`, so the update cannot create disagreement at `i`. Hence once a right half-line is coupled, it stays coupled forever.

For a finite disagreement seed let

$$
R_t=\max D_t
$$

while `D_t` is nonempty. The rightmost disagreement has a coupled right neighbour. The already checked common-uniform local table gives coalescence probability at its own rate-one update at least

$$
q=1-c+a>0.
$$

Once that rightmost disagreement coalesces, it cannot reappear. Therefore `R_t` is nonincreasing, and while nonempty the waiting time for its next strict decrease has conditional tail at most `e^{-qt}`.

Iterating at the successive rightmost-coalescence stopping times gives

$$
P(\tau>t,\ R_t>R_0-m)
\le P(\operatorname{Pois}(qt)<m).
$$

I accept this stopping-time argument. In particular, for every finite initial seed and every fixed site `j`, there is an almost surely finite time after which site `j` is permanently coupled.

This is a stronger structural statement than the earlier same-parent restart estimate and uses the actual common-uniform process, not the predecessor-trail reset coupling.

## Professor verification: survival is exactly convective escape

Let `L_0=min D_0`, and let `sigma_m` be the first time site `L_0-m` becomes disagreeing. One-sided nearest-neighbour propagation implies that discovery of the `m`-th new site to the left requires at least `m` successive rate-one site rings in causal order. Thus

$$
P(\sigma_m\le t)
\le P(\operatorname{Pois}(t)\ge m).
$$

If the finite seed survives forever, the permanent rightmost-coupling argument forces infinitely many strict decreases of `R_t`, hence `R_t\to-\infty`; every intermediate site must therefore be discovered. Conversely, if every `sigma_m` is finite, finite speed gives `sigma_m\to\infty`, so disagreements occur at arbitrarily large times and the absorbing empty state was never reached.

Therefore

$$
\boxed{
\{D_t\ne\varnothing\ \forall t\ge0\}
=
\{\sigma_m<\infty\ \forall m\ge1\}
\quad\text{a.s.}
}
$$

for every finite nonempty seed.

Thus finite-seed survival, if it exists, is purely **convective survival to `-infinity`**. There is no persistent disagreement mode in any fixed spatial window.

## Professor verification: additive moving-frame contraction

G proves the exact local drift inequality

$$
\boxed{
\mathcal L^{\rm coup}D_i
\le -qD_i+cD_{i+1}.
}
$$

The cases are direct: no creation when both local pairs agree; creation at an exposed agreed site is at most `c`; and any existing disagreement coalesces at intensity at least `q`.

The verifier checks all 16 local pair/right-pair cases exactly at the hard rational point.

For

$$
V_z(D)=\sum_i z^iD_i,
$$

with `z>c/q`, summation gives

$$
\mathcal LV_z
\le-\left(q-\frac cz\right)V_z.
$$

Hence

$$
\boxed{
E V_z(D_t)
\le e^{-(q-c/z)t}V_z(D_0).
}
$$

This is a legitimate exponentially contracting moving-frame norm. It does **not** imply global extinction because a disagreement cloud translating left is discounted exponentially by `z^i`.

At

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

`q=1/5000`, and `z=10000` gives

$$
q-c/z=\frac{10001}{100000000}>0.
$$

## Professor verification: finite-time Hamming amplification

Let `Phi_t` be the random map generated by one common graphical slab and define

$$
\alpha(t)
=
\sup_{\eta,i}
E\,d_H(\Phi_t\eta,\Phi_t\eta^i).
$$

Finite speed gives `alpha(t)<infinity` (G records the simple bound `alpha(t)<=1+t`). For two finite-difference initial configurations, interpolate by single-spin flips and use the triangle inequality under the same random map. This gives

$$
E d_H(\Phi_t\eta,\Phi_t\xi)
\le\alpha(t)d_H(\eta,\xi).
$$

Independent graphical slabs then imply

$$
\boxed{
\alpha(t+s)\le\alpha(t)\alpha(s).
}
$$

Therefore one strict finite-time inequality

$$
\boxed{\alpha(T)<1}
$$

would imply, for every finite seed,

$$
E|D_{nT}|\le\alpha(T)^n|D_0|,
\qquad
P(\tau>nT)\le\alpha(T)^n|D_0|.
$$

I accept this as a genuine nonlocal block path-coupling criterion. It bundles all damage creation and clearing inside a time slab before charging Hamming norm; it is not one of the refuted spatial product correctors.

## Professor verification: finite controlled-CTMC upper certificate

For integers `L,R>=0`, G keeps the full coupled state on `[-L,0]`, the agreed common spins on `[1,R]`, and replaces the common spin at `R+1` seen by updates of site `R` by an arbitrary predictable control `z in {0,1}`. This enlarges the actual right environment.

Let `A_{L,R}(T)` be the maximal expected disagreement count in `[-L,0]` at time `T`, optimized over all finite initial common backgrounds with one discrepancy at zero and over the boundary control. This is a finite-state continuous-time control problem of size at most

$$
4^{L+1}2^R.
$$

The actual infinite process is one admissible controlled history on the retained window. Disagreements beyond `-L` are bounded by the left-discovery Poisson tail. Consequently

$$
\boxed{
\alpha(T)
\le
A_{L,R}(T)
+E[(\operatorname{Pois}(T)-L)_+].
}
$$

I accept this as an exact certificate hierarchy. A finite verified inequality with right side below one proves quantitative global extinction. No such inequality has yet been obtained.

The controller enlargement can be pessimistic at small `R`; Assignment 007 should not interpret failure of one finite certificate as evidence of survival.

## Near-East stress check

At the hard rational point, take a single `01` disagreement at site zero, common right spin zero, and common left spin one. The source coalesces at rate `q`, while an update at the left child creates a disagreement at rate `c`. Hence

$$
\boxed{
\left.\frac d{dt}E|D_t|\right|_{t=0}
=c-q
=\frac{9997}{10000}>0.
}
$$

The verifier checks this exactly. Thus `alpha(t)>1` for all sufficiently small positive times. Any eventual Hamming contraction must be genuinely finite-time and nonlocal, with initial expansion later outweighed by clearing.

## Circularity check

G correctly does not import the predecessor-trail reset-height drift into the actual common-uniform process. The trail reset chain allows at most one new unresolved level per transfer and then applies a certified clearing variable; the actual continuous-time disagreement cloud can create many descendants during one source lifetime. Identifying these two chains would assume the global composition theorem under investigation.

The same-parent geometric restart theorem is likewise retained only at its proved stopping-time scope.

## Interface with F

F's common-mass results are unaffected. If a later block proves `alpha(T)<1`, the mass/disagreement decomposition could condition its disagreement channel on genuine complete common-coupling slabs of length `T`; the return object would be the full random-map block, not a 16-phase scalar cocycle. This would still require compatibility with F's duration-resolved profile norm and would not by itself prove `J_{x,r}->0`.

If convective survival is proved instead, the narrow conclusion is that no proof may require eventual global coalescence of this synchronous coupling. Local common-coupling identities and the independent common-mass profile analysis survive.

## Direction judgment

Assignment 006 is another unresolved endpoint, but it materially narrows the coupling question. The previous vague survival/extinction problem is now split into:

1. a proved local-erasure/moving-frame theorem;
2. a precise convective-survival alternative;
3. a finite-time random-map coefficient `alpha(T)` whose strict contraction would settle quantitative extinction;
4. an exact finite controlled-CTMC upper-certificate hierarchy for that contraction.

This is enough to justify one bounded execution block on `alpha(T)`. It is **not** authorization for general matrix-product or nonlocal-norm engineering.

Student F Assignment 012 is still in flight. The promised route-level expected-value review remains due when F012 returns. G may in parallel execute the finite `alpha(T)` diagnostic because that is the exact theorem Assignment 006 reduced to, rather than a new architecture.

## Ruling

- `state_narrowed: yes`.
- Every finite disagreement seed becomes permanently coupled at each fixed site.
- Finite-seed survival is equivalent to convective escape to `-infinity`.
- The actual coupling has the exponential moving-frame Lyapunov family `V_z` for every `z>c/q`.
- The finite-time single-flip Hamming coefficient `alpha` is finite and submultiplicative.
- `alpha(T)<1` at one finite time would imply exponential global extinction from every finite seed.
- `alpha(T)` has an exact finite controlled-CTMC upper-certificate hierarchy with explicit Poisson left-cone error.
- At the hard rational point the worst local geometry is initially expansive, so any Hamming contraction must be genuinely nonlocal in time.
- Neither convective survival nor global extinction is proved.
- G is assigned one bounded finite-time random-map certificate block. F continues Assignment 012 unchanged. The route-level review remains scheduled when F012 returns.
