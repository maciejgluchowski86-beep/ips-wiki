# FA-INFO-002a: adaptive evaluator and exact likelihood identities

Date: 2026-08-17

## 1. Graphical evaluator

Fix a finite graphical circuit and all of its Poisson/ring locations and refresh coins. Its bottom-layer spins are independent Bernoulli variables under the stationary reference law `mu_q`; write spin `0` for vacancy, so

\[
\nu_q(0)=q,\qquad \nu_q(1)=p:=1-q.
\]

At a ring at site `i` with old-site value `X`, neighbour values `L,R`, and known refresh coin `z`, the post-ring value is

\[
F_z(X,L,R)=
\begin{cases}
z,&L=0\text{ or }R=0,\\ X,&L=R=1.\end{cases}
\tag{1.1}
\]

An exact adaptive evaluator is an ordinary decision tree for the resulting Boolean circuit. At each step it chooses an unresolved predecessor value using only the fixed graphical marks and already revealed values. It may exploit both exact short circuits:

1. a revealed vacant neighbour certifies legality, so the other neighbour is irrelevant to legality;
2. if the old-site value equals `z`, then (1.1) equals that common value whether the ring is legal or illegal, so the neighbours are irrelevant to the output.

A positive-time query is recursively evaluated through earlier rings. If two recursive branches reach the same bottom coordinate, the value is cached and queried once. The tree stops as soon as the terminal output is logically determined.

Thus the transcript separates cleanly into fixed graphical marks and a finite ordered list of distinct queried time-zero coordinates and bits.

## 2. Adaptive product likelihood ratio

Let

\[
Q=(i_1,b_1,\ldots,i_K,b_K)
\]

be the complete time-zero query transcript under the reference product law `mu_q`. The query index `i_j` is measurable with respect to the graphical marks and the previously revealed pairs `(i_1,b_1),...,(i_{j-1},b_{j-1})`; it does not depend on an unrevealed bottom bit.

Let the alternative initial product law have vacancy density `q_0`, and put

\[
p_0=1-q_0,
\qquad
\ell(0)=\frac{q_0}{q},
\qquad
\ell(1)=\frac{p_0}{p}.
\tag{2.1}
\]

### Proposition 2.1 (exact transcript likelihood)

For every transcript with positive reference probability,

\[
\boxed{
L(Q)
:=
\frac{d\Law_{\mu_{q_0}}(Q)}{d\Law_{\mu_q}(Q)}
=
\prod_{j=1}^{K}\ell(b_j).
}
\tag{2.2}
\]

### Proof

Condition on the fixed graphical marks. Once the first `j-1` queried values are specified, the decision rule chooses the same next coordinate `i_j` under both initial product laws. Because repeated bottom coordinates are cached, `i_j` is a fresh product coordinate. Hence

\[
P_{q}(b_j\mid i_1,b_1,\ldots,i_j)
=\nu_q(b_j),
\]

and the corresponding probability under `q_0` is `nu_{q_0}(b_j)`. Multiplying the conditional likelihood ratios gives (2.2). The value-dependence of the *future query set* causes no problem because every choice of the next index is predictable from the already revealed transcript and therefore contributes the same indicator under numerator and denominator. `square`

The caching condition is load-bearing. If the same bottom bit is encountered by two recursive branches it contributes one likelihood factor, not two.

## 3. Raw transcript chi-square

Equation (2.2) gives

\[
\boxed{
1+\chi^2(\Law_{q_0}(Q),\Law_q(Q))
=E_q[L(Q)^2].
}
\tag{3.1}
\]

For exact decision-tree enumeration, querying a fresh bit contributes the squared-likelihood weights

\[
\boxed{
w_0=\frac{q_0^2}{q},\qquad w_1=\frac{p_0^2}{p}.}
\tag{3.2}
\]

Thus if a partial decision tree queries a fresh bit and its two child costs are `C_0,C_1`, its exact raw second-moment cost is

\[
w_0C_0+w_1C_1.
\tag{3.3}
\]

This gives a finite dynamic program over partial assignments. It optimizes over **all** exact predictable query orders, not merely left-first/right-first rules.

If `Y` is the terminal output determined by `Q`, data processing gives

\[
\chi^2(\Law_{q_0}(Y),\Law_q(Y))
\le
E_q[L(Q)^2]-1.
\tag{3.4}
\]

The inequality can be strict because the full transcript records certificates which are discarded after the output has been determined.

## 4. Why a bare random-set overlap formula is invalid

If the query set `R(Q)` were chosen independently of the bottom bits, one could condition on `R` and factor likelihood moments site by site. Here this conditioning is generally invalid: the event that a coordinate is queried can depend on earlier revealed values. For example, after revealing a vacant neighbour the evaluator does not query the second neighbour. Conditioning on the final query set therefore biases the revealed values.

Consequently a formula depending only on `|R cap R'|` is not an exact identity for this adaptive evaluator unless additional independence is separately proved. The transcript likelihood (2.2) remains exact, but the random set by itself is not sufficient.

## 5. Exact two-copy replacement for the terminal output

Let `(Q,Y)` and `(Q',Y')` be two independent copies of the complete graphical experiment under the reference initial law `mu_q`, including independent graphical marks and independent bottom configurations. Since the graphical law is the same under `q_0` and `q`, Proposition 2.1 applies after averaging over marks as well.

Let

\[
\pi(y)=P_q(Y=y).
\]

Then

\[
\begin{aligned}
1+\chi^2(\Law_{q_0}(Y),\Law_q(Y))
&=\sum_y\frac{P_{q_0}(Y=y)^2}{\pi(y)}\\
&=\boxed{
E_{q\otimes q}\left[
L(Q)L(Q')
\frac{\mathbf 1_{\{Y=Y'\}}}{\pi(Y)}
\right].}
\tag{5.1}
\end{aligned}
\]

For a terminal FA spin started from equilibrium, stationarity gives

\[
\pi(0)=q,\qquad \pi(1)=p.
\tag{5.2}
\]

Equation (5.1) is the exact weighted two-copy information object for the bounded test. It is evaluator-independent after expectation, whereas the raw transcript upper bound (3.4) is evaluator-dependent.

The two-copy coupling occurs through the output-match kernel, not a bare intersection count. This is the correct replacement at the present level of generality.

## 6. First structural warning about composition

The sharp output statistic in (5.1) aggregates all transcripts leading to the same final bit. That aggregation is exactly what can make it much smaller than the raw transcript cost.

However an upper ring does not receive only one predecessor bit: its evaluator may need the **joint law** of its old site and two neighbours. Therefore a scalar terminal-output likelihood is not automatically an iterable state. The frozen S1/S2 experiment must decide whether the information discarded by the output aggregation can be compressed into a bounded pair state, or whether the next adjacent constrained ring forces a growing joint-history hierarchy.

This is the precise closure question tested next.
