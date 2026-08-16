# Student G 003: restart-count corrector for the trail mass/disagreement block

## Verdict

The restart-count block can be completed on the coupling side.

The single-exposure bound from Assignment 002 can be summed over **arbitrarily many re-entries of the same exposed parent level**. If

$$
h:=h_1<1
$$

is the Professor-checked worst-case child-before-parent-coalescence probability for one exposure, then the number `N` of exposure entries of that parent before its first coalescence satisfies

$$
\boxed{
\mathbb P(N\ge n\mid\mathcal F)\le h^{n-1},\qquad n\ge1.
}
$$

Hence, for

$$
1\le s<h^{-1},
$$

the complete same-parent restart bundle has the explicit probability-generating bound

$$
\boxed{
\mathbb E[s^N\mid\mathcal F]
\le
M(s):=
\frac{(1-h)s}{1-hs}.
}
\tag{R}
$$

This is the first part of the bridge: deaths and reinfections at one exposed edge can be integrated out into a finite multiplicative corrector. They do not require an unbounded restart state.

The deeper reinfections which occur **after the parent itself has coalesced** are genuinely new ancestry and are exactly the phenomenon recorded by the principal's unresolved stack height `H`. Combining `(R)` with the accepted stack-clearing tail from E7 gives a joint Foster--Lyapunov estimate for stack height and restart count.

Put

$$
B=b+c-a,
\qquad
\omega=1-c+a,
$$

and

$$
\alpha=
\frac{B+\omega}{B+2\omega}.
$$

E7 gives a clearing variable `K` whose conditional tail dominates

$$
\mathbb P(K\ge j\mid\mathcal F)
\ge
\alpha 2^{-(j-1)},
\qquad j\ge1,
\tag{K}
$$

and one transfer adds at most one unresolved level:

$$
H'\le(H-K)_++1.
\tag{H}
$$

For

$$
1<\lambda<\lambda_*:=\frac{B+2\omega}{2\omega},
$$

define

$$
\phi(\lambda)
=
\lambda\left(
1-\alpha+
\frac{\alpha}{2\lambda-1}
\right).
$$

Then

$$
\boxed{\phi(\lambda)<1.}
$$

Choose additionally

$$
1<s<
\frac{1}{h+(1-h)\phi(\lambda)}.
\tag{A}
$$

This interval is nonempty because `h<1` and `phi(lambda)<1`. With

$$
\chi:=M(s)\phi(\lambda)<1,
$$

there are explicit finite `H_0=H_0(a,b,c,lambda,s)` and `theta<1` such that the restart-corrected disagreement stack satisfies, whenever `H>=H_0`,

$$
\boxed{
\mathbb E\left[
 s^{\Delta R}\,\mathcal V_s(\Sigma')
 \mid\mathcal F
\right]
\le
\theta\,\mathcal V_s(\Sigma).
}
\tag{FL}
$$

Here `Delta R` is the number of newly realized exposure re-entries during the transfer, `Sigma` is the unresolved coupled-stack state, and

$$
\mathcal V_s(\Sigma)
=\lambda^{H(\Sigma)}\mathcal C_s(\Sigma)
$$

is a finite-phase restart corrector. Each unresolved level contributes a local remaining-restart factor between `1` and `M(s)`; the product of these factors is `C_s`. The local factors are chosen from the two-state exposure renewal equation below, so already-existing same-parent restarts have nonpositive corrected drift. Creating the at-most-one genuinely new unresolved level costs at most `M(s)`, while each certified stack removal releases a factor at least `lambda`.

Consequently the coupling-side state can be reduced to **bounded stack height plus finitely many local exposure phases**. Moreover the number of restart entries accumulated before a genuine clearance of the inherited stack has an exponential moment at every strict residual parameter point.

This does **not** prove the complete mass/disagreement block contraction. The remaining finite problem is the bounded-height signed branching kernel created by

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f).
\tag{MD}
$$

Assignment 003 therefore supplies the missing coupling-side bridge promised at Meeting 007: restart count is no longer an unbounded variable. Student F's block calculation can work with a finite bounded-height mass/disagreement kernel, while `(FL)` controls every excursion outside that finite set.

Near East this remains genuinely contractive. Along

$$
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2,
$$

