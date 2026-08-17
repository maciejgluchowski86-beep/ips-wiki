# Student G 012a: exact Boolean random-map and ancestry polytope

## Result

At the hard point

$$
P_h=(a,b,c)=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

the exact continuous-time random-map decompositions of the local generator project to the following ancestry-rate polytope. Write

- `d` for the aggregate rate of constant maps;
- `s` for nontrivial self-only maps;
- `j` for right-only maps;
- `r` for genuinely two-parent maps.

After discarding the global identity map, the attainable set is exactly the set of nonnegative `(d,s,j,r)` satisfying

$$
\begin{aligned}
d&\ge0,\qquad s\ge0,\qquad j\ge0,\\
j+r&\ge \frac{9999}{10000},\\
d+r&\ge \frac{9999}{10000},\\
d+s+j+r&\ge1,\\
d+2s+j&\le\frac1{5000},\\
2d+4s+2j+r&\le\frac{5051}{5000}.
\end{aligned}
\tag{P}
$$

The exact verifier `012a-random-map-polytope-verifier.py` enumerates all 40 basic feasible decompositions of the 15 nonidentity Boolean maps, projects them to 26 ancestry points, and verifies that `(P)` has exactly 11 vertices, each realized by an exact random-map decomposition. Thus `(P)` is an exact H-description, not a numerical hull fit.

Two immediate consequences are

$$
\boxed{d_{\max}=a+(1-c)=\frac1{5000}}
$$

and, subject to maximal death,

$$
\boxed{r_{\min}=c=\frac{9999}{10000}}.
$$

Hence every maximal-oblivious-death representation still branches at rate essentially one.

The canonical four-mark decomposition is an ancestry vertex but is not lexicographically optimal. Its ancestry rates are

$$
(d,s,j,r)
=\left(\frac1{5000},0,0,\frac{5049}{5000}\right).
$$

Replacing the OR mark by XOR and reducing the `x AND (NOT y)` rate gives the strict improvement

$$
(d,s,j,r)
=\left(\frac1{5000},0,0,\frac{9999}{10000}\right).
$$

This matters for the bounded pair experiment, but the first-moment branching rate remains only diagnostic.

## 1. Exact local decomposition constraints

Index a Boolean map by its truth table

$$
F=(F_{00},F_{01},F_{10},F_{11})\in\{0,1\}^4.
$$

Let `q_F>=0` be its Poisson rate. Since applying `F` at input `(x,y)` flips the spin exactly when `F_{xy}\ne x`, exact reproduction of the spin generator is equivalent to

$$
\boxed{
\sum_{F:F_{00}=1}q_F=a,
\qquad
\sum_{F:F_{01}=1}q_F=b,
}
$$

$$
\boxed{
\sum_{F:F_{10}=0}q_F=1-c,
\qquad
\sum_{F:F_{11}=0}q_F=1.
}
\tag{1}
$$

The identity map `(0,0,1,1)` has zero flip vector and may be discarded. Every other map has positive cost in at least one equation, so the feasible polytope is bounded.

The 15 remaining maps split by essential parent set as follows:

- two constants, parent set `emptyset`;
- one nontrivial self-only map, `NOT x`;
- two right-only maps, `y` and `NOT y`;
- ten genuinely two-parent maps.

For the mark-only backward support process, only these four classes matter.

## 2. Why the inequalities in `(P)` are necessary

The three nonnegativity inequalities are immediate.

For every map which is constant or self-only, the flip indicators at inputs `10` and `11` agree. Therefore the difference

$$
\lambda_{11}-\lambda_{10}=1-(1-c)=c
$$

must be carried by maps depending on the right parent. Hence

$$
j+r\ge c.
$$

At the hard point `1-a=c`. For self-only and right-only maps the flip-indicator difference between `11` and `00` is zero, while a constant or two-parent map contributes at most one to that difference. Thus

$$
d+r\ge \lambda_{11}-\lambda_{00}=1-a=c.
$$

Every nonidentity mark can flip input `11` at most once, while the total required flip rate there is one, so

