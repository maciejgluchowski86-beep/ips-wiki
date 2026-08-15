# Graduate Student C 001: exact two-site agreed-block wall test

Date: 2026-08-15

Status: exact two-site calculation complete; the proposed inference from length two to all fixed finite walls is refuted by a targeted length-three persistence check. The length-three observation is diagnostic only and is not a project result under the standing novelty standard.

## Executive conclusion

The two-site agreed-block test is a sharp negative near the East boundary.

On the strict residual path

$$
r_{11}=0,\qquad r_{10}=1-\varepsilon^2,\qquad r_{01}=\frac\varepsilon2,\qquad r_{00}=\varepsilon,
\qquad 0<\varepsilon<\frac12,
$$

the exact two-site killed excursion has Perron factor

$$
\rho_2(\varepsilon)
=
\frac{3-2\varepsilon-2\varepsilon^2+
\sqrt{(1-\varepsilon)^2+2\varepsilon^3}}{4}
\longrightarrow 1,
$$

and, starting from the fully agreed block `11` against a frozen exterior disagreement, its one-attack crossing factor is

$$
F_2(\varepsilon)
=
\frac{2(1-\varepsilon^2)(3+2\varepsilon-2\varepsilon^2-2\varepsilon^3)}
{6+7\varepsilon+6\varepsilon^2+4\varepsilon^3}
\longrightarrow 1.
$$

Thus length two gives no contraction margin stable as the residual approaches East. At the limiting East rule, a boundary disagreement creates the alternating local pair `10`, and the next update of the left site crosses deterministically before the right site can regenerate.

However, **this does not justify killing the whole finite-block wall mechanism**. The obstruction is genuinely length-two. A targeted exact length-three check on the same path gives

$$
\lim_{\varepsilon\downarrow0}R_3^{\mathrm{adv}}(\varepsilon)=\frac9{10}<1
$$

for the same one-attack/frozen-exterior test, where the adversary ranges over all fully agreed three-site configurations and the two exterior disagreement orientations. The maximizer in the limit is the all-one block. Hence the proposed proof-spine alternative “the length-two cycle persists for every fixed block length” is false on this diagnostic.

This is not a length-three theorem and not a contribution under the novelty standard. It is enough to change the next question: before abandoning finite walls, characterize the length-three factor over **all** residual approaches to the East boundary and then decide whether a structural block-renewal theorem is plausible. Do not proceed by a blind sequence of larger numerical blocks.

Recommendation:

`unresolved — precise next falsification test: characterize the exact length-three adversarial crossing/regeneration factor over every asymptotic approach to the residual East boundary; in particular decide whether its limsup is uniformly <1. Do not move to length four unless this characterization exposes a new obstruction.`

---

## 1. Source conventions checked directly

The notation is

$$
r_{xy}:=P_0(1\mid xy),\qquad x,y\in\{0,1\},
$$

for a homogeneous one-sided nearest-neighbor binary IPS. Each site has a rate-one clock. At an update, the new binary value is sampled from the local transition law. Under the canonical coupling, all initial conditions use the same site clocks and the same uniform random variable at a given update.

The 2026 long-lived-state theorem defines, for a candidate common state `a`,

$$
\beta(a)=\min_\zeta P_0(a\mid\zeta),
\qquad
\delta(a)=\max_{\zeta:\zeta(0)=a}\bigl(1-P_0(a\mid\zeta)\bigr),
$$

and proves ergodicity when

$$
\delta(a)<\sqrt2\,\beta(a).
$$

The factor `sqrt(2)` is not a finite-state eigenvalue. In the proof it is the sign condition for the drift of the two random walks bounding the disagreement region after the time-scaling lemma preserves the ratio `beta/delta` while sending both rates to zero.

The same paper records that, after the earlier reductions, the unresolved region on the face `r11=0` lies next to

$$
(r_{11},r_{10},r_{01},r_{00})=(0,1,\text{positive},0).
$$

The 2025 result covers, on the face `r11=0`, the union of

