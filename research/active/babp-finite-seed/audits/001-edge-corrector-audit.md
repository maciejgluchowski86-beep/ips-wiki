# Independent audit 001: BABP edge corrector

Date: 2026-08-15

Role: fresh independent auditor. I did not use the Professor's acceptance of the claim as mathematical evidence. I rederived the edge generator from the BABP transition rules, independently decoded and evaluated the committed rational certificate, independently rebuilt the `k=8` linear programme, and separately checked the accessible primary historical record.

## Executive verdict

The mathematical core of `BABP-EDGE-001` survives the hostile audit.

At

$$
\lambda=\frac1{40},\qquad k=10,
$$

the committed certificate really does define a bounded rational corrector `phi` for which every one of the `2^{11}=2048` possible edge-window/exterior-bit states has generator drift at least

$$
\frac{1033}{40000000}=0.000025825>0.
$$

The edge-window generator encoded by the certificate is the correct generator for

$$
H(B)=R(B)+\phi(u(B))
$$

under the convention in the audit request. One unresolved bit beyond the ten-site window is sufficient. No event class is missing.

Uniform drift gives, for every finite nonempty initial state,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge \frac{1033}{40000000}
\qquad\text{a.s.}
$$

and by reflection

$$
\limsup_{t\to\infty}\frac{L(B_t)}t
\le -\frac{1033}{40000000}
\qquad\text{a.s.}
$$

There is no hidden factor depending on the total number of particles. The full finite-particle chain is nonexplosive, and the martingale associated with `H` has bounded jumps and predictable quadratic variation `O(t)` with a constant depending only on `k`, `lambda`, and `phi`.

A terminology qualification is necessary. The argument above proves a strictly positive **lower asymptotic edge velocity** in the displayed `liminf/limsup` sense. It does not by itself prove that `R(B_t)/t` or `L(B_t)/t` has a limit. If the phrase “asymptotic speed” is intended to assert existence of those limits, that stronger wording is not established by this certificate alone. The claim registry should state the displayed `liminf/limsup` conclusion unless an independent speed-existence theorem is cited.

The `k=1` strict-feasibility threshold is exactly `lambda>1/3`. A fresh `k=8` LP implementation places the zero crossing at

```text
0.0346195434755...
```

and changes sign between `0.03461954` and `0.03461955`, so the numerical calibration `0.03461954...` is correct to the requested precision.

The historical identification is weaker. The accessible primary Sudbury (1999) record directly says that finite-seed convergence is extended from the old `1/3` range to `lambda >= 0.0347` and that edge-speed bounds are obtained; the paper is explicitly titled *Hunting submartingales ...* and is indexed with keyword `submartingale`. However, the full body was not accessible through Cambridge Core: the nominal PDF URL redirects to the abstract/access page. I therefore cannot verify that Sudbury literally used the identical finite-window LP, the identical normalization, or an eight-site window. The numerical coincidence at `k=8`, together with the exact `k=1` calibration and Sudbury's contemporaneous finite-boundary computational methodology, is strong evidence, but it remains inference rather than a source-verified identity.

Finally, this audit does **not** promote a finite-seed convergence theorem at `lambda=1/40`. The verified result is a positive finite-window edge-drift/ballistic-edge statement. Until the separate edge-speed-to-local-convergence bridge is proved, it is misleading to describe the present result as a strict improvement of Sudbury's published **convergence theorem**. It is a strict improvement below `0.0347` of the finite-window edge certificate and of the resulting ballistic-edge bound.

## 1. Fresh derivation of the edge-window generator

### 1.1 BABP transition rule

For a finite occupied set `B subset Z`, let

$$
N_x(B)=\mathbf 1_{\{x-1\in B\}}+\mathbf 1_{\{x+1\in B\}}.
$$

The requested convention is the single-site flip chain

$$
0\to1\text{ at rate }\lambda N_x(B),
\qquad
1\to0\text{ at rate }N_x(B).
$$

If `B` is nonempty and finite, write `R=max B`. Fix `k>=1` and define

$$
u_j=\mathbf 1_{\{R-j\in B\}},\qquad j=1,\ldots,k,
$$

and

