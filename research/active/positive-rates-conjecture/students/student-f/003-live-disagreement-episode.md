# Student F 003: live disagreement source contraction under the true coupling

## Verdict

The first live-source estimate exists and is elementary enough to be exact.

Under the canonical common-uniform coupling, take a **rightmost disagreement** at site `j`: the two copies disagree at `j` and agree on the whole half-line strictly to its right. Assume the site `j-1` immediately to its left is still agreed. Let

\[
\tau=\inf\{t\ge0:X_j(t)=Y_j(t)\}
\]

be death of the rightmost source and

\[
\sigma=\inf\{t\ge0:X_{j-1}(t)\ne Y_{j-1}(t)\}
\]

be creation of its first left child.

Write

\[
d=b-a,\qquad q=1-c+a.
\]

Throughout the residual chamber, `d,q>0`. Conditional on **any actual common right-hand history**, the source coalescence hazard is at least `q`. Before `sigma`, the agreed spin at `j-1` is a two-state chain whose exact child-creation rates are `d` from state zero and `c` from state one. Solving this killed two-state chain gives

\[
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F_0)
\le h_1=1-\delta<1,
}
\]

uniformly over the common environment, where

\[
D=(b+q)(1+q)-a(1-c)
\]

and

\[
\boxed{
\delta=\frac{q(d+2q)}D>0.
}
\]

If the agreed spin immediately to the left is zero, the sharper bound is `h_0<h_1`, with

\[
1-h_0=\frac{q(a+q+1)}D.
\]

This is an **actual source-episode contraction**. The exterior disagreement is not frozen: it evolves at its true clock and is allowed to disappear. The common right environment also evolves arbitrarily. The estimate is valid conditionally at stopping times and hence is compatible with a regeneration construction.

There is also a finite-slab version. For every `T>0`,

\[
\boxed{
\mathbb P(\tau<\sigma,\ \tau\le T\mid\mathcal F_0)
\ge
\delta_T
:=
\frac{1-c+a}{1+a}
\left(1-e^{-(1+a)T}\right)>0.
}
\]

Thus an agreed block immediately to the left of a rightmost live source has a positive, explicit probability of being permanently protected from that source episode during the slab because the source dies before producing any child.

This does not yet prove ergodicity. Once a child is produced, it is generally **not** rightmost; its coalescence law changes because its right neighbour can itself disagree, and repeated reinfection prevents multiplying the one-source factor `delta` site by site. The report below identifies that exact next obstruction and derives a coupling-generator inequality that interfaces it with Student G's `11`-suppression estimate.

## 1. Convention and canonical coupling

Use the original normalized spin convention of Student G. At an update of site `i`, if the current local state is `(x,y)=(eta_i,eta_{i+1})`, the new spin is Bernoulli with parameter

\[
r_{00}=a,\qquad r_{01}=b,\qquad r_{10}=c,\qquad r_{11}=0.
\tag{1.1}
\]

The residual chamber is

\[
0<a<b,\qquad \frac12\le c<1,\qquad c\ge a+b,
\qquad b\ge\sqrt2(1-c).
\tag{1.2}
\]

Couple two copies `X,Y` with the same rate-one clock at each site and the same uniform mark `U`. At a ring of site `i`, set

\[
X_i'=1_{\{U<r_{X_iX_{i+1}}\}},
\qquad
Y_i'=1_{\{U<r_{Y_iY_{i+1}}\}}.
\tag{1.3}
\]

If

\[
p=r_{X_iX_{i+1}},\qquad \widetilde p=r_{Y_iY_{i+1}},
\]

then the post-update pair has probabilities

\[
\begin{array}{c|c}
(X_i',Y_i') & \text{probability}\\ \hline
(1,1) & \min(p,\widetilde p)\\
(0,0) & 1-\max(p,\widetilde p)\\
(1,0) & (p-\widetilde p)_+\\
(0,1) & (\widetilde p-p)_+.
\end{array}
\tag{1.4}
\]

In particular, if

\[
D_i=1_{\{X_i\ne Y_i\}},
\]

then at a ring of `i`

