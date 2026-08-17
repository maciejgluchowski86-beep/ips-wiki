# FA-INFO-002: adaptive causal information stops at finite-state closure

Date: 2026-08-17

## Verdict

**`STOP-NO-ITERABLE-STATE`.**

The bounded adaptive-information experiment finds real short-circuiting and real cancellation, but not an iterable bounded pair state.

At the registered low-density stress point

\[
q=\frac1{10},
\qquad
q_0\in\left\{\frac1{20},\frac15\right\},
\]

the exact finite test separates four natural information states:

1. the raw adaptive transcript likelihood is exact and compositional but its optimal `L^2` cost expands the one-bit divergence;
2. the same-graphical-history pair state is exact and block-local but increases under the first adjacent composition, and is already above baseline for `q_0=1/20`;
3. the universal chi-square channel coefficient is below one, but multiplying by the necessary predecessor-vector divergence gives an expansive bound;
4. the fully averaged terminal-output chi-square does contract from the initial product bit, but it is not an iterable state: S2 is larger than S1 and exact adjacent composition creates a new nonzero correlation order at every step.

Thus the cancellation exists only after averaging away information which the next constrained update needs. Retaining enough information to compose destroys the contraction.

This is not a theorem that no conceivable adaptive-information proof of FA-1f can exist. It closes the bounded likelihood/pair implementation pre-registered in Assignment 002. The assignment forbids replacing the failure by a larger transcript, larger radius, third block, or multiscale hierarchy.

## 1. Exact adaptive evaluator

At a ring with old-site value `X`, neighbours `L,R`, and refresh coin `z`,

\[
F_z(X,L,R)=
\begin{cases}
z,&L=0\text{ or }R=0,\\ X,&L=R=1.\end{cases}
\]

A valid exact evaluator may exploit both short circuits:

- a revealed vacant neighbour certifies legality;
- if `X=z`, the output equals `z` whether legal or illegal, so neighbours are irrelevant.

Recursive positive-time queries are evaluated backward through earlier rings; repeated time-zero coordinates are cached. Query choices depend only on graphical marks and already revealed values.

This is strictly smaller than the mark-only globally essential support. For the one-ring circuit S1, every fixed-coin Boolean map has all three predecessors globally essential, but the optimal adaptive evaluator at `q=1/10` uses only

\[
\boxed{E_q|Q_{S1}|=\frac{671}{500}}
\]

queries on average.

So the negative conclusion below is not a failure of adaptive pruning itself.

## 2. Exact transcript likelihood

For an adaptive transcript

\[
Q=(i_1,b_1,\ldots,i_K,b_K),
\]

the predictable choice of the next fresh coordinate cancels from the likelihood ratio. With

\[
p=1-q,
\qquad p_0=1-q_0,
\]

one has exactly

\[
\boxed{
L(Q)
=\prod_{j=1}^{K}
\left(\frac{q_0}{q}\right)^{1-b_j}
\left(\frac{p_0}{p}\right)^{b_j}.}
\]

Thus

\[
1+\chi^2(\Law_{q_0}(Q),\Law_q(Q))=E_qL(Q)^2.
\]

The random query set alone is not sufficient: membership depends on revealed values, so conditioning on the final set biases the bits. The usual bare intersection-count formula cannot be imported.

For one terminal output `Y`, the exact two-copy replacement is

