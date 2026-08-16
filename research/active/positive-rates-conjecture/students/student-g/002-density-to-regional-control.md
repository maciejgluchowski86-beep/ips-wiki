# Student G 002: weighted regional control, composition failure, and a live-edge $J_i$ occupation bound

## Verdict

Assignment 002 can be completed, but not with a positive scaffold-composition theorem.

I independently rederived the exact minimal regional kernel. The one-cell regional insertion is nonnegative, but the first genuine composition step has the signed transfer

$$
\Psi_\Delta(z)=B K_\Delta(z)-c,
\qquad
B=b+c-a,
$$

and

$$
\Psi_\Delta(0)<0
$$

for every sufficiently short positive cell at every residual parameter point. Since the same transfer is positive for sufficiently long cells, two consecutive hidden cells can have negative product. Thus the cellwise last-exit/scaffold route cannot be repaired by strengthening the one-time density estimate. This agrees with Student F's independently obtained Assignment 002 conclusion and is now a closed route in the proof spine.

There is, however, a reusable weighted estimate that interfaces directly with the current live-disagreement programme. Combining the exact two-state calculation behind Assignment 002 with Meeting 004's new fact that **every** disagreement has coalescence intensity at least

$$
q:=1-c+a,
$$

gives an exposure-edge theorem for the high-risk coupling state

$$
J_i
=1_{\{D_i=0,D_{i+1}=1,X_i=Y_i=1\}}.
$$

Whenever site $i$ is agreed and $i+1$ disagrees, stop when either $i$ becomes a disagreement or $i+1$ coalesces. On that whole exposure interval the dangerous $J_i$ occupation has an explicit killed-chain resolvent. In particular, if the common spin at $i$ is initially $x\in\{0,1\}$, then

$$
\mathbb E\int J_i(s)\,ds
\le g_x,
$$

where

$$
g_0=\frac{a}{\mathfrak D},
\qquad
g_1=\frac{b+q}{\mathfrak D},
\qquad
\mathfrak D=(b+q)(1+q)-a(1-c).
$$

Moreover the exact infection compensator on the exposure interval is

$$
\boxed{
\mathbb P(\text{left child before right coalescence}\mid\mathcal F)
=
\mathbb E\int \bigl[(b-a)+(c-b+a)J_i(s)\bigr]\,ds.
}
$$

The left side is at most the explicit $h_x$ from the killed two-state chain, with

$$
h_0=\frac{(b-a)(1+q)+ac}{\mathfrak D},
$$

$$
h_1=\frac{c(b+q)+(1-c)(b-a)}{\mathfrak D}<1.
$$

Meeting 003 proved these $h_x$ for a rightmost source. The new point here is that Meeting 004 removes the rightmost hypothesis, so the same weighted exposure estimate holds for **every** edge with an agreed site immediately to the left of a live disagreement, including inside an arbitrary-depth ancestry stack.

This does not by itself prove all-depth contraction: repeated deaths and reinfections can create arbitrarily many exposure intervals. I give an explicit all-time bound in terms of the number of exposure entries, and show exactly why replacing that entry count by crude disagreement occupation loses the near-East gain.

Supporting exact symbolic checks are in

`students/student-g/002-regional-moment-verifier.py`.

## 1. Conventions

On the normalized face

$$
r_{00}=a,
\qquad r_{01}=b,
\qquad r_{10}=c,
\qquad r_{11}=0,
$$

work in the residual chamber

$$
0<a<b,
\qquad \frac12\le c<1,
\qquad c\ge a+b,
\qquad b\ge\sqrt2(1-c).
$$

For the old last-exit calculation use Student F's complemented spin convention and put

$$
d:=b-a>0,
\qquad
k:=1-c>0,
\qquad
B:=c+d=b+c-a,
\qquad
\rho:=\frac cB.
\tag{1.1}
$$

The noise-reduced process $L^-$ then has local rates

$$
0\to1\text{ at rate }1-c\eta_{i+1},
\qquad
1\to0\text{ at rate }d(1-\eta_{i+1}).
\tag{1.2}
$$

At a hidden successful dual interaction the signed source factor is

$$
B\eta_i-c=B(\eta_i-\rho).
\tag{1.3}
$$

For the live-coupling calculation below I return to the original normalized spins $X,Y$ and the common-uniform coupling. Write

$$
D_i=1_{\{X_i\ne Y_i\}}.
\tag{1.4}
$$

## 2. Minimal regional cell: exact positive kernel

