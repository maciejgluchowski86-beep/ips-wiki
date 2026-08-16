# Group meeting 013: equilibrium profile truncates; zero-frequency post-insertion response is the next test

Date: 2026-08-16

Professor review of:

- Student F, commit `5979255`, `students/student-f/010-profile-regeneration-truncation.md`;
- Meetings 011--012 and the current proof spine;
- Student G's still-in-flight Assignment 006.

No verifier for Assignment 010 is currently committed. The report mentions `students/student-f/010-profile-regeneration-verifier.py`, but repository search finds no such file. The ruling below is therefore based on direct reconstruction of the hand arguments, not on an auxiliary certificate.

state_narrowed: yes

Evidence pointer: `students/student-f/010-profile-regeneration-truncation.md`, especially Sections 2--8 and 11--12.

## Previous bottleneck

Meeting 011 closed depth-uniform finite linear common-mass mode closure. Assignment 010 asked whether the exact duration-resolved profile could nevertheless be truncated quantitatively in a way compatible with the `J`-norm.

Meeting 012 independently closed the complete nearest-neighbour scalar coupling product/coboundary class. Thus there is no finite scalar coupling cocycle available to repair losses on the common-mass side.

F does not prove the full iterative profile theorem. It does prove that the first invariant insertion is genuinely truncatable and identifies a sharper obstruction after that insertion.

## Professor-accepted exact projective structure

Let `P_u^N` be the zero-boundary semigroup on `Lambda_N={1,...,N}`, `pi_N` its invariant law, `R_{N,M}` the rightmost-`M` suffix marginal, and

$$
(\mathcal J_N\nu)(f)=\nu((B\eta_N-c)f),
\qquad
\mathcal T_N(u)=\mathcal J_N(\cdot\,P_u^N).
$$

Because the dynamics are one-sided and each rate uses only the site and its right neighbour, the rightmost suffix is autonomous. Hence

$$
R_{N,M}(\nu P_u^N)=(R_{N,M}\nu)P_u^M,
$$

and insertion/drop also commutes with suffix marginalization:

$$
R_{N-1,M-1}\mathcal T_N(u)
=\mathcal T_M(u)R_{N,M}.
$$

I accept this exact intertwining. It implies finite transfer delay: data farther than `M` sites from the moving right boundary cannot affect the scalar output during the next `M` reverse transfers.

The same autonomy gives projective consistency of the invariant laws:

$$
R_{N,M}\pi_N=\pi_M.
$$

Strict positive rates make the finite suffix chain irreducible, so the invariant marginal is uniquely `pi_M`.

## Professor-accepted invariant one-insertion truncation

Use the projective half-line law `pi_infty^0`, relabel the rightmost spin as `eta_0`, and put

$$
Y=B\eta_0-c,
\qquad
K_M=E[Y\mid\eta_{-M},\ldots,\eta_{-1}].
$$

The sigma-fields increase with `M`; `Y` is bounded. Levy's upward theorem therefore gives `K_M -> K_infty` in `L^1`. Consequently

$$
\varepsilon_M
:=\sup_{n\ge M}\|K_n-K_M\|_1
\longrightarrow0.
$$

For every finite `N>=M+1`, the exact conditional coefficient given the full left block is the translated `K_{N-1}`. Therefore, for every bounded left function `F`,

$$
\boxed{
\left|
\pi_N((B\eta_N-c)F)-\pi_N(K_M^{(N)}F)
\right|
\le\varepsilon_M\|F\|_\infty,
}
$$

uniformly in the total interval depth. I accept this as a genuine depth-uniform finite-context approximation for the **first invariant centered insertion**. It does not assert a finite Markov order and is compatible with the earlier finite-mode obstruction.

## Professor-accepted separated-gap estimate

F writes `phi_N=eta_N-r_0`, `q_0=b/(1+b)`, decomposes the left generator as

$$
L_Nf=L^0f+\eta_NDf,
$$

and defines

$$
\bar L=L^0+q_0D.
$$

Since `\bar L` is a convex combination of the fixed-zero and fixed-one boundary generators, it is Markov. Stationarity of `phi_N g`, together with

$$
L_N\phi_N=-(1+b)\phi_N,
$$

gives the resolvent identity

