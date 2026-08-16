# Student F 002: regional insertion positivity and its two-cell failure

## Verdict

The minimal nontrivial scaffold cell can be integrated exactly. With the predecessor interaction type fixed to be source-retaining, so that there is genuinely a left branch, the resulting companion factor is nonnegative and separates from the current source region. Thus the one-cell insertion step is valid after the already proved source burn-in.

However, this positivity does **not** survive composition when the predecessor interaction is itself treated as the hidden successful interaction of the preceding cell. The exact two-cell transfer contains

\[
\Psi_\Delta(z)=B K_\Delta(z)-c,
\]

where `K_Delta` is a one-site zero-boundary `L^-` semigroup. For every residual parameter point,

\[
\Psi_\Delta(0)<0
\]

for all sufficiently short positive cell lengths `Delta`. A second, older cell can simultaneously be beyond the verified burn-in and have positive transfer. Their product is then strictly negative.

Hence the principal's old route does not admit a cellwise regional-insertion iteration in the form tested at Meeting 001. The failure is not the old raw-Duhamel left dependence: the scaffold integration removes that dependence on one cell. The failure occurs one step later, when the preceding successful type is also hidden and the source-retention branch is too young for its zero-boundary transfer to reach the insertion threshold.

A concrete counterexample occurs at

\[
(a,b,c)=\left(\frac1{10},\frac3{10},\frac45\right)\in\mathcal R,
\]

with a predecessor-cell length `Delta=0.1` and a preceding source-cell length `u=20`.

## 1. Notation

Work in the complemented canonical spin convention of Assignment 001. Put

\[
d=b-a,
\qquad
k=1-c,
\qquad
B=b+c-a=d+c,
\qquad
\rho=\frac cB.
\tag{1.1}
\]

Throughout the residual chamber,

\[
d>0,
\qquad
k>0,
\qquad
0<\rho<1.
\]

The noise-reduced process `L^-` has local canonical-spin rates

\[
\begin{array}{c|cc}
\eta_{i+1} & 0\to1 & 1\to0\\ \hline
0 & 1 & d\\
1 & k & 0.
\end{array}
\tag{1.2}
\]

A successful rightward dual interaction has two hidden types:

- source retained, signed coefficient `+B`;
- source removed, signed coefficient `-c`.

Thus, before any regional continuation is inserted, hiding its type gives

\[
B\eta_i-c=B(\eta_i-\rho).
\tag{1.3}
\]

The Professor has independently verified (1.3) and the conditional estimate

\[
\mathbb E^-[(B\eta_i(t)-c)F]\ge0
\tag{1.4}
\]

for nonnegative right-history-measurable `F` after

\[
T_\rho
=
\frac1k\log\frac{B}{dk}.
\tag{1.5}
\]

The identity between (1.5) and the formula in Assignment 001 uses
`d=b-a` and `k=1-c`.

## 2. The minimal scaffold cell

Translate the cell so that the current revealed successful interaction is

\[
q=(i,s): i\longrightarrow i+1,
\]

and its predecessor is

\[
p=(i-1,r): i-1\longrightarrow i,
\qquad r<s.
\]

Write

\[
\Delta=s-r.
\]

The predecessor relation certifies two facts relevant to the left branch:

1. the interaction at `p` makes dual site `i` active;
2. no later successful interaction crosses `i-1 -> i` during `(r,s]`.

For the genuinely nontrivial one-cell test, fix the predecessor type at `p` to be source-retaining. Then the source `i-1` remains as a left branch immediately after `r`. The certifying absence edge between `i-1` and the forced-active tube at `i` kills this branch at the first later successful nonempty-target crossing through that edge.

All other marks in this left white region are integrated out.

This is exactly the confined-interaction situation from the canonical patch paper: killing the signed dual on a successful crossing through the edge is dual to the spin process with canonical zero boundary at `i`.

The zero boundary, rather than boundary one, is important. It comes from the **absence edge** on the left side of the forced-active tube. The other side of the forced tube carries the boundary-one rule from Assignment 001, Section 4. These two boundaries should not be interchanged.

## 3. Exact one-site regional kernel