Consider a predecessor interaction at $i-1\to i$ followed after time $\Delta$ by the current successful interaction at $i\to i+1$. Fix the predecessor type to be source-retaining, so that a genuine left predecessor branch remains. The scaffold no-crossing condition on the left side of the forced-active tube gives canonical zero boundary at site $i$.

After all unrevealed marks in that one-site left region are integrated, the retained predecessor branch contributes

$$
K_\Delta(z)
=(P_\Delta^{-,0}\eta_{i-1})(z),
\qquad z\in\{0,1\}.
\tag{2.1}
$$

Under zero boundary, (1.2) reduces to

$$
0\xrightarrow{1}1,
\qquad
1\xrightarrow{d}0.
$$

Therefore

$$
\boxed{
K_\Delta(z)
=
\frac1{1+d}
+
\left(z-\frac1{1+d}\right)e^{-(1+d)\Delta}.
}
\tag{2.2}
$$

In particular

$$
K_\Delta(0)=\frac{1-e^{-(1+d)\Delta}}{1+d}\ge0,
$$

$$
K_\Delta(1)=\frac{1+d e^{-(1+d)\Delta}}{1+d}>0.
\tag{2.3}
$$

Thus the first regional integration does remove the raw left-spin sign problem: with the predecessor type fixed source-retaining, the left region is a nonnegative scalar factor. The current hidden interaction can then use the already proved source/right insertion estimate after its burn-in.

This independently confirms that the minimal cell itself is not the obstruction.

## 3. The actual composition step is signed and fails

At the next composition step the predecessor interaction cannot remain artificially fixed source-retaining. It is itself the hidden successful interaction of the preceding cell.

Its two hidden types have the same revealed predecessor geometry but different left continuation:

- source-retaining type: coefficient $+B$ and branch contribution $K_\Delta(z)$;
- source-removing type: coefficient $-c$ and no left branch, hence left contribution $1$.

Therefore the exact probability-weighted transfer is

$$
\boxed{
\Psi_\Delta(z)=B K_\Delta(z)-c.
}
\tag{3.1}
$$

For the worst lower spin $z=0$,

$$
\Psi_\Delta(0)
=
\frac{B}{1+d}
\left(1-e^{-(1+d)\Delta}\right)-c.
\tag{3.2}
$$

At $\Delta=0$ this equals $-c$. Its unique zero is

$$
\boxed{
\tau_*
=
\frac1{1+d}\log\frac{B}{d(1-c)}.
}
\tag{3.3}
$$

Indeed

$$
B-c(1+d)=d(1-c)>0.
$$

Hence at every strict residual parameter point

$$
\boxed{
0<\Delta<\tau_*
\quad\Longrightarrow\quad
\Psi_\Delta(0)<0.
}
\tag{3.4}
$$

On the other hand

$$
\lim_{u\to\infty}\Psi_u(0)
=
\frac{d(1-c)}{1+d}>0.
\tag{3.5}
$$

Thus one may choose a long first cell $u$ with $\Psi_u(0)>0$ and an arbitrarily nearby short next cell $\Delta<\tau_*$ with $\Psi_\Delta(0)<0$. Their two-cell transfer is strictly negative.

This is not a failure of marginal density to reach a numerical threshold. It is an **age problem**: the new hidden predecessor branch can be too young to relax past $\rho$. No amount of burn-in of an older region forces the next inter-successful-interaction gap to exceed $\tau_*$. The Poisson scaffold has positive probability of arbitrarily short gaps.

Therefore Assignment 002 has a definitive negative answer for cellwise regional composition:

$$
\boxed{
\text{one cell positive, two hidden cells not sign-preserving.}
}
\tag{3.6}
$$

The cellwise last-exit/scaffold route is correctly closed in the current proof spine.

## 4. A generic $L^-$ weighted insertion lemma that remains correct

The failed two-cell transfer should not be confused with a separate correlation estimate from my earlier partial work.

Take two consecutive canonical spins

$$
x=\eta_{i-1},\qquad y=\eta_i,
$$

with an arbitrary prescribed right-boundary path $z(t)$ for $y$. Put

$$
m=\mathbb E y,
\qquad n=\mathbb E x,
\qquad w=\mathbb E(xy),
$$

and

$$
H=w-\rho n=\mathbb E[(y-\rho)x].
$$

A direct generator calculation gives