one may take `lambda=2` and

$$
s=1+\frac{\varepsilon^2}{4}.
$$

Then

$$
M(s)\phi(2)\longrightarrow\frac{16}{21}<1.
$$

Thus the restart correction survives precisely in the hard regime where the crude global `J_i` occupation substitution lost all damping. The admissible exponential tilt has scale `log s = Theta(epsilon^2)`, which is the natural scale of the local coalescence gap.

A symbolic verifier is committed beside this report as

`students/student-g/003-restart-count-verifier.py`.

## 1. Inputs used from the current spine

Work throughout in the residual chamber

$$
0<a<b,
\qquad
\frac12\le c<1,
\qquad
c\ge a+b,
\qquad
b\ge\sqrt2(1-c).
$$

Set

$$
d=b-a,
\qquad
\omega=1-c+a,
\qquad
B=b+c-a.
$$

I use two Professor-checked inputs.

### 1.1 Single live exposure

At a stopping time with

$$
D_i=0,
\qquad
D_{i+1}=1,
$$

stop when either site `i` becomes a disagreement or site `i+1` coalesces. Assignment 002 and Meeting 007 give

$$
\mathbb P(\text{child before right coalescence}\mid\mathcal F)
\le h_x,
$$

where

$$
h_0
=\frac{d(1+\omega)+ac}{\mathfrak D},
$$

$$
h_1
=\frac{c(b+\omega)+(1-c)d}{\mathfrak D},
$$

and

$$
\mathfrak D
=(b+\omega)(1+\omega)-a(1-c).
$$

Moreover

$$
0<h_0<h_1<1.
\tag{1.1}
$$

This estimate is uniform over disagreement orientation and arbitrary deeper ancestry.

### 1.2 Stack clearing

For the trail-generated conditional-law disagreement stack, E7 gives a random number `K` of consecutive unresolved levels removed in one zero-boundary transfer segment satisfying `(K)`, and `(H)`.

The point of this report is to combine these two inputs without replacing restart count by raw disagreement occupation.

## 2. Same-parent re-entry count is geometric

Fix an exposed edge `(i,i+1)` at a stopping time. Call the disagreement at `i+1` the **parent**. Let `S_1` be the present exposure entry. If the exposure ends by parent coalescence, stop. If it ends by child creation at `i`, wait until either

- the parent coalesces, in which case stop; or
- site `i` becomes agreed again while the parent is still alive, in which case the same edge re-enters exposure and define this time to be `S_2`.

Continue recursively. Let `N` be the number of such entries before the first parent coalescence.

This definition includes arbitrary child deaths and reinfections while the same parent remains alive. If the parent coalesces and is later reinfected from still deeper ancestry, that later disagreement is a **new parent episode**. It belongs to the unresolved-height dynamics and is not hidden inside the same-parent count `N`.

### Proposition 2.1 (restart-bundle tail)

At every parent episode start,

$$
\boxed{
\mathbb P(N\ge n\mid\mathcal F_{S_1})
\le h_1^{n-1},
\qquad n\ge1.
}
\tag{2.1}
$$

#### Proof

For `N>=n+1`, the `n`th exposure must end in child creation before parent coalescence, and the process must later return to another exposure with that parent still alive. Conditional at `S_n`, Meeting 007 bounds the first of these events by `h_{X_i(S_n)}<=h_1`. The additional requirement that the child subsequently disappear before the parent only decreases the probability.

Therefore

$$
\mathbb P(N\ge n+1\mid\mathcal F_{S_n},N\ge n)
\le h_1.
$$

Iteration by the strong Markov property proves (2.1). `square`

For `1<=s<h_1^{-1}`, the tail-sum identity gives

$$
\begin{aligned}
\mathbb E[s^N]
&=1+(s-1)\sum_{n\ge1}s^{n-1}\mathbb P(N\ge n)\\
&\le
1+(s-1)\sum_{n\ge1}(s h_1)^{n-1}\\
&=
\boxed{\frac{(1-h_1)s}{1-h_1s}}.
\end{aligned}
\tag{2.2}
$$

This proves `(R)`.

The difference from Assignment 002 is substantive: (2.2) has already summed **all repeated exposure entries of one parent**, rather than controlling a single exposure and then counting re-entries crudely by coalescence events.

