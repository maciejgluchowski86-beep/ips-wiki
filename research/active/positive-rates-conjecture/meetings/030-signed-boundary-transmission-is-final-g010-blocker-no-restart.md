# Group meeting 030: G010 ends at one signed boundary-transmission operator; no restart

Date: 2026-08-17

Professor review of:

- Meetings 027--029 and their bounded-block / restart rules;
- Student G final report `0a4079e`, `students/student-g/010l-connected-tail-final-report.md`;
- corrected recentered-boundary files through `b7abc5a`;
- reversible left-slice reduction `c444db5`;
- component-weight obstruction `d9c477e`;
- exact scalar verifier `adf50d9`, which the principal reports passes as committed;
- current `state.md` and `proof-spine.md`.

`state_narrowed: yes`.

## Ruling

Assignment 010 is complete **unresolved after substantive work**. The late in-flight response materially sharpens the exact residual object, but it still does **not** clear the Meetings 028--029 restart bar. No G011 is issued. Student G remains idle; Student F remains idle. Consultation 002 / Meeting 025 `no-credible-route` is again the operative proof-architecture assessment.

The fixed-filter renewal witness is neither proved supercritical nor refuted. `(CT)` and `rho_J(P_*)>1` remain open.

## 1. Exact three-branch insertion decomposition accepted

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

put

$$
r=1+b=11/10,
\qquad
\varepsilon=9/10000,
\qquad
X_N=Y_N+\varepsilon,
\qquad
g_0=999/10000.
$$

With `A_N=-L_N`, the recentered fresh insertion satisfies exactly

$$
A_NM_{X_N}
=
M_{X_N}(A_{N-1}+r)
-g_0B M_{\eta_N}P_{N-1}.
\tag{30.1}
$$

Combining the corresponding Duhamel formula with the embedding identity and `Y=X-\varepsilon` gives

$$
\boxed{
\begin{aligned}
e^{tL_N}M_{Y_N}
={}&e^{-rt}M_{X_N}e^{tL_{N-1}}
-\varepsilon I_Ne^{tL_{N-1}}\\
&+B\int_0^t e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}\,ds.
\end{aligned}
}
\tag{30.2}
$$

I checked this algebra directly from the accepted last-coordinate identities. Thus every fresh connected extension splits into exactly three channels:

1. a fresh recentered branch with frequency shift `r`;
2. a scalar miscentring branch of size `epsilon`;
3. one right-boundary transmission branch containing `P_{N-1}`.

For the fixed signed time kernel `h(t)=w_*(t)\sigma(t)`, the first two channels are individually subcritical under safe absolute-value bounds:

$$
\boxed{
BZ_{\omega+r}
=\frac{1065933}{1068400}<1,
}
\tag{30.3}
$$

and

$$
\boxed{
\varepsilon Z
=\frac{1719}{3100}<1.
}
\tag{30.4}
$$

The verifier `010k-boundary-reduction-verifier.py` at `adf50d9` exactly checks these scalar identities and inequalities. They are diagnostic channel bounds; their sum is not a contraction theorem.

## 2. Exact residual operator

After integrating the third line of `(30.2)` against `h`, the only uncontrolled branch in this decomposition is

$$
\boxed{
\begin{aligned}
\mathcal V_N f
:={}&B\int_0^\infty h(t)\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}\\
&\hspace{26mm}\times
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
\end{aligned}
}
\tag{30.5}
$$

For Assignment 010 the needed input is the actual connected orbit. A sufficient continuation theorem would control `\mathcal V_N q_{N-1}` depth-uniformly strongly enough to make the renewal coefficients summable/geometric, or equivalently control the boundary-resolvent quantity already isolated in Meeting 028.

This operator genuinely retains two-time sign cancellation: `g_0e^{-rs}-epsilon` changes sign, and the outer fixed filter `h(t)` also changes sign. Taking absolute values before the two integrations destroys the mechanism presently carrying the remaining margin.

The final reduction therefore strengthens the separation from F013/F014: the stationary discrepancy was already eliminated exactly, and the remaining object is now a specific signed boundary-transmission Volterra operator on one connected orbit, not unrestricted tail-shift TV.

## 3. Raw coefficient repair is ruled out at a broader level

Commit `d9c477e` extends the 010a obstruction. In scaled coefficient variables, the two-parameter norm

$$
\|f\|_{\theta,\phi}
=
\sum_{A\ne\varnothing}
\theta^{|A|}\phi^{\kappa(A)}|x_A|
$$

cannot make the actual nonconstant raw semigroup uniformly nonexpansive for any `theta,phi>0`.

The contradiction comes from the necessary long-block, separated-dimer, and separated-singleton inequalities

$$
(c-\alpha)\frac\phi\theta\le c+\omega,
\tag{30.6}
$$

$$
g\theta+\frac c\theta\le c+g+2\omega,
\tag{30.7}
$$

$$
g\theta+\frac{\alpha}{\theta\phi}\le g+\omega,
\tag{30.8}
$$

with `alpha=1/100`. The dimer inequality forces `theta>99/100`; then `(30.6)` makes the singleton left side exceed `g+omega`. The exact scalar checks are included in `adf50d9`.

So adding a multiplicative component-count weight does not rescue the route by making the raw semigroup contractive before filtering. Cancellation at the fixed-filter/resolvent level remains load-bearing.

## 4. Reversible reference reduction retained but does not reopen

Commit `c444db5` gives an exact orthogonal left-slice decomposition at the frozen-weight reversible reference point `P_0`:

$$
L_{0,N}=L_{0,N-1}\oplus G_{N-1},
$$

and hence for the frozen-reference connected transfer

$$
T_{0,N}=T_{0,N-1}\oplus S_{N-1},
\qquad
S_n=H^\sigma(G_n)J_n.
$$

Thus a bound

$$
\sup_n\|H^\sigma(G_n)J_n\|_{2\to2}<1
$$

would settle the entire frozen-reference transfer norm. The killed family itself has a self-adjoint two-component recursion. This is a useful reduction, but it remains a reference-model statement; even its completion would still require transport through the actual nonreversible boundary defect.

Meeting 029's reversible fresh-insertion Sobolev gain is likewise retained. Neither result supplies the missing actual-`P_*` propagation theorem.

## 5. Stop-rule application

The in-flight response was worth preserving: it replaced a vague `H^1`-transport target by the explicit signed operator `(30.5)` and ruled out one broader raw-semigroup repair. But no depth-uniform estimate retaining the two-time cancellation in `(30.5)` was proved.

Accordingly the restart bar is now sharpened to **new input specifically controlling the signed boundary-transmission operator `(30.5)` on the actual connected orbit**, or a materially different proof architecture. Merely asking for another norm, another reversible comparison, another filter, or further finite coefficients does not clear the bar.

Current status:

- `state_narrowed: yes`;
- Assignment 010 complete unresolved;
- `(J-SPEC)` open;
- `(CT)` open;
- no G011; Student G idle;
- no F016; Student F idle;
- no active proof architecture;
- consultation 002 / Meeting 025 `no-credible-route` operative pending genuinely new principal, external, or literature input.
