# Dimer Metropolis Ising: block-end centered positivity fails

Date: 2026-08-19

This note tests the strengthened disjoint-block end condition proposed in `multisite-disjoint-block-patches.md` on the simplest genuinely interacting two-site block-flip model found within the exact generator class.

## Model

Take the one-dimensional zero-field ferromagnetic Ising Hamiltonian in spins

\[
\sigma_i=2\eta_i-1\in\{-1,+1\},
\qquad
H(\sigma)=-J\sum_i \sigma_i\sigma_{i+1},
\qquad J>0.
\]

Partition the lattice into dimers

\[
Q_n=\{2n,2n+1\}.
\]

At a clock of block `Q_n`, propose to flip both spins in the dimer and accept with the Metropolis rate

\[
c_{Q_n}(\eta)=\min\{1,e^{-\beta\Delta_{Q_n}H(\eta)}\}.
\]

The internal Ising bond is unchanged by the pair flip. For `Q={1,2}` with outside neighbours `0,3`,

\[
\Delta_QH
=2J(\sigma_0\sigma_1+\sigma_2\sigma_3).
\]

Write

\[
\rho=e^{-4\beta J}\in(0,1].
\]

Then

\[
c_Q(\eta)=\rho
\]

exactly when both boundary bonds `(0,1)` and `(2,3)` are aligned, and `c_Q(\eta)=1` otherwise.

This is a genuine simultaneous two-site flip on a fixed disjoint block partition.

## Exact rate coefficients needed for one record

Expand

\[
c_Q(\eta)=\sum_{S\subseteq\{0,1,2,3\}}c_Q(S)\chi_S(\eta).
\]

For external target

\[
T=\{0\}
\]

only the four internal variants below matter:

\[
\begin{aligned}
c_Q(\{0\})&=1-\rho,\\
c_Q(\{0,1\})&=-2(1-\rho),\\
c_Q(\{0,2\})&=-(1-\rho),\\
c_Q(\{0,1,2\})&=2(1-\rho).
\end{aligned}
\]

Take pre-source dual block state

\[
D=\{1\}.
\]

Using the canonical block aggregation from `multisite-disjoint-block-patches.md`, the four rate modes cancel in every post-source state except

\[
\boxed{
a_{Q,\{1\}}^{\varnothing}(\{0\})=1-\rho,
\qquad
a_{Q,\{1\}}^{\{2\}}(\{0\})=-(1-\rho).
}
\]

All coefficients for post-states `\{1\}` and `\{1,2\}` cancel exactly.

For `0<rho<1`, this is a realized nonempty-target successful record. Its total absolute record rate is

\[
2(1-\rho).
\]

Conditional on the record, the two hidden post-source states therefore have equal probability `1/2`, with opposite signs.

## Zero-length outgoing end patch

Put the terminal horizon immediately after this outgoing record. There are no interior marks. The end block contribution is therefore

\[
\boxed{
C_Q(u_1,u_2)
=\frac12-\frac12u_2
=\frac{1-u_2}{2}.
}
\]

Let `p^*=(p_1^*,p_2^*)` be any proposed centered profile. Then

\[
C_Q(u_1,u_2)
=
\frac{1-p_2^*}{2}
-\frac12(u_2-p_2^*).
\]

Hence the centered coefficient of the singleton monomial `u_2-p_2^*` is

\[
\boxed{\kappa_{\{2\}}=-\frac12<0}
\]

for every choice of `p^*`.

Therefore the strengthened block-end condition

\[
C_Q(u,P)
=\sum_{R\subseteq Q}\kappa_R(P)
\prod_{i\in R}(u_i-p_i^*),
\qquad \kappa_R(P)\ge0,
\]

**fails** for this two-site block Metropolis dynamics at every interacting temperature `beta J>0`.

At `beta=0`, `rho=1` and the entire offending record has zero rate. This is only the trivial constant-rate limit, not a positive parameter region in which the condition survives.

## Consequence for the cheap tier

The disjoint-block representation tier remains real: the signed block dual, enriched skeleton, one-block factorization architecture and multilinear end factors are unaffected by this counterexample.

What fails is the proposed route from that representation to the paper's centered-moment cone by requiring all centered coefficients of every end block factor to be nonnegative. Even the simplest interacting ferromagnetic dimer Metropolis example violates that condition before any positive-length transfer calculation is needed.

Thus the eventual report should not present centered block-end positivity as a natural generic property of disjoint blocks. It is an additional restrictive hypothesis, and this exact example shows that it fails throughout a standard interacting block-flip family.