$$
z=\mathbf 1_{\{R-k-1\in B\}}.
$$

Let `u=(u_1,...,u_k)` and

$$
H(B)=R+\phi(u).
$$

I now enumerate transitions from the particle rules, rather than starting from the formula in the student note.

### 1.2 Birth at `R+1`

Because `R` is the rightmost particle, `R+1` is vacant, has occupied left neighbour `R`, and has vacant right neighbour `R+2`. Hence the flip rate is exactly `lambda`.

After the flip the edge is `R+1`; the old edge becomes the first occupied site behind it. Therefore

$$
T_+u=(1,u_1,\ldots,u_{k-1}),
$$

and

$$
\Delta H=1+\phi(T_+u)-\phi(u).
$$

Contribution:

$$
\lambda\bigl[1+\phi(T_+u)-\phi(u)\bigr].
$$

### 1.3 Death of the rightmost particle

The site `R` has no occupied neighbour to its right. Its only possible occupied neighbour is `R-1`, with indicator `u_1`. Thus the death rate of `R` is exactly `u_1`.

If `u_1=1`, then after the death of `R` the new right edge is `R-1`. The new `k`-word is

$$
T_-^z u=(u_2,\ldots,u_k,z).
$$

Hence

$$
\Delta H=-1+\phi(T_-^z u)-\phi(u),
$$

and the contribution is

$$
u_1\bigl[-1+\phi(T_-^z u)-\phi(u)\bigr].
$$

If `u_1=0`, the rightmost particle has no occupied neighbour and cannot die, so there is no missing “edge jump across a gap” event.

### 1.4 Flips inside the recorded window

For `j=1,...,k`, the site `R-j` has neighbour indicators

$$
u_{j-1},\qquad u_{j+1},
$$

where I set

$$
u_0=1,\qquad u_{k+1}=z.
$$

Thus

$$
n_j^z(u)=u_{j-1}+u_{j+1}.
$$

If `u_j=0`, the flip rate is `lambda n_j^z(u)`; if `u_j=1`, it is `n_j^z(u)`. Equivalently the rate is

$$
n_j^z(u)\,[\lambda(1-u_j)+u_j].
$$

The right edge does not move. If `u^{(j)}` is obtained by flipping bit `j`, then

$$
\Delta H=\phi(u^{(j)})-\phi(u).
$$

Summing these contributions gives

$$
\sum_{j=1}^k n_j^z(u)[\lambda(1-u_j)+u_j]
[\phi(u^{(j)})-\phi(u)].
$$

### 1.5 Why one exterior bit is enough

The site `R-k-1` itself can flip, and its rate can depend on `R-k-2`. But such a flip changes neither `R` nor the recorded word `u`, hence it has `Delta H=0` and contributes zero to the generator of `H`. Sites farther left also have `Delta H=0`; sites farther right than `R+1` cannot flip because they have no occupied neighbour.

The bit `z` is needed only for two current effects:

1. it is the left neighbour needed to compute the flip rate of recorded site `R-k`;
2. it becomes the last recorded bit when the right edge dies and shifts one step left.

No second exterior bit is needed to evaluate the instantaneous generator. Future flips of `z` merely move the process between the two already-enumerated values `z=0,1`; uniformity over both values handles that future evolution.

### 1.6 Resulting generator

The complete drift is therefore

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda[1+\phi(T_+u)-\phi(u)]\\
&+u_1[-1+\phi(T_-^zu)-\phi(u)]\\
&+\sum_{j=1}^k n_j^z(u)[\lambda(1-u_j)+u_j]
[\phi(u^{(j)})-\phi(u)].
\end{aligned}
$$

This agrees with the committed implementation, but the event enumeration above is independent of it.

A bookkeeping point worth making explicit: when `u_1=1`, an adjacent pair `(R-1,R)` yields two distinct directed death transitions under the requested convention. Death of `R` is the edge-death term; death of `R-1` is the `j=1` internal-flip term. Both are present.

## 2. Uniform positive drift implies ballistic edge motion

### 2.1 The finite-particle process is nonexplosive

