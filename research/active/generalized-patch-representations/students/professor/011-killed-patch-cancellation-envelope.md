# Assignment 011 report: killed-patch cancellation envelope without bulk positivity

Date: 2026-08-17

## Ruling

\[
\boxed{\texttt{STOP-CANCELLATION-NO-QUALITATIVE-GAIN}.}
\]

This is a deliberate opportunity-cost stop, not exhaustion. The block found a real composable cancellation theorem beyond pointwise patch positivity, but after the required prior-work/value check it did not produce a new natural-model consequence strong enough to justify another research block.

## 1. Exact patch-variation kernel

In finite volume let

\[
Q_t(\xi,\zeta)
=E_\xi\left[
\sigma_t e^{\int_0^tV(\xi_u)du}
1_{\{\tau_\dagger>t\}}1_{\{\xi_t=\zeta\}}
\right]
\]

be the signed FK kernel, and let

\[
A_t(\xi,\zeta)
=E_\xi\left[
e^{\int_0^tV(\xi_u)du}
1_{\{\tau_\dagger>t\}}1_{\{\xi_t=\zeta\}}
\right]
\]

be the raw absolute-FK kernel.

Using Assignment 003's **unnormalized** killed patch representation, define `R_t` by taking absolute values only after each hidden patch expectation and before integrating over the successful skeleton.

Then exactly

\[
\boxed{|Q_t|\le R_t\le A_t}
\]

entrywise.

The second inequality is the delayed-absolute-value gain. It uses Assignment 002's killed weighted-Mecke identity, so cemetery histories are handled exactly; the false bare skeleton factorization is not used.

Decisive note: `011a-unnormalized-patch-variation-envelope.md`, commit `59115cb7`.

## 2. Strict natural-model cancellation

The inequality can be strict in the already-verified Potts Metropolis model.

At

\[
z=1/2,\qquad q=1,
\]

use the source-type-1 singleton target record

\[
p=(3/16,5/16,-3/16),
\qquad\Lambda=11/16,
\]

and terminate the source patch at an incoming target of type `2`.

At

\[
t_*=(8/3)\log(5/4),
\]

the exact normalized signed and raw local factors are

\[
\frac{10178204}{38671875}
\quad\text{and}\quad
\frac{17919551}{38671875},
\]

so

\[
\boxed{
|E_P[w_P1_{Con(P)}]|
< E_P[|w_P|1_{Con(P)}].}
\]

The exact gap is

\[
2580449/12890625.
\]

Here the empty-target transfer itself is Metzler; the gain comes solely from hidden outcomes `0` and `2` being averaged before the incoming compatibility event.

Decisive note: `011b-potts-strict-hidden-mark-cancellation.md`, commit `4df18585`.

Verifier: `011-cancellation-envelope-verifier.py`, commit `6dab532c`.

## 3. The gain composes

The central structural question was whether deterministic time cuts destroy the gain.

They do not. If a whole-horizon patch crosses a deterministic cut, reveal its finite local type at the cut and split it into two half-patches. The whole-patch signed factor is the sum over intermediate cut types of products of the two half-patch factors. Taking the absolute value before revealing that cut type can only decrease the result.

After multiplying over all crossing patches and integrating the split candidate-skeleton measures,

\[
\boxed{R_{t+s}\le R_tR_s}
\]

entrywise.

Thus `R_t` is a positive submultiplicative kernel family. The intermediate compatible typed dual configuration is sufficient boundary memory; no infinite-memory obstruction appears.

Decisive note: `011c-submultiplicative-patch-variation-kernel.md`, commit `070598bc`.

## 4. Oscillation/renewal consequence

For

\[
\omega(\zeta)=|\operatorname{supp}\zeta|,
\]

the site-oscillation seminorm satisfies

\[
\operatorname{Osc}(P_tH_\xi)
\le(R_t\omega)(\xi).
\]

Because support size is subadditive under compatible merges, `R_t omega` is dominated by a collision-free first-moment patch tree. The finite patch types are:

- incoming starts `I_a`;
- outgoing starts `O_alpha`, one for each successful-record label.

For local start row `b_u`, the active terminal and next-record kernels are

\[
h_u(t)=\sum_{b\in E_*}|b_u e^{tK}e_b^T|,
\]

\[
k_{u\beta}(t)
=\Lambda_\beta|b_u e^{tK}e_{r_\beta}^T|.
\]

