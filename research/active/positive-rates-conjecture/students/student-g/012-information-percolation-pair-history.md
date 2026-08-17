# Student G Assignment 012: optimized backward-history pair-intersection test

## Verdict

`STOP-PAIR-OBSTRUCTION`.

At the hard point

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

the exact Boolean random-map ancestry polytope forces every admissible mark-only backward-support process to have loss rate

$$
u=d+j\le\frac1{5000}
$$

and genuine two-parent branching rate

$$
r\ge\frac{4999}{5000}.
$$

For two independent histories, these inequalities produce a decomposition-independent width-one oriented lower cluster inside the intersection `A_t cap A'_t`. At block time `T=8`, a common site creates and retains two adjacent common sites with bad-cell probability strictly below `1/128`. The cell field is independent between time layers and one-dependent in space. An elementary bad-cut Peierls estimate gives positive-probability survival of the lower cluster. Consequently, from `A_0=A'_0={0}`,

$$
\boxed{
\inf_{n\ge0}
\mathbb E\left[2^{|A_{8n}\cap A'_{8n}|}-1\right]
>\frac1{121}.
}
$$

Thus the pair-intersection observable requested by Assignment 012 does not decay for **any** admissible deterministic-Boolean random-map decomposition at `P_h`. This is not a first-moment obstruction and uses no truncation boundary. It is the strong negative outcome contemplated in Part D of the assignment.

No full positive-rates proof architecture is reopened.

## A. Exact random-map and ancestry polytope

Let a deterministic local map have truth table

$$
F=(F_{00},F_{01},F_{10},F_{11})\in\{0,1\}^4
$$

and Poisson rate `q_F`. Exact reproduction of the local spin generator is equivalent to

$$
\sum_{F:F_{00}=1}q_F=a,
\qquad
\sum_{F:F_{01}=1}q_F=b,
$$

$$
\sum_{F:F_{10}=0}q_F=1-c,
\qquad
\sum_{F:F_{11}=0}q_F=1.
\tag{A.1}
$$

Discard the global identity map. The remaining 15 maps consist of two constants, one nontrivial self-only map, two right-only maps, and ten genuinely two-parent maps.

Write `(d,s,j,r)` for their aggregate rates by essential parent set. At `P_h`, the exact projected polytope is

$$
\begin{aligned}
d&\ge0,\qquad s\ge0,\qquad j\ge0,\\
j+r&\ge \frac{9999}{10000},\\
d+r&\ge \frac{9999}{10000},\\
d+s+j+r&\ge1,\\
d+2s+j&\le\frac1{5000},\\
2d+4s+2j+r&\le\frac{5051}{5000}.
\end{aligned}
\tag{A.2}
$$

The verifier `012a-random-map-polytope-verifier.py` proves this exactly by enumerating the 40 basic feasible decompositions, projecting them to 26 ancestry points, enumerating the vertices of `(A.2)`, and verifying that its 11 vertices are all realized by exact decompositions.

### Canonical decomposition

The four familiar marks are

- reset to `1` at rate `a`;
- reset to `0` at rate `1-c`;
- `x OR y` at rate `b-a`;
- `x AND (NOT y)` at rate `c`.

Their ancestry point is

$$
\left(d,s,j,r\right)
=
\left(\frac1{5000},0,0,\frac{5049}{5000}\right).
$$

It is an extreme point but is not lexicographically optimal.

### Maximal death and minimal branching

The maximum possible oblivious-death rate is

$$
d_{\max}=a+(1-c)=\frac1{5000}.
$$

Subject to this maximum, replace OR by XOR at rate

$$
g=b-a=\frac{99}{10000}
$$

and use `x AND (NOT y)` at rate `c-g`. This gives

$$
\left(d,s,j,r\right)
=
\left(\frac1{5000},0,0,\frac{9999}{10000}\right).
$$

The polytope facet `d+r>=c` proves this is the smallest possible branching rate among maximal-death decompositions.

The lexicographic optimizer is therefore genuinely better than the canonical decomposition for ancestry, but the improvement is far too small to change the pair-level conclusion.

## B. Exact backward-support generator

For a feasible ancestry point, self-only marks do not change support and may be omitted. For finite `A subset Z`,

$$
\begin{aligned}
\mathcal G f(A)
={}&\sum_{i\in A} d\,[f(A\setminus\{i\})-f(A)]\\
&+\sum_{i\in A} j\,[f((A\setminus\{i\})\cup\{i+1\})-f(A)]\\
&+\sum_{i\in A} r\,[f(A\cup\{i+1\})-f(A)].
\end{aligned}
\tag{B.1}
$$

Thus an ancestor dies at rate `d`, moves one step right at rate `j`, or branches to retain itself and add the right neighbor at rate `r`; collisions merge by set union.

For two independent copies,

$$
\mathcal G^{(2)}=\mathcal G\otimes I+I\otimes\mathcal G,
$$

and the assignment's observable is

$$
\Psi(A,A')=2^{|A\cap A'|}-1.
$$

No conclusion below uses `E|A_t|`.

## C. Pair-level obstruction

### C1. Uniform rates across the entire ancestry polytope

From `(A.2)`,

$$
\boxed{d+j\le\frac1{5000}.}
\tag{C.1}
$$

Also

$$
d+r\ge c,
\qquad
j+r\ge c.
$$

Since

$$
\min(d,j)\le\frac{d+j}{2}\le\frac1{10000},
$$

we get

$$
\boxed{r\ge c-\frac1{10000}=\frac{4999}{5000}.}
\tag{C.2}
$$

These inequalities hold for every feasible decomposition, not merely every ancestry vertex.

### C2. Width-one common-ancestor block

Run independent support histories `A_t,A'_t`. Set `T=8`. For site `i` and block `n`, declare `G_{i,n}` good when, in both copies during `[8n,8(n+1)]`,

1. no death or right-only mark occurs at either `i` or `i+1`;
2. at least one two-parent branch mark occurs at `i`.

If

$$
i\in A_{8n}\cap A'_{8n}
$$

and `G_{i,n}` occurs, then

$$
\boxed{\{i,i+1\}\subseteq A_{8(n+1)}\cap A'_{8(n+1)}.}
\tag{C.3}
$$

With `u=d+j`, `(C.1)`--`(C.2)` give

$$
\mathbb P(G_{i,n})
\ge e^{-4uT}(1-e^{-rT})^2.
$$

The exact scalar certificate `012b-pair-intersection-obstruction-verifier.py` uses

$$
e^{-4uT}>\frac{621}{625},
$$

and, because `rT>31/4` and the first twelve Taylor terms of `e^{31/4}` exceed `2000`,

$$
e^{-rT}<\frac1{2000}.
$$

Therefore

$$
\mathbb P(G_{i,n})
>
\frac{2481516621}{2500000000},
$$

so the bad-cell probability satisfies

$$
\boxed{q<\frac{18483379}{2500000000}<\frac1{128}.}
\tag{C.4}
$$

### C3. Oriented lower cluster

Define

$$
C_0=\{0\},
$$

$$
C_{n+1}
=
\bigcup_{i\in C_n:\,G_{i,n}}\{i,i+1\}.
\tag{C.5}
$$

The graphical cell implication gives

$$
\boxed{C_n\subseteq A_{8n}\cap A'_{8n}}
\tag{C.6}
$$

for every `n`.

The `G` field is independent across time layers. Inside one layer, cells with spatial indices at distance at least two are independent, so the field is one-dependent in space.

If the reached oriented cluster from `(0,0)` is finite, a finite bad vertex cut separates it from high time levels. A minimal cut can be traced by a non-backtracking planar contour. For length `m`, a conservative count gives at most

$$
2m\,3^m
$$

anchored candidate contours. On any fixed contour, at least half the bad cells can be chosen mutually independent, because dependence occurs only between horizontally adjacent cells in the same layer. Therefore a fixed length-`m` contour is bad with probability at most

$$
q^{m/2}.
$$

Since

$$
q<\frac1{128}<\left(\frac4{45}\right)^2,
$$

we have `3 sqrt(q)<4/15`, and hence

$$
\begin{aligned}
\mathbb P(\text{some finite bad cut})
&\le 2\sum_{m\ge1}m(3\sqrt q)^m\\
&<2\sum_{m\ge1}m\left(\frac4{15}\right)^m\\
&=\frac{120}{121}<1.
\end{aligned}
\tag{C.7}
$$

Thus the lower cluster has survival probability greater than `1/121`. On that event `C_n` is nonempty for every `n`; by `(C.6)` the two independent backward supports intersect at every block time. This proves

$$
\boxed{
\mathbb E\Psi(A_{8n},A'_{8n})>\frac1{121}
\quad\text{for every }n.
}
\tag{C.8}
$$

This is the required pair-level statement. It is strictly stronger than saying the expected ancestor number is supercritical.

## D. Stop-rule application

Assignment 012 asked for `STOP-PAIR-OBSTRUCTION` if there is a decomposition-independent lower bound preventing pair-intersection decay. Equation `(C.8)` is exactly such a bound.

The proof is not a favourable finite-box effect:

- it uses width one;
- no spatial truncation is imposed;
- escape to larger width only helps the true histories and is not killed;
- the lower oriented cluster iterates directly in the full infinite support process.

Therefore the `UNRESOLVED-BOUNDED` clause does not apply, and there is no reason to enlarge the calculation to widths `2,...,8`.

The obstruction also does not use any pre-existing stopped positive-rates object. It assumes neither ergodicity, common-coupling extinction, tail-shift agreement, nor Meeting 030's signed boundary-transmission estimate.

## What is and is not killed

Killed by this block: the specific **optimized mark-only deterministic-Boolean support-pair architecture** in Assignment 012. No admissible decomposition at `P_h` can have the required decay of

$$
2^{|A_t\cap A'_t|}-1.
$$

Not killed: a different information-reveal architecture which observes spin values and can dynamically short-circuit a globally essential parent after that value is known. Such a state-adaptive reveal process is not `(B.1)` and was outside Assignment 012. It would require a separately specified bridge and anti-circularity test before any restart.

This result also says nothing about nonergodicity of the spin system. It eliminates one sufficient information-percolation bridge at the hard point.

## Durable files

- exact ancestry-polytope verifier: `012a-random-map-polytope-verifier.py`, initial commit `ad1b1d6`;
- exact ancestry-polytope report: `012a-random-map-polytope.md`, commit `c26558a`;
- pair-obstruction scalar verifier: `012b-pair-intersection-obstruction-verifier.py`, strengthened at commit `5140286`;
- analytic pair obstruction: `012b-pair-intersection-obstruction.md`, corrected/tightened through commit `4246ac0`.
