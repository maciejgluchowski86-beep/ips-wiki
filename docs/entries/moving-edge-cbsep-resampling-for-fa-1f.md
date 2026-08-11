---
title: Moving-edge CBSEP resampling for one-dimensional FA-1f
status: proved here
tags:
  - FA-1f
  - CBSEP
  - chronology
  - graphical construction
  - coarse graining
---

# Moving-edge CBSEP resampling for one-dimensional FA-1f

This entry records an exact local coarse graining of the one-dimensional [FA-1f model](fa-1f-model.md). A complete random sequence of FA updates on an edge is stopped at a local regeneration time. The state at that stopping time has exactly the single-edge heat-bath law of the coalescing-branching simple exclusion process (CBSEP). Thus the CBSEP resampling is obtained only after averaging the local FA chronology; no assertion is made for a deterministic update word.

Use vacancy variables, so that a site in state \(1\) is vacant. Fix \(q\in(0,1)\) and put \(p=1-q\).

## The isolated edge chain

Consider two adjacent sites with occupied exterior boundary condition, and restrict to the nonempty-vacancy states

$$
10,\qquad 01,\qquad 11.
$$

The induced FA chain has the only nontrivial transitions

$$
10\longrightarrow11\quad\text{at rate }q,
\qquad
01\longrightarrow11\quad\text{at rate }q,
$$

and

$$
11\longrightarrow10\quad\text{at rate }p,
\qquad
11\longrightarrow01\quad\text{at rate }p.
\tag{1}
$$

Indeed, from a singleton vacancy only the occupied endpoint is facilitated by the vacancy inside the edge. From \(11\), both endpoints are facilitated by each other.

The stationary law of (1) is

$$
\pi_e(11)=\frac{q}{2-q},
\qquad
\pi_e(10)=\pi_e(01)=\frac{p}{2-q}.
\tag{2}
$$

This is exactly product Bernoulli-\(q\) on the two sites conditioned on the edge containing at least one vacancy, which is the one-edge CBSEP heat-bath law.

## Exact stopping-time resampling

There is a stopping rule that produces (2) exactly from every nonempty initial edge state.

1. If the current state is \(10\) or \(01\), run the FA edge chain until it first reaches \(11\). If the state is already \(11\), skip this step.
2. Toss an independent coin \(C\) with

   $$
   \mathbb P(C=1)=\frac{q}{2-q}.
   $$

   If \(C=1\), stop immediately at \(11\).
3. If \(C=0\), continue the FA edge chain until the first endpoint becomes occupied, and stop there.

Starting from \(11\), the first occupation event occurs at either endpoint with equal probability, because the two relevant proposal processes have the same rate \(p\). Hence the stopped state has probabilities

$$
\frac{q}{2-q},\qquad
\frac12\left(1-\frac{q}{2-q}\right),\qquad
\frac12\left(1-\frac{q}{2-q}\right)
$$

on \(11,10,01\), respectively. The last two probabilities equal \(p/(2-q)\). Thus the stopped state has law \(\pi_e\), independently of the initial nonempty edge state.

The construction averages both update counts and update order. For example, before the transition from a singleton to \(11\), arbitrarily many legal refreshes may leave the occupied endpoint occupied. Likewise, before the first coalescence from \(11\), arbitrarily many vacancy proposals may occur at either endpoint. None of these clocks is exposed in the output kernel.

## A moving edge in the full FA process

The same resampling can be embedded in the unrestricted one-dimensional FA graphical construction without freezing the exterior.

Start from an ordered edge \((X,Y)\) in state \(10\): \(X\) is the tagged vacant endpoint and \(Y\) is occupied. Monitor the rate-\(q\) vacancy-proposal process at \(Y\). Every such proposal is legal because \(X\) is vacant. The first such proposal makes the edge \(11\).

Before this happens, the tagged vacancy at \(X\) can become occupied only if the other neighbor \(Z\) of \(X\), outside the current edge, is vacant. If that occupation occurs first, transfer the tag to \(Z\) and replace the ordered edge \((X,Y)\) by \((Z,X)\). The new edge is again in state \(10\). Restart the same rule. The reflected construction applies when the tagged vacancy is initially the right endpoint.

