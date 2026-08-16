# Student G 001: transport--dissipation and finite-box density estimates

## Scope and status

This is an independent attack on the residual positive-rates chamber. I did not use the principal's remembered last-successful-interaction construction. The output is an estimate on the original spin dynamics, not a change of representation.

On the normalized face

$$
r_{11}=0,
$$

write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

In the source-corrected residual chamber

$$
0<a<b,\qquad \frac12\le c<1,\qquad c\ge a+b,\qquad b\ge\sqrt2(1-c).
$$

In particular

$$
0<a<b<c<1.
$$

The main point is that the normalized condition $r_{11}=0$ gives a surprisingly strong dissipative identity for the one-density. The one-sided dependence appears only as a discrete transport term, which telescopes over intervals. This gives a macroscopic density of zeros after an $O(1)$ burn-in uniformly over the initial configuration and with only an $O(1/L)$ right-boundary loss. A second local identity shows that adjacent $11$ pairs are suppressed at rate one; near the East boundary $b\downarrow0$, this gives a quantitative mesoscopic approximation by the hard-core subshift with no adjacent ones.

These statements do **not** prove ergodicity. They do produce the finite-box/high-density input requested in the assignment in a form that is independent of convergence or an invariant measure.

## 1. Exact one-site transport--dissipation identity

Let $\eta(t)\in\{0,1\}^{\mathbb Z}$ denote the normalized simple IPS. Each site has a rate-one clock, and at an update of site $i$ the new spin is Bernoulli with parameter $r_{\eta_i\eta_{i+1}}$.

Set

$$
m_i(t)=\mathbb E[\eta_i(t)],\qquad q_i(t)=\mathbb P(\eta_i(t)=0,\eta_{i+1}(t)=0).
$$

Also put

$$
k=1+b+c,\qquad A=b+c-a.
$$

In the residual chamber $A>0$.

### Lemma 1 (exact drift identity)

For every initial law and every site $i$,

$$
\boxed{
\frac{d}{dt}m_i
=(b+c)-k m_i-Aq_i+c(m_i-m_{i+1}).
}
$$

The same identity holds in a finite interval, including the last interior site, with $m_{i+1}$ there interpreted as the prescribed right-boundary spin (or its expectation for an exogenous boundary process).

### Proof

Write $p_{xy}=\mathbb P(\eta_i=x,\eta_{i+1}=y)$. Since the coordinate function changes only when site $i$ updates,

$$
\frac{d}{dt}m_i
=a p_{00}+b p_{01}-(1-c)p_{10}-p_{11}.
$$

Using

$$
p_{00}=q_i,\qquad
p_{11}=q_i+m_i+m_{i+1}-1,
$$

and the corresponding identities $p_{01}=m_{i+1}-p_{11}$ and $p_{10}=m_i-p_{11}$ gives the displayed formula by direct simplification. $\square$

The useful feature is the sign. The $00$ term is an **additional negative term** in the one-density, while all spatial dependence has been isolated into the divergence $c(m_i-m_{i+1})$.

## 2. Boundary-uniform finite-interval density lower bound

Let

$$
I=\{\ell,\ell+1,\ldots,\ell+L-1\}
$$

and define the expected number of ones and zeros in $I$ by

$$
S_I(t)=\sum_{i\in I}m_i(t),\qquad Z_I^{\rm av}(t)=L-S_I(t).
$$

Summing Lemma 1 over $I$ gives the **exact** balance

$$
\frac{d}{dt}S_I
=L(b+c)-kS_I-A\sum_{i\in I}q_i
+c\bigl(m_\ell-m_{\ell+L}\bigr).
$$

Hence, since $A\ge0$ and $m_\ell-m_{\ell+L}\le1$,

$$
S_I'(t)\le L(b+c)-kS_I(t)+c.
$$

Solving this scalar differential inequality and using $S_I(0)\le L$ yields

$$
S_I(t)
\le e^{-kt}L+\frac{L(b+c)+c}{k}(1-e^{-kt}).
$$