With the deterministic offspring incidence at a successful record, this gives a finite matrix renewal equation

\[
Z=h+\mathcal K*Z.
\]

If for some `gamma>0` the exponentially tilted next-generation kernel satisfies

\[
\rho\left(\int_0^\infty e^{\gamma t}\mathcal K(t)dt\right)<1
\]

and the terminal kernels have the corresponding exponential tail, then

\[
\operatorname{Osc}(P_tH_\xi)
\le C e^{-\gamma t}|\operatorname{supp}\xi|
\]

uniformly in finite volume. This is a patch-cancelled, volume-uniform sufficient criterion which does not assume pointwise bulk patch positivity.

Decisive note: `011d-oscillation-renewal-majorant.md`, commit `85b8145b`.

## 5. Exact qualitative separation from raw absolute FK

The patch renewal criterion is not algebraically equivalent to the raw absolute first-moment criterion.

For a one-neighbour three-state Potts Metropolis local rule at `z=1/2`, exact integration gives a color-symmetric patch next-generation quotient

\[
G=
\begin{pmatrix}
7/4&3/4&1\\
7/9&1/3&4/9\\
21/16&9/16&3/4
\end{pmatrix},
\qquad
\rho(G)=17/6.
\]

Removing hidden signs before source-line averaging gives

\[
\bar G=
\begin{pmatrix}
7/4&3/4&1\\
7/6&1/2&2/3\\
21/16&9/16&3/4
\end{pmatrix},
\qquad
\rho(\bar G)=3.
\]

Scale only nonempty neighbour-dependent tensor modes by

\[
\varepsilon=17/50,
\]

which at the physical-rate level is the convex interpolation

\[
c_\varepsilon=(1-\varepsilon)c(\emptyset)+\varepsilon c(\eta_N).
\]

All physical rates remain nonnegative and neighbour dependence remains active. Since record hazards scale by `epsilon` while `K` and normalized outgoing rows stay fixed,

\[
\boxed{
\rho(G_\varepsilon)=289/300<1
<51/50=\rho(\bar G_\varepsilon).}
\]

Thus the patch-cancelled renewal criterion can be subcritical while the corresponding raw absolute-FK criterion is supercritical.

Verifier: `011-oscillation-renewal-verifier.py`, commit `c1ffaafb`.

This is a structural separation gate, not a claimed published-model application.

## 6. Prior-work/value audit

The downstream machinery is largely established:

- Dobrushin-type oscillation/variation contraction and ergodicity criteria are classical;
- Głuchowski--Menz (J. Stat. Phys. 2025) already gives an arbitrary-finite-alphabet representational-seminorm recursion implying exponential covariance decay for IPS and applies it to the two-stage contact process;
- multitype age-dependent renewal and next-generation spectral-radius criteria are standard Bellman--Harris branching-process tools;
- signed matrix-semigroup domination is standard.

No equivalent source was found for the specific intermediate killed-skeleton majorant `R_t`, but that is best viewed as an extension/corollary of the same killed typed patch mechanism that survived Assignment 008, not as a separate application theorem.

For the two natural published applications already selected independently of the criterion:

- two-stage/SIRS do not gain enough source-line cancellation to open a new route;
- Potts has strict cancellation, but its high-temperature mixing/ergodicity is already accessible by established methods, and the exact threshold-separation gate above deliberately modifies interaction strength to demonstrate mechanism rather than solve a new Potts problem.

Decisive note: `011e-prior-work-and-value-ruling.md`, commit `f07a8c15`.

## 7. Final opportunity-cost decision

Assignment 011 clears the structural cancellation questions:

- delayed absolute values give strict gain;
- cemetery does not obstruct the gain;
- the gain survives deterministic time cuts;
- it yields a finite-type renewal/oscillation criterion genuinely stronger than raw absolute FK.

But it does **not** clear the research-value continuation bar: there is no new natural-model consequence beyond already established contraction/ergodicity methods.

Therefore:

- do not open another model search;
- do not return to pointwise patch positivity;
- do not start generic `d>3` external-positivity algebra;
- stop the generalized-patch programme deliberately.

The retained plausible contribution remains the cemetery-aware killed typed patch factorization/representation, now supplemented by the submultiplicative patch-variation majorant as a mathematically useful corollary. The `d=3` spectral criterion remains explicitly outside the contribution claim.