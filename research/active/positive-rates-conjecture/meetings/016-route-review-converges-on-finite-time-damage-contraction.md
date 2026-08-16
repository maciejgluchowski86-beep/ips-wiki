# Group meeting 016: route-level review; profile and coupling sides converge on finite-time damage contraction

Date: 2026-08-16

Professor review of:

- Student F, commit `2093c22`, `students/student-f/012-tail-shift-agreement.md`;
- original verifier commit `3750a53`, `students/student-f/012-tail-shift-agreement-verifier.py`;
- subsequent verifier repair commit `5494008`;
- Student G `006-common-coupling-survival.md`, Meeting 015, and G's in-flight Assignment 007;
- current `state.md` and `proof-spine.md`.

This is the promised route-level expected-value review after F012 and G006. G007 is already in flight because Meeting 015 authorized one bounded execution of the exact finite-time diagnostic exposed by G006.

state_narrowed: yes

Evidence pointer: F012 Sections 2--8 and 10; G006 Sections 4--7; Meeting 015.

## Verifier incident

The verifier as originally committed in `3750a53` does **not** run to completion. Its symbolic geometric-series assertion asks SymPy to simplify an infinite sum with symbolic `rho>0`; SymPy retains the convergence condition `rho<1` in `Piecewise` form, so the asserted bare symbolic identity does not simplify to zero.

This is not treated as a passing certificate. The principal independently reran the script after changing only that assertion to select the `rho<1` branch; all remaining exact checks passed. The underlying identity

$$
\sum_{n=K}^\infty \rho^n\left(T+\frac{T^2}{2}\right)
=
\left(T+\frac{T^2}{2}\right)\frac{\rho^K}{1-\rho},
\qquad 0<\rho<1,
$$

is elementary and is proved directly in the report.

F subsequently committed `5494008`, replacing the problematic symbolic `rho` check by an exact rational test `rho=2/5`. That repair addresses the tooling defect rather than changing the mathematical argument. The ruling below rests on proof reconstruction, not on treating the failed `3750a53` artifact as successful.

## F012: accepted Green-response / damage-susceptibility bound

For the `(N-1)`-site zero-boundary chain, let

$$
\delta_N(f)=\bar\pi_N(f)-\pi_{N-1}(f).
$$

The accepted zero-frequency identity is

$$
\delta_N(f)
=
\pi_N\left[
\eta_ND\int_0^\infty
P_t^{N-1,0}(f-\pi_{N-1}f)dt
\right].
$$

At the boundary-nearest retained site `i=N-1`, changing the fixed boundary from zero to one changes the flip rate by `-c` when the spin is zero and by `-(b-a)` when it is one. Since `c>b-a`,

$$
|Dh(\xi)|
\le c\,|h(\xi^i)-h(\xi)|.
$$

Couple `\xi` and `\xi^i` by the actual common-uniform zero-boundary random map. If `f` is supported at least `M-1` edges to the left of `i`, then pointwise in Green time,

$$
|P_tf(\xi^i)-P_tf(\xi)|
\le
2\|f\|_\infty
E\sum_{j\le i-(M-1)}D_j(t).
$$

Define

$$
\beta_m(t)
=
\sup_{n,\eta,i}
E\sum_{j\le i-m}D_j(t)
$$

for finite zero-boundary chains. Taking the required suprema gives the new exact sufficient estimate

$$
\boxed{
\Delta_M
\le
2c\int_0^\infty \beta_{M-1}(t)dt.
}
$$

I accept this. Absolute values are taken before the Green-time integral, so it does not use the forbidden duration-averaging cancellation from Meeting 009.

## Finite speed and the zero-boundary Hamming susceptibility

Let

$$
\alpha_0(t)
=
\sup_{n,\eta,i}E\sum_jD_j(t)
$$

for finite zero-boundary chains. One-sided finite propagation gives

$$
\beta_m(t)
\le
E[(\operatorname{Pois}(t)-m+1)_+],
$$

while trivially `beta_m(t)<=alpha_0(t)`. Hence, for every fixed `t`, `beta_m(t)->0`. Therefore

$$
\boxed{
\int_0^\infty\alpha_0(t)dt<\infty
\quad\Longrightarrow\quad
\Delta_M\to0
}
$$

by dominated convergence. Combined with Meeting 014, integrable zero-boundary single-flip susceptibility proves tail-shift agreement of the projective half-line invariant law.

This is a genuine new criterion. It is not merely another restatement of the tail sigma-field question.

## Finite-time contraction is a sufficient common diagnostic

The path-coupling argument used by G on the full line applies to each finite zero-boundary interval, and taking the supremum over interval size gives

$$
\alpha_0(t+s)\le\alpha_0(t)\alpha_0(s).
$$

If for one finite `T`

$$
\alpha_0(T)\le\rho<1,
$$