## 3. A finite local restart corrector

The geometric estimate can be expressed as a finite phase corrector, which is the form useful for block composition.

Let

$$
M=M(s)=\frac{(1-h_1)s}{1-h_1s}.
$$

At an exposure entry with common spin `x`, pessimistically assume that every child-first outcome eventually returns to a new exposure while the same parent survives. If the future corrected value at any such return is bounded by `M`, then the value at the present entry is at most

$$
v_x(s)
:=s\bigl[(1-h_x)+h_xM\bigr].
\tag{3.1}
$$

Since `h_x<=h_1` and `M>=1`, the right side is increasing in `h_x`, and

$$
v_1(s)
=s[(1-h_1)+h_1M]
=M.
$$

Hence

$$
\boxed{1\le v_x(s)\le M(s).}
\tag{3.2}
$$

The actual child-alive interval can end by parent coalescence before re-entry, so (3.1) is indeed an upper corrector.

Thus every currently unresolved parent level needs only a finite local phase: no active exposure, exposed with common spin zero, or exposed with common spin one. Its entire future same-parent re-entry history is represented by a factor in `[1,M(s)]`.

For a stack state `Sigma`, let

$$
\mathcal C_s(\Sigma)
$$

be the product of these remaining-restart factors over its unresolved levels, taking factor one for levels not currently carrying an exposed parent phase. Define

$$
\boxed{
\mathcal V_s(\Sigma)
:=\lambda^{H(\Sigma)}\mathcal C_s(\Sigma).
}
\tag{3.3}
$$

Evolution internal to an already existing parent level, including arbitrary exposure re-entry, has nonpositive corrected drift by (3.1). The only positive bookkeeping cost not prepaid in `C_s` is the creation of a genuinely new unresolved level. Because one trail transfer adds at most one level, that cost is at most `M(s)`.

When a certified clearing removes a level, its height factor `lambda` disappears and its local corrector factor is at least one, so ignoring removal of the local factor is conservative.

## 4. Explicit exponential height drift from E7

The E7 tail bound is equivalent to stochastic domination by an integer random variable `kappa` with

$$
\mathbb P(\kappa=0)=1-\alpha,
$$

and

$$
\mathbb P(\kappa=j)=\alpha 2^{-j},
\qquad j\ge1,
\tag{4.1}
$$

where

$$
\alpha=\frac{B+\omega}{B+2\omega}>\frac12.
\tag{4.2}
$$

Indeed

$$
\mathbb P(\kappa\ge j)
=\alpha 2^{-(j-1)}.
$$

For `lambda>1`,

$$
\mathbb E[\lambda^{-\kappa}]
=1-\alpha+\frac{\alpha}{2\lambda-1}.
$$

Hence define

$$
\boxed{
\phi(\lambda)
=\lambda\mathbb E[\lambda^{-\kappa}]
=\lambda\left(
1-\alpha+\frac{\alpha}{2\lambda-1}
\right).
}
\tag{4.3}
$$

A direct simplification gives

$$
\phi(\lambda)-1
=
\frac{(\lambda-1)(-B+2\lambda\omega-2\omega)}
{(B+2\omega)(2\lambda-1)}.
\tag{4.4}
$$

Therefore

$$
\boxed{
1<\lambda<\lambda_*
:=\frac{B+2\omega}{2\omega}
\quad\Longrightarrow\quad
\phi(\lambda)<1.
}
\tag{4.5}
$$

This is an explicit exponential version of the negative first-moment drift in E7.

## 5. Joint stack/restart Foster inequality

Fix `lambda` satisfying (4.5). Since `M(1)=1`, continuity gives restart tilts `s>1` for which the restart cost does not destroy the height contraction. In fact the admissible interval is explicit.

From (2.2),

$$
M(s)\phi(\lambda)<1
$$

is equivalent to

$$
\boxed{
1<s<
\frac1{h_1+(1-h_1)\phi(\lambda)}.
}
\tag{5.1}
$$

Put

$$
\chi=M(s)\phi(\lambda)<1.
\tag{5.2}
$$

For finite height, clearing is truncated at `H`. Since `K` stochastically dominates `kappa`,

