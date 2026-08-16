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
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/013-equilibrium-profile-truncates-zero-frequency-response-remains.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-011.md`, zero-frequency boundary-response locality;
- Student G: `students/student-g/assignment-006.md`, survival/extinction viability test for the common-uniform disagreement process near East.

## Closed mechanisms

Closed: fixed finite walls; cellwise nonnegative scaffold insertion; one-step centered `L^1` contraction; crude scalar `max{c,b-a}Z<1`; G's exposed-only global Foster product; G's full nearest-neighbour scalar edge-product/coboundary Foster class; F's depth-uniform finite linear common-mass mode closure.

Do not reopen these by enlarging finite scalar contexts or finite common-mass alphabets.

## Global predecessor-trail target

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a,
$$

and `w(u)=e^{-omega u}s_1(u)`. The working reduction leaves

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du.
$$

Showing `J_{x,r}->0` with depth is sufficient for the nonempty-exit term. Exact Poisson--Mecke factorization and the no-exit complement remain downstream audits after `J` decay is actually proved.

## Common-mass side

The exact insertion decomposition is

$$
g\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

Professor-checked strict right-weighted losses remain

$$
|Br_0-c|Z<\frac23,
\qquad
\kappa_T=BZ_{\omega+1+b}<1,
\qquad r_0=\frac1{1+b}.
$$

The exact common-mass semigroup has no depth-uniform finite linear mode closure: on an `N`-site interval,

$$
L_N^j h_{p_*}(\eta_1)=q_*^{-1}B^j\eta_1\cdots\eta_{j+1}+R_j,
\qquad \deg R_j\le j,
$$

so the cyclic mode dimension is at least `N`.

Meeting 013 accepts new positive profile structure from F Assignment 010:

1. exact suffix intertwining of the zero-boundary semigroup and reverse insertion/drop transfer;
2. suffix projectivity `R_{N,M}\pi_N=\pi_M` of the finite invariant laws;
3. depth-uniform finite-context `L^1` truncation of the **first invariant insertion** via
   $$
   K_M=E[B\eta_0-c\mid\eta_{-M},\ldots,\eta_{-1}],
   \qquad
   \sup_{n\ge M}\|K_n-K_M\|_1\to0;
   $$
4. separated-gap localization
   $$
   \left|\pi_N((B\eta_N-c)f)-(Br_0-c)\pi_N(f)\right|
   \le
   \frac{2Bbc}{(1+b)^3(2+b)^{M-1}}\|f\|_\infty;
   $$
5. one-segment weighted finite-speed tail
   $$
   \int_0^\infty w(u)\|P_uf-P_u^{(M)}f\|_\infty du
   \le\frac{2}{\omega(1+\omega)^M}\|f\|_\infty.
   $$

The iterative profile theorem is still open. The mass branch after insertion carries `bar pi_N`, not `pi_{N-1}`. Its exact discrepancy is the zero-frequency boundary response

$$
\boxed{
\bar\pi_N(f)-\pi_{N-1}(f)
=
\pi_N\left[
\eta_ND\int_0^\infty
P_t^{N-1,0}(f-\pi_{N-1}(f))dt
\right].
}
$$

Finite speed alone is nonintegrable at zero frequency. F Assignment 011 asks whether the far-left operator norm of this response tends to zero uniformly in volume.

No Assignment-010 verifier is currently committed despite the report mentioning one; Meeting 013's ruling is from direct proof reconstruction.

## Coupling side

G's same-parent geometric restart theorem and separate stack-clearing minorant survive. Two scalar local global-corrector classes are refuted. Meeting 012 accepts the exact balanced-circulation obstruction to every nearest-neighbour scalar edge-product/coboundary corrector at a strict near-East point.

G Assignment 006 now tests whether the common-uniform disagreement process itself survives from a finite seed near East. Survival would close every proof mechanism requiring global coalescence of this synchronous coupling; extinction would require a genuinely nonlocal regeneration theorem.

## Current route-level checkpoint

Both active lines now point to nonlocal structure. Do not launch open-ended matrix-product engineering yet.

- F011 is a surgical test of zero-frequency common-mass boundary locality.
- G006 is a surgical test of common-uniform coupling viability.

After both return, hold a route-level review before authorizing any general nonlocal/matrix-product construction.

## Anti-circularity

Do not integrate duration before the actual absolute-value norm; use `16/21` as a global Foster multiplier; enlarge scalar local corrector context mechanically; revive finite common-mass mode closure; replace the signed disagreement channel by unrestricted total variation; or assume a uniform spectral gap / the positive rates conjecture inside the zero-frequency response problem.

## Wiki

Keep the live wiki frozen during research.
