---
title: Patch positivity property
status: proved here
audit: current
tags:
  - duality
  - spin systems
  - patch
  - positivity
---

# Patch positivity property

A spin system is **patch positive** when

$$
C(P)\ge0
$$

for every possible full [patch](patch.md) shape $P$. The canonical paper gives an exact criterion in terms of the multilinear coefficients of the two flip rates.

Put

$$
r_i=c_i^0(\varnothing)+c_i^1(\varnothing).
$$

## Theorem: coefficient criterion

At every site $i$ with $r_i=0$, patch positivity holds exactly when

$$
c_i\equiv0.
\tag{1}
$$

At every site with $r_i>0$, patch positivity holds exactly when, for each nonempty $S\subseteq N(i)$,

$$
c_i^0(S)+c_i^1(S)\le0,
\tag{2}
$$

and

$$
c_i^1(\varnothing)c_i^0(S)
\ge
c_i^0(\varnothing)c_i^1(S).
\tag{3}
$$

## Proof

Fix a site $i$ and use the full-patch formulas from [patch contribution](patch-contribution.md). The contributions of patches beginning with an incoming interaction are

$$
C(P)
=
\begin{cases}
\displaystyle\frac{\psi_i(\Delta,1)}{\varphi_i(\Delta)},
&\mathsf X(P)\mathsf Y(P)\in\{\mathsf{II},\mathsf{IE}\},\\[1.1em]
e^{V_i\Delta},
&\mathsf X(P)\mathsf Y(P)=\mathsf{IO}.
\end{cases}
$$

Both are nonnegative. Thus only patches beginning with an outgoing successful interaction impose restrictions.

Let $P$ begin outgoing with nonempty target $S$. For a patch of type $\mathsf{OO}$,

$$
C(P)=\sigma_i^\beta(S)e^{V_i\Delta},
$$

while

$$
\beta_i(S)\sigma_i^\beta(S)
=-c_i^0(S)-c_i^1(S).
$$

Hence all $\mathsf{OO}$ contributions are nonnegative exactly when (2) holds.

For a patch of type $\mathsf{OI}$ or $\mathsf{OE}$, the denominator in the contribution formula is positive on every realized patch. Its numerator is

$$
N_{i,S}(\Delta)
=
c_i^0(S)
-
\bigl(c_i^0(S)+c_i^1(S)\bigr)\psi_i(\Delta,1).
\tag{4}
$$

### The case $r_i=0$

If $r_i=0$, then $\psi_i(\Delta,1)=1$, so (4) becomes

$$
N_{i,S}(\Delta)=-c_i^1(S).
$$

Nonnegativity for every nonempty $S$ gives

$$
c_i^1(S)\le0.
$$

Since $c_i^1(\varnothing)=0$ and $c_i^1(\eta)\ge0$ as an actual flip rate, the multilinear expansion forces $c_i^1\equiv0$. Indeed, every nonconstant coefficient is nonpositive, so adding $1$'s to a neighbourhood can only decrease the function from its value $0$ at the empty neighbourhood; nonnegativity then leaves only the zero function.

Condition (2) now gives $c_i^0(S)\le0$ for every nonempty $S$. Again $c_i^0(\varnothing)=0$ and $c_i^0\ge0$, so $c_i^0\equiv0$. Thus patch positivity forces $c_i\equiv0$ when $r_i=0$.

Conversely, if $c_i\equiv0$, there are no outgoing interactions from $i$, and all incoming-initial contributions are nonnegative. This proves (1).

### The case $r_i>0$

Assume (2). The empty-neighbour relaxation formula is

$$
\psi_i(\Delta,1)
=
\frac{c_i^0(\varnothing)}{r_i}
+
\frac{c_i^1(\varnothing)}{r_i}e^{-r_i\Delta}.
\tag{5}
$$

Because $c_i^0(\varnothing),c_i^1(\varnothing)\ge0$, the function in (5) is nonincreasing in $\Delta$. Under (2),

$$
-c_i^0(S)-c_i^1(S)\ge0,
$$

so the numerator (4) is also nonincreasing in $\psi_i(\Delta,1)$ and therefore is minimized in the long-patch limit. Using (5),

$$
\lim_{\Delta\to\infty}N_{i,S}(\Delta)
=
\frac{
c_i^1(\varnothing)c_i^0(S)
-
c_i^0(\varnothing)c_i^1(S)
}{r_i}.
\tag{6}
$$

Thus $N_{i,S}(\Delta)\ge0$ for every patch length exactly when (3) holds. Combining the incoming cases, the $\mathsf{OO}$ case, and the $\mathsf{OI}/\mathsf{OE}$ cases proves the criterion.

## Corollary: monotonicity of local rates

Patch positivity implies that the functions $c_i^1$ and $c_i^0+c_i^1$ are coordinatewise nonincreasing as $1$'s are added to the neighbourhood of $i$.

### Proof

If $r_i=0$, then $c_i\equiv0$ and there is nothing to prove. Suppose $r_i>0$. By (2), every nonconstant coefficient of $c_i^0+c_i^1$ is nonpositive, so this function is coordinatewise nonincreasing.

It remains to show that every nonconstant coefficient of $c_i^1$ is nonpositive. If some nonempty $S$ satisfied $c_i^1(S)>0$, then (2) would imply $c_i^0(S)<0$. Since $c_i^0(\varnothing),c_i^1(\varnothing)\ge0$ and at least one is positive,

$$
c_i^1(\varnothing)c_i^0(S)
-
c_i^0(\varnothing)c_i^1(S)<0,
$$

contradicting (3). Hence $c_i^1(S)\le0$ for every nonempty $S$, which gives the claimed coordinatewise monotonicity.

For a fixed neighbourhood configuration with positive total flip intensity, the two rates can be viewed as a Bernoulli refresh with total intensity $c_i^0+c_i^1$ and calm-state probability $c_i^0/(c_i^0+c_i^1)$. Patch positivity therefore implies that replacing facilitating $0$-neighbours by calm $1$-neighbours cannot increase either the total local update intensity or the $1\to0$ transition rate. It does **not** imply that $c_i^0$ itself is monotone, and coordinatewise monotonicity alone is weaker than the coefficient criterion (2)-(3).

Patch positivity controls full-patch factors. Nonnegativity of end factors additionally depends on the terminal calm-state density and is encoded by the [patch threshold profile](patch-critical-density.md).
