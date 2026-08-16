# Group meeting 019: two-spin zero-frequency occupation closure fails; abandon common-uniform global-coalescence as the proof interface

Date: 2026-08-17

Professor review of:

- Meeting 018 and its explicit stopping rule;
- Student G successor commit `f2f0804`, `students/student-g/008-occupation-weighted-front.md`;
- `students/student-g/008-occupation-weighted-front-verifier.py` from the same return;
- G003/G006 only at the scopes used in G008;
- F010 and F012 for the signed-profile / Green interfaces;
- current `state.md` and `proof-spine.md`.

`state_narrowed: yes`.

Evidence pointer: G008 Sections 2--6 and its exact verifier. The route decision also uses the stopping rule stated in Meeting 018 and Assignment 008.

## Ruling in one sentence

G008 supplies the negative outcome explicitly authorized in Assignment 008: the retained two-spin first-exposure state does not close the zero-frequency occupation problem with the source-lifetime information currently proved. The common-uniform **global-coalescence / occupation** mechanism is therefore abandoned as a load-bearing proof interface. We do not enlarge the exposure state and do not issue a G009 continuation of that mechanism.

This does **not** refute the actual occupation estimate `(OCC)`, tail-shift agreement, extinction of the common-uniform coupling, or the positive-rates conjecture.

## Professor check: exact one-episode numbers

At the hard point

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\qquad
q=1-c+a=\frac1{5000},
\qquad
g=b-a=\frac{99}{10000},
$$

G uses the already accepted least-killing one-source comparison. With

$$
\mathfrak D=(b+q)(1+q)-a(1-c)=\frac{1020203}{100000000},
$$

the child-before-source-kill probabilities are

$$
\boxed{
h_0=\frac{1000197}{1020203},
\qquad
h_1=\frac{1019997}{1020203}.
}
$$

I recomputed the first-step equations

$$
(b+q)h_0=g+ah_1,
\qquad
(1+q)h_1=c+(1-c)h_0,
$$

and the displayed fractions. They are exact.

The true one-episode child probability is bounded above by this comparison; G does not use `h_0` as an actual lower bound.

## Professor check: the retained state is genuinely non-Markov after source death

Let `y=x+1` be the current source. Stop immediately after `y` has genuinely coalesced to common spin zero, while `x,x-1` remain coupled with retained spins `(s,t)`. The projected state is `(s,t,C0)`.

There are reachable actual histories with the same projection but different future return laws:

1. if the entire half-line `[y,\infty)` is coupled, `y` can never become disagreement again;
2. if `y+1` is still disagreeing, then with probability `1/2` the rate-one clock at `y` rings before the one at `y+1`, and conditional on that event a mark set of measure `g` creates disagreement at `y`.

Hence the second history has source re-entry probability at least

$$
\boxed{\frac g2=\frac{99}{20000}}
$$

before the next `y+1` ring, while the first has zero. This is an actual-history statement, not an immortal-source comparison.

I accept it as a precise state-sufficiency defect: `(s,t,C0/C1)` forgets residual right-ancestry capacity after a genuine source coalescence.

## Scope of the existing renewal facts

The distinction with G003 is load-bearing. G003 controls repeated exposure entries **while the same parent episode remains alive**. Once that parent coalesces, a later reinfection from the right is a new parent episode and G003 restarts rather than summing the all-depth sequence.

G006 proves that every fixed site is eventually permanently coupled, so the number of such episodes is almost surely finite for a finite initial seed. It does not give a uniform zero-frequency tail or expectation for their number. Therefore neither existing theorem supplies the missing post-coalescence return kernel.

## Professor check: robust closed two-spin Bellman envelope loses every strict factor

G defines a deliberately robust finite-depth closure of the **projected** state. It is an upper-certificate envelope, not an asserted lower process for the actual coupling. Its values obey

$$
r_0=h_0,
\qquad
\boxed{
r_n=\frac{h_0}{1-(1-h_0)r_{n-1}}.}
$$

The algebra gives

$$
1-r_n
=
\frac{(1-h_0)(1-r_{n-1})}
{1-(1-h_0)r_{n-1}},
$$

and therefore

$$
1-r_n
\le
\frac{1-h_0}{h_0}(1-r_{n-1}),
\qquad
\frac{1-h_0}{h_0}
=
\frac{20006}{1000197}
<\frac1{49}.
$$

Thus

$$
\boxed{r_n\uparrow1.}
$$

The verifier checks the exact recurrence and rational contraction of the deficit.

I accept the following **qualified** conclusion: if hidden post-coalescence ancestry is robustly closed on the same retained two-spin state using only the currently proved source-lifetime information, the resulting zero-frequency Bellman envelope has contraction-factor supremum one. No positive reweighting of the retained spin can make that closed envelope uniformly contractive.