Therefore the moving edge remains a singleton-vacancy edge until an internal vacancy proposal creates \(11\). At that moment apply the stopping coin and, when required, the first-coalescence step above. Since the two endpoints of \(11\) facilitate each other, exterior vacancies do not alter the rates of the coalescence step.

Let \(\tau_{\mathrm{br}}\) be the time at which the moving edge first reaches \(11\). While \(t<\tau_{\mathrm{br}}\), there is exactly one occupied partner of the tagged vacancy, and its vacancy-proposal clock has rate \(q\). When an exterior occupation of the tagged site moves the edge, the strong Markov property restarts the same rate-\(q\) clock at the new occupied partner. Consequently

$$
\mathbb P(\tau_{\mathrm{br}}>t)=e^{-qt}.
\tag{3}
$$

In particular, the internal branching time is an exact exponential clock of rate \(q\), despite arbitrary exterior FA activity and arbitrary motion of the tagged edge before the branch.

At \(\tau_{\mathrm{br}}\), the stopped output on the final edge has the CBSEP heat-bath law (2), independent of the singleton orientation with which the final attempt began. If the stopping coin requests coalescence, the additional waiting time is exponential of rate \(2p\), and the surviving endpoint is uniform.

## Spatial buffer bound

Let \(N\) be the number of shifts of the moving singleton edge before \(\tau_{\mathrm{br}}\). Every shift is caused by an occupation proposal at the tagged vacancy. Such a proposal has rate \(p\), and it produces a shift only when the exterior neighbor is vacant. The competing branch clock has rate \(q\). Hence, at every stage before the branch, conditional on the past, the probability that the next effective event is a shift rather than the branch is at most

$$
\frac{p}{p+q}=p.
$$

By induction,

$$
\mathbb P(N\ge m)\le p^m,
\qquad m\ge0.
\tag{4}
$$

Thus a complete chronology-averaged local regeneration is spatially local with an exponential tail, uniformly over the exterior FA history.

There is an equally elementary time bound. Let \(\tau_{\mathrm{reg}}\) be the final stopping time of the CBSEP resampling. For any \(s,u\ge0\),

$$
\mathbb P(\tau_{\mathrm{reg}}>s+u)
\le e^{-qs}+e^{-2pu}.
\tag{5}
$$

The second term is needed only when the stopping coin requests a coalescence. Combining (4) and (5), a regeneration can be confined with arbitrarily high probability to a fixed spacetime box whose dimensions depend only on \(q\) and the desired error probability.

## Phase chain

If the independent stopping coin is omitted and one simply alternates between the singleton and double-vacancy phases, the phase itself is an exact two-state continuous-time chain. A singleton moving edge reaches the double-vacancy phase at rate \(q\) by (3). A double-vacancy edge loses one endpoint at total rate \(2p\). Therefore

$$
1\xrightarrow{\ q\ }2,
\qquad
2\xrightarrow{\ 2p\ }1.
\tag{6}
$$

Its stationary double-vacancy probability is \(q/(2-q)\), agreeing with (2). Formula (6) does not make the spatial edge position autonomous: the singleton edge can shift before its branch. It isolates, however, the part of the dynamics that is already independent of the exterior environment after chronology averaging.

## Interpretation

The lemma gives a local chronology-averaging mechanism specific to one-dimensional FA-1f. A tagged vacancy provides a guaranteed facilitator. If activity on the opposite side removes that vacancy before the desired local branch, the tag is not killed: the coarse edge moves to the vacancy that enabled the removal. The next local attempt starts in the same singleton state. Eventually an internal branch occurs at the fixed hazard \(q\), and the complete branch/coalescence excursion produces an exact CBSEP edge resampling.

This is consistent with the standard observation that CBSEP branching and coalescing moves are FA-1f moves and that a CBSEP exclusion move can be composed from one branch and one coalescence. The statement here is stronger at the local level: the CBSEP heat-bath projection itself is realized as a stopped average over the actual FA chronology.

The remaining global problem is to concatenate moving-edge resamplings into a sparse spacetime process of tagged vacancies without conditioning away the unrevealed FA clocks in the regions between tags. The exponential buffer bound (4) shows that this problem can be posed as a finite-range block construction up to an arbitrarily small error; such a construction is not claimed here.
