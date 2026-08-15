# Graduate Student C 002: uniform three-site wall characterization

Date: 2026-08-16

Status: the exact length-three frozen-exterior one-attack factor has a **sharp uniform East-boundary asymptotic gap**. After correcting a source-level residual-region inconsistency, the regime-wide boundary supremum is `5/6`. This is a diagnostic local theorem only. The one-attack factor by itself does not concatenate under a persistent/dynamically evolving exterior, because repeated attacks eventually penetrate every fixed finite block when an exterior disagreement is held forever.

## Executive conclusions

Write on the normalized face `r11=0`

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

Combining the actual theorem statements in Głuchowski--Menz (2025) with the 2026 long-lived-state theorem gives the unresolved set

$$
\mathcal R=
\left\{
0<a<b,\quad
\frac12\le c<1,\quad
c\ge a+b,\quad
b\ge \sqrt2(1-c)
\right\}.
\tag{R}
$$

In particular, throughout `R`,

$$
1>c>b>a>0=r_{11},
$$

so there is only one canonical-coupling ordering chamber. The path used in assignment 001,

$$
a=\varepsilon,\qquad b=\varepsilon/2,\qquad c=1-\varepsilon^2,
$$

is **not** in the actual unresolved set: it is covered by Corollary 7.2 of the published 2025 paper because `b<=a`. The repository labels calling it a genuine strict residual path must be corrected.

Let `R_3^adv(r)` be the maximum unconditional one-attack crossing factor over all eight fully agreed three-site words and both exterior disagreement orientations. Then

$$
\boxed{
\sup_{\bar r\in\partial_E\mathcal R}
\limsup_{\substack{r\to\bar r\\r\in\mathcal R}}
R_3^{\rm adv}(r)
=\frac56.
}
\tag{1}
$$

Here the open East edge is

$$
\partial_E^\circ\mathcal R
=\{(a,b,c)=(0,b,1):0<b\le1\},
$$

and for compactness I include its endpoint `(0,0,1)` in `partial_E R`. The value in (1) is unchanged if the endpoint is omitted and the supremum is taken over the open edge.

The constant `5/6` is sharp along the **genuine residual** sequence

$$
a=\frac\varepsilon2,\qquad
b=\varepsilon,\qquad
c=1-\varepsilon^2,
\qquad \varepsilon\downarrow0.
\tag{2}
$$

Thus assignment 002 yields a uniform local gap, not loss of uniformity. For example, by (1) there exists an East-boundary neighborhood `U` in `R` such that

$$
R_3^{\rm adv}(r)\le\frac{11}{12}
\qquad(r\in U),
\tag{3}
$$

so one may take the explicit contraction margin `delta=1/12`. I have not extracted a numerical Euclidean radius for `U`; (1) is the exact asymptotic statement requested by the assignment and implies (3) by sequential compactness.

However, (1) does **not** supply the required block-renewal theorem. If an exterior disagreement is frozen forever, then under strict positive rates it eventually penetrates every fixed finite agreed block with probability one, despite a sub-one one-attack factor. Hence any valid concatenation must use the stochastic lifetime/evolution of the exterior disagreement and cannot be a theorem whose only local hypothesis is `R_3^adv<1`. This is the exact remaining structural obstruction.

---

## 1. Source correction: the residual chamber in the repository is reversed

This has to be resolved before the finite-state calculation, because assignment 002 explicitly requires the true residual set rather than the path from assignment 001.

### 1.1 What the published 2025 theorem actually says

On the normalized face `r11=0`, the 2025 paper proves ergodicity in at least the following regions relevant here:

1. the product-basis criterion
   $$
   c<a+b;
   $$
2. the additional product-basis region
   $$
   c<\frac12;
   $$
3. Corollary 7.2, which on this face gives
   $$
   0<b\le a.
   $$

The third item is the important one. The version of record states the hypotheses