\[
\mathbb P(D_i'=1\mid X,Y)
=
\left|r_{X_iX_{i+1}}-r_{Y_iY_{i+1}}\right|.
\tag{1.5}
\]

This local identity is the only coupling input used below.

## 2. Exact death hazard of a rightmost disagreement

Suppose `j` is a rightmost disagreement. Thus

\[
X_j\ne Y_j,
\qquad
X_k=Y_k\quad\text{for all }k\ge j+1.
\tag{2.1}
\]

By one-sidedness and the common graphical construction, the half-line `k>=j+1` remains coupled forever. Let its current common spin immediately to the right be

\[
Z(t)=X_{j+1}(t)=Y_{j+1}(t).
\]

While the source at `j` is alive, its two current spins are `0,1` in some orientation.

If `Z=0`, the two update probabilities at the source are `a,c`. Hence a source update leaves a disagreement with probability `c-a` and coalesces the pair with probability

\[
q_0=1-(c-a)=1-c+a.
\tag{2.2}
\]

If `Z=1`, the two probabilities are `b,0`; the source coalesces with probability

\[
q_1=1-b.
\tag{2.3}
\]

The residual inequality `c>=a+b` gives

\[
q_1-q_0=c-a-b\ge0.
\tag{2.4}
\]

Therefore, conditional on every realized common right-hand history,

\[
\boxed{
\text{source-death intensity}\ge q:=1-c+a>0.
}
\tag{2.5}
\]

This is where the present calculation differs from the closed fixed-wall route: the disagreement source is not held off-diagonal. Its own true updates create a positive killing intensity.

## 3. Exact pre-child dynamics of the left neighbour

Before the first child time `sigma`, the pair at `j-1` is agreed. Write its common value as `x in {0,1}`.

Because the source pair at `j` is off-diagonal, orientation is irrelevant for the following probabilities.

### 3.1 Agreed zero immediately to the left

If `x=0`, the two local update probabilities at `j-1` are `a,b`. Therefore one update of `j-1` gives

- a new disagreement with probability `d=b-a`;
- common value `1` with probability `a`;
- common value `0` with probability `1-b`.

Ignoring self-loops, the effective transitions are

\[
0\xrightarrow{d}\text{child},
\qquad
0\xrightarrow{a}1.
\tag{3.1}
\]

### 3.2 Agreed one immediately to the left

If `x=1`, the two local update probabilities are `c,0`. Hence

\[
1\xrightarrow{c}\text{child},
\qquad
1\xrightarrow{1-c}0.
\tag{3.2}
\]

The source has, simultaneously, death intensity at least `q` from (2.5).

Consequently the probability of producing a child before source death is maximized by replacing the actual, history-dependent source-death rate by the constant minimal rate `q`. This produces a two-state killed continuous-time Markov chain. No environment is frozen: this is a stochastic domination of the true source lifetime, uniform over the actual right-hand trajectory.

## 4. Exact rightmost-source contraction

Let `h_0,h_1` denote the probability that the dominating chain produces a child before its independent rate-`q` killing, starting from the agreed left spin `0` or `1` respectively.

First-step equations using (3.1)--(3.2) are

\[
(b+q)h_0=d+a h_1,
\tag{4.1}
\]

and

\[
(1+q)h_1=c+(1-c)h_0.
\tag{4.2}
\]

Put

\[
D=(b+q)(1+q)-a(1-c).
\tag{4.3}
\]

Since `q,d,a>0`, one may also write

\[
D=a^2+a+dq+d+q^2+q>0.
\tag{4.4}
\]

Solving (4.1)--(4.2) gives

\[
\boxed{
h_0=\frac{d(1+q)+ac}{D},}
\tag{4.5}
\]

\[
\boxed{
h_1=\frac{c(b+q)+(1-c)d}{D}.}
\tag{4.6}
\]

The complements simplify to

\[
\boxed{
1-h_0=\frac{q(a+q+1)}D>0,
}
\tag{4.7}
\]

and

\[
\boxed{
1-h_1=\frac{q(d+2q)}D>0.
}
\tag{4.8}
\]

Moreover

\[
h_1-h_0
=
\frac{q(c-d)}D>0,
\tag{4.9}
\]

because `d=b-a<c` in the residual chamber.

Therefore the worst initial agreed spin is `1`, and we obtain:

### Proposition 4.1 (rightmost-source childless regeneration)

At any stopping time at which `j` is a rightmost disagreement and `j-1` is agreed,

\[
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F)
\le
1-\delta,
\qquad
\delta:=\frac{q(d+2q)}D>0.
}
\tag{4.10}
\]

