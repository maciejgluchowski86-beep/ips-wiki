# Professor verification: patch transfer equals the E1 Markov semigroup

Date: 2026-08-15

Status: **verified for the strategic decision in Meeting 002**.

This note independently checks the load-bearing identification in Student A assignment 002. It does not rely on the first- or second-record heuristic.

## Finite-volume coefficient identity

Work first on a finite cycle `V`. For each `A subseteq V`, let

$$
e_A(\eta):=\chi_A^*(\eta)=\prod_{i\in A}(\eta(i)-p).
$$

The family `(e_B)_{B subseteq V}` is a basis of all real functions on `{0,1}^V`. Define the unique centered-basis coefficient matrix `K_t` by

$$
P_t e_A=\sum_{B\subseteq V}K_t(A,B)e_B.
\tag{1}
$$

The canonical patch representation computes the same semigroup `P_t`. For centered input one must first expand

$$
e_A=\sum_{C\subseteq A}(-p)^{|A\setminus C|}\chi_C,
\tag{2}
$$

apply the exact ordinary-monomial patch expansion to each `chi_C`, expand the affine terminal factors about `p`, and collect centered monomials. By uniqueness of the basis expansion, whatever coefficient matrix the complete patch calculation produces is exactly the `K_t` in (1). This is the bookkeeping correction recorded in Student A's clarification note.

The already verified E1 duality gives, on the same finite cycle,

$$
P_t e_A(\eta)
=
q^{|A|}\sum_{B\subseteq V}Q_t(A,B)q^{-|B|}e_B(\eta),
\tag{3}
$$

where `Q_t=e^{t\mathcal G}` is the Markov semigroup of the transformed neighbour-refresh process. Comparing the unique coefficients of the basis `(e_B)` in (1) and (3) yields

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B).
\tag{4}
$$

Hence

$$
\sum_B q^{|B|-|A|}K_t(A,B)
=
\sum_BQ_t(A,B)
=1.
\tag{5}
$$

This proves that the complete `h`-weighted centered coefficient transfer is conservative. No local decomposition of the exact patch formula can produce a strict contraction of this total transfer unless it uses extra information not present in the coefficient dynamics itself.

## Independent check of the weighted row sum

Equation (5) can be checked without E1. At the all-occupied configuration `mathbf 1`,

$$
e_B(\mathbf 1)=q^{|B|}.
$$

Hard FA-1f leaves `mathbf 1` absorbing, so

$$
P_t e_A(\mathbf 1)=e_A(\mathbf 1)=q^{|A|}.
$$

Evaluating (1) at `mathbf 1` gives precisely

$$
q^{|A|}=\sum_BK_t(A,B)q^{|B|},
$$

which is (5). This alone proves conservation of the weighted coefficient mass; E1 additionally identifies every coefficient with the Markov transition probability in (4).

## Boundary normalization issue

Student A's clarification correctly notes that the kernels called `k_s` and `k_c` in the first-composition calculation are `h`-normalized coefficient kernels, not bare products of only the open patches strictly between the two record times. Zero-length boundary patches at the second record carry the missing `q` factors. After the `q^{|B|-|A|}` coordinate change, the two sectors are exactly the next-clock sectors of the E1 process. This is consistent with (4) and removes the only bookkeeping ambiguity relevant to the strategic conclusion.

## Strategic consequence

The identification (4) is correct. The unnormalized successful-skeleton expansion does expose a real penalty inside a restricted routing sector, but after the complete branching transfer the penalty is redistributed rather than lost. The unnormalization-only route therefore cannot supply the missing E3 contraction. Any successful continuation on the FA-1f target would require genuinely new one-dimensional spatial information not encoded by either E1 or the local patch weights.