$$
r_{11}\le r_{10}<1,
\qquad
0<r_{01}\le r_{00},
$$

and proves exponential ergodicity by flipping the state labels on alternating sites and applying Gray's theorem to the resulting periodic weakly monotone system.

This is not only a line in the statement. The proof gives even-site parameters

$$
(c,0,a,b)
$$

and odd-site parameters

$$
(1-b,1-a,1,1-c),
$$

and explicitly says weak monotonicity plus positive rates is equivalent to the displayed hypotheses. Thus the inequality direction `b<=a` is load-bearing in the proof.

### 1.2 The 2026 summary is inconsistent with that theorem

The arXiv text of the 2026 paper summarizes the region covered by the 2025 paper on `r11=0` as containing

$$
b>a.
$$

Taken literally, this contradicts the published Corollary 7.2 above. I found no correction notice. I therefore do **not** use that summary inequality to define the residual. I use the actual proved theorem statements.

This matters immediately: assignment 001 used `a=epsilon`, `b=epsilon/2`, hence `b<a`, so its path is on the already-proved side. Its finite-state calculations remain correct as diagnostics, but statements in the current state/proof-spine/meeting note calling it a genuine unresolved path are false.

### 1.3 Add the 2026 long-lived-state theorem

The 2026 theorem says that a state `s` yields ergodicity if

$$
\delta(s)<\sqrt2\,\beta(s).
$$

On `r11=0`, state `1` has `beta(1)=0` and gives nothing. On the complement of the 2025 regions we have

$$
b>a,\qquad c\ge a+b>b,
$$

so for wall state `0`,

$$
\beta(0)=1-c,
\qquad
\delta(0)=b.
$$

Hence the 2026 theorem additionally covers

$$
b<\sqrt2(1-c).
$$

Taking the complement of these strict sufficient criteria gives exactly (R). Equalities remain in the unresolved set because the corresponding criteria are strict, except for the already-covered `b<=a` boundary.

A useful by-product is that the true residual has the single strict ordering

$$
c>b>a>0=r_{11}.
\tag{4}
$$

No piecewise canonical-coupling chamber decomposition is needed after the source correction.

---

## 2. Exact global definition of the length-three factor

Fix `r in R`. Use a block of sites `0,1,2`, with site `0` protected and site `2` adjacent to the exterior. A coupled-site state is a pair in

$$
\{00,11,01,10\}.
$$

After a designated ring at site `2` against an exterior disagreement `e in {01,10}`, an **attack** occurs if the two copies at site `2` become off-diagonal. If no attack occurs, the one-attack factor is zero.

Conditional on an attack, run the three block clocks until one of two absorbing events:

- `C` (crossing): site `0` becomes off-diagonal;
- `G` (regeneration): all three block pairs are diagonal again.

While this excursion runs, the exterior pair is frozen at `e`. The transient state space is

$$
\mathcal S
=\{(z_0,z_1,z_2):z_0\in\{00,11\},\ z_1,z_2\in\{00,11,01,10\},
\text{ at least one }z_i\text{ off-diagonal}\},
$$

so

$$
|\mathcal S|=2\cdot4\cdot4-2^3=24.
$$

At each embedded step one of the three sites is selected with probability `1/3`, and its new coupled pair is generated by the canonical coupling of the two Bernoulli transition laws. Let `K_r^e` be the resulting `24 x 24` substochastic transient kernel and `x_r^e` the crossing vector. Then

$$
h_r^e=(I-K_r^e)^{-1}x_r^e
\tag{5}
$$

is the vector of conditional crossing-before-regeneration probabilities.

For a fully agreed word `w in {0,1}^3`, let `A_{w,e}(r)` be the probability that the designated boundary ring attacks, and let `nu_{w,e}(r)` be the conditional distribution of the attacked transient state. Define

$$
F_{w,e}(r)
=A_{w,e}(r)\,\nu_{w,e}(r)h_r^e,
\qquad
R_3^{\rm adv}(r)=\max_{w,e}F_{w,e}(r).
\tag{6}
$$

