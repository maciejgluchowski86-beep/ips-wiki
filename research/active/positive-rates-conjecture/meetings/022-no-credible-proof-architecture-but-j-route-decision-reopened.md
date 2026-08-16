# Group meeting 022: no credible proof architecture; principal evidence reopens only the `J` route-decision problem

Date: 2026-08-17

Professor review of:

- Meeting 021 and its route-level stop;
- outside consultation 002, returned to the principal without repository edits, with verdict `RECOMMENDATION: no-credible-route`;
- consultant brief `consultants/assignment-002-post-trail-architecture-review.md`;
- the principal's independently generated target-hierarchy / finite-box study, relayed verbatim to the Professor;
- durable normalization of that study in `notes/principal-target-hierarchy-and-j-norm-evidence.md`;
- `principal-centered-trail-reduction.md` for the canonical `J` normalization;
- current `state.md` and `proof-spine.md`.

`state_narrowed: yes`.

Evidence pointer: the trajectory-kernel theorem from consultation 002, independently checked below, plus the new principal finite-box evidence that the absolute-duration `J` target itself may be supercritical at strict residual points. The numerical part is not treated as proved; it changes the route-decision target, not theorem status.

## Ruling in one sentence

I accept the consultant's conclusion that **no presently identified proof architecture clears the continuation bar**. The principal's parallel calculation does not contradict that conclusion: it supplies no proof architecture. It does, however, expose a logically prior and sharply testable possibility that the current absolute-duration `J` criterion is itself false on part of the residual chamber. I therefore authorize exactly one bounded **route-decision** block on `(J-SPEC)`, not another proof attempt for `J`, tail shift, common coupling, or trajectory-kernel exactness.

Student F remains idle. Student G receives Assignment 009 on `(J-SPEC)`. This numbering does not reopen G's stopped common-coupling route.

## 1. Independent check of the consultant's trajectory transfer

Let

$$
\mathscr X=D(\mathbb R,\{0,1\})
$$

be the two-sided cadlag trajectory space. For a prescribed right-neighbour trajectory `y`, define the trajectory at the site immediately to its left using independent graphical marks:

- rate `1-c`: set the site to `1`;
- rate `a`: set the site to `0`;
- rate `B=b+c-a`: if `y=0`, refresh the site to Bernoulli `c/B`; if `y=1`, do nothing.

The neighbour-independent reset rate is

$$
\omega=a+1-c>0.
$$

At each finite time there is almost surely a last such reset in the past, so the bi-infinite output trajectory is determined from `y` and the site marks without choosing an initial spin at time `-infinity`. Denote the resulting kernel by

$$
Q(y,dx).
$$

Because the dynamics are one-sided, independent site-mark families recursively generate the stationary trajectory field of every finite zero-boundary system from the constant-zero boundary trajectory. Its time-zero projection is the finite invariant law `pi_N`. I accept this as an exact spatial Markov representation on **whole trajectories**.

This representation is genuinely different from the predecessor trail and the common-uniform disagreement process.

## 2. The natural full path-space contraction is exactly false

Let `bold0` and `bold1` be the constant zero and constant one trajectories.

Under `bold0`, the output site is the stationary two-state chain

$$
0\xrightarrow{1}1,
\qquad
1\xrightarrow{b}0.
$$

Its stationary one-density and jump intensity are

$$
r_0=\frac1{1+b},
\qquad
j_0=\frac{2b}{1+b}.
$$

Under `bold1`, the output chain is

$$
0\xrightarrow{1-c}1,
\qquad
1\xrightarrow{a}0,
$$

with

$$
r_1=\frac{1-c}{a+1-c},
\qquad
j_1=\frac{2a(1-c)}{a+1-c}.
$$

If `r_0!=r_1`, the two stationary path laws are mutually singular because their almost-sure occupation fractions differ. Equality `r_0=r_1` is exactly

$$
a=b(1-c).
$$

On that surface,

$$
j_1=\frac{2b(1-c)}{1+b}
\ne
\frac{2b}{1+b}=j_0
$$

because `c>0`, so the almost-sure jump frequencies separate the path laws instead. Hence throughout the residual problem

$$
\boxed{Q(\mathbf 0,\cdot)\perp Q(\mathbf 1,\cdot).}
$$

For

$$
\lambda_p=p\delta_{\mathbf0}+(1-p)\delta_{\mathbf1},
$$

mutual singularity of the two output components gives

$$
\boxed{
\|\lambda_pQ-\lambda_qQ\|_{TV}=|p-q|,
}
$$

and

$$
\boxed{
D(\lambda_pQ\|\lambda_qQ)
=
p\log\frac pq+(1-p)\log\frac{1-p}{1-q}.
}
$$

Thus the Dobrushin coefficient of `Q` is one and relative entropy can be transmitted isometrically on a simple stationary two-point input class. Ordinary Doeblin/Dobrushin/entropy contraction on the full path-law class is not the missing theorem.

I accept this theorem. It does **not** refute weak ergodicity of the particular reachable orbit from the zero boundary. But consultation 002 found no rate-level mechanism for that restricted theorem which does not simply rename the missing spatial-tail problem. I agree with the recommendation not to assign `prove Q is exact`, derive a generic `g`-function, search `bar d`/Hellinger norms, or optimize block maximal couplings.

## 3. Consultation 002 route ruling

The consultant tested the requested architecture classes:

- direct spatial law: exact trajectory kernel exists, but its natural global contraction principles fail exactly;
- alternative coupling: no concrete regenerative quantity was found which avoids endpoint boundary-memory control;
- alternative dual/transform: F013's invariant spectral projection persists under the actual unsplit signed transfer, and no nonlinear cancellation theorem was identified.

