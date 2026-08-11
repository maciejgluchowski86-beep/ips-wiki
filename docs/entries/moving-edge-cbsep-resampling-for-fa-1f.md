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

This entry records exact local coarse grainings of the one-dimensional [FA-1f model](fa-1f-model.md). Complete random sequences of FA updates on an edge are stopped at local regeneration times. The resulting state has exactly the single-edge heat-bath law of the coalescing-branching simple exclusion process (CBSEP). Thus the CBSEP resampling is obtained only after averaging the local FA chronology; no assertion is made for a deterministic update word.

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

## A fixed-edge regeneration brick

The preceding resampling can be made uniform over all three nonempty input states without inspecting the exterior configuration. Split the rate-one clock at each endpoint of an edge \(e=\{x,y\}\) into its independent vacancy-proposal and occupation-proposal processes, of rates \(q\) and \(p\), respectively.

Let \(T_x^q,T_y^q\) be the first vacancy-proposal times at the two endpoints and let

$$
T^p=\min\{T_x^p,T_y^p\}
$$

be the first occupation-proposal time at either endpoint. Define

$$
\mathcal R_e=\left\{\max(T_x^q,T_y^q)<T^p\right\}.
\tag{3}
$$

If the edge is nonempty initially, then on \(\mathcal R_e\) it is in state \(11\) at time \(\max(T_x^q,T_y^q)\), for every initial state in \(\{10,01,11\}\). Indeed, before that time no endpoint receives an occupation proposal, so an initial vacancy cannot disappear. Each vacancy proposal is legal once it is needed because the other endpoint is still vacant.

The event \(\mathcal R_e\) depends only on the proposal clocks at the two endpoints and is independent of the exterior graphical history. Its probability is

$$
\begin{aligned}
\mathbb P(\mathcal R_e)
&=\mathbb E\left[e^{-2p\max(T_x^q,T_y^q)}\right]\\
&=2q\int_0^\infty e^{-(q+2p)t}(1-e^{-qt})\,dt\\
&=\frac{q^2}{2-q}.
\end{aligned}
\tag{4}
$$

After the synchronization to \(11\), apply the independent stopping coin and, when requested, the first-coalescence step from the previous section. The resulting edge state has law \(\pi_e\), independent of the initial nonempty edge state and of the exterior history. Thus \(\mathcal R_e\) is a genuine local regeneration event: a positive-probability set of actual FA chronologies erases all input information on a nonempty edge.

This formulation is useful for spacetime block constructions. Regeneration events on disjoint sets of endpoint clocks are independent, and arbitrary graphical activity outside the two endpoints is left unrevealed.

## A moving edge in the full FA process

The same resampling can be embedded without fixing the spatial edge. Start from an ordered edge \((X,Y)\) in state \(10\): \(X\) is the tagged vacant endpoint and \(Y\) is occupied. Monitor the rate-\(q\) vacancy-proposal process at \(Y\). Every such proposal is legal because \(X\) is vacant. The first such proposal makes the edge \(11\).

Before this happens, the tagged vacancy at \(X\) can become occupied only if the other neighbor \(Z\) of \(X\), outside the current edge, is vacant. If that occupation occurs first, transfer the tag to \(Z\) and replace the ordered edge \((X,Y)\) by \((Z,X)\). The new edge is again in state \(10\). Restart the same rule. The reflected construction applies when the tagged vacancy is initially the right endpoint.

Therefore the moving edge remains a singleton-vacancy edge until an internal vacancy proposal creates \(11\). At that moment apply the stopping coin and, when required, the first-coalescence step above. Since the two endpoints of \(11\) facilitate each other, exterior vacancies do not alter the rates of the coalescence step.

Let \(\tau_{\mathrm{br}}\) be the time at which the moving edge first reaches \(11\). While \(t<\tau_{\mathrm{br}}\), there is exactly one occupied partner of the tagged vacancy, and its vacancy-proposal clock has rate \(q\). When an exterior occupation of the tagged site moves the edge, the strong Markov property restarts the same rate-\(q\) clock at the new occupied partner. Consequently

$$
\mathbb P(\tau_{\mathrm{br}}>t)=e^{-qt}.
\tag{5}
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
\tag{6}
$$

Thus a complete chronology-averaged local regeneration is spatially local with an exponential tail, uniformly over the exterior FA history.

