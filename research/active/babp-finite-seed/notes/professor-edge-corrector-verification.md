# Professor verification: BABP finite-window edge corrector

Date: 2026-08-15

Status: Professor-checked for proof-spine use; the new project claim remains `claimed` pending a fresh independent audit.

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

## 2. Positive drift implies positive edge speed

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

almost surely. Reflection gives the analogous strictly negative speed for the left edge.

This validates the consequence drawn from an exact positive-drift certificate.

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

Thus the one-site corrector recovers the classical `1/3` boundary exactly, not approximately.

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

This reproduces Student B's finite-window thresholds without using the committed certificate or Student B's LP code.

## 5. Historical calibration judgment

The accessible publisher record gives the following facts:

- Mountford's 1993 paper states finite-seed convergence for BABP for parameter `>1/3`;
- Sudbury's 1999 paper is titled *Hunting submartingales in the jumping voter model and the biased annihilating branching process*;
- its abstract states that the finite-seed convergence range is extended from `1/3` to `0.0347` and that bounds on the edge speed are obtained.

The full 1999 proof text was not accessible through the available publisher interface, so I cannot certify that Sudbury literally used the identical `k=8` state encoding or exactly the same LP normalization.

Nevertheless, the mechanism identification is strong enough for present research use: the exact BABP right-edge generator criterion reproduces the old `1/3` threshold at `k=1`, and the same finite-window hierarchy reproduces `0.0346195435...` at `k=8`, while the relevant published paper explicitly ties its improvement to hunted submartingales and edge-speed bounds. I therefore accept that the project has located the historical threshold mechanism at the level needed to direct research, while retaining the exact line-by-line historical identification as an audit item.

## 6. Claim boundary

The exact project claim supported by Student B's certificate is:

$$
\lambda=\frac1{40},\qquad k=10,
$$

admits a bounded rational corrector with

$$
\min_{u,z}D_{10,1/40}(u,z;\phi)
=\frac{1033}{40000000}>0.
$$

The principal independently ran the committed exact-arithmetic verifier and reproduced this minimum. The Professor has independently checked the generator criterion and separately solved the LP numerically, obtaining positive feasibility at the same parameter.

This is a strict improvement of the finite-window edge-submartingale/edge-speed certificate below the historical `0.0347` cutoff. It is **not yet** a proof of finite-seed convergence at `lambda=1/40`: the edge-speed-to-local-convergence bridge must still be verified or reproved.

Decisive student files:

- `students/student-b/001-threshold-and-dfp.md`;
- `students/student-b/edge-corrector-certificate.py`.
