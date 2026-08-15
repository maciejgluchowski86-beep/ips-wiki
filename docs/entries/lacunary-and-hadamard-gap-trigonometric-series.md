---
title: Lacunary and Hadamard-gap trigonometric series
status: standard fact
audit: current
tags:
  - analysis
  - Fourier analysis
  - trigonometric series
  - lacunary series
  - PDE
---

# Lacunary and Hadamard-gap trigonometric series

A lacunary trigonometric series places its Fourier mass on frequencies that grow rapidly with the index. Such series are useful when one wants to put infinitely many widely separated spatial scales into one fixed function. The basic regularity question is elementary: rapid frequency growth makes derivatives expensive, but sufficiently rapid coefficient decay compensates for every fixed derivative order.

This entry records only the standard deterministic facts needed for that use. It does not use the deeper probabilistic theory of lacunary Fourier series.

**References.** These facts are standard Fourier analysis; see, for example, Antoni Zygmund, *Trigonometric Series*, or Yitzhak Katznelson, *An Introduction to Harmonic Analysis*.

## Trigonometric series on the torus

Write

$$
\mathbb T=\mathbb R/(2\pi\mathbb Z).
$$

Let

$$
1\leq N_1<N_2<\cdots
$$

be integers, let \(b_m\in\mathbb C\), and let \(\theta_m\in\mathbb R\). A typical real trigonometric series is

$$
f(x)
=
\sum_{m=1}^\infty
b_m\cos(N_mx+\theta_m),
\tag{1}
$$

with real coefficients \(b_m\). The complex form

$$
\sum_m a_me^{iN_mx}
$$

is equivalent and is often algebraically simpler.

For distinct positive integers \(N_m\), the modes are orthogonal in \(L^2(\mathbb T)\):

$$
\int_0^{2\pi}
e^{iN_mx}e^{-iN_\ell x}\,dx
=
2\pi\ind(m=\ell).
\tag{2}
$$

Thus a mode at frequency \(N_m\) can be recovered by its Fourier coefficient; widely separated frequencies are not needed for orthogonality itself.

## Lacunary and Hadamard-gap sequences

Terminology varies slightly between sources. In this wiki, a strictly increasing integer sequence \((N_m)\) is called *Hadamard-gap* if there is a number \(q>1\) such that

$$
\frac{N_{m+1}}{N_m}\geq q
\qquad
\text{for every }m.
\tag{3}
$$

A trigonometric series supported on such a sequence is called a *Hadamard-gap series*. The word *lacunary* is used more broadly for a Fourier series with large gaps between successive active frequencies; every Hadamard-gap series is lacunary.

Condition (3) implies exponential separation:

$$
N_m\geq N_1q^{m-1}.
\tag{4}
$$

If one also has an upper exponential bound

$$
N_m\leq Ce^{am},
\tag{5}
$$

then the active frequency at index \(m\) is of exponential order in \(m\). Many constructions use a sequence comparable to \(q^m\), in which case both (4) and (5) hold.

The gap condition is a scale-separation statement. It is logically separate from smoothness: smoothness depends on how the coefficients \(b_m\) compare with the derivative factors \(N_m^k\).

## A sufficient criterion for \(C^r\) regularity

Fix an integer \(r\geq0\). Suppose

$$
\sum_{m=1}^\infty
|b_m|N_m^k
<\infty
\qquad
\text{for every }0\leq k\leq r.
\tag{6}
$$

Then the series (1) defines a function \(f\in C^r(\mathbb T)\), and the derivatives may be taken term by term through order \(r\).

Indeed, the \(k\)-th derivative of the \(m\)-th summand has sup norm at most

$$
|b_m|N_m^k.
$$

Condition (6) and the Weierstrass \(M\)-test therefore give uniform convergence of every derivative series through order \(r\). The standard termwise-differentiation theorem then yields the claim.

In particular, if

$$
\sum_{m=1}^\infty
|b_m|N_m^k
<\infty
\qquad
\text{for every integer }k\geq0,
\tag{7}
$$

then

$$
f\in C^\infty(\mathbb T).
\tag{8}
$$

Condition (7) is only a sufficient criterion, but it is the convenient one for fixed-datum constructions with explicitly chosen coefficients and frequencies.

## Superexponential coefficient decay beats exponential frequencies

Call a positive sequence \((c_m)\) *superexponentially decaying in the index* if

$$
\lim_{m\to\infty}
\frac{-\log c_m}{m}
=\infty.
\tag{9}
$$

Equivalently, for every \(A>0\),

$$
c_m\leq e^{-Am}
$$

for all sufficiently large \(m\).

Suppose the frequencies obey the exponential upper bound (5) and the coefficients satisfy

$$
|b_m|\leq c_m
$$

for a superexponentially decaying sequence \((c_m)\). Then (7) holds, and hence the trigonometric series is \(C^\infty\).

To see this, fix \(k\geq0\). From (5),

$$
|b_m|N_m^k
\leq
C^k c_m e^{akm}.
$$

Choose \(A>ak+1\). For all sufficiently large \(m\), (9) gives

$$
|b_m|N_m^k
\leq
C^k e^{-(A-ak)m}
\leq
C^ke^{-m},
$$

which is summable. Since \(k\) was arbitrary, (7) follows.

Thus one fixed smooth function can contain infinitely many exponentially separated frequencies even when the active frequency at index \(m\) grows like \(e^{am}\), provided its coefficients decay superexponentially in \(m\).

## Factorial decay as a standard example

For every \(\vartheta>0\), the sequence

$$
c_m=(m!)^{-\vartheta}
\tag{10}
$$

is superexponentially decaying in the sense of (9). Stirling's formula gives

$$
\log(m!)
=
m\log m-m+O(\log m),
$$

and therefore

$$
\frac{-\log c_m}{m}
=
\vartheta\frac{\log(m!)}m
=
\vartheta\log m+O(1)
\longrightarrow\infty.
\tag{11}
$$

Consequently, if \(N_m\leq Ce^{am}\), then for every fixed \(k\),

$$
\sum_m(m!)^{-\vartheta}N_m^k<\infty,
$$

by the preceding superexponential-decay argument. The corresponding trigonometric series is therefore \(C^\infty\).

The important quantifier is *for every fixed derivative order \(k\)*. The frequency may grow exponentially with \(m\); factorial or stronger coefficient decay still eventually dominates the exponential factor associated with that fixed derivative order.

## What the Hadamard gap does and does not give

The smoothness argument above uses only the upper growth of \(N_m\) and the decay of \(b_m\). The lower gap (3) supplies a different feature: separation of scales. In particular, if \(N_{m+1}/N_m\geq q>1\), then frequency windows of sufficiently small fixed relative width around the \(N_m\)'s are disjoint. A Fourier multiplier supported in one such window can therefore isolate one active scale without touching the others.

This scale separation is often why Hadamard-gap frequencies are chosen. No advanced lacunary-series theorem is needed for the elementary \(C^\infty\) criterion (7).