Equivalently:

### Proposition 2 (uniform density creation)

For every initial configuration or initial law, every interval $I$ of length $L$, and every $t\ge0$,

$$
\boxed{
\frac1L\sum_{i\in I}\mathbb P(\eta_i(t)=0)
\ge
\theta_{L,t}:=
\frac{1-e^{-kt}}{k}\left(1-\frac cL\right).
}
$$

The same estimate holds for the process in a finite interval with **either fixed right boundary condition**, and more generally for any prescribed boundary history. No assumption is made on the left boundary because the dynamics is one-sided to the right.

For the true residual chamber, $b<c<1$, so

$$
k=1+b+c<3.
$$

Consequently

$$
\liminf_{t\to\infty}\liminf_{L\to\infty}
\inf_{\text{initial states, right boundary}}
\frac1L\sum_{i\in I}\mathbb P(\eta_i(t)=0)
\ge \frac1{1+b+c}>\frac13.
$$

This is substantially stronger near the noisy-East boundary than the trivial forcing obtained from the smallest one-step probability of creating a zero, which is $1-c$ and tends to zero at that boundary.

### Invariant-law corollary

If $\mu$ is **any** invariant law, not assumed translation invariant, stationarity in Proposition 2 and then $t\to\infty$ give

$$
\boxed{
\frac1L\sum_{i\in I}\mu(\eta_i=0)
\ge \frac1k\left(1-\frac cL\right).
}
$$

Thus every invariant law has lower Cesaro zero density at least $1/k>1/3$, uniformly over the location of the interval. If $\mu$ is translation invariant, this reduces to

$$
\mu(\eta_0=0)\ge\frac1{1+b+c}>\frac13.
$$

This conclusion uses invariance only after the transient estimate has already been proved; it is not an invariant-measure reformulation of the PRC.

## 3. Quantitative one-sided finite propagation

The preceding estimate is in expectation. For the requested finite-box interface it is useful that one-sided nearest-neighbour propagation has a particularly simple quantitative error.

Let

$$
H_R(t)=\mathbb P(\operatorname{Pois}(t)\ge R).
$$

Consider the graphical construction from a deterministic initial configuration. To make the spin at $(i,t)$ depend on the initial state or graphical randomness at site $i+R$, there must be a decreasing-time chain of clock rings at the unique sequence of sites

$$
i,i+1,\ldots,i+R-1.
$$

Reading backwards, the waiting times to the successive required clock rings are independent $\operatorname{Exp}(1)$ variables. Therefore

$$
\boxed{
\mathbb P(\text{the backward influence cone from $(i,t)$ reaches $i+R$})
\le H_R(t).
}
$$

In particular, if two versions of the process have identical initial data and graphical randomness up to site $i+R-1$ but arbitrary different data to the right, then

$$
\mathbb P(\eta_i(t)\ne\widetilde\eta_i(t))\le H_R(t).
$$

For fixed $t$, this error is superexponentially small in $R$ in the elementary Poisson-tail sense

$$
H_R(t)\le\left(\frac{et}{R}\right)^R
\qquad (R>et).
$$

This is the quantitative boundary error needed to pass between large one-sided boxes and the infinite system at a fixed burn-in time.

## 4. A finite-box high-probability density estimate

Let

$$
Z_I(t)=\sum_{i\in I}(1-\eta_i(t))
$$

be the actual number of zeros in a block of length $L$.

For each $i$, truncate the graphical construction at distance $R$ to the right, replacing site $i+R$ by a fixed boundary trajectory, and call the resulting zero indicator $X_i^{(R)}(t)$. Then

$$
\mathbb P\bigl(X_i^{(R)}(t)\ne1_{\{\eta_i(t)=0\}}\bigr)\le H_R(t).
$$

Conditional on the initial configuration, the family $\{X_i^{(R)}(t):i\equiv s\pmod R\}$ is independent for each residue class $s$, because its members use disjoint sets of sitewise Poisson clocks and marks. Thus a coloring into $R$ residue classes and Hoeffding's inequality give the following.

