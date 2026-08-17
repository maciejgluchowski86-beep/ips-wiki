# Student G Assignment 010 final report: connected renewal stops at one signed boundary-transmission operator

**Stopping-rule outcome:** `unresolved after substantive work; connected-tail blocker: the exact tail-shift functional can be eliminated, the fresh recentered and scalar insertion branches are individually subcritical, and the only remaining uncontrolled branch is the signed right-boundary transmission Volterra operator (9) below.  No depth-uniform estimate retaining its two-time cancellation was proved.`

## 1. Goal

At

\[
P_*=(a,b,c)=\left(\frac1{1000},\frac1{10},\frac{9999}{10000}\right)
\]

with the fixed filter

\[
\sigma(t)=1-2e^{-4t/125},
\]

prove the connected-renewal tail bound

\[
\sum_{k\ge8}|\lambda_k|<\delta_7
\]

or another all-depth theorem for the same exact recurrence implying `rho_J(P_*)>1`.

I did not prove that theorem.  The block nevertheless narrows the remaining object substantially beyond both F009's growing-mode obstruction and the stopped F013/F014 tail-shift object.

## 2. Summary of mathematical content

### 2.1 The filtered tail-shift functional is not irreducible

Checkpoint `010h-boundary-resolvent-elimination-checkpoint.md` proves the following exact identity.  Let

\[
r=1+b=\frac{11}{10},\qquad
S_N=(rI-L_N)^{-1},\qquad
D_N=(I-L_N)S_N,
\]

\[
\varepsilon=\frac9{10000},\qquad
g_0=\frac{999}{10000},
\]

and let

\[
q_N:=Q_N^\sigma f_N,
\qquad
f_1=Y_1,
\qquad
f_N=Y_Nq_{N-1}.
\]

Then `pi_N(q_N)=0` and the 010g discrepancy functional `delta_N=A_N-pi_N` can be eliminated from the connected coefficient:

\[
\boxed{
 c_{N+1}
 =A_N\!\left[
 -\varepsilon q_N
 +g_0B(I-L_N)(rI-L_N)^{-1}
 P_N(rI-L_N)^{-1}q_N
 \right].
}
\tag{1}
\]

The derivation uses only

\[
\delta_NL_N=-BA_ND_NP_N,
\]

the resolvent equation for `S_Nq_N`, and `pi_N(q_N)=0`.

Consequently the connected coefficient does **not** require a norm bound on the bare stationary discrepancy `delta_N`.  In particular, 010g does not prove equivalence with the stopped zero-frequency tail-shift problem: the discrepancy can be removed algebraically before any estimate is made.

A completely crude consequence is

\[
|c_{N+1}|\le C_*\operatorname{osc}(q_N),
\qquad
C_*=rac{342081}{1718750}\approx0.199029,
\tag{2}
\]

but this loses far too much after multiplication by `z_sigma` and is not a tail theorem.

### 2.2 Recentring isolates the exact branch which blocks iteration

Checkpoint `010i-recentered-boundary-intertwining-checkpoint.md` introduces

\[
X_i:=Y_i+\varepsilon=B\eta_i-c_0,
\qquad
c_0=\frac{999}{1000},
\qquad
B=c_0+g_0.
\]

The fresh coordinate `X_i` is centered under Bernoulli density `10/11`, the exact one-site zero-boundary equilibrium density.

Writing `A_N=-L_N`, `I_N` for embedding from `N-1` sites, and `P_{N-1}` for the old right-boundary coefficient projection, the last-coordinate block gives the exact commutators

\[
A_NI_N=I_NA_{N-1}-BM_{\eta_N}P_{N-1},
\tag{3}
\]

and

\[
\boxed{
A_NM_{X_N}
=M_{X_N}(A_{N-1}+r)
-g_0B M_{\eta_N}P_{N-1}.
}
\tag{4}
\]

Thus a fresh recentered insertion shifts temporal frequency by the fixed amount `r=1.1`; **the only failure of exact shifted intertwining is the old right-boundary projection**.

