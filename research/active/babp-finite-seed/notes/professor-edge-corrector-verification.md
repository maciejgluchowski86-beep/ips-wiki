# Professor verification: BABP finite-window edge corrector

Date: 2026-08-15

Status: Professor check completed; subsequent fresh hostile audit `audits/001-edge-corrector-audit.md` at commit `d1ef2ca` verified the mathematical core with the corrections recorded below.

## Audit correction

Three phrases in the original Professor note were too strong.

1. Uniform positive drift proves

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v,
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t\le -v
\quad\text{a.s.},
$$

not existence of limiting edge speeds. The phrase “positive edge speed” below should be read only in this lower-asymptotic-velocity sense unless a separate speed-existence theorem is supplied.

2. The exact identification of Sudbury's internal 1999 computation with this `k=8` LP is unverified because the full paper body remained inaccessible. The numerical and methodological calibration is strong evidence, not source-verified identity.

3. The `lambda=1/40` certificate is not yet an improvement of Sudbury's published convergence theorem. It is a verified positive finite-window corrector and ballistic-edge bound below `0.0347`; the convergence bridge remains open.

`BABP-EDGE-001` is now `verified` with this narrower wording in `research/claim-registry.md`.

## 1. Generator convention and edge observable

Use the time-scaled particle convention in which a vacant site becomes occupied at rate `lambda` times its number of occupied nearest neighbours, while an occupied site becomes vacant at rate its number of occupied nearest neighbours.

For a finite nonempty particle set `B`, let

$$
R(B)=\max B.
$$

Fix `k>=1` and encode the first `k` sites behind the right edge by

$$
u_j=\mathbf 1_{\{R-j\in B\}},\qquad j=1,\dots,k,
$$

and the next unresolved bit by

$$
z=\mathbf 1_{\{R-k-1\in B\}}.
$$

For a bounded corrector `phi:{0,1}^k -> R`, define

$$
H(B)=R(B)+\phi(u(B)).
$$

Write

$$
T_+u=(1,u_1,\dots,u_{k-1}),
$$

and, when `u_1=1`,

$$
T_-^zu=(u_2,\dots,u_k,z).
$$

Set `u_0=1`, `u_{k+1}=z`, and

$$
n_j^z(u)=u_{j-1}+u_{j+1}.
$$

A direct event enumeration gives

$$
\begin{aligned}
D_{k,\lambda}(u,z;\phi)
={}&\lambda\bigl[1+\phi(T_+u)-\phi(u)\bigr]\\
&+u_1\bigl[-1+\phi(T_-^zu)-\phi(u)\bigr]\\
&+\sum_{j=1}^k n_j^z(u)\bigl[\lambda(1-u_j)+u_j\bigr]
\bigl[\phi(u^{(j)})-\phi(u)\bigr].
\end{aligned}
$$

I checked the bookkeeping independently:

- the only event increasing `R` is birth at `R+1`, at rate `lambda`;
- the only event decreasing `R` is death of `R`, which occurs at rate `u_1`;
- flips of the `k` recorded sites have exactly the displayed birth/death rates;
- changes at `R-k-1` or farther left do not change `H` at the instant of the event.

Thus the finite linear programme in Student B's note is the exact uniform-drift problem for this observable, not a surrogate.

## 2. Positive drift implies a lower asymptotic edge velocity

If for some `v>0`

$$
D_{k,\lambda}(u,z;\phi)\ge v
$$

for every `u,z`, then

$$
H(B_t)-H(B_0)-\int_0^t \mathcal L H(B_s)\,ds
$$

is a martingale. Only a fixed finite window around the edge can change `H`; for fixed `k,lambda,phi` the jump sizes and the rate of `H`-changing events are uniformly bounded. Hence the martingale has quadratic variation `O(t)` and divided by `t` converges to zero almost surely. Since `phi` is bounded,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t\ge v
$$

almost surely. Reflection gives

$$
\limsup_{t\to\infty}\frac{L(B_t)}t\le -v
$$

almost surely.

This validates the ballistic consequence drawn from an exact positive-drift certificate. It does not prove that either ratio has a limit.

## 3. Independent `k=1` calibration

Let `phi(0)=0`, `phi(1)=a`. The four boundary states give

$$
D(0,0)=\lambda(1+2a),
$$

$$
D(0,1)=\lambda(1+3a),
$$

and

$$
D(1,0)=D(1,1)=\lambda-1-2a.
$$

Uniform strict positivity is possible exactly when

$$
a>-\frac13,
\qquad
 a<-\frac{1-\lambda}{2},
$$

which is equivalent to

$$
\lambda>\frac13.
$$

Thus the one-site corrector recovers the classical `1/3` numerical boundary exactly.

## 4. Independent numerical LP calibration for `k=8`

I independently rewrote the LP from the generator formula above and solved it with a separate `scipy.optimize.linprog` implementation. The maximized minimum drift satisfies numerically

```text
k=8, lambda=0.0346:        v_k(lambda) < 0
k=8, lambda=0.0346195435:  v_k(lambda) approximately 0
k=8, lambda=0.0347:        v_k(lambda) > 0
```

with the zero crossing at approximately

```text
0.0346195435.
```

The same independent implementation gives positive optimum at

```text
k=10, lambda=0.025.
```

The subsequent hostile audit independently rebuilt this LP and refined the crossing to `0.0346195434755...`.

## 5. Historical calibration judgment

The accessible publisher record gives the following facts:

- Mountford's 1993 paper states finite-seed convergence for BABP for parameter `>1/3`;
- Sudbury's 1999 paper is titled *Hunting submartingales in the jumping voter model and the biased annihilating branching process*;
- its abstract states that the finite-seed convergence range is extended from `1/3` to `0.0347` and that bounds on the edge speed are obtained.

The full 1999 proof text was not accessible through the available publisher interface, so I cannot certify that Sudbury literally used the identical `k=8` state encoding or exactly the same LP normalization.

The audit therefore records the historical conclusion as **partial**: the exact `k=1` calibration, numerical `k=8` calibration, paper title, abstract, and contemporaneous finite-boundary submartingale methodology strongly support mechanism-level reconstruction, but literal `k=8` equivalence remains an open provenance question.

## 6. Verified claim boundary

The exact project claim is:

$$
\lambda=\frac1{40},\qquad k=10,
$$

admits a bounded rational corrector with

$$
\min_{u,z}D_{10,1/40}(u,z;\phi)
=\frac{1033}{40000000}>0.
$$

Consequently, for every finite nonempty initial configuration,

$$
\liminf_{t\to\infty}\frac{R(B_t)}t
\ge\frac{1033}{40000000},
\qquad
\limsup_{t\to\infty}\frac{L(B_t)}t
\le-\frac{1033}{40000000}
\quad\text{a.s.}
$$

The principal independently ran the committed exact-arithmetic verifier. The Professor independently checked the generator criterion. The fresh auditor independently rederived the generator, decoded the payload, and verified all `2048` inequalities and the martingale consequence.

This result stands mathematically without resolving the historical provenance question. It is **not yet** a proof of finite-seed convergence at `lambda=1/40` and is **not** a theorem asserting limiting edge-speed existence.

Decisive files:

- `students/student-b/001-threshold-and-dfp.md`;
- `students/student-b/edge-corrector-certificate.py`;
- `audits/001-edge-corrector-audit.md`.
