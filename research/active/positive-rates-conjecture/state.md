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

Latest meeting: `meetings/012-balanced-circulation-refutes-16-phase-product-class.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-010.md`, profile regeneration/truncation of the growing common-mass hierarchy in the `J`-compatible `L^1(w)` norm;
- Student G: `students/student-g/assignment-006.md`, decide survival/extinction of the common-uniform disagreement process near East.

## Closed mechanisms / corrections

1. Fixed finite agreed-block / frozen-exterior wall crossing.
2. Cellwise last-exit/scaffold insertion positivity.
3. Meeting 005 one-generation centered-transfer contraction `(T)`.
4. The crude condition `max{c,b-a}Z<1` on the residual chamber: throughout `R`, `c>b-a` and `cZ>1`.
5. Student G Assignment 003's exposed-only independent-level product Foster lift.
6. Student G Assignments 004--005's entire **nearest-neighbour scalar edge-product/coboundary Foster class**: an exact balanced-circulation certificate gives unavoidable positive bulk drift at a strict residual point.
7. Student F Assignments 008--009's proposed **depth-uniform finite linear generator/mode closure** for the common-mass signed sector: the cyclic mode dimension is at least the remaining spatial depth even at disagreement height zero.

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
Z=\int_0^\infty w(u)du.
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

Showing `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. The exact Poisson--Mecke trail factorization and complementary no-exit term still require independent audit before a closing proof.

## Exact mass/disagreement decomposition

Each centered insertion splits as

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The first term is signed common mass; the second is a conditional-law disagreement channel.

## Accepted coupling inputs that survive the Foster failures

For one fixed parent disagreement, the number `N` of exposure re-entries before that parent first coalesces satisfies

$$
P(N\ge n\mid\mathcal F)\le h_1^{n-1},
$$

hence has an explicit exponential pgf. The principal stack-clearing minorant separately gives negative height drift and an exponential height factor on an explicit interval.

These scalar facts do **not** compose into a global local-product Foster theorem. The old `16/21` near-East number is only a diagnostic.

### Meeting 012: 16-phase scalar product class refuted

At

$$
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

Student G gives an exact normalized rational circulation `mu` on the 64 triple phases with spatial flow conservation, zero expected exponent change for every scalar edge weight, and positive exposure-entry flux `R_mu`.

For every positive edge matrix `Q` and every `s>1`, weighted AM--GM yields

$$
\boxed{
\sum_e\mu_eG_Q(e)
\ge
C_\mu\left(s^{R_\mu/C_\mu}-1\right)>0.
}
$$

Any coboundary potential would force the same circulation average to be nonpositive, a contradiction. Equivalently at least one directed spatial cycle has positive mean bulk drift for every `Q,s`. Repeating the cycle defeats all finite boundary/height corrections.

Thus the nearest-neighbour scalar product/coboundary Foster class cannot prove the required all-height coupling return throughout the residual chamber.

Student G is no longer enlarging local scalar correctors. Assignment 006 tests the more structural question whether the common-uniform disagreement process itself survives from a finite seed near East. Survival would close any route requiring global coalescence of that synchronous coupling; extinction would require a genuinely nonlocal regeneration theorem.

## Accepted common-mass signed inputs

For

$$
r_0=\frac1{1+b},
$$

Student F proves

$$
\boxed{|Br_0-c|Z<\frac23.}
$$

The first transient mass mode also contracts:

$$
\boxed{
\kappa_T=B Z_{\omega+1+b}<1,
}
$$

with exact gap, writing `k=1-c`,

$$
a^2+5ab+ak+7a+4bk+6k>0.
$$

Near East,

$$
\kappa_T
=1-\frac{13}{3}\varepsilon^2
+\frac{38}{9}\varepsilon^3+O(\varepsilon^4).
$$

The exact one-segment signed transfer is operator-valued and duration-resolved. Duration integration cannot precede the final absolute-value norm: near East the false signed-averaged factor is `3/5`, while the correct `L^1` factor is `7/5`.

### Meeting 011: no depth-uniform finite linear mode closure

On an `N`-site zero-boundary interval,

$$
L_N^j h_{p_*}(\eta_1)
=\frac{B^j}{q_*}\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

for `0<=j<N`. Hence these `N` vectors are linearly independent and any exact semigroup-invariant linear mode space containing the one-site centered insertion has dimension at least `N`.

Therefore bounded disagreement height does not imply bounded common-mass mode dimension. Student F Assignment 010 now seeks a quantitative profile regeneration/truncation theorem rather than another exact finite mode state.

## Current bottleneck

The predecessor-trail route now has two nonlocal interfaces.

1. **Common-mass profile tail (F).** Prove a depth-uniform truncation/ancestry-tail estimate in the exact `J`-compatible profile norm, or exhibit an obstruction.
2. **Common-uniform coupling viability (G).** Decide finite-seed disagreement survival versus extinction near East. If survival holds, abandon global-coalescence/Foster use of this synchronous coupling. If extinction holds, extract a genuinely nonlocal regeneration theorem rather than another local product corrector.

Only after these issues produce a route to `J_{x,r}->0` should the full predecessor-trail factorization and no-exit term be audited for final ergodicity.

## Anti-circularity rule

Do not use `16/21` as a global Foster multiplier, enlarge scalar local coupling products mechanically, integrate duration before the `L^1(w)` absolute value, revive a depth-uniform finite generator-mode state, iterate diagnostic finite matrices as the proof kernel, return to one-step `(T)`, or replace the disagreement/common-mass signed structure by unrestricted total variation.

## Wiki

Keep the live wiki frozen during research.