The estimate is uniform over the entire common configuration on the right and over its future evolution.

If the agreed spin at `j-1` is zero, replace `delta` by the larger gap in (4.7).

This is an episode quantity, not a one-attack frozen-wall statistic. Between the initial time and `sigma wedge tau`, both the source and its right environment may update arbitrarily many times.

## 5. Finite-time slab regeneration

There is a simpler, explicit finite-time version useful for coarse graining.

Before `sigma`, child creation at `j-1` has intensity at most `c`. Source death has intensity at least `q`. Couple these with independent comparison clocks of rates `c` and `q`. If the rate-`q` source-death clock rings before the rate-`c` potential-child clock and before time `T`, then the true source has died before producing a child.

Therefore

\[
\begin{aligned}
\mathbb P(\tau<\sigma,\ \tau\le T\mid\mathcal F)
&\ge
\int_0^T q e^{-(q+c)t}\,dt\\
&=
\frac q{q+c}(1-e^{-(q+c)T}).
\end{aligned}
\tag{5.1}
\]

Since `q+c=1+a`,

\[
\boxed{
\delta_T
=
\frac{1-c+a}{1+a}
\left(1-e^{-(1+a)T}\right)>0.
}
\tag{5.2}
\]

### Corollary 5.1 (agreed-block protection in one slab)

Suppose an interval immediately to the left of `j` is coupled at the initial stopping time, while `j` is the rightmost disagreement. With conditional probability at least `delta_T`, by time `T` the source has coalesced and no disagreement from that source has entered the interval.

On this event the source cannot reappear: the whole right half-line is coupled, so after `j` coalesces, site `j` remains coupled forever.

For any block length `L`, the event that this source episode reaches the left endpoint of the initially agreed block is contained in `{sigma<tau}`. Hence the infinite-episode bound (4.10) also gives

\[
\boxed{
\mathbb P(\text{source episode crosses the agreed block}\mid\mathcal F)
\le1-\delta<1.
}
\tag{5.3}
\]

The present estimate does not improve with `L`; obtaining decay in `L` requires controlling descendants after the first child is born.

## 6. Exact coupling-generator bridge to Student G's `11` estimate

The one-source calculation can be connected directly to the transient information from Student G.

For any coupled configuration define

\[
D_i=1_{\{X_i\ne Y_i\}},
\tag{6.1}
\]

and define the high-risk state

\[
J_i
=
1_{\{D_i=0,\ D_{i+1}=1,\ X_i=Y_i=1\}}.
\tag{6.2}
\]

Thus `J_i=1` means site `i` is still agreed, the site to its right disagrees, and the agreed left spin is the high-transmission value `1`.

Let

\[
\Delta_i
=
\left|r_{X_iX_{i+1}}-r_{Y_iY_{i+1}}\right|.
\]

A complete local case split gives

\[
\boxed{
\Delta_i
\le
(c-a)D_i+dD_{i+1}+(c-d)J_i.
}
\tag{6.3}
\]

The cases are:

1. `D_i=0,D_{i+1}=0`: `Delta_i=0`.
2. `D_i=0,D_{i+1}=1`, common spin at `i` zero: `Delta_i=d`.
3. `D_i=0,D_{i+1}=1`, common spin at `i` one: `Delta_i=c`, and `J_i=1`, so the right side is `d+(c-d)=c`.
4. `D_i=1,D_{i+1}=0`: the rate differences are `c-a` when the common right spin is zero and `b` when it is one. The latter is at most `c-a` because `c>=a+b`.
5. `D_i=D_{i+1}=1`: equal orientations give rate difference `a`; opposite orientations give `c-b`. Both are at most `c-a`: `c>=a+b>2a` gives `a<c-a`, and `b>a` gives `c-b<c-a`.