Let `z in {0,1}` be the canonical spin at `i-1` at the lower end of the left region. The retained predecessor branch contributes the probability-weighted kernel

\[
K_\Delta(z)
=
(P_{\Delta}^{-,0}\eta_{i-1})(z),
\tag{3.1}
\]

where the superscript `0` denotes the zero boundary at site `i`.

By (1.2), this is the two-state chain

\[
0\xrightarrow{1}1,
\qquad
1\xrightarrow{d}0.
\]

Therefore

\[
\boxed{
K_\Delta(z)
=
\frac1{1+d}
+
\left(z-\frac1{1+d}\right)e^{-(1+d)\Delta}.
}
\tag{3.2}
\]

In particular,

\[
K_\Delta(0)
=
\frac{1-e^{-(1+d)\Delta}}{1+d},
\qquad
K_\Delta(1)
=
\frac{1+d e^{-(1+d)\Delta}}{1+d}.
\tag{3.3}
\]

Both are strictly positive for `Delta>0`, and `K_0(1)=1`, `K_0(0)=0`.

### Direct dual derivation

Formula (3.2) can also be read directly from the signed dual, which is useful for checking that no conditioning normalizer has been lost.

Suppose the predecessor is source-retaining. While its source branch remains active, a successful birth or jump through the absence edge is forbidden. Empty-target death at rate one is allowed. The `L^-` Feynman--Kac potential on this active branch is `2c`, while the total active-site dual jump rate is `1+B+c`. Hence the probability-weighted contribution of a death at age `u` is

\[
e^{-(1+B+c)u}e^{2cu}\,du
=
e^{-(1+d)u}\,du,
\]

because `1+B-c=1+d`. If no mark acts before `Delta`, the terminal active branch contributes `z`. Thus

\[
\int_0^\Delta e^{-(1+d)u}\,du
+z e^{-(1+d)\Delta},
\]

which is exactly (3.2).

So `K_Delta` is the **unnormalized probability-weighted regional contribution**. If one conditions further on the geometric cell, a positive conditional-probability denominator appears. It has no effect on any sign conclusion below.

## 4. One-cell insertion positivity passes

Keep the current interaction `q=(i,s)` type hidden, but keep the predecessor `p` source-retaining so the cell has a genuine left branch.

After the left white region is integrated out, its complete contribution is the nonnegative scalar

\[
K_\Delta(z_{i-1}).
\]

The scaffold conditional-independence split separates this scalar from the graphical randomness in the source/right region of `q`. Consequently, for deterministic initial configuration, the hidden current-type contribution has the form

\[
K_\Delta(z_{i-1})
\,\mathbb E^-[(B\eta_i-c)R],
\tag{4.1}
\]

where `R` is the remaining nonnegative right-region companion factor. The same statement for an arbitrary initial law follows by integrating the pointwise statement over its initial configuration.

Thus the left predecessor branch does **not** create the raw-Duhamel obstruction after the minimal regional marks are summed. The left factor has become a scalar regional kernel.

If the source/right part has had the burn-in required in Assignment 001, then (1.4) gives

\[
K_\Delta(z_{i-1})
\,\mathbb E^-[(B\eta_i-c)R]
\ge0.
\tag{4.2}
\]

This proves the one-cell insertion test for every `Delta>=0`.

This is a genuine improvement over the ungrouped Duhamel calculation: the first-order factor `c+B eta_{i-1}` found in Assignment 001 is replaced, after the actual scaffold absence cell is integrated, by the positive Markov kernel `K_Delta`.

## 5. What changes under composition

To compose two consecutive scaffold cells, the predecessor `p` cannot remain artificially fixed to be source-retaining. It is itself the hidden successful interaction of the preceding cell.

Both hidden types make the target `i` active, so the **same predecessor geometry** and forced-active tube occur in either case. But the source-side continuation is different:

- if `p` is source-retaining, coefficient `+B`, the left branch is present and contributes `K_Delta(z)`;
- if `p` is source-removing, coefficient `-c`, the left branch is absent and the certifying no-crossing statement above `p` is automatic, so its left contribution is `1`.