then for `t=nT+s`, `0<=s<T`,

$$
\alpha_0(t)\le\rho^n(1+s),
$$

so

$$
\int_0^\infty\alpha_0(t)dt
\le
\frac{T+T^2/2}{1-\rho}.
$$

Thus one finite-time Hamming contraction proves F's stationary tail-shift theorem.

F's split at spatial distance `m=M-1`, with early-time finite speed and late-time block contraction, also yields an explicit exponentially decaying upper bound on `Delta_M`. The derivation is valid for fixed `T` and `rho<1`; the original verifier failure was only SymPy's handling of the convergence condition.

## Finite certificate interface

G006 introduced the finite controlled-CTMC value `A_{L,R}(T)` for the full-line coefficient `alpha(T)`. F observes that the zero-boundary coefficient `alpha_0(T)` is covered by the same controlled problem when the fixed zero boundary is farther than `R` sites to the right of the initial flip, plus finitely many additional controlled problems for boundary distances `0,...,R-1`.

Writing the maximum of these finite values as `\widehat A_{L,R}(T)`, the same left-cone estimate gives

$$
\boxed{
\alpha_0(T)
\le
\widehat A_{L,R}(T)
+E[(\operatorname{Pois}(T)-L)_+].
}
$$

Hence one rigorous finite strict inequality on the right proves tail-shift agreement and the first post-insertion common-mass truncation theorem.

No such strict inequality is currently proved.

A distinction remains important: a theorem `alpha_0(T)<1` settles F's stationary zero-boundary problem but does not by itself prove extinction of G's full-line common coupling. Conversely, a proof of full-line `alpha(T)<1` does not automatically discharge the finitely many close-zero-boundary geometries in `alpha_0`; those must be checked or compared separately. The two questions now share the same finite-time mechanism, not literally the same scalar coefficient.

## Route-level expected-value review

The recent history contains many failed local architectures: one-step `L^1`, scalar sup bounds, exposed-only products, the full nearest-neighbour scalar product/coboundary class, and depth-uniform finite common-mass modes. F's last several assignments also ended without the requested all-depth profile theorem.

However, the present convergence is not another renamed blocker. Two independently developed sides have reduced to one concrete nonlocal phenomenon:

> Does the complete common-uniform random map, after allowing its initial near-East damage expansion and later clearing, have a finite time at which single-flip Hamming damage contracts?

A positive answer to the full-line version gives quantitative disagreement extinction. A positive answer to the zero-boundary version gives the tail-shift theorem and explicit common-mass truncation. Both admit finite controlled-CTMC certificates with explicit causal-cone errors.

This makes the already-authorized G007 block worth completing. It does **not** justify starting a matrix-product norm or another family of local credits.

### Direction decision

1. **Continue only through the current finite-time random-map diagnostic.** G007 remains in flight unchanged.
2. **Do not dispatch F to a duplicate HJB search now.** F should finish its current response and then remain idle pending G007. Its alpha-zero reduction is retained as the zero-boundary interface if G produces a useful finite block.
3. **No matrix-product/nonlocal-norm construction is authorized.** The correct next object, if any, is the complete finite-time random map itself.
4. **Hard stop condition for this implementation:** if G007 returns unresolved and the remaining proposal is only larger `L,R,T` computation, a more elaborate controller, or generic matrix-product engineering with no new theorem controlling the finite approximation, do not issue G008/F013 variants of the same search. Reassess the predecessor-trail route and move to a different proof-spine mechanism or a bounded outside consultation.
5. If G007 proves `alpha(T)<1`, first propagate the exact block theorem to the F interface: check the finitely many close-zero-boundary cases needed for `alpha_0`, then formulate one combined block transfer before attempting arbitrary trail iteration.
6. If G007 proves convective survival or otherwise proves `alpha(T)>=1` for all `T`, close every route requiring global coalescence of this synchronous coupling. F's common-mass localization facts remain valid, but the disagreement channel needs a different representation.

## Ruling

- `state_narrowed: yes`.
- F012's bound `Delta_M <= 2c int beta_{M-1}` is accepted.
- Integrable zero-boundary Hamming susceptibility is sufficient for tail-shift agreement.
- A single `alpha_0(T)<1` gives an explicit exponential tail-shift bound.
- The controlled-CTMC hierarchy extends to a finite certificate for `alpha_0(T)` after finitely many close-boundary cases are included.
- Tail-shift agreement, `alpha_0(T)<1`, full-line `alpha(T)<1`, and convective survival all remain unproved.
- The original F012 verifier `3750a53` failed and is not counted as a passing certificate; `5494008` repairs the SymPy convergence-check defect without changing the proof.
- The route continues for the already-authorized G007 finite-time contraction block only. F is idle after finishing its current response. Broader nonlocal/matrix-product engineering is deferred and has an explicit stop condition after G007.
