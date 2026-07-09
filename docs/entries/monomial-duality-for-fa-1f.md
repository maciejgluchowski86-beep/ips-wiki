---
title: Monomial duality for FA-1f
status: proved here
tags:
  - duality
  - FA-1f
  - monomials
  - KCSM
---

# Monomial duality for FA-1f

This entry specializes [monomial duality for spin systems](monomial-duality-for-spin-systems.md) to the [FA-1f model](fa-1f-model.md) on an arbitrary [lattice](lattice-and-graph.md) with finite neighbour sets. The dual process is a [signed additive set process](signed-additive-set-process.md) on finite subsets of \(\Lambda\).

Let \(q\) be the vacancy density and \(p=1-q\). The hard FA-1f generator can be written in flip form as

$$
\cL f(\eta)
=
\sum_{i\in\Lambda}
\left(1-\chi_{N(i)}(\eta)\right)
\left(q\eta(i)+p(1-\eta(i))\right)
\left(f(\eta^i)-f(\eta)\right).
$$

Equivalently, this is the [Bernoulli refresh](bernoulli-refresh-operator.md) KCSM in which a refresh at \(i\) is legal if at least one neighbour of \(i\) is vacant.

## Hard FA-1f

Assume first that \(N(i)\ne\vn\). In the notation of the general monomial duality entry,

$$
c_i^0(\eta)=p\left(1-\chi_{N(i)}(\eta)\right),
\qquad
c_i^1(\eta)=q\left(1-\chi_{N(i)}(\eta)\right).
$$

Therefore the only nonzero signed coefficients are

$$
a_i^\delta(\vn)=p,
\qquad
a_i^\delta(N(i))=-p,
$$

and

$$
a_i^\beta(\vn)=-1,
\qquad
a_i^\beta(N(i))=1.
$$

Thus the nonzero dual updates at a source site \(i\in A\) are:

$$
D_{i,\vn}Y=\left(A\setminus\{i\},\sigma\right)
\qquad\text{at rate }p,
$$

$$
D_{i,N(i)}Y=\left((A\setminus\{i\})\cup N(i),-\sigma\right)
\qquad\text{at rate }p,
$$

and

$$
B_{i,N(i)}Y=\left(A\cup N(i),\sigma\right)
\qquad\text{at rate }1.
$$

The source-keeping empty update is omitted by the convention \(\beta_i(\vn)=0\). Its signed coefficient is absorbed into the Feynman--Kac potential. For hard FA-1f,

$$
V_i=2p,
\qquad
V(A)=\sum_{i\in A}V_i=2p|A|.
$$

With \(H(A,\sigma,\eta)=\sigma\chi_A(\eta)\), the duality relation is

$$
\cL_\eta H(Y,\eta)
=
\cD H(Y,\eta)+V(A)H(Y,\eta).
$$

If \(N(i)=\vn\), the hard FA-1f constraint at \(i\) is identically zero, so site \(i\) contributes no dual updates and no potential term.

## Soft FA-1f

Let \(\varepsilon_i\in[0,1]\) be a softness parameter and replace the hard constraint by

$$
g_i^\varepsilon(\eta)=1-(1-\varepsilon_i)\chi_{N(i)}(\eta).
$$

The softened generator is

$$
\cL^\varepsilon f(\eta)
=
\sum_{i\in\Lambda}
g_i^\varepsilon(\eta)
\left(q\eta(i)+p(1-\eta(i))\right)
\left(f(\eta^i)-f(\eta)\right).
$$

For \(N(i)\ne\vn\), the nonzero signed coefficients are

$$
a_i^\delta(\vn)=p,
\qquad
a_i^\delta(N(i))=-(1-\varepsilon_i)p,
$$

and

$$
a_i^\beta(\vn)=-1,
\qquad
a_i^\beta(N(i))=1-\varepsilon_i.
$$

Thus the same three update types remain, but the two updates that activate \(N(i)\) have rates multiplied by \(1-\varepsilon_i\):

$$
D_{i,\vn} \text{ has rate }p,
\qquad
D_{i,N(i)} \text{ has rate }(1-\varepsilon_i)p,
\qquad
B_{i,N(i)} \text{ has rate }1-\varepsilon_i.
$$

The site potential is

$$
V_i^\varepsilon
=
2p-\varepsilon_i(1+p),
\qquad
V^\varepsilon(A)=\sum_{i\in A}V_i^\varepsilon.
$$

The hard model is the case \(\varepsilon_i=0\). The fully softened case \(\varepsilon_i=1\) is the unconstrained Bernoulli refresh at site \(i\), for which the only remaining dual update is \(D_{i,\vn}\) at rate \(p\) and \(V_i=-q\).

If \(N(i)=\vn\), then \(g_i^\varepsilon\equiv\varepsilon_i\). In that isolated-site case, the soft model has only \(D_{i,\vn}\) at rate \(\varepsilon_i p\) and has site potential \(V_i^\varepsilon=-\varepsilon_i q\).

## Adding pure deaths

Let

$$
\mathcal N_d^0 f(\eta)
=
\sum_{i\in\Lambda}d_i\eta(i)\left(f(\eta^{i,0})-f(\eta)\right),
\qquad d_i\ge0,
$$

be a pure-death generator. By the [duality noise lemma](duality-noise-lemma.md),

$$
\mathcal N_d^0\chi_A
=-\left(\sum_{i\in A}d_i\right)\chi_A.
$$

Therefore pure deaths do not change the dual update maps. They only subtract \(d_i\) from the site potential. For hard FA-1f with pure deaths and \(N(i)\ne\vn\),

$$
V_i^{0,d}=2p-d_i.
$$

For soft FA-1f with pure deaths and \(N(i)\ne\vn\),

$$
V_i^{\varepsilon,d}
=2p-\varepsilon_i(1+p)-d_i,
\qquad
V^{\varepsilon,d}(A)=\sum_{i\in A}V_i^{\varepsilon,d}.
$$

For an isolated site, the corresponding soft-death potential is \(-\varepsilon_i q-d_i\).

Thus softening changes the dual rates through the factor \(1-\varepsilon_i\), while pure deaths keep the chosen soft-FA dual process fixed and only decrease the Feynman--Kac potential.

## Calculation

The hard FA-1f constraint has the monomial expansion

$$
1-\chi_{N(i)}.
$$

Thus \(c_i^0\) contributes \(p\) at \(\vn\) and \(-p\) at \(N(i)\), while \(c_i^1\) contributes \(q\) at \(\vn\) and \(-q\) at \(N(i)\). Since

$$
a_i^\delta(S)=c_i^0(S),
\qquad
a_i^\beta(S)=-c_i^0(S)-c_i^1(S),
$$

one obtains the hard coefficients. The soft coefficients follow by replacing \(\chi_{N(i)}\) with \((1-\varepsilon_i)\chi_{N(i)}\). The pure-death perturbation adds \(d_i\) to \(c_i^1(\vn)\), hence subtracts \(d_i\) from the source-keeping empty coefficient and only changes the Feynman--Kac potential.
