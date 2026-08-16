# Student G 008: occupation-weighted actual front

## Verdict

At the hard point

\[
(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
\]

I do **not** prove or refute the actual estimate

\[
G_m:=\sup_{\text{finite zero-boundary systems},\eta,i}
\int_0^\infty \mathbb E\sum_{j\le i-m}D_j(t)\,dt
\le C\theta^m.
\tag{OCC}
\]

I prove the negative outcome allowed in Assignment 008: the Meeting-018 retained state

\[
Z=(s,t)\in\{00,01,10,11\},\qquad M\in\{D,C0,C1\},
\]

does not close to a strict **zero-frequency** occupation renewal using the source-lifetime information currently proved in G003/G006. The obstruction occurs after a genuine source coalescence, not by replacing the source with an immortal disagreement.

The missing variable is the residual right-ancestry capacity to create **distinct future source episodes**. G003 sums repeated exposures while one parent episode stays alive. It explicitly stops when that parent coalesces. A later reinfection of that site from the right is a new parent episode. G006 proves that a fixed site has only finitely many such episodes almost surely, but gives no state-uniform zero-frequency tail for their number.

Two exact statements make the obstruction precise:

1. actual histories with the same `(s,t,C0)` have different future source-return kernels, with a gap at least
   \[
   \frac{b-a}{2}=\frac{99}{20000};
   \tag{1}
   \]
2. if the unrecorded post-coalescence return capacity is closed recursively on the same two-spin state, the finite-depth Bellman values satisfy
   \[
   r_0=h_0,\qquad
   r_n=\frac{h_0}{1-(1-h_0)r_{n-1}},
   \tag{2}
   \]
   where
   \[
   h_0=\frac{1000197}{1020203}>\frac12.
   \tag{3}
   \]
   Hence `r_n\uparrow1`. Every finite-depth envelope has only finitely many source episodes almost surely and uses no immortal source, but no positive two-spin stage weight can have a uniform contraction factor below one.

This is a state-sufficiency obstruction, not a lower process for the actual coupling. In particular I do not prove convective survival, `G_m=\infty`, or failure of tail-shift agreement.

## 1. Exact one-episode input

Put

\[
g=b-a=\frac{99}{10000},\qquad
k=1-c=\frac1{10000},\qquad
q=1-c+a=\frac1{5000}.
\]

Before a fresh target `x` first disagrees, Meeting 018 retains its common spin `s`, the next-left common spin `t`, and only the source mode at `x+1`. In mode `D`, before target discovery,

\[
0\xrightarrow{a}1,
\qquad 0\xrightarrow{g}\text{child},
\]

and

\[
1\xrightarrow{k}0,
\qquad 1\xrightarrow{c}\text{child}.
\]

Every actual disagreement has coalescence intensity at least `q`. Replacing source coalescence by an independent kill of rate exactly `q` is therefore the least-killing comparison already used in G002/G003. Let `h_s` be child-before-source-kill probability in this comparison. First-step analysis gives

\[
(b+q)h_0=g+a h_1,
\qquad
(1+q)h_1=c+k h_0.
\tag{4}
\]

With

\[
\mathfrak D=(b+q)(1+q)-ak
=\frac{1020203}{100000000},
\]

one gets

\[
h_0=\frac{g(1+q)+ac}{\mathfrak D}
=\frac{1000197}{1020203}
=0.980390177249\ldots,
\tag{5}
\]

\[
h_1=\frac{c(b+q)+kg}{\mathfrak D}
=\frac{1019997}{1020203}
=0.999798079401\ldots.
\tag{6}
\]

The true one-episode child probability is bounded **above** by this comparison because the true source can die faster. I use `(5)` below only inside the robust least-killing Bellman envelope; I do not assert it as a lower bound for the actual coupling.

## 2. Actual post-coalescence histories are not determined by `(s,t,M)`

Let `y=x+1`. Consider a stopping time immediately after `y` has genuinely coalesced to common spin zero, while `x` and `x-1` are still coupled with prescribed common spins `(s,t)`. The retained state is `(s,t,C0)`.

There are two reachable finite common-uniform histories with this same projection.

- **A:** the entire half-line `[y,\infty)` is coupled. Then no spontaneous disagreement can appear to the right, so `y` never re-enters `D`.
- **B:** site `y+1` is disagreeing. The clocks at `y` and `y+1` are independent rate-one clocks. With probability `1/2`, `y` rings first. Conditional on that event, since `y` is common zero and its right neighbour disagrees, mark measure exactly `g=b-a` creates a disagreement at `y`. Therefore
  \[
  \boxed{
  \mathbb P(D_y\text{ returns before the next }y+1\text{ ring}\mid\mathcal F)
  \ge\frac g2=\frac{99}{20000}.}
  \tag{7}
  \]

Both histories are reachable with positive probability from one disagreement seed by prescribing finitely many strict clock/mark events. For B, start with a disagreement at `y+1`, create a child at `y`, then let that child coalesce to common zero while `y+1` remains disagreeing and `x` remains fresh.

Thus after an **actual** source death, the two-spin projection forgets information which changes the next-source-episode law by a fixed positive amount.

## 3. Why G003 does not close this return

G003 fixes one live parent and counts repeated entries of the exposure edge before that same parent first coalesces. If `N` is that count,

\[
\mathbb P(N\ge n\mid\mathcal F)\le h_1^{n-1}.
\tag{8}
\]

This is exactly the right theorem for target deaths and reinfections while one source episode survives. The return in `(7)` occurs **after the source itself has coalesced**. G003 classifies it as a new parent episode.

One may apply G003 again one site farther right, but after that deeper parent dies the same question moves another step right. The residual depth/state of this ancestry is absent from `(s,t,M)`. G006 supplies only the qualitative terminal statement that each fixed site eventually couples permanently from a finite seed.

The next calculation shows that at zero frequency, forgetting how much of this right ancestry remains forces the projected Bellman closure to reset its worst continuation value.

## 4. Finite-depth closed return envelope

Define a state-only envelope recursively. This is an upper-certificate class, not an actual lower process.

- `E_0`: one least-killing source episode from Section 1.
- `E_n`, `n>=1`: run one such source episode. If it discovers the target, stop. If the source is killed first, invoke a depth-`n-1` hidden return mechanism one level to the right. If no return occurs, stop in permanent coupling. If a return does occur, the retained state again only records a fresh target and a live source; because the residual right ancestry is unrecorded, the closed state-only Bellman value resets to `E_n`.

Each source episode is finite. At every finite depth the probability of another top-level retry is strictly below one, so the number of source episodes is geometric and finite almost surely. There is no immortal `D`. We also use only one target exposure per distinct source episode, so the within-parent G003 bound `(8)` is respected; all recursion is between genuinely distinct parent episodes.

Downgrade every one-episode discovery probability to the uniform worst value `h_0`. Let `r_n` be the discovery value of `E_n`. Then

\[
r_0=h_0,
\]

and for `n>=1`,

\[
r_n=h_0+(1-h_0)r_{n-1}r_n,
\]

hence

\[
\boxed{r_n=\frac{h_0}{1-(1-h_0)r_{n-1}}.}
\tag{9}
\]

### Proposition 4.1

At the hard point,

\[
\boxed{r_n\uparrow1.}
\tag{10}
\]

Indeed,

\[
1-r_n
=\frac{(1-h_0)(1-r_{n-1})}
{1-(1-h_0)r_{n-1}}
\le\frac{1-h_0}{h_0}(1-r_{n-1}),
\]

and

\[
\frac{1-h_0}{h_0}
=\frac{20006}{1000197}
<\frac1{49}.
\tag{11}
\]

Thus

\[
1-r_n\le
\left(\frac{1-h_0}{h_0}\right)^{n+1}.
\tag{12}
\]

The first exact-decimal values are

\[
r_0=0.980390177249\ldots,
\quad
r_1=0.999607916946\ldots,
\quad
r_2=0.999992157592\ldots,
\quad
r_3=0.999999843135\ldots.
\]

These are values of the **closed projected envelope**, not claimed actual discovery probabilities. The calculation says precisely what information is missing: after a source reinfection, the actual right ancestry has aged or been consumed, but `(s,t,M)` has no variable with which to lower its future return capacity. A state-only robust Bellman closure therefore resets the same worst hidden continuation.

## 5. No positive two-spin stage weight gives strict zero-frequency contraction

Let `v(0),v(1)>0` be any positive spatial-stage weight of the form used in Meeting 018, and put `v_*=\min(v(0),v(1))`. Start from a spin attaining `v_*`. On target discovery the next-current spin is either zero or one, so its terminal weight is at least `v_*`. Therefore the depth-`n` closed envelope gives

\[
\mathbb E[v(t_{\rm abs});\text{ discovery}]
\ge v_* r_n.
\tag{13}
\]

For every `theta<1`, `(10)` gives finite `n` with `r_n>theta`, and then `(13)` is larger than `theta v_*`. Hence:

\[
\boxed{
\text{the zero-frequency closed two-spin Bellman envelope has no uniform positive-weight contraction }\theta<1.}
\tag{14}
\]

This is not failure of one guessed scalar norm. Every positive reweighting of the retained spin type fails after robust closure over hidden depth.

Meeting 018 escapes `(14)` because its positive Laplace factor `e^{-\lambda\tau}` charges late returns. At `lambda=0`, a finite but recursively renewable hidden ancestry carries no cost unless its residual return capacity is quantitatively controlled.

## 6. The missing episode count is itself a zero-frequency observable

Let `N_i` be the number of maximal disagreement episodes at site `i`, and

\[
O_i:=\int_0^\infty D_i(t)\,dt.
\]

Two elementary bounds show that controlling `N_i` is not a free local supplement.

First,

\[
\boxed{\mathbb E N_i\le\mathbb E O_i.}
\tag{15}
\]

At the start of each disagreement episode, `D_i=1`. Only the clock at `i` can change `D_i`, so the episode contains the interval to the next independent rate-one ring at `i`, whose conditional mean is one. These first inter-ring intervals are disjoint across episodes, proving `(15)`.

Second, every episode after a possible initial one begins with a `0\to1` disagreement birth at `i`. Such a birth requires `D_{i+1}=1`; its rate is `g` when the common spin at `i` is zero and `c` when it is one. Hence the birth compensator gives

\[
\boxed{
\mathbb E N_i
\le D_i(0)+c\,\mathbb E O_{i+1}.}
\tag{16}
\]

Thus an all-depth theorem controlling distinct post-coalescence source episodes would already be a new zero-frequency spatial occupation mechanism. Fixed-site permanent coupling only says `N_i<\infty` almost surely; it does not supply the quantitative input needed to break `(9)`.

## 7. Scope and handoff

Nothing above proves that the actual coupling realizes the envelope `E_n`, that actual eventual discovery has probability one, or that `(OCC)` is false. In particular I prove neither convective survival nor failure of F012's tail-shift target.

What is proved is narrower and structural:

- `(s,t,M)` is not Markov after genuine source coalescence, by the actual-history gap `(7)`;
- G003 removes same-parent re-entry but not distinct post-coalescence parent episodes;
- closing the still-hidden return capacity on the same projected state gives the exact finite-depth recursion `(9)`, with contraction-factor supremum one;
- the missing episode-count quantity is itself controlled by zero-frequency occupation through `(15)`--`(16)`.

Therefore a positive `(OCC)` proof along this interface would require a new all-depth theorem for the residual source-return kernel, or an equivalent occupation estimate. That is information beyond the retained two-spin exploration rather than a further optimization of it.

Exact transfer status:

> `two-spin occupation exploration refuted because: after a genuine source coalescence the retained state (s,t,C0/C1) forgets the residual right-ancestry capacity for distinct future source episodes. Actual common-uniform histories with the same projected state have different return kernels, with an explicit gap at least (b-a)/2=99/20000. G003 controls repetitions only while one parent episode remains alive, and G006 gives only almost-sure eventual permanent coupling. Robustly closing the missing post-coalescence return capacity on the same two-spin state yields r_0=h_0 and r_n=h_0/[1-(1-h_0)r_{n-1}], where h_0=1000197/1020203>1/2, so r_n tends to 1 although every finite-depth envelope has only finitely many source episodes almost surely. Hence no positive two-spin stage weight has zero-frequency contraction factor theta<1. This is a state-sufficiency obstruction, not a refutation of actual OCC; a new all-depth source-return/episode-count theorem would be required.`

The exact rational checks are in

`students/student-g/008-occupation-weighted-front-verifier.py`.