Duhamel gives the exact raw-insertion identity, best written as

\[
\boxed{
\begin{aligned}
e^{tL_N}M_{Y_N}
={}&e^{-rt}M_{X_N}e^{tL_{N-1}}
-\varepsilon I_Ne^{tL_{N-1}}\\
&+B\int_0^t e^{(t-s)L_N}M_{\eta_N}P_{N-1}
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}\,ds.
\end{aligned}
}
\tag{5}
\]

Let

\[
h(t):=w_*(t)\sigma(t).
\]

The first two branches in (5) are individually subcritical under completely safe absolute-value estimates:

\[
\int_0^\infty |h(t)|e^{-rt}\,dt
\le Z_{\omega+r}=\frac{2425}{2671},
\]

hence

\[
\boxed{
BZ_{\omega+r}
=\frac{1065933}{1068400}
\approx0.997691<1,
}
\tag{6}
\]

while

\[
\boxed{
\varepsilon\int_0^\infty w_*(t)|\sigma(t)|\,dt
\le \varepsilon Z
=\frac9{10000}\frac{19100}{31}
\approx0.55452<1.
}
\tag{7}
\]

These estimates do not combine to a contraction by summation; their role is diagnostic.  They show that neither the fresh frequency-shifted insertion nor the scalar miscentring `Y=X-epsilon` is, by itself, the obstruction.

The same checkpoint also gives the exact positive second-moment identity

\[
\boxed{
\pi_N(Y_N^2f^2)
=A_{N-1}\Bigl[g^2I+(c-g)g_0K_{N-1}\Bigr]f^2,
\qquad
K_{N-1}=r(rI-L_{N-1})^{-1},
}
\tag{8}
\]

with total positive coefficient

\[
g^2+(c-g)g_0=0.09980091.
\]

This makes an `L^2` route plausible only if one can compare the prefix marginal `A_{N-1}` to the stationary Hilbert structure without reintroducing the stopped spatial-memory problem.  I did not obtain such a comparison.

### 2.3 The precise unresolved operator

Integrating the last line of (5) against the fixed signed kernel `h` leaves the operator

\[
\boxed{
\begin{aligned}
\mathcal V_N f
:={}&B\int_0^\infty h(t)
\int_0^t
 e^{(t-s)L_N}M_{\eta_N}P_{N-1}\\
&\hspace{28mm}\times
\bigl(g_0e^{-rs}-\varepsilon\bigr)e^{sL_{N-1}}f
\,ds\,dt.
\end{aligned}
}
\tag{9}
\]

The Assignment-010 blocker is now exactly this boundary-transmission branch on the **actual connected orbit** `f=q_{N-1}`.

This is sharper than the old statements for three reasons.

1. It is not the growing full mode hierarchy: (4)--(5) isolate one boundary projection `P_{N-1}` as the sole non-shifted interaction branch.
2. It is not bare tail shift: equation (1) eliminates `delta_N` exactly.
3. It is genuinely signed and two-time.  The inner coefficient
   \[
   g_0e^{-rs}-\varepsilon
   \]
   changes sign at
   \[
   s=\frac{\log 111}{r},
   \]
   while `h(t)` changes sign at
   \[
   t=\frac{\log2}{\tau}.
   \]
   Taking absolute values before the `s,t` integrations destroys precisely the cancellation which the fixed filter was designed to retain.

A continuation would need a depth-uniform estimate for `mathcal V_N q_{N-1}` (or directly for the boundary quantity `P_NS_Nq_N` in (1)) which retains this cancellation.  I did not prove one.

### 2.4 A natural raw-semigroup repair is rigorously impossible

Checkpoint `010j-component-weight-obstruction-checkpoint.md` tests the most immediate refinement of 010a.  In the exact scaled coefficient variables `x_A=g^{|A|}q_A`, consider

\[
\|f\|_{\theta,\phi}
=\sum_{A\ne\varnothing}
\theta^{|A|}\phi^{\kappa(A)}|x_A|,
\]

