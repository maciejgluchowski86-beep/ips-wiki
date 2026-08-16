# Student F 004: two-generation live episode with reinfection

## Verdict

The two-generation parent--child episode has a uniform positive regeneration probability at every strict residual parameter point, even after all child deaths and reinfections are included in the underlying process.

The key new observation is stronger than Assignment 003's rightmost-source bound:

> **Every disagreement site has coalescence intensity at least**
> \[
> q:=1-c+a>0,
> \]
> **regardless of whether its right neighbour is agreed or disagreed and regardless of disagreement orientation.**

This gives a direct two-stage clearing event after the first child is born. If `j` is the rightmost parent, `j-1` its first child, and `j-2` is still agreed, then

\[
\boxed{
\mathbb P(\tau_2<\sigma_2\mid\mathcal F)
\ge
\delta_2(a,b,c)
:=
\left(\frac{q}{1+q}\right)^2
>0.
}
\]

Equivalently,

\[
\boxed{
\mathbb P(\sigma_2<\tau_2\mid\mathcal F)
\le
1-\left(\frac{1-c+a}{2-c+a}\right)^2.
}
\]

The bound is uniform over the actual common right-hand environment and over every post-first-child orientation/state. Reinfection is not removed from the model: the successful regeneration event is the positive-probability subevent on which the child coalesces before the grandchild-site clock rings and then the parent coalesces before the child-site clock rings again. Outside that event the full process, including arbitrary reinfections, continues unchanged.

The structured zero-born near-East calculation confirms that the post-birth killing mechanism is real and substantially stronger than the first-generation worst-case gap. An exact 24-state controlled CTMC gives, for

\[
a=\varepsilon^2,\qquad b=\varepsilon,\qquad c=1-\varepsilon^2,
\]

and structured state

\[
(\text{grandchild pair},\text{child pair},\text{parent pair})
=(00,01,01),
\]

the adaptive-control upper envelope

\[
\boxed{
V_*(\varepsilon)
=
1-\frac92\varepsilon
+\frac{135}{4}\varepsilon^2
+O(\varepsilon^3).
}
\]

Thus even against a stronger adversary that may choose the common right-boundary value as a state-feedback control, the regeneration gap is of order `epsilon`, not the order `epsilon^2` first-generation worst-case gap from Meeting 003. However, it still vanishes at the excluded East boundary. Fixed common right boundaries give different nontrivial limits (`3/5` for boundary zero and `1/3` for boundary one), so the exact structured episode genuinely depends on the right-boundary trajectory and on the common grandchild-site spin.

The positive two-generation estimate does **not** yet close spatial composition. After a grandchild is born, the state contains a three-generation disagreement stack, and the parent of the new leftmost site is no longer rightmost. There is nevertheless an exact finite-depth ordered-clearing lemma: a configuration with at most `m` live ancestral disagreements and a coupled right tail can be completely cleared before the next leftward creation with conditional probability at least

\[
\left(\frac q{1+q}\right)^m.
\]

This proves positive regeneration at every finite depth but gives no depth-uniform renewal constant. The natural product of the corresponding failure bounds need not tend to zero, because the clearing probabilities are summable in the depth. A new mechanism must therefore control the growing ancestry stack or prove a disagreement-weighted drift; the two-generation calculation alone cannot be iterated by restarting the same two-state episode.

## 1. Setup

Work in the original normalized spin convention

\[
r_{00}=a,\qquad r_{01}=b,\qquad r_{10}=c,\qquad r_{11}=0,
\]

in the residual chamber

\[
0<a<b,
\qquad
\frac12\le c<1,
\qquad
c\ge a+b,
\qquad
b\ge\sqrt2(1-c).
\]

Use the common-uniform coupling of two copies `X,Y`. At a rate-one update of site `i`, with local update probabilities

\[
p=r_{X_iX_{i+1}},
\qquad
\widetilde p=r_{Y_iY_{i+1}},
\]

the post-update pair at `i` disagrees with probability

\[
|p-\widetilde p|.
\]

Put

\[
D_i=1_{\{X_i\ne Y_i\}},
\qquad
q=1-c+a.
\]

Meeting 003 established the lower coalescence intensity `q` for a **rightmost** disagreement. The first step here is to remove the rightmost hypothesis.

## 2. Uniform coalescence of every disagreement