Let `N=|B|`. The total birth rate is at most `2 lambda N`: each occupied site has at most two occupied-vacant oriented edges on which it can create a birth. The total death rate is at most `2N`: each occupied site has at most two occupied neighbours that can kill it. Hence the total jump rate satisfies

$$
q(B)\le 2(1+\lambda)|B|.
$$

Each jump changes `|B|` by exactly one. Starting from `N_0<infinity`, after `m` jumps the particle count is at most `N_0+m`, so the chain is dominated for explosion purposes by a Yule pure-birth chain with linear rate `2(1+lambda)n`. That chain is nonexplosive because the sum of reciprocal rates is a divergent harmonic series. Thus the BABP remains a well-defined finite set at every finite time.

The empty state cannot be reached from a nonempty finite state: a singleton has no occupied neighbour and therefore has zero death rate.

### 2.2 The martingale has bounds independent of total particle number

For fixed `k`, only the following sites can change `H` in one jump:

- `R+1`;
- `R`;
- the `k` sites `R-1,...,R-k`.

Each internal recorded site has flip rate at most `2 max(1,lambda)`. Consequently the total rate of `H`-changing jumps is bounded uniformly in the entire particle configuration by, for example,

$$
C_0=\lambda+1+2k\max(1,\lambda).
$$

Because `phi` is a function on a finite state space, it is bounded. Every jump of `H` is bounded by

$$
1+\operatorname{osc}(\phi).
$$

After standard localization, Dynkin's formula gives the martingale

$$
M_t=H(B_t)-H(B_0)-\int_0^t \mathcal LH(B_s)\,ds.
$$

Its predictable quadratic variation satisfies

$$
\langle M\rangle_t\le C_1 t
$$

for a deterministic `C_1=C_1(k,lambda,phi)`, with no dependence on `|B_t|`. The bounded-jump martingale strong law therefore gives

$$
\frac{M_t}{t}\longrightarrow0
\qquad\text{a.s.}
$$

### 2.3 Consequence of the certificate

If

$$
\mathcal LH(B)=D_{k,\lambda}(u,z;\phi)\ge v>0
$$

for all `(u,z)`, then

$$
H(B_t)\ge H(B_0)+vt+M_t.
$$

Dividing by `t`, using `M_t/t -> 0`, and using boundedness of `phi`, gives

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v
\qquad\text{a.s.}
$$

Reflection of the entire graphical construction gives

$$
\limsup_{t\to\infty}\frac{L(B_t)}t\le -v
\qquad\text{a.s.}
$$

Both probability-one statements can of course be intersected. This establishes positive two-sided outward linear motion. It does not establish existence of the limits `R(B_t)/t` and `L(B_t)/t` without an additional theorem.

## 3. Independent analytic `k=1` calculation

Set

$$
\phi(0)=0,\qquad \phi(1)=a.
$$

Fresh event enumeration gives the four boundary states.

For `(u,z)=(0,0)`, the edge birth contributes `lambda(1+a)` and the vacant recorded site is born at rate `lambda`, changing the corrector by `a`. Thus

$$
D(0,0)=\lambda(1+2a).
$$

For `(u,z)=(0,1)`, the recorded vacant site has two occupied neighbours, so

$$
D(0,1)=\lambda(1+3a).
$$

For `u=1`, the edge birth leaves the one-bit word equal to `1`, the right-edge death and internal death terms together give the same total for either `z`, and

$$
D(1,0)=D(1,1)=\lambda-1-2a.
$$

Uniform strict positivity requires

$$
a>-\frac13
$$

(the `a>-1/2` condition from the first inequality is weaker) and

$$
a< -\frac{1-\lambda}{2}.
$$

The interval is nonempty exactly when

$$
-\frac13<-\frac{1-\lambda}{2},
$$

i.e.

$$
\lambda>\frac13.
$$

At `lambda=1/3`, strict positivity is impossible. Therefore the `k=1` strict-feasibility threshold is exactly `lambda>1/3`.

## 4. Independent exact audit of the `k=10`, `lambda=1/40` certificate

I did not call the committed `drift` routine for this check. I independently decoded the payload and independently evaluated the physical-event formula above.

### 4.1 Decompression and state ordering

