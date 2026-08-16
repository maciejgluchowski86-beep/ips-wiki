# Project state

This file is the compact current-state index for the autonomous research programme. Detailed mathematics lives under `research/` and in Git history. `CHATGPT.md` governs the workflow except where the principal has explicitly fixed the present target below.

## Standing novelty standard

A quantitatively improved instance of an existing arbitrary-size/window/order method does not count as a new project result merely because it improves a numerical constant or range. Qualifying work must add structural mathematics or resolve/correct the target problem.

## Principal-fixed active scientific direction

**Positive rates conjecture for simple IPS.**

- Branch: `research/positive-rates-conjecture`.
- Workspace: `research/active/positive-rates-conjecture/`.
- Target fixed by the principal until the principal changes or stops it: prove that every simple IPS with positive rates is ergodic.
- Latest meeting: `research/active/positive-rates-conjecture/meetings/005-principal-trail-reduction-and-all-depth-transfer.md`, `state_narrowed: yes`.
- Principal trail note: `research/active/positive-rates-conjecture/notes/principal-centered-trail-reduction.md`.
- Student F: `students/student-f/assignment-006.md`, independent audit and all-depth centered predecessor-trail transfer.
- Student G: still finishing `students/student-g/assignment-002.md`.

On the normalized face `r11=0`, with

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

the source-corrected unresolved chamber remains

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

### Live-coupling mathematics retained but paused

Student F proved that every disagreement site under the common-uniform coupling has predictable coalescence intensity at least

$$
q=1-c+a>0,
$$

and obtained genuine one- and two-generation regeneration events plus finite-depth ordered clearing. The certified depth-dependent clearing gaps are summable, so these facts do not by themselves give arbitrary-depth extinction. The live-disagreement all-depth search is paused, not closed.

Student G's transient density, finite-box, and adjacent-`11` estimates remain reusable, as does F's coupling drift with the weighted high-risk state `J_i`.

### Meeting 005: centered predecessor-trail reduction

A separate principal exploration supplied an exact centered predecessor-trail decomposition. In the residual centered dual put

$$
B=b+c-a,
\qquad
p_*=\frac cB,
\qquad
q_* = \frac{b-a}{B},
\qquad
\omega=1-c+a.
$$

The canonical trail from root `x` to exit through the right boundary has depth `n=r-x+1`; selected residual trail interactions are births and the vertical trail contributes

$$
\boxed{e^{-\omega\tau}}.
$$

After averaging the final refresh coin before absolute values, the right-region contribution is uniformly bounded independently of interval length and trail depth. For fixed interval, the left region relaxes to the zero-boundary invariant law. The positive-rate factor `omega>0` makes recent exits exponentially negligible.

Consequently the nonempty-trail term is reduced to the all-depth invariant criterion

$$
\boxed{
B(b-a)^{n-1}
\int_{(0,\infty)^n}
 e^{-\omega|u|}
 |\pi^0_{m,r}(F_{x,u})|\,du
\longrightarrow0.
}
\tag{L}
$$

The complementary no-exit term must still be checked explicitly when the exact proof is reconstructed.

A sufficient theorem is an all-depth centered signed-measure contraction: for the trail transfer

$$
(\mathcal C_{y,u}\nu)(f)
=\nu(h_{p_*}(\eta_y)P_u^{<y,0}f),
$$

find a norm on the generated class and `theta<1` such that

$$
\boxed{
(b-a)\int_0^\infty e^{-\omega u}
\|\mathcal C_{y,u}\nu\|_*\,du
\le\theta\|\nu\|_*.
}
\tag{T}
$$

At exact East, the zero-boundary invariant trail expectation is exactly zero because the final trail birth inserts a centered character independent of the preceding factor under product Bernoulli equilibrium. Along `a=eps^2,b=eps,c=1-eps^2`, the one-site constant-mode factor equals

$$
\frac{1-eps}{2(1+eps)}<\frac12.
$$

The principal exploration reports a two-level scalar sign change, so pointwise positivity is not expected; that latest sign-change claim still needs independent reproduction. Signed-measure contraction remains open.

The same scale appears in both current mechanisms:

$$
q=\omega=1-c+a.
$$

No automatic bridge is claimed.

### Current proof direction

Prefer the centered predecessor-trail route because it already resolves the right region and post-exit relaxation and leaves the narrower all-depth target (L)/(T). Student F Assignment 005 is superseded by Assignment 006. Student F must independently audit the exact factorization, including the no-exit complement and the reported two-level sign change, and then prove or obstruct the all-depth transfer mechanism.

Do not revive cellwise positivity, finite-generation escalation, or generic mixing as substitutes for the actual all-depth estimate.

## Most recently completed programme: random-regular voter discordance concentration

`VOTER-CONC-001` is mathematically verified but not a new project result under the standing novelty standard; the project factor-`2` variance bound and quotient-genealogy proof remain verified technical mathematics.

## Wiki freeze

The live wiki remains frozen during active research.
