# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/006-one-step-transfer-refuted-block-stack-target.md`, `state_narrowed: yes`.
- Principal trail notes: `notes/principal-centered-trail-reduction.md` and `notes/principal-centered-trail-update2.md`.
- Student F: `students/student-f/assignment-007.md`. Assignment 006 is superseded immediately.
- Student G: still finishing `students/student-g/assignment-002.md`.

On the normalized face `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the residual chamber remains

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

The frozen-exterior finite-wall route and cellwise nonnegative scaffold-transfer route remain closed.

### Centered predecessor trail survives; Meeting 005 one-step target does not

Use

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The canonical predecessor-trail decomposition remains the active reduction. Selected residual trail interactions are births and the trail contributes the positive factor

$$
e^{-\omega\tau}.
$$

The full Poisson-Mecke factorization and no-exit complement still require independent audit before use in a closing proof.

The right region has a stronger segmentwise survival bound

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_k s_1(u_k).
$$

Set

$$
w(u)=e^{-\omega u}s_1(u),
$$

and

$$
Z=\int_0^\infty w(u)\,du
=\frac{\omega+1+B+a}{(\omega+a)(\omega+1+B)-a}.
$$

This already proves trail-depth decay on the genuine parameter subregion

$$
\max\{c,g\}Z<1.
$$

The difficult near-East regime is not covered.

### Exact depth-two obstruction

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

the exact depth-two invariant scalar changes sign. The Professor independently checked the principal's limits

$$
\frac{g}{|m_\varepsilon|}\int_0^\infty e^{-\omega u}|A_{2,\varepsilon}(u)|\,du\to\frac32,
$$

and

$$
\frac{g}{|m_\varepsilon|}\int_0^\infty w(u)|A_{2,\varepsilon}(u)|\,du\to\frac75.
$$

Therefore the one-generation centered-transfer contraction `(T)` adopted at Meeting 005 is **false** near East, even after the improved right-region killing factor. Pointwise regional positivity and simple one-step absolute-value iteration are likewise closed.

### Correct right-weighted criterion

The sufficient all-depth quantity is now

$$
J_{x,r}
=B g^{n-1}
\int_{(0,\infty)^n}
\left(\prod_k w(u_k)\right)
|\pi^0_{m,r}(F_{x,u})|\,du.
$$

The trail reduction gives

$$
\limsup_{t\to\infty}\sup_\eta |D_R(t,\eta)|
\le C_A\sum_{x\in A}J_{x,r}.
$$

Thus `J_{x,r}->0` with trail depth is sufficient for the nonempty-exit term.

### Mass/disagreement stack mechanism

Each centered insertion splits exactly as

$$
(b-a)\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

The first term is a signed mass channel; the second is a positive conditional-law disagreement channel. Near East the equilibrium mass coefficient is order `epsilon^2`, the disagreement coefficient order `epsilon`, while the right-weighted mass multiplier tends to `2/5`.

The principal's reset coupling gives strict negative drift for the unresolved disagreement-stack height. This connects directly to Student F's independent result that every disagreement under the common-uniform coupling has coalescence intensity at least

$$
q=1-c+a=\omega.
$$

The unresolved point is not stack recurrence by itself but **signed branching** through repeated mass/disagreement decompositions.

### Current proof target

The active theorem is a parameter-dependent **block contraction**, not a one-step norm:

find a norm on trail-generated decompositions into signed mass components and coupled disagreement pairs, weighted by unresolved stack height, and constants

$$
m_0<\infty,\qquad \theta<1
$$

such that

$$
\|T^{m_0}\nu\|_*\le\theta\|\nu\|_*.
$$

A proof must imply `J_{x,r}->0`. Replacing the disagreement channel by unrestricted total variation is not acceptable because it recreates the exact depth-two expansion.

Student F has been urgently redirected to audit this correction and attack the block theorem. Student G continues its current assignment unchanged.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard; the project factor-`2` variance bound and quotient-genealogy proof remain verified technical mathematics.

## Wiki freeze

The live wiki remains frozen during active research.