### Proposition 3 (finite-box concentration)

Fix $t>0$, an interval $I$ of length $L$, and $u\in(0,\theta_{L,t})$. For any integer $1\le R\le L$ satisfying $H_R(t)\le u/2$,

$$
\boxed{
\mathbb P\left(\frac{Z_I(t)}L\le\theta_{L,t}-u\right)
\le
L H_R(t)
+R\exp\left(-\frac{u^2L}{4R}\right).
}
$$

The bound is uniform over the initial configuration. Hence it also holds for an arbitrary random initial law by conditioning. It is also uniform over fixed right-boundary conditions in finite volume.

### Proof

Couple the full and truncated variables using the same graphical construction. A union bound shows that they all agree with probability at least $1-LH_R(t)$. Moreover their expected sums differ by at most $LH_R(t)$. Proposition 2 therefore gives

$$
\mathbb E\sum_{i\in I}X_i^{(R)}(t)
\ge (\theta_{L,t}-H_R(t))L.
$$

On the event that all couplings agree, if $Z_I(t)\le(\theta_{L,t}-u)L$, then the truncated sum lies at least $(u-H_R(t))L\ge uL/2$ below its mean. Splitting the truncated sum among the $R$ residue classes, at least one class lies at least $uL/(2R)$ below its own mean. Each class contains at most $L/R+1\le2L/R$ independent $[0,1]$ variables. Hoeffding and a union bound over the $R$ classes give

$$
R\exp\left(-\frac{u^2L}{4R}\right).
$$

Adding the coupling-failure probability proves the claim. $\square$

Taking, for example, $R=\lceil\sqrt L\rceil$ shows that after any fixed positive burn-in, a positive macroscopic zero density holds with a stretched-exponential-in-$\sqrt L$ error (up to the even smaller Poisson-tail term), uniformly over initial states.

This is a genuine finite-box statement rather than the assertion that an invariant law "should have high density".

## 5. Adjacent-one suppression and a mesoscopic hard-core regime

There is a second estimate that is sharper near the East boundary.

Let

$$
v_i(t)=\mathbb P(\eta_i(t)=\eta_{i+1}(t)=1).
$$

For $F_i(\eta)=\eta_i\eta_{i+1}$, the two sites that can change $F_i$ give

$$
\frac{d}{dt}v_i
=b\,\mathbb P(01)-\mathbb P(11)
+a\,\mathbb P(100)+b\,\mathbb P(101)
-(1-c)\mathbb P(110)-\mathbb P(111).
$$

Because $a<b$, the positive triple terms are bounded by

$$
a\,\mathbb P(100)+b\,\mathbb P(101)
\le b\,\mathbb P(10),
$$

while the last two terms are nonpositive. Since

$$
\mathbb P(01)+\mathbb P(10)\le1-v_i,
$$

we obtain

$$
\boxed{
v_i'(t)\le b-(1+b)v_i(t).
}
$$

Hence

$$
\boxed{
v_i(t)
\le \frac{b+e^{-(1+b)t}}{1+b}.
}
$$

For every invariant law, again without assuming translation invariance,

$$
\boxed{
\mu(\eta_i=\eta_{i+1}=1)\le\frac{b}{1+b}.
}
$$

Now set

$$
t_b=\frac{\log(1/b)}{1+b}
$$

when $b<1$. Then, uniformly over initial states,

$$
v_i(t_b)\le\frac{2b}{1+b}\le2b.
$$

Thus for any interval $I$ of length $L$,

$$
\boxed{
\mathbb P(\text{$I$ contains an adjacent $11$ pair at time $t_b$})
\le 2b(L-1).
}
$$

On the complementary event, the word on $I$ belongs to the one-dimensional hard-core subshift (no adjacent ones), so it deterministically contains at least $\lfloor L/2\rfloor$ zeros. Consequently