The committed payload has 3657 Base85 characters. Decoding with `base64.b85decode`, then `zlib.decompress`, gives exactly 4096 bytes. Interpreting those bytes as

```text
<1024i
```

produces exactly 1024 little-endian signed 32-bit numerators. Dividing by `10^6` gives the rational corrector values. The first value, corresponding to the all-zero state, is exactly zero, so the intended additive gauge is present.

For an independent indexing check, I did not reuse the certificate's dictionary. I used

$$
\operatorname{index}(u_1,\ldots,u_{10})
=\sum_{j=1}^{10}u_j2^{10-j}.
$$

This is exactly the ordering generated by Python's

```text
itertools.product((0,1), repeat=10)
```

with the last bit varying fastest. Hence numerator number `i` is attached to the state the verifier intends.

Transfer-integrity hashes of the audited payload are:

```text
SHA256(Base85 payload)
94ceb1b75280595a84303980a09e98b76a500108f4d9f338138408fcb5a3eb90

SHA256(decompressed 4096 bytes)
425268d4706653361278088a389204fda4bb0ea0dab7a078424b17dde519c9be
```

The integer numerators range from `-982257` to `0`; there are 1023 distinct numerator values. Thus the corrector is bounded (in fact contained in `[-0.982257,0]`).

### 4.2 All 2048 inequalities

I evaluated all

$$
2^{10}\times2=2048
$$

pairs `(u,z)` using `fractions.Fraction` and the independently derived event formula. Every drift is strictly positive.

The unique minimum is

$$
\frac{1033}{40000000}=0.000025825
$$

at

```text
u = (0,1,1,1,1,1,0,0,1,1)
z = 1
```

exactly as reported. The second-smallest exact drift in my ordering is

$$
\frac{17}{625000}=0.0000272,
$$

so the reported minimum is not a tie or an ordering artifact.

This check covers the payload decompression, integer unpacking, denominator, state order, physical generator encoding, and all 2048 exact inequalities.

## 5. Independent `k=8` zero-drift calibration

I separately built the `k=8` LP from the fresh event enumeration in Section 1. I fixed `phi(0^8)=0`, used the other 255 corrector values and the scalar `v` as free variables, and imposed all 512 inequalities

$$
D_{8,\lambda}(u,z;\phi)\ge v.
$$

The objective was to maximize `v`. This implementation did not import the student's LP or the `k=10` certificate.

Using SciPy 1.17.0 / HiGHS, I obtained:

```text
lambda          optimal v_8(lambda)
0.0346          -4.1686153218e-7
0.0346194       -3.0620410750e-9
0.0346195       -9.2785201895e-10
0.03461954      -7.4174089770e-11
0.03461955      +1.3924629828e-10
0.0347          +1.7210899003e-6
```

Bisection on the zero crossing gives

```text
0.03461954347549849...
```

and all three HiGHS modes (`highs`, `highs-ds`, `highs-ipm`) agreed on the sign near the crossing. On the negative side at `lambda=0.0346194`, the numerical dual has 256 positive weights, total weight `1+O(10^-15)`, cancellation residual about `2.4e-16`, and weighted constant about `-3.06e-9`. On the positive side, rounding an independently optimized corrector at `lambda=0.0346196` to denominator `10^12` and reevaluating with exact rational arithmetic still gives a positive minimum `3/2500000000 = 1.2e-9`.

Because the negative-side dual was not rationalized exactly, I regard the last digits as a high-accuracy **numerical** LP determination, not an exact symbolic theorem about `lambda_8`. That is nevertheless enough for the audit request: the claimed `0.03461954...` calibration is reproduced independently and the sign change occurs in the stated eighth-decimal neighbourhood. A coarse scan from `lambda=0` to `0.0346` found no earlier positive-feasibility island; `v_8(0)=0` and the optimum is negative throughout the sampled positive range before the displayed crossing.

## 6. Historical-source audit

### 6.1 What the primary accessible record proves

The primary Cambridge Core record for Aidan Sudbury,

*Hunting submartingales in the jumping voter model and the biased annihilating branching process*, Advances in Applied Probability 31 (1999), 839--854, DOI `10.1239/aap/1029955207`,