$$
\boxed{
H'
=-(2+d-Bz)H
-\rho
+\frac dB n
+\left(1-\frac{cd}{B}\right)m.
}
\tag{4.1}
$$

Student F's one-site conditional estimate gives $m,n\ge\rho$ after

$$
T_\rho
=
\frac1{1-c}
\log\frac{B}{d(1-c)}.
\tag{4.2}
$$

At $m=n=\rho$, the non-$H$ forcing in (4.1) is

$$
\frac{cd(1-c)}{B^2}>0.
$$

Since $H\ge-\rho$, it follows that

$$
\boxed{
H(t)\ge0
\quad\text{for all}\quad
t\ge
T_2:=T_\rho+\frac{B}{d(1-c)}.
}
\tag{4.3}
$$

Thus any affine nonnegative companion $A+Cx$ satisfies

$$
\mathbb E^-[(B y-c)(A+Cx)]\ge0
\qquad(t\ge T_2).
\tag{4.4}
$$

This is a genuine weighted correlation estimate. It does **not** rescue (3.1), because the second hidden cell contributes the signed factor $\Psi_\Delta$ itself; for short $\Delta$ that factor is not a nonnegative affine companion to which (4.4) can be applied.

The symbolic verifier checks (4.1) and its forcing exactly.

## 5. Current live-coupling interface: exposure edges

The current proof spine no longer uses the cellwise scaffold route. Its dangerous coupling state is

$$
J_i
=1_{\{D_i=0,D_{i+1}=1,X_i=Y_i=1\}}.
\tag{5.1}
$$

Also define the low-risk exposure state

$$
K_i
=1_{\{D_i=0,D_{i+1}=1,X_i=Y_i=0\}}.
\tag{5.2}
$$

Whenever

$$
D_i=0,\qquad D_{i+1}=1,
$$

exactly one of $K_i,J_i$ is one.

Fix a stopping time $s$ at which this exposure condition holds. Let

$$
\sigma
=
\inf\{t>s:D_i(t)=1\}
$$

be creation of the left child and

$$
\tau
=
\inf\{t>s:D_{i+1}(t)=0\}
$$

be coalescence of the right disagreement. Set $e=\sigma\wedge\tau$.

Meeting 004 proves that, while $D_{i+1}=1$, its predictable coalescence intensity is at least

$$
q:=1-c+a.
\tag{5.3}
$$

Crucially, before $e$ the evolution of the common spin at $i$ is independent of the orientation of the right disagreement:

- in state $K_i$, a ring at $i$ creates $J_i$ at rate $a$ and creates the child at rate
  $$
  d=b-a;
  $$
- in state $J_i$, a ring at $i$ returns to $K_i$ at rate
  $$
  k=1-c
  $$
  and creates the child at rate $c$.

Noncoalescing updates at $i+1$ may change its disagreement orientation but do not change these four rates.

Therefore the exposure is dominated by the two-state chain with an additional constant killing rate $q$:

$$
K\xrightarrow{a}J,
\qquad
K\xrightarrow{d}\text{child},
$$

$$
J\xrightarrow{k}K,
\qquad
J\xrightarrow{c}\text{child},
$$

and

$$
K,J\xrightarrow{q}\text{right coalescence}.
\tag{5.4}
$$

The word "dominated" here is only in the direction needed: the true right disagreement may coalesce faster than rate $q$, which can only shorten the exposure and reduce child probability and nonnegative occupation times.

## 6. Exact child probability for an arbitrary live exposure

Let $h_0,h_1$ be the child-before-right-coalescence probabilities in the comparison chain (5.4), starting from $K$ and $J$ respectively. First-step equations are

$$
(b+q)h_0=d+a h_1,
\tag{6.1}
$$

$$
(1+q)h_1=c+k h_0.
\tag{6.2}
$$

Put

$$
\boxed{
\mathfrak D
=(b+q)(1+q)-ak>0.
}
\tag{6.3}
$$

Then

$$
\boxed{
h_0
=\frac{d(1+q)+ac}{\mathfrak D},
}
\tag{6.4}
$$

$$
\boxed{
h_1
=\frac{c(b+q)+kd}{\mathfrak D}.
}
\tag{6.5}
$$

The gaps are

$$
1-h_0
=\frac{q(a+q+1)}{\mathfrak D}>0,
\tag{6.6}
$$

$$
1-h_1
=\frac{q(d+2q)}{\mathfrak D}>0,
\tag{6.7}
$$

and

$$
h_1-h_0
=\frac{q(c-d)}{\mathfrak D}>0.
\tag{6.8}
$$