Therefore, after the predecessor type is hidden, the exact probability-weighted transfer passed from the preceding cell into the current cell is

\[
\boxed{
\Psi_\Delta(z)
=
B K_\Delta(z)-c.
}
\tag{5.1}
\]

This is the load-bearing two-cell formula.

There is no missing normalization in (5.1). If the scaffold geometry is normalized to a conditional law, the denominator is the positive unsigned probability density of that geometry. The sign is still the sign of (5.1).

Using `rho=c/B`, (5.1) is

\[
\Psi_\Delta(z)
=
B\bigl(K_\Delta(z)-\rho\bigr).
\tag{5.2}
\]

Thus the regional transfer asks whether the retained-source zero-boundary kernel has relaxed past exactly the same insertion threshold `rho` found in Assignment 001.

## 6. Short cells have the wrong sign

The worst lower spin is `z=0`. By (3.3),

\[
\Psi_\Delta(0)
=
\frac{B}{1+d}
\left(1-e^{-(1+d)\Delta}\right)-c.
\tag{6.1}
\]

At zero length,

\[
\Psi_0(0)=-c<0.
\]

The unique zero occurs when

\[
e^{-(1+d)\Delta}
=
1-\frac{c(1+d)}B.
\]

The right side simplifies exactly:

\[
B-c(1+d)
=d+c-c-cd
=d(1-c)
=dk.
\]

Hence define

\[
\boxed{
\tau_*
=
\frac1{1+d}
\log\frac{B}{dk}.
}
\tag{6.2}
\]

Then

\[
\boxed{
\Psi_\Delta(0)<0
\quad\Longleftrightarrow\quad
0\le\Delta<\tau_*.
}
\tag{6.3}
\]

Since `d,k>0` and `B=d+c>d`, one has `B/(dk)>1`, so `tau_*>0` throughout the residual chamber.

Compare this with the Professor-verified one-site source burn-in

\[
T_\rho
=
\frac1k\log\frac{B}{dk}.
\tag{6.4}
\]

Because `1+d>k`,

\[
0<\tau_*<T_\rho.
\tag{6.5}
\]

Thus a scaffold can contain simultaneously:

- an older source region that has already passed the insertion burn-in;
- an immediately preceding predecessor cell of length less than `tau_*` whose hidden transfer has the opposite sign.

The scaffold definition imposes no lower bound on consecutive predecessor time gaps, so such cells cannot be excluded geometrically.

## 7. Explicit residual counterexample

Take

\[
\boxed{
(a,b,c)
=
\left(\frac1{10},\frac3{10},\frac45\right).
}
\tag{7.1}
\]

This lies strictly in the live residual chamber:

\[
0<\frac1{10}<\frac3{10},
\qquad
\frac45\ge\frac12,
\qquad
\frac45>\frac1{10}+\frac3{10},
\]

and

\[
\frac3{10}
>
\sqrt2\left(1-\frac45\right)
=
\frac{\sqrt2}{5}.
\]

Here

\[
d=\frac15,
\qquad
k=\frac15,
\qquad
B=1,
\qquad
\rho=\frac45,
\qquad
1+d=\frac65.
\tag{7.2}
\]

Therefore

\[
\tau_*
=
\frac56\log 25
\approx2.6823965207,
\tag{7.3}
\]

while

\[
T_\rho
=5\log25
\approx16.0943791243.
\tag{7.4}
\]

Choose a short predecessor cell

\[
\Delta=0.1.
\]

With lower spin `z=0`,

\[
K_{0.1}(0)
=
\frac56\left(1-e^{-0.12}\right)
\approx0.0942329694,
\]

so

\[
\boxed{
\Psi_{0.1}(0)
\approx-0.7057670306<0.
}
\tag{7.5}
\]

Now choose a preceding source cell with the same zero-boundary kernel, lower spin zero, and length

\[
u=20>T_\rho.
\]

Then

\[
K_{20}(0)
=
\frac56\left(1-e^{-24}\right)
\approx0.8333333333,
\]

and hence

\[
\boxed{
\Psi_{20}(0)
\approx0.0333333333>0.
}
\tag{7.6}
\]

