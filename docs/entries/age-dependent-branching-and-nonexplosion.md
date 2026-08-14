---
title: Age-dependent branching and finite-horizon nonexplosion
status: standard fact
tags:
  - probability
  - branching process
  - nonexplosion
  - PDE
---

# Age-dependent branching and finite-horizon nonexplosion

A branching representation is only a finite product on each sample if its genealogy contains finitely many particles before every finite horizon. Positive lifetimes alone rule out infinitely many births along one fixed lineage, but a branching tree contains exponentially many possible lineages. Finite mean offspring still suffices to exclude finite-time explosion for the age-dependent branching processes used in the PDE constructions here.

**References.** This is the standard Bellman--Harris age-dependent branching setting. The argument below is elementary and is the nonexplosion estimate used implicitly in branching-diffusion constructions such as HLOTW.

## Age-dependent branching process

Start with one particle at time \(0\). Each particle independently receives:

- a lifetime \(\tau>0\) almost surely;
- an offspring number \(N\in\mathbb N_0\) with finite mean
  $$
  m:=\mathbb E N<\infty.
  $$

At the end of its lifetime, the particle dies and produces \(N\) children. The children repeat the same rule independently.

The process is *nonexplosive on finite horizons* if, for every \(T<\infty\), only finitely many particles are born before time \(T\), almost surely.

## Proposition

Assume

$$
\tau>0\quad\text{almost surely},
\qquad
\mathbb E N=m<\infty.
\tag{1}
$$

Then the age-dependent branching process is nonexplosive on every finite horizon.

## Proof

Let \(S_n=\tau_1+\cdots+\tau_n\), where the \(\tau_i\) are independent copies of the lifetime. A particle in generation \(n\) can be born by time \(T\) only if the sum of the \(n\) lifetimes along its ancestral line satisfies

$$
S_n\leq T.
$$

The expected number of generation-\(n\) particles is \(m^n\). By independence of lifetimes and offspring counts, the expected number of generation-\(n\) particles born by time \(T\) is therefore

$$
m^n\mathbb P(S_n\leq T).
\tag{2}
$$

Fix \(a>0\). Markov's inequality applied to \(e^{-aS_n}\) gives

$$
\begin{aligned}
\mathbb P(S_n\leq T)
&=
\mathbb P(e^{-aS_n}\geq e^{-aT})\\
&\leq
 e^{aT}\mathbb E e^{-aS_n}\\
&=
 e^{aT}
\left(\mathbb E e^{-a\tau}\right)^n.
\end{aligned}
\tag{3}
$$

Since \(\tau>0\) almost surely,

$$
\mathbb E e^{-a\tau}
\longrightarrow0
\qquad(a\to\infty)
$$

by dominated convergence. Choose \(a\) so large that

$$
m\mathbb E e^{-a\tau}<1.
\tag{4}
$$

Combining (2)--(4), the expected total number of particles born by time \(T\) is bounded by

$$
\sum_{n\geq0}
 m^n\mathbb P(S_n\leq T)
\leq
 e^{aT}
\sum_{n\geq0}
\left(
 m\mathbb E e^{-a\tau}
\right)^n
<\infty.
\tag{5}
$$

A nonnegative integer-valued random variable with finite expectation is finite almost surely. Hence only finitely many particles are born by time \(T\).

## Remarks

The lifetime distribution may have substantial mass arbitrarily close to zero. No deterministic positive lower bound on lifetimes is required. What matters in the proof is only

$$
\mathbb P(\tau=0)=0,
$$

which makes the Laplace transform \(\mathbb E e^{-a\tau}\) tend to zero as \(a\to\infty\).

Likewise, the offspring number need not be bounded. Finite mean is enough for the estimate above.

## Why this matters for PDE branching trees

The [branching-diffusion construction](branching-diffusions-and-duhamel-trees.md) and the [HLOTW marked branching scheme](marked-branching-diffusion-for-gradient-nonlinearities.md) use positive lifetimes and finite mean offspring. The proposition shows that their finite-horizon random genealogies contain finitely many particles almost surely.

This is only a well-definedness statement. It does not imply that the associated multiplicative functional is integrable. A finite random product can still have infinite first or higher moments, which is the separate issue studied by the coding-tree obstruction results and the random-patch conjecture.