This is exactly the unconditional one-attack quantity requested in assignment 002. Exchanging the labels of the two coupled copies maps exterior `01` to `10` and preserves crossing and regeneration, hence

$$
F_{w,01}(r)=F_{w,10}(r)
\tag{7}
$$

for every fully agreed word. It nevertheless remains useful to keep both orientations in the definition.

---

## 3. Fixed nonzero point on the East edge

First take an East-boundary point

$$
a=0,\qquad c=1,\qquad b\in(0,1].
\tag{8}
$$

For `b>0`, the full `24 x 24` system (5) is nonsingular. I solved it exactly over `Q(b)`. For words ending in `1`, the designated attack probability is one; for words ending in `0`, it is `b`.

The exact verifier proves, for each of the eight words,

$$
F_{w,01}(0,b,1)\le\frac56.
\tag{9}
$$

The proof is algebraic, not numerical. For the rational functions whose common degree-eight denominator is

$$
D_8(b)=
304b^8+1336b^7+892b^6-5496b^5-14351b^4-16234b^3-9651b^2-2844b-324,
$$

we first certify `D_8(b)<0` on `[0,1]`. Under

$$
b=\frac{x}{1+x},\qquad x\ge0,
$$

multiplying `-D_8` by `(1+x)^8` gives the coefficient vector

$$
(46368,232348,477603,535944,362506,152008,38631,5436,324),
$$

which is strictly positive.

For each word, after accounting for the sign of its denominator, the same Mobius substitution turns the numerator of

$$
\frac56-F_{w,01}(0,b,1)
$$

into a polynomial with nonnegative coefficients and at least one positive coefficient. The exact coefficient vectors are emitted by the verifier; no root isolation or floating-point sign decision is used.

Finally,

$$
\lim_{b\downarrow0}F_{111,01}(0,b,1)=\frac56.
\tag{10}
$$

Thus every fixed nonzero point on the East edge has factor at most `5/6`, and the edge supremum can only be attained as `b` tends to zero.

---

## 4. Singular East corner `b -> 0`

This is the only place where simply substituting the boundary parameters into (5) loses information: at `(a,b,c)=(0,0,1)` the zero-order killed chain acquires recurrent classes, and first-order small rates select the eventual crossing probability.

### 4.1 Compact ratios forced by the true residual

For a sequence in `R` with `b -> 0`, set

$$
\alpha=\frac{a}{b},
\qquad
\gamma=\frac{1-c}{b}.
\tag{11}
$$

By (R),

$$
0<\alpha<1,
\qquad
0\le\gamma\le\frac1{\sqrt2}.
\tag{12}
$$

Hence every sequence has a subsequence on which `(alpha,gamma)` converges in the compact rectangle

$$
[0,1]\times[0,1/\sqrt2].
$$

Because of the fixed ordering (4), every entry of the embedded kernel is affine in `a,b,1-c`. Therefore along such a sequence

$$
P=P_0+bP_1(\alpha,\gamma)
\tag{13}
$$

**exactly**, not merely to first order.

### 4.2 Seven-class reduction

At `b=0`, the zero-order chain has seven recurrent singleton classes. In the order

$$
G,\quad
(00,00,10),\quad
(00,10,00),\quad
(00,01,10),\quad
(00,01,00),\quad
(11,00,10),\quad
C,
$$

eliminating the fast zero-order transient states gives the effective generator

