# Programme state

## Direction

Title: positive rates conjecture for simple IPS

Branch: `research/positive-rates-conjecture`

Workspace: `research/active/positive-rates-conjecture/`

Principal ruling: **the scientific target is fixed until the principal changes or stops it.** Proof routes may be closed or redirected; the target does not change.

On `r11=0`, write

$$
a=r_{00},\qquad b=r_{01},\qquad c=r_{10},
$$

with residual chamber

$$
\mathcal R=
\left\{0<a<b,\ \frac12\le c<1,\ c\ge a+b,\ b\ge\sqrt2(1-c)\right\}.
$$

Latest meeting: `meetings/026-dual-renewal-connected-tail-reopens-one-bounded-j-spec-block.md`, `state_narrowed: yes`.

Active work:

- Student G: `students/student-g/assignment-010.md`, one bounded connected dual-renewal tail block at `P_*`.
- Student F: idle; no F016.
- No second proof route is active.

Operational overlap: G's `394b7e3` landed after Meeting 025 because the idle ruling had not yet been relayed. Meeting 026 treats it as new post-stop input, not disregard of the stop.

## Route status

Stopped/abandoned interfaces remain:

- common-uniform global coalescence / zero-frequency disagreement occupation (Meeting 019);
- the current centered predecessor-trail/profile composition based on repeated equilibrium replacement (Meeting 021);
- global path-space TV/KL contraction of the exact trajectory kernel `Q`;
- the current stationary boundary-control Bellman-corrector concatenation implementation (Meeting 024);
- the singular fixed-depth short/long renewal continuation of G009 (Meeting 025).

Consultation 002's `no-credible-route` assessment was operative after Meeting 025. Meeting 026 records one new exception: the exact connected/separator renewal of G009b is mathematically different from the stopped zero-frequency replacement error and clears the bar for one bounded feasibility/certificate block.

## Canonical `J` normalization

For singleton depth `n`, G's exact normalization is

$$
\boxed{
J_n=\frac BgR_n=\frac gBN_n,
}
$$

so `R_n`, `J_n`, and `N_n` have the same exponential growth rate

$$
\rho_J(a,b,c)=\limsup_{n\to\infty}J_n^{1/n}.
$$

`(J-SPEC)` remains open.

## G009 fixed-depth theorem retained

Along

$$
a=\varepsilon,\qquad b=\frac1{10},\qquad 1-c=\frac\varepsilon{10},
$$

G009 proves, for every fixed `n`,

$$
\lim_{\varepsilon\downarrow0}
\frac{I_n(\varepsilon)}{|m_0(\varepsilon)|}
=
\left(\frac{499}{341}\right)^{n-1}.
$$

The base decomposes as

$$
\frac{499}{341}=\frac{10}{11}+\frac{189}{341}>1.
$$

This does not imply fixed-rate `rho_J>1`; the long invariant-reset channel is nonuniform in depth and recreates the stopped spatial reset/tail-shift problem.

## New exact dual-renewal reduction

Fix an admissible `sigma:[0,infty)->[-1,1]` and define

$$
H_N^\sigma=\int_0^\infty w(u)\sigma(u)P_u^N\,du,
\qquad
z_\sigma=\int_0^\infty w(u)\sigma(u)\,du,
$$

$$
\boxed{Q_N^\sigma=H_N^\sigma-z_\sigma\Pi_N.}
$$

Then

$$
Q_N^\sigma\mathbf1=0,
\qquad
\pi_NQ_N^\sigma=0.
$$

For connected coefficients

$$
c_1=m_0,
$$

$$
\boxed{
c_k^\sigma
=\pi_kJ_kQ_{k-1}^\sigma J_{k-1}\cdots Q_1^\sigma J_1,
\qquad k\ge2,
}
$$

the fixed-filter signed witness has the exact ordered-composition expansion. With

$$
a_k=z_\sigma c_k^\sigma,
\qquad
V_n=(-1)^nv_n,
\qquad
\lambda_k=(-1)^ka_k,
$$

one obtains the exact all-depth recurrence

$$
\boxed{
V_n=\sum_{k=1}^n\lambda_kV_{n-k},
\qquad V_0=1.
}
$$

The associated witness satisfies `R_n>=|W_n^sigma|`, so exponential growth of `V_n` proves `rho_J>1`.

## Fixed filter for Assignment 010

At

$$
P_*=(1/1000,1/10,9999/10000),
$$

fix

$$
\boxed{
\sigma(u)=1-2e^{-(4/125)u}.
}
$$

Then

$$
z_\sigma=\frac{114559900}{205809}.
$$

G009b reports, and the Professor independently reconstructed numerically, that

$$
\lambda_1,\ldots,\lambda_5>0,
\qquad
\lambda_6,\lambda_7<0,
$$

and

$$
\sum_{k=1}^7\lambda_k\approx1.047155757329804.
$$

No verifier accompanied `394b7e3`. Assignment 010 must first commit the exact rational verifier and exact

$$
\delta_7:=\sum_{k=1}^7\lambda_k-1>0.
$$

## Active sufficient target

The primary target is

$$
\boxed{
\sum_{k\ge8}|\lambda_k|<\delta_7.
}
\tag{CT}
$$

If `(CT)` holds, then `sum_k lambda_k>1`; the renewal generating function has a singularity inside the unit disk and therefore

$$
\rho_J(P_*)>1.
$$

The load-bearing operator is

$$
\boxed{
\mathcal K_N^\sigma=Q_N^\sigma J_N.
}
$$

The invariant projection is extracted exactly as a renewal separator, so `(CT)` is not the F013/F014 tail-shift approximation problem. However `Q_N^sigma Pi_N=0` is not itself a contraction: slow nonzero modes can remain. Assignment 010 must prove a depth-uniform theorem on the actual connected orbit.

## Anti-circularity / stopping rule

Do not count a longer table of `lambda_k` as progress. Do not optimize `sigma`, posit finite-dimensional mode closure, seek an exact finite-cylinder eigenprofile, or return to bare tail-shift/common-coupling/Bellman searches.

A positive outcome requires a genuine all-depth connected-tail theorem. A substantive negative outcome must identify a structural obstruction sharper than the already known growing mode hierarchy. If Assignment 010 returns only more finite coefficients or a generic request for a better norm, this branch stops and the programme returns to Meeting 025's `no-credible-route` state.

## Unresolved target-level facts

Open:

- `(J-SPEC)`;
- the connected-tail bound `(CT)`;
- one-/two-step tail-shift agreement off the product surface;
- `Gamma_M->0` and general `J_{x,r}->0`;
- common-uniform extinction versus convective survival;
- stationary diameter collapse `D_N(h)->0`;
- full ergodicity in the residual chamber.

## Wiki

Keep the live wiki frozen during research.