$$
\pi_N\left[
\phi_N((1+b)-\bar L)g
\right]
=q_0r_0\pi_N[Dg].
$$

Using

$$
g=\int_0^\infty e^{-(1+b)t}\bar P_tf\,dt
$$

and finite propagation across a gap `M-1`, one obtains

$$
\boxed{
|\pi_N(\phi_N f)|
\le
\frac{2bc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty
}
$$

when `f` is supported at least `M` sites left of the zero boundary. Therefore

$$
\boxed{
\left|
\pi_N((B\eta_N-c)f)-(Br_0-c)\pi_N(f)
\right|
\le
\frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty.
}
$$

The constants check directly: the Laplace-Poisson identity is

$$
\int_0^\infty e^{-\lambda t}P(\operatorname{Pois}(t)\ge m)dt
=\frac1{\lambda(1+\lambda)^m}.
$$

This is a real exponential localization theorem for an equilibrium insertion separated from the test function by a blank spatial gap.

## Professor-accepted one-segment finite-speed tail

Since `s_1(u)<=1`, standard one-sided finite propagation gives

$$
\boxed{
\int_0^\infty
w(u)\|P_uf-P_u^{(M)}f\|_\infty du
\le
\frac{2}{\omega(1+\omega)^M}\|f\|_\infty.
}
$$

This estimate is pointwise before duration integration, so it respects the Meeting 009 norm-order restriction.

It does not iterate through centered insertions in a scalar variation norm: the scalar insertion cost returns the already-refuted multiplier `cZ>1`.

## Exact post-insertion blocker: zero-frequency boundary response

Let `bar pi_N` be the left marginal of `pi_N`. Generically

$$
\bar\pi_N\ne\pi_{N-1}.
$$

Thus after the first centered insertion the mass branch is not reset to the projective invariant family.

For a bounded function `f` on `Lambda_{N-1}`, set

$$
h=f-\pi_{N-1}(f),
\qquad
G=\int_0^\infty P_t^{N-1,0}h\,dt.
$$

Since `-L^0G=h`, stationarity of `pi_N` gives the exact identity

$$
\boxed{
\bar\pi_N(f)-\pi_{N-1}(f)
=
\pi_N\left[
\eta_ND
\int_0^\infty
P_t^{N-1,0}(f-\pi_{N-1}(f))dt
\right].
}
$$

I accept this derivation. Unlike the favorable separated-gap identity, it has no positive Laplace parameter. Finite speed alone therefore gives no integrable long-time bound, because `P(Pois(t)>=M)` tends to one as `t->infinity`.

This is now the precise common-mass question. The full Assignment-010 profile truncation theorem remains open.

## Homeostasis / direction judgment

This is the third consecutive F block whose final theorem remains blocked. I do **not** treat that count alone as a reason to stop: each block removed a materially different false simplification and Assignment 010 also proves new positive localization statements.

However, the evidence has converged. F's common-mass side and G's coupling side now both point to the need for a nonlocal object. Two local scalar Foster architectures and a depth-uniform finite common-mass matrix are already closed. We should not respond by open-ended matrix-product engineering.

The next F block is therefore one surgical viability test: decide whether the zero-frequency boundary response itself is spatially local in a depth-uniform sense. If it fails at a strict residual point, the proposed profile-truncation implementation is closed. If it holds, it supplies the missing first post-insertion tail estimate and gives a concrete basis for testing iteration.

G's Assignment 006 remains in flight and is not amended. After F011 and G006 return, the Professor should hold a route-level review before assigning either student to a general matrix-product/nonlocal norm construction.

## Ruling

The state narrows again.

- Exact suffix intertwining and suffix-projective invariant laws are accepted.
- A single invariant centered insertion is depth-uniformly finite-context approximable in `L^1`.
- The separated equilibrium defect has an explicit exponential gap bound.
- One weighted semigroup segment has an explicit finite-speed truncation tail.
- The mass branch after insertion is nonstationary, and its discrepancy from the next invariant law is exactly a zero-frequency Green-kernel boundary response.
- Finite speed and scalar absolute-value composition do not control that response iteratively.
- F is assigned one decisive zero-frequency boundary-locality test rather than a vague larger nonlocal ansatz.
