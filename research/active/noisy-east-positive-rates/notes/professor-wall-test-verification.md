# Professor verification: assignment-001 wall diagnostics

Date: 2026-08-15

Source under review: `students/student-c/001-two-site-wall.md` and its two verifier scripts.

## Post-verification source correction

The finite-state calculations in this note were independently reconstructed correctly, but their parameter-path interpretation was wrong.

On the normalized face `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10}.
$$

Published Głuchowski--Menz (2025), Corollary 7.2, proves exponential ergodicity when `0<b<=a` under the corresponding order/positive-rate assumptions. Hence the path used here,

$$
a=\varepsilon,
\qquad b=\frac\varepsilon2,
\qquad c=1-\varepsilon^2,
$$

is already covered because `b<a`. Any earlier wording in this note calling it a genuine residual or unresolved path is retracted.

Assignment 002 subsequently reconstructed the true normalized unresolved set as

$$
\mathcal R=
\left\{
0<a<b,
\quad \frac12\le c<1,
\quad c\ge a+b,
\quad b\ge\sqrt2(1-c)
\right\}.
$$

See `notes/professor-uniform-three-site-review.md` for the source check and the target-relevant three-site analysis.

## 1. Two-site killed excursion on the assignment-001 path

With exterior orientation `01`, the orientation-`10` subsystem

$$
S_0=(0;10),\qquad S_1=(1;10)
$$

has transient kernel

$$
K=\frac12
\begin{pmatrix}
1-a+c-b & b\\
1-c & c-b
\end{pmatrix}
$$

and crossing vector

$$
x=\frac12
\begin{pmatrix}a-b\\c\end{pmatrix}.
$$

The larger eigenvalue is

$$
\rho(K)=
\frac{1-a-2b+2c+\sqrt{(1-a)^2+4b(1-c)}}4.
$$

Independent enumeration of the full four-state transient kernel confirms that on the path above this is its Perron root. Substitution gives

$$
\rho_2(\varepsilon)
=
\frac{3-2\varepsilon-2\varepsilon^2+
\sqrt{(1-\varepsilon)^2+2\varepsilon^3}}4
\longrightarrow1.
$$

Solving `(I-K)h=x` and multiplying by the boundary-attack probability gives

$$
F_2(\varepsilon)
=
\frac{2(1-\varepsilon^2)(3+2\varepsilon-2\varepsilon^2-2\varepsilon^3)}
{6+7\varepsilon+6\varepsilon^2+4\varepsilon^3}
\longrightarrow1.
$$

## 2. East-limit local mechanism

At `epsilon=0`,

$$
r_{10}=1,
\qquad
r_{00}=r_{01}=r_{11}=0.
$$

Starting from agreed `11` with exterior disagreement `01`, a boundary update creates disagreement orientation `10` deterministically. Boundary updates preserve it; the next protected-site update compares environments `11` and `10` and creates disagreement deterministically. This exactly explains the two limits to one.

## 3. Length-three diagnostic on the same path

The independently reconstructed 24-state length-three killed chain gives conditional limits

$$
001:\frac{43}{75},\qquad
011:\frac45,\qquad
101:\frac{19}{30},\qquad
111:\frac9{10}
$$

for the four agreed words ending in one. The four words ending in zero have vanishing attack probability. The opposite exterior orientation gives the same values, so

$$
R_3^{\rm adv}(\varepsilon)\to\frac9{10}.
$$

## 4. Correct status

The mathematics above remains a verified finite-state diagnostic. It does **not** establish failure of a two-site wall within the unresolved noisy-East set, because the chosen path was already covered by the 2025 theorem. Likewise the `9/10` value is not residual evidence.

The target-relevant replacement is assignment 002: on the true residual set the sharp East-boundary frozen-exterior three-site supremum is `5/6`, while repeated attacks show that the one-attack statistic does not concatenate. Those facts, not the assignment-001 path, control the programme's final direction decision.