Hence $J$ is the worst exposure start.

Student F Assignment 003 derived the same formulas when $i+1$ was a **rightmost** source. The current new deduction is:

### Proposition 6.1 (non-rightmost exposure contraction)

At any stopping time with $D_i=0,D_{i+1}=1$, regardless of whether $i+1$ is rightmost and regardless of all deeper disagreements to its right,

$$
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F_s)
\le
h_{X_i(s)}
\le h_1<1.
}
\tag{6.9}
$$

### Proof

Until $e$, the common spin at $i$ has exactly the transition and child-creation rates in (5.4). By Meeting 004, the competing right-coalescence intensity is an adapted rate $r_t\ge q$. The functions $h_0,h_1$ solve the backward equations when $r_t=q$. Replacing $q$ by $r_t\ge q$ makes their generator inequalities superharmonic. Optional stopping at $e$ therefore gives (6.9). Equivalently, predictably thin the true coalescences to a rate-$q$ killing subprocess and ignore all additional coalescences; this can only increase the chance of a child. $\square$

This is an episode estimate valid inside an arbitrary-depth live stack, not a rightmost-source statement.

## 7. Explicit weighted $J_i$ occupation

The same killed chain gives a more direct answer to the quantity highlighted in the current proof spine.

Let $g_x$ be the expected total time spent in state $J$ before child or right coalescence in the comparison chain. The resolvent equations are

$$
(b+q)g_0=a g_1,
\tag{7.1}
$$

$$
(1+q)g_1=1+k g_0.
\tag{7.2}
$$

Hence

$$
\boxed{
g_0=\frac a{\mathfrak D},
\qquad
g_1=\frac{b+q}{\mathfrak D}.
}
\tag{7.3}
$$

Since the true exposure can only be killed faster,

### Proposition 7.1 (weighted live-edge occupation)

For every exposure stopping time $s$ as above,

$$
\boxed{
\mathbb E\left[
\int_s^{e}J_i(t)\,dt
\,\middle|\,
\mathcal F_s
\right]
\le
g_{X_i(s)}
\le g_1.
}
\tag{7.4}
$$

There is also an exact compensator identity that displays why $J_i$ is the correct weight. Before $e$, the child-creation intensity at site $i$ is

$$
dK_i+cJ_i
=d+(c-d)J_i.
\tag{7.5}
$$

Only one child can be created before $e$. Therefore

$$
\boxed{
\mathbb P(\sigma<\tau\mid\mathcal F_s)
=
\mathbb E\left[
\int_s^e
\left(d+(c-d)J_i(t)\right)dt
\,\middle|\,
\mathcal F_s
\right].
}
\tag{7.6}
$$

Combining (6.9) and (7.6),

$$
\boxed{
(c-d)
\mathbb E\left[
\int_s^eJ_i(t)dt
\,\middle|\,
\mathcal F_s
\right]
\le
h_{X_i(s)}
-d\,\mathbb E[e-s\mid\mathcal F_s].
}
\tag{7.7}
$$

This is the requested kind of **disagreement-weighted $J_i$ control**: it does not replace $J_i$ by an unconditional $11$ probability. It controls exactly the high-risk occupation while a live right disagreement is capable of transmitting left.

## 8. Summing the exposure estimate over time

Let

$$
S_i=(1-D_i)D_{i+1}.
$$

Its maximal intervals with $S_i=1$ are precisely the exposure intervals used above. Let $N_i(T)$ be the number of such intervals that start by time $T$, counting a possible interval already active at time zero.

By strong Markov and Proposition 7.1,

$$
\boxed{
\mathbb E\int_0^T J_i(t)\,dt
\le
g_1\,\mathbb E N_i(T).
}
\tag{8.1}
$$

An exposure can start only in one of three ways:

1. it is already active at time zero;
2. $D_i$ coalesces while $D_{i+1}=1$;
3. $D_{i+1}$ is newly created while $D_i=0$.

Let $C_i(T)$ count coalescences of $D_i$ and let $B_{i+1}(T)$ count creations of $D_{i+1}$. Pathwise,

$$
N_i(T)\le1+C_i(T)+B_{i+1}(T).
\tag{8.2}
$$

Because site $i$ rings at rate one,

$$
\mathbb E C_i(T)
\le
\int_0^T u_i(t)\,dt,
\qquad
u_i(t):=\mathbb E D_i(t).
\tag{8.3}
$$

