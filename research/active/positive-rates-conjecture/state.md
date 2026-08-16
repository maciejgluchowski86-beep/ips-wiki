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

Latest meeting: `meetings/008-restart-tail-and-empty-supnorm-region.md`, `state_narrowed: yes`.

Active work:

- Student F: `students/student-f/assignment-008.md`, bounded-height signed mass/disagreement kernel, conditional on the global Foster lift;
- Student G: `students/student-g/assignment-004.md`, make the global restart-corrector Foster lift rigorous or refute it.

## Closed proof mechanisms

1. Fixed finite agreed-block / frozen-exterior wall crossing.
2. Cellwise last-exit/scaffold insertion positivity.
3. Meeting 005 one-generation centered-transfer contraction `(T)`: exact near-East depth-two ratios tend to `3/2` without right killing and `7/5` with it.
4. The claim that the crude right-weighted criterion `max{c,b-a}Z<1` already proves a nonempty part of the residual chamber. Student F proves `cZ>1` throughout `R`, so this condition has no residual solutions.

The canonical predecessor-trail decomposition remains active.

## Canonical trail and global sufficient quantity

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The principal's centered-dual working reduction gives a canonical predecessor trail with positive factor

$$
e^{-\omega\tau}.
$$

The right region has segmentwise survival

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_k s_1(u_k).
$$

With

$$
w(u)=e^{-\omega u}s_1(u),
$$

and

$$
Z=\int_0^\infty w(u)du
=\frac{a+b+2}{2ab+3a-bc+b-2c+2},
$$

the crude sup-norm sufficient condition would be `max{c,g}Z<1`. However throughout the residual chamber

$$
c>g
\qquad\text{and}\qquad
\boxed{cZ>1},
$$

so this criterion contributes no residual subregion.

The correct global right-weighted invariant quantity is

$$
\boxed{
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|du.
}
$$

Showing `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term. The full Poisson-Mecke trail factorization and the complementary no-exit term still require independent audit before a closing proof.

## Mass/disagreement decomposition

Each centered insertion splits exactly as

$$
\boxed{
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).}
$$

The first term is a signed mass channel; the second is a positive conditional-law disagreement channel. Near East the equilibrium mass coefficient is order `epsilon^2`, the disagreement coefficient order `epsilon`, and the right-weighted equilibrium mass multiplier tends to `2/5`.

The unresolved disagreement-stack height has negative drift under the reset coupling, and Student F proved that every disagreement under the common-uniform coupling has coalescence intensity at least

$$
q=1-c+a=\omega.
$$

## Student G Assignment 003: same-parent restart count

Meeting 007 gave a single-exposure child probability bounded by `h_1<1`, uniformly even for non-rightmost disagreements.

G now proves that if `N` is the number of exposure entries of the **same parent disagreement** before that parent first coalesces, then

$$
\boxed{
P(N\ge n\mid\mathcal F)\le h_1^{n-1},\qquad n\ge1.
}
$$

Hence for `1<=s<h_1^{-1}`,

$$
\boxed{
E[s^N\mid\mathcal F]
\le M(s):=\frac{(1-h_1)s}{1-h_1s}.}
$$

This is Professor-checked and removes arbitrary same-parent re-entry as an uncontrolled variable.

The accepted stack-clearing minorant gives

$$
\phi(\lambda)
=\lambda\left(1-\alpha+\frac{\alpha}{2\lambda-1}\right)<1
$$

for an explicit interval of `lambda>1`. Along the near-East path, the algebraic choice `lambda=2`, `s=1+epsilon^2/4` gives

$$
M(s)\phi(2)\to\frac{16}{21}<1.
$$

This is a **coupling-side restart/height stress factor**, not a multiplier for `J_{x,r}` and not a signed block theorem.

## What remains unverified in G's Foster lift

G proposes a product corrector over all unresolved parent levels and a global Foster inequality. The scalar pgf, height minorant, finite-height algebra, and `16/21` limit check. The missing rigorous step is the global phase bookkeeping: inactive/exposed/child-alive phases and later new-parent reinfections must be represented by an explicit Markov state and shown transition by transition to be superharmonic under the proposed corrector.

Thus the **same-parent restart bundle is solved**; the global product/phase lift is still an open technical lemma.

## Current bottleneck split

The block theorem has separated into two complementary tasks.

1. **Global restart-corrector lemma (Student G).** Prove a rigorous all-level Foster inequality reducing arbitrary restart/height excursions to a finite bounded-height/phase set, or give an exact obstruction.
2. **Bounded-height signed kernel (Student F).** Conditional on that reduction, compute or dominate the finite right-weighted mass/disagreement kernel and prove block spectral radius `<1`, or exhibit an exact residual obstruction.

If both succeed, they must be combined to prove `J_{x,r}->0`. Only then should the full trail/no-exit convergence implication be reconstructed.

## Anti-circularity rule

Do not return to the empty crude criterion, rescue one-step `(T)`, replace disagreement by unrestricted total variation, or enumerate fixed scalar depths. The next accepted progress must settle one of the two precise block lemmas above.

## Wiki

Keep the live wiki frozen during research.
