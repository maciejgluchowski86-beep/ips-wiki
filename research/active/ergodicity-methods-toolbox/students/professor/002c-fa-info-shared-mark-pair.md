# FA-INFO-002c: shared-mark pair state and universal chi-square channel audit

Date: 2026-08-17

This note checks the remaining natural bounded pair states after `002b` separated the expansive raw transcript from the contracting-but-nonclosed fully averaged output statistic.

## 1. Shared-graphical-history pair statistic

Let `W` denote the graphical marks of one frozen circuit. For one terminal vacancy indicator `Y`, write

\[
\phi(Y)=\frac{\mathbf1_{\{Y=0\}}-q}{\sqrt{q(1-q)}}.
\]

For initial product density `q_0`, define the mark-conditioned deviation

\[
d(W)
=E_{q_0}[\phi(Y)\mid W]-E_q[\phi(Y)\mid W].
\]

The natural shared-history pair state is

\[
\boxed{
\mathcal B:=E_W[d(W)^2].}
\tag{1.1}
\]

By Jensen,

\[
\mathcal X
=\left(E_W d(W)\right)^2
\le \mathcal B,
\tag{1.2}
\]

where `X` is the exact terminal-spin chi-square from `002b`.

Using the adaptive transcript likelihood `L(Q)` from `002a`, (1.1) has the exact same-marks two-copy representation

\[
\boxed{
\mathcal B
=E\left[
(L(Q)-1)(L(Q')-1)\phi(Y)\phi(Y')
\right],}
\tag{1.3}
\]

where the two reference initial configurations are independent `mu_q` fields but are evaluated with the same graphical marks `W`. Conditional on `W`, the two copies are independent, so (1.3) is simply the square of the conditional mean.

This is the closest bounded analogue here of the shared-history pair object used in information-percolation arguments. Unlike a bare query-set intersection count, it remains exact for a value-adaptive evaluator.

## 2. Exact S1/S2 values

Keep

\[
q=\frac1{10},
\qquad
\mathcal C_0=\frac{(q_0-q)^2}{q(1-q)}.
\]

The final exact verifier gives:

for `q_0=1/20`,

\[
\boxed{
\frac{\mathcal B_1}{\mathcal C_0}
=\frac{35921}{32000}>1,}
\qquad
\boxed{
\frac{\mathcal B_2}{\mathcal C_0}
=\frac{31388053}{25600000}>1,}
\tag{2.1}
\]

and

\[
\boxed{
\frac{\mathcal B_2}{\mathcal B_1}
=\frac{31388053}{28736800}>1.}
\tag{2.2}
\]

For `q_0=1/5`,

\[
\frac{\mathcal B_1}{\mathcal C_0}
=\frac{6697}{10000}<1,
\qquad
\frac{\mathcal B_2}{\mathcal C_0}
=\frac{1631729}{2000000}<1,
\tag{2.3}
\]

but still

\[
\boxed{
\frac{\mathcal B_2}{\mathcal B_1}
=\frac{1631729}{1339400}>1.}
\tag{2.4}
\]

Thus the shared-history pair state is already noncontractive relative to the one-bit baseline at the lower-vacancy quench `q_0=1/20`, and the first adjacent composition increases it at **both** registered stress quenches.

Because `B` depends only on the actual circuit channel and the conditioning on `W`, these values do not depend on which exact adaptive reveal order is used to evaluate the circuit.

## 3. Interpretation: conditioning needed for locality loses the cancellation

The three exact levels now form a strict hierarchy.

1. The raw transcript second moment keeps the entire adaptive certificate. It is positive and directly compositional, but expands already at S1 for both stress quenches.
2. The shared-mark pair state keeps enough graphical information to make a block history local and pair-composable. It improves substantially on the raw transcript, but is still expansive at `q_0=1/20` and increases from S1 to S2 for both stresses.
3. The fully averaged terminal-output chi-square `X` contracts relative to the initial product bit, but only after averaging away precisely the graphical/certificate information needed for local block composition. `002b` proves that its exact recursion creates an unbounded correlation hierarchy.

This is the finite-block closure dichotomy requested by the assignment: the locally measurable positive states lose the needed cancellation; the state which retains the cancellation is not locally closed.

## 4. Universal chi-square strong-data-processing coefficient

There is one further natural compression independent of decision trees. Let `K` be the channel from the complete predecessor vector to the terminal bit after averaging the circuit coins, with reference input `mu_q^n` and output `Ber(q)`. Its exact chi-square contraction coefficient is the squared maximal correlation

\[
\eta(K)
=\frac{\operatorname{Var}_{\mu_q^n}(P(Y=0\mid X))}{q(1-q)}.
\tag{4.1}
\]

For S1, using

\[
P(Y=0\mid X)
=q+(V_0-q)(1-V_{-1})(1-V_1),
\]

gives

\[
\boxed{\eta_1=(1-q)^2.}
\tag{4.2}
\]

For S2, exact enumeration/algebra gives

\[
\boxed{\eta_2=(1-q)^3(1+q^2).}
\tag{4.3}
\]

At `q=1/10`,

\[
\eta_1=\frac{81}{100},
\qquad
\eta_2=\frac{73629}{100000}.
\]

Both coefficients are strictly below one, but they multiply the chi-square divergence of the **entire predecessor vector**. For product `q_0` input on `n` predecessors that divergence is

\[
(1+\mathcal C_0)^n-1.
\tag{4.4}
\]

Consequently the best universal S1 channel estimate gives, relative to `C_0`,

\[
\frac{\eta_1((1+C_0)^3-1)}{C_0}
=
\begin{cases}
\dfrac{3997}{1600},&q_0=1/20,\\[2mm]
\dfrac{271}{100},&q_0=1/5,
\end{cases}
\tag{4.5}
\]

and the S2 estimate gives

\[
\frac{\eta_2((1+C_0)^4-1)}{C_0}
=
\begin{cases}
\dfrac{3929809}{1280000},&q_0=1/20,\\[2mm]
\dfrac{347339}{100000},&q_0=1/5.
\end{cases}
\tag{4.6}
\]

All four are greater than one. Thus the strongest universal one-output chi-square channel coefficient is not a hidden bounded bridge either; paying for the full predecessor vector is even more expensive than the adaptive transcript.

## 5. Registered outcome

Combining `002a`, `002b`, and this note leaves no bounded state satisfying the pre-registered continuation rule:

- raw transcript: exact/compositional, noncontractive;
- shared-mark pair: exact and history-local, noncontractive under the first adjacent composition and already above baseline for `q_0=1/20`;
- full-predecessor chi-square SDPI: contractive channel coefficient but expansive after predecessor-volume cost;
- fully averaged output chi-square: genuinely contractive from the product input but nonmonotone from S1 to S2 and structurally nonclosed, with new nonzero correlation order at every adjacent staircase step.

The only exact repair currently visible is to retain the growing joint transcript/correlation hierarchy. That is precisely the continuation forbidden by the frozen assignment.

Therefore FA-INFO-002 ends with

> **`STOP-NO-ITERABLE-STATE`.**

This is a stop theorem for the bounded adaptive-likelihood implementation tested here. It is not a proof that every conceivable state-adaptive proof of FA-1f convergence is impossible.
