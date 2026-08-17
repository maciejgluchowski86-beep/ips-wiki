# FA-INFO-002b: exact S1/S2 test and the growing correlation hierarchy

Date: 2026-08-17

This note executes the frozen finite-block test from `assignment-002-fa-info.md`. All displayed stress-point fractions are independently recomputed by `002-fa-info-finite-circuit-verifier.py` using `fractions.Fraction` and exhaustive dynamic programming over all exact decision trees.

## 1. S1: adaptive pruning is real

Fix one ring at site `0` with known refresh coin `z`. In predecessor spin variables

\[
(X,L,R)=(\eta_0,\eta_{-1},\eta_1),
\]

the output is

\[
F_z(X,L,R)=
\begin{cases}
z,&L=0\text{ or }R=0,\\ X,&L=R=1.\end{cases}
\tag{1.1}
\]

For either fixed coin, all three predecessor bits are globally essential: the mark-only support has size three.

An adaptive evaluator can do better. Query `X` first.

- If `X=z`, stop immediately: the output equals `z` whether the ring is legal or illegal.
- If `X!=z`, query one neighbour. A vacancy certifies legality and stops; an occupied neighbour forces a query of the other neighbour.

At the stress reference density

\[
q=\frac1{10},
\]

the exact dynamic program confirms this is optimal for expected query count and, for both registered `q_0`, also optimal for raw transcript `L^2` cost. Averaging over the equilibrium refresh coin gives

\[
\boxed{E_q|Q_{S1}|=\frac{671}{500}=1.342.}
\tag{1.2}
\]

Thus the adaptive object is genuinely smaller than the mark-only support. The negative result below is not a claim that short-circuiting is absent.

## 2. S1 raw transcript likelihood expands

Let

\[
\mathcal C_0
=\chi^2(\operatorname{Ber}(q_0),\operatorname{Ber}(q))
=\frac{(q_0-q)^2}{q(1-q)}.
\tag{2.1}
\]

Let `C_1` be the optimal raw transcript excess

\[
\mathcal C_1
=\inf_A\{E_q[L_A(Q)^2]-1\},
\tag{2.2}
\]

where the infimum runs over all exact predictable decision trees for (1.1).

For `q_0=1/20`,

\[
\mathcal C_0=\frac1{36},
\qquad
\boxed{
\frac{\mathcal C_1}{\mathcal C_0}
=\frac{807341}{648000}>1.}
\tag{2.3}
\]

For `q_0=1/5`,

\[
\mathcal C_0=\frac19,
\qquad
\boxed{
\frac{\mathcal C_1}{\mathcal C_0}
=\frac{17594}{10125}>1.}
\tag{2.4}
\]

Therefore the pre-registered rule rejects the raw adaptive transcript likelihood as the iterable contraction state already at S1.

This is a pair/likelihood statement, not a first-moment query-count statement. The same evaluator which reduces the expected number of leaves from three to `671/500` still has second moment too large.

## 3. S1 sharp output chi-square contracts

The failure of the transcript bound is not a failure of the actual local channel.

Let vacancy indicators be

\[
V_j=\mathbf1_{\{\eta_j=0\}}.
\]

After averaging only over the equilibrium refresh coin, the conditional vacancy probability after one ring is exactly

