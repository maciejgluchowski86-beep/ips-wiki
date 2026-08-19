# Addendum: canonical source-target overlap simplification

For the multi-site flip note `multisite-flip-extension.md`, let `B` be the current monomial support, `D=A cap B`, and let `S` be a multilinear target from the expansion of `c_A`.

The raw identity

\[
\chi_S\bigl(\chi_B(\eta^A)-\chi_B(\eta)\bigr)
=
\sum_{J\subseteq D}\theta_D(J)
\chi_{S\cup(B\setminus D)\cup J}
\]

should be canonically combined before defining dual clocks.

If

\[
S\cap D\neq\varnothing,
\]

then the flipped term contains `eta_i(1-eta_i)` for some `i in S cap D` and vanishes. Hence exactly

\[
\boxed{
\chi_S\bigl(\chi_B(\eta^A)-\chi_B(\eta)\bigr)
=-\chi_{B\cup S}.
}
\]

Thus there is only one signed dual branch, with coefficient `-c_A(S)`, and no hidden post-source subset.

The genuinely multi-source hidden branch occurs only when

\[
S\cap D=\varnothing.
\]

Then the outputs are distinct as `J subseteq D` varies and

\[
a_{A,D,J}(S)=c_A(S)\theta_D(J),
\]

where

\[
\theta_D(J)=(-1)^{|J|}\quad(J\neq D),
\qquad
\theta_D(D)=(-1)^{|D|}-1.
\]

At fixed `(A,D,S)` with `S cap D=emptyset`, the total absolute branch weight is

\[
\sum_{J\subseteq D}|\theta_D(J)|
=2^{|D|}-(-1)^{|D|}.
\]

This is the version that should be used in any formal graphical construction or positivity criterion. In particular, simultaneous source/target incidences do not require a new hidden boundary type after the identical monomial outputs are combined.