$$
Q(\alpha,\gamma)=
\begin{pmatrix}
0&0&0&0&0&0&0\\
\frac{\gamma+1}{3}&-\frac{2\alpha+\gamma+1}{3}&0&\frac\alpha3&0&\frac\alpha3&0\\
\frac\alpha2+\frac\gamma3&\frac\alpha6&-\frac{2\alpha+\gamma+1}{3}&0&0&0&\frac13\\
\frac16&\frac\gamma3&0&-\frac{2\gamma}{3}-\frac12&\frac\gamma3&0&\frac13\\
\frac\alpha3+\frac\gamma3+\frac16&0&0&\frac\alpha6&-\frac\alpha2-\frac\gamma3-\frac12&0&\frac13\\
\frac{\gamma+1}{3}&\frac\gamma3&0&\frac\alpha6&0&-\frac\alpha6-\frac{2\gamma}{3}-\frac12&\frac16\\
0&0&0&0&0&0&0
\end{pmatrix}.
\tag{14}
$$

For completeness, this reduction follows by ordering the states into fast zero-order transient states `T` and zero-order recurrent states `M`. Solve the `T` rows of the hitting system, substitute into the `M` rows, divide the latter by `b`, and let `b -> 0`. The resulting stochastic-complement generator is exactly (14). The verifier performs this elimination directly from the full 26-state matrix (`24 + C + G`) and checks every entry of (14).

### 4.3 Exact corner factors

Let

$$
\begin{aligned}
D(\alpha,\gamma)={}&
8\alpha^3\gamma+18\alpha^3
+54\alpha^2\gamma^2+139\alpha^2\gamma+81\alpha^2\\
&+80\alpha\gamma^3+252\alpha\gamma^2+264\alpha\gamma+90\alpha\\
&+32\gamma^4+128\gamma^3+186\gamma^2+117\gamma+27.
\end{aligned}
\tag{15}
$$

All coefficients are positive. Solving (14), the four nonvanishing corner limits correspond to the words ending in `1`. The word `111` is the largest throughout (12). One convenient expression is

$$
L_{111}(\alpha,\gamma)
=\frac12+
\frac{
6\alpha^3+32\alpha^2\gamma+27\alpha^2
+42\alpha\gamma^2+73\alpha\gamma+30\alpha
+16\gamma^3+40\gamma^2+33\gamma+9
}{D(\alpha,\gamma)}.
\tag{16}
$$

The exact deficit from `5/6` is

$$
\frac56-L_{111}(\alpha,\gamma)
=
\frac{\gamma}{3D(\alpha,\gamma)}
\Big(
8\alpha^3+54\alpha^2\gamma+43\alpha^2
+80\alpha\gamma^2+126\alpha\gamma+45\alpha
+32\gamma^3+80\gamma^2+66\gamma+18
\Big).
\tag{17}
$$

Hence

$$
L_{111}(\alpha,\gamma)\le\frac56,
$$

with equality exactly when `gamma=0`.

The verifier also checks `L_111 >= L_w` for `w=001,011,101`: after multiplication by the common positive denominator `2D`, each difference is a polynomial in `(alpha,gamma)` with strictly positive coefficients. Words ending in `0` have attack probability

$$
b-a=(1-\alpha)b,
$$

so their unconditional factors tend to zero.

This proves the entire singular-corner bound

$$
\limsup R_3^{\rm adv}\le\frac56.
\tag{18}
$$

It is sharp. Along (2),

$$
\alpha=\frac12,
\qquad
\gamma=\varepsilon\to0,
$$

and (17) gives

$$
R_3^{\rm adv}\longrightarrow\frac56.
\tag{19}
$$

For sufficiently small `epsilon`, (2) satisfies every inequality in (R), so unlike the assignment-001 path this is a genuine residual sequence.

---

## 5. Proof of the regime-wide boundary theorem

Take any sequence `r_n in R` approaching the compactified East edge.

After passing to a subsequence, either:

1. `b_n -> b_* > 0`. Then `a_n -> 0`, `c_n -> 1`, and the killed system is nonsingular at `(0,b_*,1)`. The factors converge continuously to the fixed-boundary factors of Section 3, all at most `5/6`.

2. `b_n -> 0`. Then the ratios (11) have a convergent subsequence by (12), and the exact singular reduction of Section 4 gives a limiting adversarial factor at most `5/6`.

