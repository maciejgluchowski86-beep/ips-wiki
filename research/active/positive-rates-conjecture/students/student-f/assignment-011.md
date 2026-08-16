# Student F assignment 011: zero-frequency boundary-response locality

Work on branch `research/positive-rates-conjecture`.

Read first:

- `meetings/013-equilibrium-profile-truncates-zero-frequency-response-remains.md`;
- your `010-profile-regeneration-truncation.md`;
- Meetings 011--012;
- current `proof-spine.md`;
- Student G `assignment-006.md` only for interface awareness.

The scientific target remains the positive rates conjecture for simple IPS.

## What is accepted from Assignment 010

The Professor accepts:

1. exact suffix intertwining of the zero-boundary semigroup and reverse insertion/drop transfer;
2. suffix-projectivity `R_{N,M} pi_N = pi_M` of the finite zero-boundary invariant laws;
3. depth-uniform `L^1` finite-context truncation of the first invariant insertion through
   $$
   K_M=E[B\eta_0-c\mid\eta_{-M},\ldots,\eta_{-1}],
   \qquad
   \sup_{n\ge M}\|K_n-K_M\|_1\to0;
   $$
4. the separated-gap estimate
   $$
   \left|
   \pi_N((B\eta_N-c)f)-(Br_0-c)\pi_N(f)
   \right|
   \le
   \frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty;
   $$
5. the one-segment weighted finite-speed bound
   $$
   \int_0^\infty w(u)\|P_uf-P_u^{(M)}f\|_\infty du
   \le
   \frac{2}{\omega(1+\omega)^M}\|f\|_\infty;
   $$
6. the exact zero-frequency boundary-response identity
   $$
   \bar\pi_N(f)-\pi_{N-1}(f)
   =
   \pi_N\left[
   \eta_ND
   \int_0^\infty
   P_t^{N-1,0}(f-\pi_{N-1}(f))dt
   \right].
   \tag{BR}
   $$

The full iterative profile-truncation theorem is **not** proved.

No Assignment-010 verifier is currently committed despite the report mentioning one. Do not rely on an absent certificate; if you intended to commit it, either commit it separately or remove the stale pointer in your next write-up.

## Objective

Decide whether the zero-frequency boundary response `(BR)` is itself spatially local, uniformly in volume.

For `M>=2`, define

$$
\Delta_M
:=
\sup_{N\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}(f)\subseteq\{1,\ldots,N-M\}}}
\left|
\bar\pi_N(f)-\pi_{N-1}(f)
\right|.
\tag{1}
$$

Equivalently, by `(BR)`, `Delta_M` is the far-left operator norm of the zero-frequency boundary Green response.

The primary question is

$$
\boxed{\Delta_M\longrightarrow0?}
\qquad(M\to\infty).
\tag{2}
$$

This is the next load-bearing statement. It is weaker and more concrete than constructing a general matrix-product/profile norm, and it directly tests whether the post-insertion mass profile admits spatial truncation at all.

## Successful outcomes

### A. Uniform boundary-response locality

Prove `(2)` at every strict residual parameter point. A parameter-dependent rate is sufficient; it may deteriorate arbitrarily near East.

Prefer an explicit estimate

$$
\Delta_M\le\delta_M,
\qquad
\delta_M\to0.
$$

Possible mechanisms include:

- a signed Green-kernel cancellation in `(BR)`;
- a regeneration decomposition for the zero-boundary Poisson equation;
- spatial mixing of the projective half-line invariant law proved directly from the graphical construction;
- a resolvent/coupling argument which does not assume the positive rates conjecture or an unproved uniform spectral gap.

If `(2)` is proved, go one step further: use it to derive a rigorous truncation estimate for the **mass branch after one centered insertion**, and state exactly what remains before arbitrary iteration.

### B. Exact obstruction

Refute `(2)` at one strict residual point by proving

$$
\limsup_{M\to\infty}\Delta_M>0
$$

or another mathematically equivalent nonlocal boundary-memory statement.

A single strict residual counterexample closes this proposed stationary Green-kernel truncation mechanism as a proof throughout the chamber.

Do not infer nonergodicity from such a failure.

### C. Sharp reduction

If neither direction closes, reduce `(2)` to one explicit theorem whose truth would decide it. Examples: a precise half-line spatial-mixing coefficient, a specific killed disagreement process, or a uniform Poisson-equation estimate. Avoid another generic appeal to “some nonlocal norm”.

## Anti-circularity

Do not assume:

- the positive rates conjecture;
- a depth-uniform spectral gap unless independently proved here;
- global extinction of the common-uniform coupling;
- G Assignment 006 succeeds in either direction;
- a scalar total-variation composition bound through centered insertions.

In particular, finite speed by itself is insufficient at zero frequency:

$$
\int_0^\infty P(\operatorname{Pois}(t)\ge M)dt=\infty.
$$

So a proof must supply genuine long-time decay or cancellation, not repeat the bounded-time propagation estimate.

## Norm discipline

The Meeting 009 `3/5` versus `7/5` obstruction remains binding. If you pass from `(BR)` to a duration-resolved post-insertion estimate, keep every duration variable visible until the actual `L^1(w)` absolute value is taken. Do not manufacture cancellation by integrating duration first.

Likewise, do not use `cZ>1` as evidence against `(2)`: that multiplier concerns scalar absolute-value composition, while `(2)` is a stationary signed boundary-response question.

## Homeostasis / stop condition

This is intentionally a narrow viability test, not an invitation to engineer an unrestricted matrix-product norm.

If `(2)` fails, report that cleanly. If `(2)` holds but cannot be lifted even to one post-insertion mass branch without reintroducing an expansive scalar norm, identify the exact obstruction.

After this assignment and G Assignment 006 return, the Professor will reassess the predecessor-trail route before authorizing any general nonlocal/matrix-product construction.

## Durable output

Commit to

`research/active/positive-rates-conjecture/students/student-f/011-zero-frequency-boundary-response.md`

with exact verifier/certificate code if computation is used.

End with one of:

- `zero-frequency boundary response localizes uniformly: ...`;
- `post-insertion mass branch truncation proved: ...`;
- `zero-frequency boundary locality refuted at: ...`;
- `unresolved after substantive work; exact Green-kernel blocker: ...`.
