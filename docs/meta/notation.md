---
title: Notation
---

# Notation

This page records common notation for the public wiki.

| Symbol | Meaning | Default scope |
|---|---|---|
| \(I\) | countable site set | general entries |
| \(G=(I,E_G)\) | graph with site set \(I\) | graph/lattice entries |
| \(N(i)\) | neighbourhood of site \(i\) | local models |
| \(N_*(i)\) | \(N(i)\cup\{i\}\) | local models |
| \(E\) | single-site state space | IPS entries |
| \(\Omega\) | configuration space, usually \(E^I\) | Markov processes |
| \(\eta,\xi\) | configurations | IPS/spin systems |
| \(\eta^i\) | configuration obtained by flipping site \(i\) | spin systems |
| \(\eta^{i,a}\) | configuration obtained by setting site \(i\) to \(a\) | finite-state IPS |
| \(c_i(\eta)\) | flip rate at site \(i\) | spin systems |
| \(c_i^a(\eta)\) | rate of setting site \(i\) to \(a\) | finite-state IPS |
| \(\cL\) | generator | Markov processes |
| \(S(t)\) | Markov semigroup | ergodicity |
| \(\nu\) | invariant measure, when unique or distinguished | ergodicity |
| \(\mu S(t)\) | law at time \(t\) started from law \(\mu\) | ergodicity |

## Spin-system convention

A spin system has two single-site states, usually \(\{0,1\}\). Its default generator is

$$
\cL f(\eta)=\sum_{i\in I} c_i(\eta)\bigl(f(\eta^i)-f(\eta)\bigr).
$$

A process with a larger single-site state space or more general update maps is called an interacting particle system.