$$
r_{10}<\frac12,
\qquad
r_{10}<r_{01}+r_{00},
\qquad
r_{01}>r_{00}.
$$

Sources checked:

- M. Głuchowski and G. Menz, *Time-Scaling, Ergodicity, and Covariance Decay of Interacting Particle Systems*, Journal of Statistical Physics 192 (2025), article 6, especially Sections 2 and 7.
- M. Głuchowski and G. Menz, *Ergodicity Criterion for One-Sided, One-Dimensional IPS with a Long-Lived State*, Electronic Communications in Probability 31 (2026), arXiv:2508.08459, especially Theorem 3.1 and Section 4.

I found no block-wall extension in the checked 2026 proof. Its blocking objects are one-site spacetime intervals of common state.

## 2. One-site calibration

On the normalized face `r11=0`, take common state `0`. Then

$$
\beta(0)=1-\max\{r_{00},r_{01},r_{10},r_{11}\},
$$

and

$$
\delta(0)=\max\{r_{00},r_{01}\}.
$$

In the residual wedge where `r10` is the maximum,

$$
\beta(0)=1-r_{10},
\qquad
\delta(0)=\max\{r_{00},r_{01}\}.
$$

For common state `1`, `r11=0` gives

$$
\beta(1)=0,
$$

so Theorem 3.1 cannot apply.

Along the path used below,

$$
(r_{11},r_{10},r_{01},r_{00})
=
\left(0,1-\varepsilon^2,\frac\varepsilon2,\varepsilon\right),
$$

we have

$$
\beta(0)=\varepsilon^2,
\qquad
\delta(0)=\varepsilon,
$$

so the one-site criterion fails whenever `epsilon < 1/sqrt(2)`.

For `0<epsilon<1/2`, the path is also strictly outside all three 2025 covered regions:

$$
1-\varepsilon^2>\frac12,
$$

$$
1-\varepsilon^2>\frac32\varepsilon
=r_{01}+r_{00},
$$

and

$$
r_{01}=\frac\varepsilon2<\varepsilon=r_{00}.
$$

Thus it is a genuine strict residual approach to the East corner, not a path through an already covered set.

## 3. Exact canonical two-site killed chain

Take block sites `0,1`, with site `1` on the influencing/right side and site `0` on the protected/left side. Let the coupled copies be `zeta,xi`. A coupled-site state is one of

$$
00,\quad11,\quad01,\quad10.
$$

During one local excursion, freeze the exterior pair at site `2` in one of the adversarial disagreement orientations `01` or `10`.

The transient states are exactly

$$
(A;BC),
\qquad
A\in\{0,1\},
\quad
BC\in\{01,10\},
$$

meaning that site `0` is agreed in state `A`, while site `1` is disagreed with orientation `BC`.

The excursion ends in one of two ways.

- **crossing:** an update of site `0` makes its coupled pair off-diagonal;
- **regeneration:** an update of site `1` makes its coupled pair diagonal, so both block sites agree again.

Observe the embedded chain only at clock rings in the two-site block. Because both clocks have rate one, each embedded update is at site `0` or `1` with probability `1/2`.

For Bernoulli parameters `p,q`, the canonical coupling kernel is

$$
\kappa_{00}(p,q)=1-\max\{p,q\},
$$

$$
\kappa_{11}(p,q)=\min\{p,q\},
$$

$$
\kappa_{01}(p,q)=(q-p)_+,
\qquad
\kappa_{10}(p,q)=(p-q)_+.
$$

Fix exterior pair `EF in {01,10}`. From transient state `(A;BC)`, define

$$
p_0=r_{AB},\qquad q_0=r_{AC},
$$

for a site-0 update and

$$
p_1=r_{BE},\qquad q_1=r_{CF}
$$

for a site-1 update.

The exact transient kernel `K`, crossing vector `x`, and regeneration vector `y` are

