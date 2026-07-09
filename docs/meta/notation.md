---
title: Notation
---

# Notation

This page records common notation for the public wiki.

| Symbol | Meaning | Default scope |
|---|---|---|
| \(\Lambda\) | countable lattice | IPS/spin systems |
| \(G=(\Lambda,E_G)\) | graph description of the lattice | graph/lattice entries |
| \(N(i)\) | neighbour set of \(i\), not containing \(i\) | local models |
| \(N_*(i)\) | \(N(i)\cup\{i\}\), neighbours plus the site itself | local models |
| \(i\to j\) | \(j\) is reachable from \(i\) by following neighbour sets | oriented lattices |
| \(\mathcal S\) | single-site state space | IPS entries |
| \(\Omega\) | configuration space, usually \(\mathcal S^\Lambda\) | IPS/spin systems |
| \(\eta,\xi\) | configurations | IPS/spin systems |
| \(\eta^i\) | configuration obtained by flipping site \(i\) | spin systems |
| \(\eta^{i,a}\) | configuration obtained by setting site \(i\) to \(a\) | finite-state IPS |
| \(c_i(\eta)\) | flip rate or constraint at site \(i\) | spin systems/KCSM |
| \(\cL\) | generator | Markov processes |
| \(P_t\) | Markov semigroup or transition kernel | IPS/spin systems |
| \(q\) | density of the KCSM facilitating state \(0\) | KCSM |
| \(p\) | \(1-q\), density of state \(1\) | KCSM |
| \(\mu_q\) | Bernoulli product measure with zero density \(q\) | KCSM |
| \(E_i^q\) | Bernoulli refresh operator at site \(i\) | KCSM |
| \(\mathcal U_i\) | update family at site \(i\) | KCSM |
| \(\chi_A\) | monomial \(\prod_{i\in A}\eta(i)\) | algebra/duality |
| \(\chi_A^\theta\) | theta monomial assigning value \(1\) to state \(1\) | algebra/duality |
| \(\bar\chi_A^\theta\) | theta monomial assigning value \(1\) to state \(0\) | algebra/duality |
| \((A_t,\sigma_t)\) | finite-set dual process with \(\sigma_t\in\{+,-\}\) | duality |
| \(\nu\) | invariant measure, when unique or distinguished | ergodicity |
| \(\mu P_t\) | law at time \(t\) started from law \(\mu\) | ergodicity |

## Subset notation

Use unambiguous subset notation:

$$
A\subseteq B
\quad\text{means subset, possibly equal,}
$$

$$
A\subsetneq B
\quad\text{means strict subset,}
$$

and

$$
A\Subset B
\quad\text{means finite subset in this countable-lattice setting.}
$$

Do not use the bare ambiguous subset command.

## Lattice convention

The default index object is a lattice \(\Lambda\), not an abstract site set. A graph description is an alternative way of encoding the neighbourhoods of \(\Lambda\). The neighbour set \(N(i)\) does not contain \(i\), while

$$
N_*(i)=N(i)\cup\{i\}.
$$

The relation \(i\to j\) means reachability by following neighbour sets: there is a finite chain \(i=i_0,i_1,\ldots,i_n=j\) with \(i_{k+1}\in N(i_k)\). The lattice is oriented when \(i\to j\) and \(i\ne j\) imply not \(j\to i\).

## Spin-system convention

A spin system has two single-site states, usually \(\{0,1\}\). Its default generator is

$$
\cL f(\eta)=\sum_{i\in\Lambda} c_i(\eta)\bigl(f(\eta^i)-f(\eta)\bigr).
$$

A process with a larger single-site state space or more general update maps is called an interacting particle system.

## KCSM convention

For kinetically constrained spin models, \(0\) is the facilitating or vacant state. The parameter \(q\) is the density of zeros and \(p=1-q\) is the density of ones.
