# Group meeting 003: live-source contraction holds; next obstruction is two-generation reinfection

Date: 2026-08-16

Professor review of:

- Student F, commit `d0a508c`, `students/student-f/003-live-disagreement-episode.md`;
- exact verifier commit `f379cd3`, `students/student-f/003-live-disagreement-verifier.py`;
- Meeting 002 and the closed frozen-wall / cellwise-scaffold routes;
- Student G's Professor-checked Assignment 001 density and adjacent-`11` estimates, as used in F's coupling bridge.

Student G is still working on Assignment 002. This meeting does not wait for that return because F has resolved the live-source question set at Meeting 002. G's return will be folded into the next meeting.

state_narrowed: yes

Evidence pointer: `students/student-f/003-live-disagreement-episode.md`, especially Sections 2--8, and `students/student-f/003-live-disagreement-verifier.py`.

## Previous bottleneck

Meeting 002 left a direct-dynamics question: once the exterior disagreement source is allowed to evolve and die under the true canonical coupling, is there any quantitative source-episode contraction, or does the frozen-source obstruction survive unchanged?

## Professor verification of the rightmost-source calculation

Work in the original normalized spin convention. Under the common-uniform coupling, suppose `j` is a rightmost disagreement and `j-1` is still agreed. Write

$$
d=b-a>0,
\qquad
q=1-c+a>0.
$$

Let `tau` be source death at `j` and `sigma` creation of the first disagreement at `j-1`.

Because the entire half-line strictly right of `j` is coupled, it remains coupled forever. While `j` is off-diagonal, let the common spin at `j+1` be `z`.

If `z=0`, the two source update probabilities are `a,c`, so a source update coalesces the pair with probability

$$
1-(c-a)=1-c+a=q.
$$

If `z=1`, the update probabilities are `b,0`, so coalescence probability is `1-b`. The residual inequality `c\ge a+b` gives

$$
1-b\ge1-c+a=q.
$$

Thus, conditional on any realized common right-hand history, source death has predictable intensity at least `q`.

Before `sigma`, the left pair is agreed. If its common value is zero, an update produces a child with rate `d=b-a` and changes the common value to one with rate `a`. If its common value is one, an update produces a child with rate `c` and changes the common value to zero with rate `1-c`.

These rates are independent of the disagreement orientation at `j`. Replacing the actual source-death hazard by the constant lower hazard `q` therefore gives a genuine stochastic upper bound on child-before-death probability. The killed two-state first-step equations are

$$
(b+q)h_0=d+a h_1,
$$

$$
(1+q)h_1=c+(1-c)h_0.
$$

With

$$
D=(b+q)(1+q)-a(1-c)>0,
$$

the exact solutions are

$$
h_0=\frac{d(1+q)+ac}{D},
\qquad
h_1=\frac{c(b+q)+(1-c)d}{D}.
$$

I rechecked the simplifications

$$
1-h_0=\frac{q(a+q+1)}D>0,
$$

$$
1-h_1=\frac{q(d+2q)}D>0,
$$

and

$$
h_1-h_0=\frac{q(c-d)}D>0.
$$

Since `d<c` in the residual chamber, the common-left-spin value one is the worst case. Therefore at every stopping time with the stated rightmost-source geometry,

$$
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F)
\le1-\delta,
\qquad
\delta=\frac{q(d+2q)}D>0.
}
$$

This is uniform over the full common right configuration and its future evolution. It uses the true source clock; the source is not frozen.

## Finite-slab version

Before the first child, the child-creation intensity is at most `c`, while source death intensity is at least `q`. The source clock and left-site clock are independent graphical clocks, and constant-rate thinning gives a rate-`q` death subprocess and a rate-`c` potential-child superprocess. Hence

$$
\boxed{
\mathbb P(\tau<\sigma,\ \tau\le T\mid\mathcal F)
\ge
\delta_T
=
\frac{q}{q+c}(1-e^{-(q+c)T})
=
\frac{1-c+a}{1+a}(1-e^{-(1+a)T})>0.
}
$$

The strong Markov / post-stopping graphical independence needed to restart this estimate is standard and present here. This is a genuine finite-slab regeneration event for one live source.

The block statement in F's report must be read at this strength only: reaching any site to the left requires the event `sigma<tau`, so the probability that this particular source episode crosses an initially agreed block is at most `1-delta`. The bound does **not** decay with block length and is not yet an iteratable spatial contraction.