Thus every East-boundary sequence has limsup at most `5/6`. The genuine residual sequence (2) attains `5/6`, proving (1).

As an immediate corollary, fix for example `delta=1/12`. If no East-boundary neighborhood satisfied (3), there would be a sequence `r_n in R` with distance to the East edge tending to zero and

$$
R_3^{\rm adv}(r_n)>\frac{11}{12},
$$

contradicting (1). This proves the requested uniform local gap.

---

## 6. What the local theorem does **not** give: repeated attacks

The frozen-exterior one-attack statistic cannot itself be the hypothesis of a correct concatenation theorem.

### Proposition: a persistent exterior disagreement penetrates any fixed finite agreed block almost surely

Fix any strict positive-rate point in the chamber (4), freeze an off-diagonal exterior pair forever, and consider a finite agreed block immediately to its left. If crossing is declared when disagreement reaches the protected left edge, then starting from any fully agreed block,

$$
\mathbb P(\text{eventual crossing})=1.
\tag{20}
$$

#### Proof

Every excursion from a fully agreed block either crosses or eventually regenerates. Indeed, from any transient block state there is a positive-probability finite sequence of updates that forces all block pairs to become `00`: update from right to left and choose the common-zero part of each canonical coupling. Strict positive rates and `c<1` make each required common-zero probability positive. Since the transient state space is finite, there is no closed nonabsorbing class.

From any fully agreed word there is also a positive-probability finite sequence that crosses before the next regeneration. First force the common word to `11...1`: if the rightmost common bit is zero, a boundary update has common-one probability at least `a>0`; then update remaining zero sites from right to left, each with a positive common-one probability. Once the block is all ones, perform a boundary attack and then update successively from right to left. In the chamber `c>b>a>0`, each required off-diagonal propagation has positive probability (in fact the `10/01` East-like propagation uses the `c` discrepancy). Hence, uniformly over the finitely many agreed words, there is some `p(r)>0` such that after every regeneration the conditional probability of crossing before the next regeneration is at least `p(r)`.

By the strong Markov property, the probability of surviving `n` regenerations without crossing is at most `(1-p(r))^n`, which tends to zero. This proves (20).

The same argument works for every fixed finite block length.

### Consequence

`R_3^adv<1` means only that **one attacked excursion** has a chance to regenerate before crossing. If the exterior disagreement remains present, it can attack again, and repeated attacks destroy the wall with probability one.

Therefore a structurally valid theorem must use a finite-lifetime **disagreement episode**, not a frozen state. At minimum it must control, conditionally on the past,

- the lifetime of the exterior disagreement source;
- the number and timing of attacks during that lifetime;
- exterior changes while a block excursion is active;
- the possibility that several neighboring exterior sites disagree;
- overlap between consecutive three-site blocks; and
- tails of episode durations, so spatial extinction can be converted into temporal coupling.

A theorem with only the hypothesis

$$
\sup_r R_3^{\rm adv}(r)<1
$$

is false as an adversarial concatenation principle by (20).

---

## 7. Concrete block-renewal statement that would actually be sufficient

The natural replacement is an **episode crossing** bound. Here is a precise sufficient form.

For a fresh block `B={j-2,j-1,j}`, suppose the coupled trajectories agree on `B` at a stopping time `sigma`, and all disagreement capable of influencing `B` lies to its right. Let `T_B` be the first time after `sigma` at which either

1. disagreement reaches `j-2` (block crossing), or
2. the entire source episode that can influence `B` has disappeared and the block is again fully agreed (episode regeneration).

A block-renewal theorem of the required type would follow from uniform constants `q<1`, `theta>0`, `C<infinity` such that, for every such stopping configuration and conditional on the full past,

$$
\mathbb P(\text{crossing at }T_B\mid\mathcal F_\sigma)\le q,
\tag{21}
$$

and