I do **not** promote this to the stronger statement that every conceivable theorem using the two visible spins is mathematically impossible. A future theorem giving quantitative all-depth source-return information could change the closure. But that theorem would be new information not contained in the retained two-spin exploration or in G003/G006.

## Why the named all-depth episode theorem is not a reason to continue this interface

Let `N_i` be the number of maximal disagreement episodes at site `i` and

$$
O_i=\int_0^\infty D_i(t)\,dt.
$$

G records the elementary bounds

$$
\boxed{E N_i\le E O_i}
$$

because each episode contains the waiting time to the next independent rate-one ring at `i`, and

$$
\boxed{E N_i\le D_i(0)+c\,E O_{i+1}}
$$

by the disagreement-birth compensator.

These show what an all-depth source-return theorem would have to control: a zero-frequency episode/occupation observable of essentially the same kind as `(OCC)`. G008 does not supply a new mechanism for that theorem; it identifies it as the missing global quantity.

This is exactly the stopping case in Meeting 018. Continuing by adding ancestry depth, an episode counter, or a larger exposure state would move the unresolved zero-frequency object into the state rather than control it.

## Route decision: common-uniform global coalescence is no longer the disagreement interface

The common-uniform construction remains useful as an auxiliary finite-time comparison and all previously proved facts remain valid:

- fixed-site permanent coupling;
- convective-survival equivalence;
- moving-frame contraction;
- first-exposure probabilities and same-parent restart bounds;
- the actual-front first-discovery theorem from Meeting 018;
- G007's fixed-boundary approximation and finite-time noncontraction interval.

But we no longer require or pursue global extinction, integrable Hamming susceptibility, `(OCC)`, or an all-depth episode-count theorem as a step in the predecessor-trail proof.

No G009 is issued. Student G is idle.

## Return to the signed predecessor-trail spine

The reason to change representation is already visible in the accepted algebra. The positive-coupling route replaced a signed conditional-law difference by absolute disagreement occupation. That exposed a genuine but very expensive all-depth episode problem.

For any law `mu` with rightmost density `r`,

$$
r(1-r)(\mu^1-\mu^0)(f)
=\mu[(\eta_y-r)f].
$$

Thus the second term of the insertion identity

$$
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f)
$$

is intrinsically a **signed covariance**, not a positive disagreement mass.

At the invariant zero-boundary law, F010 already exploits this sign. With

$$
\phi_N=\eta_N-r_0,
\qquad r_0=\frac1{1+b},
$$

it proves the positive-frequency resolvent identity

$$
\pi_N\left[\phi_N((1+b)-\bar L)g\right]
=q_0r_0\pi_N[Dg]
$$

and consequently an explicit exponential separated-gap bound on `\pi_N(\phi_N f)`. The zero-frequency obstruction arose after splitting the first signed insertion into a mass branch and a positive disagreement branch and then trying to control the former by a global coupling.

The next proof-spine question is therefore whether the **full signed insertion can be recombined through one nonstationary segment** so that the troublesome zero-frequency pieces cancel before absolute values are taken.

This is not a claim that they do cancel. It is a bounded test of the representation that remains after the common-coupling interface is stopped.

## Next task

Student F receives one sharply bounded signed-recombination assignment. It starts from

$$
\nu_N:=\mathcal J_N\pi_N,
\qquad
(\mathcal J_N\mu)(f)=\mu((B\eta_N-c)f),
$$

lets this full signed measure evolve on the remaining `(N-1)`-site zero-boundary chain for one trail duration `u`, and applies the next centered insertion without first splitting into common mass and conditional-law disagreement.

The task is to determine whether the resulting two-insertion signed profile has a depth-uniform remote localization after the actual `L^1(w)` norm, or whether an unavoidable zero-frequency term survives recombination. This is `students/student-f/assignment-013.md`.

The result will decide whether the signed predecessor-trail route has a concrete mechanism left after the coupling stop. No matrix-product construction, finite-mode closure, or common-uniform occupation theorem is authorized inside that assignment.

## Ruling

- `state_narrowed: yes`.
- The actual two-spin projection forgets post-coalescence right-ancestry capacity; the explicit return-kernel gap is at least `99/20000`.
- G003 controls same-parent re-entry only; G006 supplies qualitative eventual local coupling but no zero-frequency episode tail.
- The robust finite-depth projected Bellman closure has `r_n->1`; the exact verifier supports this algebra.
- Actual `(OCC)`, tail-shift agreement, common-coupling extinction/survival, `J` decay, and the conjecture remain unresolved.
- Meeting 018's stopping rule is met. The common-uniform global-coalescence/occupation mechanism is abandoned as the proof interface.
- Do not enlarge the exposure state, add an ancestry counter, restart raw finite windows, or issue G009 as a continuation of this route.
- Student G is idle.
- Return to the signed predecessor-trail representation. Student F gets one bounded recombination test before any broader signed architecture is considered.
