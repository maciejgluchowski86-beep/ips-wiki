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

Latest meeting: `meetings/014-zero-frequency-response-equals-tail-shift-defect.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-012.md`, decide tail-shift agreement of the projective half-line invariant law;
- Student G successor session: `students/student-g/assignment-006.md`, survival/extinction viability test for the common-uniform disagreement process near East. The predecessor G session failed before committing its Assignment-006 work; no lost mathematics is used.

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

Assignments 010--011 establish positive projective structure: exact suffix intertwining, suffix-projectivity of the finite invariant laws, finite-context truncation of the first invariant insertion, separated-gap localization, and one-segment finite-speed tails.

### Meeting 014: zero-frequency response is exactly a tail-shift defect

Let `mu=pi_infty^0` be the projective half-line invariant law in coordinates `X_0,X_1,...` from the fixed zero boundary into the left half-line, let

$$
\theta(x_0,x_1,\ldots)=(x_1,x_2,\ldots),
$$

and

$$
\mathcal F_m=\sigma(X_j:j\ge m),
\qquad
\mathcal T=\bigcap_m\mathcal F_m.
$$

For the zero-frequency boundary response

$$
\Delta_M
=
\sup_{N\ge M+1}
\sup_{\substack{\|f\|_\infty\le1\\
\operatorname{supp}(f)\subseteq\{1,\ldots,N-M\}}}
|\bar\pi_N(f)-\pi_{N-1}(f)|,
$$

F proves and the Professor checks

$$
\boxed{
\Delta_M=\|\theta\mu-\mu\|_{\mathcal F_{M-1}}.
}
$$

Hence `Delta_M` is nonincreasing. Writing the signed density of `theta mu-mu` relative to `(mu+theta mu)/2` and applying the reverse martingale theorem gives

$$
\boxed{
\lim_{M\to\infty}\Delta_M
=\|\theta\mu-\mu\|_{\mathcal T}.
}
$$

Therefore

$$
\boxed{
\Delta_M\to0
\iff
\mu|_{\mathcal T}=(\theta\mu)|_{\mathcal T}.
}
$$

The needed theorem is tail-shift agreement, not merely separate tail triviality.

Conditional on `Delta_M->0`, the common-mass branch after one centered insertion already has the `J`-compatible one-next-segment truncation estimate

$$
\int_0^\infty w(u)
|m_0(\bar\pi_N-\pi_{N-1})(P_u f)|du
\le
\left[
\kappa_E\Delta_{M-d}
+
\frac{4|m_0|}{\omega(1+\omega)^d}
\right]\|f\|_\infty.
$$

Choosing `d~M/2` makes the error vanish if tail-shift agreement holds.

F Assignment 012 is one bounded decision block on this tail-shift theorem, preferably through finite-window likelihood ratios, relative entropy, or another explicit boundary-influence identity. Do not launch a general nonlocal/matrix-product norm construction yet.

## Coupling side

G's same-parent geometric restart theorem and separate stack-clearing minorant survive. Two scalar local global-corrector classes are refuted. Meeting 012 accepts the exact balanced-circulation obstruction to every nearest-neighbour scalar edge-product/coboundary corrector at a strict near-East point.

The original G session failed before Assignment 006 reached the repository. A successor session in the same lineage is redoing Assignment 006 unchanged. Survival of a finite disagreement seed would close every proof mechanism requiring global coalescence of this synchronous coupling; extinction would require a genuinely nonlocal quantitative regeneration theorem.

## Current route-level checkpoint

Both active lines now point to nonlocal structure, but each has one concrete decision theorem in flight.

- F012: prove or refute tail-shift agreement of the projective half-line invariant law.
- G006: decide common-uniform finite-seed disagreement survival versus extinction near East.

After both return, hold a route-level expected-value review before any broader nonlocal/matrix-product construction.

## Anti-circularity

Do not integrate duration before the actual absolute-value norm; use `16/21` as a global Foster multiplier; enlarge scalar local corrector context mechanically; revive finite common-mass mode closure; replace the signed disagreement channel by unrestricted total variation; assume a uniform spectral gap / the positive rates conjecture; or infer tail-shift agreement from separate tail 0--1 laws or from fixed finite-window convergence without uniform-in-window control.

## Wiki

Keep the live wiki frozen during research.