The two consecutive hidden-cell transfer has the product

\[
\boxed{
\Psi_{20}(0)\Psi_{0.1}(0)
\approx-0.0235255677<0.
}
\tag{7.7}
\]

All omitted scaffold-region factors can be chosen positive and are independent under the revealed split. Thus the composed regional companion has the wrong sign even though the older source cell is strictly beyond the verified one-site burn-in.

The supporting script

`students/student-f/002-regional-insertion-verifier.py`

checks the residual inequalities and the numerical values in (7.3)--(7.7) directly from the closed formulas. No Monte Carlo or numerical matrix exponential is used.

## 8. Why this is not a zero-probability-conditioning artifact

The scaffold is naturally described by interaction-time densities, as in the patch factorization construction. Equations (3.2) and (5.1) are probability-weighted kernels before division by any Janossy/conditional normalizer.

Moreover, the inequalities in the counterexample are strict. Therefore there are open intervals of predecessor gaps around `0.1` and source-cell lengths around `20` on which the signs remain respectively negative and positive. The corresponding Poisson timing events have positive probability density and positive probability after thickening the time windows.

So the failure is a genuine regional sign failure, not conditioning on a single null-time event.

## 9. What exactly has been falsified

The one-cell calculation shows that the scaffold grouping does repair the first issue from Assignment 001:

\[
\text{raw left-dependent Duhamel factor}
\quad\longrightarrow\quad
\text{positive one-site regional kernel }K_\Delta.
\]

But the predecessor interaction that created that left branch is itself signed. Once its type is hidden, the transfer is not `K_Delta`; it is

\[
B K_\Delta-c.
\]

That transfer changes sign at the positive time `tau_*`. Consecutive scaffold cells have arbitrarily small time gaps, so the sign cannot be propagated cell by cell from the one-cell insertion lemma.

Therefore the following proposed mechanism is false:

> reveal the scaffold geometry, hide each successful birth/jump type, integrate the adjacent region, obtain a nonnegative insertion-preserving cell, and iterate these cells along the predecessor trail.

The failure occurs already at two-cell composition and at a strict residual parameter point.

This does **not** prove that every possible coarser regrouping of several signed cells fails. In particular, a future method could in principle sum over short-cell clusters before asking for a sign. But such a cluster cancellation would be a new mechanism, not the cellwise regional insertion route assigned here.

## 10. Anti-circularity / research delta

### Previous live statement

Meeting 001 left one finite question: does the minimal scaffold grouping convert the hidden interaction into an insertion-positive regional kernel, and does that property compose?

### One-way result

The exact finite kernel is (3.2). One cell with a genuinely retained predecessor branch is positive after regional integration, so the raw Duhamel left-dependence is not itself fatal.

### Material obstruction

When the predecessor is itself hidden for composition, the transfer is exactly (5.1), and it is negative on every short interval `0<Delta<tau_*` at lower spin zero. The explicit strict residual example (7.1)--(7.7) gives a negative two-cell product even with an older cell beyond `T_rho`.

### Why this is target-relevant rather than another representation

This is a falsifiable sign calculation on the exact regional object selected by the narrowed proof spine. It eliminates the proposed cellwise iteration. No invariant-measure or convergence statement was restated.

### What would have to be new after this

A continuation of the principal's old route would need a genuinely coarser mechanism that sums a random cluster of short predecessor cells before taking signs, with a quantitative cluster estimate. Merely renaming `Psi_Delta` or imposing the one-cell threshold on every cell cannot work because the scaffold has no minimum time spacing.

## Handoff

`one-cell works but composition fails at: hiding the predecessor type changes the positive retained-branch kernel K_Delta into the signed transfer Psi_Delta=B K_Delta-c; for every residual parameter point Psi_Delta(0)<0 on 0<Delta<tau_*=(1+b-a)^{-1} log((b+c-a)/((b-a)(1-c))), and at (a,b,c)=(1/10,3/10,4/5) the consecutive lengths 20 and 0.1 give Psi_20(0)>0 but Psi_0.1(0)<0, so the two-cell regional product is strictly negative.`
