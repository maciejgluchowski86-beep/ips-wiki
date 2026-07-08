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
| \(\mathcal S\) | single-site state space | IPS entries |
| \(\Omega\) | configuration space, usually \(\mathcal S^\Lambda\) | IPS/spin systems |
| \(\eta,\xi\) | configurations | IPS/spin systems |
| \(\eta^i\) | configuration obtained by flipping site \(i\) | spin systems |
| \(\eta^{i,a}\) | configuration obtained by setting site \(i\) to \(a\) | finite-state IPS |
| \(c_i(\eta)\) | flip rate at site \(i\) | spin systems |
| \(c_i^a(\eta)\) | rate of setting site \(i\) to \(a\) | finite-state IPS |
| \(\cL\) | generator | Markov processes |
| \(P_t\) | Markov semigroup or transition kernel | IPS/spin systems |
| \(\nu\) | invariant measure, when unique or distinguished | ergodicity |
| \(\mu P_t\) | law at time \(t\) started from law \(\mu\) | ergodicity |

## Lattice convention

The default index object is a lattice \(\Lambda\), not an abstract site set. A graph description is an alternative way of encoding the neighbourhoods of \(\Lambda\). The neighbour set \(N(i)\) does not contain \(i\), while

$$
N_*(i)=N(i)\cup\{i\}.
$$

## Spin-system convention

A spin system has two single-site states, usually \(\{0,1\}\). Its default generator is

$$
\cL f(\eta)=\sum_{i\in\Lambda} c_i(\eta)\bigl(f(\eta^i)-f(\eta)\bigr).
$$

A process with a larger single-site state space or more general update maps is called an interacting particle system.