\[
1+\chi^2(\Law_{q_0}(Y),\Law_q(Y))
=
E_{q\otimes q}\left[
L(Q)L(Q')
\frac{\mathbf1_{\{Y=Y'\}}}{P_q(Y)}
\right].
\]

This identity is sharp but, after averaging, it retains only the terminal output and therefore does not by itself compose through a constrained upper ring.

## 3. S1 raw transcript obstruction

Let

\[
\mathcal C_0
=\chi^2(\operatorname{Ber}(q_0),\operatorname{Ber}(q))
=\frac{(q_0-q)^2}{q(1-q)}.
\]

Exhaustive dynamic programming over all exact predictable decision trees gives the optimal raw transcript excess `C_1`.

For `q_0=1/20`,

\[
\boxed{
\frac{\mathcal C_1}{\mathcal C_0}
=\frac{807341}{648000}>1.}
\]

For `q_0=1/5`,

\[
\boxed{
\frac{\mathcal C_1}{\mathcal C_0}
=\frac{17594}{10125}>1.}
\]

Hence the most direct positive likelihood state is rejected at the first registered gate despite the much smaller expected query count.

## 4. Exact output cancellation on S1

Let

\[
V_j=\mathbf1_{\{\eta_j=0\}}.
\]

After averaging only the equilibrium refresh coin,

\[
\boxed{
E[V_0'\mid V_{-1},V_0,V_1]
=q+(V_0-q)(1-V_{-1})(1-V_1).}
\]

For product input `mu_{q_0}` this gives

\[
E_{q_0}V_0'-q=(q_0-q)(1-q_0)^2,
\]

and therefore

\[
\boxed{
\mathcal X_1=(1-q_0)^4\mathcal C_0.}
\]

At the two stress values,

\[
\frac{\mathcal X_1}{\mathcal C_0}
=
\frac{130321}{160000}
\quad\text{and}\quad
\frac{256}{625},
\]

both below one.

Thus the actual local channel does contain a cancellation which the raw transcript bound loses.

## 5. S2 destroys scalar iteration

The second frozen circuit rings site `1` and then site `0`. Its bottom variables are

\[
(X_{-1},X_0,X_1,X_2).
\]

The optimal adaptive expected query count is

\[
\frac{58829}{50000},
\]

but the raw likelihood state remains expansive:

\[
\frac{\mathcal C_2}{\mathcal C_0}
=
\frac{2667393941}{2332800000}>1
\quad(q_0=1/20),
\]

and

\[
\frac{\mathcal C_2}{\mathcal C_0}
=
\frac{12552281}{9112500}>1
\quad(q_0=1/5).
\]

The exact output chi-square is still below the original one-bit baseline, but it **increases from S1 to S2**:

\[
\boxed{
\frac{\mathcal X_2}{\mathcal X_1}
=
\frac{15689521}{14440000}>1
\quad(q_0=1/20),}
\]

\[
\boxed{
\frac{\mathcal X_2}{\mathcal X_1}
=
\frac{58081}{40000}>1
\quad(q_0=1/5).}
\]

So the S1 output contraction is not an iterable scalar coefficient.

## 6. Shared-history pair state also fails

Condition on the graphical marks `W` of the circuit and write

\[
\phi(Y)=\frac{\mathbf1_{\{Y=0\}}-q}{\sqrt{q(1-q)}}.
\]

The natural same-history pair quantity is

\[
\mathcal B
=E_W\left[
\left(E_{q_0}[\phi(Y)\mid W]-E_q[\phi(Y)\mid W]\right)^2
\right].
\]

Equivalently, with two independent reference initial fields driven by the same `W`,

\[
\mathcal B
=E[(L(Q)-1)(L(Q')-1)\phi(Y)\phi(Y')].
\]

This is exact for the value-adaptive evaluator and is closer to the shared-history pair object sought in information percolation than a bare query-set intersection.

For `q_0=1/20`, already

\[
\boxed{
\frac{\mathcal B_1}{\mathcal C_0}
=\frac{35921}{32000}>1.}
\]

Moreover the first adjacent composition increases the pair state at both registered quenches:

\[
\boxed{
\frac{\mathcal B_2}{\mathcal B_1}
=
\frac{31388053}{28736800}>1
\quad(q_0=1/20),}
\]

\[
\boxed{
\frac{\mathcal B_2}{\mathcal B_1}
=
\frac{1631729}{1339400}>1
\quad(q_0=1/5).}
\]

Thus keeping enough graphical information to make the history blockwise measurable loses the cancellation recovered by the fully averaged output.

## 7. Universal chi-square channel coefficient is not a repair

The exact chi-square strong-data-processing coefficient of the S1 channel from its full predecessor vector to one output is

\[
\eta_1=(1-q)^2,
\]

and for S2 it is

\[
\eta_2=(1-q)^3(1+q^2).
\]

At `q=1/10`,

\[
\eta_1=\frac{81}{100},
\qquad
\eta_2=\frac{73629}{100000}.
\]

These are genuine contractions for arbitrary perturbations of the full input vector. But the input-vector chi-square of product `q_0` versus product `q` on `n` sites is

\[
(1+\mathcal C_0)^n-1.
\]

After paying this predecessor-volume cost, the S1 bounds are larger than `C_0` by factors

\[
\frac{3997}{1600},\qquad \frac{271}{100},
\]

and the S2 factors are

\[
\frac{3929809}{1280000},\qquad \frac{347339}{100000}.
\]

So full-vector chi-square is even less useful than the adaptive transcript.

## 8. Structural exact closure obstruction

For a right-to-left staircase of `m` adjacent equilibrium-coin rings at sites

\[
m-1,m-2,\ldots,0,
\]

let `M_k` be the conditional mean vacancy after rings `m-1,...,k`, with bottom vacancy variables

\[
V_{-1},V_0,\ldots,V_m.
\]

Then

\[
M_m=V_m,
\]

and

\[
\boxed{
M_k
=q+(V_k-q)(1-V_{k-1})(1-M_{k+1}).}
\]

The coefficient of the full centered monomial

\[
\prod_{j=-1}^{m}(V_j-q)
\]

in `M_0-q` is exactly

\[
\boxed{(-q)^{m-1}\ne0.}
\]

The proof uses the factorization

\[
M_{k+1}-q=(1-V_k)G_{k+1}
\]

and the binary identity

\[
(V_k-q)(1-V_k)=-q(1-V_k),
\]

which gives the top-coefficient recursion `c_k=-q c_{k+1}` with `c_{m-1}=1`.

Consequently exact adjacent composition creates genuinely new correlation order at every step.

At S2 there are even two input laws with **identical every proper marginal** but different terminal output: perturb `mu_q^4` by

\[
\frac{d\nu_\pm}{d\mu_q^4}
=1\pm\varepsilon
\frac{\prod_{j=-1}^{2}(V_j-q)}{(q(1-q))^2}
\]

for sufficiently small `epsilon`. All proper marginals agree because integrating any coordinate kills the perturbation, but the S2 output differs because the four-body coefficient is `-q`.

Thus an exact repair cannot be achieved by retaining a fixed finite collection of lower-order local marginals. The natural exact repair is the growing joint correlation/transcript hierarchy.

## 9. Decision against the pre-registered rule

The assignment required one bounded state `Phi` which survives S1 and S2 with strict contraction and an exact/controlled composition rule.

The finite experiment instead gives:

- adaptive expected leaf count: improved, but irrelevant by itself;
- raw transcript likelihood: closed but noncontractive;
- shared-mark pair likelihood: locally measurable but noncontractive under adjacent composition;
- full-predecessor chi-square: universal but pays an expansive volume cost;
- sharp fully averaged output likelihood: contractive from product input but nonclosed and nonmonotone under S1 to S2;
- exact closure repair: a hierarchy whose correlation order grows indefinitely under the adjacent staircase.

This is exactly the pre-registered `STOP-NO-ITERABLE-STATE` case. No third block, larger radius, larger transcript state, or multiscale information-percolation programme is authorized by this result.

## Decisive files

- likelihood derivation: `002a-fa-info-adaptive-likelihood.md`, commit `ae910cd9`;
- S1/S2 and staircase closure theorem: `002b-fa-info-finite-circuit-closure.md`, commit `c5113b6e`;
- shared-mark pair and channel audit: `002c-fa-info-shared-mark-pair.md`, commit `4d76c8c0`;
- final exact verifier: `002-fa-info-finite-circuit-verifier.py`, commit `5bcf597c`.

No public `docs/` file or `mkdocs.yml` is edited.