$$
\boxed{
\mathbb P\left(Z_I(t_b)<\lfloor L/2\rfloor\right)
\le2b(L-1).
}
$$

In particular, along any genuine residual approach to the East boundary $b\downarrow0$, taking

$$
L_b=\lfloor b^{-1/2}\rfloor
$$

gives a diverging box on which, after a logarithmic burn-in,

$$
\mathbb P\left(\eta_I(t_b)\text{ has no adjacent ones and }Z_I(t_b)\ge\lfloor L_b/2\rfloor\right)
\ge1-O(\sqrt b),
$$

uniformly over the initial configuration and boundary condition.

This is the strongest target-specific output of this block: the noisy-East residual dynamically enters a mesoscopic hard-core regime with an explicit error, rather than merely having some unspecified positive density of the facilitating state.

## 6. What this makes strictly easier

The previous unresolved statement was ergodicity/disagreement extinction in the residual chamber. The new statements do not encode disagreement at all and are strictly weaker than convergence:

1. **Macroscopic density after fixed burn-in.** Every trajectory, from every initial state, has expected zero density at least $(1-e^{-kt})/k$ up to an $O(1/L)$ boundary term, with residual-wide asymptotic floor $>1/3$.
2. **Finite-box probability.** The same statement holds with an explicit high-probability error from one-sided finite propagation.
3. **Noisy-East hard-core approximation.** As $b\to0$, boxes of any size $L=o(1/b)$ contain no adjacent ones with probability $1-o(1)$ after time $O(\log(1/b))$; on such boxes at least half the sites are zero.
4. **Invariant-law consequence without uniqueness.** Every invariant law satisfies the same one-density floor and the $11$ suppression bound.

These can be falsified or improved without solving PRC, so they pass the anti-circularity test.

The most immediate interface with Student F's separate reconstruction is quantitative: if the recovered Duhamel inequality only needs a zero-density threshold below $1/(1+b+c)$ (or a half-zero-density statement on mesoscopic East boxes), the premise is now proved. If it needs density tending to one, or a persistent/regenerating zero rather than a one-time density statement, this block does not supply it.

## 7. Exact blocker after this block

Density by itself does not control the lifetime of a zero wall or the evolution of a disagreement source. The old frozen-exterior obstruction therefore remains untouched: repeated attacks can cross a fixed wall if the exterior disagreement is artificially held forever.

The next non-circular step would have to use one of the estimates above to prove an **episode-level** statement, for example:

- convert the mesoscopic no-$11$ event into a regeneration probability for the actual dynamic exterior source; or
- show that the last-successful-interaction/Duhamel terms are small under the proved density/hard-core bounds.

I do not currently have that implication. This is the exact remaining blocker, not a hidden equivalent formulation.

## 8. Literature check

I checked the primary Głuchowski--Menz 2025 paper and the 2026 long-lived-state paper before developing the estimate, as well as the closed noisy-East branch. The 2026 paper explicitly describes the unresolved models as noisy East systems and notes heuristically/simulationally that "1s annihilate each other", but its proof uses the long-lived-state coupling criterion rather than a transient density or $11$-pair drift estimate. I did not find Proposition 2, Proposition 3, or the mesoscopic hard-core estimate stated in those sources or in the current repository.

The one-sided finite-propagation ingredient itself is standard graphical-construction technology; it is not claimed as novel. The target-relevant content here is the transport--dissipation identity and its combination with finite propagation, plus the adjacent-$11$ dissipation estimate. This is a novelty check against the closest project/target sources, not a claim of priority over all IPS literature.

new target-relevant estimate: on the true normalized residual chamber, every initial state develops a boundary-uniform macroscopic zero density with asymptotic floor $1/(1+b+c)>1/3$ and explicit finite-box concentration; moreover, near the East boundary $b\downarrow0$, after time $\log(1/b)/(1+b)$ every box of length $o(1/b)$ is hard-core (no adjacent ones, hence at least half zeros) with probability $1-o(1)$.