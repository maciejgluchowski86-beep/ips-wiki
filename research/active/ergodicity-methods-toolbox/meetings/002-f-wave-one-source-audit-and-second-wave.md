# Group meeting 002: F wave one source-audited; analytic wave two opens

Date: 2026-08-17

Professor review of Student F's first six staged toolbox entries, the principal's mechanical-validator report, the correction commit `d895ec5`, and the cited primary-source material.

## Ruling

All six F-wave-one entries are **accepted for later wiki integration**. They stay in the research staging area until the first F/G integration pass, where headings, cross-links, and overlap will be normalized together before anything enters `docs/`.

The six accepted methods are:

1. `poincare-spectral-gap.md`;
2. `log-sobolev-modified-log-sobolev.md`;
3. `dirichlet-form-canonical-path-comparison.md`;
4. `block-dynamics-bisection-variance.md`;
5. `dobrushin-shlosman-spatial-to-dynamical.md`;
6. `east-distinguished-zero-screening.md`.

The principal reports that `validate_entries.py` passes all six. That is a structural check only; the rulings below are the Professor's source audit.

## 1. Source audit

### Poincare / spectral-gap criterion

Accepted. Caputo--Menz--Tetali Section 1.1 gives the heat-bath generator and Dirichlet form, Poincare inequality (1.7), and the equivalent variance decay

$$
\operatorname{Var}_\mu(P_t f)\le e^{-2t/C}\operatorname{Var}_\mu(f).
$$

Cancrini--Martinelli--Roberto--Toninelli Theorem 2.2 identifies simplicity of the zero eigenvalue with $L^2$ convergence, Theorem 3.3 gives a positive-gap finite-scale good-block criterion, and Corollary 3.5 gives the internally-spanned-block specialization. The entry keeps the important limitation that mixing of the reversible KCSM law need not imply uniqueness of all stationary measures.

### Log-Sobolev and modified log-Sobolev

Accepted. Caputo--Menz--Tetali equations (1.8)--(1.10) distinguish classical LSI from mLSI, identify hypercontractivity versus entropy decay, and record

$$
LS(C)\Rightarrow MLS(C/4)\Rightarrow P(C/2).
$$

Proposition 1.1 supports the approximate-tensorization route, and Corollary 2.3 gives the stated $q<2/3$ sufficient condition. Stroock--Zegarlinski's primary article explicitly states the equivalence between Dobrushin--Shlosman mixing and uniform LSI and, through Theorems 3.2 and 3.6, a uniform Glauber relaxation statement.

### Dirichlet-form / canonical-path comparison

Accepted. Diaconis--Saloff-Coste Theorem 2.1 is exactly the path-congestion comparison of Dirichlet forms; Theorem 2.3 is the multicommodity-flow version. Section 3 applies the comparison to finite symmetric exclusion by comparing with Bernoulli--Laplace diffusion; Theorems 3.1 and 3.2 give the corresponding eigenvalue bounds. This is a genuine IPS application, not merely a generic finite-chain example.

### Block dynamics / bisection variance decomposition

Accepted. Cancrini--Martinelli--Roberto--Toninelli Theorem 4.2 is proved by the stated bisection architecture. Equations (4.8)--(4.10) give the exact recursion

$$
\gamma_k\le
\frac{1}{1-\sqrt{\varepsilon_k}}
\left(1+\frac1{s_k}\right)\gamma_{k-1}
$$

and its product iteration. The same paper uses the mechanism for positive gap in East (Theorem 6.1) and FA-1f (Theorem 6.3). The entry correctly presents the convergent-product condition as the reusable core.

### Dobrushin--Shlosman spatial mixing to dynamical relaxation

Accepted after F's `d895ec5` pinpoint correction. Stroock--Zegarlinski's article states directly that, for its finite-range lattice-gas setting, uniform LSI is equivalent to the Dobrushin--Shlosman mixing condition and that Theorems 3.2 and 3.6 characterize the corresponding uniform rate of Glauber convergence. The entry also correctly separates this block/spatial criterion from the elementary one-site Dobrushin influence contraction that belongs in the coupling/influence lane.

### East distinguished-zero screening

Accepted. In Faggionato--Martinelli--Roberto--Toninelli, Definition 8.1 defines the distinguished zero, Remark 8.1 records the one-sided shielding property, and Lemma 8.2 proves that conditional on the distinguished-zero trajectory the region left behind remains exactly at equilibrium. The proof of Theorem 3.5 then uses that screening together with the East Poincare inequality to obtain exponential relaxation of local observables from non-equilibrium Bernoulli initial laws. The entry states explicitly that the spectral gap is an imported input rather than something proved by the distinguished-zero argument itself.

## 2. Deduplication ruling

The repeated use of Caputo--Menz--Tetali is **not** a duplicate-entry problem. The Poincare page records a coercive variance criterion and its spectral-gap consequence; the LSI/mLSI page records entropy/hypercontractive criteria and approximate entropy tensorization. One primary article legitimately contains both. During wiki integration these pages should cross-link rather than duplicate their common heat-bath setup.

There is likewise intentional overlap between the LSI/mLSI page and the Dobrushin--Shlosman page: one is organized by the functional inequality, the other by a static spatial-mixing hypothesis that produces it. Both belong in a toolbox if the bridge is stated once and cross-linked.

## 3. Integration timing

Do not promote these six to `docs/` yet. Wait for G's first wave and perform one joint first-wave taxonomy pass. That pass should remove duplicated preliminaries, choose related-method links, and decide the order of the new `Ergodicity methods` hub before live-wiki admission.

## 4. Student F continuation

F has cleared its first assignment. Assignment 002 is opened immediately to fill analytic gaps rather than deepen the already dense first-wave topics. Its targets are:

- Lu--Yau / martingale conditional-variance recursion;
- spectral independence / local-to-global influence methods;
- block or approximate factorization of entropy as a standalone proof architecture;
- bounded-perturbation / Holley--Stroock transfer of coercive inequalities;
- moving-particle / long-jump comparison for conservative IPS;
- finite-size or finite-volume criteria converting local/boundary mixing estimates into uniform spectral-gap or log-Sobolev bounds.

As before, each completed entry is committed immediately and must be grounded in inspected primary sources with exact pinpoints.

## 5. Current work status

- Student F: active on Assignment 002.
- Student G: still in flight on Assignment 001; do not interrupt or retask it before handoff.
- No live-wiki promotion yet.
