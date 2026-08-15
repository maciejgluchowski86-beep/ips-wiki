# Professor verification: two-site failure and length-three persistence diagnostic

Date: 2026-08-15

Source under review: `students/student-c/001-two-site-wall.md` and its two verifier scripts.

This note records an independent Professor reconstruction of the two load-bearing calculations used for the first noisy-East direction decision. The calculations below were rebuilt from the canonical coupling rather than inferred from Student C's closed forms.

## 1. Two-site killed excursion

Use the residual path

$$
r_{11}=0,\qquad
r_{10}=1-\varepsilon^2,\qquad
r_{01}=\frac\varepsilon2,\qquad
r_{00}=\varepsilon,
\qquad 0<\varepsilon<\frac12.
$$

For a two-site agreed block with a frozen exterior disagreement, the transient states have the protected/left site diagonal and the boundary/right site off-diagonal. With exterior orientation `01`, the orientation-`10` subsystem

$$
S_0=(0;10),\qquad S_1=(1;10)
$$

is closed. Writing generally

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},\qquad r_{11}=0,
$$

with `c>a>=b`, direct canonical-coupling enumeration gives

$$
K=rac12
\begin{pmatrix}
1-a+c-b & b\\
1-c & c-b
\end{pmatrix},
$$

and crossing vector

$$
x=rac12
\begin{pmatrix}a-b\\c\end{pmatrix}.
$$

The larger eigenvalue of this matrix is

$$
\rho(K)=
\frac{1-a-2b+2c+\sqrt{(1-a)^2+4b(1-c)}}4.
$$

I also independently enumerated the full four-state transient kernel. Along the path above, this eigenvalue is the Perron root of the full killed kernel, not merely of the closed subsystem. Substitution gives

$$
\rho_2(\varepsilon)
=
\frac{3-2\varepsilon-2\varepsilon^2+
\sqrt{(1-\varepsilon)^2+2\varepsilon^3}}4
=1-\frac34\varepsilon-\frac12\varepsilon^2+O(\varepsilon^3),
$$

hence

$$
\rho_2(\varepsilon)\to1.
$$

Solving

$$
(I-K)h=x
$$

gives for the entry state `S_1`

$$
h_1=
\frac{a+2bc-b-c^2+c}
{ab-ac+2a+b^2-bc+2b+c^2-3c+2}.
$$

Starting from the fully agreed block `11`, the designated boundary attack against exterior `01` enters `S_1` with probability `c`. Therefore

$$
F_2=c h_1.
$$

On the residual path,

$$
F_2(\varepsilon)
=
\frac{2(1-\varepsilon^2)(3+2\varepsilon-2\varepsilon^2-2\varepsilon^3)}
{6+7\varepsilon+6\varepsilon^2+4\varepsilon^3}
=1-\frac12\varepsilon-\frac{25}{12}\varepsilon^2+O(\varepsilon^3),
$$

so

$$
F_2(\varepsilon)\to1.
$$

The fully agreed block `11` is also the worst one-attack state along this path for small `epsilon`; exchanging the two copies gives the same value for the opposite exterior orientation.

## 2. Deterministic East-limit mechanism

At `epsilon=0`,

$$
r_{10}=1,
\qquad
r_{00}=r_{01}=r_{11}=0.
$$

Thus an updated site becomes `1` exactly in local environment `10`.

Start from a fully agreed two-site block `11` with exterior disagreement `01`. A boundary update at the right block site compares environments `10` and `11`, hence creates disagreement orientation `10` deterministically. While the right block site updates, the two environments are `10` and `01`, so the disagreement remains. When the protected left site next updates, its two copies see environments `11` and `10`, hence its coupled pair becomes `01` deterministically. Crossing has occurred before regeneration.

This is the exact local mechanism behind both limits to one.

## 3. Independent length-three reconstruction

I rebuilt the full length-three killed embedded chain along the same path. A transient state is a triple of coupled-site pairs such that the protected leftmost pair is diagonal and at least one block pair is off-diagonal. There are

$$
2\cdot4\cdot4-2^3=24
$$

such states. At each embedded block update, one of the three sites is selected with probability `1/3`; crossing absorbs when site zero becomes off-diagonal, and regeneration absorbs when all three block sites are diagonal.

For exterior orientation `01`, exact symbolic solution of the independently reconstructed system gives, conditional on a successful boundary attack of orientation `10`, the following limits for the four fully agreed words whose rightmost common bit is `1`:

$$
001:\ \frac{43}{75},\qquad
011:\ \frac45,\qquad
101:\ \frac{19}{30},\qquad
111:\ \frac9{10}.
$$

For the four fully agreed words whose rightmost common bit is `0`, the attack probability is

$$
|r_{00}-r_{01}|=\frac\varepsilon2,
$$

so their unconditional one-attack crossing factors tend to zero.

I separately reconstructed the operator with exterior orientation `10`. Its four nonvanishing limits are again

$$
\frac{43}{75},\quad\frac45,\quad\frac{19}{30},\quad\frac9{10},
$$

as also follows from exact copy-label exchange symmetry of the canonical coupling. Thus the adversary genuinely ranges over all eight fully agreed three-site words and both exterior disagreement orientations, and

$$
\boxed{
\lim_{\varepsilon\downarrow0}R_3^{\rm adv}(\varepsilon)=\frac9{10}.
}
$$

The maximizer is the all-one word `111` for either exterior orientation.

## 4. Status boundary

The two-site conclusion is a verified diagnostic negative: length two has no contraction margin stable along this genuine residual approach to East.

The length-three calculation refutes the proposed inference that the same local cycle automatically forces every fixed block length to have limiting factor one. It does **not** prove a length-three wall theorem, uniform contraction throughout the residual parameter region, or a concatenation theorem for the infinite IPS.

Under the standing novelty standard, neither finite-state computation is a project result. Their role is to determine whether there is enough structural evidence to spend one further block on a regime-wide characterization of the finite-wall mechanism.