$$
\begin{aligned}
\lambda\,
\mathbb E[\lambda^{-\min(K,H)}\mid\mathcal F]
&\le
\lambda\,
\mathbb E[\lambda^{-\min(\kappa,H)}]\\
&\le
\phi(\lambda)
+2\alpha\lambda(2\lambda)^{-H}.
\end{aligned}
\tag{5.3}
$$

The last term is simply the tail correction on `{kappa>=H}`.

The restart corrector in Section 3 costs at most one factor `M(s)` for the at-most-one newly created level. Existing same-parent re-entries have already been prepaid and removed levels only help. Consequently

$$
\boxed{
\frac{
\mathbb E[s^{\Delta R}\mathcal V_s(\Sigma')\mid\mathcal F]
}{\mathcal V_s(\Sigma)}
\le
M(s)
\left[
\phi(\lambda)
+2\alpha\lambda(2\lambda)^{-H}
\right].
}
\tag{5.4}
$$

Choose

$$
H_0
\ge
\frac{
\log\left(4\alpha\lambda M(s)/(1-\chi)\right)
}{\log(2\lambda)}
\tag{5.5}
$$

and put

$$
\theta=\frac{1+\chi}{2}<1.
\tag{5.6}
$$

Then for every `H>=H_0`, (5.4) gives `(FL)`.

### Proposition 5.1 (restart-corrected stack drift)

For every strict residual parameter point there exist

$$
\lambda>1,
\qquad s>1,
\qquad H_0<\infty,
\qquad\theta<1
$$

such that the trail-generated conditional-law disagreement stack has strict multiplicative drift outside `{H<H_0}` after **all same-parent exposure re-entries are included**.

This is an all-depth statement. No fixed ancestry depth appears in the theorem.

## 6. Exponential restart moment up to genuine stack regeneration

A genuine regeneration of the inherited disagreement stack occurs on a transfer for which all incoming unresolved levels are removed before the possible new insertion, i.e. `K>=H`. On the bounded set

$$
\mathcal S_0=\{H\le H_0\},
$$

E7 gives the uniform minorization

$$
\boxed{
\mathbb P(K\ge H\mid\mathcal F)
\ge
p_0:=\alpha 2^{-(H_0-1)}>0.
}
\tag{6.1}
$$

Proposition 5.1 gives an exponential restart-weighted return to `S_0`. Inside `S_0` there are only finitely many height/exposure phases, and every local restart bundle has finite pgf for `s<h_1^{-1}`. Therefore, after possibly reducing `s>1`, the standard small-set renewal argument applies:

- excursions from `S_0` have uniformly finite restart exponential moment by `(FL)`;
- each return to `S_0` has probability at least `p_0` of clearing the entire inherited stack on the next transfer;
- the number of failed visits before regeneration is geometrically dominated;
- the weighted failed-cycle kernel is strictly below one for `s>1` sufficiently close to one, by continuity from its value `1-p_0<1` at `s=1`.

Hence:

### Corollary 6.1 (restart-count exponential moment)

Let `R_reg` be the total number of exposure entries accumulated from a trail-generated disagreement stack until the first genuine regeneration of its inherited levels. There exist

$$
\widehat s>1,
\qquad C<\infty
$$

depending only on `(a,b,c)` such that

$$
\boxed{
\mathbb E_{\Sigma}[\widehat s^{R_{\rm reg}}]
\le
C\,\mathcal V_s(\Sigma).
}
\tag{6.2}
$$

uniformly over ancestry depth and the exterior environment allowed by the trail coupling.

The constant and exponential tilt may deteriorate at the excluded East boundary. Strict positivity of the rates is enough for `widehat s>1` at every live parameter point.

This is the requested restart-count theorem: repeated deaths and reinfections have an exponential tail once they are charged through the finite local corrector and the all-depth stack drift.

## 7. Near-East stress test

Take

$$
a=\varepsilon^2,
\qquad
b=\varepsilon,
\qquad
c=1-\varepsilon^2.
$$

Then

$$
B=1+\varepsilon-2\varepsilon^2,
\qquad
\omega=2\varepsilon^2,
$$

and

$$
\alpha
=1-2\varepsilon^2+2\varepsilon^3+O(\varepsilon^4).
\tag{7.1}
$$

The worst one-exposure child probability is

$$
h_1
=1-2\varepsilon^2-2\varepsilon^3+O(\varepsilon^4).
\tag{7.2}
$$

For all sufficiently small positive `epsilon`, `lambda=2` lies in the interval (4.5), and

$$
\phi(2)
=\frac23+\frac83\varepsilon^2+O(\varepsilon^3).
\tag{7.3}
$$

Choose

$$
s=1+\frac{\varepsilon^2}{4}.
\tag{7.4}
$$

Then

$$
M(s)
=\frac87-\frac8{49}\varepsilon+O(\varepsilon^2),
\tag{7.5}
$$

and therefore

$$
\boxed{
M(s)\phi(2)
=\frac{16}{21}
-\frac{16}{147}\varepsilon
+O(\varepsilon^2)
<1
}
\tag{7.6}
$$

for sufficiently small positive `epsilon`.

This matters because Assignment 002's crude all-time substitution gave

$$
\omega-(c-d)g_1=-1+O(\varepsilon),
$$

which lost all damping. The restart-corrected norm has a strict large-height factor tending instead to `16/21`.

The price is that

$$
\log s\sim\frac{\varepsilon^2}{4},
$$

so the controlled exponential moment is on the natural `omega` scale. No uniform East-boundary constant is claimed.

## 8. Interface with the mass/disagreement decomposition

The active centered insertion identity is

$$
g\,\mu(h_{p_*}(\eta_y)f)
=(Br-c)\bar\mu(f)
+Br(1-r)(\mu^1-\mu^0)(f).
$$

For the disagreement channel, couple `mu^1` and `mu^0` by the reset/live coupling used in E7--E8 and measure the resulting unresolved state by the functional `V_s` above. Proposition 5.1 says:

> outside the finite set `H<H_0`, the complete coupling evolution, including arbitrary same-parent exposure restarts, has strict multiplicative drift.

Therefore the infinite-dimensional restart bookkeeping can be removed from the remaining block theorem. It suffices to retain:

1. the signed mass coefficient `Br-c`;
2. the disagreement coefficient `Br(1-r)`;
3. stack heights `0,...,H_0`;
4. the finite local exposure phases from Section 3.

Everything outside this finite state set is returned with a strict factor `theta<1`.

This is complementary to Student F Assignment 007. It does **not** assert that the finite bounded-height mass/disagreement kernel has spectral radius below one; that is still the load-bearing signed-branching calculation. But it shows that repeated exposure re-entry cannot by itself create an unbounded state variable or destroy the all-depth reduction.

If that bounded kernel has a block spectral radius `<1`, then combining it with `(FL)` gives the full block norm required in E10. Iteration then implies decay of the right-weighted invariant trail quantity `J_{x,r}` exactly as in Meeting 006. The no-exit complementary term must still be included when the final trail decomposition is turned into ergodicity.

## 9. What this does and does not settle

### Proved here

- arbitrary same-parent exposure re-entry count has geometric tail (2.1);
- it has explicit exponential pgf (2.2);
- the restart history can be compressed into a finite phase corrector (3.1)--(3.3);
- the E7 stack drift upgrades to the restart-corrected Foster inequality (5.4);
- restart count up to genuine inherited-stack regeneration has an exponential moment (6.2);
- near East the combined large-height multiplier can be chosen to tend to `16/21<1`.

### Not proved here

- the complete signed mass/disagreement block kernel has spectral radius `<1`;
- `J_{x,r}->0` without that bounded-height mass calculation;
- the final ergodicity implication including the no-exit term.

Thus the coupling-side restart bottleneck from Meeting 007 is closed, but E10 as a whole remains open.

## Handoff

`restart-count block bridge proved: repeated exposure re-entries of one parent have geometric tail h_1^{n-1} and explicit pgf M(s); combining the resulting finite restart corrector with the principal E7 clearing tail yields a Foster--Lyapunov function V_s for unresolved height plus restart state, with strict drift outside finite height and an exponential moment for total restart count up to genuine inherited-stack regeneration. Near East one may take lambda=2 and s=1+epsilon^2/4, giving restart-corrected large-height factor ->16/21. The remaining block problem is finite: prove spectral radius <1 for the bounded-height signed mass/disagreement kernel and then insert it into J_{x,r}->0 and the full trail/no-exit decomposition.`