$$
d+s+j+r\ge1.
$$

Now sum the required flip rates at inputs `00` and `10`:

$$
\lambda_{00}+\lambda_{10}=a+(1-c)=\frac1{5000}.
$$

A constant mark contributes exactly one to this two-input flip count, `NOT x` contributes two, and a right-only mark contributes exactly one. Two-parent contributions are nonnegative. Therefore

$$
d+2s+j\le\frac1{5000}.
$$

Finally sum all four required flip rates:

$$
a+b+(1-c)+1=\frac{5051}{5000}.
$$

Constants flip exactly two inputs, `NOT x` flips four, right-only maps flip two, and every genuinely two-parent nonidentity map flips at least one. Hence

$$
2d+4s+2j+r\le\frac{5051}{5000}.
$$

The exact vertex enumeration in the verifier proves these necessary inequalities are also sufficient at `P_h`.

## 3. Canonical versus lexicographic optimizer

Put

$$
g=b-a=\frac{99}{10000}.
$$

The canonical decomposition is

- constant `1` (`1111`) at rate `a`;
- constant `0` (`0000`) at rate `1-c`;
- `x OR y` (`0111`) at rate `g`;
- `x AND (NOT y)` (`0010`) at rate `c`.

It gives

$$
d=a+1-c=\frac1{5000},
\qquad
r=c+g=\frac{5049}{5000}.
$$

Since each constant rate is bounded by the corresponding smallest flip rate, no representation can have `d>a+1-c`; thus this already maximizes oblivious death.

With those two constant rates saturated, the residual flip vector is

$$
(0,g,0,c).
$$

Use instead

- XOR (`0110`) at rate `g`;
- `x AND (NOT y)` (`0010`) at rate `c-g`.

Both are two-parent maps and their flip vectors sum to the residual vector. This gives

$$
r=g+(c-g)=c.
$$

The facet `d+r>=c` shows this is minimal among maximal-death representations.

## 4. Exact ancestry vertices to test

The 11 vertices of `(P)` are

$$
\begin{array}{c|c|c|c}
d&s&j&r\\ \hline
0&0&0&1\\
0&0&0&5051/5000\\
0&0&1/10000&9999/10000\\
0&0&1/5000&9999/10000\\
0&0&1/5000&5049/5000\\
0&1/10000&0&9999/10000\\
0&1/10000&0&5049/5000\\
1/10000&0&0&9999/10000\\
1/10000&0&1/10000&4999/5000\\
1/5000&0&0&9999/10000\\
1/5000&0&0&5049/5000
\end{array}
$$

Self-only marks do not change backward supports, but their rate is retained in the polytope because spending flip budget on them changes the feasible `(d,j,r)` values. The bounded pair-support experiment must therefore test all 11 projected vertices, not only the maximal-death optimizer.

## 5. Backward-support generator

For any feasible ancestry point, self-only marks may be omitted from support dynamics. For a finite set `A` of active ancestors and bounded `f`,

$$
\boxed{
\begin{aligned}
\mathcal G f(A)
={}&\sum_{i\in A} d\,[f(A\setminus\{i\})-f(A)]\\
&+\sum_{i\in A} j\,[f((A\setminus\{i\})\cup\{i+1\})-f(A)]\\
&+\sum_{i\in A} r\,[f(A\cup\{i+1\})-f(A)].
\end{aligned}
}
\tag{2}
$$

Duplicate ancestors are merged automatically by the set union. Thus the minimal mark-only support is a one-sided branching/jumping/coalescing finite-set process with death rate `d`, right-jump rate `j`, and right-branch rate `r` per active site.

For two independent histories `(A,A')`, the pair generator is

$$
\mathcal G^{(2)}=\mathcal G\otimes I+I\otimes\mathcal G.
$$

The Assignment-012 observable is

$$
\Psi(A,A')=2^{|A\cap A'|}-1.
$$

The next checkpoint tests this pair process. No conclusion is drawn from the fact that the one-copy branching rate is large.
