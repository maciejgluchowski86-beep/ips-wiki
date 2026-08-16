# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/007-student-g-exposure-resolvent-and-restart-bottleneck.md`, `state_narrowed: yes`.
- Principal trail notes: `notes/principal-centered-trail-reduction.md` and `notes/principal-centered-trail-update2.md`.
- Student F: `students/student-f/assignment-007.md`, complete block mass/disagreement contraction.
- Student G: `students/student-g/assignment-003.md`, coupling-side restart-count/renewal bridge.

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

The frozen-exterior finite-wall route, cellwise nonnegative scaffold-transfer route, and Meeting 005 one-step centered-transfer norm `(T)` are closed.

### Active predecessor-trail reduction

Put

$$
B=b+c-a,\qquad g=b-a,\qquad \omega=1-c+a.
$$

The canonical centered predecessor trail remains the active reduction. Selected residual trail interactions are births and the trail contributes `e^{-omega tau}`. The right region has segmentwise survival

$$
|R_{\gamma,t}(\eta)|\le C_A\prod_k s_1(u_k).
$$

With `w(u)=e^{-omega u}s_1(u)` and `Z=int_0^infty w(u)du`, direct decay is proved on

$$
\max\{c,g\}Z<1.
$$

Near East, exact depth-two ratios `3/2` and `7/5` refute one-step absolute-value contraction even with right killing.

The correct global sufficient quantity is

$$
J_{x,r}
=B g^{n-1}\int\left(\prod_k w(u_k)\right)|\pi^0_{m,r}(F_{x,u})|du,
$$

and `J_{x,r}->0` with trail depth would control the nonempty-exit term. The full trail factorization and no-exit complement still require independent audit before a closing proof.

### Mass/disagreement block mechanism

Each centered insertion splits exactly as

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)+Br(1-r)(\mu^1-\mu^0)(f).
$$

The unresolved stack of conditional-law disagreements has negative drift under the reset coupling, and every disagreement under Student F's common-uniform coupling has coalescence intensity at least

$$
q=1-c+a=\omega.
$$

The remaining theorem is a parameter-dependent block contraction on signed mass components and coupled disagreement components, not a one-step norm.

### Student G's new exposure-edge theorem

Student G Assignment 002, commit `c7a33b5` with verifier `e20847a`, adds exact weighted control inside arbitrary-depth disagreement stacks.

At a stopping time with `D_i=0,D_{i+1}=1`, stop when either a left child is created or the right disagreement coalesces. The high-risk local state

$$
J_i=1_{\{D_i=0,D_{i+1}=1,X_i=Y_i=1\}}
$$

has an explicit killed-chain resolvent and the exact child compensator

$$
P(\text{child before right coalescence})
=E\int[(b-a)+(c-b+a)J_i(t)]dt.
$$

The corresponding child probability is uniformly `<1` even for non-rightmost disagreements.

A crude global summation over repeated exposure entries is nevertheless noncontractive near East. Thus the missing coupling quantity is the **exposure-entry/restart count**, not the one-exposure occupation.

This local `J_i` is not the global trail quantity `J_{x,r}`. G's near-East obstruction therefore does not refute `J_{x,r}->0`; it says that crude global `J_i` summation cannot prove the block theorem.

### Current proof target

Find a norm/Lyapunov/renewal scheme on trail-generated signed mass and coupled disagreement components, weighted by unresolved stack/restart state, and finite constants

$$
m_0<\infty,\qquad \theta<1
$$

such that

$$
\|T^{m_0}\nu\|_*\le\theta\|\nu\|_*.
$$

Student F attacks the complete block theorem. Student G attacks the complementary restart-count bridge from `mu^1-mu^0` to such a block contraction. Replacing the disagreement channel by unrestricted total variation or the restart count by crude disagreement occupation is not acceptable.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard.

## Wiki freeze

The live wiki remains frozen during active research.