$$
K_{(A;BC),(A';BC)}
\mathrel{+}=\frac12\kappa_{A'A'}(p_0,q_0),
\qquad A'\in\{0,1\},
$$

$$
x_{(A;BC)}
=\frac12\lvert p_0-q_0\rvert,
$$

$$
K_{(A;BC),(A;B'C')}
\mathrel{+}=\frac12\kappa_{B'C'}(p_1,q_1),
\qquad B'C'\in\{01,10\},
$$

$$
y_{(A;BC)}
=\frac12\bigl(1-\lvert p_1-q_1\rvert\bigr).
$$

Every row satisfies the exact bookkeeping identity

$$
K\mathbf1+x+y=\mathbf1.
$$

Let `h_s` be the probability of crossing before regeneration from transient state `s`. First-step decomposition gives

$$
h=Kh+x,
$$

hence

$$
\boxed{h=(I-K)^{-1}x.}
$$

Also,

$$
\mathbb P_s(\text{no absorption in the first }n\text{ block updates})
=e_s^\top K^n\mathbf1.
$$

Therefore the Perron root `rho(K)` is exactly the spectral survival factor of the killed excursion.

This is the requested finite-state operator. A numerical eigenvalue is not being substituted for it.

### Important interpretation

For any strict positive-rate point with a positive regeneration probability, `rho(K)<1` is almost automatic for this finite substochastic chain. Thus `rho(K)<1` at a single parameter point is not itself a useful ergodicity theorem. The informative issue for this falsification test is whether either the spectral factor or the actual crossing factor retains a nontrivial contraction margin as one approaches the unresolved East boundary.

## 4. Closed two-state subsystem on the strict residual path

Write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},\qquad d=r_{11}.
$$

Assume

$$
d=0,\qquad c>b,\qquad a\ge b,
$$

and freeze the exterior disagreement as `01`. If the right-site disagreement has orientation `10`, then while it survives it remains orientation `10`. The four-state chain therefore has the closed two-state subsystem

$$
S_0=(0;10),
\qquad
S_1=(1;10).
$$

On the ordered basis `(S0,S1)`,

$$
\boxed{
K=
\frac12
\begin{pmatrix}
1-a+c-b & b\\
1-c & c-b
\end{pmatrix}.}
$$

The crossing and regeneration vectors are

$$
\boxed{
x=\frac12
\begin{pmatrix}
a-b\\c
\end{pmatrix},
\qquad
y=\frac12
\begin{pmatrix}
1-c+b\\1-c+b
\end{pmatrix}.}
$$

In particular, if `c<1` and `b>0`, every row has a strictly positive one-step regeneration probability. Hence `rho(K)<1` on an open strict residual set, including points outside the one-site theorem. This answers the weak “is it ever <1?” question positively, but that fact by itself is not the desired mechanism.

The Perron root is

$$
\boxed{
\rho(K)=
\frac{1-a-2b+2c+
\sqrt{(1-a)^2+4b(1-c)}}{4}.}
$$

Solving `(I-K)h=x`, with denominator

$$
D=ab-ac+2a+b^2-bc+2b+c^2-3c+2,
$$

gives

$$
\boxed{
h_0=
\frac{ab-ac+2a-b^2+2bc-2b}{D},}
$$

$$
\boxed{
h_1=
\frac{a+2bc-b-c^2+c}{D}.}
$$

Now suppose the fully agreed block is `11` and the exterior pair is `01`. A designated boundary update at site `1` compares the parameters `c=r10` and `d=r11=0`. It creates the transient state `S1=(1;10)` with probability `c`; otherwise the block remains agreed. Thus the exact one-attack crossing factor is

$$
\boxed{
F_2(a,b,c)
=c\,h_1
=
\frac{c(a+2bc-b-c^2+c)}
{ab-ac+2a+b^2-bc+2b+c^2-3c+2}.}
$$

Copy-label exchange gives the same factor for exterior orientation `10`.

## 5. Sharp two-site failure approaching East

Insert

$$
a=\varepsilon,
\qquad
b=\frac\varepsilon2,
\qquad
c=1-\varepsilon^2.
$$

Then

$$
\boxed{
\rho_2(\varepsilon)
=
\frac{3-2\varepsilon-2\varepsilon^2+
\sqrt{(1-\varepsilon)^2+2\varepsilon^3}}{4}.}
$$

Its expansion is

$$
\rho_2(\varepsilon)
=1-\frac34\varepsilon-\frac12\varepsilon^2+O(\varepsilon^3).
$$

For the entry state `S1`,

$$
\boxed{
h_1(\varepsilon)
=
\frac{2(3+2\varepsilon-2\varepsilon^2-2\varepsilon^3)}
{6+7\varepsilon+6\varepsilon^2+4\varepsilon^3}.}
$$

Hence

$$
h_1(\varepsilon)
=1-\frac12\varepsilon-\frac{13}{12}\varepsilon^2+O(\varepsilon^3).
$$

The boundary attack succeeds with probability `c=1-epsilon^2`, so

$$
\boxed{
F_2(\varepsilon)
=
\frac{2(1-\varepsilon^2)(3+2\varepsilon-2\varepsilon^2-2\varepsilon^3)}
{6+7\varepsilon+6\varepsilon^2+4\varepsilon^3}.}
$$

Therefore

$$
F_2(\varepsilon)
=1-\frac12\varepsilon-\frac{25}{12}\varepsilon^2+O(\varepsilon^3)
\longrightarrow1.
$$

Exact verifier values include

$$
F_2(1/10)=\frac{157311}{169100}\approx0.9302838557,
$$

$$
F_2(1/100)
=\frac{15097480101}{15176510000}
\approx0.9947926171.
$$

This is a sharp negative for a two-site wall: the contraction margin collapses linearly in the noise scale along a path that remains strictly unresolved by the existing theorems.

## 6. The exact local cycle at the East limit

At `epsilon=0`, the limiting transition rule is

$$
r_{00}=r_{01}=r_{11}=0,
\qquad
r_{10}=1.
$$

Equivalently, the updated value is `1` exactly in local environment `10`.

Take exterior disagreement `01` and a fully agreed two-site block `11`. The boundary update at the right site sends

$$
(11;01)\longrightarrow (11;10)
$$

deterministically: the first copy sees environment `10` and the second sees `11`.

From `(11;10)`, every right-site update preserves the disagreement `10`. The next left-site update compares environments `11` and `10`, hence sends the left coupled pair to `01` deterministically. Crossing therefore occurs before any regeneration.

This is the local reason for

$$
\rho_2(\varepsilon)\to1,
\qquad
F_2(\varepsilon)\to1.
$$

## 7. Persistence check: the obstruction does **not** automatically extend to length three

The proof spine explicitly asked whether the length-two obstruction obviously persists for every fixed block length. It does not.

There is already a qualitative difference at length three. At the exact East rule, after a disagreement enters the rightmost site of an all-one agreed block, the middle site must update before a premature update of the left site can freeze that left site into a common zero. This introduces an ordering obstruction absent at length two.

Because the East-limit chain is singular, that heuristic ordering probability alone is **not** the correct small-noise limit: failed orderings can enter metastable states that are eventually released by rare noise. Therefore I did not infer the length-three factor from the corner dynamics. I constructed the full exact symbolic killed chain.

For length three, the transient state space consists of all triples of coupled-site pairs for which

1. the leftmost pair is diagonal, and
2. at least one of the three sites is off-diagonal.

There are exactly

$$
2\cdot4\cdot4-2^3=24
$$

transient states. At each embedded update one of the three block sites is selected with probability `1/3`; the same canonical kernel `kappa` gives the new coupled-site pair. Crossing and regeneration are defined exactly as for length two.

Along the same strict residual path, exact symbolic elimination of the 24-state system gives the following conditional crossing limits after a successful right-boundary entry with orientation `10`, for the four fully agreed blocks whose rightmost common state is `1`:

$$
001:\quad \frac{43}{75},
$$

$$
011:\quad \frac45,
$$

$$
101:\quad \frac{19}{30},
$$

$$
111:\quad \frac9{10}.
$$

If the rightmost common state is `0`, the boundary-entry probability itself is

$$
r_{00}-r_{01}=\frac\varepsilon2\to0,
$$

so those one-attack factors vanish. The opposite exterior orientation gives the same values after exchanging the two coupled copies. Consequently

$$
\boxed{
\lim_{\varepsilon\downarrow0}R_3^{\mathrm{adv}}(\varepsilon)=\frac9{10}.}
$$

The symbolic verifier constructs the 24-state operator from the canonical coupling and checks these limits exactly. No floating-point spectral calculation is used for this statement.

This refutes the inference

> length two tends to one near East, therefore every fixed finite wall does.

It does **not** prove that length three works throughout the residual region, nor that a block-renewal argument can be concatenated in the infinite system. It establishes only that the two-site local cycle is not a structural all-fixed-length obstruction.

## 8. What this means for the proof spine

### E1: one-site wall

No change except calibration is now checked directly against the source convention. The residual path above lies strictly outside both the 2025 covered region and the 2026 one-site criterion.

### E2: two-site falsification test

Mark **negative near East**.

The exact killed operator is now known. On a strict unresolved path,

$$
\rho_2(\varepsilon)\to1,
\qquad
F_2(\varepsilon)\to1.
$$

A two-site agreed block has no East-stable contraction margin.

### E4: proposed structural obstruction

Do **not** promote the proposed statement that the same cycle persists for every fixed block length. The length-three exact persistence check contradicts that inference on the same path:

$$
R_3^{\mathrm{adv}}(\varepsilon)\to9/10.
$$

Thus E4, as presently motivated by the length-two cycle, should be replaced rather than strengthened.

### New unresolved edge suggested

The next question should be structural rather than “compute length four”:

> For the exact length-three killed operator, characterize the supremal adversarial crossing/regeneration factor over the entire residual noisy-East region and over every asymptotic approach to the East boundary. Is its limsup strictly below one?

If yes, the Professor should then formulate and audit the missing block-renewal/concatenation theorem that turns such a local factor into decay of disagreements. If no, the bad asymptotic path should identify the next genuine obstruction.

Under the standing novelty standard, simply obtaining a better numerical region from the 24-state operator is not a project result.

## 9. Verification files

- `research/active/noisy-east-positive-rates/students/student-c/001-two-site-wall-verifier.py`
  - standard-library exact rational construction of the four-state/two-state killed chain;
  - checks `K 1 + x + y = 1` exactly;
  - solves `(I-K)h=x` over `Fraction`;
  - checks the closed two-site formulas on `epsilon=1/10,1/100,1/1000`.

- `research/active/noisy-east-positive-rates/students/student-c/001-three-site-east-limit.py`
  - exact SymPy construction of the 24-state length-three killed operator along the strict residual path;
  - exact symbolic solution of `(I-K)h=x`;
  - verifies the four nonvanishing East-limit crossing probabilities `43/75, 4/5, 19/30, 9/10` and the adversarial limit `9/10`.

## 10. Status boundary

Established by exact derivation in this note and executable verification:

- the exact two-site killed operator;
- the closed two-state formulas in the ordered residual wedge;
- the strict unresolved path;
- `rho_2(epsilon)->1` and `F_2(epsilon)->1` on that path;
- the exact 24-state length-three diagnostic and its `9/10` adversarial limit on the same path.

Not established:

- ergodicity anywhere new;
- a global block-renewal theorem;
- uniform length-three contraction throughout the full residual region;
- impossibility of parameter-dependent or longer agreed blocks;
- a project-level novelty claim for the finite-state calculations themselves.

The length-three diagnostic is included because it changes the scientific conclusion of the assigned falsification test: the Professor should reject length two, but should **not** infer from it that the finite-wall mechanism as a whole is structurally dead.