There is an equally elementary time bound. Let \(\tau_{\mathrm{reg}}\) be the final stopping time of the CBSEP resampling. For any \(s,u\ge0\),

$$
\mathbb P(\tau_{\mathrm{reg}}>s+u)
\le e^{-qs}+e^{-2pu}.
\tag{7}
$$

The second term is needed only when the stopping coin requests a coalescence. Combining (6) and (7), a regeneration can be confined with arbitrarily high probability to a fixed spacetime box whose dimensions depend only on \(q\) and the desired error probability.

## Phase chain

If the independent stopping coin is omitted and one simply alternates between the singleton and double-vacancy phases, the phase itself is an exact two-state continuous-time chain. A singleton moving edge reaches the double-vacancy phase at rate \(q\) by (5). A double-vacancy edge loses one endpoint at total rate \(2p\). Therefore

$$
1\xrightarrow{\ q\ }2,
\qquad
2\xrightarrow{\ 2p\ }1.
\tag{8}
$$

Its stationary double-vacancy probability is \(q/(2-q)\), agreeing with (2). Formula (8) does not make the spatial edge position autonomous: the singleton edge can shift before its branch. It isolates, however, the part of the dynamics that is already independent of the exterior environment after chronology averaging.

## Negative-fugacity cancellation after regeneration

The resampling also gives a concrete local cancellation relevant to the Bernoulli-quench sign problem. Put

$$
a=1-\frac{q_0}{q}=\frac{r-p}{q},
\qquad r=1-q_0.
$$

Let \(K\in\{1,2\}\) be the number of vacancies in an edge sampled from \(\pi_e\). Then

$$
\mathbb E_{\pi_e}[a^{K-1}]
=\frac{2p+qa}{2-q}
=\frac{p+r}{2-q}\ge0,
\tag{9}
$$

and the size-biased version is

$$
\mathbb E_{\pi_e}[K a^{K-1}]
=\frac{2p+2qa}{2-q}
=\frac{2r}{2-q}\ge0.
\tag{10}
$$

These inequalities are not coefficientwise assumptions. The powers with opposite signs have already been averaged over the complete local branch/coalescence excursion. In particular, (9)--(10) remain nonnegative throughout the hard range \(a\in[-p/q,0]\).

Equations (9)--(10) do not by themselves identify the global punctured moment in the centered dual. Their role is to show that the local sign obstruction disappears under an explicit stopped FA chronology, rather than under a conjectural positive cone.

## Primal-versus-dual warning

The full-process embedding above is specific to the primal OR-FA graphical construction. Once an edge is in state \(11\), each endpoint has one rate-one site clock and is already facilitated by the other endpoint; an exterior vacancy does not create an additional occupation clock. This is why the first coalescence has total rate exactly \(2p\).

The positive centered set dual has a different graphical mechanism: active source sites ring and overwrite their neighbors. An active site on a two-site dual edge can therefore be deleted by an active source outside the edge, creating additional deletion clocks. Consequently the moving-edge CBSEP resampling does not transfer verbatim to the centered dual. Any use of (9)--(10) in the dual sign problem must first pass through an exact primal/dual regional identity, such as [undoing duality under confined interactions](undoing-duality-under-confined-interactions.md), rather than identifying the two edge processes.

## Interpretation

The lemma gives a local chronology-averaging mechanism specific to one-dimensional FA-1f. A tagged vacancy provides a guaranteed facilitator. If activity on the opposite side removes that vacancy before the desired local branch, the tag is not killed: the coarse edge moves to the vacancy that enabled the removal. The next local attempt starts in the same singleton state. Eventually an internal branch occurs at the fixed hazard \(q\), and the complete branch/coalescence excursion produces an exact CBSEP edge resampling.

This is consistent with the standard observation that CBSEP branching and coalescing moves are FA-1f moves and that a CBSEP exclusion move can be composed from one branch and one coalescence. The statement here is stronger at the local level: the CBSEP heat-bath projection itself is realized as a stopped average over the actual FA chronology.

The remaining global problem is to concatenate local regenerations into a sparse spacetime process without conditioning away the unrevealed FA clocks in the regions between regenerated edges. The fixed-edge event (3) gives input-erasing bricks on predetermined edges; the moving-edge construction gives an exponential spatial buffer when a fixed edge loses its vacancy. A successful global scaffold should combine these two features.