$$
\mathbb E\left[e^{\theta(T_B-\sigma)}\mid\mathcal F_\sigma\right]\le C.
\tag{22}
$$

Together with the one-sided nearest-neighbor geometry, (21) permits iteration across successive fresh blocks by the tower property; independence is not required. The probability that the influence of one initial disagreement crosses `n` fresh blocks is at most `q^n`. The exponential episode-time bound (22), combined with finite propagation, then gives a temporal coupling tail and hence ergodicity by the same type of influence-cone criterion used in the 2026 paper.

The problem is that (21) is **strictly stronger** than the frozen one-attack inequality. Proposition (20) shows that one cannot verify (21) by simply replacing the dynamic exterior by a permanently adversarial off-diagonal state: under that domination the left side becomes one.

So the next mathematical object is not another block size. It is a source-episode process that includes enough exterior dynamics to prove (21)--(22), or a different spacetime-block construction that is robust to repeated attacks. I do not currently have a rigorous reduction of (21) to `R_3^adv` plus a separately controlled scalar lifetime parameter. Without such a reduction, the Professor's pre-committed dynamic-exterior stop condition is triggered in substance: the local `5/6` theorem alone does not justify continuing the finite-wall architecture.

A small non-rigorous diagnostic is favorable but not load-bearing: on the sharp sequence (2), a finite chain consisting of the three-site block plus one live disagreement source whose right neighbor is held in common state `0` has crossing probability tending numerically to about `2/3`, rather than one. This suggests that source lifetime can matter in the right direction, but a leftward disagreement front may have further disagreements immediately to its right, so this four-site toy does not verify (21) and I do not promote it as evidence for a theorem.

---

## 8. Exact verification

Verifier:

`research/active/noisy-east-positive-rates/students/student-c/002-uniform-three-site-wall-verifier.py`

It performs only exact SymPy algebra for the load-bearing claims. It:

1. reconstructs the full 26-state matrix for the singular corner;
2. finds/eliminates the zero-order fast states;
3. verifies the seven-class generator (14) entry by entry;
4. solves the effective crossing system;
5. verifies (17), sharpness at `gamma=0`, and exact dominance of `111` by positive-coefficient polynomial differences;
6. solves the full `24 x 24` boundary killed system at `(a,b,c)=(0,b,1)`;
7. proves all eight boundary factors are at most `5/6` using exact Mobius-transform coefficient certificates; and
8. checks that the all-one boundary factor tends to `5/6` as `b -> 0`.

The script prints

`all assignment-002 exact certificates passed`.

---

## 9. Required repository corrections for the Professor

I am not editing Professor-owned state/proof-spine files in this assignment, but the next meeting should correct the following factual statements.

1. `state.md`, `proof-spine.md`, Meeting 001, and the Professor verification note currently call
   $$
   (a,b,c)=(\varepsilon,\varepsilon/2,1-\varepsilon^2)
   $$
   a genuine strict residual path. It is not; published Corollary 7.2 already covers it.

2. E0 should define the actual residual by (R), with the source inconsistency recorded explicitly.

3. E3's `9/10` result remains a correct finite-state calculation, but it is a diagnostic on an already-proved parameter path and should not be used as evidence about the unresolved residual.

4. E4 is now solved for the frozen-exterior one-attack quantity, with sharp boundary supremum `5/6`.

5. The live proof-spine obstruction is E5: whether one can prove an episode-level estimate such as (21)--(22) under the dynamically evolving disagreement exterior. Proposition (20) shows that `R_3^adv<1` alone is insufficient.

No new stable project claim should be registered from the finite-state theorem by itself under the standing novelty standard.

Recommendation:

`unresolved — exact remaining obstruction: upgrade the sharp frozen-exterior bound sup R_3^adv=5/6 to an episode-level dynamic-exterior crossing bound such as (21)--(22); repeated attacks make the permanently adversarial exterior crossing probability equal to one, so R_3^adv alone cannot concatenate.`
