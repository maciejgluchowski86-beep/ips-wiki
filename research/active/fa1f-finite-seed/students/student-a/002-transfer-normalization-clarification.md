# Clarification to Student A 002

This note fixes two bookkeeping points in `002-unnormalized-patches.md`. It does not change any of the zero/one/two-record formulas for the target deviation or the criticality conclusion.

## 1. The kernels in Section 9 are `h`-normalized coefficient kernels

Under the convention of Section 4 of the main note, the intensity `lambda=1+p` of a selected record is assigned to the unique outgoing-start patch created **at that record**. Therefore, if the horizon is placed exactly at the second record, the zero-length patches created by that record cannot literally be omitted from the raw patch product.

For example, at an all-occupied terminal configuration, the zero-length outgoing end patch created at the second record has intensity-absorbed value

$$
\widetilde C(1,OE_0)=q.
$$

The transfer densities

$$
k_{\mathrm s}(r)=e^{-r}(p+qe^{-r})^2,
$$

and

$$
k_{\mathrm c}(r)=2q e^{-2r}(p+qe^{-r})
$$

in equations (44)--(45) of the main note are therefore not bare products of only the open patches strictly between the two record times. They are the **centered coefficient transfer after the `h`-weighting**

$$
Q_t(A,B)=q^{|B|-|A|}K_t(A,B).
$$

Equivalently, include the zero-length boundary patches at the second record, then apply the `q^{|B|-|A|}` change of coordinates. The boundary `q` factors are exactly redistributed by this `h`-weighting. After that normalization the two possible next-source sectors are precisely

$$
k_{\mathrm s}(r)
=\mathbf E[e^{-(1+K)r}],
$$

and

$$
k_{\mathrm c}(r)
=\mathbf E[K e^{-(1+K)r}],
\qquad K\sim\operatorname{Binomial}(2,q),
$$

so

$$
\int_0^\infty(k_{\mathrm s}+k_{\mathrm c})(r)\,dr=1.
$$

Thus the criticality statement is unchanged; this clarification only states the measure under which the kernels are being compared.

The direct target-deviation formulas (31)--(40) in the main note already include all post-record end patches and all `lambda` factors explicitly and need no correction.

## 2. Centered input requires linearity before collecting patch coefficients

The canonical patch representation is stated for ordinary monomials. For a centered input one first uses

$$
\chi_A^*
=
\prod_{i\in A}(\eta(i)-p)
=
\sum_{C\subseteq A}(-p)^{|A\setminus C|}\chi_C,
$$

applies the unnormalized ordinary-monomial patch expansion to each `chi_C`, and then expands the affine end factors about `p` and collects centered output monomials. This produces the unique coefficients `K_t(A,B)` in

$$
P_t\chi_A^*
=
\sum_BK_t(A,B)\chi_B^*.
$$

The verified E1 identity then gives

$$
K_t(A,B)=q^{|A|-|B|}Q_t(A,B).
$$

So the global resummation argument in equations (52)--(56) of the main note is correct, but the sentence saying that the unnormalized patch formula computes the centered coefficients merely by expanding end amplitudes should be read with this initial linear-combination step included.

These two clarifications strengthen the interpretation of the main result: the full `h`-weighted transfer is exactly stochastic, and the apparent same-source loss is not a raw consistency-probability contraction.