Since only an update at `i` changes `D_i`, (1.5) gives

\[
\mathcal L^{\rm coup}D_i=\Delta_i-D_i.
\]

Using `q=1-c+a`, (6.3) yields the pathwise drift inequality

\[
\boxed{
\mathcal L^{\rm coup}D_i
\le
-qD_i+dD_{i+1}+(c-d)J_i.
}
\tag{6.4}
\]

This is the cleanest direct interface I found between disagreement propagation and the actual spin environment.

If

\[
u_i(t)=\mathbb P(X_i(t)\ne Y_i(t)),
\]

then

\[
\boxed{
u_i'(t)
\le
-q u_i(t)+d u_{i+1}(t)+(c-d)\mathbb E J_i(t).
}
\tag{6.5}
\]

Now `J_i=1` forces an adjacent `11` in exactly one of the two copies, because the right pair is off-diagonal and the agreed left spin is one. Therefore

\[
\mathbb E J_i(t)
\le
\mathbb P(X_i=X_{i+1}=1)
+
\mathbb P(Y_i=Y_{i+1}=1).
\tag{6.6}
\]

Student G's Professor-checked estimate gives, for each copy and every initial law,

\[
\mathbb P(11\text{ at edge }i)
\le
\frac{b+e^{-(1+b)t}}{1+b}.
\tag{6.7}
\]

Hence

\[
\boxed{
u_i'(t)
\le
-q u_i(t)+d u_{i+1}(t)
+
\frac{2(c-d)}{1+b}
\left(b+e^{-(1+b)t}\right).
}
\tag{6.8}
\]

Equation (6.8) is a genuine density-to-disagreement bridge, but it also shows why the present unweighted density information is not yet a proof. Replacing the correlated quantity `E J_i` by a marginal `11` bound creates an additive error that does not vanish with the disagreement probability.

The sharper quantity one would want is an occupation or conditional estimate for

\[
J_i
=
1_{\{\text{right disagreement}\}}
1_{\{\text{agreed left spin}=1\}},
\]

not merely the unconditional probability of `11`.

## 7. Why the no-`11` snapshot is not by itself a regeneration event

There is a second, complementary obstruction to using Student G's current good event directly.

Consider the genuine residual path

\[
\boxed{
a=\varepsilon^2,\qquad
b=\varepsilon,\qquad
c=1-\varepsilon^2,
\qquad 0<\varepsilon\le\frac12.
}
\tag{7.1}
\]

Indeed,

\[
0<a<b,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c),
\quad c\ge\frac12.
\]

Start the two copies from the all-zero configuration except for one rightmost source at `j`, say

\[
(X_j,Y_j)=(0,1).
\tag{7.2}
\]

Both individual configurations have **no adjacent `11` anywhere**, and the common environment is maximally zero-rich.

Before any change of this local hard-core geometry, Poisson splitting gives the following relevant rates:

- child creation at `j-1`: `d=b-a=epsilon-epsilon^2`;
- source death while `j+1=0`: `q=1-c+a=2epsilon^2`;
- common `0->1` change at `j-1`: rate `a=epsilon^2`;
- common `0->1` change at `j+1`: rate `a=epsilon^2`.

All other local marks are self-loops for this first-event comparison. Therefore the probability that the disagreement creates a left child **before any of the three competing mechanisms can destroy the initial hard-core/all-zero geometry** is exactly

\[
\boxed{
\frac d{d+q+2a}
=
\frac{1-\varepsilon}{1+3\varepsilon}
\longrightarrow1.
}
\tag{7.3}
\]

At that child-creation event, one copy acquires an adjacent `11` across the source edge. Thus a live disagreement can itself be the mechanism that exits the hard-core sector.

This does not contradict Proposition 4.1: for each fixed positive parameter point the childless gap `delta` is strictly positive. It shows instead that a statement of the form

> "after burn-in there are many zeros / no adjacent `11`, therefore a live disagreement has a residual-uniform chance bounded away from one of propagating"

is false. Along (7.1), even the perfect all-zero/no-`11` local state has first-transmission probability tending to one.

For the exact rightmost-source formula, along (7.1)

