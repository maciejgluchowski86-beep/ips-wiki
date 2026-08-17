---
method_id: stochastic-localization-ising-glauber-gap
title: Stochastic localization for Ising Glauber spectral gaps
category: functional-inequality
targets:
  - spectral-gap
  - mixing
model_scope: Finite Ising models with arbitrary external field and interaction matrix of operator norm below one
source_status: primary-checked
primary_source: Ronen Eldan, Frederic Koehler and Ofer Zeitouni, A Spectral Condition for Spectral Gap: Fast Mixing in High-Temperature Ising Models, Probability Theory and Related Fields 182 (2022), 1035--1051.
primary_pinpoint: Theorem 1; Lemmas 8--9; Section 3 and Theorem 11; Section 4 for the needle decomposition
primary_url: https://doi.org/10.1007/s00440-021-01085-x
application_source: Ronen Eldan, Frederic Koehler and Ofer Zeitouni, A Spectral Condition for Spectral Gap: Fast Mixing in High-Temperature Ising Models, Probability Theory and Related Fields 182 (2022), 1035--1051.
application_pinpoint: Theorem 11 and Section 5, including the Sherrington--Kirkpatrick example
application_url: https://arxiv.org/abs/2007.08200
wiki_candidate: yes
---

# Stochastic localization for Ising Glauber spectral gaps

## Criterion

For an Ising law on \(\{\pm1\}^n\),

\[
\nu(x)\propto
\exp\!\left(\frac12\langle x,Jx\rangle+\langle h,x\rangle\right),
\]

adding a scalar multiple of the identity to \(J\) does not change the law, so Eldan--Koehler--Zeitouni reduce to \(J\succeq0\). Their Theorem 1 assumes

\[
0\preceq J\prec I
\]

and proves a Poincare inequality for the **heat-bath Glauber Dirichlet form**

\[
\mathcal E_\nu(\varphi,\varphi)
 =\mathbb E_\nu\sum_{i=1}^n
 \bigl(\mathbb E_\nu[\varphi(X)\mid X_{\sim i}]-\varphi(X)\bigr)^2.
\]

In the paper's continuous-time normalization this gives spectral gap at least

\[
1-\|J\|_{\mathrm{op}}.
\]

Equivalently, for the usual discrete-time Glauber chain that updates one uniformly chosen coordinate per step, the gap is at least \((1-\|J\|_{\mathrm{op}})/n\). Section 3 and Theorem 11 turn this spectral estimate into a polynomial worst-case mixing bound.

The striking feature is the hypothesis: it controls the **operator norm** of the interaction, not a Dobrushin row sum. Dense high-temperature models can therefore satisfy the criterion even when the sum of absolute influences incident to a site grows with \(n\).

## Mechanism

The proof constructs a stochastic localization flow \((\nu_t,J_t)\) that progressively removes directions from the positive semidefinite interaction matrix while preserving the original measure as the barycenter of the random localized measures. The interaction evolves according to a matrix-valued stochastic differential equation until the stopping time at which \(J_t\) has rank at most one.

Two monotonicity properties make the flow a coercivity machine. The variance of a fixed test function is essentially preserved in expectation along the localization, while Lemma 9 shows that the Glauber Dirichlet form is a **supermartingale**. At the terminal time only a rank-one Ising interaction remains. Lemma 8 proves the required sharp Poincare inequality for that rank-one model. Averaging backward through the localization flow transfers the terminal inequality to the original high-dimensional Ising law.

Section 4 packages the same construction as a needle decomposition: the original Ising measure is represented as a mixture of rank-one Ising measures. The dynamically controlled Dirichlet form is what makes this decomposition useful for the *actual heat-bath Glauber chain*, rather than merely for an abstract Euclidean-gradient inequality.

This interface is distinct from spectral independence. Spectral independence bounds eigenvalues of conditional influence matrices and then invokes a local-to-global expansion theorem. Stochastic localization instead randomizes the external field and continuously reduces the rank of the interaction matrix, proving the functional inequality by transporting it along that random measure-valued path.

## Representative IPS use

Section 5 applies the theorem to dense high-temperature Ising systems, prominently the Sherrington--Kirkpatrick model. For SK interactions the Dobrushin \(\ell^1\) row-sum criterion is useless at constant inverse temperature, whereas the operator norm stays of constant order. After shifting the diagonal to make the interaction positive semidefinite, Theorem 1 gives a nontrivial Glauber gap whenever the shifted operator norm is below one; Theorem 11 yields polynomial-time Glauber mixing in the corresponding high-temperature regime.

The result is finite-volume, but its value for spin-system methodology is that it converts spectral information about a dense interaction matrix directly into the natural single-site heat-bath Poincare inequality.

## Limitations

The operator-norm threshold \(\|J\|_{\mathrm{op}}<1\) is sufficient, not a characterization of the true dynamical high-temperature region. For random spin glasses it leaves a gap between the proven and conjectured thresholds. The theorem is for finite Ising measures and the heat-bath Glauber chain; it does not by itself construct an infinite-volume dynamics or prove uniqueness of a Gibbs state.

The stochastic-localization proof uses the special quadratic structure of an Ising Hamiltonian and a sharp analysis of rank-one terminal models. Extending the same argument to general multispin interactions requires a localization scheme with an equally tractable terminal class. Finally, the spectral-gap estimate gives polynomial mixing but not the optimal \(O(n\log n)\) scale available from later entropy methods in some regimes.

## Sources

- Eldan, Koehler, Zeitouni, *A Spectral Condition for Spectral Gap: Fast Mixing in High-Temperature Ising Models*, Theorem 1 and Lemmas 8--9, https://doi.org/10.1007/s00440-021-01085-x.
- The same paper, Section 3 and Theorem 11 for mixing consequences, Section 4 for the needle decomposition, and Section 5 for examples, https://arxiv.org/abs/2007.08200.
