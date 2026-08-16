# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

Latest meeting: `meetings/010-exposed-product-refuted-and-16-phase-foster-reduction.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-009.md`, mode-resolved `L^1(w)` block operator retaining mass relaxation/reset-history modes;
- Student G: `students/student-g/assignment-005.md`, solve or refute the 16-phase all-height coupling Foster feasibility problem.

## Closed mechanisms / corrections

1. Fixed finite agreed-block / frozen-exterior wall crossing.
2. Cellwise last-exit/scaffold insertion positivity.
3. Meeting 005 one-generation centered-transfer contraction `(T)`.
4. The crude condition `max{c,b-a}Z<1` on the residual chamber: throughout `R`, `c>b-a` and `cZ>1`.
5. Student G Assignment 003's **exposed-only independent-level product Foster lift**. Same-parent restart tails remain valid, but multiplying them by the scalar height factor does not give a global corrector.

The canonical predecessor-trail decomposition remains active.

## Global trail target

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
$$

and

$$
w(u)=e^{-\omega u}s_1(u),
\qquad
Z=\int_0^\infty w(u)du
=\frac{a+b+2}{a(2b+3)+(1-c)(b+2)}.
$$

The nonempty-exit term is controlled by

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Showing `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. The exact Poisson--Mecke trail factorization and the complementary no-exit term still require independent audit before a closing proof.

## Exact mass/disagreement decomposition

Each centered insertion splits as

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The first term is signed mass; the second is a positive conditional-law disagreement channel.

## Student G: accepted local restart inputs

For one fixed parent disagreement, the number `N` of exposure re-entries before that parent first coalesces satisfies

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1},
$$

hence

$$
E[s^N\mid\mathcal F]\le\frac{(1-h_1)s}{1-h_1s}.
$$

The stack-height minorant also gives an exponential height factor `phi(lambda)<1`. Near East the scalar product of these two separately derived factors can tend to `16/21<1`, but Meeting 010 establishes that this is **not** a valid global Foster multiplier.

## Meeting 010: exposed-only product Foster lift is false

Student G Assignment 004, commit `4128cee` with verifier commits `bec4dda` and `4586833`, gives a reachable all-`01` disagreement stack

$$
\sigma_i=(X_i,Y_i)=01,
\qquad 0\le i\le H-1,
$$

for which the Assignment-003 exposed-only product corrector has exact tilted drift

$$
\boxed{
\frac{\mathscr L_sV}{V}
=(1-a)(s-1)
+(H-2)(1-a)(s e_0-1)
+\omega(\lambda^{-1}-1).
}
$$

Here `s>1`, `lambda>1`, and the exposed factor `e_0>=1`. Therefore the middle term is positive and grows linearly with `H`, while the right-boundary height gain is `O(1)`. The old global product is positive-drift for sufficiently large height.

With the old near-East choices,

$$
\frac{\mathscr L_sV}{V}\to\frac{H-2}{7}.
$$

Thus Assignment 003's product rule is refuted. The same-parent tail itself is unaffected.

## Exact 16-phase coupling reduction

Let

$$
\mathcal A=\{00,11,01,10\}
$$

be the coupled pair states and choose positive nearest-neighbour edge weights

$$
q_{\alpha\beta}>0,
\qquad (\alpha,\beta)\in\mathcal A^2.
$$

For

$$
C_Q(\sigma)=\prod_i q_{\sigma_{i-1},\sigma_i},
$$

the common-uniform coupling and exposure-entry tilt give an exact local bulk drift `G_Q(alpha,beta,gamma)` for each of the 64 triples.

For this nearest-neighbour product/coboundary class, all-height interior control is equivalent to a finite no-positive-cycle condition on the 16-vertex de Bruijn graph. Equivalently, find a phase potential `psi` satisfying

$$
G_Q(\alpha,\beta,\gamma)
\le
\psi(\alpha,\beta)-\psi(\beta,\gamma)
$$

for all triples. Full Foster contraction additionally requires finitely many right-boundary height, insertion, left-boundary, and suffix-trimming inequalities.

Existence of such weights throughout the residual chamber is open. Student G Assignment 005 attacks exactly this finite feasibility problem.

## Student F: uniform regenerated-mass loss and mode obstruction

For the one-site zero-boundary equilibrium density

$$
r_0=\frac1{1+b},
$$

Student F proves, and the Professor checks,

$$
\boxed{|Br_0-c|Z<\frac23}
$$

at every strict residual point.

A mass branch nevertheless carries a transient relaxation mode

$$
r(u)=r_0+(r-r_0)e^{-(1+b)u}.
$$

Near East,

$$
\frac g{|m_\varepsilon|}\left|\int w(u)A_{2,\varepsilon}(u)du\right|\to\frac35,
$$

but the `J`-compatible norm has

$$
\boxed{
\frac g{|m_\varepsilon|}\int w(u)|A_{2,\varepsilon}(u)|du\to\frac75.
}
$$

Therefore duration/reset modes must remain visible until the `L^1(w)` block norm is taken. Short static spin words do not close the invariant law either.

## Current bottleneck

The block route now has two explicit interfaces.

1. **G:** solve or refute the 16-phase nearest-neighbour product/coboundary Foster feasibility problem, including boundary/height transitions. A success gives a valid all-height coupling return mechanism; a failure closes this corrector class.
2. **F:** build a mode-resolved `L^1(w)` signed block operator retaining equilibrium mass, transient mass/reset modes, disagreement phases, and duration information until the norm. The uniform equilibrium loss `<2/3` is the regenerative anchor.

G's 16 coupling phases and F's mass-relaxation modes address different state-closure problems. Both are required before one can infer `J_{x,r}->0` by this route.

## Anti-circularity rule

Do not use `16/21` as a global Foster multiplier, repair only the all-`01` stack without checking all phase cycles, integrate duration before the absolute-value norm, iterate the diagnostic `K^(1)` matrix as the true signed kernel, return to one-step `(T)`, or replace the disagreement channel by unrestricted total variation.

## Wiki

Keep the live wiki frozen during research.
