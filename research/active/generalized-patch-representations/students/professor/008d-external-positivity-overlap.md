# 008d: external positivity directly subsumes the scalar `d=3` spectral sign problem

Date: 2026-08-17

This note records the strongest negative novelty finding of Assignment 008 so far. It concerns packages B--D, especially the Assignment-006 finite spectral criterion.

## 1. The remaining `OI` condition is a standard external-positivity problem

After Assignment 005, each boundary-complete three-state `OI` numerator has the form

\[
N(t)=p e^{tK} f,
\]

where `K` is a real `3 x 3` matrix with zero row at the inactive state, `p` is an outgoing signed row, and `f=e_0^T+e_b^T`.

In linear-systems language, the condition

\[
N(t)\ge0\qquad(t\ge0)
\]

is exactly nonnegativity of a scalar matrix-exponential response. More specifically, for any `d>0`,

\[
h(t)=e^{-dt}N(t)=p e^{t(K-dI)}f
\]

has the same sign as `N(t)` for every `t`, while `A=K-dI` has all eigenvalues shifted strictly into the left half-plane. Thus `h` is the impulse response of the continuous-time SISO realization

\[
A=K-dI,\qquad B=f,\qquad C=p,
\]

and typed `OI` positivity is exactly **external positivity** of this realization.

This identification is mathematical, not just terminological.

## 2. External positivity is a classical control-theory object

For a continuous-time SISO linear system, external positivity is equivalent to nonnegativity of its impulse response

\[
C e^{tA}B\ge0\qquad(t\ge0).
\]

This is standard positive-systems theory. Internal positivity is the stronger realization-level condition `A` Metzler with nonnegative input/output vectors; external positivity permits signed realizations and asks only for the scalar input-output response to remain nonnegative.

Consequently the general question "when is `p e^{tK}f` nonnegative for all `t`?" is not new.

## 3. Exact third-order external positivity was known before this project

Two sources are decisive.

### Lin--Fang 1997

S.-K. Lin and C.-J. Fang, *Nonovershooting and monotone nondecreasing step responses of a third-order SISO linear system*, IEEE Trans. Automat. Control 42 (1997), 1299--1303, DOI 10.1109/9.623097.

Their abstract states that they give **necessary and sufficient conditions** for a third-order SISO system to have a monotone nondecreasing step response when the transfer function has real poles, in terms of numerator coefficients. A monotone step response is equivalent to a nonnegative impulse response, hence external positivity.

The active spectrum in Assignment 006 is real. After the harmless scalar shift above, the three poles are real and strictly negative. Therefore the generic Assignment-006 scalar sign problem belongs directly to the class characterized in Lin--Fang.

### Weller--Martin 2020

S. R. Weller and J. H. Martin, *On strongly unimodal third-order SISO linear systems with applications to pharmacokinetics*, IFAC-PapersOnLine 53 (2020), 4654--4661, DOI 10.1016/j.ifacol.2020.12.509.

The paper explicitly "addresses the problem of characterizing external positivity (equivalently, non-negative impulse response) of third-order single-input, single-output linear systems" and gives an exact geometric solution using order-three matrix-exponential distributions.

This modern source makes the overlap unambiguous even without translating formula-by-formula to Lin--Fang's numerator inequalities.

A useful successor calibration is S. R. Weller, *External positivity of linear systems: approximate characterization via convex polytopes*, IFAC-PapersOnLine 56 (2023), 5077--5082: its abstract describes exact transfer-function characterization of external positivity as difficult in general and targets orders `n>=4`. That is consistent with order three being a separately tractable, already studied case.

## 4. Consequence for Assignment 006

The Assignment-006 derivation

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}
\]

and its unique-critical-point test are correct and useful *inside this project*, but they are not an independent novelty anchor. They are a direct special-case solution of a pre-existing third-order external-positivity problem.

The exact formula used here is adapted to the Markov/patch coordinates and may be different from the coordinate formulas in the control literature. That does not create a new theorem: equivalence under the realization above is enough for subsumption of the scalar sign result.

### Item 4 status: exact `d=3` finite spectral criterion

\[
\boxed{\texttt{known / directly subsumed}.}
\]

This is the clearest negative component-level novelty finding in the audit.

## 5. Package B is not entirely subsumed by control theory

Package B contains more than the scalar external-positivity question. Assignment 004 proves, from the signed patch law, that the weighted killed local transfer generator is exactly

\[
K_i(r,s)=a_{i,r}^s(\emptyset),
\]

because the ordinary empty-target escape subtraction and the no-success killing rate cancel against the local Feynman--Kac potential. It then identifies *which finitely many input/output vectors* arise from each typed patch boundary orientation.

The control literature starts from a given realization `(A,B,C)`; it does not supply this IPS-to-transfer cancellation or the patch-boundary dictionary.

Therefore:

### Item 3 status: transfer-matrix bulk positivity formulation

\[
\boxed{\texttt{known ingredients, assembly plausibly new}.}
\]

The finite-dimensional positivity language is standard external/internal positive-systems theory. The derivation of the realization from the typed patch representation, especially `K=A^emptyset`, was not found in prior IPS work.

## 6. Exchange-symmetric criterion

Assignment 007 imposes a structured physical generator

\[
Q=\begin{pmatrix}
-2a&a&a\\
b&-(b+c)&c\\
b&c&-(b+c)
\end{pmatrix}
\]

and translates exact patch positivity into the algebraic inequalities

\[
c\ge a,
\]

\[
p_1,p_2,p_0+p_1,p_0+p_2\ge0,
\]

\[
(b+2a)p_0+a(p_1+p_2)\ge0.
\]

Once the patch-to-SISO reduction is made, the proof uses standard symmetry/eigenmode ordering and external-positivity ideas. I found no source stating these **IPS coefficient inequalities** for typed patch positivity, but their scalar semigroup content is a structured corollary of known external positivity rather than a fundamentally new positivity theory.

### Item 5 status: exchange-symmetric exact algebraic criterion

\[
\boxed{\texttt{known ingredients, assembly plausibly new}.}
\]

It remains a useful project-specific corollary and a useful application gate, but should not be advertised as an independent novelty anchor.

## 7. Broader lesson for `d>3`

This comparison also changes the interpretation of arbitrary `d`. For fixed local dimension, typed `OI` positivity is a finite-dimensional external-positivity problem. The control literature indicates that exact characterization becomes genuinely hard at higher order; modern work explicitly treats orders `>=4` by approximate or sufficient methods in general.

Thus a future generic `d>3` tractable-criterion programme would overlap a substantial existing control-theory problem. This supports Meeting 007's decision **not** to launch an automatic `d>3` algebra block before applications.

It does not affect the arbitrary-finite-state patch representation itself, which precedes the external-positivity reduction.