where `kappa(A)` is the number of one-dimensional connected components.

If the raw nonconstant coefficient semigroup were uniformly nonexpansive, three families of configurations would force

\[
(c-\alpha)\frac\phi\theta\le c+\omega
\qquad\text{(long blocks)},
\tag{10}
\]

\[
g\theta+\frac c\theta\le c+g+2\omega
\qquad\text{(separated dimers)},
\tag{11}
\]

and

\[
g\theta+\frac{\alpha}{\theta\phi}\le g+\omega
\qquad\text{(separated singletons)},
\tag{12}
\]

with `alpha=1/100`.

Equation (11) implies `theta>99/100`; (10) then makes the left side of (12) strictly larger than `g+omega`.  Hence no `theta,phi>0` work.

So the remaining boundary branch cannot be disposed of by first making the raw semigroup contractive with a degree/component `ell^1` Lyapunov norm and only afterwards applying the fixed filter.  Filter-level cancellation is load-bearing.

## 3. Files to edit

No further student-side mathematical file is required beyond the committed checkpoints and this report.

Professor-side state files which may need a ruling update:

- `research/active/positive-rates-conjecture/state.md`;
- `research/active/positive-rates-conjecture/proof-spine.md`;
- optionally a new meeting note recording the Assignment-010 stop.

Relevant new student files are:

- `010h-boundary-resolvent-elimination-checkpoint.md`;
- `010i-recentered-boundary-intertwining-checkpoint.md`;
- `010j-component-weight-obstruction-checkpoint.md`;
- `010k-boundary-reduction-verifier.py`;
- this report.

## 4. Exact changes requested

If the Professor accepts the stopping-rule outcome, I suggest recording:

1. `(T)` remains unproved and the fixed-filter renewal witness is therefore not promoted to `rho_J(P_*)>1`.
2. The connected problem should **not** be reclassified as equivalent to F013/F014 tail shift: 010h equation (1) eliminates the stationary discrepancy exactly.
3. The exact residual target is the signed boundary-transmission operator (9), or equivalently direct decay of the boundary-resolvent quantity in (1) along the actual connected orbit.
4. The raw one-step coefficient route remains closed even after adding a multiplicative component-count weight, by 010j.
5. Unless a future input supplies a theorem controlling (9) with its sign cancellation intact, Assignment 010 returns the programme to the Meeting-025 `no-credible-route` state.

## 5. Checks to run

1. Existing repaired verifier:
   ```bash
   python research/active/positive-rates-conjecture/students/student-g/010e-terminal-kernel-verifier.py
   ```
   This is already reported by the principal as passing end to end.

2. New scalar verifier:
   ```bash
   python research/active/positive-rates-conjecture/students/student-g/010k-boundary-reduction-verifier.py
   ```
   It checks exactly the parameter identities, (6), the crude constant in (2), and the strict scalar inequalities used in the 010j contradiction.  I also ran the same assertions in the working environment before committing the script.

The all-depth identities (1), (4), and (5) are symbolic operator identities derived from the already verified last-coordinate block; no finite-depth numerical extrapolation is used in this report.

## 6. Suggested `project-state.md` update

`Positive-rates Assignment 010 completed unresolved after substantive work.  The fixed-filter connected renewal remains distinct from the stopped zero-frequency tail-shift problem: G010h eliminates the stationary discrepancy exactly from the connected coefficient.  Recentring Y=X-epsilon gives an exact shifted-frequency intertwining; the fresh shifted and scalar branches are individually subcritical, leaving only a signed right-boundary transmission Volterra operator involving P_N.  G010j proves that a degree/component multiplicative l1 Lyapunov norm cannot make the raw semigroup nonexpansive, so cancellation must occur at the fixed-filter boundary operator itself.  No all-depth estimate for that operator was proved; (26.8) and rho_J(P_*)>1 remain open.  In the absence of new input specifically controlling this signed boundary-transmission branch, return to Meeting 025 no-credible-route.`

## 7. Suggested commit message

`Record G010 unresolved signed boundary-transmission blocker`
