# Student G Assignment 012 handoff

## Status

`STOP-PAIR-OBSTRUCTION`

Assignment 012 is complete under its pre-registered stop rule. No full proof architecture is reopened.

Main report:

- `students/student-g/012-information-percolation-pair-history.md`, commit `26a3e1a80cb7ceafe0d35891e51f1cee6b14b8af`.

No toolbox-branch file, `docs/` file, or `mkdocs.yml` was edited.

## Decisive result

At

$$
P_h=\left(\frac1{10000},\frac1{100},\frac{9999}{10000}\right),
$$

the exact random-map ancestry polytope forces every admissible deterministic-Boolean decomposition to satisfy

$$
d+j\le\frac1{5000},
\qquad
r\ge\frac{4999}{5000},
$$

where `d` is oblivious death, `j` is right-only ancestry motion, and `r` is genuine two-parent branching.

For two independent backward supports started from `{0}`, a width-one block event of duration `T=8` retains a common site and creates its right neighbor in both copies. Uniformly over the entire ancestry polytope, the bad-cell probability is less than

$$
\frac{18483379}{2500000000}<\frac1{128}.
$$

These good cells are independent between time layers and one-dependent in space. A direct bad-cut Peierls estimate gives a positive-probability infinite oriented common-ancestor cluster. Consequently

$$
\boxed{
\inf_{n\ge0}
\mathbb E\left[2^{|A_{8n}\cap A'_{8n}|}-1\right]
>\frac1{121}.
}
$$

Thus the Assignment-012 pair observable itself cannot decay for any admissible Boolean-map decomposition at the hard point.

This is not a first-moment argument, common-coupling survival statement, tail-shift statement, or finite-box boundary artifact. It directly satisfies the assignment's strong-negative criterion.

## Exact ancestry polytope

The local generator constraints are

$$
\sum_{F:F_{00}=1}q_F=a,
\quad
\sum_{F:F_{01}=1}q_F=b,
\quad
\sum_{F:F_{10}=0}q_F=1-c,
\quad
\sum_{F:F_{11}=0}q_F=1.
$$

After classifying the 15 nonidentity Boolean maps by essential parent set, the exact projected polytope at `P_h` is

$$
\begin{aligned}
d,s,j&\ge0,\\
j+r&\ge9999/10000,\\
d+r&\ge9999/10000,\\
d+s+j+r&\ge1,\\
d+2s+j&\le1/5000,\\
2d+4s+2j+r&\le5051/5000.
\end{aligned}
$$

The exact verifier enumerates 40 basic feasible decompositions and proves this H-description has 11 realized vertices.

The canonical four-mark decomposition is extremal but improvable for ancestry. It has

$$
(d,s,j,r)=(1/5000,0,0,5049/5000).
$$

Maximizing death and then minimizing branching instead uses XOR at rate `b-a` and `x AND (NOT y)` at rate `c-(b-a)`, giving

$$
(d,s,j,r)=(1/5000,0,0,9999/10000).
$$

The pair obstruction is uniform over both of these and every other feasible decomposition.

## Why widths 2--8 were not run

The assignment allowed exceeding the preferred finite calculation only if a structural recursion was discovered. Here the decisive recursion occurs already at width one and is an honest lower process in the untruncated infinite history system. Larger-width finite matrices cannot reverse the positive survival theorem and would add computation without information.

Therefore I stopped rather than producing a favourable-boundary `UNRESOLVED-BOUNDED` calculation.

## Scope boundary

This kills the **mark-only minimal-support process defined in Assignment 012**, for every exact decomposition into deterministic Boolean maps at `P_h`.

It does not prove nonergodicity of the spin system. It also does not rule out a genuinely different state-adaptive reveal process which conditions on discovered spin values and then prunes a globally essential parent. Such a process is not the support generator tested here and would need a new bridge statement before research restarts.

## Durable commits

- ancestry-polytope verifier — `ad1b1d62be1638cb035bb2b8bfb03d47a544223c`;
- ancestry-polytope report — `c26558a88a23fc6b57f92e6c65c23d0350718071`;
- initial pair scalar verifier — `fd4d4ca2eac90d52c37a6a0cde46a42c2517cdf6`;
- strengthened pair scalar verifier — `514028666825266bfe20ddb586e96f0285bb7c01`;
- initial analytic pair obstruction — `3f4706601a5cf8841510f8ede9d39b65aab9f8b1`;
- tightened analytic pair obstruction — `99d108e252d0b3f2b17f73f18ee56e90e57c2c21`;
- notation-clean analytic checkpoint — `4246ac01cd3a0c0d8c2b967fa0b4c2601da39bd0`;
- final report — `26a3e1a80cb7ceafe0d35891e51f1cee6b14b8af`.

The two exact verifier scripts were also independently reconstructed/run during the assignment; all asserted rational identities passed.
