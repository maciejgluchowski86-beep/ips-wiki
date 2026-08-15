---
title: Age-dependent branching and finite-horizon nonexplosion
status: standard fact
audit: current
tags:
  - probability
  - branching process
  - nonexplosion
  - PDE
---

# Age-dependent branching and finite-horizon nonexplosion

A finite-horizon branching representation is a finite product on each sample only if its genealogy contains finitely many births before every finite time. For the Bellman--Harris setting below, strictly positive lifetimes and finite mean offspring exclude finite-time explosion.

## Setting

Start with one particle at time $0$. For every particle sample a pair $(\tau,N)$ such that

$$
\tau>0\quad\text{almost surely},
\qquad
N\in\mathbb N_0,
\qquad
m:=\mathbb E N<\infty.
$$

Assume that the pairs attached to distinct particles are independent and identically distributed, and that within each pair the lifetime $\tau$ is independent of the offspring number $N$. At the end of its lifetime the particle dies and produces $N$ children, which repeat the same rule independently.

The process is **nonexplosive on finite horizons** if only finitely many particles are born before every deterministic $T<\infty$, almost surely.

## Proposition

Under the assumptions above, the process is nonexplosive on every finite horizon.

## Proof

Let $S_n=\tau_1+\cdots+\tau_n$ for independent copies of the lifetime. A generation-$n$ particle can be born by time $T$ only if $S_n\leq T$. Independence of lifetimes from offspring counts gives

$$
\mathbb E[\text{generation-$n$ particles born by }T]
=
m^n\mathbb P(S_n\leq T).
\tag{1}
$$

For $a>0$, Markov's inequality applied to $e^{-aS_n}$ gives

$$
\mathbb P(S_n\leq T)
\leq
e^{aT}\left(\mathbb E e^{-a\tau}\right)^n.
\tag{2}
$$

Since $\tau>0$ almost surely, dominated convergence yields $\mathbb E e^{-a\tau}\to0$ as $a\to\infty$. Choose $a$ so that

$$
m\mathbb E e^{-a\tau}<1.
$$

Summing (1)--(2),

$$
\mathbb E[\text{total births by }T]
\leq
e^{aT}\sum_{n\geq0}
\left(m\mathbb E e^{-a\tau}\right)^n
<\infty.
$$

The total number of births is a nonnegative integer-valued random variable, so finite expectation implies finiteness almost surely.

## Remarks

No deterministic lower bound on $\tau$ is needed; mass arbitrarily close to zero is allowed. Bounded offspring is also unnecessary: finite mean suffices under the independence assumptions stated above.

The proposition is a well-definedness statement, not a moment estimate. A finite random tree can carry a multiplicative functional with infinite first or higher moments. This distinction is essential in [branching-diffusion representations](branching-diffusions-and-duhamel-trees.md) and in the [HLOTW marked branching scheme](marked-branching-diffusion-for-gradient-nonlinearities.md).

**Further reading.** This is the standard Bellman--Harris age-dependent branching framework; branching-diffusion papers such as HLOTW use the same finite-horizon nonexplosion mechanism.
