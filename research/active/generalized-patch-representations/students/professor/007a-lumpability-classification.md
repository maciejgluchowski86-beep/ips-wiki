# 007a: lumpability classification

Date: 2026-08-17

This note executes Part A of Assignment 007.

## 1. Reference-neighbour physical chain

Write the physical one-site generator, with every neighbour frozen in the reference state, as

\[
Q(x,y)=q_{xy}\quad(x\ne y),
\qquad
Q(x,x)=-\sum_{y\ne x}q_{xy}.
\]

The partition under consideration is

\[
\mathcal L=\{\{0\},\{1,2\}\}.
\]

For a continuous-time Markov chain, strong lumpability with respect to this partition requires that states in the active block have the same total rate to the other block. Hence

\[
\boxed{q_{10}=q_{20}=:d.}
\tag{1.1}
\]

There is no second condition: for an active state the total rate to the active block is then automatically the negative of the common rate to state 0, and the singleton block gives no compatibility condition.

The quotient generator on states `0,A` is

\[
\bar Q=
\begin{pmatrix}
-c&c\\
d&-d
\end{pmatrix},
\qquad
c=q_{01}+q_{02}.
\tag{1.2}
\]

## 2. Which patch value functions lump

For an outgoing coefficient row

\[
p=(p_0,p_1,p_2),
\]

Assignment 005 identifies the remaining `OI` numerator with

\[
N_b(t)=E_b[g(Z_t)],
\qquad
 g=(g_0,g_1,g_2)
=(p_0,p_0+p_1,p_0+p_2).
\tag{2.1}
\]

The function `g` descends to the two-block quotient exactly when it is constant on the active block:

\[
g_1=g_2
\iff
\boxed{p_1=p_2.}
\tag{2.2}
\]

When (1.1) and (2.2) both hold, write the quotient values as `g_0,g_A`. Then for either active initial type

\[
N_b(t)
=\bar L+(g_A-\bar L)e^{-(c+d)t},
\tag{2.3}
\]

where

\[
\bar L=\frac{d g_0+c g_A}{c+d}
\]

when `c+d>0`. The degenerate case is constant. Thus, inside the class in which every relevant outgoing row satisfies (2.2), all-time `OI` positivity is equivalent to its zero-length and long-time endpoint inequalities.

## 3. Honesty classification

The simplification in (2.3) is **binary-reducible** in the precise sense prohibited by Part D of Assignment 007. Both the dynamics relevant to the observable and the observable itself factor through the quotient `0/A`. The hidden distinction between active states cannot affect any tested numerator.

Therefore this is not the desired genuinely multi-state simplification.

## 4. Dynamic lumpability alone does not remove the second mode

Condition (1.1) by itself does not force (2.2). The exact symmetric example used in the next note makes this explicit. Take

\[
Q=
\begin{pmatrix}
-2&1&1\\
2&-2&0\\
2&0&-2
\end{pmatrix}.
\tag{4.1}
\]

It is lumpable because `q_10=q_20=2`. Its nonzero decay rates are `2` and `4`: the active-type contrast decays at rate `2`, while the quotient contrast decays at rate `4`.

For

\[
g=(-4/5,1/20,39/20),
\tag{4.2}
\]

which corresponds to

\[
p=(-4/5,17/20,11/4),
\tag{4.3}
\]

one has `g_1,g_2>0` but `g_1 != g_2`. Starting from active type 1,

\[
N_1(t)
=\frac1{10}-\frac{19}{20}e^{-2t}+\frac9{10}e^{-4t}.
\tag{4.4}
\]

Writing `x=e^{-2t}`, the unique interior minimum occurs at

\[
x_*=\frac{19}{36}
\]

and equals

\[
N_1(t_*)=-\frac{217}{1440}<0,
\tag{4.5}
\]

although `N_1(0)=1/20>0` and `N_1(infinity)=1/10>0`.

The next note embeds this row into a fully active-type-symmetric one-neighbour physical IPS. Thus lumpability of the chain alone does not simplify the exact criterion.