## Professor verification of the coupling-generator bridge

For

$$
D_i=1_{\{X_i\ne Y_i\}},
$$

and

$$
J_i=1_{\{D_i=0,\ D_{i+1}=1,\ X_i=Y_i=1\}},
$$

a direct check of the local pair states gives

$$
\left|r_{X_iX_{i+1}}-r_{Y_iY_{i+1}}\right|
\le
(c-a)D_i+dD_{i+1}+(c-d)J_i.
$$

Since only a rate-one update at `i` changes `D_i`, this yields the pathwise generator inequality

$$
\boxed{
\mathcal L^{\rm coup}D_i
\le
-qD_i+dD_{i+1}+(c-d)J_i.
}
$$

Also, `J_i=1` forces an adjacent `11` in exactly one of the two copies. Hence Student G's marginal `11` estimate does control `E J_i`, but only by an additive error independent of disagreement density. F is correct that this does not yet close the coupling inequality. The relevant missing environmental quantity is a disagreement-weighted or conditional occupation of `J_i`, not raw zero density.

## East-boundary diagnostic: ruling

The degeneration found by F is real but is **not a route-closing contradiction**.

Along

$$
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
$$

one has

$$
d\sim\varepsilon,
\qquad
q=2\varepsilon^2.
$$

Thus first-child creation occurs on a parametrically faster scale than rightmost-source death, and indeed

$$
\delta\sim2\varepsilon^2\to0.
$$

F's all-zero / no-`11` first-event calculation is also correct:

$$
\frac{d}{d+q+2a}
=
\frac{1-\varepsilon}{1+3\varepsilon}
\longrightarrow1.
$$

Therefore **no argument based only on a zero-rich or no-`11` snapshot can give a residual-uniform first-generation childless gap.** This is a genuine obstruction to that stronger hope.

I do not interpret the vanishing of `delta` itself as failure of the live-episode route. The conjecture is pointwise over strict positive-rate parameters; the East boundary `c=1` is outside the positive-rate chamber. A parameter-dependent positive contraction may be enough if it composes. More importantly, the first-child state contains dynamics not used in the one-source estimate: when a child is created from an agreed zero it has the same disagreement orientation as its parent, and its own update has a large coalescence probability. Whether that post-birth killing compensates for the slow parent death is the next finite question.

Thus the repeated East degeneration is structural for **first-generation / one-shot** quantities, through the scale separation `d/q`, but the present evidence does not justify a general claim that every live-episode mechanism must fail there.

## What has become strictly narrower

The frozen-source obstruction does not persist at the first live-source level. Every strict residual parameter has an explicit positive probability that the true rightmost source dies before producing any child, uniformly over the evolving common right environment.

The remaining obstruction is no longer "does a live source contract?" It is:

> after the first child is born, does the coupled parent-child system, including child death and reinfection by the still-live parent, have a positive probability of being eliminated before producing a grandchild, in a form that can restart spatially?

This is a finite two-generation problem. It is materially stronger than the one-source estimate and distinct from both previously closed routes.

## Ruling and next work

The live-disagreement route remains active.

Do **not** attempt to prove PRC by multiplying the one-source factor `1-delta` site by site. Once the first child exists, it is not rightmost, can die and be reinfected, and the Markov state is different.

Student F should now analyze the exact two-generation parent-child episode. The preferred output is either:

1. a parameter-point positive regeneration/contraction bound, valid after all reinfections are included, together with an explicit restart state that makes iteration plausible; or
2. an exact finite-state obstruction showing that the one-source contraction cannot be upgraded even at two generations.

The near-East scaling must be tested explicitly, but lack of a residual-uniform constant is not by itself failure. If a two-generation contraction is obtained, F must immediately identify whether it composes through a finite restart-state family rather than stopping at another isolated local inequality.

Student G should finish the already-running Assignment 002 unchanged. Its return may supply the missing `J_i`-weighted occupation control or independently eliminate that bridge; it will be incorporated at the next meeting.

## Anti-circularity check

This meeting resolves the exact object introduced at Meeting 002 with a positive quantitative estimate and identifies a strictly smaller composition problem. The next accepted progress must control the two-generation episode including reinfection, or falsify such control. Merely computing another first-child probability, another marginal density, or another frozen-source crossing statistic will not count.