When $D_{i+1}=0$, a disagreement at $i+1$ can be created only if $D_{i+2}=1$. Its creation probability at a ring is $d$ when the agreed spin at $i+1$ is zero and $c$ when it is one, hence at most $c$. Thus

$$
\mathbb E B_{i+1}(T)
\le
c\int_0^T u_{i+2}(t)\,dt.
\tag{8.4}
$$

Consequently

$$
\boxed{
\mathbb E\int_0^T J_i(t)\,dt
\le
\frac{b+q}{\mathfrak D}
\left[
1+
\int_0^T u_i(t)dt
+c\int_0^T u_{i+2}(t)dt
\right].
}
\tag{8.5}
$$

This is an all-time integrated $J_i$ estimate for arbitrary initial coupling and arbitrary ancestry depth.

It is not yet an all-depth contraction. The entry-count bound (8.2) is deliberately crude and loses the post-birth structure that F's two-generation calculation exploits.

## 9. Why this does not already close the coupling drift

Meeting 003 gives

$$
\mathcal L^{\rm coup}D_i
\le
-qD_i+dD_{i+1}+(c-d)J_i.
\tag{9.1}
$$

If one inserts only the crude global consequence (8.5), the integrated inequality contains effective same-site coefficient

$$
q-(c-d)g_1.
$$

Along the East stress path

$$
a=\varepsilon^2,
\qquad b=\varepsilon,
\qquad c=1-\varepsilon^2,
$$

one has

$$
q=2\varepsilon^2,
\qquad
g_1=1-2\varepsilon^2+O(\varepsilon^3),
$$

so

$$
q-(c-d)g_1=-1+O(\varepsilon).
\tag{9.2}
$$

Thus (8.5) by itself is far too weak near East. The loss is not inside a single exposure: (7.6) controls that exactly. The loss is the number of times the same edge can re-enter exposure after a child dies or a parent is recreated.

This identifies a precise interface with F's current Assignment 005:

> the remaining all-depth problem is to control the **exposure-entry/restart count**, using the two-generation regeneration structure or a finite summary state, rather than to improve the one-exposure $J_i$ estimate.

There is also a simple obstruction to a pointwise stopping-time bound with a strict coefficient. At an exposure start with common spin one,

$$
J_i=1,\qquad D_{i+1}=1,\qquad D_i=0.
$$

Therefore any inequality intended to hold conditionally at arbitrary live stopping times of the form

$$
\mathbb E[J_i\mid\mathcal F]
\le
\alpha\mathbb E[D_{i+1}\mid\mathcal F]
+\beta\mathbb E[D_i\mid\mathcal F]
$$

must have $\alpha\ge1$. A strict pointwise conditional suppression of $J_i$ is impossible. The exposure-integrated form (7.7), or a corrector that accounts for restarts, is the natural level at which a genuine gain can occur.

## 10. Anti-circularity and assignment completion

### What was the Assignment 002 question?

Turn the unweighted density information into the weighted regional insertion required by the last-exit route, or prove that this cannot be done by the proposed mechanism.

### What is the verdict?

The one-cell regional kernel is nonnegative, but hiding the preceding successful type produces the exact signed transfer $\Psi_\Delta$. It is negative on every sufficiently short cell. Thus the regional mechanism fails at the first composition step.

### What survives after that route closes?

The generic $L^-$ correlation estimate (4.4) remains correct, and the current live coupling admits the new non-rightmost exposure bounds (6.9), (7.4), and (7.7). The latter is directly expressed in terms of the high-risk $J_i$ appearing in the current coupling drift.

### What remains unresolved?

The exposure-entry/restart count. Crude summation gives (8.5), which is not contractive near East. F's two-generation regeneration result is precisely additional information about those restarts; composing the two inputs is the next structural problem.

## Handoff

`density mechanism cannot control the required regional kernel because: after one positive regional cell, hiding the predecessor type gives the exact transfer Psi_Delta(z)=B K_Delta(z)-c, and Psi_Delta(0)<0 for every sufficiently short positive Delta at every residual parameter point. Reusable weighted estimate: for any live exposure edge D_i=0,D_{i+1}=1, including non-rightmost disagreements, the high-risk occupation satisfies E[int J_i]<=g_x and the exact child compensator is E[int(d+(c-d)J_i)]=P(child before right coalescence)<=h_x<1. The remaining all-depth blocker is the exposure-entry/restart count, not the one-exposure J_i occupation.`