### Lemma 2.1

If `D_i=1`, then at the next update of site `i`, conditional on the complete coupled configuration,

\[
\boxed{
\mathbb P(D_i'=0\mid X,Y)\ge q=1-c+a.
}
\]

Therefore, while site `i` disagrees, its predictable coalescence intensity is at least `q`, regardless of the pair state at `i+1`.

### Proof

Assume first that

\[
(X_i,Y_i)=(0,1).
\]

The four possible pair states at `i+1` give the following coalescence probabilities at an update of `i`:

\[
\begin{array}{c|c|c}
(X_{i+1},Y_{i+1})
& |r_{0,X_{i+1}}-r_{1,Y_{i+1}}|
& \mathbb P(D_i'=0)
\\ \hline
(0,0) & c-a & 1-c+a=q\\
(1,1) & b & 1-b\\
(0,1) & a & 1-a\\
(1,0) & c-b & 1-c+b
\end{array}
\]

The differences of the last column from `q` are respectively

\[
0,
\qquad
c-a-b,
\qquad
c-2a,
\qquad
b-a.
\]

All are nonnegative in the residual chamber. Indeed `c>=a+b`, `b>a`, and hence

\[
c-2a=(c-a-b)+(b-a)>0.
\]

For orientation `(1,0)` the same four numbers occur in permuted order. This proves the claim. `square`

This lemma is useful beyond the present two-generation calculation: coalescence of a disagreement is never slower than rate `q`, even inside a live disagreement cluster.

## 3. A stopping-time race lemma

Let site `i` disagree at a stopping time, and let `R_{i-1}` be the first subsequent ring of the independent rate-one clock at site `i-1`. Let `T_i` be the first subsequent coalescence time of site `i`.

By Lemma 2.1, conditional on every intervening evolution,

\[
\mathbb P(T_i>t\mid\text{history up to the stopping time and no ring of }i-1)
\le e^{-qt}.
\]

Since `R_{i-1}` is an independent `Exp(1)` time,

\[
\begin{aligned}
\mathbb P(T_i<R_{i-1}\mid\mathcal F)
&\ge
\int_0^\infty (1-e^{-qt})e^{-t}\,dt\\
&=
\frac q{1+q}.
\end{aligned}
\]

Thus

\[
\boxed{
\mathbb P(T_i<R_{i-1}\mid\mathcal F)
\ge p,
\qquad
p:=\frac q{1+q}.
}
\tag{3.1}
\]

This argument allows all other clocks and all right-hand pair states to evolve. Equivalently one may obtain (3.1) by predictable thinning of the coalescence events to a constant rate-`q` subprocess and racing it against the independent left clock.

## 4. Exact two-generation regeneration bound

At a stopping time suppose:

- `j` is the rightmost disagreement;
- its first child at `j-1` has just been created;
- `j-2` is still agreed;
- the half-line strictly right of `j` is coupled, hence remains coupled forever.

Define

\[
\sigma_2
=
\inf\{t:\ D_{j-2}(t)=1\},
\]

and

\[
\tau_2
=
\inf\{t:\ D_j(t)=D_{j-1}(t)=0\}.
\]

Once `tau_2` occurs, the entire half-line from `j-1` to the right is permanently coupled.

### Proposition 4.1

For every such post-first-child state and every strict residual parameter point,

\[
\boxed{
\mathbb P(\tau_2<\sigma_2\mid\mathcal F)
\ge p^2
=
\left(\frac{1-c+a}{2-c+a}\right)^2.
}
\tag{4.1}
\]

### Proof

**Stage 1.** Apply (3.1) to the child `j-1` and the grandchild-site clock at `j-2`. With conditional probability at least `p`, the child coalesces before `j-2` rings.

On this event no grandchild can have been created. The parent `j` may have updated arbitrarily many times and may already have coalesced; this only helps.

**Stage 2.** At the child-coalescence stopping time, if the parent is already coupled then `tau_2` has occurred. Otherwise `j` still disagrees while `j-1` is agreed. Apply (3.1) again, now to the parent `j` and the next clock ring of `j-1`. With conditional probability at least `p`, the parent coalesces before the child site rings again.

On the intersection of the two stage events:

1. `j-2` never rings while `j-1` disagrees, so `sigma_2` does not occur;
2. after `j-1` coalesces, its clock does not ring again before the parent dies, so the child cannot be reinfected;
3. after the parent coalesces, all sites from `j-1` rightward are coupled permanently.

Strong Markov at the first coalescence time gives the product lower bound `p^2`. `square`

### Remark 4.2: reinfection is included rather than assumed away

The full episode outside the successful event contains arbitrary child deaths, parent survival, child reinfections, orientation changes, and right-environment evolution. Proposition 4.1 does not modify those trajectories. It identifies an explicit positive-probability subset of the genuine episode on which elimination occurs before any reinfection capable of continuing the episode.

Thus this is not the prohibited approximation "assume the child cannot be reinfected."

## 5. Combining with the first-generation bound

Let `delta_1` be Meeting 003's rightmost-source childless gap

\[
\delta_1
=
\frac{q(d+2q)}{(b+q)(1+q)-a(1-c)},
\qquad d=b-a.
\]

Starting from one rightmost source with the next two sites to its left agreed, reaching the second site to the left requires:

1. creation of the first child before source death;
2. after that child is born, creation of the grandchild before two-generation elimination.

Therefore

\[
\boxed{
\mathbb P(\text{the source episode reaches distance two to the left}\mid\mathcal F)
\le
(1-\delta_1)(1-\delta_2),
}
\tag{5.1}
\]

where

\[
\delta_2=p^2.
\]

This is a true two-generation live-episode contraction. It is stronger than multiplying the one-source factor blindly because the second factor is proved on the correct post-birth state and includes reinfection in the episode definition.

It is still not a renewal theorem, because on the complementary event the grandchild is born while older ancestors may remain alive.

## 6. Exact finite-state formulation of the complete two-generation episode

For the near-East diagnostic I also solved the entire local episode, rather than only the clearing subevent.

Before grandchild creation, represent the local coupled state by

\[
S=(G,C,P),
\]

where

- `G` is the pair state at `j-2` and lies in `{00,11}`;
- `C` is the child pair at `j-1` and lies in `{00,11,01,10}`;
- `P` is the parent pair at `j` and lies in the same four-state set.

States with both `C` and `P` agreed are absorbing success. An update of `G` that makes it off-diagonal is absorbing failure. Removing these absorbing states leaves exactly

\[
2\cdot4\cdot4-2\cdot2\cdot2=24
\]

transient states.

The right half-line is coupled, so at the parent site the only external variable is the common right-neighbour spin

\[
z(t)\in\{0,1\}.
\]

For a prescribed common right-boundary path this is an ordinary finite time-inhomogeneous CTMC. To obtain a robust bound uniform over all actual common right environments, I enlarge the class and allow `z` to be chosen at each parent update as a state-feedback control. This is a **stronger adversary** than the actual autonomous one-sided environment, because the true right environment cannot react to left-side randomness.

If `V(S)` denotes the controlled maximal probability of grandchild creation before elimination, it satisfies the finite HJB system

\[
\boxed{
0
=
\mathcal L_GV(S)
+
\mathcal L_CV(S)
+
\max_{z\in\{0,1\}}\mathcal L_P^{(z)}V(S),
}
\tag{6.1}
\]

with boundary values `V=1` at grandchild creation and `V=0` when child and parent are both agreed.

Because the control class contains every actual right-boundary trajectory,

\[
\mathbb P(\sigma_2<\tau_2\mid\text{any actual right environment})
\le V(S).
\tag{6.2}
\]

Proposition 4.1 already proves `V(S)<=1-p^2<1` for every strict residual point. The HJB is used below only to resolve the structured near-East asymptotic more sharply.

## 7. Structured zero-born child near the East boundary

Take the genuine residual path

\[
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
\qquad
\varepsilon\downarrow0.
\tag{7.1}
\]

Suppose the first child was born from an agreed zero and inherited the parent's orientation. By symmetry take

\[
C=P=01.
\]

First take the grandchild site also agreed zero:

\[
S_0=(00,01,01).
\tag{7.2}
\]

### 7.1 Fixed common right boundary: the fast child kill really compensates

If the common right boundary of the parent is fixed to zero, exact solution of the 24-state hitting system gives

\[
\boxed{
V_0(S_0)
=
\frac35
-\frac{24}{25}\varepsilon
+\frac{1349}{250}\varepsilon^2
+O(\varepsilon^3).
}
\tag{7.3}
\]

Thus the grandchild probability tends to `3/5`, not to one.

If the common right boundary is fixed to one,

\[
\boxed{
V_1(S_0)
=
\frac13
+\frac29\varepsilon
+\frac{11}{54}\varepsilon^2
+O(\varepsilon^3).
}
\tag{7.4}
\]

Thus under either constant boundary the post-birth killing mechanism compensates for the slow parent death strongly enough to leave a nontrivial limiting regeneration probability.

These two fixed-boundary calculations are diagnostics only; they are not used as the live-environment theorem.

### 7.2 Robust adaptive-control envelope

For the stronger state-feedback control of Section 6, the maximizing policy for every sufficiently small positive `epsilon` is:

- choose `z=1` exactly when the child disagrees and the parent is either common `1` or has the same disagreement orientation as the child;
- choose `z=0` in the other transient states.

The verifier solves the resulting symbolic 24-state system and checks every HJB action inequality by its first nonzero Taylor coefficient. Since there are finitely many states and every action advantage is rational and analytic at `epsilon=0`, these strict leading signs certify the policy for all sufficiently small positive `epsilon`.

For `S_0`,

\[
\boxed{
V_*(S_0)
=
1-\frac92\varepsilon
+\frac{135}{4}\varepsilon^2
-\frac{3233}{12}\varepsilon^3
+O(\varepsilon^4).
}
\tag{7.5}
\]

Hence, uniformly even against this stronger adaptive environment,

\[
\boxed{
\mathbb P(\tau_2<\sigma_2\mid S_0)
\ge
\frac92\varepsilon+O(\varepsilon^2).
}
\tag{7.6}
\]

This is much larger than the crude universal bound

\[
\delta_2
=
\left(\frac{2\varepsilon^2}{1+2\varepsilon^2}\right)^2
=4\varepsilon^4+O(\varepsilon^6).
\]

The fast post-birth child killing therefore provides a real compensation mechanism.

However, the robust gap still tends to zero. The structured two-generation problem is better scaled than the worst first-generation bound, but it is not residual-uniform near the East boundary.

### 7.3 A further state variable matters

The state `S_0` also assumed the grandchild site was agreed zero. If instead

\[
S_1=(11,01,01),
\]

the same controlled HJB gives

\[
\boxed{
V_*(S_1)
=
1-\varepsilon
+\frac{11}{24}\varepsilon^2
+O(\varepsilon^3).
}
\tag{7.7}
\]

Thus the common spin at the prospective grandchild site changes the leading regeneration gap from `(9/2) epsilon` to `epsilon` in the robust controlled calculation.

So the phrase "zero-born child" does not specify the full two-generation state. The common grandchild-site spin and the common right-boundary trajectory are genuine state variables. Proposition 4.1 is uniform over them; sharper near-East estimates are not.

## 8. Why the near-East result is not a route failure

Meeting 003 correctly ruled that degeneration at the excluded boundary is not by itself a contradiction.

The new calculation changes the picture in two ways:

1. the favorable structured fixed-boundary episode has a nontrivial limit strictly below one (`3/5` or `1/3` depending on boundary);
2. even the stronger adaptive-control envelope has a positive parameter-point gap, of order `epsilon` in the structured states above.

Thus the post-birth killing mechanism is quantitatively real. What degenerates is the **uniformity over the East closure**, not the existence of two-generation regeneration at strict positive rates.

## 9. Composition test: finite-depth ordered clearing

The two-generation regeneration has an exact finite-depth extension.

Suppose a finite disagreement episode has a coupled right tail and at most `m` disagreement sites in the finite active span, while the site immediately to the left of the leftmost disagreement is agreed.

Order the live disagreement sites from left to right. Clear them successively. At each stage require that the current leftmost disagreement coalesces before the next clock ring at the agreed site immediately to its left. By (3.1), conditional on all previous stages, this has probability at least `p=q/(1+q)`.

Other sites may update arbitrarily. If there is a gap of agreed sites between live disagreements, it only helps. After the last disagreement clears, the coupled right tail makes the cleared region permanent.

Therefore:

### Proposition 9.1 (finite-depth ordered clearing)

For every finite live episode with at most `m` active disagreement sites and coupled right tail,

\[
\boxed{
\mathbb P(\text{complete elimination before the next leftward creation}\mid\mathcal F)
\ge
p^m,
\qquad
p=\frac q{1+q}.
}
\tag{9.1}
\]

For `m=2`, this is Proposition 4.1.

This tests the next composition step rather than stopping at two generations. It shows that a three-generation episode also has a positive clearing probability `p^3`, and similarly at every fixed depth.

## 10. Why Proposition 9.1 still does not close spatial iteration

The restart after **successful** clearing is perfect: the whole source episode is gone and the coupled half-line is permanent.

The problem is the failure state. If a grandchild is born before two-generation elimination, the active ancestry depth can increase. The next failure may increase it again. No fixed finite family of two-generation states contains all such failure states.

The guaranteed clearing probability in Proposition 9.1 decays as

\[
p^m.
\]

If one tries to bound successive leftward advances using only this estimate, the corresponding failure factors are

\[
1-p,
\quad
1-p^2,
\quad
1-p^3,
\quad\ldots
\]

and

\[
\sum_{m\ge1}p^m<\infty.
\]

Consequently

\[
\prod_{m\ge1}(1-p^m)>0.
\]

So these certified finite-depth clearing gaps are **summable** in the depth and do not force the probability of indefinite leftward propagation to vanish.

This is the precise composition obstruction after Assignment 004. It is not a counterexample to the live-episode route: the true clearing probabilities may be much larger than `p^m`, as the structured near-East 24-state calculation already demonstrates at depth two. But the presently proved restart mechanism is not a finite-state spatial contraction theorem.

The next useful theorem must therefore do one of the following:

- find a regeneration probability that does not decay summably with active ancestry depth;
- prove a Lyapunov drift for a weighted disagreement stack;
- control the high-risk `J_i` occupation conditionally on the disagreement ancestry;
- identify a finite summary state whose transition kernel dominates all deeper ancestry configurations.

Simply multiplying the two-generation number is not legitimate.

## 11. Verification

The supporting file

`students/student-f/004-two-generation-verifier.py`

contains no simulation. It uses exact symbolic linear algebra to check:

1. the four local coalescence probabilities and the general lower bound `q`;
2. the universal two-generation gap
   \[
   \left(\frac{1-c+a}{2-c+a}\right)^2;
   \]
3. the complete 24-state common-uniform CTMC on the near-East path;
4. the fixed-boundary expansions (7.3)--(7.4);
5. the adaptive HJB policy and every local action inequality for sufficiently small positive `epsilon`;
6. the controlled expansions (7.5) and (7.7).

The exact verifier commit is `5e3c4bc`.

## 12. Research delta / anti-circularity

### Previous live statement

Meeting 003 left the finite question whether child killing and reinfection can be controlled after the first child is born, or whether the live-source contraction collapses immediately at two generations.

### New theorem

Proposition 4.1 gives a parameter-point positive two-generation regeneration probability under the true coupling, uniform over the complete right environment and all post-first-child local states.

### New structural lemma

Lemma 2.1 shows every disagreement, including non-rightmost descendants, has coalescence intensity at least `q`. This is stronger than the rightmost-source death estimate and is the reason the two-generation race can be restarted after child birth.

### Near-East resolution

The exact structured CTMC verifies the Professor's proposed compensation mechanism: under constant right environments the grandchild probability has a nontrivial limit below one, while the stronger adaptive-control gap is order `epsilon`. The episode depends on further local/environment variables; it is not determined by the phrase "zero-born child" alone.

### Remaining blocker

A grandchild failure creates a deeper ancestry stack rather than returning to the two-generation restart state. The available finite-depth clearing probability `p^m` decays summably in the depth, so it does not by itself yield extinction of the disagreement front.

## Handoff

`two-generation contraction proved but composition remains at: every disagreement under the common-uniform coupling has coalescence intensity at least q=1-c+a, which gives the exact environment-uniform regeneration bound P(tau_2<sigma_2)>=((1-c+a)/(2-c+a))^2 after the first child, with all reinfections retained in the episode; the exact 24-state near-East controlled chain confirms a stronger structured gap of order epsilon, but after grandchild creation the active ancestry depth grows, and the currently certified depth-m clearing probability (q/(1+q))^m is summable in m, so no finite-state or depth-uniform spatial renewal closure has yet been proved.`