The consultation therefore returns `no-credible-route`.

I accept that recommendation **as a proof-architecture judgment**. If the principal's parallel target study had not arrived, the correct action would be to keep both students idle and report that no current architecture justifies another substantial proof block.

## 4. The principal's parallel calculation changes a different question

The principal independently asked what the target statements should be before attempting another proof. The resulting finite-box study is recorded in

`notes/principal-target-hierarchy-and-j-norm-evidence.md`.

The calculation used the canonical singleton predecessor-trail absolute-duration norm, normalized as `N_n` with

$$
J_n=\frac gB N_n.
$$

Define

$$
\rho_J(a,b,c)
:=
\limsup_{n\to\infty}N_n^{1/n}
=
\limsup_{n\to\infty}J_n^{1/n}.
$$

The reported finite-depth estimates through depth ten show decreasing behavior near East but apparent growth at two strict residual points. In particular, for

$$
(a,b,1-c)=\left(\frac1{1000},\frac1{10},\frac1{10000}\right),
$$

so

$$
(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right),
$$

the capture reports

$$
\rho_{7,10}\approx1.153,
\qquad
N_{10}\approx2.3975.
$$

At the nearby rational growth point

$$
(a,b,c)=\left(\frac1{500},\frac1{10},\frac{9999}{10000}\right),
$$

it reports

$$
\rho_{7,10}\approx1.070,
\qquad
N_{10}\approx1.2969.
$$

Both are strict residual points. These computations are **not independently verified asymptotic results**. Finite-depth growth alone cannot prove `rho_J>1`.

The same study reports extremely strong cancellation in signed duration-resolvent pairings at the growing points. At depth ten, the absolute norm and zero-shift signed pairing are reported as

$$
2.3975\quad\text{versus}\quad0.00325
$$

at the strong-growth point. Sampled real and complex Laplace-reweighted signed pairings also decay through depth ten.

This evidence changes the target hierarchy even though it does not provide a proof architecture.

## 5. Immediate route-decision target `(J-SPEC)`

The canonical predecessor-trail reduction uses `J_n->0` only as a **sufficient bound after replacing the exact right-region contribution by an absolute survival bound**. The new evidence makes it unsafe to continue treating this sufficient bound as if it were likely true globally.

The immediate decision problem is therefore

$$
\boxed{
\text{either prove }\rho_J<1\text{ throughout the residual chamber,
 or prove }\rho_J>1\text{ at one strict residual point.}
}
\tag{J-SPEC}
$$

For current expected value, the second alternative is the primary target because the numerical margin is large at the strong-growth point.

A proof

$$
\rho_J>1
$$

there would establish that the current **absolute-duration** `J` strategy is genuinely false at that strict residual parameter. It would not invalidate the exact predecessor-trail identity; rather, it would prove that the proof discarded essential right-region/duration cancellation when it replaced the exact factor by its uniform absolute bound.

This would be a material route-killing theorem and would sharply determine what any future predecessor-trail proof must retain.

## 6. Why this does not contradict Meeting 021

Meeting 021 stopped further attempts to prove `J->0` through the current profile implementation. Assignment 009 does not attempt that.

It asks whether the target `J->0` itself fails. This is logically prior to selecting another architecture and is justified by new evidence which did not exist at Meeting 021.

No third insertion, tail-shift theorem, common-coupling occupation theorem, trajectory-kernel exactness theorem, generic matrix norm, or larger raw random-map window is reopened.

## 7. Later targets are recorded but not yet active

The principal proposes a scalar signed resolvent target `(ML)` and, more importantly, an exact right-region target `(JT)` / possible matrix-resolvent formulation `(MR)` that retains the duration-dependent right contribution inside the signed integral.

I do **not** authorize those as proof tasks now.

Reasons:

1. the scalar `(ML)` evidence is sampled, not certified;
2. `(ML)` is not yet linked to ergodicity without an exact recursion for the right-region class;
3. if `(J-SPEC)` unexpectedly favors `rho_J<1`, the route hierarchy changes again;
4. if `(J-SPEC)` proves `rho_J>1`, the next formal task is first to reconstruct the exact right-region class `R_{n,u}` and determine whether it has a closed signed resolvent recursion before attempting any norm theorem.

## 8. Next task and stopping rule

Student G receives `students/student-g/assignment-009.md`.

The task is to decide `(J-SPEC)` at a strict growth point by an **asymptotic certificate**, not by extending the same finite-depth Monte Carlo table.

A successful route-killing output is a rigorous block/minorization/Perron-Frobenius or other theorem implying

$$
\rho_J>1
$$

at the strong-growth or rational-growth point.

A successful opposite output is a theorem implying `rho_J<1` on a genuine residual region.

If G returns unresolved with only deeper finite-box evidence and no asymptotic mechanism, do not continue by larger `n`. Return to the consultation-002 conclusion: no presently credible proof architecture or route-decision mechanism is available, and keep the students idle until a genuinely new input arrives.

## Ruling

- `state_narrowed: yes`.
- Consultation 002's exact trajectory-kernel representation is accepted.
- `Q(0,.)` and `Q(1,.)` are mutually singular; global path-space TV/KL contraction is not available.
- The consultant's `no-credible-route` recommendation is accepted as the current proof-architecture assessment.
- The principal's new finite-box study is recorded as unverified but target-relevant evidence.
- Do not presume `J_n->0`; decide `(J-SPEC)` first.
- Exactly one bounded route-decision block is authorized: Student G Assignment 009.
- Student F remains idle.
- `(ML)`, `(JT)`, `(MR)`, trajectory exactness, `g`-measure variation, alternative couplings, and further predecessor-trail/profile compositions are not active tasks.