states in its abstract that, for one-dimensional BABP from a finite nonzero initial configuration, the known convergence range is extended from the old `1/3` range to

$$
\lambda\ge0.0347,
$$

and it explicitly states that bounds on the edge speed are obtained. The article title and the publisher's keyword list explicitly identify `submartingale` as a central method.

The earlier Neuhauser--Sudbury (1993) primary record describes the model as particles placing offspring on empty neighbouring sites at rate `lambda` and destroying neighbours at rate 1, consistent with the directed single-site convention audited above. Mountford's 1993 abstract states the finite-particle convergence theorem for parameter `>1/3`.

I also found Sudbury's contemporaneous paper *A method for finding bounds on critical values for non-attractive interacting particle systems* (Journal of Physics A, 1998, pp. 8323--8331). Its public abstract describes a computer search for a function with a sign-controlled expectation by enumerating all relevant `0/1` configurations near the boundary of a finite one-dimensional process, including computations to a fixed number of sites from the boundary. This supports the general finite-boundary computational methodology, but it is not a substitute for the missing body of the 1999 BABP paper.

### 6.2 What I could not verify

The Cambridge “PDF” endpoint for the 1999 paper redirects to the abstract/access page and states that full-version access is required. JSTOR identifies the article and page range but did not expose the body through the available interface. I did not find an author-hosted or repository full text.

Therefore I cannot source-verify any of the following literal historical claims:

- that Sudbury's BABP calculation used exactly the observable `R+phi(u)` in the normalization above;
- that his state variable was literally the first eight bits behind the edge plus one exterior bit;
- that the internal numerical computation was exactly the present 512-inequality `k=8` LP;
- that no additional boundary reduction or altered state encoding was used.

### 6.3 Strength of the inference

The inference is unusually strong but still an inference:

1. the fresh one-site calculation gives the old strict-feasibility boundary `lambda>1/3` exactly;
2. the fresh eight-site LP gives `0.0346195434755...`, which is the published `0.0347` number at the quoted precision;
3. the 1999 paper is explicitly about hunting submartingales and says it obtains edge-speed bounds while extending the BABP convergence range;
4. Sudbury's contemporaneous methodological work explicitly uses finite-boundary state enumeration and computer-searched drift functions.

This is enough to say that the present construction is very plausibly reconstructing Sudbury's threshold mechanism at a conceptual level. It is **not** enough to say that the historical calculation was literally an eight-site window unless the full 1999 text (or independent archival evidence) is obtained.

Historical identification verdict: **PARTIAL -- mechanism-level identification strongly supported; literal `k=8` equivalence unverified.**

## 7. Claim boundary and recommended wording

What is verified by this audit:

- the finite-window generator formula in the requested BABP convention;
- sufficiency of one unresolved exterior bit;
- nonexplosion of the finite-seed process;
- bounded jump/rate estimates for the `H` martingale independent of total particle number;
- `M_t/t -> 0` almost surely and therefore the stated `liminf/limsup` ballistic edge bounds;
- exact `k=1` strict feasibility iff `lambda>1/3`;
- exact positivity of every committed `k=10`, `lambda=1/40` inequality and exact minimum `1033/40000000`;
- independent numerical reproduction of the `k=8` zero crossing `0.0346195434755...`.

What is **not** verified by this audit:

- existence of limits `R(B_t)/t` and `L(B_t)/t` from the corrector argument alone;
- finite-seed local convergence at `lambda=1/40`;
- the edge-speed-to-convergence bridge;
- a theorem that the finite-window thresholds tend to zero;
- literal identification of Sudbury's 1999 computation with an eight-site window.

For promotion of `BABP-EDGE-001`, I recommend replacing the potentially ambiguous phrase “strictly positive outward asymptotic speeds” by the exact conclusion

$$
\liminf_{t\to\infty}R(B_t)/t\ge1033/40000000,
\qquad
\limsup_{t\to\infty}L(B_t)/t\le-1033/40000000
\quad\text{a.s.}
$$

for every finite nonempty initial configuration.

With that precise interpretation, the central project claim is correct.

Historical identification verdict: **PARTIAL**.

VERIFIED
