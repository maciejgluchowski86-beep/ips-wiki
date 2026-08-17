# 006c: finite boundary-complete three-state spectral criterion and usability

Date: 2026-08-17

This note combines the generic and degenerate analyses into the exact finite criterion required by Part D of Assignment 006 and makes the tractability ruling.

## 1. Full boundary-complete criterion

At one site, assume the boundary-complete `d=3` hypothesis of Assignment 005. Let

\[
K(0,\cdot)=0,
\qquad K(r,s)=a_r^s(\emptyset),\quad r=1,2.
\]

For every nonempty-target outgoing row write

\[
p=(p_0,p_1,p_2)=\mathbf a_{r,\tau}.
\]

Then typed bulk patch positivity is equivalent to the following finite conditions.

### (I) Interior Metzler conditions

\[
\boxed{K(1,2)\ge0,\qquad K(2,1)\ge0.}
\tag{1.1}
\]

Deletion entries into state `0` are already nonnegative physical rates. Under boundary completeness, (1.1) is necessary by arbitrarily short `IO` patches. It makes `K` Metzler, hence `e^{tK}` entrywise nonnegative.

Consequently all incoming-initial `II/IO` families are automatic.

### (II) Outgoing zero-length conditions

For every outgoing row `p`, require

\[
\boxed{
p_1\ge0,
\qquad p_2\ge0,
\qquad p_0+p_1\ge0,
\qquad p_0+p_2\ge0.}
\tag{1.2}
\]

The first two are the zero-length `OO` conditions. Together with the Metzler property they make every `OO` numerator nonnegative for all time. The last two are the zero-length `OI` conditions.

Thus after (1.1)--(1.2), **only `OI` remains**.

### (III) One finite spectral test for each `OI` descriptor

For each outgoing row `p` and each incoming terminal type `b in {1,2}`, put

\[
f_b=e_0^T+e_b^T,
\qquad
N_{p,b}(t)=p e^{tK}f_b.
\tag{1.3}
\]

Classify the active `2 x 2` spectrum.

#### Generic distinct negative eigenvalues

If the active eigenvalues are `-mu,-nu`, `0<mu<nu`, compute `L,A,B` by `006a`:

\[
N(t)=L+A e^{-\mu t}+B e^{-\nu t}.
\]

Require

\[
N(0)\ge0,
\qquad L\ge0.
\tag{1.4}
\]

If

\[
A<0<B,
\qquad
0<R:=-\frac{\mu A}{\nu B}<1,
\tag{1.5}
\]

also require the unique interior-minimum inequality

\[
\boxed{
L+\frac{\nu-\mu}{\nu}
A R^{\mu/(\nu-\mu)}\ge0.}
\tag{1.6}
\]

No other time is tested.

#### One zero active eigenvalue

The numerator has form `L+A exp(-nu t)`. Require its two endpoints to be nonnegative.

#### Repeated nonzero diagonalizable active block

Again the numerator has one decaying mode. Require its two endpoints to be nonnegative.

#### Repeated nonzero Jordan active block

Write

\[
N(t)=L+(A+Bt)e^{-\mu t}
\]

using the formulas of `006b`. Require

\[
N(0)=L+A\ge0,
\qquad L\ge0.
\]

If

\[
B<0,
\qquad B-\mu A<0,
\tag{1.7}
\]

also require the unique interior-minimum inequality

\[
\boxed{
L+\frac B\mu
\exp\left(-\frac{B-\mu A}{B}\right)\ge0.}
\tag{1.8}
\]

#### All-zero active spectrum

The numerator is constant.

These cases include reducible reference-neighbour physical chains; irreducibility is nowhere assumed.

## 2. Necessity and sufficiency

### Theorem 2.1

Under boundary completeness, conditions (I)--(III) are necessary and sufficient for typed bulk patch positivity at the site.

### Proof

Necessity of (I) and (II) is the short-time/zero-length argument of Assignment 005. Once `K` is Metzler, all incoming-initial numerators are nonnegative. Once also `p_1,p_2>=0`, every `OO` numerator is nonnegative because the zeroth row of `e^{tK}` contributes nothing to an active terminal and the two active columns are entrywise nonnegative.

Thus the only remaining numerators are the finitely many `OI` functions (1.3). `006a` proves the generic distinct-spectrum test is necessary and sufficient because the derivative has at most one positive zero, and the only possible interior minimum is (1.5). `006b` proves the corresponding exhaustive classification for every degenerate spectral case, again with at most one interior minimum. Therefore (III) is equivalent to all-time nonnegativity of every remaining `OI` family. This proves the result. `square`

## 3. The test is genuinely finite

At a fixed site the local state space and neighbour set are finite, hence there are finitely many nonempty typed targets and finitely many outgoing rows. Boundary completeness asks for two incoming terminal types.

For each pair `(p,b)`, Theorem 2.1 requires:

- its value at `t=0` (already included in (II));
- its long-time value;
- **at most one** interior critical value.

There is no mesh, no limiting time scan, no root enumeration of growing complexity, and no optimization over `t`. The critical time is given explicitly by the local spectral data.

Therefore this is materially stronger than the Assignment-004 definition

\[
N_{p,b}(t)\ge0\quad\text{for every }t\ge0,
\]

which is an uncountable semigroup family.

## 4. Algebraic versus spectral tractability

The criterion is not a binary-style polynomial/rational coefficient cone.

For rational or algebraic physical rates, the generic eigenvalues `mu,nu` and the coefficients `L,A,B,R` are algebraic: they require at most the quadratic radical from the active `2 x 2` discriminant. In an interior-minimum regime, however, the exact critical value contains

\[
R^{\mu/(\nu-\mu)}.
\tag{4.1}
\]

The Jordan case similarly contains one ordinary exponential evaluated at an explicitly known algebraic critical time.

This is an unavoidable remnant of the continuous-time spectrum and is precisely the information lost by the endpoint-only criterion refuted in Assignment 005.

Nevertheless it is not an unresolved time-dependent sign problem: (4.1) is a **single explicitly specified real number**. A fixed local descriptor is decided by one critical comparison, not by checking a continuum of times. In rational-spectrum examples, including both mandatory gates, it reduces further to exact rational algebra.

For algebraic input with an irrational algebraic exponent in (4.1), a purely algebraic elimination should not be expected in general. This limits how simple a later coefficient theorem can be, but it does not make the spectral criterion a restatement of the semigroup definition.

## 5. Tractability ruling

Assignment 006 requires a choice between:

1. a genuinely finite spectral criterion; and
2. a formula so close to scanning all `t` that it gives no practical mathematical gain.

Theorem 2.1 is in the first category. It compresses each all-time family to at most three distinguished evaluations, with the only interior point explicitly computed from a `2 x 2` spectrum.

Accordingly the tractability gate **passes**.

The appropriate limitation to carry forward is:

> boundary-complete three-state positivity has an exact finite spectral criterion, but Assignment 005 shows that it does not generally collapse to endpoint coefficient inequalities, and the generic critical inequality is not purely algebraic in the local coefficients.

This is a meaningful theorem rather than a sufficient subcone or a time-scan restatement.
