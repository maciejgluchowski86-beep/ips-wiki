# Proof spine

## Main target

Prove the positive rates conjecture for simple IPS:

> Every one-dimensional homogeneous binary one-sided nearest-neighbour IPS with positive rates is ergodic.

The scientific target is fixed by the principal. Proof routes may be abandoned; the target does not change.

## E0. Source reduction

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

The source-corrected unresolved chamber is

$$
\boxed{
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
}
$$

The fixed-wall route and the cellwise scaffold-positivity route are closed.

## E1. Reusable hidden-interaction algebra

In complemented spins, with

$$
B=b+c-a,\qquad \rho=\frac cB,
$$

a hidden successful rightward dual interaction has signed type average

$$
B\eta_i-c=B(\eta_i-\rho).
$$

For the noise-reduced process `L^-`, after explicit burn-in the hidden insertion is nonnegative against nonnegative right-history-measurable companions.

One-cell regional integration removes the raw left-spin Duhamel dependence, but two-cell composition has signed transfer

$$
\Psi_\Delta(z)=(b+c-a)K_\Delta(z)-c
$$

and is negative on sufficiently short cells at every residual parameter point.

**Status:** correct reusable mathematics; the cellwise last-exit/scaffold route is closed.

## E2. Direct transient information on the original dynamics

Student G Assignment 001, Professor-checked at Meeting 001, gives

$$
\boxed{
\frac d{dt}m_i
=(b+c)-(1+b+c)m_i-(b+c-a)q_i+c(m_i-m_{i+1}),
}
$$

with boundary-uniform transient zero-density and finite-box concentration, plus

$$
\boxed{
\frac d{dt}\mathbb P(11)
\le b-(1+b)\mathbb P(11).
}
$$

These are direct dynamical inputs, but marginal density / `11` control does not by itself close disagreement contraction.

## E3. Coupling drift and high-risk state

For

$$
D_i=1_{\{X_i\ne Y_i\}},
$$

and

$$
J_i=1_{\{D_i=0,D_{i+1}=1,X_i=Y_i=1\}},
$$

one has

$$
\boxed{
\mathcal L^{\rm coup}D_i
\le
-(1-c+a)D_i+(b-a)D_{i+1}+(c-b+a)J_i.
}
$$

A useful environmental estimate must control `J_i` weighted by disagreement. Substituting only the marginal `11` probability creates an additive error.

**Status:** Professor-checked direct bridge and precise missing weighted quantity.

## E4. Uniform coalescence hazard for every disagreement

Student F Assignment 004 strengthens the rightmost-source observation.

Put

$$
q:=1-c+a>0.
$$

At an update of any disagreeing site, the four possible right-neighbour pair states give coalescence probabilities

$$
1-c+a,\qquad 1-b,\qquad 1-a,\qquad 1-c+b.
$$

All are at least `q` throughout `R`. Therefore

$$
\boxed{
D_i=1
\Longrightarrow
\text{predictable coalescence intensity of site }i\ge q,
}
$$

without a rightmost hypothesis and without fixing the disagreement orientation.

If `T_i` is the next coalescence of a disagreeing site and `R_{i-1}` the next ring immediately to its left, then

$$
\boxed{
\mathbb P(T_i<R_{i-1}\mid\mathcal F)
\ge
p:=\frac q{1+q}.
}
$$

**Status:** Professor-checked structural live-coupling lemma.

## E5. One-source and two-generation regeneration

For a rightmost source `j` with `j-1` agreed, Meeting 003 proved a positive probability that the source dies before creating its first child.

Assignment 004 now controls the correct post-birth state. After the first child at `j-1` has been created, with `j-2` still agreed, let `sigma_2` be grandchild creation and `tau_2` elimination of both parent and child. The race lemma E4 applied twice yields

$$
\boxed{
\mathbb P(\tau_2<\sigma_2\mid\mathcal F)
\ge
p^2
=
\left(\frac{1-c+a}{2-c+a}\right)^2>0.
}
$$

The full process still permits arbitrary child death and reinfection outside this successful clearing subevent. The bound is uniform over the actual common right environment and all post-first-child local states.

**Status:** Professor-checked two-generation live-episode contraction.

## E6. East-boundary stress test

Along

$$
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
$$

the crude universal two-generation clearing event has probability `4 epsilon^4+O(epsilon^6)`. However, F's exact controlled 24-state post-birth calculation on structured states gives much stronger regeneration gaps of order `epsilon` even against a state-feedback right-boundary adversary.

For prospective grandchild spin zero,

$$
V_*=1-\frac92\varepsilon+O(\varepsilon^2),
$$

and for prospective grandchild spin one,

$$
V_*=1-\varepsilon+O(\varepsilon^2).
$$

**Status:** diagnostic, not load-bearing. It confirms a real post-birth killing mechanism but no uniform East-boundary gap.

## E7. Finite-depth ordered clearing and correction

The ordered-clearing argument extends to arbitrary finite active-span depth.

If the live disagreement episode occupies a span of depth at most `m` between a coupled left boundary and coupled right tail, sequentially require the current leftmost disagreement to coalesce before the next ring at the agreed site immediately to its left. Each successful race has conditional probability at least `p`, and each success permanently advances the coupled prefix by at least one site. Hence

$$
\boxed{
\mathbb P(\text{clear a depth-}m\text{ episode before a new disagreement crosses its left boundary}\mid\mathcal F)
\ge p^m.
}
$$

The exponent is **active-span depth**, not merely current disagreement count. Internal agreed gaps can be infected and therefore do not justify counting only currently off-diagonal sites.

Since

$$
\sum_{m\ge1}p^m<\infty,
$$

these certified depth-dependent clearing gaps are summable. They do not force extinction when failures increase ancestry depth indefinitely.

**Status:** finite-depth theorem plus explicit obstruction to naive depth-by-depth multiplication.

## E8. Current load-bearing edge: all-depth disagreement-stack contraction

Finite-depth escalation stops here. Do not compute separate depth-three, depth-four, etc. episodes.

The remaining problem is to control arbitrary ancestry depth structurally. A qualifying next edge must be one of:

1. a weighted disagreement-stack Lyapunov/supermartingale with negative drift;
2. a finite multi-type branching/influence domination with spectral radius `<1`;
3. a disagreement-weighted `J_i` estimate that closes E3 after summation / Gronwall;
4. a finite summary or restart kernel dominating arbitrary deeper stacks;
5. a rigorous obstruction showing that a materially defined class of all-depth contractions cannot work.

The uniform coalescence lemma E4 is the principal new input. The crude contact-process comparison using death `q` and maximal left-birth rate is not expected to suffice near the East boundary unless additional state structure is proved.

Student F is attacking E8 in `students/student-f/assignment-005.md`. Student G is still completing Assignment 002 and may independently provide the weighted `J_i` control.

## Anti-circularity checkpoint

Meeting 004 resolves the two-generation reinfection question positively and immediately tests composition far enough to show why finite-depth positive numbers are not a proof. The next accepted spine change must handle arbitrary depth in one structural theorem or eliminate such a theorem. A third-generation hitting probability alone does not count.

## Current direction

Attack E8 while preserving the fixed positive-rates target.
