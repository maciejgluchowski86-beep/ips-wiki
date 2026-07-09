---
title: Monomials
status: definition
tags:
  - monomials
  - local functions
  - duality
---

# Monomials

Monomials are local observables on \(\{0,1\}^\Lambda\). They are useful for algebraic manipulations of [spin-system](spin-system.md) generators and later duality constructions.

## Definition

For \(A\Subset\Lambda\), define

$$
\chi_A(\eta)=\prod_{i\in A}\eta(i).
$$

The empty product convention gives

$$
\chi_\varnothing=1.
$$

The function \(\chi_A\) is the indicator that all sites in \(A\) are occupied, meaning equal to \(1\).

## Product identity

Since \(\eta(i)^2=\eta(i)\) for \(\eta(i)\in\{0,1\}\),

$$
\chi_A\chi_B=\chi_{A\cup B}.
$$

In particular, if \(A\subseteq B\), then

$$
\chi_B\le \chi_A.
$$

## Single-site replacement

Let \(a\in\{0,1\}\). If \(i\notin A\), then

$$
\chi_A(\eta^{i,a})=\chi_A(\eta).
$$

If \(i\in A\), then

$$
\chi_A(\eta^{i,a})=a\,\chi_{A\setminus\{i\}}(\eta).
$$

Equivalently,

$$
\chi_A(\eta)=\eta(i)\chi_{A\setminus\{i\}}(\eta)
\qquad\text{for }i\in A.
$$

## Bernoulli refresh identity

For the [Bernoulli refresh operator](bernoulli-refresh-operator.md),

$$
E_i^q\chi_A=
\begin{cases}
\chi_A, & i\notin A,\\
p\chi_{A\setminus\{i\}}, & i\in A,
\end{cases}
$$

where \(p=1-q\). Therefore

$$
(E_i^q-I)\chi_A=
\begin{cases}
0, & i\notin A,\\
p\chi_{A\setminus\{i\}}-\chi_A, & i\in A.
\end{cases}
$$

These identities are often the starting point for duality computations.

## Vacancy indicators

Since the KCSM convention uses \(0\) as the facilitating state, vacancy events are written using products of \(1-\eta(i)\). For \(A\Subset\Lambda\),

$$
\prod_{i\in A}(1-\eta(i))
$$

is the indicator that every site in \(A\) is vacant.
