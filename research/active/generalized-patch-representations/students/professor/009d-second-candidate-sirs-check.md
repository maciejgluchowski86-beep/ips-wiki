# 009d: bounded second-candidate check — spatial SIRS has the same catalytic-birth obstruction

Date: 2026-08-17

Assignment 009 allows one materially different second candidate after the selected model's base verdict is complete. This note checks the stochastic spatial SIRS model and stops there; it is not an open-ended application search.

Representative source: J. Joo and J. L. Lebowitz, *Pair approximation of the stochastic susceptible-infected-recovered-susceptible epidemic model on the hypercubic lattice*, Phys. Rev. E 70 (2004), 036114, DOI 10.1103/PhysRevE.70.036114.

## 1. Physical dynamics

Use

- `0=S`: susceptible;
- `1=I`: infected;
- `2=R`: recovered/immune.

The continuous-time local rules are

\[
0\to1 \text{ at rate } \lambda n_1(x),
\qquad
1\to2 \text{ at rate } \delta,
\qquad
2\to0 \text{ at rate } \gamma,
\tag{1.1}
\]

with nonnegative parameters. Every event is a single-site replacement. For finite positive `delta,gamma`, the recovered state is dynamically genuine rather than a passive color.

## 2. Typed coefficient table

Take susceptible state `0` as the reference state. For each neighbour `j`, let

\[
\tau_j=\{j\mapsto1\}.
\]

The only nonzero nonempty physical tensor coefficient is

\[
\widehat c^{0\to1}(\tau_j)=\lambda.
\]

Therefore the successful outgoing row is again

\[
\boxed{
\mathbf a_{1,\tau_j}
=(\lambda,-\lambda,-\lambda).}
\tag{2.1}
\]

The empty-target rows are

\[
\boxed{
\mathbf a_{1,\emptyset}=(0,-\delta,0),
\qquad
\mathbf a_{2,\emptyset}=(0,\delta,-\gamma).}
\tag{2.2}
\]

Thus

\[
K=
\begin{pmatrix}
0&0&0\\
0&-\delta&0\\
0&\delta&-\gamma
\end{pmatrix}.
\tag{2.3}
\]

Every successful record has source type `1`, incoming target type `1`, and hidden post-source outcome `0,1,2` with signs `+,-,-`.

## 3. Exact realized `OO` obstruction

The hidden outcome `S=1` has positive reference probability whenever `lambda>0`, and the next successful record again requires pre-source type `1`. Therefore the same-source `OO` descriptor is realized.

Its zero-length signed numerator is

\[
\mathbf a_{1,\tau_j}e_1^T=-\lambda<0.
\tag{3.1}
\]

More strongly, since the active block of (2.3) is Metzler and the terminal type is `1`,

\[
N_{OO}(t)
=\mathbf a_{1,\tau_j}e^{tK}e_1^T
\]

is a negative linear combination of nonnegative active-column entries, with the strictly positive contribution

\[
-\lambda e^{-\delta t}.
\]

Hence

\[
\boxed{N_{OO}(t)<0\quad\text{for all finite }t\ge0\text{ whenever }\lambda>0.}
\tag{3.2}
\]

The killed-reference denominator is strictly positive for the same reason as in `009c`: the hidden source-preserving branch has absolute mass `lambda` and a no-success interval has positive probability.

Thus spatial SIRS also fails typed patch positivity throughout its interacting infection range.

## 4. Interpretation

This second candidate is materially different from the two-stage contact process:

- its three states form the epidemic cycle `S->I->R->S`;
- the successful target is infected type `1`, not mature type `2`;
- the recovered state returns to the reference state instead of dying from a population process.

Nevertheless both models share the same local catalytic structure:

\[
0\to r
\quad\text{with a positive nonempty target mode,}
\]

with no matching target-mode coefficient into `r` from active source states. The indicator-basis expansion then forces the source-preserving hidden coefficient `a_r^r(tau)` to be negative.

Therefore the general catalytic-birth no-go lemma in `009c` is the structural explanation, not a biological peculiarity of the selected model.

No third model is checked in this block.