\[
\boxed{
H_1
:=E[V_0'\mid V_{-1},V_0,V_1]
=q+(V_0-q)(1-V_{-1})(1-V_1).}
\tag{3.1}
\]

For product input vacancy density `q_0`,

\[
E_{q_0}H_1-q
=(q_0-q)(1-q_0)^2.
\tag{3.2}
\]

Hence the exact terminal-spin chi-square is

\[
\boxed{
\mathcal X_1
=(1-q_0)^4\mathcal C_0.}
\tag{3.3}
\]

At the two stress values,

\[
\frac{\mathcal X_1}{\mathcal C_0}
=
\begin{cases}
\dfrac{130321}{160000},&q_0=1/20,\\[2mm]
\dfrac{256}{625},&q_0=1/5.
\end{cases}
\tag{3.4}
\]

Both are strictly below one.

Thus exact aggregation over transcripts with the same terminal output recovers a substantial cancellation which the positive raw transcript second moment loses.

## 4. The scalar sharp state is not closed even for one upper ring

Equation (3.1) also shows the closure defect immediately. For a general predecessor law `nu`,

\[
E_\nu V_0'-q
=
E_\nu[(V_0-q)(1-V_{-1})(1-V_1)].
\tag{4.1}
\]

So the next one-site density is not determined by the predecessor one-site density. It needs a three-site centered correlation.

For example, product `mu_q^3` and the law under which

\[
V_{-1}=V_0=V_1=B,
\qquad B\sim\operatorname{Ber}(q),
\]

have identical one-site marginals. Under product input the output vacancy density is `q`; under the diagonal law it is `q^2`. Thus the exact scalar terminal likelihood/chi-square cannot be iterated after the first block without additional joint information.

## 5. S2: adjacent composition

The frozen second circuit has a ring at site `1` followed by a ring at site `0`. Let the bottom spins be

\[
(X_{-1},X_0,X_1,X_2),
\]

and the refresh coins be `(z_1,z_0)`. Put

\[
Y_1=F_{z_1}(X_1,X_0,X_2),
\qquad
Y_0=F_{z_0}(X_0,X_{-1},Y_1).
\tag{5.1}
\]

The optimal expected number of bottom queries, averaged over the equilibrium coins, is

\[
\boxed{E_q|Q_{S2}|=\frac{58829}{50000}.}
\tag{5.2}
\]

The small first moment is again not sufficient. The exact raw transcript excess remains above the initial one-bit divergence:

for `q_0=1/20`,

\[
\boxed{
\frac{\mathcal C_2}{\mathcal C_0}
=\frac{2667393941}{2332800000}>1,}
\tag{5.3}
\]

and for `q_0=1/5`,

\[
\boxed{
\frac{\mathcal C_2}{\mathcal C_0}
=\frac{12552281}{9112500}>1.}
\tag{5.4}
\]

So the raw transcript state is noncontractive at both S1 and S2.

## 6. The sharp output statistic also fails blockwise scalar composition

The exact S2 terminal vacancy probabilities under the two product quenches are

\[
P_{1/20}(Y_0=0)=\frac{84741}{1600000},
\qquad
P_{1/5}(Y_0=0)=\frac{1107}{6250}.
\tag{6.1}
\]

The corresponding exact output chi-square ratios relative to `C_0` are

\[
\frac{\mathcal X_2}{\mathcal C_0}
=
\begin{cases}
\dfrac{5663917081}{6400000000},&q_0=1/20,\\[2mm]
\dfrac{232324}{390625},&q_0=1/5.
\end{cases}
\tag{6.2}
\]

They remain below one relative to the initial product bit. But they are **larger than S1**:

\[
\boxed{
\frac{\mathcal X_2}{\mathcal X_1}
=
\begin{cases}
\dfrac{15689521}{14440000}>1,&q_0=1/20,\\[2mm]
\dfrac{58081}{40000}>1,&q_0=1/5.
\end{cases}}
\tag{6.3}
\]

Therefore even the sharp scalar output chi-square is not a monotone block state under the first adjacent composition. Its S1 contraction is not an iterable one-step coefficient.

## 7. Exact correlation hierarchy generated by adjacent rings

The S2 failure is not just one unfortunate fraction. There is a structural growing-degree identity.

Consider a right-to-left staircase of `m` equilibrium-coin rings at sites

\[
m-1,m-2,\ldots,0,
\]

with bottom vacancy indicators

\[
V_{-1},V_0,\ldots,V_m.
\]

Let `M_k` be the conditional mean vacancy at site `k` after the rings at sites `m-1,...,k` have been performed, conditional on all bottom spins. Then

\[
M_m=V_m,
\]

and exact one-ring conditioning gives

\[
\boxed{
M_k
=q+(V_k-q)(1-V_{k-1})(1-M_{k+1}),
\qquad k=m-1,\ldots,0.}
\tag{7.1}
\]

### Proposition 7.1 (nonzero top centered coefficient)

In the multilinear expansion of `M_0-q` in the centered variables

\[
U_j=V_j-q,
\qquad j=-1,0,\ldots,m,
\]

the coefficient of the full monomial

\[
\prod_{j=-1}^{m}U_j
\]

is exactly

\[
\boxed{(-q)^{m-1}.}
\tag{7.2}
\]

In particular it is nonzero for every `q in (0,1)` and every `m>=1`.

### Proof

Shifting variables by `q` does not change the coefficient of the top-degree monomial, so it is enough to track the coefficient of

\[
\prod_{j=k-1}^{m}V_j
\]

in `D_k:=M_k-q`.

From (7.1),

\[
D_{k+1}
=(V_{k+1}-q)(1-V_k)(1-M_{k+2})
=(1-V_k)G_{k+1},
\tag{7.3}
\]

where `G_{k+1}` does not depend on `V_k`. Also

\[
D_k
=(V_k-q)(1-V_{k-1})(p-D_{k+1}).
\tag{7.4}
\]

The `p` term in (7.4) cannot contribute to the full monomial. In the remaining term use the binary identity

\[
(V_k-q)(1-V_k)=-q(1-V_k).
\tag{7.5}
\]

If `c_{k+1}` is the full-monomial coefficient in `D_{k+1}=(1-V_k)G_{k+1}`, then the corresponding top coefficient in `G_{k+1}` is `-c_{k+1}`. Equations (7.4)--(7.5) therefore give

\[
c_k=-q c_{k+1}.
\tag{7.6}
\]

For the first ring at the right edge,

\[
D_{m-1}
=(V_{m-1}-q)(1-V_{m-2})(1-V_m),
\]

whose full coefficient is `c_{m-1}=1`. Iterating (7.6) yields

\[
c_0=(-q)^{m-1}.
\]

This is also the full centered coefficient. `square`

For S1 (`m=1`) the top centered coefficient is `1`. For S2 (`m=2`) it is `-q`; the exact verifier checks `-1/10` at the registered stress density.

## 8. All proper marginals can agree while S2 output differs

The top coefficient gives an exact finite-state closure witness.

On four bottom sites under `mu_q^4`, set

\[
\Psi
=\frac{\prod_{j=-1}^{2}(V_j-q)}{(q(1-q))^2}.
\]

For sufficiently small `epsilon>0`, the two probability laws

\[
\frac{d\nu_\pm}{d\mu_q^4}=1\pm\epsilon\Psi
\tag{8.1}
\]

are positive. Integrating out any one coordinate kills `Psi`, so `nu_+` and `nu_-` have **identical every proper marginal**, in particular identical one-, two- and three-site marginals.

But Proposition 7.1 at `m=2` gives

\[
E_{\mu_q^4}[H_2\Psi]
=-q\,(q(1-q))^2\ne0,
\tag{8.2}
\]

where `H_2` is the S2 conditional terminal-vacancy probability after averaging its two refresh coins. Hence

\[
E_{\nu_+}H_2\ne E_{\nu_-}H_2.
\tag{8.3}
\]

Thus even **all proper local marginals** fail to determine the S2 terminal output. Exact composition needs the new four-body coordinate. Proposition 7.1 shows that the adjacent staircase creates a new nonzero order at every further composition.

## 9. Consequence for the registered finite-state test

The two natural Part-B states separate as follows.

1. **Raw adaptive transcript likelihood.** It is exact, positive and directly compositional at the decision-tree level, but its optimal second moment expands the initial one-bit divergence already on S1 and remains expansive on S2.
2. **Sharp terminal-output two-copy likelihood.** It exhibits genuine cancellation and contracts relative to the initial product perturbation on S1/S2, but it is not closed: S1 requires three-body predecessor information, S2 creates a new four-body coordinate, and the exact staircase recursion creates unbounded correlation order. Even its scalar value increases from S1 to S2 at both registered stress quenches.

No bounded weighted pair/overlap state appears between these two extremes in the frozen radius/depth test. The only exact repair presently available is to retain the enlarging joint transcript/correlation hierarchy which the assignment explicitly forbids as a continuation.

This meets the registered `STOP-NO-ITERABLE-STATE` criterion unless an independent bounded pair inequality is found inside the remaining audit of the same S1/S2 data. It is not a theorem that no conceivable adaptive-information proof of FA-1f can exist.
