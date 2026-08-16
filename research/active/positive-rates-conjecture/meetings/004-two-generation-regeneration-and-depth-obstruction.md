# Group meeting 004: two-generation regeneration holds; finite-depth clearing is not an all-depth contraction

Date: 2026-08-16

Professor review of:

- Student F, commit `893700c`, `students/student-f/004-two-generation-episode.md`;
- exact verifier commit `5e3c4bc`, `students/student-f/004-two-generation-verifier.py`;
- Meeting 003 and Student F Assignment 003;
- the current proof spine and the closed frozen-wall / cellwise-scaffold routes.

Student G is still working on Assignment 002. This meeting does not wait for that return because F has resolved the exact two-generation question set at Meeting 003. G's return will be folded into the next meeting.

state_narrowed: yes

Evidence pointer: `students/student-f/004-two-generation-episode.md`, especially Sections 2--10, and `students/student-f/004-two-generation-verifier.py`.

## Previous bottleneck

Meeting 003 established a positive childless probability for one rightmost live source, but the estimate could not be iterated because the first child is not rightmost and can die and be reinfected while its parent survives. The next question was whether the full parent-child episode has a genuine regeneration probability after reinfection is retained exactly.

## Professor verification: every disagreement has a uniform local coalescence hazard

Put

$$
q:=1-c+a>0.
$$

Suppose site `i` disagrees. At its next rate-one update, if the pair at `i` is `(0,1)`, the four possible pair states at `i+1` give post-update disagreement probabilities

$$
c-a,\qquad b,\qquad a,\qquad c-b,
$$

and therefore coalescence probabilities

$$
1-c+a,\qquad 1-b,\qquad 1-a,\qquad 1-c+b.
$$

Subtracting `q` gives

$$
0,\qquad c-a-b,\qquad c-2a,\qquad b-a.
$$

All are nonnegative in the residual chamber: `c>=a+b`, `b>a`, and therefore `c-2a=(c-a-b)+(b-a)>0`. The opposite disagreement orientation gives the same four values in permuted order.

Hence, for **every** disagreement site, regardless of whether its right neighbour is agreed or disagreed and regardless of orientation,

$$
\boxed{
\text{predictable coalescence intensity}\ge q=1-c+a.
}
$$

This strictly strengthens Meeting 003, where the lower hazard had only been used for a rightmost disagreement.

## Stopping-time race

Let `T_i` be the next coalescence time of a currently disagreeing site `i`, and let `R_{i-1}` be the next ring of the independent rate-one clock at the site immediately to its left. The lower coalescence hazard `q`, together with independence of the left clock, gives

$$
\boxed{
\mathbb P(T_i<R_{i-1}\mid\mathcal F)
\ge p:=\frac q{1+q}.
}
$$

This remains true while all other clocks and the entire right-hand coupled environment evolve arbitrarily.

## Two-generation regeneration

After the first child at `j-1` has been born from rightmost parent `j`, let `j-2` still be agreed. Let `sigma_2` be first creation of a disagreement at `j-2`, and `tau_2` the first time both `j` and `j-1` are coupled.

Use the race bound twice:

1. require the child `j-1` to coalesce before the clock at `j-2` rings;
2. at that coalescence time, if the parent is still alive, require the parent `j` to coalesce before the next ring at `j-1`.

On this event no grandchild is created, no reinfection of the child occurs after its coalescence, and after parent coalescence the half-line from `j-1` rightward is permanently coupled. Strong Markov gives

$$
\boxed{
\mathbb P(\tau_2<\sigma_2\mid\mathcal F)
\ge p^2
=
\left(\frac{1-c+a}{2-c+a}\right)^2>0.
}
$$

Equivalently,

$$
\boxed{
\mathbb P(\sigma_2<\tau_2\mid\mathcal F)
\le
1-\left(\frac{1-c+a}{2-c+a}\right)^2.
}
$$

The bound is uniform over every actual common right-hand history and every post-first-child local orientation/state. Reinfection has not been removed from the process: the proof isolates a positive-probability subevent of the genuine episode on which reinfection does not get the opportunity to occur.

This is a valid two-generation live-episode contraction and is strictly stronger than the one-source result.

## Near-East controlled calculation

F's 24-state calculation is not load-bearing for the universal two-generation theorem, but I checked the reduction and the verifier logic sufficiently for its diagnostic use.

For

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

and structured state `(G,C,P)=(00,01,01)`, the exact fixed-boundary systems give

$$
V_0=\frac35-\frac{24}{25}\varepsilon+O(\varepsilon^2),
$$

and

$$
V_1=\frac13+\frac29\varepsilon+O(\varepsilon^2).
$$

The stronger state-feedback control problem over the common parent boundary has certified local HJB inequalities and gives

$$
V_*=1-\frac92\varepsilon+\frac{135}{4}\varepsilon^2+O(\varepsilon^3)
$$

from grandchild spin zero, and

$$
V_*=1-\varepsilon+O(\varepsilon^2)
$$

from grandchild spin one.

Thus the post-birth killing mechanism is real: the robust structured two-generation regeneration gap is order `epsilon`, rather than the order `epsilon^2` worst-case first-generation gap. It still degenerates at the excluded East boundary. No residual-uniform conclusion is inferred from this diagnostic.

## Correction to the finite-depth statement in F's report

The report's Proposition 9.1 is usable after one wording correction.

The proof gives a lower bound `p^m` when `m` bounds the **length/depth of the finite active disagreement span from the coupled left boundary to the coupled right tail**, not merely the number of disagreement sites currently present. If there are internal agreed gaps, those sites can be infected while clearing earlier disagreements, so the number of currently disagreeing sites alone is not a safe stage count.

With `m` interpreted as active-span depth, the ordered-clearing proof is valid: each successful race permanently advances the coupled prefix by at least one site, and at most `m` races are needed. Hence

$$
\mathbb P(\text{clear the entire depth-}m\text{ episode before any new disagreement crosses its left boundary}\mid\mathcal F)
\ge p^m.
$$

This correction does not change F's composition conclusion. Since

$$
\sum_{m\ge1}p^m<\infty,
$$

the certified depth-dependent gaps are summable, and

$$
\prod_{m\ge1}(1-p^m)>0.
$$

Therefore the currently proved ordered-clearing events do not force extinction of an indefinitely growing ancestry stack.

## Ruling

The live-episode route remains active and has made another genuine gain.

What is now established is stronger than a sequence of isolated finite-state computations:

1. every disagreement site, including a non-rightmost descendant, has coalescence hazard at least `q`;
2. the full two-generation parent-child episode has a positive environment-uniform regeneration probability with reinfection retained;
3. every fixed active-span depth has a positive ordered-clearing event.

The remaining obstruction is now **all-depth composition**. We will not proceed by computing depth three, depth four, and so on. That would be the finite-depth analogue of the reformulation loop the principal explicitly asked us to avoid.

The next accepted theorem must control arbitrary ancestry depth structurally. Useful forms include:

- a weighted Lyapunov/supermartingale for the disagreement stack with negative drift;
- a finite multi-type domination whose spectral radius is below one;
- a disagreement-weighted estimate for the high-risk `J_i` occupation that closes the coupling drift;
- a finite summary/restart kernel that dominates every deeper ancestry configuration;
- or a rigorous obstruction showing that this entire class of all-depth contractions cannot hold.

A third-generation hitting probability by itself will not count as progress.

## Direction

Continue on the fixed positive-rates target. Route Student F to an all-depth disagreement-stack theorem or obstruction. Student G should finish Assignment 002 unchanged; its result may supply precisely the weighted `J_i` control needed here and will be folded in at the next meeting.