\[
1-h_0
=
\frac{2\varepsilon(3\varepsilon^2+1)}
{3\varepsilon^3+2\varepsilon^2+2\varepsilon+1}
\sim2\varepsilon,
\tag{7.4}
\]

while the worst-spin uniform gap satisfies

\[
\delta=1-h_1
=
\frac{2\varepsilon^2(3\varepsilon+1)}
{3\varepsilon^3+2\varepsilon^2+2\varepsilon+1}
\sim2\varepsilon^2.
\tag{7.5}
\]

So the new regeneration probability is real but becomes small near this East boundary, exactly where a more structured multi-site episode argument is needed.

## 8. What has and has not been proved

### 8.1 New irreversible estimate

The frozen-source obstruction from the old noisy-East programme is removed at the first episode level. A rightmost source has a strictly positive probability `delta` of disappearing before creating any child, uniformly over the **evolving** common environment to its right. The finite-time version `delta_T` is explicit.

This is strictly different from the old one-attack wall factor: the source clock is part of the probability space and source death is the regeneration mechanism.

### 8.2 Exact interface with the transient density estimates

The pointwise generator inequality

\[
\mathcal L^{\rm coup}D_i
\le
-qD_i+dD_{i+1}+(c-d)J_i
\]

identifies the environmental quantity that actually accelerates propagation. Student G's `11` estimate controls `J_i` only additively through its marginal probability.

### 8.3 Remaining obstruction

After a child is born, there may be two adjacent disagreements. The child is no longer rightmost, and its local coalescence probability depends on the disagreement orientation to its right. If it dies while its parent remains alive, the parent can reinfect it. Therefore one cannot multiply the factor `1-delta` across successive sites.

A useful next calculation is now narrower than "control a live source": analyze the **two-generation episode after the first child is born**, retaining the parent until its actual death, and bound the probability that the parent-child system creates a grandchild before both sources behind that edge are eliminated. The local state created by a child from an agreed zero is particularly structured: parent and child have the same disagreement orientation, and an update of the child coalesces it with probability `1-a`. This fast post-birth killing is not used in Proposition 4.1 and is the most concrete possible gain left by the present calculation.

## 9. Anti-circularity check

The previous live statement was qualitative: allow the exterior source to evolve and seek an episode contraction.

The present report proves two quantitative statements that can be checked without ergodicity:

\[
\mathbb P(\sigma<\tau\mid\mathcal F)\le1-\delta<1
\]

and

\[
\mathbb P(\tau<\sigma,\tau\le T\mid\mathcal F)\ge\delta_T>0.
\]

It also derives the exact local drift bridge (6.4). None is equivalent to convergence or uniqueness.

The next falsifiable question is whether the two-generation parent-child episode has a similar contraction after reinfection is included. A negative exact finite-state result there would show that the single-source regeneration does not compose; a positive result would be genuinely stronger than the frozen-wall and scaffold quantities already closed.

## Verifier

`students/student-f/003-live-disagreement-verifier.py` checks the closed formulas, the local coupling inequality on rational residual samples, the strict sample `(a,b,c)=(0.1,0.3,0.8)`, and the residual near-East diagnostic (7.1)--(7.3). No simulation is used.

At the strict sample,

\[
h_0=\frac{17}{38}\approx0.44737,
\qquad
h_1=\frac{13}{19}\approx0.68421,
\qquad
\delta=\frac6{19}\approx0.31579.
\]

## Handoff

`live-source contraction proved: for a rightmost disagreement under the true canonical coupling, with q=1-c+a and d=b-a, the probability of creating a first left child before the source coalesces is at most h_1=1-delta, where delta=q(d+2q)/((b+q)(1+q)-a(1-c))>0 uniformly over the evolving common right-hand environment; moreover a finite slab has regeneration probability at least delta_T=((1-c+a)/(1+a))(1-e^{-(1+a)T}); the exact coupling drift is L D_i <= -q D_i+d D_{i+1}+(c-d)J_i, so the next nontrivial obstruction is the two-generation parent-child episode and the conditional occupation of the high-risk J_i state rather than unweighted zero/no-11 density.`
